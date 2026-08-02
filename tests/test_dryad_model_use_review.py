"""Regression tests for the human/model-use Dryad boundary."""

from pathlib import Path

from eyedatahub.datasets.registry import REGISTRY
from eyedatahub.datasets.scope_exclusions import (
    CATALOG_SCOPE_EXCLUSIONS,
    INSUFFICIENT_MODEL_EVIDENCE_IDS,
    NONHUMAN_DRYAD_RECORD_IDS,
    NOT_DISTINCT_MODEL_RESOURCE_IDS,
    RELATIONSHIP_ONLY_RESOURCE_IDS,
)
from hub.audit.build_dryad_model_use_review import build


ROOT = Path(__file__).resolve().parents[1]


def test_reviewed_dryad_scope_counts() -> None:
    assert len(NONHUMAN_DRYAD_RECORD_IDS) == 58
    assert len(NOT_DISTINCT_MODEL_RESOURCE_IDS) == 3
    assert len(INSUFFICIENT_MODEL_EVIDENCE_IDS) == 1
    assert len(RELATIONSHIP_ONLY_RESOURCE_IDS) == 1
    assert len(CATALOG_SCOPE_EXCLUSIONS) == 63
    assert not set(CATALOG_SCOPE_EXCLUSIONS).intersection(REGISTRY.names())
    assert len([name for name in REGISTRY.names() if name.startswith("dryad_")]) == 82


def test_dryad_review_is_record_level_and_complete() -> None:
    rows, summary = build(
        inventory_path=(
            ROOT / "hub" / "audit" / "dryad_model_use_inventory_2026-08-02.json"
        ),
        structure_path=(
            ROOT / "hub" / "audit" / "dryad_model_use_structure_2026-08-02.json"
        ),
        curated_review_path=(
            ROOT / "hub" / "audit" / "dryad_model_use_decisions_2026-08-02.json"
        ),
    )

    assert len(rows) == 145
    assert len({row["record_id"] for row in rows}) == 145
    assert summary["headline_catalog_included"] == 82
    assert summary["headline_catalog_excluded"] == 63
    assert summary["decision_counts"] == {
        "excluded_analysis_only": 2,
        "excluded_insufficient_model_use_evidence": 1,
        "excluded_nonhuman_or_nonhuman_derived": 58,
        "excluded_not_suitable_for_model_training_or_evaluation": 1,
        "excluded_relationship_only_resource": 1,
        "included_human_or_human_derived_model_resource": 82,
    }
    assert summary["credential_values_serialized"] is False
    assert summary["signed_or_download_urls_serialized"] is False
    assert summary["participant_values_serialized"] is False


def test_known_borderline_records_are_not_headline_records() -> None:
    expected = {
        "dryad_eye_head_visual_selection",
        "dryad_pg4f4qrwf",
        "dryad_rod_cone_dystrophy_genes",
        "dryad_rn8pk0pmm",
        "dryad_glaucoma_tears_mirna",
        "dryad_sf7m0cggh",
        "dryad_vq83bk3s8",
    }
    assert expected <= set(CATALOG_SCOPE_EXCLUSIONS)
