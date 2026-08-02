"""Consistency tests for the reviewed inter-record relationship graph."""

from __future__ import annotations

import csv
import json
from pathlib import Path

from eyedatahub.core.relationships import RELATIONSHIP_EVIDENCE, RELATIONSHIP_TYPES
from eyedatahub.datasets.registry import REGISTRY


ROOT = Path(__file__).resolve().parents[1]
AUDIT_DIR = ROOT / "hub" / "audit"
REVIEW_DATE = "2026-08-01"


def test_relationship_graph_is_valid_and_matches_runtime_catalog() -> None:
    datasets = {dataset.info.name: dataset for dataset in REGISTRY.list_datasets()}
    evidence_edges = {
        (edge.source_record_id, edge.relationship_type, edge.target_record_id)
        for edge in RELATIONSHIP_EVIDENCE
    }
    runtime_edges = {
        (record_id, relationship["type"], relationship["target"])
        for record_id, dataset in datasets.items()
        for relationship in dataset.info.relationships
    }

    assert len(datasets) == 386
    assert len(RELATIONSHIP_EVIDENCE) == len(evidence_edges) == 142
    assert runtime_edges == evidence_edges
    assert all(source != target for source, _, target in evidence_edges)
    assert all(kind in RELATIONSHIP_TYPES for _, kind, _ in evidence_edges)
    assert all(source in datasets and target in datasets for source, _, target in evidence_edges)
    assert all(
        edge.evidence_url.startswith(("http://", "https://"))
        for edge in RELATIONSHIP_EVIDENCE
    )


def test_symmetric_and_component_relationships_have_inverses() -> None:
    edges = {
        (edge.source_record_id, edge.relationship_type, edge.target_record_id)
        for edge in RELATIONSHIP_EVIDENCE
    }
    for source, relationship_type, target in edges:
        if relationship_type == "same_or_overlapping_cohort_as":
            assert (target, relationship_type, source) in edges
        if relationship_type == "has_component":
            assert (target, "component_of", source) in edges


def test_record_level_review_and_edge_exports_match_graph() -> None:
    review_path = AUDIT_DIR / f"resource_relationship_review_{REVIEW_DATE}.csv"
    edge_path = AUDIT_DIR / f"resource_relationship_edges_{REVIEW_DATE}.csv"
    summary_path = AUDIT_DIR / f"resource_relationship_summary_{REVIEW_DATE}.json"

    with review_path.open(newline="", encoding="utf-8") as handle:
        review_rows = list(csv.DictReader(handle))
    with edge_path.open(newline="", encoding="utf-8") as handle:
        edge_rows = list(csv.DictReader(handle))
    summary = json.loads(summary_path.read_text(encoding="utf-8"))

    assert len(review_rows) == 386
    assert len({row["record_id"] for row in review_rows}) == 386
    assert len(edge_rows) == len(RELATIONSHIP_EVIDENCE) == 142
    assert summary["catalog_record_count"] == 386
    assert summary["reviewed_record_count"] == 386
    assert summary["directed_relationship_edge_count"] == 142
    assert summary["records_participating_in_confirmed_relationships"] == 94
    assert summary["third_party_dataset_files_included"] is False


def test_known_false_positive_links_are_absent() -> None:
    edges = {
        (edge.source_record_id, edge.relationship_type, edge.target_record_id)
        for edge in RELATIONSHIP_EVIDENCE
    }
    prohibited_pairs = {
        ("airogs", "eyepacs"),
        ("fairvlmed", "harvard_fairvision"),
        ("brset", "mbrset"),
        ("mbrset", "brset"),
        ("maples_dr", "messidor2"),
        ("riga_plus", "messidor2"),
        ("ut_fsocta", "rose"),
        ("ophora", "ophnet2024"),
    }
    assert not {
        (source, target)
        for source, _, target in edges
        if (source, target) in prohibited_pairs
    }
