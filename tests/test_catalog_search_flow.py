import json

import pytest

from hub.audit.build_catalog_search_flow import build_flow


def _row(
    platform: str,
    stable_id: str,
    decision: str,
    canonical_ids: list[str] | None = None,
) -> dict[str, str]:
    return {
        "platform": platform,
        "stable_id": stable_id,
        "final_decision": decision,
        "canonical_record_ids": json.dumps(canonical_ids or []),
    }


def _summary(*, ready: bool = True) -> dict[str, object]:
    sources = ["dryad", "mendeley", "kaggle", "figshare", "huggingface"]
    return {
        "workflow_sources": sources,
        "manuscript_flow_ready": ready,
        "source_search_status": {
            source: {
                "status": "completed",
                "result_set_complete": True,
                "unique_search_hits": 1,
            }
            for source in sources
        },
    }


def test_flow_counts_repository_hits_and_canonical_records_separately() -> None:
    rows = [
        _row("dryad", "d1", "existing_catalog_record", ["alpha"]),
        _row(
            "figshare",
            "f1",
            "excluded_duplicate_or_alternate_deposit",
            ["alpha"],
        ),
        _row("kaggle", "k1", "included_new_record", ["beta"]),
        _row("huggingface", "h1", "excluded_not_eye_or_ophthalmology"),
        _row("mendeley", "m1", "excluded_insufficient_source_metadata"),
    ]
    _, reconciliation, output = build_flow(
        ledger_rows=rows,
        screening_summary=_summary(),
        catalog_rows=[{"record_id": value} for value in ("alpha", "beta", "gamma")],
    )

    assert output["total_repository_search_hits"] == 5
    assert output["eligible_repository_hits"] == 2
    assert output["unique_catalog_records_represented_by_repository_searches"] == 2
    assert output["additional_catalog_records_from_other_documented_search_routes"] == 1
    assert output["final_unique_catalog_records"] == 3
    assert len(reconciliation) == 3


def test_flow_refuses_incomplete_screening() -> None:
    with pytest.raises(ValueError, match="Candidate flow is not ready"):
        build_flow(
            ledger_rows=[],
            screening_summary=_summary(ready=False),
            catalog_rows=[{"record_id": "alpha"}],
        )
