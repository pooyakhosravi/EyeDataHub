import json

from hub.audit import inventory_mendeley_catalog as inventory_module
from hub.audit.build_mendeley_verification_report import build


def test_browser_inventory_confirms_exact_versioned_archive(monkeypatch):
    monkeypatch.setattr(
        inventory_module,
        "_mendeley_browser_archive_size",
        lambda **_kwargs: (206, 123),
    )
    record = inventory_module._inventory_one(
        {
            "name": "example",
            "full_name": "Example",
            "source_landing_page_url": (
                "https://data.mendeley.com/datasets/abc123def4/2"
            ),
            "download_url": "",
            "resource_version": None,
        }
    )

    assert record["dataset_identifier"] == "abc123def4"
    assert record["catalog_deposit_version"] == "2"
    assert record["listing_result"] == "official_archive_route_confirmed"
    assert record["expected_bytes"] == 123


def test_browser_inventory_keeps_controlled_access_separate(monkeypatch):
    monkeypatch.setattr(
        inventory_module,
        "_mendeley_browser_archive_size",
        lambda **_kwargs: (404, None),
    )
    monkeypatch.setattr(
        inventory_module,
        "_mendeley_browser_page_metadata",
        lambda **_kwargs: ("1", "PENDING"),
    )
    monkeypatch.setattr(
        inventory_module,
        "_public_snapshot_state",
        lambda *_args: {
            "http_status": 200,
            "is_confidential": True,
            "blocked_reason": "",
        },
    )

    record = inventory_module._inventory_one(
        {
            "name": "controlled",
            "full_name": "Controlled",
            "source_landing_page_url": (
                "https://data.mendeley.com/datasets/abc123def4/1"
            ),
            "download_url": "",
            "resource_version": None,
        }
    )

    assert record["listing_result"] == "controlled_access_required"


def test_browser_inventory_records_source_block(monkeypatch):
    monkeypatch.setattr(
        inventory_module,
        "_mendeley_browser_archive_size",
        lambda **_kwargs: (404, None),
    )
    monkeypatch.setattr(
        inventory_module,
        "_mendeley_browser_page_metadata",
        lambda **_kwargs: ("1", "PENDING"),
    )
    monkeypatch.setattr(
        inventory_module,
        "_public_snapshot_state",
        lambda *_args: {
            "http_status": 451,
            "is_confidential": None,
            "blocked_reason": "As per author's request",
        },
    )

    record = inventory_module._inventory_one(
        {
            "name": "blocked",
            "full_name": "Blocked",
            "source_landing_page_url": (
                "https://data.mendeley.com/datasets/def456abc7/1"
            ),
            "download_url": "",
            "resource_version": None,
        }
    )

    assert record["listing_result"] == "source_blocked_by_author"


def test_focused_report_keeps_source_preparing_separate(tmp_path):
    inventory_path = tmp_path / "inventory.json"
    content_path = tmp_path / "content.json"
    json_path = tmp_path / "report.json"
    csv_path = tmp_path / "report.csv"
    inventory_path.write_text(
        json.dumps(
            {
                "records": [
                    {
                        "record_id": "ready",
                        "canonical_name": "Ready",
                        "official_source_url": (
                            "https://data.mendeley.com/datasets/abc123def4/1"
                        ),
                        "dataset_identifier": "abc123def4",
                        "catalog_deposit_version": "1",
                        "listing_result": "official_archive_route_confirmed",
                        "expected_bytes": 123,
                    },
                    {
                        "record_id": "preparing",
                        "canonical_name": "Preparing",
                        "official_source_url": (
                            "https://data.mendeley.com/datasets/def456abc7/1"
                        ),
                        "dataset_identifier": "def456abc7",
                        "catalog_deposit_version": "1",
                        "listing_result": "official_archive_preparing",
                        "expected_bytes": None,
                    },
                ]
            }
        ),
        encoding="utf-8",
    )
    content_path.write_text(
        json.dumps(
            {
                "records": [
                    {
                        "record_id": "ready",
                        "provider": "mendeley",
                        "download_completed": True,
                        "acquired_bytes": 123,
                        "acquired_file_count": 2,
                        "archive_uncompressed_bytes": 456,
                        "archive_integrity_confirmed": True,
                        "local_archive_sha256": "a" * 64,
                        "inspection_date": "2026-08-03",
                    }
                ]
            }
        ),
        encoding="utf-8",
    )

    report = build(
        inventory_path=inventory_path,
        content_path=content_path,
        json_path=json_path,
        csv_path=csv_path,
    )

    assert report["catalog_mendeley_record_count"] == 2
    assert report["complete_versioned_zip_verified_count"] == 1
    assert report["source_archive_preparing_count"] == 1
    assert report["source_archive_preparing_record_ids"] == ["preparing"]
    assert report["controlled_access_required_count"] == 0
    assert report["source_blocked_count"] == 0
