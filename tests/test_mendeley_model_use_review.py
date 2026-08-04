import json
from pathlib import Path

from eyedatahub.datasets.registry import REGISTRY
from eyedatahub.datasets.scope_exclusions import (
    MENDELEY_AUTHOR_REMOVED_UNCERTAIN_RECORD_IDS,
    MENDELEY_NOT_USEFUL_RECORD_IDS,
    MENDELEY_SCOPE_EXCLUSIONS,
)
from hub.audit.build_mendeley_model_use_review import build


SOURCE = Path("hub/audit/mendeley_download_verification_2026-08-03.json")
REVIEW = Path("hub/audit/mendeley_model_use_review_2026-08-03.json")


def test_mendeley_scope_exclusions_are_complete_and_absent_from_registry():
    assert len(MENDELEY_NOT_USEFUL_RECORD_IDS) == 20
    assert len(MENDELEY_AUTHOR_REMOVED_UNCERTAIN_RECORD_IDS) == 5
    assert len(MENDELEY_SCOPE_EXCLUSIONS) == 25
    assert not (set(MENDELEY_SCOPE_EXCLUSIONS) & set(REGISTRY.names()))


def test_mendeley_model_use_review_matches_builder_and_registry():
    expected = build(SOURCE)
    deposited = json.loads(REVIEW.read_text(encoding="utf-8"))
    assert deposited == expected
    assert deposited["records_reviewed"] == 141
    assert deposited["headline_catalog_included"] == 116
    assert deposited["headline_catalog_excluded"] == 25
    assert (
        sum(
            "data.mendeley.com/datasets/"
            in str(dataset.info.source_landing_page_url or "")
            for dataset in REGISTRY.list_datasets()
        )
        == 116
    )
