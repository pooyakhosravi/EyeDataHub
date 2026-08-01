from __future__ import annotations

import subprocess
import zipfile
from pathlib import Path

import pytest
import requests

from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets import download_utils
from eyedatahub.datasets.registry import REGISTRY


def test_nested_released_layouts_load(tmp_path: Path) -> None:
    fives_image = (
        tmp_path
        / "fives"
        / "FIVES A Fundus Image Dataset for AI-based Vessel Segmentation"
        / "train"
        / "Original"
        / "001.png"
    )
    fives_mask = fives_image.parent.parent / "Ground truth" / "001.png"
    fives_image.parent.mkdir(parents=True)
    fives_mask.parent.mkdir(parents=True)
    fives_image.touch()
    fives_mask.touch()
    fives_samples = REGISTRY.get_dataset("fives").load(tmp_path, split="train")
    assert len(fives_samples) == 1
    assert fives_samples[0].image_path == str(fives_image)
    assert fives_samples[0].label == str(fives_mask)

    octdl_image = tmp_path / "octdl" / "OCTDL" / "AMD" / "amd_001.jpg"
    octdl_image.parent.mkdir(parents=True)
    octdl_image.touch()
    octdl_samples = REGISTRY.get_dataset("octdl").load(tmp_path)
    assert len(octdl_samples) == 1
    assert octdl_samples[0].image_path == str(octdl_image)
    assert octdl_samples[0].label == 0

    ddr_root = tmp_path / "ddr" / "_ext" / "DDR-dataset" / "DR_grading"
    ddr_image = ddr_root / "train" / "image_001.jpg"
    ddr_image.parent.mkdir(parents=True)
    ddr_image.touch()
    (ddr_root / "train.txt").write_text(
        "image_001.jpg 2\n",
        encoding="utf-8",
    )
    ddr_samples = REGISTRY.get_dataset("ddr").load(tmp_path, split="train")
    assert len(ddr_samples) == 1
    assert ddr_samples[0].image_path == str(ddr_image)
    assert ddr_samples[0].label == 2


def test_goals_loader_ignores_macos_metadata(tmp_path: Path) -> None:
    real_image = tmp_path / "goals" / "GOALS" / "Train" / "Image" / "0001.png"
    apple_double = (
        tmp_path
        / "goals"
        / "__MACOSX"
        / "GOALS"
        / "Train"
        / "Image"
        / "._0001.png"
    )
    real_image.parent.mkdir(parents=True)
    apple_double.parent.mkdir(parents=True)
    real_image.touch()
    apple_double.touch()

    samples = REGISTRY.get_dataset("goals").load(tmp_path, split="train")
    assert [sample.image_path for sample in samples] == [str(real_image)]


def test_stare_recognizes_extracted_layout(tmp_path: Path) -> None:
    image = tmp_path / "STARE" / "images" / "im0001.ppm"
    image.parent.mkdir(parents=True)
    image.touch()
    assert REGISTRY.get_dataset("stare").is_downloaded(tmp_path)


def test_grape_loads_nested_figshare_collection_layout(tmp_path: Path) -> None:
    image = (
        tmp_path
        / "grape"
        / "article_23575926"
        / "CFPs"
        / "1_OD_1.jpg"
    )
    image.parent.mkdir(parents=True)
    image.touch()

    samples = REGISTRY.get_dataset("grape").load(tmp_path, split="all")
    assert [sample.image_path for sample in samples] == [str(image)]


