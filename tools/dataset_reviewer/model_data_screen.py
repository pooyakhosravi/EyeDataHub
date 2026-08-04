"""Evidence-backed model-data triage for the local catalog reviewer.

This module never changes a catalog record or a saved author decision. It adds
an internal suggestion that helps the author distinguish reusable model data
from paper-supporting tables and image-derived measurements whose source images
are absent.
"""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path
from typing import Any


PRIMARY_MODALITY_CORRECTIONS = {
    "mendeley_application_machine_learning_detecting_iron_deficiency": [
        "external_eye",
        "tabular",
    ],
    "mendeley_code_manuscript_fixational_eye_movements_as": [
        "eye_tracking",
        "tabular",
    ],
    "mendeley_conjunctival_melanoma_detection_using_deep_learning": [
        "external_eye",
        "tabular",
    ],
    "mendeley_cp_anemic_conjunctival_pallor_ghana": [
        "external_eye",
        "tabular",
    ],
    "mendeley_development_deep_learning_based_system_optic": [
        "ocular_ultrasound",
        "tabular",
    ],
    "mendeley_digital_holograms_rbcs_glaucoma_patients_healthy": [
        "cell_microscopy",
        "tabular",
    ],
    "mendeley_electrooculography_eog_blink_analysis_ocular_fatigue": [
        "electrophysiology",
        "tabular",
    ],
    "mendeley_nuclear_cataract_database_biomedical_machine_learning": [
        "external_eye",
        "tabular",
    ],
    "mendeley_ocular_sebaceous_neoplasms": [
        "external_eye",
        "cell_microscopy",
        "tabular",
    ],
    "mendeley_red_lesion_localization_messidor_retinal_images": [
        "fundus",
        "tabular",
    ],
    "mendeley_retinal_blood_vessel_segmentation_rop": [
        "fundus",
        "tabular",
    ],
    "mendeley_sub_cone_visual_resolution_by_active": [
        "adaptive_optics",
        "eye_tracking",
        "tabular",
    ],
    "mendeley_two_photon_excited_fluorescence_scanning_laser": [
        "retinal_imaging",
        "tabular",
    ],
    "mendeley_vivo_cone_photoreceptor_topography_human_foveola": [
        "adaptive_optics",
        "tabular",
    ],
}


DERIVED_IMAGING_WITHOUT_SOURCE_DATA = {
    "central_retinal_vessel_trunk_oag",
    "dryad_gcc_glaucoma",
    "dryad_v9p0b",
    "mendeley_3_year_follow_up_optic_neuritis",
    "mendeley_anterior_segment_optical_coherence_tomography_angiography",
    "mendeley_comparison_retinal_choroidal_vascular_changes_via",
    "mendeley_difference_retinal_nerve_fiber_layer_thickness",
    "mendeley_microvascular_changes_poag_after_npds",
    "mendeley_peripapillary_retinal_nerve_fiber_layer_thinning",
    "mendeley_radial_peripapillary_capillary_density_as_predictive",
}


MIXED_DERIVED_MEASUREMENTS_NEED_REVIEW = {
    "dryad_crvo_vegf_tortuosity",
    "mendeley_dex_combined_ppv_pdr",
}


SPATIAL_MEASUREMENT_EXCEPTIONS = {
    "mendeley_interocular_retinal_nerve_fiber_layer_thickness",
}


INHERENTLY_TABULAR_TERMS = (
    "axial length",
    "biometr",
    "clinical record",
    "clinical outcome",
    "contrast sensitivity",
    "electrophysiolog",
    "gene expression",
    "genomic",
    "intraocular pressure",
    "iol",
    "keratometr",
    "laboratory",
    "metabolom",
    "omics",
    "perimetr",
    "psychophys",
    "questionnaire",
    "refraction",
    "refractive",
    "rna",
    "signal",
    "tear fluid",
    "topograph",
    "visual acuity",
    "visual field",
)


