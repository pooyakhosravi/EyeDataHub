"""Regression tests for repository-search reconciliation."""

from hub.audit.build_repository_screening_ledger import _catalog_match


CATALOG_ROW = {
    "record_id": "example_dataset",
    "dataset_doi": "10.6084/m9.figshare.12345.v2",
    "associated_publication_doi": "10.1000/example.paper",
    "repository_record_id": "12345",
    "download_url": "https://doi.org/10.6084/m9.figshare.12345.v2",
    "source_landing_page_url": "https://doi.org/10.6084/m9.figshare.12345.v2",
    "preferred_route_url": "https://doi.org/10.6084/m9.figshare.12345.v2",
    "canonical_resolver_url": "https://doi.org/10.6084/m9.figshare.12345.v2",
}


def test_publication_doi_does_not_identify_a_dataset_deposit() -> None:
    candidate = {
        "stable_id": "99999",
        "official_source_url": "https://figshare.com/articles/dataset/99999",
        "public_metadata": {"doi": "10.1000/example.paper.s001"},
    }
    detail = {
        "doi": "10.1000/example.paper.s001",
        "resource_doi": "10.1000/example.paper",
    }

    assert _catalog_match(candidate, detail, [CATALOG_ROW]) == ""


def test_versioned_figshare_doi_matches_its_dataset_family() -> None:
    candidate = {
        "stable_id": "12345",
        "official_source_url": "https://figshare.com/articles/dataset/12345",
        "public_metadata": {"doi": "10.6084/m9.figshare.12345.v3"},
    }
    detail = {"doi": "10.6084/m9.figshare.12345.v3"}

    assert _catalog_match(candidate, detail, [CATALOG_ROW]) == "example_dataset"

