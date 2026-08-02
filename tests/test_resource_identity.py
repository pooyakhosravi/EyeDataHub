"""Tests for current-version retention and dataset-family counting."""

from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path

from eyedatahub.core.relationships import RELATIONSHIP_EVIDENCE
from eyedatahub.core.resource_identity import (
    ANNOTATION_RECORD_IDS,
    RETIRED_CATALOG_RECORDS,
    dataset_family_for,
    resource_role_for,
)
from eyedatahub.datasets.registry import REGISTRY


ROOT = Path(__file__).resolve().parents[1]
AUDIT_DIR = ROOT / "hub" / "audit"
AUDIT_DATE = "2026-08-02"


def test_current_catalog_identity_counts() -> None:
    record_ids = {dataset.info.name for dataset in REGISTRY.list_datasets()}
    retired_ids = {entry.former_record_id for entry in RETIRED_CATALOG_RECORDS}
    families = {dataset_family_for(record_id) for record_id in record_ids}
    role_counts = Counter(resource_role_for(record_id) for record_id in record_ids)

    assert len(record_ids) == 475
    assert len(families) == 470
    assert not record_ids & retired_ids
    assert role_counts == {
        "current_dataset": 431,
        "annotation_layer": 17,
        "derivative_dataset": 17,
        "task_view": 3,
        "component_dataset": 3,
        "collection": 2,
        "extension_dataset": 2,
    }


def test_relationship_and_annotation_identity_is_complete() -> None:
    record_ids = {dataset.info.name for dataset in REGISTRY.list_datasets()}
    derived_ids = {
        edge.source_record_id
        for edge in RELATIONSHIP_EVIDENCE
        if edge.relationship_type == "derived_from"
    }

    assert len(derived_ids) == 33
    assert len(ANNOTATION_RECORD_IDS) == 17
    assert len(derived_ids & ANNOTATION_RECORD_IDS) == 16
    assert ANNOTATION_RECORD_IDS <= record_ids
    assert all(
        edge.source_record_id in record_ids and edge.target_record_id in record_ids
        for edge in RELATIONSHIP_EVIDENCE
    )


def test_retired_routes_are_preserved_on_current_records() -> None:
    records = {dataset.info.name: dataset.info for dataset in REGISTRY.list_datasets()}
    alternate_urls = {
        record_id: {
            source.get("url")
            for source in info.alternate_sources
        }
        for record_id, info in records.items()
    }

    for entry in RETIRED_CATALOG_RECORDS:
        assert entry.evidence_url in alternate_urls[entry.canonical_record_id]


def test_generated_identity_review_matches_runtime_catalog() -> None:
    review_path = AUDIT_DIR / f"resource_identity_review_{AUDIT_DATE}.csv"
    summary_path = AUDIT_DIR / f"resource_identity_summary_{AUDIT_DATE}.json"
    history_path = AUDIT_DIR / f"superseded_and_alternate_records_{AUDIT_DATE}.csv"

    with review_path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    with history_path.open(newline="", encoding="utf-8") as handle:
        history_rows = list(csv.DictReader(handle))
    summary = json.loads(summary_path.read_text(encoding="utf-8"))

    assert len(rows) == 475
    assert len({row["record_id"] for row in rows}) == 475
    assert len({row["dataset_family_id"] for row in rows}) == 470
    assert len(history_rows) == 4
    assert summary["current_catalog_record_count"] == 475
    assert summary["dataset_family_count"] == 470
    assert summary["records_with_documented_derived_from_relationship"] == 33
    assert summary["annotation_layer_count"] == 17
    assert summary["component_dataset_count"] == 3
    assert summary["superseded_versions_not_counted"] == 2
    assert summary["alternate_repository_copies_not_counted"] == 2