def _stable_mendeley_id(record: dict[str, Any]) -> str:
    values = (
        record.get("repository_record_id"),
        record.get("dataset_doi"),
        record.get("download_url"),
    )
    for value in values:
        match = re.search(r"(?:10\.17632/|datasets/)?([a-z0-9]{10})(?:[/.]|$)", str(value or ""))
        if match:
            return match.group(1)
    return ""


def load_source_evidence(repo_root: Path) -> tuple[dict[str, dict], dict[str, dict]]:
    """Load source-review summaries without loading any downloaded datasets."""

    mendeley_path = (
        repo_root / "hub" / "audit" / "mendeley_source_confirmation_2026-08-02.json"
    )
    dryad_path = repo_root / "hub" / "audit" / "dryad_model_use_review_2026-08-02.csv"

    mendeley: dict[str, dict] = {}
    if mendeley_path.exists():
        payload = json.loads(mendeley_path.read_text(encoding="utf-8"))
        for row in payload.get("records", []):
            stable_id = str(row.get("stable_id") or "")
            if stable_id:
                mendeley[stable_id] = row

    dryad: dict[str, dict] = {}
    if dryad_path.exists():
        with dryad_path.open("r", encoding="utf-8-sig", newline="") as handle:
            for row in csv.DictReader(handle):
                record_id = str(row.get("record_id") or "")
                if record_id:
                    dryad[record_id] = row
    return mendeley, dryad


def _result(
    classification: str,
    suggested_action: str,
    rationale: str,
    source_evidence: str,
    evidence_level: str,
    suggested_tags: list[str],
    suggested_modalities: list[str] | None = None,
) -> dict[str, Any]:
    return {
        "classification": classification,
        "suggested_action": suggested_action,
        "rationale": rationale,
        "source_evidence": source_evidence,
        "evidence_level": evidence_level,
        "suggested_tags": suggested_tags,
        "suggested_modalities": suggested_modalities or [],
        "automatic_decision_applied": False,
    }


