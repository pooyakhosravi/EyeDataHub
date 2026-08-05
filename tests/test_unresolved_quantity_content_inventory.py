import json
import zipfile

from hub.audit import inspect_unresolved_quantity_deposits as content_module


def _mendeley_record(*, result="official_archive_route_confirmed"):
    return {
        "record_id": "example_mendeley",
        "canonical_name": "Example Mendeley Dataset",
        "provider": "mendeley",
        "official_source_url": "https://data.mendeley.com/datasets/abc123def4/2",
        "dataset_identifier": "abc123def4",
        "catalog_deposit_version": "2",
        "listing_result": result,
        "expected_bytes": 123,
    }


def test_mendeley_archive_is_inspected_and_deleted(monkeypatch, tmp_path):
    def fake_download(**kwargs):
        destination = kwargs["destination"]
        with zipfile.ZipFile(destination, "w") as archive:
            archive.writestr("images/one.jpg", b"image")
            archive.writestr("labels.csv", b"image,label\none,normal\n")
        return {
            "transferred_archive_bytes": kwargs["expected_bytes"],
            "local_archive_sha256": "a" * 64,
        }

    monkeypatch.setattr(content_module, "_download_mendeley_archive", fake_download)

    result = content_module._process_mendeley_record(
        record=_mendeley_record(),
        work_dir=tmp_path,
    )

    assert result["archive_integrity_confirmed"] is True
    assert result["acquired_file_count"] == 2
    assert result["content_extensions"] == {".csv": 1, ".jpg": 1}
    assert result["temporary_dataset_files_retained"] is False
    assert not list(tmp_path.rglob("*.zip"))


def test_run_selects_ready_mendeley_archive_but_not_preparing(
    monkeypatch, tmp_path
):
    ready = _mendeley_record()
    preparing = {
        **_mendeley_record(result="official_archive_preparing"),
        "record_id": "preparing_mendeley",
    }
    inventory_path = tmp_path / "inventory.json"
    output_path = tmp_path / "report.json"
    inventory_path.write_text(
        json.dumps({"records": [ready, preparing]}),
        encoding="utf-8",
    )
    processed = []

    def fake_process(*, record, work_dir):
        processed.append(record["record_id"])
        return {
            "record_id": record["record_id"],
            "provider": "mendeley",
            "download_completed": True,
            "acquired_file_count": 2,
            "acquired_bytes": 123,
        }

    monkeypatch.setattr(content_module, "_process_mendeley_record", fake_process)

    report = content_module.run(
        inventory_path=inventory_path,
        output_path=output_path,
        work_dir=tmp_path / "work",
        max_record_bytes=None,
        record_ids=set(),
    )

    assert processed == ["example_mendeley"]
    assert report["completed_record_count"] == 1
    assert report["completed_records_by_provider"] == {"mendeley": 1}
    assert report["mendeley_ready_archive_count"] == 1
    assert report["mendeley_completed_archive_count"] == 1
    assert report["mendeley_source_archive_preparing_records"] == [
        "preparing_mendeley"
    ]
