from pathlib import Path
import json
import pytest

from click.testing import CliRunner

import eyedatahub as edh
from eyedatahub.cli import _resolve_datasets, main
from eyedatahub.datasets.registry import REGISTRY
from eyedatahub.datasets.scope_exclusions import CATALOG_SCOPE_EXCLUSIONS


EXPECTED_DATASET_COUNT = 479


def test_registry_export_and_count():
    assert edh.REGISTRY is REGISTRY
    assert len(REGISTRY.list_datasets()) == EXPECTED_DATASET_COUNT


def test_registry_required_fields_and_license_families():
    allowed_license_families = {
        "cc0",
        "cc-by",
        "cc-by-sa",
        "mit",
        "apache",
        "odc-by",
        "cc-by-nc",
        "cc-by-nc-sa",
        "cc-by-nc-nd",
        "research-only",
        "unknown",
    }
    for ds in REGISTRY.list_datasets():
        info = ds.info
        assert info.name
        assert info.full_name
        assert info.modality
        assert info.tasks
        assert info.download_type
        assert info.license
        assert info.license_family in allowed_license_families


def test_explicitly_unknown_dataset_license_takes_precedence():
    from eyedatahub.core.dataset import classify_license

    assert classify_license("Unknown — needs check (article CC BY-NC-ND)") == "unknown"
    assert classify_license("Academic request / Unknown") == "unknown"
    assert classify_license("ODC-BY 1.0 (Open Data Commons Attribution)") == "odc-by"


def test_targeted_source_metadata_corrections(monkeypatch, tmp_path):
    expected = {
        "airogs": ("CC BY-NC-ND 4.0", "cc-by-nc-nd"),
        "oct_cirrus": (
            "Research only: research and educational use; commercialization "
            "and redistribution prohibited",
            "research-only",
        ),
        "corn_pro": ("CC BY 4.0", "cc-by"),
        "justraigs": ("CC BY-NC-ND 4.0", "cc-by-nc-nd"),
        "oct5k": ("CC0 1.0", "cc0"),
        "oimhs": ("CC0 1.0", "cc0"),
        "mario": ("CC BY 4.0", "cc-by"),
        "ophthalwechat": ("CC BY 4.0 for the deposited Figshare files", "cc-by"),
        "tear_meniscus": ("CC BY 4.0", "cc-by"),
        "migs_video": ("CC BY 4.0", "cc-by"),
        "perg_ioba": (
            "ODC-BY 1.0 (Open Data Commons Attribution)",
            "odc-by",
        ),
    }
    for slug, (license_text, family) in expected.items():
        info = REGISTRY.get_dataset(slug).info
        assert info.license == license_text
        assert info.license_family == family

    assert "10.1109/TMI.2022.3156906" in REGISTRY.get_dataset("corn1500").info.citation
    assert "10.13026/d24m-w054" in REGISTRY.get_dataset("perg_ioba").info.citation
    assert REGISTRY.get_dataset("jsiec").info.num_samples == 1000
    assert REGISTRY.get_dataset("nehut").info.classes == ["Normal", "Drusen", "CNV"]
    assert REGISTRY.get_dataset("duke_rpedc").info.num_samples == 384

    migs = REGISTRY.get_dataset("migs_video")
    assert migs.info.num_samples == 186
    assert migs.info.item_count_unit == "videos"
    assert migs.info.dataset_doi == "10.5281/zenodo.19438128"
    assert migs.info.associated_publication_doi == "10.1038/s41597-026-07535-2"
    assert migs.info.access_friction == "anonymous_direct"
    assert migs.info.acquisition_support == "transfer_tested_partial"

    calls = []
    monkeypatch.setattr(
        "eyedatahub.datasets.community_2026.download_zenodo",
        lambda record_id, destination, extract: calls.append(
            (record_id, Path(destination), extract)
        ),
    )
    migs.download(tmp_path)
    assert calls == [("19438128", tmp_path / "migs_video", False)]


def test_literature_refresh_records_are_registered():
    expected = {
        "agar300",
        "drive",
        "hei_med",
        "dridb",
        "eyeq",
        "real_fundus",
        "fiqs",
        "octa_macula_coronal",
        "fang_sbsdi_oct",
        "duke_amd_chiu",
        "maetschke_glaucoma_oct",
        "ochid",
        "thoct1800",
        "vietai_retinal_disease",
    }
    assert expected <= set(REGISTRY.names())


