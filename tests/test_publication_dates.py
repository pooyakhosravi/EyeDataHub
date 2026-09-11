"""Publication dates are sourced metadata, not inferred citation years."""

import csv
import json
from datetime import date
from types import SimpleNamespace

import pytest
from click.testing import CliRunner

from eyedatahub.catalog import info_to_record, search_datasets
from eyedatahub.cli import main
from eyedatahub.core.dataset import DatasetInfo
from eyedatahub.core.publication_dates import (
    PUBLICATION_DATE_FIELDS,
    date_interval,
    publication_date_errors,
    publication_date_basis,
    reviewed_publication_dates,
)
from eyedatahub.datasets.registry import REGISTRY
from hub.docs.generate_dataset_pages import build_page, build_static_dataset_index
from hub.export_catalog import export_catalog


def make_info(name="date_fixture", value=None, **overrides):
    fields = {}
    if value is not None:
        fields = {
            "publication_date": value,
            "publication_date_precision": {4: "year", 7: "month", 10: "day"}[
                len(value)
            ],
            "publication_date_source_url": "https://example.org/dataset/history",
            "publication_date_source_field": "First published",
            "publication_date_scope": "initial_public_release",
            "publication_date_reviewed_on": "2026-09-11",
        }
    fields.update(overrides)
    return DatasetInfo(
        name=name,
        full_name=name,
        description="Fixture",
        modality="fundus",
        tasks=["classification"],
        num_samples=None,
        splits=["all"],
        **fields,
    )


def fixtures():
    return [
        SimpleNamespace(info=make_info(name, value))
        for name, value in [
            ("unknown", None),
            ("year", "2020"),
            ("month", "2020-06"),
            ("day", "2020-06-15"),
            ("early", "2019-12-31"),
            ("late", "2021-01-01"),
        ]
    ]


def names(**kwargs):
    return [ds.info.name for ds in search_datasets(fixtures(), **kwargs)]


@pytest.mark.parametrize(
    "value,start,end",
    [
        ("2020", date(2020, 1, 1), date(2020, 12, 31)),
        ("2020-02", date(2020, 2, 1), date(2020, 2, 29)),
        ("2020-02-29", date(2020, 2, 29), date(2020, 2, 29)),
    ],
)
def test_partial_precision(value, start, end):
    assert date_interval(value) == (start, end)
    info = make_info(value=value)
    assert not publication_date_errors(info)
    assert info_to_record(info)["publication_date"] == value


@pytest.mark.parametrize(
    "value",
    ["0000", "2023-02-29", "2020-13", "2020-1", "today", "2020-01-01T00:00:00Z", 2020],
)
def test_invalid_dates(value):
    with pytest.raises(ValueError):
        date_interval(value)


def test_unknown_date_not_inferred_from_title_citation_or_review():
    info = make_info(
        name="study_2020",
        citation="Dataset article. 2021.",
        source_check_date="2026-08-02",
    )
    assert all(getattr(info, field) is None for field in PUBLICATION_DATE_FIELDS)
    assert not publication_date_errors(info)


@pytest.mark.parametrize(
    "overrides",
    [
        {"publication_date_precision": "year"},
        {"publication_date_source_url": None},
        {"publication_date_source_url": 2020},
        {"publication_date_source_url": "https://[malformed"},
        {"publication_date_source_url": "https://user:secret@example.org/history"},
        {"publication_date_source_field": ""},
        {"publication_date_source_field": 2020},
        {"publication_date_notes": ["invalid"]},
        {"publication_date_scope": "article_publication"},
        {"publication_date_scope": []},
        {"publication_date_reviewed_on": "2026"},
        {"publication_date_reviewed_on": "2019-12-31"},
    ],
)
def test_incoherent_evidence_rejected(overrides):
    assert publication_date_errors(make_info(value="2020-06-15", **overrides))


def test_orphan_evidence_rejected():
    assert publication_date_errors(make_info(publication_date_precision="day"))


