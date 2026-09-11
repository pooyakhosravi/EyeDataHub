"""Every catalog record must have a date or a documented source check."""

import json
from datetime import date
from pathlib import Path

from eyedatahub.core.publication_dates import PUBLICATION_DATE_FIELDS
from eyedatahub.datasets.registry import REGISTRY


AUDIT_DIR = Path(__file__).resolve().parents[1] / "hub" / "audit"
SOURCES = ("dryad_mendeley", "zenodo_figshare", "project_sources")


def test_date_research_covers_every_record_without_duplicate_assignments():
    known = {}
    unresolved = {}
    for source in SOURCES:
        initial = json.loads(
            (AUDIT_DIR / f"publication_dates_{source}.json").read_text(encoding="utf-8")
        )
        remaining = json.loads(
            (AUDIT_DIR / f"publication_dates_remaining_{source}.json").read_text(
                encoding="utf-8"
            )
        )
        for row in initial["records"] + remaining["records"]:
            record_id = row["record_id"]
            assert record_id not in known, record_id
            known[record_id] = row
        for row in remaining["unresolved"]:
            record_id = row["record_id"]
            assert record_id not in unresolved, record_id
            assert row["reason"].strip(), record_id
            assert row["checked_urls"], record_id
            assert all(
                url.startswith(("https://", "http://")) for url in row["checked_urls"]
            )
            date.fromisoformat(row["review_date"])
            unresolved[record_id] = row

    catalog = {ds.info.name: ds.info for ds in REGISTRY.list_datasets()}
    assert not known.keys() & unresolved.keys()
    assert known.keys() | unresolved.keys() == catalog.keys()
    for record_id, info in catalog.items():
        if record_id in unresolved:
            assert info.publication_date is None, record_id
        else:
            for field in PUBLICATION_DATE_FIELDS:
                if field != "publication_date_notes":
                    assert getattr(info, field) == known[record_id][field], (
                        record_id,
                        field,
                    )
