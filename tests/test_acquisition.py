import csv
import json
from pathlib import Path
from types import SimpleNamespace

from click.testing import CliRunner

from eyedatahub.acquisition import (
    EXIT_INVALID_REQUEST,
    EXIT_MANUAL_BLOCKED,
    EXIT_SUCCESS,
    EXIT_TRANSFER_FAILED,
    MANIFEST_FILENAME,
    acquire_dataset,
    preflight_dataset,
)
from eyedatahub.catalog import citation_payload, search_datasets
from eyedatahub.cli import main
from eyedatahub.core.dataset import DatasetInfo, EyeDataHubDataset
from eyedatahub.core.metadata import (
    ACCESS_FRICTION_VALUES,
    ACQUISITION_SUPPORT_VALUES,
    AVAILABILITY_STATUS_VALUES,
    BOOL_OR_UNKNOWN_FIELDS,
)
from eyedatahub.datasets.platform_2026 import PlatformDiscoveryDataset
from eyedatahub.datasets.registry import REGISTRY


class FakeDataset(EyeDataHubDataset):
    def __init__(self, *, name="fake_direct", mode="success", **metadata):
        self._SUBDIR = name
        self.mode = mode
        defaults = dict(
            name=name,
            full_name="Synthetic acquisition fixture",
            description="Local test fixture; no network access.",
            modality="fundus",
            modalities=["fundus"],
            tasks=["classification"],
            num_samples=1,
            splits=["all"],
            download_type="direct",
            download_url="https://example.test/dataset.zip",
            license="CC BY 4.0",
            source_terms="CC BY 4.0",
            terms_scope="dataset_files",
            terms_evidence_url="https://example.test/terms",
            access_friction="anonymous_direct",
            availability_status="available",
            acquisition_support="loader_implemented_not_live_tested",
            requires_registration=False,
            requires_authentication=False,
            requires_api_token=False,
            requires_clickthrough=False,
            requires_manual_approval=False,
            requires_data_use_agreement=False,
            requires_author_contact=False,
            requires_payment=False,
            size_gb=None,
        )
        defaults.update(metadata)
        self._info = DatasetInfo(**defaults)
        self.download_calls = 0

    @property
    def info(self):
        return self._info

    def is_downloaded(self, data_dir):
        return (Path(data_dir) / self._SUBDIR / "payload.bin").exists()

    def download(self, data_dir):
        self.download_calls += 1
        if self.mode == "interrupt":
            raise KeyboardInterrupt()
        if self.mode == "fail":
            raise RuntimeError("simulated transfer failure")
        destination = Path(data_dir) / self._SUBDIR
        destination.mkdir(parents=True, exist_ok=True)
        (destination / "payload.bin").write_bytes(b"fixture")

    def load(self, data_dir, split="test"):
        return []


def test_every_record_has_independent_access_and_automation_dimensions():
    records = REGISTRY.list_datasets()
    assert len(records) == 475
    for dataset in records:
        info = dataset.info
        assert info.access_friction in ACCESS_FRICTION_VALUES
        assert info.acquisition_support in ACQUISITION_SUPPORT_VALUES
        assert info.availability_status in AVAILABILITY_STATUS_VALUES
        for field in BOOL_OR_UNKNOWN_FIELDS:
            assert getattr(info, field) in {True, False, None}


def test_manual_or_authorized_routes_are_never_reported_as_automated():
    restricted = {
        "controlled_or_manual",
        "author_contact",
        "model_to_data_or_secure_environment",
    }
    for dataset in REGISTRY.list_datasets():
        if dataset.info.access_friction in restricted:
            assert dataset.info.acquisition_support == "manual_access_blocked"


def test_dry_run_is_side_effect_free(tmp_path):
    dataset = FakeDataset()
    target = tmp_path / "not-created"
    result = acquire_dataset(dataset, target, dry_run=True)
    assert result.exit_code == EXIT_SUCCESS
    assert result.transfer_started is False
    assert result.preflight["terms_accepted_by_eyedatahub"] is False
    assert result.preflight["source_term_flags"]["attribution_condition_recorded"] is True
    assert any("attribution" in warning.lower() for warning in result.warnings)
    assert not target.exists()
    assert dataset.download_calls == 0


