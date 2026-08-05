"""Inspect the structure of small Dryad deposits, then remove local copies.

The audit downloads complete current deposits only when their official total is
at or below the configured byte threshold. It records file types and structural
metadata such as table dimensions, never participant-level cell values. Larger
deposits remain listing-only. Every temporary acquisition directory is created
under the repository's ignored ``.audit-work`` directory and is removed after
inspection.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import sys
import tempfile
import time
import zipfile
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from xml.etree import ElementTree
from urllib.parse import quote

import requests


ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from eyedatahub.datasets.download_utils import download_dryad  # noqa: E402
from eyedatahub.utils.credentials import load_credentials  # noqa: E402


DEFAULT_INPUT = ROOT / "hub" / "audit" / "dryad_model_use_inventory_2026-08-02.json"
DEFAULT_OUTPUT = ROOT / "hub" / "audit" / "dryad_model_use_structure_2026-08-02.json"
DEFAULT_CSV = ROOT / "hub" / "audit" / "dryad_model_use_structure_2026-08-02.csv"
DEFAULT_REVIEW = ROOT / "hub" / "audit" / "dryad_model_use_decisions_2026-08-02.json"
WORK_ROOT = ROOT / ".audit-work" / "dryad-model-use"


def _safe_headers(values: list[Any], limit: int = 100) -> list[str]:
    return [str(value).strip()[:200] for value in values[:limit] if str(value).strip()]


def _inspect_delimited(path: Path) -> dict[str, Any]:
    delimiter = "\t" if path.suffix.lower() in {".tsv", ".tab"} else ","
    with path.open(encoding="utf-8-sig", errors="replace", newline="") as handle:
        reader = csv.reader(handle, delimiter=delimiter)
        header = next(reader, [])
        row_count = 1 if header else 0
        max_columns = len(header)
        for row in reader:
            row_count += 1
            max_columns = max(max_columns, len(row))
    return {
        "kind": "delimited_table",
        "rows_including_header": row_count,
        "columns": max_columns,
        "column_names": _safe_headers(header),
    }


def _inspect_xls(path: Path) -> dict[str, Any]:
    try:
        import xlrd
    except ImportError:
        return {"kind": "xls_workbook", "inspection": "xlrd_not_available"}
    workbook = xlrd.open_workbook(path, on_demand=True)
    sheets = []
    for sheet_name in workbook.sheet_names():
        sheet = workbook.sheet_by_name(sheet_name)
        headers = sheet.row_values(0) if sheet.nrows else []
        sheets.append(
            {
                "name": sheet_name,
                "rows": sheet.nrows,
                "columns": sheet.ncols,
                "column_names": _safe_headers(headers),
            }
        )
    workbook.release_resources()
    return {"kind": "xls_workbook", "sheets": sheets}


def _inspect_xlsx(path: Path) -> dict[str, Any]:
    namespace = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
    with zipfile.ZipFile(path) as archive:
        workbook = ElementTree.fromstring(archive.read("xl/workbook.xml"))
        sheet_names = [
            element.attrib.get("name", "")
            for element in workbook.findall(".//m:sheet", namespace)
        ]
        dimensions = []
        sheet_paths = sorted(
            name
            for name in archive.namelist()
            if name.startswith("xl/worksheets/sheet") and name.endswith(".xml")
        )
        for sheet_path in sheet_paths:
            root = ElementTree.fromstring(archive.read(sheet_path))
            dimension = root.find("m:dimension", namespace)
            dimensions.append(dimension.attrib.get("ref") if dimension is not None else None)
    return {
        "kind": "xlsx_workbook",
        "sheet_names": sheet_names,
        "sheet_dimensions": dimensions,
    }


def _inspect_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8", errors="replace"))
    if isinstance(value, dict):
        return {
            "kind": "json",
            "top_level_type": "object",
            "top_level_keys": sorted(str(key) for key in value)[:100],
        }
    if isinstance(value, list):
        return {
            "kind": "json",
            "top_level_type": "array",
            "top_level_items": len(value),
        }
    return {"kind": "json", "top_level_type": type(value).__name__}


def _inspect_zip(path: Path) -> dict[str, Any]:
    with zipfile.ZipFile(path) as archive:
        members = [item for item in archive.infolist() if not item.is_dir()]
    return {
        "kind": "zip_archive",
        "member_count": len(members),
        "member_extensions": dict(
            sorted(Counter(Path(item.filename).suffix.lower() or "[none]" for item in members).items())
        ),
    }


def _inspect_text(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8", errors="replace") as handle:
        line_count = sum(1 for _ in handle)
    return {"kind": "text", "line_count": line_count}


def _inspect_file(path: Path) -> dict[str, Any]:
    suffix = path.suffix.lower()
    try:
        if suffix in {".csv", ".tsv", ".tab"}:
            return _inspect_delimited(path)
        if suffix == ".xls":
            return _inspect_xls(path)
        if suffix == ".xlsx":
            return _inspect_xlsx(path)
        if suffix == ".json":
            return _inspect_json(path)
        if suffix == ".zip":
            return _inspect_zip(path)
        if suffix in {".txt", ".md", ".rtf", ".r", ".m"}:
            return _inspect_text(path)
    except Exception as exc:  # Structural parsing must not abort the audit.
        return {
            "kind": "parse_not_completed",
            "error_type": type(exc).__name__,
        }
    return {"kind": "file_type_confirmed"}


def _fresh_dryad_token() -> str:
    client_id = os.environ.get("DRYAD_CLIENT_ID")
    client_secret = os.environ.get("DRYAD_SECRET")
    if not client_id or not client_secret:
        token = str(os.environ.get("DRYAD_TOKEN") or "").strip()
        if token:
            return token
        raise RuntimeError(
            "Dryad per-file inspection requires DRYAD_TOKEN or both "
            "DRYAD_CLIENT_ID and DRYAD_SECRET."
        )
    response = requests.post(
        "https://datadryad.org/oauth/token",
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
    return token


def _safe_dryad_relative_path(value: str) -> Path:
    normalized = value.replace("\\", "/").lstrip("/")
    parts = [part for part in normalized.split("/") if part not in {"", "."}]
    if not parts or any(part == ".." for part in parts):
        raise RuntimeError(f"Unsafe Dryad file path: {value!r}")
    invalid = re.compile(r'[<>:"|?*\x00-\x1f]')
    safe_parts = []
    for part in parts:
        safe = invalid.sub(lambda match: f"%{ord(match.group(0)):02X}", part)
        while safe.endswith((" ", ".")):
            safe = safe[:-1] + f"%{ord(safe[-1]):02X}"
        safe_parts.append(safe)
    return Path(*safe_parts)


def _download_dryad_per_file(
    record: dict[str, Any],
    destination: Path,
) -> dict[str, str]:
    """Download one current Dryad version through its authenticated file API."""
    base_url = "https://datadryad.org"
    token = _fresh_dryad_token()
    headers = {"Authorization": f"Bearer {token}"}

    def get(url: str, *, stream: bool = False) -> requests.Response:
        nonlocal token, headers
        response = requests.get(
            url,
            headers=headers,
            stream=stream,
            timeout=(20, 60),
        )
        if response.status_code == 401:
            response.close()
            token = _fresh_dryad_token()
            headers = {"Authorization": f"Bearer {token}"}
            response = requests.get(
                url,
                headers=headers,
                stream=stream,
                timeout=(20, 60),
            )
        response.raise_for_status()
        return response

    identifier = str(record["dataset_identifier"])
    identifier = identifier if identifier.startswith("doi:") else f"doi:{identifier}"
    dataset_url = f"{base_url}/api/v2/datasets/{quote(identifier, safe='')}"
    with get(dataset_url) as response:
        version_href = (
            response.json().get("_links", {}).get("stash:version", {}).get("href")
        )
    if not version_href:
        raise RuntimeError(f"Dryad exposed no current version for {identifier[4:]}")
    version_url = version_href if version_href.startswith("http") else base_url + version_href
    with get(version_url) as response:
        version_payload = response.json()
    observed_version = str(version_payload.get("versionNumber") or "")
    expected_version = str(record.get("observed_deposit_version") or "")
    if observed_version and expected_version and observed_version != expected_version:
        raise RuntimeError(
            f"Dryad version changed for {identifier[4:]}: "
            f"expected {expected_version}, observed {observed_version}"
        )
    next_href = (
        version_payload.get("_links", {}).get("stash:files", {}).get("href")
    )
    if not next_href:
        raise RuntimeError(f"Dryad exposed no file listing for {identifier[4:]}")

    files: list[dict[str, Any]] = []
    while next_href:
        files_url = next_href if next_href.startswith("http") else base_url + next_href
        with get(files_url) as response:
            payload = response.json()
        files.extend(payload.get("_embedded", {}).get("stash:files", []))
        next_href = payload.get("_links", {}).get("next", {}).get("href")

    expected = {str(item["path"]): item for item in record.get("files") or []}
    observed = {str(item.get("path") or ""): item for item in files}
    if set(observed) != set(expected):
        raise RuntimeError(
            f"Dryad file listing changed for {identifier[4:]}: "
            f"expected {len(expected)} paths, observed {len(observed)}"
        )

    source_paths_by_local_path: dict[str, str] = {}
    for path_text, source in sorted(observed.items()):
        relative = _safe_dryad_relative_path(path_text)
        local_key = relative.as_posix()
        if local_key in source_paths_by_local_path:
            raise RuntimeError(f"Dryad file-name collision after sanitizing {path_text!r}")
        source_paths_by_local_path[local_key] = path_text
        target = (destination / relative).resolve()
        if destination.resolve() not in target.parents:
            raise RuntimeError(f"Unsafe Dryad destination: {path_text!r}")
        target.parent.mkdir(parents=True, exist_ok=True)
        download_href = (
            source.get("_links", {}).get("stash:download", {}).get("href")
        )
        if not download_href:
            raise RuntimeError(f"Dryad exposed no download route for {path_text!r}")
        download_url = (
            download_href
            if download_href.startswith("http")
            else base_url + download_href
        )
        partial = target.with_name(target.name + ".part")
        with get(download_url, stream=True) as response:
            with partial.open("wb") as handle:
                for chunk in response.iter_content(chunk_size=1024 * 1024):
                    if chunk:
                        handle.write(chunk)
        partial.replace(target)
        expected_size = int(expected[path_text].get("bytes") or 0)
        if expected_size and target.stat().st_size != expected_size:
            raise IOError(
                f"Dryad file size mismatch for {path_text!r}: "
                f"expected {expected_size}, acquired {target.stat().st_size}"
            )
        expected_checksum = str(
            expected[path_text].get("source_checksum") or ""
        ).lower()
        checksum_type = str(
            expected[path_text].get("source_checksum_type") or ""
        ).lower()
        algorithms = {
            "md5": "md5",
            "sha-256": "sha256",
            "sha256": "sha256",
        }
        if expected_checksum and checksum_type in algorithms:
            digest = hashlib.new(algorithms[checksum_type], usedforsecurity=False)
            with target.open("rb") as handle:
                for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                    digest.update(chunk)
            if digest.hexdigest() != expected_checksum:
                raise IOError(f"Dryad source checksum mismatch for {path_text!r}")
    return source_paths_by_local_path


def _record_output(
    record: dict[str, Any],
    *,
    threshold: int,
    token: str | None,
    download_small_deposits: bool,
    prefer_per_file: bool,
) -> dict[str, Any]:
    expected_bytes = int(record.get("expected_bytes") or 0)
    base = {
        "record_id": record["record_id"],
        "dataset_doi": record["dataset_identifier"],
        "source_version": record["observed_deposit_version"],
        "expected_file_count": record["expected_file_count"],
        "expected_bytes": expected_bytes,
        "threshold_bytes": threshold,
        "local_files_retained": False,
        "participant_values_serialized": False,
    }
    if expected_bytes > threshold or not download_small_deposits:
        return {
            **base,
            "inspection_level": "complete_official_file_listing",
            "complete_deposit_downloaded_for_structure_review": False,
            "structure_review_note": (
                "above_configured_download_threshold"
                if expected_bytes > threshold
                else "listing_only_after_repository_rate_limit"
            ),
            "file_extension_counts": dict(
                sorted(
                    Counter(
                        Path(str(item.get("path") or "")).suffix.lower() or "[none]"
                        for item in record.get("files") or []
                    ).items()
                )
            ),
            "files": [],
        }

    WORK_ROOT.mkdir(parents=True, exist_ok=True)
    resolved_work = WORK_ROOT.resolve()
    resolved_root = ROOT.resolve()
    if resolved_root not in resolved_work.parents:
        raise RuntimeError("Dryad audit work directory is outside the repository")
    with tempfile.TemporaryDirectory(prefix="deposit-", dir=resolved_work) as temporary:
        temp_path = Path(temporary).resolve()
        if resolved_work not in temp_path.parents:
            raise RuntimeError("Unsafe Dryad temporary directory")
        source_paths_by_local_path: dict[str, str] = {}
        if prefer_per_file:
            source_paths_by_local_path = _download_dryad_per_file(record, temp_path)
        else:
            download_dryad(
                record["dataset_identifier"],
                temp_path,
                extract=True,
                token=token,
            )
        files = sorted(path for path in temp_path.rglob("*") if path.is_file())
        file_rows = []
        for path in files:
            relative = path.relative_to(temp_path).as_posix()
            file_rows.append(
                {
                    "path": source_paths_by_local_path.get(relative, relative),
                    "bytes": path.stat().st_size,
                    "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                    "structure": _inspect_file(path),
                }
            )
        acquired_bytes = sum(item["bytes"] for item in file_rows)
    return {
        **base,
        "inspection_level": "complete_current_deposit_structurally_inspected",
        "complete_deposit_downloaded_for_structure_review": True,
        "acquired_file_count_after_extraction": len(file_rows),
        "acquired_bytes_after_extraction": acquired_bytes,
        "file_extension_counts": dict(
            sorted(
                Counter(Path(item["path"]).suffix.lower() or "[none]" for item in file_rows).items()
            )
        ),
        "files": file_rows,
    }


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(payload, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )
    temporary.replace(path)


def _write_csv(path: Path, records: list[dict[str, Any]]) -> None:
    fields = (
        "record_id",
        "dataset_doi",
        "source_version",
        "expected_file_count",
        "expected_bytes",
        "inspection_level",
        "complete_deposit_downloaded_for_structure_review",
        "acquired_file_count_after_extraction",
        "acquired_bytes_after_extraction",
        "file_extension_counts_json",
        "local_files_retained",
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for record in records:
            writer.writerow(
                {
                    **{field: record.get(field, "") for field in fields[:-2]},
                    "file_extension_counts_json": json.dumps(
                        record["file_extension_counts"], sort_keys=True
                    ),
                    "local_files_retained": record["local_files_retained"],
                }
            )


def generate(
    *,
    input_path: Path,
    output_path: Path,
    csv_path: Path,
    threshold: int,
    seconds_between_downloads: float,
    rate_limit_backoff_seconds: float,
    max_record_attempts: int,
    download_small_deposits: bool,
    refresh_listing_only: bool,
    retained_only: bool,
    review_path: Path,
    prefer_per_file: bool,
) -> dict[str, Any]:
    load_credentials()
    source = json.loads(input_path.read_text(encoding="utf-8"))
    all_records = source["records"]
    processing_records = all_records
    if retained_only:
        review = json.loads(review_path.read_text(encoding="utf-8"))
        retained_ids = {
            str(record["record_id"])
            for record in review.get("records") or []
            if record.get("decision") == "include_model_resource"
        }
        processing_records = [
            record for record in all_records if record["record_id"] in retained_ids
        ]
        if len(processing_records) != len(retained_ids):
            raise ValueError("Retained Dryad review IDs and inventory IDs differ")
    previous = (
        json.loads(output_path.read_text(encoding="utf-8"))
        if output_path.exists()
        else {}
    )
    completed = {
        record["record_id"]: record for record in previous.get("records", [])
    }
    if refresh_listing_only and download_small_deposits:
        refreshable_ids = {
            record["record_id"]
            for record in processing_records
            if int(record.get("expected_bytes") or 0) <= threshold
        }
        completed = {
            record_id: record
            for record_id, record in completed.items()
            if record_id not in refreshable_ids
            or record.get("complete_deposit_downloaded_for_structure_review")
        }
    token = os.environ.get("DRYAD_TOKEN") or None
    for index, record in enumerate(processing_records, start=1):
        record_id = record["record_id"]
        if record_id in completed:
            print(f"[{index:03d}/{len(processing_records)}] {record_id}: checkpointed")
            continue
        for attempt in range(1, max_record_attempts + 1):
            try:
                completed[record_id] = _record_output(
                    record,
                    threshold=threshold,
                    token=token,
                    download_small_deposits=download_small_deposits,
                    prefer_per_file=prefer_per_file,
                )
                break
            except Exception as exc:
                response = getattr(exc, "response", None)
                status_code = getattr(response, "status_code", None)
                if status_code != 429 or attempt == max_record_attempts:
                    raise
                wait_seconds = rate_limit_backoff_seconds * attempt
                print(
                    f"[{index:03d}/{len(processing_records)}] {record_id}: "
                    f"Dryad rate limit on attempt {attempt}/{max_record_attempts}; "
                    f"waiting {wait_seconds:.0f} seconds before retry"
                )
                time.sleep(wait_seconds)
        records = [completed[key] for key in sorted(completed)]
        payload = {
            "schema_version": "1.0",
            "generated_at_utc": datetime.now(timezone.utc).isoformat(),
            "source_inventory": input_path.name,
            "threshold_bytes": threshold,
            "record_count": len(records),
            "credential_values_serialized": False,
            "signed_or_download_urls_serialized": False,
            "participant_values_serialized": False,
            "temporary_files_removed_after_each_record": True,
            "records": records,
        }
        _write_json(output_path, payload)
        print(
            f"[{index:03d}/{len(processing_records)}] {record_id}: "
            f"{completed[record_id]['inspection_level']}"
        )
        if completed[record_id]["complete_deposit_downloaded_for_structure_review"]:
            time.sleep(seconds_between_downloads)

    records = [completed[key] for key in sorted(completed)]
    payload = {
        "schema_version": "1.0",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "source_inventory": input_path.name,
        "threshold_bytes": threshold,
        "record_count": len(records),
        "credential_values_serialized": False,
        "signed_or_download_urls_serialized": False,
        "participant_values_serialized": False,
        "temporary_files_removed_after_each_record": True,
        "complete_structural_inspections": sum(
            record["complete_deposit_downloaded_for_structure_review"]
            for record in records
        ),
        "listing_only_records": sum(
            not record["complete_deposit_downloaded_for_structure_review"]
            for record in records
        ),
        "records": records,
    }
    _write_json(output_path, payload)
    _write_csv(csv_path, records)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--csv-out", type=Path, default=DEFAULT_CSV)
    parser.add_argument("--max-bytes", type=int, default=50_000_000)
    parser.add_argument("--seconds-between-downloads", type=float, default=5.0)
    parser.add_argument("--rate-limit-backoff-seconds", type=float, default=60.0)
    parser.add_argument("--max-record-attempts", type=int, default=6)
    parser.add_argument(
        "--finish-with-listings-only",
        action="store_true",
        help=(
            "Do not request additional archives; complete unprocessed rows from "
            "their already-reviewed official current-version file listings."
        ),
    )
    parser.add_argument(
        "--refresh-listing-only",
        action="store_true",
        help=(
            "Revisit checkpointed listing-only records that now fall within "
            "the configured download threshold."
        ),
    )
    parser.add_argument(
        "--retained-only",
        action="store_true",
        help="Process only Dryad records retained by the scientific scope review.",
    )
    parser.add_argument("--review", type=Path, default=DEFAULT_REVIEW)
    parser.add_argument(
        "--prefer-per-file",
        action="store_true",
        help=(
            "Use Dryad's authenticated per-file API instead of its assembled "
            "whole-version ZIP."
        ),
    )
    args = parser.parse_args()
    payload = generate(
        input_path=args.input,
        output_path=args.output,
        csv_path=args.csv_out,
        threshold=args.max_bytes,
        seconds_between_downloads=args.seconds_between_downloads,
        rate_limit_backoff_seconds=args.rate_limit_backoff_seconds,
        max_record_attempts=args.max_record_attempts,
        download_small_deposits=not args.finish_with_listings_only,
        refresh_listing_only=args.refresh_listing_only,
        retained_only=args.retained_only,
        review_path=args.review,
        prefer_per_file=args.prefer_per_file,
    )
    print(
        f"Inspected {payload['record_count']} records: "
        f"{payload['complete_structural_inspections']} complete small deposits, "
        f"{payload['listing_only_records']} listing-only records."
    )


if __name__ == "__main__":
    main()
