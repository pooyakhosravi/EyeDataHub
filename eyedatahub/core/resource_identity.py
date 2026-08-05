"""Controlled resource roles and dataset-family identifiers.

EyeDataHub indexes current data products, not necessarily independent cohorts.
This module separates three questions that must not be conflated:

* whether a record is the current canonical release;
* what kind of data product the record represents; and
* which closely related records belong to the same dataset family.

Earlier releases and unmodified alternate deposits remain documented as source
history, but are not exposed as separate catalog records.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, FrozenSet

from eyedatahub.core.relationships import RELATIONSHIP_EVIDENCE


RESOURCE_ROLES = frozenset(
    {
        "current_dataset",
        "derivative_dataset",
        "annotation_layer",
        "component_dataset",
        "collection",
        "extension_dataset",
        "task_view",
    }
)


RESOURCE_ROLE_DEFINITIONS = {
    "current_dataset": (
        "A current cataloged data product without a more specific structural role."
    ),
    "derivative_dataset": (
        "A distinct data product that reuses one or more cataloged resources and "
        "adds processing, representations, synthesis, aggregation, or benchmark "
        "structure."
    ),
    "annotation_layer": (
        "A data product whose principal addition is labels, masks, reports, "
        "questions, reasoning records, or other annotations for existing data."
    ),
    "component_dataset": (
        "A separately named and citable component of a cataloged collection."
    ),
    "collection": (
        "A combined deposit or portal that exposes multiple named component datasets."
    ),
    "extension_dataset": (
        "A current data product that adds data to an earlier related resource without "
        "being documented as a replacement of the same release."
    ),
    "task_view": (
        "A separately indexed task or label view over the same documented data payload."
    ),
}


# Annotation-focused resources are reviewed manually because the graph alone
# cannot distinguish a new annotation layer from a transformed or composite
# derivative. Every identifier below is supported by its record description and
# the evidence in ``RELATIONSHIP_EVIDENCE``.
ANNOTATION_RECORD_IDS: FrozenSet[str] = frozenset(
    {
        "aptos_arcade_onh_masks",
        "cadis",
        "cataract101_extended_labels",
        "dme_vqa",
        "dme_vqa_logical",
        "eyeq",
        "fundus_report_dataset",
        "glaucoma_expert_cot_refined",
        "hrf_seg_plus",
        "insegcat",
        "itec_iris_pupil",
        "lmod_cataract_1k_cot",
        "mendeley_utilizing_responsive_web_portal_studying_disc",
        "mm_retinal_reason",
        "refuge1_multirater",
        "reta_benchmark",
        "rite",
    }
)


# Family membership is deliberately narrow. It groups only documented
# collection/component records and exact task views. Derivatives, extensions,
# and records with uncertain cohort overlap remain separate families.
DATASET_FAMILY_OVERRIDES: Dict[str, str] = {
    "corn_collection": "corn_collection",
    "corn1500": "corn_collection",
    "corn_pro": "corn_collection",
    "gamma": "ichallenge_gamma",
    "ichallenge_oct": "ichallenge_gamma",
    "stage_task1": "stage_2023",
    "stage_task2": "stage_2023",
    "stage_task3": "stage_2023",
}


@dataclass(frozen=True)
class RetiredCatalogRecord:
    """A source-history item intentionally omitted from the current catalog."""

    former_record_id: str
    canonical_record_id: str
    disposition: str
    evidence_url: str
    reason: str


RETIRED_CATALOG_RECORDS = (
    RetiredCatalogRecord(
        former_record_id="refuge2018",
        canonical_record_id="refuge2",
        disposition="previous_version",
        evidence_url="https://refuge.grand-challenge.org/",
        reason=(
            "REFUGE2 retains all 1,200 REFUGE 2018 images and adds 800 images; "
            "the earlier release is preserved as a previous-version link."
        ),
    ),
    RetiredCatalogRecord(
        former_record_id="glaucoma_expert_cot_raw",
        canonical_record_id="glaucoma_expert_cot_refined",
        disposition="previous_version",
        evidence_url=(
            "https://huggingface.co/datasets/yuzhench/"
            "glaucoma-expert-cot-raw-1077"
        ),
        reason=(
            "The refined release is the current corrected version; the raw release "
            "is preserved as a previous-version link."
        ),
    ),
    RetiredCatalogRecord(
        former_record_id="bidr",
        canonical_record_id="eyepacs",
        disposition="alternate_repository_copy",
        evidence_url=(
            "https://www.kaggle.com/datasets/pkdarabi/"
            "diagnosis-of-diabetic-retinopathy"
        ),
        reason=(
            "BiDR republishes the same 35,126-image EyePACS training split without "
            "a distinct annotation layer."
        ),
    ),
    RetiredCatalogRecord(
        former_record_id="dr_arranged",
        canonical_record_id="eyepacs",
        disposition="alternate_repository_copy",
        evidence_url="https://tianchi.aliyun.com/dataset/93926",
        reason=(
            "The arranged Tianchi record republishes the same 35,126-image EyePACS "
            "training split without a distinct annotation layer."
        ),
    ),
)


_OUTGOING_RELATIONSHIP_TYPES: Dict[str, FrozenSet[str]] = {}
for _edge in RELATIONSHIP_EVIDENCE:
    _OUTGOING_RELATIONSHIP_TYPES.setdefault(_edge.source_record_id, set()).add(
        _edge.relationship_type
    )
_OUTGOING_RELATIONSHIP_TYPES = {
    record_id: frozenset(values)
    for record_id, values in _OUTGOING_RELATIONSHIP_TYPES.items()
}


def resource_role_for(record_id: str) -> str:
    """Return the mutually exclusive reviewed role for a current record."""

    relationship_types = _OUTGOING_RELATIONSHIP_TYPES.get(record_id, frozenset())
    if record_id in ANNOTATION_RECORD_IDS:
        return "annotation_layer"
    if "component_of" in relationship_types:
        return "component_dataset"
    if "has_component" in relationship_types:
        return "collection"
    if "derived_from" in relationship_types:
        return "derivative_dataset"
    if "extension_of" in relationship_types:
        return "extension_dataset"
    if record_id in {"stage_task1", "stage_task2", "stage_task3"}:
        return "task_view"
    return "current_dataset"


def dataset_family_for(record_id: str) -> str:
    """Return the narrow dataset-family identifier used for headline counting."""

    return DATASET_FAMILY_OVERRIDES.get(record_id, record_id)


def identity_fields_for(record_id: str) -> Dict[str, object]:
    """Return stable identity fields added to machine-readable catalog exports."""

    role = resource_role_for(record_id)
    return {
        "resource_role": role,
        "resource_role_definition": RESOURCE_ROLE_DEFINITIONS[role],
        "dataset_family_id": dataset_family_for(record_id),
        "current_catalog_record": True,
    }
