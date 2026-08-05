import json
from types import SimpleNamespace

from hub.audit import inventory_unresolved_quantity_deposits as inventory_module
from hub.audit.inventory_unresolved_quantity_deposits import (
    MENDELEY_DATA_API_ROOT,
    MENDELEY_PATTERN,
    _figshare_inventory,
    _inventory_provider,
    _mendeley_inventory,
)


class _Response:
    def __init__(self, payload, status_code=200, headers=None):
        self._payload = payload
        self.status_code = status_code
        self.headers = headers or {}

    def json(self):
        return self._payload

    def raise_for_status(self):
        return None


class _Session:
    def __init__(self, payload, status_code=200):
        self.payload = payload
        self.status_code = status_code
        self.urls = []

    def get(self, url, *args, **kwargs):
        self.urls.append(url)
        return _Response(self.payload, status_code=self.status_code)


def test_mendeley_pattern_accepts_versioned_and_unversioned_urls():
    versioned = MENDELEY_PATTERN.search(
        "https://data.mendeley.com/datasets/abc123def4/2"
    )
    unversioned = MENDELEY_PATTERN.search(
        "https://data.mendeley.com/datasets/abc123def4"
    )

    assert versioned.groupdict() == {"dataset_id": "abc123def4", "version": "2"}
    assert unversioned.groupdict() == {
        "dataset_id": "abc123def4",
        "version": None,
    }


def test_manual_repository_routes_are_inventoried_by_their_actual_provider():
    mendeley = SimpleNamespace(
        source_landing_page_url="https://data.mendeley.com/datasets/abc123def4",
        download_url="",
        repository_record_id="abc123def4",
        download_type="manual",
    )
    figshare = SimpleNamespace(
        source_landing_page_url="https://doi.org/10.6084/m9.figshare.12345.v1",
        download_url="",
        repository_record_id="12345",
        download_type="manual",
    )

    assert _inventory_provider(mendeley) == "mendeley"
    assert _inventory_provider(figshare) == "figshare"


def test_figshare_inventory_omits_download_urls_and_retains_checksums():
    session = _Session(
        {
            "doi": "10.6084/m9.figshare.12345.v1",
            "version": 1,
            "files": [
                {
                    "id": 7,
                    "name": "dataset.zip",
                    "size": 123,
                    "mimetype": "application/zip",
                    "supplied_md5": "a" * 32,
                    "computed_md5": "a" * 32,
                    "download_url": "https://example.invalid/short-lived-url",
                    "is_link_only": False,
                }
            ],
        }
    )

    result = _figshare_inventory(
        session,
        record_id="example",
        canonical_name="Example",
        official_source_url="https://doi.org/10.6084/m9.figshare.12345.v1",
        article_id="12345",
        catalog_version="1",
    )

    assert result["dataset_identifier"] == "12345"
    assert result["expected_file_count"] == 1
    assert result["expected_bytes"] == 123
    assert result["source_checksums_available"] == 1
    assert "short-lived-url" not in json.dumps(result)


def test_mendeley_inventory_uses_only_the_official_data_api_host():
    session = _Session(
        [
            {
                "id": "file-id",
                "filename": "dataset.zip",
                "size": 456,
                "download_url": "https://example.invalid/short-lived-url",
            }
        ]
    )

    result = _mendeley_inventory(
        session,
        record_id="example",
        canonical_name="Example",
        official_source_url="https://data.mendeley.com/datasets/abc123def4/2",
        catalog_version="2",
        headers={"Authorization": "Bearer test-only-token"},
        authentication_source="authorization_code",
    )

    assert session.urls == [
        f"{MENDELEY_DATA_API_ROOT}/datasets/publics/abc123def4/files"
    ]
    assert result["listing_result"] == "official_file_listing_confirmed"
    assert result["expected_file_count"] == 1
    assert result["expected_bytes"] == 456
    assert "test-only-token" not in json.dumps(result)
    assert "short-lived-url" not in json.dumps(result)


def test_mendeley_inventory_falls_back_to_official_browser_archive(monkeypatch):
    session = _Session({"message": "Unauthorized"}, status_code=401)
    monkeypatch.setattr(inventory_module, "_MENDELEY_BEARER_REJECTED", False)
    monkeypatch.setattr(
        inventory_module,
        "_mendeley_browser_archive_size",
        lambda **_kwargs: (206, 42_027_691),
    )

    result = _mendeley_inventory(
        session,
        record_id="example",
        canonical_name="Example",
        official_source_url="https://data.mendeley.com/datasets/abc123def4/2",
        catalog_version="2",
        headers={"Authorization": "Bearer rejected-test-token"},
        authentication_source="refresh_token",
    )

    assert result["listing_result"] == "official_archive_route_confirmed"
    assert result["expected_bytes"] == 42_027_691
    assert result["expected_file_count"] is None
    assert "rejected-test-token" not in json.dumps(result)