def test_corrected_oct_loaders_follow_released_layouts(tmp_path):
    cirrus_root = tmp_path / "oct_cirrus" / "AMD"
    cirrus_root.mkdir(parents=True)
    for index in range(21):
        (cirrus_root / f"scan_{index:02d}.tif").touch()
    dme_scan = tmp_path / "oct_cirrus" / "DME" / "scan_00.tif"
    dme_scan.parent.mkdir(parents=True)
    dme_scan.touch()
    cirrus = REGISTRY.get_dataset("oct_cirrus")
    assert cirrus.is_downloaded(tmp_path)
    cirrus_samples = cirrus.load(tmp_path)
    assert len(cirrus_samples) == 22
    assert {sample.label for sample in cirrus_samples} == {0, 1}
    assert len({sample.sample_id for sample in cirrus_samples}) == 22

    rpedc_root = tmp_path / "duke_rpedc"
    amd = rpedc_root / "AMD" / "Farsiu_Ophthalmology_2013_AMD_Subject_1.mat"
    normal = (
        rpedc_root
        / "Normal"
        / "Farsiu_Ophthalmology_2013_Normal_Subject_2.mat"
    )
    amd.parent.mkdir(parents=True)
    normal.parent.mkdir(parents=True)
    amd.touch()
    normal.touch()
    rpedc_samples = REGISTRY.get_dataset("duke_rpedc").load(tmp_path)
    assert len(rpedc_samples) == 2
    assert {sample.label for sample in rpedc_samples} == {0, 1}


def test_jsiec_loader_handles_official_wrapper_and_extensions(tmp_path):
    root = tmp_path / "jsiec" / "1000images"
    normal = root / "0.0.Normal" / "normal.JPG"
    myopia = root / "9.Pathological myopia" / "myopia.tif"
    normal.parent.mkdir(parents=True)
    myopia.parent.mkdir(parents=True)
    normal.touch()
    myopia.touch()
    samples = REGISTRY.get_dataset("jsiec").load(tmp_path)
    assert len(samples) == 2
    assert {sample.label for sample in samples} == {0, 38}
    assert len({sample.sample_id for sample in samples}) == 2


def test_nehut_loader_uses_official_csv_columns(tmp_path):
    root = tmp_path / "nehut"
    image = root / "CNV" / "scan_1.jpg"
    image.parent.mkdir(parents=True)
    image.touch()
    (root / "data_information.csv").write_text(
        "Patient ID,Class,Eye,B-scan,Label,Directory\n"
        "P001,CNV,R,1,CNV,CNV\\scan_1.jpg\n",
        encoding="utf-8",
    )
    samples = REGISTRY.get_dataset("nehut").load(tmp_path)
    assert len(samples) == 1
    assert samples[0].image_path == str(image)
    assert samples[0].label == 2
    assert samples[0].sample_id == "CNV_scan_1"


def test_registry_validation_and_duplicate_protection():
    REGISTRY.validate()

    from eyedatahub.datasets.registry import DatasetRegistry

    local_registry = DatasetRegistry()
    dataset = REGISTRY.get_dataset("stare")
    local_registry.register(dataset)
    with pytest.raises(ValueError, match="Duplicate dataset slug 'stare'"):
        local_registry.register(dataset)


def test_octdl_uses_canonical_mendeley_v4_record():
    info = REGISTRY.get_dataset("octdl").info
    assert info.download_type == "mendeley"
    assert info.download_url == "https://data.mendeley.com/datasets/sncdhf53xc/4"


def test_base_sentinel_expands_user():
    ds = REGISTRY.get_dataset("chase_db1")
    sentinel = ds.sentinel_path("~/.eyedatahub/data")
    assert sentinel.is_absolute()
    assert str(sentinel).startswith(str(Path.home()))


def test_dryad_backend_resolves_latest_version(monkeypatch, tmp_path):
    from eyedatahub.datasets import download_utils

    class FakeResponse:
        def __init__(self, payload):
            self.payload = payload
            self.status_code = 200

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
        if url.endswith("/versions/1"):
            return FakeResponse(
                {"_links": {"stash:files": {"href": "/api/v2/versions/1/files"}}}
            )
        return FakeResponse(
            {
                "_links": {},
                "_embedded": {
                    "stash:files": [
                        {
                            "path": "nested/data.csv",
                            "_links": {
                                "stash:download": {
                                    "href": "/api/v2/files/2/download"
                                }
                            },
                        }
                    ]
                },
            }
        )

    def fake_download_file(url, dest_path, desc=None, headers=None):
        assert headers == {"Authorization": "Bearer test-token"}
        destination = Path(dest_path)
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text("value\n1\n", encoding="utf-8")
        return destination

    monkeypatch.setattr(download_utils.requests, "get", fake_get)
    monkeypatch.setattr(download_utils, "download_file", fake_download_file)

    paths = download_utils.download_dryad(
        "10.5061/dryad.example",
        tmp_path,
        extract=False,
        token="test-token",
    )
    assert paths == [tmp_path / "nested" / "data.csv"]
    assert paths[0].read_text(encoding="utf-8") == "value\n1\n"