def test_dryad_prefers_public_version_archive(monkeypatch, tmp_path: Path) -> None:
    class FakeResponse:
        status_code = 200

        def __init__(self, payload):
            self.payload = payload

        def json(self):
            return self.payload

        def raise_for_status(self):
            return None

    def fake_get(url, headers, timeout):
        if "/datasets/" in url:
            return FakeResponse(
                {"_links": {"stash:version": {"href": "/api/v2/versions/1"}}}
            )
        return FakeResponse(
            {
                "_links": {
                    "stash:download": {
                        "href": "/api/v2/versions/1/download"
                    },
                    "stash:files": {
                        "href": "/api/v2/versions/1/files"
                    },
                }
            }
        )

    def fake_download_file(url, dest_path, desc=None, headers=None):
        assert url.endswith("/api/v2/versions/1/download")
        assert headers == {}
        destination = Path(dest_path)
        with zipfile.ZipFile(destination, "w") as archive:
            archive.writestr("nested/data.csv", "value\n1\n")
        return destination

    monkeypatch.setattr(download_utils.requests, "get", fake_get)
    monkeypatch.setattr(download_utils, "download_file", fake_download_file)

    paths = download_utils.download_dryad(
        "10.5061/dryad.example",
        tmp_path,
        extract=True,
    )
    assert paths == [tmp_path / "nested" / "data.csv"]
    assert paths[0].read_text(encoding="utf-8") == "value\n1\n"
    assert not (tmp_path / "dryad-version.zip").exists()


def test_dryad_falls_back_to_authenticated_files(
    monkeypatch,
    tmp_path: Path,
) -> None:
    class FakeResponse:
        status_code = 200

        def __init__(self, payload):
            self.payload = payload

        def json(self):
            return self.payload

        def raise_for_status(self):
            return None

    def fake_get(url, headers, timeout):
        assert headers == {"Authorization": "Bearer test-token"}
        if "/datasets/" in url:
            return FakeResponse(
                {"_links": {"stash:version": {"href": "/api/v2/versions/1"}}}
            )
        if url.endswith("/api/v2/versions/1"):
            return FakeResponse(
                {
                    "_links": {
                        "stash:download": {
                            "href": "/api/v2/versions/1/download"
                        },
                        "stash:files": {
                            "href": "/api/v2/versions/1/files"
                        },
                    }
                }
            )
        if url.endswith("/api/v2/versions/1/files"):
            return FakeResponse(
                {
                    "_embedded": {
                        "stash:files": [
                            {
                                "path": "data.csv",
                                "_links": {
                                    "stash:download": {
                                        "href": "/api/v2/files/2/download"
                                    }
                                },
                            }
                        ]
                    },
                    "_links": {},
                }
            )
        raise AssertionError(url)

    def fake_download_file(url, dest_path, desc=None, headers=None):
        if url.endswith("/api/v2/versions/1/download"):
            response = requests.Response()
            response.status_code = 405
            raise requests.HTTPError("too large", response=response)
        assert url.endswith("/api/v2/files/2/download")
        assert headers == {"Authorization": "Bearer test-token"}
        destination = Path(dest_path)
        destination.write_text("value\n1\n", encoding="utf-8")
        return destination

    monkeypatch.setattr(download_utils.requests, "get", fake_get)
    monkeypatch.setattr(download_utils, "download_file", fake_download_file)

    paths = download_utils.download_dryad(
        "10.5061/dryad.example",
        tmp_path,
        extract=True,
        token="test-token",
    )
    assert paths == [tmp_path / "data.csv"]


def test_download_file_uses_system_trust_fallback(
    monkeypatch,
    tmp_path: Path,
) -> None:
    destination = tmp_path / "payload.bin"

    def fail_requests(*args, **kwargs):
        raise requests.exceptions.SSLError("test certificate chain")

    def system_trust(url, partial_path, label, headers):
        Path(partial_path).write_bytes(b"payload")

    monkeypatch.setattr(download_utils, "_stream_requests_download", fail_requests)
    monkeypatch.setattr(
        download_utils,
        "_stream_system_trust_download",
        system_trust,
    )

    assert download_utils.download_file(
        "https://example.test/payload.bin",
        destination,
    ) == destination
    assert destination.read_bytes() == b"payload"
    assert not destination.with_name("payload.bin.part").exists()


