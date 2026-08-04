"""Tests for source-linked catalog quantity evidence and its exports."""

from __future__ import annotations

import csv
import json
from collections import defaultdict

from eyedatahub.core.dataset import DatasetInfo
from eyedatahub.core.quantities import (
    EVIDENCE_BASES,
    EXACTNESS_VALUES,
    PUBLIC_QUANTITY_FIELDS,
    QUANTITY_UNITS,
)
from eyedatahub.datasets.registry import REGISTRY
from hub.audit import generate_quantity_review as quantity_review
from hub.export_catalog import export_catalog


def test_reviewed_primary_override_replaces_legacy_count_and_preserves_exactness() -> (
    None
):
    """A central review can correct the compatibility primary-count fields."""

    info = DatasetInfo(
        name="rasti_oct",
        full_name="Rasti OCT Dataset",
        description="Legacy volume-level count",
        modality="oct",
        tasks=["classification"],
        num_samples=148,
        splits=["all"],
        download_url="https://example.org/rasti",
    )

    assert info.num_samples == 4254
    assert info.item_count_unit == "b_scans"
    assert info.reported_quantities[0] == {
        "count": 4254,
        "unit": "b_scans",
        "scope": "Approximate B-scan count",
        "evidence_url": "https://doi.org/10.1109/TMI.2017.2780115",
        "evidence_basis": "associated_publication",
        "primary": True,
        "exactness": "approximate",
        "review_date": "2026-08-01",
        "notes": "",
    }


def test_record_level_quantity_evidence_is_preserved_when_no_central_review_exists() -> (
    None
):
    evidence = {
        "count": 12,
        "unit": "participants",
        "scope": "Source-described study cohort",
        "evidence_url": "https://doi.org/10.5061/dryad.example",
        "evidence_basis": "official_source_description",
        "primary": True,
        "exactness": "exact",
        "review_date": "2026-08-01",
        "notes": "",
    }
    info = DatasetInfo(
        name="test_inline_quantity_evidence",
        full_name="Inline Quantity Test",
        description="A test-only source-reviewed record.",
        modality="tabular",
        tasks=["classification"],
        num_samples=None,
        splits=["all"],
        download_url="https://doi.org/10.5061/dryad.example",
        reported_quantities=[evidence],
    )

    assert info.reported_quantities == [evidence]
    assert info.num_samples == 12
    assert info.item_count_unit == "participants"
    assert info.item_count_evidence_url == evidence["evidence_url"]


def test_multiple_quantities_keep_component_scopes_and_units_separate() -> None:
    entries = REGISTRY.get_dataset("ut_fsocta").info.reported_quantities

    assert len(entries) == 4
    assert entries[0]["primary"] is True
    assert entries[0]["unit"] == "participants"
    assert [entry["count"] for entry in entries[1:]] == [194, 194, 362]
    assert {entry["unit"] for entry in entries[1:]} == {"images"}
    assert "not an independent cohort" in entries[2]["notes"]


def test_complete_deposit_inspection_resolves_three_primary_quantities() -> None:
    china = REGISTRY.get_dataset("china_fundus_cimt").info
    assert (china.num_samples, china.item_count_unit) == (5806, "images")
    assert [entry["count"] for entry in china.reported_quantities] == [5806, 2]

    gleam = REGISTRY.get_dataset("gleam").info
    assert (gleam.num_samples, gleam.item_count_unit) == (3600, "images")
    assert [(entry["count"], entry["unit"]) for entry in gleam.reported_quantities] == [
        (3600, "images"),
        (1200, "records"),
        (841, "participants"),
    ]
    assert "repeat samples" in gleam.reported_quantities[0]["notes"]

    rpgr = REGISTRY.get_dataset("dryad_rpgr_cone_rod_wes").info
    assert (rpgr.num_samples, rpgr.item_count_unit) == (1, "participants")
    assert [entry["count"] for entry in rpgr.reported_quantities] == [1, 2]


def test_retinal_corrugations_uses_current_source_version_and_flags_conflict() -> None:
    info = REGISTRY.get_dataset("retinal_corrugations_oct").info

    assert info.download_url == "https://data.mendeley.com/datasets/bzsc7gd9p3/2"
    assert info.num_samples == 69
    assert info.item_count_unit == "b_scans"
    assert info.reported_quantities[0]["exactness"] == "source_conflict"
    assert info.reported_quantities[1]["count"] == 66
    assert info.reported_quantities[1]["unit"] == "participants"


def test_runtime_quantities_match_the_public_schema_and_controlled_vocabularies() -> (
    None
):
    for dataset in REGISTRY.list_datasets():
        for quantity in dataset.info.reported_quantities:
            assert tuple(quantity) == PUBLIC_QUANTITY_FIELDS
            assert quantity["unit"] in QUANTITY_UNITS
            assert quantity["evidence_basis"] in EVIDENCE_BASES
            assert quantity["exactness"] in EXACTNESS_VALUES


def test_catalog_json_and_csv_serialize_reported_quantities(tmp_path) -> None:
    json_path, csv_path = export_catalog(tmp_path)
    payload = json.loads(json_path.read_text(encoding="utf-8"))
    by_id = {record["record_id"]: record for record in payload["records"]}

    assert (
        by_id["ut_fsocta"]["reported_quantities"]
        == REGISTRY.get_dataset("ut_fsocta").info.reported_quantities
    )

    with csv_path.open(newline="", encoding="utf-8") as handle:
        rows = {row["record_id"]: row for row in csv.DictReader(handle)}
    assert (
        json.loads(rows["ut_fsocta"]["reported_quantities"])
        == by_id["ut_fsocta"]["reported_quantities"]
    )


def test_quantity_review_reports_current_counts_and_never_sums_unlike_units(
    monkeypatch, tmp_path
) -> None:
    monkeypatch.setattr(quantity_review, "REVIEW_PATH", tmp_path / "review.csv")
    monkeypatch.setattr(quantity_review, "EVIDENCE_PATH", tmp_path / "evidence.csv")
    monkeypatch.setattr(quantity_review, "UNIT_PATH", tmp_path / "by_unit.csv")
    monkeypatch.setattr(quantity_review, "UNRESOLVED_PATH", tmp_path / "unresolved.csv")
    monkeypatch.setattr(quantity_review, "SUMMARY_PATH", tmp_path / "summary.json")

    _, _, unit_path, unresolved_path, summary_path = quantity_review.generate()
    summary = json.loads(summary_path.read_text(encoding="utf-8"))

    assert summary["catalog_record_count"] == 451
    assert summary["records_with_resolved_primary_quantity"] == 324
    assert summary["records_with_unresolved_primary_quantity"] == 127
    assert len(summary["unresolved_record_ids"]) == 127
    assert "retinal_corrugations_oct" not in summary["unresolved_record_ids"]

    with unit_path.open(newline="", encoding="utf-8") as handle:
        unit_rows = list(csv.DictReader(handle))
    expected_primary_sums = defaultdict(int)
    for dataset in REGISTRY.list_datasets():
        for quantity in dataset.info.reported_quantities:
            if quantity["primary"]:
                expected_primary_sums[quantity["unit"]] += quantity["count"]
    assert {
        row["unit"]: int(row["sum_of_primary_counts"]) for row in unit_rows
    } == expected_primary_sums
    assert "total_primary_count" not in summary

    with unresolved_path.open(newline="", encoding="utf-8") as handle:
        unresolved_rows = list(csv.DictReader(handle))
    assert {row["record_id"] for row in unresolved_rows} == set(
        summary["unresolved_record_ids"]
    )