def test_mendeley_backend_uses_public_v4_api(monkeypatch, tmp_path):
    from eyedatahub.datasets import download_utils

    class FakeResponse:
        status_code = 200

        def json(self):
            return [
                {
                    "id": "file-1",
                    "filename": "octdl.zip",
                    "content_details": {
                        "download_url": "https://download.example/octdl.zip"
                    },
                }
            ]

        def raise_for_status(self):
            return None

    calls = []

    def fake_get(url, headers, params, timeout):
        calls.append((url, headers, params, timeout))
        return FakeResponse()

    def fake_download_file(url, dest_path, desc=None):
        destination = Path(dest_path)
        destination.write_bytes(b"not-an-archive")
        return destination

    monkeypatch.setattr(download_utils.requests, "get", fake_get)
    monkeypatch.setattr(download_utils, "download_file", fake_download_file)

    paths = download_utils.download_mendeley(
        "sncdhf53xc", 4, tmp_path, extract=False
    )

    assert paths == [tmp_path / "octdl.zip"]
    assert calls[0][0] == (
        "https://api.data.mendeley.com/datasets/publics/sncdhf53xc/files"
    )
    assert calls[0][2] == {"version": 4, "$start": 0, "$limit": 100}
    assert calls[0][1]["Accept"] == (
        "application/vnd.mendeley-public-dataset.1+json"
    )


def test_cli_show_json_and_copy_python():
    runner = CliRunner()

    json_result = runner.invoke(main, ["show", "airogs", "--json"])
    assert json_result.exit_code == 0
    assert '"name": "airogs"' in json_result.output

    copy_result = runner.invoke(main, ["show", "airogs", "--copy", "python"])
    assert copy_result.exit_code == 0
    assert "Path('~/.eyedatahub/data').expanduser()" in copy_result.output
    assert "preflight_dataset(ds, data_dir)" in copy_result.output
    assert "acquire_dataset(ds, data_dir)" in copy_result.output


def test_modality_alias_resolution():
    # Contained modalities are searchable, including resources whose primary
    # category differs from a contained modality.
    assert len(_resolve_datasets("uwf")) == 11
    assert len(_resolve_datasets("uwf_fundus")) == 11
    assert len(_resolve_datasets("octa")) == 10
    assert len(_resolve_datasets("ivcm")) == 6
    assert len(_resolve_datasets("external_eye")) == 21
    assert len(_resolve_datasets("eyelid")) == 21
    assert len(_resolve_datasets("surgical")) == 16
    assert len(_resolve_datasets("aoslo")) == 2
    assert len(_resolve_datasets("cell_microscopy")) == 2
    assert len(_resolve_datasets("genomics")) == 32
    assert len(_resolve_datasets("gaze")) == 16
    assert len(_resolve_datasets("pupil")) == 16
    assert len(_resolve_datasets("iris")) == 7
    assert len(_resolve_datasets("ocular_biometrics")) == 7


def test_mcp_python_snippet_expands_user():
    from eyedatahub.agent.mcp_server import call_tool

    payload = call_tool("eyedatahub.get_dataset", {"name": "airogs"})
    snippet = payload["content"]["snippets"]["python"]
    assert "Path('~/.eyedatahub/data').expanduser()" in snippet
    assert "preflight_dataset(ds, data_dir)" in snippet
    assert "acquire_dataset(ds, data_dir)" in snippet


def test_url_audit_report_has_reproducibility_metadata():
    report = json.loads(Path("hub/audit/url_report.json").read_text(encoding="utf-8"))
    assert report["metadata"]["package"] == "eyedatahub"
    assert report["metadata"]["package_version"]
    assert report["metadata"]["generated_at"]
    assert report["metadata"]["timeout_seconds"] == 30
    assert report["metadata"]["concurrency"] == 8
    assert "ok" in report["metadata"]["status_definitions"]
    assert report["summary"]["total"] == len(report["findings"])
    audited = {item["name"] for item in report["findings"]}
    assert audited <= set(REGISTRY.names())


def test_discovery_refresh_decision_log_matches_registry():
    log = json.loads(
        Path("hub/audit/first_release_discovery_2026.json").read_text(encoding="utf-8")
    )
    assert log["metadata"]["working_record_count_before_final_audit"] == 209
    assert log["metadata"]["records_identified_in_final_audit"] == 30
    assert log["metadata"]["draft_records_corrected_before_release"] == 2
    assert log["metadata"]["first_release_registry_count"] == 239
    assert log["metadata"]["literature_refresh_records_added"] == 14
    assert log["metadata"]["final_registry_count"] == 251

    dryad_summary = json.loads(
        Path("hub/audit/dryad_discovery_decisions_2026-08-01_summary.json").read_text(
            encoding="utf-8"
        )
    )
    assert dryad_summary["total_unique_api_results"] == 722
    assert dryad_summary["final_decision_counts"]["included_new_record"] == 135
    repository_summary = json.loads(
        Path("hub/audit/repository_screening_summary_2026-08-02.json").read_text(
            encoding="utf-8"
        )
    )
    assert (
        251
        + dryad_summary["final_decision_counts"]["included_new_record"]
        - len(CATALOG_SCOPE_EXCLUSIONS)
        + repository_summary["overall_counts"]["included_new_record"]
        == EXPECTED_DATASET_COUNT
    )
    included = {item["slug"] for item in log["included"]}
    assert len(included) == 30
    assert included <= set(REGISTRY.names()) | set(CATALOG_SCOPE_EXCLUSIONS)
    assert {item["slug"] for item in log["corrected"]} == {"mmrdr", "octdl"}
