"""Build the reviewed August 2026 Dryad catalog module.

The three input batches are human-reviewed outputs derived from the official
Dryad API search snapshot and current-version file listings. This script
performs deterministic source-consistency checks before writing the runtime
module and a merged machine-readable review artifact.
"""

from __future__ import annotations

import json
import pprint
import re
from dataclasses import fields as dataclass_fields
from pathlib import Path
from typing import Any

from eyedatahub.core.dataset import DatasetInfo
from eyedatahub.core.quantities import (
    EVIDENCE_BASES,
    EXACTNESS_VALUES,
    PUBLIC_QUANTITY_FIELDS,
    QUANTITY_UNITS,
)
from eyedatahub.datasets.registry import REGISTRY


ROOT = Path(__file__).resolve().parents[2]
AUDIT_DIR = ROOT / "hub" / "audit"
REQUIRED_INPUT_PATHS = tuple(
    AUDIT_DIR / f"dryad_catalog_records_{batch}_2026-08-01.json"
    for batch in "abc"
)
OPTIONAL_INPUT_PATHS = (
    AUDIT_DIR / "dryad_catalog_records_deferred_2026-08-01.json",
)
SEARCH_PATH = AUDIT_DIR / "dryad_search_candidates_2026-08-01.json"
MERGED_PATH = AUDIT_DIR / "dryad_catalog_records_2026-08-01.json"
MODULE_PATH = ROOT / "eyedatahub" / "datasets" / "dryad_2026.py"

PRIMARY_CATEGORIES = frozenset(
    {
        "adaptive_optics",
        "cell_microscopy",
        "confocal",
        "corneal_topography",
        "electrophysiology",
        "external_eye",
        "eye_tracking",
        "fundus",
        "iris_biometrics",
        "multimodal",
        "oct",
        "octa",
        "omics",
        "surgical_video",
        "tabular",
        "text",
        "uwf_fundus",
        "visual_field",
    }
)
EXTRA_RECORD_FIELDS = {"source"}
DOI_URL_RE = re.compile(r"^https?://(?:dx\.)?doi\.org/", re.IGNORECASE)
QUANTITY_UNIT_NORMALIZATION = {
    "patients": "participants",
    "retinal_prosthesis_participants": "participants",
    "mouse_models": "animal_models",
    "rabbits": "experimental_animals",
}


def _load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _bare_doi(value: Any) -> Any:
    if not isinstance(value, str):
        return value
    return DOI_URL_RE.sub("", value.strip())


def _validate_quantity(record: dict[str, Any], quantity: dict[str, Any]) -> None:
    assert tuple(quantity) == PUBLIC_QUANTITY_FIELDS, (
        f"{record['name']}: quantity keys do not match the public schema"
    )
    assert quantity["unit"] in QUANTITY_UNITS, (
        f"{record['name']}: unsupported quantity unit {quantity['unit']}"
    )
    assert quantity["evidence_basis"] in EVIDENCE_BASES
    assert quantity["exactness"] in EXACTNESS_VALUES
    assert isinstance(quantity["count"], int) and quantity["count"] >= 0


