"""Machine-readable plans for bounded agent workflows.

The planner is intentionally side-effect free. It selects catalog records,
explains why they were selected, and returns exact inspection and download
commands. It never downloads data, accepts upstream terms, or starts training.
Those actions remain explicit decisions for the user or the calling agent.
"""
from __future__ import annotations

import hashlib
import json
import re
from typing import Iterable

from eyedatahub.core.dataset import license_matches_filter


PLAN_SCHEMA_VERSION = "1.0"

_DEFAULT_GAPS = ("diabetic_retinopathy", "glaucoma", "amd")
_GAP_ALIASES = {
    "diabetic_retinopathy": {"diabetic_retinopathy", "dr"},
    "glaucoma": {"glaucoma"},
    "amd": {"amd", "age_related_macular_degeneration"},
    "myopia": {"myopia", "high_myopia", "pathological_myopia"},
    "rop": {"rop", "retinopathy_of_prematurity", "pediatric"},
    "cataract": {"cataract"},
    "retinal_vessels": {
        "artery",
        "artery_vein",
        "retinal_vessels",
        "vessel",
        "vessel_segmentation",
        "vessels",
    },
}
_CREDENTIAL_BACKENDS = {
    "dataverse",
    "gdrive",
    "github",
    "huggingface",
    "kaggle",
    "physionet",
    "synapse",
}
_DERIVATIVE_TAGS = {"aggregator", "augmented", "derivative", "synthetic"}


def _normalize_gap(value: str) -> str:
    normalized = re.sub(r"[^a-z0-9]+", "_", value.strip().lower()).strip("_")
    return normalized or "unspecified"


def _normalized_gaps(gaps: Iterable[str] | None) -> list[str]:
    values = [_normalize_gap(value) for value in (gaps or _DEFAULT_GAPS)]
    return list(dict.fromkeys(values))


def _tags(dataset) -> set[str]:
    return {str(tag).strip().lower() for tag in (dataset.info.tags or [])}


def _is_derivative(dataset) -> bool:
    tags = _tags(dataset)
    return any(
        tag in _DERIVATIVE_TAGS
        or tag.startswith("derivative_of_")
        or tag.startswith("duplicate_of_")
        for tag in tags
    )


def access_state(dataset) -> str:
    info = dataset.info
    if info.access_friction in {
        "controlled_or_manual",
        "author_contact",
        "model_to_data_or_secure_environment",
    }:
        return "human_action_required"
    if info.access_friction == "self_service_clickthrough":
        return "user_clickthrough_required"
    if info.access_friction == "self_service_authenticated":
        return "user_authentication_required"
    if info.availability_status != "available":
        return info.availability_status
    return "explicit_download_required"


def loader_status(dataset) -> str:
    """Report whether the dataset class provides a concrete sample loader."""
    load_method = dataset.__class__.load
    code = getattr(load_method, "__code__", None)
    if code is None or "NotImplementedError" in code.co_names:
        return "metadata_only"
    return "implemented"


def _candidate_sort_key(dataset) -> tuple:
    info = dataset.info
    access_rank = 0 if info.access_friction in {
        "anonymous_direct", "self_service_authenticated", "self_service_clickthrough"
    } else 1
    unknown_count = 1 if info.num_samples is None else 0
    return (access_rank, unknown_count, -(info.num_samples or 0), info.name)