def screen_record(
    record: dict[str, Any],
    mendeley_evidence: dict[str, dict] | None = None,
    dryad_evidence: dict[str, dict] | None = None,
) -> dict[str, Any] | None:
    """Return a non-binding screen for records currently labeled tabular-only."""

    modalities = list(record.get("modalities") or [])
    if modalities != ["tabular"]:
        return None

    record_id = str(record.get("record_id") or record.get("name") or "")
    mendeley_evidence = mendeley_evidence or {}
    dryad_evidence = dryad_evidence or {}
    mendeley = mendeley_evidence.get(_stable_mendeley_id(record), {})
    dryad = dryad_evidence.get(record_id, {})
    evidence = mendeley or dryad
    source_evidence = str(
        evidence.get("file_listing_summary")
        or evidence.get("structure_summary")
        or evidence.get("reason")
        or record.get("description")
        or "No file-level evidence summary is available."
    )
    evidence_level = (
        "complete_deposit_structure_reviewed"
        if "complete" in str(dryad.get("file_review_level") or "").lower()
        else "official_file_listing_or_source_description"
        if evidence
        else "catalog_description_only"
    )

    if record_id in PRIMARY_MODALITY_CORRECTIONS:
        suggested = PRIMARY_MODALITY_CORRECTIONS[record_id]
        return _result(
            "primary_model_data_present_but_modality_incomplete",
            "correct_modality_and_retain",
            "The source evidence describes reusable images, raw signals, or image annotations. The current tabular-only label is incomplete.",
            source_evidence,
            evidence_level,
            ["primary_images_or_signals_present", "metadata_problem"],
            suggested,
        )

    if record_id in SPATIAL_MEASUREMENT_EXCEPTIONS:
        return _result(
            "inherently_tabular_or_spatial_model_data",
            "retain",
            "The deposit contains a dense spatial measurement map rather than only aggregate image-derived summary values.",
            source_evidence,
            evidence_level,
            ["inherently_tabular_useful"],
        )

    if record_id in DERIVED_IMAGING_WITHOUT_SOURCE_DATA:
        return _result(
            "derived_imaging_measurements_without_source_data",
            "exclude_unless_source_images_are_found",
            "The reviewed deposit appears to contain OCT, OCTA, RNFL, vessel-density, or related image-derived values without the source scans or another independently useful primary modality.",
            source_evidence,
            evidence_level,
            ["derived_measurements_without_source_data", "images_missing_from_deposit"],
        )

    if record_id in MIXED_DERIVED_MEASUREMENTS_NEED_REVIEW:
        return _result(
            "mixed_primary_and_image_derived_tabular_measurements",
            "needs_review",
            "The table mixes potentially useful primary clinical or laboratory measurements with values derived from missing images. Confirm whether the non-imaging variables provide sufficient standalone model value.",
            source_evidence,
            evidence_level,
            ["quantity_unclear"],
        )

    mendeley_recommendation = str(mendeley.get("final_recommendation") or "")
    dryad_decision = str(dryad.get("model_use_decision") or "")
    if "nonhuman" in dryad_decision or "nonhuman" in mendeley_recommendation:
        return _result(
            "nonhuman_out_of_scope",
            "exclude",
            "The source review identifies nonhuman data without a separable human or human-derived component.",
            source_evidence,
            evidence_level,
            ["not_human"],
        )

    if mendeley_recommendation in {
        "exclude_not_model_resource",
        "exclude_insufficient",
    } or (
        dryad_decision
        and not dryad_decision.startswith("included_human_or_human_derived")
    ):
        classification = (
            "paper_support_tables_or_no_reusable_model_data"
            if mendeley_recommendation == "exclude_not_model_resource"
            or "not_model_resource" in dryad_decision
            else "insufficient_file_level_evidence"
        )
        action = "exclude" if "paper_support" in classification else "needs_review"
        tags = (
            ["paper_support_tables_only", "no_reusable_data"]
            if action == "exclude"
            else ["metadata_problem"]
        )
        return _result(
            classification,
            action,
            "The source review did not confirm observation-level model inputs, targets, or annotations in the current deposit.",
            source_evidence,
            evidence_level,
            tags,
        )

    combined_text = " ".join(
        str(value or "")
        for value in (
            record.get("canonical_name"),
            record.get("description"),
            record.get("notes"),
            evidence.get("data_granularity"),
            source_evidence,
        )
    ).lower()
    if any(term in combined_text for term in INHERENTLY_TABULAR_TERMS):
        return _result(
            "inherently_tabular_model_data",
            "retain",
            "The evidence describes participant-, eye-, sample-, or trial-level measurements that are themselves usable model variables or targets.",
            source_evidence,
            evidence_level,
            ["inherently_tabular_useful"],
        )

    if mendeley_recommendation == "confirmed_include_new" or dryad_decision.startswith(
        "included_human_or_human_derived"
    ):
        return _result(
            "observation_level_tabular_data_needs_author_scope_check",
            "needs_review",
            "A prior source review found observation-level data, but the deposit does not match one of the clearly retained inherently tabular categories. Confirm its standalone value for model training or evaluation.",
            source_evidence,
            evidence_level,
            [],
        )

    return _result(
        "insufficient_file_level_evidence",
        "needs_review",
        "The current evidence does not establish whether the table is reusable observation-level model data or only a paper-supporting output.",
        source_evidence,
        evidence_level,
        ["metadata_problem"],
    )


def attach_model_data_screens(catalog: dict[str, Any], repo_root: Path) -> dict[str, Any]:
    """Attach internal triage hints to catalog records in memory."""

    mendeley, dryad = load_source_evidence(repo_root)
    for record in catalog.get("records", []):
        screen = screen_record(record, mendeley, dryad)
        if screen is not None:
            record["internal_model_data_screen"] = screen
    return catalog
