import csv
import io

import pytest

from tools.dataset_reviewer.server import (
    export_csv,
    publication_url,
    source_url,
    validate_review,
)
from tools.dataset_reviewer.model_data_screen import screen_record


def test_source_url_prefers_official_route():
    record = {
        "preferred_route_url": "https://official.example/data",
        "source_landing_page_url": "https://landing.example/data",
        "download_url": "https://mirror.example/data",
    }
    assert source_url(record) == "https://official.example/data"


def test_publication_url_uses_associated_doi():
    record = {
        "associated_publication_doi": "10.1000/example.123",
        "citation": "Example citation",
    }
    assert publication_url(record) == "https://doi.org/10.1000/example.123"


def test_publication_url_extracts_doi_from_citation():
    record = {
        "citation": "Example paper. doi:10.1000/example.456.",
    }
    assert publication_url(record) == "https://doi.org/10.1000/example.456"


def test_validate_review_accepts_multiple_tags():
    review = validate_review(
        {
            "decision": "needs_review",
            "score": 3,
            "tags": ["not_human", "no_reusable_data", "not_human"],
            "notes": "Check the files.",
        }
    )
    assert review["decision"] == "needs_review"
    assert review["score"] == 3
    assert review["tags"] == ["not_human", "no_reusable_data"]


def test_validate_review_rejects_unknown_decision():
    with pytest.raises(ValueError, match="Unsupported decision"):
        validate_review({"decision": "maybe", "tags": []})


def test_csv_export_contains_unreviewed_and_reviewed_records():
    catalog = {
        "records": [
            {
                "record_id": "one",
                "canonical_name": "One",
                "modalities": ["fundus"],
                "tasks": ["classification"],
                "preferred_route_url": "https://example.org/one",
                "internal_model_data_screen": {
                    "classification": "inherently_tabular_model_data",
                    "suggested_action": "retain",
                    "rationale": "Refraction is inherently tabular.",
                    "source_evidence": "Participant-level refraction rows.",
                    "suggested_modalities": ["tabular"],
                },
            },
            {
                "record_id": "two",
                "canonical_name": "Two",
                "modalities": ["oct"],
                "tasks": [],
                "preferred_route_url": "https://example.org/two",
            },
        ]
    }
    reviews = {
        "reviews": {
            "one": {
                "decision": "include",
                "score": 5,
                "tags": ["strong_dataset"],
                "notes": "Useful.",
                "reviewed_at": "2026-08-02T00:00:00+00:00",
            }
        }
    }
    rows = list(csv.DictReader(io.StringIO(export_csv(catalog, reviews).decode("utf-8-sig"))))
    assert len(rows) == 2
    assert rows[0]["decision"] == "include"
    assert rows[0]["screen_suggested_action"] == "retain"
    assert rows[0]["screen_suggested_modalities"] == "tabular"
    assert rows[1]["decision"] == ""


def test_model_data_screen_flags_derived_oct_measurements_without_scans():
    screen = screen_record(
        {
            "record_id": "mendeley_difference_retinal_nerve_fiber_layer_thickness",
            "modalities": ["tabular"],
            "description": "RNFL thickness values derived from OCT.",
        }
    )
    assert screen["classification"] == (
        "derived_imaging_measurements_without_source_data"
    )
    assert screen["suggested_action"] == "exclude_unless_source_images_are_found"
    assert screen["automatic_decision_applied"] is False


def test_model_data_screen_retains_refraction_as_inherently_tabular():
    screen = screen_record(
        {
            "record_id": "refraction_example",
            "modalities": ["tabular"],
            "description": "Participant-level refraction and visual acuity measurements.",
        }
    )
    assert screen["classification"] == "inherently_tabular_model_data"
    assert screen["suggested_action"] == "retain"


def test_model_data_screen_detects_incomplete_image_modality():
    screen = screen_record(
        {
            "record_id": "mendeley_nuclear_cataract_database_biomedical_machine_learning",
            "modalities": ["tabular"],
            "description": "Clinical slit-lamp image dataset.",
        }
    )
    assert screen["suggested_action"] == "correct_modality_and_retain"
    assert "external_eye" in screen["suggested_modalities"]