def _candidate_payload(dataset, role: str, reasons: list[str]) -> dict:
    info = dataset.info
    family = info.license_family
    status = loader_status(dataset)
    python_load = None
    if status == "implemented":
        python_load = (
            "from pathlib import Path\n"
            "from eyedatahub.datasets.registry import REGISTRY\n"
            f"dataset = REGISTRY.get_dataset('{info.name}')\n"
            "samples = dataset.load(Path('<DATA_DIR>'), split='<SPLIT>')"
        )
    return {
        "name": info.name,
        "full_name": info.full_name,
        "role": role,
        "modality": info.modality,
        "modalities": list(info.modalities),
        "tasks": list(info.tasks or []),
        "tags": list(info.tags or []),
        "reported_records": info.num_samples,
        "reported_size_gb": info.size_gb,
        "license": info.license,
        "license_family": family,
        "license_review": (
            "share_alike_interpretation_required"
            if family == "cc-by-sa"
            else "verify_current_source_terms"
        ),
        "download_type": info.download_type,
        "access_friction": info.access_friction,
        "acquisition_support": info.acquisition_support,
        "access_state": access_state(dataset),
        "loader_status": status,
        "selection_reasons": reasons,
        "commands": {
            "inspect": f"eyehub show {info.name} --json",
            "citation": f"eyehub cite {info.name} --type dataset --format bibtex",
            "preflight": f"eyehub download {info.name} --data-dir <DATA_DIR> --dry-run",
            "download_after_approval": (
                f"eyehub download {info.name} --data-dir <DATA_DIR>"
            ),
            "python_load_after_download": python_load,
        },
    }


def _matches_gap(dataset, gap: str) -> bool:
    aliases = _GAP_ALIASES.get(gap, {gap})
    return bool(_tags(dataset) & aliases)


