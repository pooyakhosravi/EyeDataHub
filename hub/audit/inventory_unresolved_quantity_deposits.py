"""Inventory official files for records without a resolved primary quantity.

The inventory is a metadata and file-listing audit. It never serializes bearer
tokens or short-lived download URLs, and it does not download dataset files.
Dryad and Mendeley Data versions are compared with the exact versions recorded
in the catalog so later source changes are visible rather than silently folded
into the analyzed snapshot.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import quote, urljoin

import requests

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from eyedatahub.datasets.registry import REGISTRY  # noqa: E402
from eyedatahub.utils.credentials import load_credentials  # noqa: E402


API_ROOT = "https://datadryad.org"
DRYAD_TEST_ENDPOINT = f"{API_ROOT}/api/v2/test"
DRYAD_TOKEN_ENDPOINT = f"{API_ROOT}/oauth/token"
DEFAULT_INPUT = ROOT / "hub" / "audit" / "resource_quantity_unresolved_2026-08-02.csv"
DEFAULT_JSON = ROOT / "hub" / "audit" / "unresolved_quantity_deposit_inventory_2026-08-02.json"
DEFAULT_CSV = ROOT / "hub" / "audit" / "unresolved_quantity_deposit_inventory_2026-08-02.csv"


def _get_json(
    session: requests.Session,
    url: str,
    *,
    headers: dict[str, str],
    params: dict[str, Any] | None = None,
) -> requests.Response:
    for attempt in range(5):
        response = session.get(url, headers=headers, params=params, timeout=60)
        if response.status_code != 429 and response.status_code < 500:
            return response
        if attempt == 4:
            return response
        time.sleep(2**attempt)
    raise AssertionError("unreachable")


def _dryad_headers(session: requests.Session) -> tuple[dict[str, str], str]:
    load_credentials()
    token = os.environ.get("DRYAD_TOKEN", "").strip()
    if token:
        headers = {"Authorization": f"Bearer {token}"}
        response = session.get(DRYAD_TEST_ENDPOINT, headers=headers, timeout=30)
        if response.ok:
            return headers, "DRYAD_TOKEN"

    client_id = os.environ.get("DRYAD_CLIENT_ID", "").strip()
    client_secret = os.environ.get("DRYAD_SECRET", "").strip()
    if not client_id or not client_secret:
        raise RuntimeError(
            "Dryad file listings require DRYAD_TOKEN or both "
            "DRYAD_CLIENT_ID and DRYAD_SECRET."
        )
    response = session.post(
        DRYAD_TOKEN_ENDPOINT,
        data={
            "client_id": client_id,
            "client_secret": client_secret,
            "grant_type": "client_credentials",
        },
        headers={"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"},
        timeout=30,
    )
    response.raise_for_status()
    token = str(response.json().get("access_token") or "").strip()
    if not token:
        raise RuntimeError("Dryad returned no access token.")
    return {"Authorization": f"Bearer {token}"}, "client_credentials"


def _dryad_inventory(
    session: requests.Session,
    *,
    record_id: str,
    canonical_name: str,
    official_source_url: str,
    doi: str,
    catalog_version: str | None,
    headers: dict[str, str],
) -> dict[str, Any]:
    identifier = quote(f"doi:{doi}", safe="")
    dataset_response = _get_json(
        session,
        f"{API_ROOT}/api/v2/datasets/{identifier}",
        headers=headers,
    )
    dataset_response.raise_for_status()
    dataset = dataset_response.json()
    version_href = dataset.get("_links", {}).get("stash:version", {}).get("href")
    if not version_href:
        raise RuntimeError("Dryad did not expose the current version link.")

    version_response = _get_json(
        session,
        urljoin(API_ROOT, version_href),
        headers=headers,
    )
    version_response.raise_for_status()
    version = version_response.json()
    observed_version = str(version.get("versionNumber") or "")
    files_href = version.get("_links", {}).get("stash:files", {}).get("href")
    if not files_href:
        raise RuntimeError("Dryad did not expose the current version file listing.")

    files: list[dict[str, Any]] = []
    next_href: str | None = files_href
    while next_href:
        response = _get_json(
            session,
            urljoin(API_ROOT, next_href),
            headers=headers,
        )
        response.raise_for_status()
        payload = response.json()
        for item in payload.get("_embedded", {}).get("stash:files", []):
            files.append(
                {
                    "path": item.get("path"),
                    "bytes": item.get("size"),
                    "mime_type": item.get("mimeType"),
                    "source_checksum_type": item.get("digestType"),
                    "source_checksum": item.get("digest"),
                    "source_status": item.get("status"),
                }
            )
        next_href = payload.get("_links", {}).get("next", {}).get("href")

    expected_bytes = sum(int(item.get("bytes") or 0) for item in files)
    return {
        "record_id": record_id,
        "canonical_name": canonical_name,
        "provider": "dryad",
        "official_source_url": official_source_url,
        "dataset_identifier": doi,
        "catalog_deposit_version": str(catalog_version or ""),
        "observed_deposit_version": observed_version,
        "version_matches_catalog": observed_version == str(catalog_version or ""),
        "listing_result": "official_file_listing_confirmed",
        "expected_file_count": len(files),
        "expected_bytes": expected_bytes,
        "source_checksums_available": sum(
            bool(item.get("source_checksum")) for item in files
        ),
        "files": files,
        "notes": "Official current-version metadata and file listing reviewed.",
    }


MENDELEY_PATTERN = re.compile(
    r"data\.mendeley\.com/datasets/(?P<dataset_id>[A-Za-z0-9]+)/(?P<version>\d+)"
)


def _mendeley_inventory(
    session: requests.Session,
    *,
    record_id: str,
    canonical_name: str,
    official_source_url: str,
    catalog_version: str | None,
) -> dict[str, Any]:
    match = MENDELEY_PATTERN.search(official_source_url)
    if not match:
        raise RuntimeError("Could not parse the Mendeley dataset ID and version.")
    dataset_id = match.group("dataset_id")
    observed_version = match.group("version")
    headers = {"Accept": "application/vnd.mendeley-public-dataset.1+json"}
    token = os.environ.get("MENDELEY_TOKEN", "").strip()
    if token:
        headers["Authorization"] = f"Bearer {token}"

    files: list[dict[str, Any]] = []
    start = 0
    limit = 100
    while True:
        response = session.get(
            f"https://api.data.mendeley.com/datasets/publics/{dataset_id}/files",
            headers=headers,
            params={"version": observed_version, "$start": start, "$limit": limit},
            timeout=60,
        )
        if response.status_code in (401, 403):
            return {
                "record_id": record_id,
                "canonical_name": canonical_name,
                "provider": "mendeley",
                "official_source_url": official_source_url,
                "dataset_identifier": dataset_id,
                "catalog_deposit_version": str(catalog_version or observed_version),
                "observed_deposit_version": observed_version,
                "version_matches_catalog": observed_version
                == str(catalog_version or observed_version),
                "listing_result": "credential_required",
                "expected_file_count": None,
                "expected_bytes": None,
                "source_checksums_available": None,
                "files": [],
                "notes": (
                    "The official Mendeley API requires a configured token for "
                    "this request; this is an access requirement, not a source failure."
                ),
            }
        response.raise_for_status()
        payload = response.json()
        if isinstance(payload, list):
            batch = payload
        else:
            batch = payload.get("results", payload.get("files", []))
        if not isinstance(batch, list):
            raise RuntimeError("Mendeley returned an unexpected file-listing response.")
        for item in batch:
            details = item.get("content_details") or {}
            files.append(
                {
                    "path": item.get("filename") or item.get("name") or item.get("id"),
                    "bytes": item.get("size") or details.get("size"),
                    "mime_type": item.get("content_type") or details.get("content_type"),
                    "source_checksum_type": None,
                    "source_checksum": None,
                    "source_status": None,
                }
            )
        if len(batch) < limit:
            break
        start += len(batch)

    expected_bytes = sum(int(item.get("bytes") or 0) for item in files)
    return {
        "record_id": record_id,
        "canonical_name": canonical_name,
        "provider": "mendeley",
        "official_source_url": official_source_url,
        "dataset_identifier": dataset_id,
        "catalog_deposit_version": str(catalog_version or observed_version),
        "observed_deposit_version": observed_version,
        "version_matches_catalog": observed_version
        == str(catalog_version or observed_version),
        "listing_result": "official_file_listing_confirmed",
        "expected_file_count": len(files),
        "expected_bytes": expected_bytes,
        "source_checksums_available": 0,
        "files": files,
        "notes": "Official version-specific Mendeley file listing reviewed.",
    }


def _write_csv(path: Path, records: list[dict[str, Any]]) -> None:
    fieldnames = [
        "record_id",
        "canonical_name",
        "provider",
        "official_source_url",
        "dataset_identifier",
        "catalog_deposit_version",
        "observed_deposit_version",
        "version_matches_catalog",
        "listing_result",
        "expected_file_count",
        "expected_bytes",
        "file_index",
        "file_path",
        "file_bytes",
        "mime_type",
        "source_checksum_type",
        "source_checksum_available",
        "source_status",
        "notes",
    ]
    rows: list[dict[str, Any]] = []
    for record in records:
        files = record["files"] or [None]
        for index, item in enumerate(files, start=1):
            rows.append(
                {
                    "record_id": record["record_id"],
                    "canonical_name": record["canonical_name"],
                    "provider": record["provider"],
                    "official_source_url": record["official_source_url"],
                    "dataset_identifier": record["dataset_identifier"],
                    "catalog_deposit_version": record["catalog_deposit_version"],
                    "observed_deposit_version": record["observed_deposit_version"],
                    "version_matches_catalog": record["version_matches_catalog"],
                    "listing_result": record["listing_result"],
                    "expected_file_count": record["expected_file_count"],
                    "expected_bytes": record["expected_bytes"],
                    "file_index": index if item else "",
                    "file_path": item.get("path") if item else "",
                    "file_bytes": item.get("bytes") if item else "",
                    "mime_type": item.get("mime_type") if item else "",
                    "source_checksum_type": (
                        item.get("source_checksum_type") if item else ""
                    ),
                    "source_checksum_available": (
                        bool(item.get("source_checksum")) if item else ""
                    ),
                    "source_status": item.get("source_status") if item else "",
                    "notes": record["notes"],
                }
            )
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def generate(input_path: Path, json_path: Path, csv_path: Path) -> dict[str, Any]:
    load_credentials()
    with input_path.open(encoding="utf-8", newline="") as handle:
        unresolved = list(csv.DictReader(handle))
    if not unresolved:
        raise RuntimeError("The unresolved-quantity input contains no records")

    registry = {dataset.info.name: dataset.info for dataset in REGISTRY.list_datasets()}
    session = requests.Session()
    dryad_headers, dryad_authentication_source = _dryad_headers(session)
    records: list[dict[str, Any]] = []
    for index, row in enumerate(unresolved, start=1):
        record_id = row["record_id"]
        info = registry[record_id]
        try:
            if info.download_type == "dryad":
                record = _dryad_inventory(
                    session,
                    record_id=record_id,
                    canonical_name=info.full_name,
                    official_source_url=info.source_landing_page_url or info.download_url,
                    doi=info.dataset_doi or "",
                    catalog_version=info.resource_version,
                    headers=dryad_headers,
                )
            elif info.download_type == "mendeley":
                record = _mendeley_inventory(
                    session,
                    record_id=record_id,
                    canonical_name=info.full_name,
                    official_source_url=info.source_landing_page_url or info.download_url,
                    catalog_version=info.resource_version,
                )
            else:
                raise RuntimeError(
                    f"No inventory implementation for backend {info.download_type!r}."
                )
        except requests.RequestException as exc:
            response = getattr(exc, "response", None)
            status_code = getattr(response, "status_code", None)
            record = {
                "record_id": record_id,
                "canonical_name": info.full_name,
                "provider": info.download_type,
                "official_source_url": info.source_landing_page_url or info.download_url,
                "dataset_identifier": info.dataset_doi or "",
                "catalog_deposit_version": str(info.resource_version or ""),
                "observed_deposit_version": None,
                "version_matches_catalog": None,
                "listing_result": "request_not_completed",
                "expected_file_count": None,
                "expected_bytes": None,
                "source_checksums_available": None,
                "files": [],
                "notes": f"Official API request did not complete (HTTP {status_code}).",
            }
        records.append(record)
        print(
            f"[{index:02d}/{len(unresolved)}] {record_id}: "
            f"{record['listing_result']}"
        )

    confirmed = [
        record
        for record in records
        if record["listing_result"] == "official_file_listing_confirmed"
    ]
    payload = {
        "schema_version": "1.0",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "input": input_path.name,
        "record_count": len(records),
        "providers": {
            "dryad": sum(record["provider"] == "dryad" for record in records),
            "mendeley": sum(record["provider"] == "mendeley" for record in records),
        },
        "listing_results": {
            result: sum(record["listing_result"] == result for record in records)
            for result in sorted({record["listing_result"] for record in records})
        },
        "confirmed_expected_file_count": sum(
            int(record["expected_file_count"] or 0) for record in confirmed
        ),
        "confirmed_expected_bytes": sum(
            int(record["expected_bytes"] or 0) for record in confirmed
        ),
        "dryad_authentication_source": dryad_authentication_source,
        "credential_values_serialized": False,
        "signed_or_download_urls_serialized": False,
        "dataset_files_downloaded": False,
        "records": records,
    }
    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(
        json.dumps(payload, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )
    _write_csv(csv_path, records)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--csv-out", type=Path, default=DEFAULT_CSV)
    args = parser.parse_args()
    payload = generate(args.input, args.json_out, args.csv_out)
    print(
        f"Wrote {payload['record_count']} record inventories; "
        f"{payload['listing_results']}."
    )


if __name__ == "__main__":
    main()
