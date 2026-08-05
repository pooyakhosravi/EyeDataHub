"""Parity checks for the source-confirmed Mendeley search additions."""

from __future__ import annotations

import json
from pathlib import Path

from eyedatahub.datasets.repository_search_mendeley_2026 import (
    MENDELEY_REPOSITORY_SEARCH_RECORDS,
    WITHHELD_SOURCE_IDS,
)
from eyedatahub.datasets.registry import DatasetRegistry


ROOT = Path(__file__).resolve().parents[1]


def _expected_source_ids() -> set[str]:
    reconciliation = json.loads(
        (ROOT / "hub" / "audit" / "mendeley_canonical_reconciliation_2026-08-02.json").read_text(
            encoding="utf-8"
        )
    )["records"]
    confirmation = {
        row["stable_id"]: row
        for row in json.loads(
            (ROOT / "hub" / "audit" / "mendeley_source_confirmation_2026-08-02.json").read_text(
                encoding="utf-8"
            )
        )["records"]
    }
    return {
        row["stable_id"]
        for row in reconciliation
        if row["canonical_action"] == "new_canonical_record"
        and confirmation[row["stable_id"]]["final_recommendation"] == "confirmed_include_new"
        and row["stable_id"] not in WITHHELD_SOURCE_IDS
    }


def test_mendeley_search_additions_match_reconciled_source_ids() -> None:
    source_ids = {row["repository_record_id"] for row in MENDELEY_REPOSITORY_SEARCH_RECORDS}
    assert source_ids == _expected_source_ids()
    assert len(MENDELEY_REPOSITORY_SEARCH_RECORDS) == len(source_ids)


def test_mendeley_search_additions_have_unique_stable_slugs() -> None:
    slugs = [row["name"] for row in MENDELEY_REPOSITORY_SEARCH_RECORDS]
    assert len(slugs) == len(set(slugs))
    assert all(slug.startswith("mendeley_") for slug in slugs)


def test_mendeley_search_additions_pass_registry_validation() -> None:
    registry = DatasetRegistry()
    for dataset in __import__(
        "eyedatahub.datasets.repository_search_mendeley_2026",
        fromlist=["MENDELEY_REPOSITORY_SEARCH_DATASETS"],
    ).MENDELEY_REPOSITORY_SEARCH_DATASETS:
        registry.register(dataset)
    assert registry.validation_errors() == []
