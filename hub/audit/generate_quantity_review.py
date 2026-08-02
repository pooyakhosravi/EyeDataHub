"""Generate record-level and quantity-level source-count audit exports.

The review keeps one primary quantity per catalog record for compatibility and
also exports every additional source-reported component quantity.  Totals are
only calculated within the exact same unit.  Because related catalog records
and derivative components can overlap, unit totals are descriptive sums of
record-level primary quantities, not counts of unique people or files.
"""

from __future__ import annotations

import csv
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from eyedatahub import __version__  # noqa: E402
from eyedatahub.core.quantities import QUANTITY_UNITS  # noqa: E402
from eyedatahub.datasets.registry import REGISTRY  # noqa: E402
from hub.export_catalog import CATALOG_CUTOFF, CATALOG_RECORD_COUNT  # noqa: E402


AUDIT_DIR = ROOT / "hub" / "audit"
REVIEW_DATE = "2026-08-02"
REVIEW_PATH = AUDIT_DIR / f"resource_quantity_review_{REVIEW_DATE}.csv"
EVIDENCE_PATH = AUDIT_DIR / f"resource_quantity_evidence_{REVIEW_DATE}.csv"
UNIT_PATH = AUDIT_DIR / f"resource_quantity_by_unit_{REVIEW_DATE}.csv"
UNRESOLVED_PATH = AUDIT_DIR / f"resource_quantity_unresolved_{REVIEW_DATE}.csv"
SUMMARY_PATH = AUDIT_DIR / f"resource_quantity_summary_{REVIEW_DATE}.json"


def _write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def _primary(entries: list[dict[str, Any]]) -> dict[str, Any] | None:
    matches = [entry for entry in entries if entry["primary"]]
    if len(matches) > 1:
        raise RuntimeError("A record has more than one primary quantity")
    return matches[0] if matches else None