def _normalize_and_validate(
    records: list[dict[str, Any]], raw_by_doi: dict[str, dict[str, Any]]
) -> list[dict[str, Any]]:
    dataset_fields = {field.name for field in dataclass_fields(DatasetInfo)}
    input_slugs = {record["name"] for record in records}
    existing_slugs = set(REGISTRY.names()) - input_slugs
    output: list[dict[str, Any]] = []
    seen_slugs: set[str] = set()
    seen_dois: set[str] = set()

    for original in sorted(records, key=lambda item: item["dataset_doi"].lower()):
        record = {
            key: value
            for key, value in original.items()
            if key in dataset_fields | EXTRA_RECORD_FIELDS
        }
        doi = _bare_doi(record["dataset_doi"]).lower()
        record["dataset_doi"] = doi
        record.setdefault("primary_category", record["modality"])
        if record["primary_category"] == "multimodal":
            record["modalities"] = [
                modality
                for modality in record.get("modalities", [])
                if modality != "multimodal"
            ]
        record["download_url"] = f"https://doi.org/{doi}"
        record["source_landing_page_url"] = record["download_url"]
        record["preferred_route_type"] = "official_repository"
        record["preferred_route_url"] = record["download_url"]
        record["canonical_resolver_url"] = record["download_url"]
        record["associated_publication_doi"] = _bare_doi(
            record.get("associated_publication_doi")
        )
        record["source"] = {"doi": doi}

        raw = raw_by_doi[doi]
        assert raw["visibility"] == "public", f"{doi}: source is not public"
        assert raw["license"] == "https://spdx.org/licenses/CC0-1.0.html", (
            f"{doi}: unexpected source terms {raw['license']}"
        )
        record["license"] = "CC0 1.0"
        record["source_terms"] = raw["license"]
        record["terms_scope"] = "dataset_files"
        record["terms_evidence_url"] = record["download_url"]
        record["resource_version"] = str(raw["version_number"])
        record["access_friction"] = "self_service_authenticated"
        record["requires_registration"] = True
        record["requires_authentication"] = True
        record["requires_api_token"] = True
        record["requires_clickthrough"] = False
        record["requires_manual_approval"] = False
        record["requires_data_use_agreement"] = False
        record["requires_author_contact"] = False
        record["requires_payment"] = False
        record["availability_status"] = "available"
        record["acquisition_support"] = "standard_platform_supported"
        record["loader_backend"] = "dryad"
        record["loader_name"] = "dryad_loader"
        record["loader_live_tested"] = False
        record["route_last_checked"] = "2026-08-01"
        record["route_check_result"] = "official_metadata_and_file_listing_checked"
        record["route_check_notes"] = (
            "Official Dryad API metadata and current-version file listing reviewed. "
            "Data files were not downloaded during catalog discovery."
        )
        record["loader_test_scope"] = "not_run"
        record["loader_test_result"] = "not_run"
        record["transfer_check_status"] = "not_run"
        if raw.get("storage_size_bytes"):
            record["size_gb"] = raw["storage_size_bytes"] / 1_000_000_000

        slug = record["name"]
        assert re.fullmatch(r"dryad_[a-z0-9_]+", slug), f"invalid slug: {slug}"
        assert slug not in existing_slugs, f"existing slug collision: {slug}"
        assert slug not in seen_slugs, f"new slug collision: {slug}"
        assert doi not in seen_dois, f"duplicate DOI: {doi}"
        assert record["modality"] in PRIMARY_CATEGORIES
        assert record["primary_category"] == record["modality"]
        assert record["modalities"]
        if record["modality"] != "multimodal":
            assert record["modality"] in record["modalities"]
        assert record["download_type"] == "dryad"
        assert record["access_friction"] == "self_service_authenticated"
        assert record["requires_authentication"] is True
        assert record["requires_api_token"] is True
        assert record["requires_manual_approval"] is False
        assert record["loader_live_tested"] is False

        quantities = record.get("reported_quantities") or []
        for quantity in quantities:
            if quantity.get("evidence_basis") == "official_deposit_abstract":
                quantity["evidence_basis"] = "official_source_description"
            quantity["unit"] = QUANTITY_UNIT_NORMALIZATION.get(
                quantity["unit"], quantity["unit"]
            )
            _validate_quantity(record, quantity)
        primary = [quantity for quantity in quantities if quantity["primary"]]
        assert len(primary) <= 1
        if primary:
            assert record["num_samples"] == primary[0]["count"]
            record["item_count_unit"] = primary[0]["unit"]
        else:
            record["num_samples"] = None
            record["item_count_unit"] = ""

        seen_slugs.add(slug)
        seen_dois.add(doi)
        output.append(record)

    return output


def build() -> tuple[Path, Path, int]:
    missing = [str(path) for path in REQUIRED_INPUT_PATHS if not path.exists()]
    if missing:
        raise FileNotFoundError("Missing reviewed input batches: " + ", ".join(missing))
    input_paths = REQUIRED_INPUT_PATHS + tuple(
        path for path in OPTIONAL_INPUT_PATHS if path.exists()
    )

    search = _load_json(SEARCH_PATH)
    raw_by_doi = {
        candidate["doi"].lower(): candidate for candidate in search["candidates"]
    }
    records = [record for path in input_paths for record in _load_json(path)]
    normalized = _normalize_and_validate(records, raw_by_doi)

    MERGED_PATH.write_text(
        json.dumps(normalized, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    literal = pprint.pformat(normalized, width=100, sort_dicts=False)
    module = f'''"""Reviewed ophthalmic Dryad records discovered on 1 August 2026.

Generated by ``python -m hub.audit.build_dryad_2026_module`` from the archived
official-API search snapshot and reviewed inclusion batches. Dataset files are
not included in this repository.
"""

from __future__ import annotations

from typing import Any

from eyedatahub.datasets.platform_2026 import PlatformDiscoveryDataset


DRYAD_DISCOVERY_RECORDS: list[dict[str, Any]] = {literal}

DRYAD_DISCOVERY_DATASETS = [
    PlatformDiscoveryDataset(record) for record in DRYAD_DISCOVERY_RECORDS
]
'''
    MODULE_PATH.write_text(module, encoding="utf-8", newline="\n")
    return MERGED_PATH, MODULE_PATH, len(normalized)


if __name__ == "__main__":
    merged_path, module_path, count = build()
    print(f"Wrote {count} records to {merged_path.relative_to(ROOT)}")
    print(f"Wrote runtime module to {module_path.relative_to(ROOT)}")