@pytest.mark.parametrize("scope", ["repository_deposit", "associated_publication"])
def test_fallback_dates_require_explanation_and_retain_basis(scope):
    info = make_info(value="2020-06", publication_date_scope=scope)
    assert publication_date_errors(info)
    info.publication_date_notes = (
        "Selected the verified source date after conflicting metadata."
    )
    assert not publication_date_errors(info)
    assert info_to_record(info)["publication_date_scope"] == scope
    assert publication_date_basis(scope) != "Unknown"

    class FixtureDataset:
        def load(self, *args, **kwargs):
            raise NotImplementedError

    dataset = FixtureDataset()
    dataset.info = info
    page = build_page(dataset, [])
    assert publication_date_basis(scope) in page
    assert info.publication_date_notes in page


def test_reviewed_entries_are_first_class_and_valid():
    entries = reviewed_publication_dates()
    assert entries
    for name, entry in entries.items():
        info = REGISTRY.get_dataset(name).info
        assert not publication_date_errors(info), name
        assert set(entry).issubset(PUBLICATION_DATE_FIELDS)
        assert info.publication_date == entry["publication_date"]
    # A class's explicit metadata is never silently overwritten by the backfill.
    info = make_info(name=next(iter(entries)), value="2000")
    assert info.publication_date == "2000"


def test_inclusive_ranges_and_unknowns():
    assert names(published_from="2020", published_through="2020") == [
        "day",
        "month",
        "year",
    ]
    # A year/month-only date can overlap a narrower query; precision is retained.
    assert names(published_from="2020-06-15", published_through="2020-06-15") == [
        "day",
        "month",
        "year",
    ]
    assert names(publication_date_status="unknown") == ["unknown"]
    assert "unknown" not in names(publication_date_status="known")
    assert names(publication_date_status="unknown", published_from="2020") == []


def test_chronological_sort_and_search():
    assert names(sort="publication-date") == [
        "early",
        "year",
        "month",
        "day",
        "late",
        "unknown",
    ]
    assert names(sort="publication-date-desc") == [
        "late",
        "day",
        "month",
        "year",
        "early",
        "unknown",
    ]
    assert names(query="2020-06") == ["day", "month"]


@pytest.mark.parametrize(
    "kwargs",
    [
        {"published_from": "2021", "published_through": "2020"},
        {"published_from": "invalid"},
        {"sort": "invalid"},
        {"publication_date_status": "invalid"},
    ],
)
def test_invalid_search_options_raise_even_without_records(kwargs):
    with pytest.raises(ValueError):
        search_datasets([], **kwargs)


def test_cli_date_filter_sort_and_show():
    runner = CliRunner()
    result = runner.invoke(
        main,
        [
            "search",
            "--publication-date-status",
            "known",
            "--sort",
            "publication-date",
            "--json",
        ],
    )
    assert result.exit_code == 0, result.output
    payload = json.loads(result.output)
    records = payload["datasets"] if isinstance(payload, dict) else payload
    assert records and all(row["publication_date"] for row in records)
    assert [date_interval(row["publication_date"])[0] for row in records] == sorted(
        date_interval(row["publication_date"])[0] for row in records
    )
    result = runner.invoke(main, ["show", records[0]["name"], "--json"])
    assert result.exit_code == 0, result.output
    assert json.loads(result.output)["publication_date_source_url"]
    invalid = runner.invoke(
        main, ["search", "--published-from", "2025", "--published-through", "2020"]
    )
    assert invalid.exit_code == 2
    assert "must not be after" in invalid.output


def test_exports_and_website_keep_date_evidence(tmp_path):
    json_path, csv_path = export_catalog(tmp_path)
    records = json.loads(json_path.read_text(encoding="utf-8"))["records"]
    with csv_path.open(encoding="utf-8", newline="") as handle:
        csv_rows = {row["name"]: row for row in csv.DictReader(handle)}
    datasets = REGISTRY.list_datasets()
    web_rows = {
        row["name"]: row for row in build_static_dataset_index(datasets)["datasets"]
    }
    for row in records:
        for field in PUBLICATION_DATE_FIELDS:
            assert web_rows[row["name"]][field] == row[field]
            assert csv_rows[row["name"]][field] == (row[field] or "")
    name = next(iter(reviewed_publication_dates()))
    page = build_page(REGISTRY.get_dataset(name), datasets)
    assert "Publication date" in page
    assert reviewed_publication_dates()[name]["publication_date"] in page
