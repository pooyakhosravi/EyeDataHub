"""Generate the frozen per-record access-verification ledger.

The ledger combines author-conducted source reconciliation with the automated
URL probe.  A successful HTTP response is never promoted to route verification
on its own, and an automated probe failure does not overwrite a documented
manual source check.  Transfer evidence is represented separately through the
acquisition-support fields and acquisition validation log.
"""
from __future__ import annotations

import argparse
import csv
import json
import platform
from pathlib import Path
from typing import Any

from eyedatahub import __version__
from eyedatahub.datasets.registry import REGISTRY


CHECK_DATE = "2026-07-21"


def _authentication_state(info: Any) -> str:
    if info.access_friction == "anonymous_direct":
        return "unauthenticated"
    if info.requires_api_token is True:
        return "credentials_required_not_stored"
    if info.requires_authentication is True:
        return "user_authentication_required"
    if info.requires_manual_approval is True:
        return "manual_authorization_required"
    if info.requires_author_contact is True:
        return "author_correspondence_required"
    return "not_applicable_or_unknown"


def _verification_level(info: Any) -> str:
    if info.acquisition_support == "end_to_end_tested":
        return "4_complete_download_validated"
    if info.acquisition_support == "transfer_tested_partial":
        return "3_transfer_initiated"
    if info.availability_status == "available":
        return "2_acquisition_route_verified"
    return "1_source_page_checked"


def generate_rows(url_report: dict[str, Any]) -> list[dict[str, Any]]:
    probes = {row["name"]: row for row in url_report["findings"]}
    rows: list[dict[str, Any]] = []
    for dataset in sorted(REGISTRY.list_datasets(), key=lambda item: item.info.name):
        info = dataset.info
        probe = probes.get(info.name, {})
        probe_status = probe.get("status", "not_run")
        if info.availability_status == "unavailable":
            result = "official_route_unavailable_at_verification_date"
            limitation = info.failure_reason or info.route_check_notes
            current_route_visible = "false"
        elif info.availability_status == "unverified":
            result = "insufficient_evidence_for_current_acquisition_route"
            limitation = info.failure_reason or info.route_check_notes
            current_route_visible = "unknown"
        elif probe_status in {"ok", "auth_required"}:
            result = info.route_check_result
            limitation = info.route_check_notes
            current_route_visible = "true"
        else:
            result = f"{info.route_check_result}_with_probe_limitation"
            limitation = (
                f"{info.route_check_notes} Automated probe status: {probe_status}; "
                "reachability alone was not used to classify access."
            )
            current_route_visible = "true"

        rows.append(
            {
                "record_id": info.name,
                "canonical_name": info.full_name,
                "verification_date": info.route_last_checked or CHECK_DATE,
                "verification_level": _verification_level(info),
                "official_source_checked": info.source_landing_page_url or "",
                "preferred_route_checked": info.preferred_route_url or "",
                "preferred_route_type": info.preferred_route_type,
                "resolved_destination": probe.get("final_url", ""),
                "dataset_specific_page_confirmed_by_curator": (
                    "true" if info.author_source_checked is True else "unknown"
                ),
                "current_route_visible": current_route_visible,
                "authentication_state": _authentication_state(info),
                "access_friction": info.access_friction,
                "availability_status": info.availability_status,
                "route_check_result": result,
                "automated_probe_status": probe_status,
                "automated_probe_http_status": probe.get("http_status", ""),
                "failure_or_limitation": limitation,
                "curator": "EyeDataHub author team",
                "author_source_checked": "true" if info.author_source_checked else "false",
                "independent_audit_status": info.independent_audit_status,
                "source_terms_evidence_url": info.terms_evidence_url or "",
                "dataset_files_transferred_for_this_row": (
                    "complete"
                    if info.acquisition_support == "end_to_end_tested"
                    else "partial_or_metadata_only"
                    if info.acquisition_support == "transfer_tested_partial"
                    else "none"
                ),
                "environment": (
                    f"{platform.system()} | Python {platform.python_version()} | "
                    f"EyeDataHub {__version__}"
                ),
            }
        )
    return rows


def write_rows(rows: list[dict[str, Any]], output: Path, url_report: dict[str, Any]) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    output.with_suffix(".json").write_text(
        json.dumps(
            {
                "schema_version": "1.0",
                "verification_protocol": {
                    "level_1": "official source page checked",
                    "level_2": "current acquisition route checked and reconciled with the record",
                    "level_3": "official metadata, file listing, API request, or representative transfer succeeded",
                    "level_4": "complete official deposit or complete official test artifact transferred",
                    "http_probe_limitation": (
                        "HTTP reachability is supporting evidence only and does not establish "
                        "that a response is the intended acquisition endpoint."
                    ),
                },
                "source_url_probe_generated_at": url_report["metadata"].get("generated_at"),
                "record_count": len(rows),
                "records": rows,
            },
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url-report", type=Path, default=Path("hub/audit/url_report.json"))
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    url_report = json.loads(args.url_report.read_text(encoding="utf-8"))
    rows = generate_rows(url_report)
    write_rows(rows, args.out, url_report)
    print(f"access verification: {len(rows)} records; {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
