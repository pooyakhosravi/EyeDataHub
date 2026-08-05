"""Generate record-level identity, role, and current-version audit files."""

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
from eyedatahub.core.relationships import RELATIONSHIP_EVIDENCE  # noqa: E402
from eyedatahub.core.resource_identity import (  # noqa: E402
    ANNOTATION_RECORD_IDS,
    RESOURCE_ROLE_DEFINITIONS,
    RESOURCE_ROLES,
    RETIRED_CATALOG_RECORDS,
    dataset_family_for,
    resource_role_for,
)
from eyedatahub.datasets.registry import REGISTRY  # noqa: E402
from hub.export_catalog import CATALOG_CUTOFF, CATALOG_RECORD_COUNT  # noqa: E402


AUDIT_DATE = "2026-08-02"
AUDIT_DIR = ROOT / "hub" / "audit"
REVIEW_PATH = AUDIT_DIR / f"resource_identity_review_{AUDIT_DATE}.csv"
SUMMARY_PATH = AUDIT_DIR / f"resource_identity_summary_{AUDIT_DATE}.json"
HISTORY_PATH = AUDIT_DIR / f"superseded_and_alternate_records_{AUDIT_DATE}.csv"


def _write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def generate() -> tuple[Path, Path, Path]:
    records = {dataset.info.name: dataset.info for dataset in REGISTRY.list_datasets()}
    if len(records) != CATALOG_RECORD_COUNT:
        raise RuntimeError(
            f"Expected {CATALOG_RECORD_COUNT} catalog records, found {len(records)}"
        )

    retired_ids = {entry.former_record_id for entry in RETIRED_CATALOG_RECORDS}
    if retired_ids & records.keys():
        raise RuntimeError(
            "Retired records remain in the current catalog: "
            f"{sorted(retired_ids & records.keys())}"
        )
    if not ANNOTATION_RECORD_IDS <= records.keys():
        raise RuntimeError(
            "Annotation role refers to missing records: "
            f"{sorted(ANNOTATION_RECORD_IDS - records.keys())}"
        )

    outgoing: dict[str, list[Any]] = defaultdict(list)
    incoming: dict[str, list[Any]] = defaultdict(list)
    for edge in RELATIONSHIP_EVIDENCE:
        if edge.source_record_id not in records or edge.target_record_id not in records:
            raise RuntimeError(
                "Relationship refers to a non-current record: "
                f"{edge.source_record_id} {edge.relationship_type} "
                f"{edge.target_record_id}"
            )
        outgoing[edge.source_record_id].append(edge)
        incoming[edge.target_record_id].append(edge)

    family_members: dict[str, list[str]] = defaultdict(list)
    for record_id in records:
        family_members[dataset_family_for(record_id)].append(record_id)

    rows: list[dict[str, Any]] = []
    for record_id, info in sorted(records.items()):
        role = resource_role_for(record_id)
        family_id = dataset_family_for(record_id)
        related_edges = (*outgoing.get(record_id, []), *incoming.get(record_id, []))
        rows.append(
            {
                "record_id": record_id,
                "canonical_name": info.full_name,
                "catalog_version": __version__,
                "catalog_search_cutoff": CATALOG_CUTOFF,
                "identity_review_date": AUDIT_DATE,
                "current_catalog_record": True,
                "resource_role": role,
                "resource_role_definition": RESOURCE_ROLE_DEFINITIONS[role],
                "dataset_family_id": family_id,
                "dataset_family_member_count": len(family_members[family_id]),
                "dataset_family_members": "|".join(sorted(family_members[family_id])),
                "outgoing_relationship_types": "|".join(
                    sorted({edge.relationship_type for edge in outgoing.get(record_id, [])})
                ),
                "outgoing_relationship_targets": "|".join(
                    sorted({edge.target_record_id for edge in outgoing.get(record_id, [])})
                ),
                "incoming_relationship_sources": "|".join(
                    sorted({edge.source_record_id for edge in incoming.get(record_id, [])})
                ),
                "relationship_evidence_urls": "|".join(
                    sorted({edge.evidence_url for edge in related_edges})
                ),
                "official_source_url": (
                    info.source_landing_page_url or info.download_url or ""
                ),
                "counting_rule": (
                    "Current data products are counted once. Previous versions and "
                    "unmodified alternate deposits are links only. Dataset-family "
                    "counts collapse documented collection/component records and "
                    "exact task views; derivatives and uncertain overlaps remain "
                    "separate."
                ),
            }
        )

    role_counts = Counter(row["resource_role"] for row in rows)
    if set(role_counts) - RESOURCE_ROLES:
        raise RuntimeError(f"Unknown resource roles: {set(role_counts) - RESOURCE_ROLES}")

    derived_record_ids = {
        edge.source_record_id
        for edge in RELATIONSHIP_EVIDENCE
        if edge.relationship_type == "derived_from"
    }
    annotation_derived_ids = derived_record_ids & ANNOTATION_RECORD_IDS
    multi_record_families = {
        family_id: sorted(members)
        for family_id, members in family_members.items()
        if len(members) > 1
    }
    history_rows = [entry.__dict__ for entry in RETIRED_CATALOG_RECORDS]

    summary = {
        "schema_version": "1.0",
        "catalog_version": __version__,
        "catalog_search_cutoff": CATALOG_CUTOFF,
        "identity_review_date": AUDIT_DATE,
        "current_catalog_record_count": len(records),
        "dataset_family_count": len(family_members),
        "records_in_multi_record_families": sum(
            len(members) for members in multi_record_families.values()
        ),
        "multi_record_family_count": len(multi_record_families),
        "multi_record_families": multi_record_families,
        "resource_role_counts_mutually_exclusive": dict(sorted(role_counts.items())),
        "records_with_documented_derived_from_relationship": len(derived_record_ids),
        "annotation_layer_count": len(ANNOTATION_RECORD_IDS),
        "annotation_layers_with_derived_from_relationship": len(annotation_derived_ids),
        "annotation_layers_extending_an_annotation_resource": len(
            ANNOTATION_RECORD_IDS - annotation_derived_ids
        ),
        "component_dataset_count": role_counts["component_dataset"],
        "collection_count": role_counts["collection"],
        "task_view_count": role_counts["task_view"],
        "superseded_versions_not_counted": sum(
            entry.disposition == "previous_version"
            for entry in RETIRED_CATALOG_RECORDS
        ),
        "alternate_repository_copies_not_counted": sum(
            entry.disposition == "alternate_repository_copy"
            for entry in RETIRED_CATALOG_RECORDS
        ),
        "retired_or_link_only_record_count": len(RETIRED_CATALOG_RECORDS),
        "role_definitions": RESOURCE_ROLE_DEFINITIONS,
        "record_count_definition": (
            "Current canonical data-resource records. Earlier versions and "
            "unmodified alternate deposits are not counted."
        ),
        "family_count_definition": (
            "Current records after narrowly grouping documented collection/component "
            "records and exact task views. Derivatives, extensions, and uncertain "
            "cohort overlaps remain separate families. This is not a count of "
            "independent participant cohorts."
        ),
        "third_party_dataset_files_included": False,
    }

    _write_csv(REVIEW_PATH, rows)
    _write_csv(HISTORY_PATH, history_rows)
    SUMMARY_PATH.write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(
        f"Wrote {len(rows)} current records in {len(family_members)} dataset "
        f"families and {len(history_rows)} link-only history rows."
    )
    return REVIEW_PATH, SUMMARY_PATH, HISTORY_PATH


if __name__ == "__main__":
    generate()
