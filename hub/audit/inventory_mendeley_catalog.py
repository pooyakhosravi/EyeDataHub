"""Inventory the official versioned archive route for every Mendeley record."""

from __future__ import annotations

import argparse
import csv
import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from hub.audit.inventory_unresolved_quantity_deposits import (  # noqa: E402
    MENDELEY_PATTERN,
    _mendeley_browser_archive_size,
    _mendeley_browser_page_metadata,
)


DEFAULT_CATALOG = ROOT / "hub" / "catalog.json"
DEFAULT_REUSE = (
    ROOT / "hub" / "audit" / "unresolved_quantity_deposit_inventory_2026-08-02.json"
)
DEFAULT_JSON = ROOT / "hub" / "audit" / "mendeley_catalog_inventory_2026-08-03.json"
DEFAULT_CSV = ROOT / "hub" / "audit" / "mendeley_catalog_inventory_2026-08-03.csv"


def _source_url(record: dict[str, Any]) -> str:
    for field in ("source_landing_page_url", "download_url"):
        value = str(record.get(field) or "")
        if "data.mendeley.com/datasets/" in value:
            return value
    return ""


def _normalized_record(
    catalog_record: dict[str, Any],
    source_record: dict[str, Any],
) -> dict[str, Any]:
    source_url = _source_url(catalog_record)
    match = MENDELEY_PATTERN.search(source_url)
    if not match:
        raise RuntimeError("Could not parse the cataloged Mendeley URL.")
    version = match.group("version") or str(
        catalog_record.get("resource_version") or ""
    )
    return {
        **source_record,
        "record_id": catalog_record["name"],
        "canonical_name": catalog_record["full_name"],
        "provider": "mendeley",
        "official_source_url": source_url,
        "dataset_identifier": match.group("dataset_id"),
        "catalog_deposit_version": version
        or str(source_record.get("catalog_deposit_version") or ""),
        "files": [],
    }


def _public_snapshot_state(dataset_id: str, version: str) -> dict[str, Any]:
    """Return public access flags without retaining response headers or URLs."""
    curl = shutil.which("curl.exe") or shutil.which("curl")
    if not curl:
        raise RuntimeError("Native curl is required for Mendeley source review.")
    url = (
        "https://data.mendeley.com/public-api/datasets/"
        f"{dataset_id}/snapshot/{version}"
    )
    result = subprocess.run(
        [
            curl,
            "--silent",
            "--show-error",
            "--location",
            "--write-out",
            "\n%{http_code}",
            url,
        ],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=120,
        check=False,
    )
    if result.returncode or "\n" not in result.stdout:
        return {"http_status": None, "is_confidential": None, "blocked_reason": ""}
    body, status = result.stdout.rsplit("\n", 1)
    try:
        payload = json.loads(body)
    except json.JSONDecodeError:
        payload = {}
    return {
        "http_status": int(status) if status.isdigit() else None,
        "is_confidential": payload.get("is_confidential"),
        "blocked_reason": str(payload.get("blocked_reason") or ""),
    }


