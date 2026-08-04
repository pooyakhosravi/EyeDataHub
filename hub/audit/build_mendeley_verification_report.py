"""Build a focused record-level report for the full Mendeley catalog subset."""

from __future__ import annotations

import argparse
import csv
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_INVENTORY = (
    ROOT / "hub" / "audit" / "mendeley_catalog_inventory_2026-08-03.json"
)
DEFAULT_CONTENT = (
    ROOT / "hub" / "audit" / "unresolved_quantity_content_inventory_2026-08-02.json"
)
DEFAULT_JSON = (
    ROOT / "hub" / "audit" / "mendeley_download_verification_2026-08-03.json"
)
DEFAULT_CSV = (
    ROOT / "hub" / "audit" / "mendeley_download_verification_2026-08-03.csv"
)


def _write_csv(path: Path, records: list[dict[str, Any]]) -> None:
    fields = [
        "record_id",
        "canonical_name",
        "official_source_url",
        "dataset_identifier",
        "deposit_version",
        "source_archive_state",
        "verification_result",
        "download_completed",
        "expected_bytes",
        "downloaded_bytes",
        "archive_member_count",
        "archive_uncompressed_bytes",
        "archive_integrity_confirmed",
        "local_archive_sha256",
        "source_checksum_available",
        "temporary_dataset_files_retained",
        "verification_date",
        "notes",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows({field: record.get(field) for field in fields} for record in records)


def build(
    *,
    inventory_path: Path,
    content_path: Path,
    json_path: Path,
    csv_path: Path,
) -> dict[str, Any]:
    inventory = json.loads(inventory_path.read_text(encoding="utf-8"))
    content = json.loads(content_path.read_text(encoding="utf-8"))
    completed = {
        record["record_id"]: record
        for record in content["records"]
        if record.get("provider") == "mendeley"
        and record.get("download_completed") is True
    }
    records: list[dict[str, Any]] = []
    for source in inventory["records"]:
        result = completed.get(source["record_id"])
        if result:
            expected_bytes = int(source["expected_bytes"])
            downloaded_bytes = int(result["acquired_bytes"])
            if expected_bytes != downloaded_bytes:
                raise RuntimeError(
                    f"Archive size mismatch for {source['record_id']}."
                )
            if result.get("archive_integrity_confirmed") is not True:
                raise RuntimeError(
                    f"Archive integrity was not confirmed for {source['record_id']}."
                )
            record = {
                "record_id": source["record_id"],
                "canonical_name": source["canonical_name"],
                "official_source_url": source["official_source_url"],
                "dataset_identifier": source["dataset_identifier"],
                "deposit_version": source["catalog_deposit_version"],
                "source_archive_state": "available",
                "verification_result": "complete_versioned_zip_verified",
                "download_completed": True,
                "expected_bytes": expected_bytes,
                "downloaded_bytes": downloaded_bytes,
                "archive_member_count": result["acquired_file_count"],
                "archive_uncompressed_bytes": result[
                    "archive_uncompressed_bytes"
                ],
                "archive_integrity_confirmed": True,
                "local_archive_sha256": result["local_archive_sha256"],
                "source_checksum_available": False,
                "temporary_dataset_files_retained": False,
                "verification_date": result["inspection_date"],
                "notes": (
                    "The official versioned Download All ZIP matched the expected "
                    "archive size and passed ZIP integrity inspection. The local "
                    "SHA-256 identifies the downloaded archive; Mendeley did not "
                    "provide an independent source checksum through this route."
                ),
            }
        else:
            source_result = source["listing_result"]
            if source_result not in {
                "controlled_access_required",
                "official_archive_preparing",
                "source_blocked",
                "source_blocked_by_author",
            }:
                raise RuntimeError(
                    f"No completed result for ready archive {source['record_id']}."
                )
            if source_result == "controlled_access_required":
                source_state = "controlled_access"
                verification_result = "controlled_access_required"
                notes = (
                    "The official source marks this record as confidential. No "
                    "download is reported because source authorization was not obtained."
                )
            elif source_result in {"source_blocked", "source_blocked_by_author"}:
                source_state = "blocked_by_source"
                verification_result = source_result
                notes = (
                    "The official public snapshot returned HTTP 451 and reports that "
                    "access is blocked at the author's request."
                    if source_result == "source_blocked_by_author"
                    else "The official public snapshot returned HTTP 451."
                )
            else:
                source_state = "preparing"
                verification_result = "source_archive_preparing"
                notes = (
                    "The official page reports that the Download All ZIP is being "
                    "prepared. This is a temporary source state, not a failure."
                )
            record = {
                "record_id": source["record_id"],
                "canonical_name": source["canonical_name"],
                "official_source_url": source["official_source_url"],
                "dataset_identifier": source["dataset_identifier"],
                "deposit_version": source["catalog_deposit_version"],
                "source_archive_state": source_state,
                "verification_result": verification_result,
                "download_completed": False,
                "expected_bytes": None,
                "downloaded_bytes": None,
                "archive_member_count": None,
                "archive_uncompressed_bytes": None,
                "archive_integrity_confirmed": None,
                "local_archive_sha256": None,
                "source_checksum_available": False,
                "temporary_dataset_files_retained": False,
                "verification_date": None,
                "notes": notes,
            }
        records.append(record)

    verified = [record for record in records if record["download_completed"]]
    preparing = [
        record for record in records if record["source_archive_state"] == "preparing"
    ]
    controlled = [
        record
        for record in records
        if record["source_archive_state"] == "controlled_access"
    ]
    source_blocked = [
        record
        for record in records
        if record["source_archive_state"] == "blocked_by_source"
    ]
    payload = {
        "schema_version": "1.0",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "source_inventory": inventory_path.name,
        "source_content_log": content_path.name,
        "catalog_mendeley_record_count": len(records),
        "unique_versioned_deposit_count": len(
            {
                (record["dataset_identifier"], record["deposit_version"])
                for record in records
            }
        ),
        "source_archive_available_count": len(verified),
        "complete_versioned_zip_verified_count": len(verified),
        "source_archive_preparing_count": len(preparing),
        "source_archive_preparing_record_ids": [
            record["record_id"] for record in preparing
        ],
        "controlled_access_required_count": len(controlled),
        "controlled_access_record_ids": [
            record["record_id"] for record in controlled
        ],
        "source_blocked_count": len(source_blocked),
        "source_blocked_record_ids": [
            record["record_id"] for record in source_blocked
        ],
        "downloaded_archive_bytes": sum(
            record["downloaded_bytes"] for record in verified
        ),
        "archive_member_count": sum(
            record["archive_member_count"] for record in verified
        ),
        "archive_uncompressed_bytes": sum(
            record["archive_uncompressed_bytes"] for record in verified
        ),
        "size_mismatch_count": 0,
        "archive_integrity_failure_count": 0,
        "source_checksum_available_count": 0,
        "local_sha256_generated_count": sum(
            bool(record["local_archive_sha256"]) for record in verified
        ),
        "temporary_dataset_files_retained": False,
        "credential_values_serialized": False,
        "signed_or_download_urls_serialized": False,
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
    parser.add_argument("--inventory", type=Path, default=DEFAULT_INVENTORY)
    parser.add_argument("--content", type=Path, default=DEFAULT_CONTENT)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--csv-out", type=Path, default=DEFAULT_CSV)
    args = parser.parse_args()
    payload = build(
        inventory_path=args.inventory,
        content_path=args.content,
        json_path=args.json_out,
        csv_path=args.csv_out,
    )
    print(
        f"Verified {payload['complete_versioned_zip_verified_count']} of "
        f"{payload['source_archive_available_count']} available Mendeley archives; "
        f"{payload['controlled_access_required_count']} requires controlled access "
        f"and {payload['source_blocked_count']} is blocked by the source."
    )


if __name__ == "__main__":
    main()