def test_requests_download_uses_open_range_for_new_file(
    monkeypatch,
    tmp_path: Path,
) -> None:
    class FakeResponse:
        status_code = 206
        headers = {
            "content-range": "bytes 0-6/7",
            "content-length": "7",
        }

        def __enter__(self):
            return self

        def __exit__(self, *args):
            return None

        def raise_for_status(self):
            return None

        def iter_content(self, chunk_size):
            assert chunk_size == download_utils.CHUNK_SIZE
            yield b"payload"

    def fake_get(url, stream, timeout, headers):
        assert headers["Range"] == "bytes=0-"
        return FakeResponse()

    monkeypatch.setattr(download_utils.requests, "get", fake_get)
    partial = tmp_path / "payload.bin.part"
    download_utils._stream_requests_download(
        "https://example.test/payload.bin",
        partial,
        "payload",
        {},
    )
    assert partial.read_bytes() == b"payload"


def test_requests_download_rejects_short_range_response(
    monkeypatch,
    tmp_path: Path,
) -> None:
    class FakeResponse:
        status_code = 206
        headers = {
            "content-range": "bytes 0-6/10",
            "content-length": "7",
        }

        def __enter__(self):
            return self

        def __exit__(self, *args):
            return None

        def raise_for_status(self):
            return None

        def iter_content(self, chunk_size):
            yield b"payload"

    monkeypatch.setattr(
        download_utils.requests,
        "get",
        lambda *args, **kwargs: FakeResponse(),
    )
    with pytest.raises(OSError, match="Incomplete transfer"):
        download_utils._stream_requests_download(
            "https://example.test/payload.bin",
            tmp_path / "payload.bin.part",
            "payload",
            {},
        )


def test_rar_extraction_uses_validated_system_tar(
    monkeypatch,
    tmp_path: Path,
) -> None:
    archive = tmp_path / "dataset.rar"
    destination = tmp_path / "extracted"
    archive.write_bytes(b"placeholder")
    commands: list[list[str]] = []

    def fake_run(command, **kwargs):
        commands.append(command)
        if "-tf" in command:
            return subprocess.CompletedProcess(
                command,
                0,
                stdout="folder/image.jpg\n",
                stderr="",
            )
        if "-tvf" in command:
            return subprocess.CompletedProcess(
                command,
                0,
                stdout="-rw-r--r-- 0 user group 1 Jan 1 00:00 folder/image.jpg\n",
                stderr="",
            )
        image = destination / "folder" / "image.jpg"
        image.parent.mkdir(parents=True)
        image.write_bytes(b"x")
        return subprocess.CompletedProcess(command, 0, stdout="", stderr="")

    monkeypatch.setattr(download_utils.shutil, "which", lambda name: "tar")
    monkeypatch.setattr(download_utils.subprocess, "run", fake_run)

    download_utils.extract_archive(archive, destination)
    assert (destination / "folder" / "image.jpg").read_bytes() == b"x"
    assert [command[1] for command in commands] == ["-tf", "-tvf", "-xf"]


def test_corrected_access_and_size_metadata() -> None:
    hyamd = REGISTRY.get_dataset("hyamd")
    assert hyamd.info.dataset_doi == "10.13026/ydf1-z238"
    assert hyamd.info.access_friction == "controlled_or_manual"
    assert hyamd.info.requires_data_use_agreement is True
    assert preflight_dataset(hyamd, Path("data"))["status"] == (
        "manual_access_blocked"
    )

    oct5k = REGISTRY.get_dataset("oct5k")
    assert oct5k.info.download_type == "figshare"
    assert oct5k.info.size_gb == 0.05

    assert REGISTRY.get_dataset("tom500").info.size_gb == 2.31
    assert (
        preflight_dataset(REGISTRY.get_dataset("riga"), Path("data"))["status"]
        == "guided_instructions_only"
    )
    for record_id in (
        "dryad_cornea_oct_pentacam",
        "dryad_functional_oct_alzheimer",
    ):
        record = REGISTRY.get_dataset(record_id)
        assert record.info.access_friction == "anonymous_direct"
        assert record.info.acquisition_support == "guided_instructions_only"
        assert preflight_dataset(record, Path("data"))["status"] == (
            "guided_instructions_only"
        )