def generate() -> tuple[Path, Path, Path, Path, Path]:
    datasets = sorted(REGISTRY.list_datasets(), key=lambda value: value.info.name)
    if len(datasets) != CATALOG_RECORD_COUNT:
        raise RuntimeError(
            f"Expected {CATALOG_RECORD_COUNT} records, found {len(datasets)}"
        )

    review_rows: list[dict[str, Any]] = []
    evidence_rows: list[dict[str, Any]] = []
    unresolved_rows: list[dict[str, Any]] = []
    primary_by_unit: dict[str, list[dict[str, Any]]] = defaultdict(list)

    for dataset in datasets:
        info = dataset.info
        entries = list(info.reported_quantities or [])
        primary = _primary(entries)
        if primary is not None:
            if primary["count"] != info.num_samples:
                raise RuntimeError(f"Primary count mismatch for {info.name}")
            if primary["unit"] != info.item_count_unit:
                raise RuntimeError(f"Primary unit mismatch for {info.name}")
            if primary["unit"] not in QUANTITY_UNITS:
                raise RuntimeError(f"Unknown primary unit for {info.name}")
            primary_by_unit[primary["unit"]].append(primary)
            status = "primary_quantity_resolved"
        else:
            status = "primary_quantity_unresolved"
            unresolved_rows.append(
                {
                    "record_id": info.name,
                    "canonical_name": info.full_name,
                    "official_source_url": info.source_landing_page_url or "",
                    "catalog_version": __version__,
                    "catalog_search_cutoff": CATALOG_CUTOFF,
                    "quantity_review_date": REVIEW_DATE,
                    "available_nonprimary_quantities": json.dumps(
                        entries, ensure_ascii=False, sort_keys=True
                    ),
                    "reason": (
                        "No reproducible primary item count was exposed for the "
                        "cataloged source version."
                    ),
                }
            )

        review_rows.append(
            {
                "record_id": info.name,
                "canonical_name": info.full_name,
                "primary_category": info.primary_category,
                "modalities": "|".join(info.modalities),
                "catalog_version": __version__,
                "catalog_search_cutoff": CATALOG_CUTOFF,
                "quantity_review_date": REVIEW_DATE,
                "official_source_url": info.source_landing_page_url or "",
                "primary_quantity_status": status,
                "primary_count": primary["count"] if primary else "",
                "primary_unit": primary["unit"] if primary else "",
                "primary_scope": primary["scope"] if primary else "",
                "primary_exactness": primary["exactness"] if primary else "",
                "primary_evidence_basis": primary["evidence_basis"] if primary else "",
                "primary_evidence_url": primary["evidence_url"] if primary else "",
                "reported_quantity_count": len(entries),
                "additional_quantity_count": len(entries) - int(primary is not None),
                "reported_quantities_json": json.dumps(
                    entries, ensure_ascii=False, sort_keys=True
                ),
                "counting_note": (
                    "Quantities with different units are not interchangeable. "
                    "Related records and derivative components may overlap."
                ),
            }
        )

        for index, entry in enumerate(entries, start=1):
            evidence_rows.append(
                {
                    "record_id": info.name,
                    "canonical_name": info.full_name,
                    "primary_category": info.primary_category,
                    "modalities": "|".join(info.modalities),
                    "quantity_index": index,
                    **entry,
                    "catalog_version": __version__,
                    "catalog_search_cutoff": CATALOG_CUTOFF,
                }
            )

    unit_rows = []
    for unit, entries in sorted(primary_by_unit.items()):
        exactness = Counter(entry["exactness"] for entry in entries)
        unit_rows.append(
            {
                "unit": unit,
                "records_with_primary_quantity": len(entries),
                "sum_of_primary_counts": sum(int(entry["count"]) for entry in entries),
                "exact_count_records": exactness["exact"],
                "approximate_count_records": exactness["approximate"],
                "exactness_not_assessed_records": exactness["not_assessed"],
                "source_conflict_records": exactness["source_conflict"],
                "counting_note": (
                    "Record-level primary quantities are mutually exclusive by unit, "
                    "but records and cohorts can overlap through documented lineage."
                ),
            }
        )

    _write_csv(REVIEW_PATH, review_rows, list(review_rows[0]))
    _write_csv(EVIDENCE_PATH, evidence_rows, list(evidence_rows[0]))
    _write_csv(UNIT_PATH, unit_rows, list(unit_rows[0]))
    _write_csv(UNRESOLVED_PATH, unresolved_rows, list(unresolved_rows[0]))

    summary = {
        "schema_version": "1.0",
        "catalog_version": __version__,
        "catalog_search_cutoff": CATALOG_CUTOFF,
        "quantity_review_date": REVIEW_DATE,
        "catalog_record_count": len(datasets),
        "records_with_resolved_primary_quantity": sum(
            row["primary_quantity_status"] == "primary_quantity_resolved"
            for row in review_rows
        ),
        "records_with_unresolved_primary_quantity": len(unresolved_rows),
        "quantity_evidence_row_count": len(evidence_rows),
        "records_with_multiple_reported_quantities": sum(
            row["reported_quantity_count"] > 1 for row in review_rows
        ),
        "primary_quantities_by_unit": {
            row["unit"]: {
                "record_count": row["records_with_primary_quantity"],
                "sum": row["sum_of_primary_counts"],
                "exact_count_records": row["exact_count_records"],
                "approximate_count_records": row["approximate_count_records"],
                "exactness_not_assessed_records": row[
                    "exactness_not_assessed_records"
                ],
                "source_conflict_records": row["source_conflict_records"],
            }
            for row in unit_rows
        },
        "unresolved_record_ids": [row["record_id"] for row in unresolved_rows],
        "counting_note": (
            "Primary totals are calculated only within identical units. They are "
            "descriptive sums of catalog records, not unique-cohort totals, because "
            "documented derivatives, subsets, versions, mirrors, and components overlap."
        ),
        "third_party_dataset_files_included": False,
    }
    SUMMARY_PATH.write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(
        f"Wrote {len(review_rows)} record reviews, {len(evidence_rows)} quantity "
        f"rows, and {len(unresolved_rows)} unresolved records."
    )
    return REVIEW_PATH, EVIDENCE_PATH, UNIT_PATH, UNRESOLVED_PATH, SUMMARY_PATH


if __name__ == "__main__":
    generate()
