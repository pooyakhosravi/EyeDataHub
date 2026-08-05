"""Inventory every cataloged Dryad deposit for model-use eligibility review.

This audit records current official metadata and file listings only. It does
not download data files, serialize credentials, or retain temporary download
links. The output supports a separate human review of whether each deposit
contains human or human-derived sample-level inputs, labels, measurements, or
benchmark targets suitable for model training or evaluation.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import requests

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from hub.audit.inventory_unresolved_quantity_deposits import (  # noqa: E402
    _dryad_headers,
    _dryad_inventory,
)


DEFAULT_CATALOG = ROOT / "hub" / "catalog.csv"
DEFAULT_SEARCH = ROOT / "hub" / "audit" / "dryad_search_candidates_2026-08-01.json"
DEFAULT_JSON = ROOT / "hub" / "audit" / "dryad_model_use_inventory_2026-08-02.json"
DEFAULT_CSV = ROOT / "hub" / "audit" / "dryad_model_use_inventory_2026-08-02.csv"


def _load_catalog(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return [
            row
            for row in csv.DictReader(handle)
            if row["loader_backend"] == "dryad"
        ]


def _write_csv(path: Path, records: list[dict[str, Any]]) -> None:
    fields = (
        "record_id",
        "canonical_name",
        "dataset_doi",
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
        "source_checksum_available",
        "source_status",
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for record in records:
            for index, item in enumerate(record.get("files") or [None], start=1):
                writer.writerow(
                    {
                        "record_id": record["record_id"],
                        "canonical_name": record["canonical_name"],
                        "dataset_doi": record["dataset_identifier"],
                        "catalog_deposit_version": record[
                            "catalog_deposit_version"
                        ],
                        "observed_deposit_version": record[
                            "observed_deposit_version"
                        ],
                        "version_matches_catalog": record["version_matches_catalog"],
                        "listing_result": record["listing_result"],
                        "expected_file_count": record["expected_file_count"],
                        "expected_bytes": record["expected_bytes"],
                        "file_index": index if item else "",
                        "file_path": item.get("path") if item else "",
                        "file_bytes": item.get("bytes") if item else "",
                        "mime_type": item.get("mime_type") if item else "",
                        "source_checksum_available": (
                            bool(item.get("source_checksum")) if item else ""
                        ),
                        "source_status": item.get("source_status") if item else "",
                    }
                )


def _payload(
    records: list[dict[str, Any]], *, authentication_source: str
) -> dict[str, Any]:
    return {
        "schema_version": "1.0",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "catalog_record_count": len(records),
        "scope": (
            "Current official file listings for all Dryad-backed catalog records, "
            "for human and model-use eligibility review."
        ),
        "dryad_authentication_source": authentication_source,
        "credential_values_serialized": False,
        "signed_or_download_urls_serialized": False,
        "dataset_files_downloaded": False,
        "records": records,
    }


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(payload, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )
    temporary.replace(path)


def generate(
    *, catalog_path: Path, search_path: Path, json_path: Path, csv_path: Path
) -> dict[str, Any]:
    catalog = _load_catalog(catalog_path)
    search = json.loads(search_path.read_text(encoding="utf-8"))
    source_by_doi = {
        str(item["doi"]).lower(): item for item in search["candidates"]
    }
    session = requests.Session()
    headers, authentication_source = _dryad_headers(session)
    previous_records = []
    if json_path.exists():
        previous_records = json.loads(
            json_path.read_text(encoding="utf-8")
        ).get("records", [])
    completed = {record["record_id"]: record for record in previous_records}
    for index, row in enumerate(sorted(catalog, key=lambda item: item["record_id"]), 1):
        if row["record_id"] in completed:
            print(f"[{index:03d}/{len(catalog)}] {row['record_id']}: checkpointed")
            continue
        doi = row["dataset_doi"].lower()
        source = source_by_doi[doi]
        for attempt in range(5):
            try:
                record = _dryad_inventory(
                    session,
                    record_id=row["record_id"],
                    canonical_name=row["canonical_name"],
                    official_source_url=row["source_landing_page_url"],
                    doi=doi,
                    catalog_version=row["resource_version"],
                    headers=headers,
                )
                break
            except requests.HTTPError as exc:
                status = exc.response.status_code if exc.response is not None else None
                if status == 401:
                    headers, authentication_source = _dryad_headers(session)
                elif status != 429 or attempt == 4:
                    raise
                time.sleep(min(15 * (2**attempt), 60))
        else:
            raise AssertionError("unreachable")
        record["source_title"] = source.get("title")
        record["source_abstract"] = source.get("abstract")
        record["source_methods"] = source.get("methods")
        record["source_usage_notes"] = source.get("usage_notes")
        completed[row["record_id"]] = record
        records = [completed[key] for key in sorted(completed)]
        _write_json(
            json_path,
            _payload(records, authentication_source=authentication_source),
        )
        print(
            f"[{index:03d}/{len(catalog)}] {row['record_id']}: "
            f"{record['expected_file_count']} files"
        )
        time.sleep(0.75)

    records = [completed[key] for key in sorted(completed)]
    if len(records) != len(catalog):
        raise RuntimeError(f"Inventoried {len(records)} of {len(catalog)} records")
    payload = _payload(records, authentication_source=authentication_source)
    _write_json(json_path, payload)
    _write_csv(csv_path, records)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path, default=DEFAULT_CATALOG)
    parser.add_argument("--search", type=Path, default=DEFAULT_SEARCH)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--csv-out", type=Path, default=DEFAULT_CSV)
    args = parser.parse_args()
    payload = generate(
        catalog_path=args.catalog,
        search_path=args.search,
        json_path=args.json_out,
        csv_path=args.csv_out,
    )
    print(f"Inventoried {payload['catalog_record_count']} Dryad records.")


if __name__ == "__main__":
    main()