def _inventory_one(catalog_record: dict[str, Any]) -> dict[str, Any]:
    source_url = _source_url(catalog_record)
    match = MENDELEY_PATTERN.search(source_url)
    if not match:
        raise RuntimeError("Could not parse the cataloged Mendeley URL.")
    dataset_id = match.group("dataset_id")
    catalog_version = match.group("version") or str(
        catalog_record.get("resource_version") or ""
    )
    source_status = "UNKNOWN"
    observed_version = catalog_version
    if not observed_version:
        observed_version, source_status = _mendeley_browser_page_metadata(
            dataset_id=dataset_id
        )
    if not observed_version:
        raise RuntimeError("The official page exposed no deposit version.")
    status_code, archive_bytes = _mendeley_browser_archive_size(
        dataset_id=dataset_id,
        version=observed_version,
    )
    base = {
        "record_id": catalog_record["name"],
        "canonical_name": catalog_record["full_name"],
        "provider": "mendeley",
        "official_source_url": source_url,
        "dataset_identifier": dataset_id,
        "catalog_deposit_version": catalog_version or observed_version,
        "observed_deposit_version": observed_version,
        "version_matches_catalog": observed_version
        == (catalog_version or observed_version),
        "expected_file_count": None,
        "source_checksums_available": 0,
        "files": [],
    }
    if status_code == 206 and archive_bytes is not None:
        return {
            **base,
            "listing_result": "official_archive_route_confirmed",
            "expected_bytes": archive_bytes,
            "notes": (
                "Official version-specific Download All ZIP route confirmed. "
                "Archive contents are recorded in the content-verification log."
            ),
        }
    if source_status == "UNKNOWN":
        _, source_status = _mendeley_browser_page_metadata(
            dataset_id=dataset_id,
            version=observed_version,
        )
    snapshot_state = _public_snapshot_state(dataset_id, observed_version)
    if snapshot_state["is_confidential"] is True:
        return {
            **base,
            "listing_result": "controlled_access_required",
            "expected_bytes": None,
            "notes": (
                "The official public snapshot marks this record as confidential. "
                "Users must complete the source-specific controlled-access process."
            ),
        }
    if snapshot_state["http_status"] == 451:
        author_request = "author" in snapshot_state["blocked_reason"].lower()
        return {
            **base,
            "listing_result": (
                "source_blocked_by_author" if author_request else "source_blocked"
            ),
            "expected_bytes": None,
            "notes": (
                "The official public snapshot returned HTTP 451 and reports that "
                "access is blocked at the author's request."
                if author_request
                else "The official public snapshot returned HTTP 451."
            ),
        }
    if source_status in {"PENDING", "PROCESSING"}:
        return {
            **base,
            "listing_result": "official_archive_preparing",
            "expected_bytes": None,
            "notes": (
                "The official page reports that its Download All ZIP is being "
                "prepared. This is a temporary source state, not a download failure."
            ),
        }
    return {
        **base,
        "listing_result": "official_archive_route_not_confirmed",
        "expected_bytes": None,
        "notes": (
            "The official versioned archive route did not expose an archive size "
            f"during this check (HTTP {status_code}; source state {source_status})."
        ),
    }


def _write_csv(path: Path, records: list[dict[str, Any]]) -> None:
    fields = [
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
        "source_checksums_available",
        "notes",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows({field: record.get(field) for field in fields} for record in records)


def generate(
    *,
    catalog_path: Path,
    reuse_path: Path | None,
    json_path: Path,
    csv_path: Path,
) -> dict[str, Any]:
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    catalog_records = [
        record for record in catalog["records"] if _source_url(record)
    ]
    reused: dict[str, dict[str, Any]] = {}
    if reuse_path and reuse_path.exists():
        reuse_payload = json.loads(reuse_path.read_text(encoding="utf-8"))
        reused = {
            record["record_id"]: record
            for record in reuse_payload["records"]
            if record.get("provider") == "mendeley"
        }

    records: list[dict[str, Any]] = []
    reused_count = 0
    for index, catalog_record in enumerate(catalog_records, start=1):
        record_id = catalog_record["name"]
        if record_id in reused and reused[record_id].get("listing_result") in {
            "official_archive_route_confirmed",
            "official_file_listing_confirmed",
        }:
            record = _normalized_record(catalog_record, reused[record_id])
            reused_count += 1
        else:
            record = _inventory_one(catalog_record)
        records.append(record)
        print(
            f"[{index:03d}/{len(catalog_records)}] {record_id}: "
            f"{record['listing_result']}",
            flush=True,
        )

    result_counts = {
        result: sum(record["listing_result"] == result for record in records)
        for result in sorted({record["listing_result"] for record in records})
    }
    payload = {
        "schema_version": "1.0",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "catalog": catalog_path.name,
        "provider": "mendeley",
        "record_count": len(records),
        "unique_versioned_deposit_count": len(
            {
                (
                    record["dataset_identifier"],
                    record["catalog_deposit_version"],
                )
                for record in records
            }
        ),
        "reused_inventory_record_count": reused_count,
        "newly_checked_inventory_record_count": len(records) - reused_count,
        "listing_results": result_counts,
        "confirmed_archive_bytes": sum(
            int(record.get("expected_bytes") or 0)
            for record in records
            if record["listing_result"] == "official_archive_route_confirmed"
        ),
        "credential_values_serialized": False,
        "signed_or_download_urls_serialized": False,
        "dataset_files_downloaded": False,
        "records": sorted(records, key=lambda record: record["record_id"]),
    }
    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(
        json.dumps(payload, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )
    _write_csv(csv_path, payload["records"])
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path, default=DEFAULT_CATALOG)
    parser.add_argument("--reuse", type=Path, default=DEFAULT_REUSE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--csv-out", type=Path, default=DEFAULT_CSV)
    args = parser.parse_args()
    payload = generate(
        catalog_path=args.catalog,
        reuse_path=args.reuse,
        json_path=args.json_out,
        csv_path=args.csv_out,
    )
    print(
        f"Inventoried {payload['record_count']} Mendeley records: "
        f"{payload['listing_results']}."
    )


if __name__ == "__main__":
    main()