def test_manual_route_is_blocked_without_invoking_loader(tmp_path):
    dataset = FakeDataset(
        name="fake_manual",
        access_friction="controlled_or_manual",
        acquisition_support="manual_access_blocked",
        requires_registration=True,
        requires_authentication=True,
        requires_clickthrough=True,
        requires_manual_approval=True,
        requires_data_use_agreement=True,
    )
    result = acquire_dataset(dataset, tmp_path)
    assert result.status == "manual_access_blocked"
    assert result.exit_code == EXIT_MANUAL_BLOCKED
    assert result.transfer_started is False
    assert dataset.download_calls == 0


def test_unknown_terms_produce_preflight_warning(tmp_path):
    dataset = FakeDataset(
        name="fake_unknown_terms",
        license="Unknown; no dataset terms identified",
        source_terms="Unknown; no dataset terms identified",
        terms_scope="unknown",
    )
    plan = preflight_dataset(dataset, tmp_path)
    assert any("unknown" in warning.lower() for warning in plan["warnings"])
    assert plan["terms_accepted_by_eyedatahub"] is False


def test_successful_acquisition_writes_manifest_and_is_idempotent(tmp_path):
    dataset = FakeDataset()
    first = acquire_dataset(dataset, tmp_path)
    assert first.status == "completed"
    assert first.transfer_started is True
    assert dataset.download_calls == 1
    manifest = json.loads(Path(first.manifest_path).read_text(encoding="utf-8"))
    assert manifest["record_id"] == "fake_direct"
    assert manifest["complete_or_partial"] == "complete"
    assert manifest["terms_scope"] == "dataset_files"
    assert manifest["third_party_data_redistributed_by_eyedatahub"] is False
    assert manifest["acquired_files"][0]["path"] == "payload.bin"
    assert manifest["acquired_files"][0]["sha256"]

    second = acquire_dataset(dataset, tmp_path)
    assert second.status == "already_present"
    assert second.transfer_started is False
    assert dataset.download_calls == 1
    assert (tmp_path / "fake_direct" / MANIFEST_FILENAME).exists()


def test_interrupted_transfer_has_stable_failure_result(tmp_path):
    result = acquire_dataset(FakeDataset(mode="interrupt"), tmp_path)
    assert result.status == "interrupted"
    assert result.exit_code == EXIT_TRANSFER_FAILED
    assert result.transfer_started is True
    assert not (tmp_path / "fake_direct" / ".download_complete").exists()


def test_loader_exception_has_stable_failure_result(tmp_path):
    result = acquire_dataset(FakeDataset(mode="fail"), tmp_path)
    assert result.status == "failed"
    assert result.error_type == "RuntimeError"
    assert result.exit_code == EXIT_TRANSFER_FAILED


def test_invalid_destination_is_reported_without_transfer(tmp_path):
    destination = tmp_path / "file-not-directory"
    destination.write_text("fixture", encoding="utf-8")
    dataset = FakeDataset()
    result = acquire_dataset(dataset, destination)
    assert result.status == "invalid_destination"
    assert result.exit_code == EXIT_INVALID_REQUEST
    assert dataset.download_calls == 0


def test_insufficient_disk_space_blocks_before_transfer(monkeypatch, tmp_path):
    dataset = FakeDataset(size_gb=1.0)
    monkeypatch.setattr("eyedatahub.acquisition.shutil.disk_usage", lambda _: SimpleNamespace(free=1))
    result = acquire_dataset(dataset, tmp_path)
    assert result.status == "insufficient_disk_space"
    assert result.exit_code == EXIT_INVALID_REQUEST
    assert dataset.download_calls == 0


def test_cli_failure_json_is_valid_and_contains_no_secret(monkeypatch, tmp_path):
    monkeypatch.setenv("KAGGLE_USERNAME", "private-user")
    monkeypatch.setenv("KAGGLE_KEY", "private-secret")
    runner = CliRunner()
    result = runner.invoke(
        main,
        ["download", "corn_pro", "--data-dir", str(tmp_path), "--dry-run", "--json"],
    )
    assert result.exit_code == EXIT_MANUAL_BLOCKED
    payload = json.loads(result.output)
    assert payload["results"][0]["status"] == "manual_access_blocked"
    assert payload["results"][0]["preflight"]["terms_accepted_by_eyedatahub"] is False
    assert "private-user" not in result.output
    assert "private-secret" not in result.output


