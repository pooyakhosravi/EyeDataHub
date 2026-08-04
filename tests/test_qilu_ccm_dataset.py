import json
from pathlib import Path

import pytest

from eyedatahub.datasets.confocal import QiluCCMNerveSegmentationDataset
from eyedatahub.datasets.registry import REGISTRY


def test_qilu_ccm_metadata_and_registry_entry():
    dataset = REGISTRY.get_dataset("qilu_ccm_nerve_segmentation")
    info = dataset.info

    assert isinstance(dataset, QiluCCMNerveSegmentationDataset)
    assert info.num_samples == 410
    assert info.item_count_unit == "images"
    assert info.modalities == ["confocal", "tabular"]
    assert info.dataset_doi == "10.5281/zenodo.18779434"
    assert info.associated_publication_doi == "10.1038/s41597-026-07418-6"
    assert info.access_friction == "anonymous_direct"
    assert info.requires_api_token is False
    assert info.transfer_check_status == (
        "complete_current_deposit_downloaded_via_official_route"
    )


def test_qilu_ccm_loads_filename_matched_pairs(tmp_path: Path):
    dataset = QiluCCMNerveSegmentationDataset()
    root = tmp_path / dataset._SUBDIR / "Dataset"
    image_dir = root / "images"
    mask_dir = root / "annotations"
    image_dir.mkdir(parents=True)
    mask_dir.mkdir()

    for name in ("10101.png", "20101.png"):
        (image_dir / name).write_bytes(b"image")
        (mask_dir / name).write_bytes(b"mask")

    all_samples = dataset.load(tmp_path)
    set1_samples = dataset.load(tmp_path, split="set1")
    set2_samples = dataset.load(tmp_path, split="set2")

    assert [sample.sample_id for sample in all_samples] == ["10101", "20101"]
    assert [sample.sample_id for sample in set1_samples] == ["10101"]
    assert [sample.sample_id for sample in set2_samples] == ["20101"]
    assert all_samples[0].label.endswith("annotations\\10101.png") or (
        all_samples[0].label.endswith("annotations/10101.png")
    )


def test_qilu_ccm_rejects_unknown_split(tmp_path: Path):
    with pytest.raises(ValueError, match="split must be one of"):
        QiluCCMNerveSegmentationDataset().load(tmp_path, split="train")


def test_qilu_ccm_download_uses_current_zenodo_record(monkeypatch, tmp_path: Path):
    calls = []

    def fake_download(record_id, destination, extract):
        calls.append((record_id, Path(destination), extract))
        return []

    monkeypatch.setattr(
        "eyedatahub.datasets.confocal.download_zenodo",
        fake_download,
    )
    dataset = QiluCCMNerveSegmentationDataset()
    dataset.download(tmp_path)

    assert calls == [
        ("18779434", tmp_path / dataset._SUBDIR, True),
    ]


def test_qilu_ccm_public_confirmation_log_has_no_local_or_secret_values():
    path = (
        Path(__file__).resolve().parents[1]
        / "hub"
        / "audit"
        / "qilu_ccm_source_confirmation_2026-08-02.json"
    )
    document = json.loads(path.read_text(encoding="utf-8"))

    assert document["current_deposit"]["download_completed"] is True
    assert document["current_deposit"]["file"]["source_checksum_matched"] is True
    assert document["archive_structure"]["source_png_images"] == 410
    assert document["archive_structure"]["segmentation_mask_png_images"] == 410
    assert document["retention"]["third_party_dataset_files_in_repository"] is False
    serialized = json.dumps(document).lower()
    assert "authorization" not in serialized
    assert "h:\\" not in serialized