def build_fundus_foundation_plan(
    *,
    license_type: str = "standard-no-nc",
    max_pretraining_datasets: int = 8,
    gaps: Iterable[str] | None = None,
    max_validation_per_gap: int = 3,
    include_manual: bool = False,
) -> dict:
    """Build a side-effect-free fundus foundation-model data plan.

    The result is a decision and handoff manifest, not a training benchmark.
    It can be consumed by a coding agent, the CLI, or the read-only MCP server.
    """
    if max_pretraining_datasets < 1:
        raise ValueError("max_pretraining_datasets must be at least 1")
    if max_validation_per_gap < 1:
        raise ValueError("max_validation_per_gap must be at least 1")

    from eyedatahub.datasets.registry import REGISTRY

    normalized_gaps = _normalized_gaps(gaps)
    registry = REGISTRY.list_datasets()

    fundus = [
        dataset
        for dataset in registry
        if dataset.info.modality == "fundus"
        and license_matches_filter(dataset.info.license, license_type)
    ]
    primary_candidates = [
        dataset
        for dataset in fundus
        if not _is_derivative(dataset)
        and (include_manual or dataset.info.download_type != "manual")
    ]
    primary_candidates.sort(key=_candidate_sort_key)
    pretraining_datasets = primary_candidates[:max_pretraining_datasets]
    selected_names = {dataset.info.name for dataset in pretraining_datasets}

    pretraining_pool = [
        _candidate_payload(
            dataset,
            "pretraining",
            [
                "fundus modality",
                f"matches {license_type} license filter",
                "not tagged as a derivative or duplicate",
                "ranked by known record count and stable slug",
            ],
        )
        for dataset in pretraining_datasets
    ]

    validation_by_gap: dict[str, list[dict]] = {}
    validation_candidates = [
        dataset
        for dataset in registry
        if dataset.info.name not in selected_names
        and dataset.info.modality in {"fundus", "uwf_fundus", "multimodal"}
        and "fundus" in (_tags(dataset) | {dataset.info.modality})
        and license_matches_filter(dataset.info.license, license_type)
        and not _is_derivative(dataset)
        and (include_manual or dataset.info.download_type != "manual")
    ]

    for gap in normalized_gaps:
        matches = [
            dataset
            for dataset in validation_candidates
            if _matches_gap(dataset, gap)
        ]
        matches.sort(key=_candidate_sort_key)
        chosen = matches[:max_validation_per_gap]
        validation_by_gap[gap] = [
            _candidate_payload(
                dataset,
                "gap_validation",
                [
                    f"matches gap tag {gap}",
                    "kept outside the proposed pretraining pool",
                    f"matches {license_type} license filter",
                ],
            )
            for dataset in chosen
        ]

    all_payloads = pretraining_pool + [
        item for candidates in validation_by_gap.values() for item in candidates
    ]
    acquisition_queue = []
    queued_names: set[str] = set()
    for item in all_payloads:
        if item["name"] in queued_names:
            continue
        queued_names.add(item["name"])
        acquisition_queue.append(
            {
                "name": item["name"],
                "access_state": item["access_state"],
                "inspect_command": item["commands"]["inspect"],
                "download_command": item["commands"]["download_after_approval"],
            }
        )
    known_records = sum(item["reported_records"] or 0 for item in pretraining_pool)
    known_size_gb = sum(item["reported_size_gb"] or 0 for item in pretraining_pool)

    identity = {
        "license_type": license_type,
        "max_pretraining_datasets": max_pretraining_datasets,
        "gaps": normalized_gaps,
        "max_validation_per_gap": max_validation_per_gap,
        "include_manual": include_manual,
        "pretraining": [item["name"] for item in pretraining_pool],
        "validation": {
            gap: [item["name"] for item in items]
            for gap, items in validation_by_gap.items()
        },
    }
    plan_id = hashlib.sha256(
        json.dumps(identity, sort_keys=True).encode("utf-8")
    ).hexdigest()[:12]

    return {
        "schema_version": PLAN_SCHEMA_VERSION,
        "plan_id": f"fundus-foundation-{plan_id}",
        "workflow": "fundus_foundation_model",
        "status": "planning_only",
        "side_effects": {
            "downloads_started": False,
            "access_terms_accepted": False,
            "training_started": False,
        },
        "catalog": {
            "record_count": len(registry),
            "source_of_truth": "eyedatahub.datasets.registry.REGISTRY",
        },
        "selection_policy": {
            "modality": "fundus",
            "license_type": license_type,
            "exclude_derivatives_and_duplicates": True,
            "include_manual_access": include_manual,
            "reported_counts_are_source_units": True,
        },
        "pretraining_pool": pretraining_pool,
        "pretraining_summary": {
            "dataset_count": len(pretraining_pool),
            "known_reported_records": known_records,
            "known_reported_size_gb": round(known_size_gb, 3),
        },
        "gap_validation": validation_by_gap,
        "acquisition_queue": acquisition_queue,
        "agent_loop": [
            {
                "step": "inspect",
                "action": "Review source terms, provenance, and access state for every candidate.",
            },
            {
                "step": "approve",
                "action": "Obtain explicit user approval before running any download command.",
            },
            {
                "step": "acquire",
                "action": "Run approved commands individually and preserve source-specific dataset boundaries.",
            },
            {
                "step": "train",
                "action": "Pass local image paths to a user-selected training framework. EyeDataHub does not prescribe a model or optimizer.",
            },
            {
                "step": "evaluate",
                "action": "Report results by held-out source and disease gap, not only as one pooled score.",
            },
            {
                "step": "expand",
                "action": "Re-run this planner with new --gap values when evaluation reveals weak coverage.",
            },
        ],
        "trainer_handoff": {
            "framework": "user_supplied",
            "minimum_manifest_fields": [
                "dataset_name",
                "image_path",
                "source_split",
                "license_family",
            ],
            "preserve_source_boundaries": True,
            "candidate_loader_status_included": True,
            "training_implementation_included": False,
        },
        "warnings": [
            "EyeDataHub source-term categories are not legal advice. Verify current source documentation before use.",
            "Authentication, click-through, manual approval, and automation support are represented independently.",
            "Candidates marked metadata_only do not yet have a standardized sample loader and may require a contributed loader or source-specific parsing.",
            "Catalog inclusion is not a quality rating. Review labels, population coverage, duplicates, and leakage risk before training.",
            "The planner never downloads data or starts model training.",
        ],
    }