def test_cli_rejects_invalid_access_category():
    result = CliRunner().invoke(main, ["search", "--access", "not-a-category"])
    assert result.exit_code == 2
    assert "Invalid value for '--access'" in result.output


def test_expected_results_fixture_is_external_to_implementation():
    fixture = Path("tests/fixtures/expected_query_results.csv")
    with fixture.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    for row in rows:
        results = search_datasets(
            REGISTRY.list_datasets(),
            query=row["query"] or None,
            modalities=tuple(filter(None, row["modalities"].split("|"))),
            tasks=tuple(filter(None, row["tasks"].split("|"))),
            access_friction=tuple(filter(None, row["access_friction"].split("|"))),
            acquisition_support=tuple(filter(None, row["acquisition_support"].split("|"))),
        )
        observed = [dataset.info.name for dataset in results]
        expected = list(filter(None, row["expected_record_ids"].split("|")))
        assert observed == expected, row["case_id"]


def test_oct_alias_and_multimodal_containment_are_consistent():
    oct_short = search_datasets(REGISTRY.list_datasets(), modalities=["oct"])
    oct_long = search_datasets(
        REGISTRY.list_datasets(), modalities=["optical coherence tomography"]
    )
    assert [item.info.name for item in oct_short] == [item.info.name for item in oct_long]
    assert any(item.info.primary_category == "multimodal" for item in oct_short)
    gamma = REGISTRY.get_dataset("gamma").info
    assert {"fundus", "oct"}.issubset(gamma.modalities)
    assert gamma.name in {item.info.name for item in oct_short}
    fundus = search_datasets(REGISTRY.list_datasets(), modalities=["fundus"])
    assert gamma.name in {item.info.name for item in fundus}


def test_multimodal_records_name_component_modalities():
    for dataset in REGISTRY.list_datasets():
        info = dataset.info
        if info.primary_category == "multimodal":
            assert info.modalities, info.name
            assert "multimodal" not in info.modalities, info.name


def test_multimodal_component_tags_match_representative_source_records():
    expected = {
        "mm_retinal_reason": {"fundus", "fundus_angiography", "oct", "text"},
        "fairvlmed": {"fundus", "visual_field", "text", "tabular"},
        "ophthalvqa": {
            "fundus",
            "fundus_angiography",
            "oct",
            "ocular_ultrasound",
            "external_eye",
            "text",
        },
        "x_pcr": {
            "fundus",
            "fundus_angiography",
            "oct",
            "external_eye",
            "retcam",
            "text",
        },
        "lmod_plus": {
            "fundus",
            "oct",
            "external_eye",
            "surgical_video",
            "text",
            "tabular",
        },
    }
    for name, component_tags in expected.items():
        assert component_tags == set(REGISTRY.get_dataset(name).info.modalities)


def test_search_order_is_deterministic_and_missing_values_do_not_crash():
    first = search_datasets(REGISTRY.list_datasets(), tasks=["segmentation"])
    second = search_datasets(reversed(REGISTRY.list_datasets()), tasks=["segmentation"])
    first_ids = [item.info.name for item in first]
    assert first_ids == sorted(first_ids)
    assert first_ids == [item.info.name for item in second]


def test_dataset_and_article_citations_remain_separate():
    payload = citation_payload(REGISTRY.get_dataset("rvo_me").info)
    assert payload["dataset"]["doi"] == "10.6084/m9.figshare.29804435.v1"
    assert payload["dataset"]["doi"] != payload["associated_article"]["doi"]
    assert payload["software"]["version"] == "0.6.0"


def test_explicit_dataset_doi_is_not_reclassified_as_an_article_doi():
    info = REGISTRY.get_dataset("corn_collection").info
    assert info.dataset_doi == "10.5281/zenodo.19689814"
    assert info.associated_publication_doi is None


def test_platform_wrapper_recognizes_real_files_without_sentinel(tmp_path):
    dataset = PlatformDiscoveryDataset(
        {
            "name": "fixture_platform",
            "full_name": "Fixture platform record",
            "description": "Fixture",
            "modality": "fundus",
            "tasks": ["classification"],
            "num_samples": 1,
            "download_type": "figshare",
            "download_url": "https://doi.org/10.6084/m9.figshare.1",
            "license": "CC BY 4.0",
        }
    )
    target = tmp_path / "fixture_platform"
    target.mkdir()
    (target / "file.bin").write_bytes(b"data")
    assert dataset.is_downloaded(tmp_path)
