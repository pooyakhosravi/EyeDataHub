"""Create a public, path-free view of the catalog-wide acquisition audit."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


WINDOWS_ABSOLUTE_PATH = re.compile(r"[A-Za-z]:[\\/]")


def _public_result(row: dict[str, Any]) -> dict[str, Any]:
    acquisition = row.get("acquisition_test", {})
    downloaded = acquisition.get("downloaded_tree", {})
    existing = row.get("existing_data", {})
    load = row.get("load_test", {})
    return {
        "record_id": row["record_id"],
        "canonical_name": row["canonical_name"],
        "modalities": row.get("modalities", []),
        "download_type": row.get("download_type"),
        "selection": row.get("selection"),
        "selection_reason": row.get("selection_reason"),
        "estimated_size_gb": row.get("estimated_size_gb"),
        "preflight": {
            key: row.get("preflight", {}).get(key)
            for key in (
                "status",
                "exit_code",
                "automation_allowed",
                "access_friction",
                "availability_status",
                "loader_backend",
                "loader_name",
            )
        },
        "existing_data": {
            "file_count": existing.get("file_count"),
            "size_bytes": existing.get("size_bytes"),
            "recognized_by_dataset": existing.get("recognized_by_dataset"),
            "preserved": existing.get("preserved"),
        },
        "route_check": {
            key: row.get("route_check", {}).get(key)
            for key in (
                "status",
                "result",
                "dataset_transfer_started",
                "http_status",
            )
        },
        "acquisition_test": {
            "status": acquisition.get("status"),
            "exit_code": acquisition.get("exit_code"),
            "transfer_started": acquisition.get("transfer_started"),
            "message": acquisition.get("message"),
            "error_type": acquisition.get("error_type"),
            "manifest_generated": bool(acquisition.get("manifest_path")),
            "downloaded_tree": {
                "exists": downloaded.get("exists"),
                "file_count": downloaded.get("file_count"),
                "size_bytes": downloaded.get("size_bytes"),
                "metadata_fingerprint": downloaded.get("metadata_fingerprint"),
                "errors": downloaded.get("errors", []),
            },
            "worker_return_code": acquisition.get("worker_return_code"),
            "worker_timed_out": acquisition.get("worker_timed_out"),
            "worker_wall_seconds": acquisition.get("worker_wall_seconds"),
            "scratch_cleanup": {
                "status": acquisition.get("scratch_cleanup", {}).get("status"),
                "error": acquisition.get("scratch_cleanup", {}).get("error"),
            },
        },
        "load_test": {
            key: load.get(key)
            for key in (
                "status",
                "implemented",
                "split",
                "sample_count",
                "sample_path_exists",
                "image_decode_status",
            )
        },
        "record_completed": row.get("record_completed"),
    }


def sanitize(source: Path, destination: Path) -> None:
    payload = json.loads(source.read_text(encoding="utf-8"))
    metadata = payload["metadata"]
    public = {
        "metadata": {
            "schema_version": "1.0-public-redacted",
            "source_log": source.name,
            "run_started_at_utc": metadata.get("run_started_at_utc"),
            "run_completed_at_utc": metadata.get("run_completed_at_utc"),
            "catalog_records": metadata.get("catalog_records"),
            "selection_counts": metadata.get("selection_counts"),
            "excluded_backends": metadata.get("excluded_backends"),
            "surgical_video_excluded": metadata.get("surgical_video_excluded"),
            "google_drive_dataset_transfer_performed": metadata.get(
                "google_drive_dataset_transfer_performed"
            ),
            "environment": metadata.get("environment"),
            "completed_records": metadata.get("completed_records"),
            "existing_data_unchanged": metadata.get("existing_data_unchanged"),
            "scratch_root_removed": metadata.get("scratch_root_removed"),
            "checksums_calculated_for_catalog_wide_run": False,
            "public_redactions": (
                "Commands, credentials, local absolute paths, scratch paths, "
                "data roots, worker log tails, and machine-specific free-space "
                "values were excluded."
            ),
        },
        "results": [_public_result(row) for row in payload["results"]],
    }
    rendered = json.dumps(public, indent=2, ensure_ascii=False) + "\n"
    if WINDOWS_ABSOLUTE_PATH.search(rendered):
        raise RuntimeError("A Windows absolute path remains in the public audit")
    if len(public["results"]) != 251 or not all(
        row["record_completed"] for row in public["results"]
    ):
        raise RuntimeError("Public audit does not contain 251 completed rows")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(rendered, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source",
        type=Path,
        default=Path("hub/audit/download_load_verification_2026-07-30.json"),
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=Path(
            "hub/audit/download_load_verification_2026-07-30.public.json"
        ),
    )
    args = parser.parse_args()
    sanitize(args.source, args.out)
    print(f"Wrote public audit: {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
