"""Reconcile repository search hits to the unique EyeDataHub catalog.

The output supports the manuscript candidate-flow figure. Search hits are
counted at repository-record level, while the final catalog is counted at
canonical-resource level. Alternate deposits, mirrors, and versioned copies
therefore do not increase the final catalog total.

This is a point-in-time reconciliation, not an inferred history of how every
older catalog record was first discovered. Catalog records not represented by
an eligible hit in the five repository searches are grouped as records from
the other documented search routes, including publications, project and
GitHub pages, challenge sites, and other official sources.
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_LEDGER = ROOT / "hub" / "audit" / "repository_screening_ledger_2026-08-02.csv"
DEFAULT_SUMMARY = (
    ROOT / "hub" / "audit" / "repository_screening_summary_2026-08-02.json"
)
DEFAULT_CATALOG = ROOT / "hub" / "catalog.csv"
DEFAULT_FLOW_CSV = ROOT / "hub" / "audit" / "catalog_search_flow_2026-08-02.csv"
DEFAULT_FLOW_JSON = ROOT / "hub" / "audit" / "catalog_search_flow_2026-08-02.json"
DEFAULT_RECONCILIATION = (
    ROOT / "hub" / "audit" / "catalog_search_reconciliation_2026-08-02.csv"
)

ELIGIBLE_DECISIONS = {"existing_catalog_record", "included_new_record"}
EXCLUSION_DECISIONS = (
    "excluded_not_eye_or_ophthalmology",
    "excluded_duplicate_or_alternate_deposit",
    "excluded_not_distinct_reusable_resource",
    "excluded_insufficient_source_metadata",
    "excluded_nonhuman_or_nonhuman_derived",
    "excluded_not_suitable_for_model_training_or_evaluation",
)


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    if not rows:
        raise ValueError(f"No rows to write: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def _write_json(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(value, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )
    temporary.replace(path)


def _canonical_ids(row: dict[str, str]) -> list[str]:
    values = json.loads(row.get("canonical_record_ids") or "[]")
    if not isinstance(values, list) or not all(
        isinstance(value, str) for value in values
    ):
        raise ValueError(
            f"Invalid canonical_record_ids for {row['platform']}:{row['stable_id']}"
        )
    return [value for value in values if value]


def build_flow(
    *,
    ledger_rows: list[dict[str, str]],
    screening_summary: dict[str, Any],
    catalog_rows: list[dict[str, str]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], dict[str, Any]]:
    if not screening_summary.get("manuscript_flow_ready"):
        incomplete = [
            platform
            for platform, status in screening_summary.get(
                "source_search_status", {}
            ).items()
            if not status.get("result_set_complete")
        ]
        pending = sum(
            row["final_decision"] == "manual_review_pending" for row in ledger_rows
        )
        raise ValueError(
            "Candidate flow is not ready: "
            f"incomplete source searches={incomplete}, pending reviews={pending}."
        )

    workflow_sources = screening_summary["workflow_sources"]
    unexpected_sources = sorted(
        {row["platform"] for row in ledger_rows} - set(workflow_sources)
    )
    if unexpected_sources:
        raise ValueError(f"Unexpected screening sources: {unexpected_sources}")

    catalog_ids = {row["record_id"] for row in catalog_rows}
    represented_by: dict[str, set[str]] = defaultdict(set)
    eligible_hit_count = 0
    for row in ledger_rows:
        if row["final_decision"] not in ELIGIBLE_DECISIONS:
            continue
        canonical_ids = _canonical_ids(row)
        if not canonical_ids:
            raise ValueError(
                "Eligible screening row lacks a canonical record id: "
                f"{row['platform']}:{row['stable_id']}"
            )
        eligible_hit_count += 1
        for record_id in canonical_ids:
            if record_id not in catalog_ids:
                raise ValueError(
                    f"Screening row references uncataloged record id: {record_id}"
                )
            represented_by[record_id].add(row["platform"])

    represented_ids = set(represented_by)
    other_ids = catalog_ids - represented_ids
    per_source_hits = {
        source: sum(row["platform"] == source for row in ledger_rows)
        for source in workflow_sources
    }
    exclusion_counts = {
        decision: sum(row["final_decision"] == decision for row in ledger_rows)
        for decision in EXCLUSION_DECISIONS
    }
    pending_count = sum(
        row["final_decision"] == "manual_review_pending" for row in ledger_rows
    )
    total_hits = len(ledger_rows)
    accounted_hits = eligible_hit_count + sum(exclusion_counts.values()) + pending_count
    if accounted_hits != total_hits:
        raise ValueError(
            f"Screening decisions account for {accounted_hits} of {total_hits} hits."
        )

    flow_rows: list[dict[str, Any]] = []
    for source in workflow_sources:
        flow_rows.append(
            {
                "stage": "repository_search_hits",
                "item": source,
                "count": per_source_hits[source],
                "counting_unit": "repository_records",
            }
        )
    for decision in EXCLUSION_DECISIONS:
        flow_rows.append(
            {
                "stage": "excluded_after_record_review",
                "item": decision,
                "count": exclusion_counts[decision],
                "counting_unit": "repository_records",
            }
        )
    flow_rows.extend(
        [
            {
                "stage": "eligible_repository_hits",
                "item": "eligible_after_screening",
                "count": eligible_hit_count,
                "counting_unit": "repository_records",
            },
            {
                "stage": "canonical_reconciliation",
                "item": "unique_catalog_records_represented_by_repository_searches",
                "count": len(represented_ids),
                "counting_unit": "canonical_catalog_records",
            },
            {
                "stage": "other_documented_search_routes",
                "item": "additional_records_from_publications_projects_github_challenges_and_other_official_sources",
                "count": len(other_ids),
                "counting_unit": "canonical_catalog_records",
            },
            {
                "stage": "final_catalog",
                "item": "unique_catalog_records",
                "count": len(catalog_ids),
                "counting_unit": "canonical_catalog_records",
            },
        ]
    )

    reconciliation_rows = [
        {
            "record_id": record_id,
            "represented_by_eligible_repository_hit": str(
                record_id in represented_ids
            ).lower(),
            "repository_search_sources": json.dumps(
                sorted(represented_by.get(record_id, set())), ensure_ascii=True
            ),
            "flow_source_group": (
                "five_repository_searches"
                if record_id in represented_ids
                else "other_documented_search_routes"
            ),
        }
        for record_id in sorted(catalog_ids)
    ]

    output = {
        "schema_version": "1.0",
        "search_dates": {
            platform: screening_summary["source_search_status"][platform]
            for platform in workflow_sources
        },
        "repository_search_hit_counts": per_source_hits,
        "total_repository_search_hits": total_hits,
        "exclusion_counts": exclusion_counts,
        "eligible_repository_hits": eligible_hit_count,
        "unique_catalog_records_represented_by_repository_searches": len(
            represented_ids
        ),
        "additional_catalog_records_from_other_documented_search_routes": len(
            other_ids
        ),
        "final_unique_catalog_records": len(catalog_ids),
        "counting_note": (
            "Repository hits and exclusions count repository records. The final "
            "catalog counts canonical resources. Alternate deposits, mirrors, and "
            "versioned copies do not add to the final total. Records in the other-"
            "routes group are a point-in-time source reconciliation, not an inferred "
            "historical discovery provenance classification."
        ),
        "credential_values_serialized": False,
        "signed_or_download_urls_serialized": False,
    }
    return flow_rows, reconciliation_rows, output


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ledger", type=Path, default=DEFAULT_LEDGER)
    parser.add_argument("--summary", type=Path, default=DEFAULT_SUMMARY)
    parser.add_argument("--catalog", type=Path, default=DEFAULT_CATALOG)
    parser.add_argument("--flow-csv", type=Path, default=DEFAULT_FLOW_CSV)
    parser.add_argument("--flow-json", type=Path, default=DEFAULT_FLOW_JSON)
    parser.add_argument(
        "--reconciliation-csv", type=Path, default=DEFAULT_RECONCILIATION
    )
    args = parser.parse_args()
    flow_rows, reconciliation_rows, output = build_flow(
        ledger_rows=_read_csv(args.ledger),
        screening_summary=json.loads(args.summary.read_text(encoding="utf-8")),
        catalog_rows=_read_csv(args.catalog),
    )
    _write_csv(args.flow_csv, flow_rows)
    _write_csv(args.reconciliation_csv, reconciliation_rows)
    _write_json(args.flow_json, output)
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
