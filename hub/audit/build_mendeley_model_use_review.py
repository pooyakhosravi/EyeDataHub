"""Build the final Mendeley model-use screening record.

The source verification log contains all 141 versioned Mendeley deposits that
were present before the final scientific-scope review. This script keeps that
source history immutable while recording which resources remain in the
headline catalog after file-structure and author review.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any

from eyedatahub.datasets.scope_exclusions import (
    MENDELEY_AUTHOR_REMOVED_UNCERTAIN_RECORD_IDS,
    MENDELEY_NOT_USEFUL_RECORD_IDS,
)


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_SOURCE = (
    ROOT / "hub" / "audit" / "mendeley_download_verification_2026-08-03.json"
)
DEFAULT_OUTPUT = ROOT / "hub" / "audit" / "mendeley_model_use_review_2026-08-03.json"
REVIEW_DATE = "2026-08-03"


DOCUMENT_OR_MANUSCRIPT_SUPPORT_IDS = frozenset(
    {
        "chronic_corneal_disorders",
        "mendeley_effect_prednisone_plus_either_adalimumab_or",
        "mendeley_keratoconus_ukraine_children",
        "mendeley_performance_corneal_vs_scleral_rigid_gas",
        "mendeley_selective_laser_trabeculoplasty_patients_angle_recession",
    }
)


DERIVED_MEASUREMENTS_WITHOUT_PRIMARY_DATA_IDS = frozenset(
    {
        "mendeley_anterior_segment_optical_coherence_tomography_angiography",
        "mendeley_clinical_assessment_scleral_canal_expansion_glaucoma",
        "mendeley_difference_retinal_nerve_fiber_layer_thickness",
        "mendeley_improved_retinal_displacement_quantification_between_retinal",
        "mendeley_microvascular_changes_poag_after_npds",
        "mendeley_peripapillary_retinal_nerve_fiber_layer_thinning",
        "mendeley_radial_peripapillary_capillary_density_as_predictive",
        "mendeley_vivo_analysis_comparison_anterior_segment_structures",
    }
)


def _decision(record_id: str) -> tuple[str, bool, str]:
    if record_id in MENDELEY_AUTHOR_REMOVED_UNCERTAIN_RECORD_IDS:
        return (
            "excluded_after_author_review_due_to_uncertain_scope",
            False,
            "The record was removed rather than retained with unresolved model-use value.",
        )
    if record_id in DOCUMENT_OR_MANUSCRIPT_SUPPORT_IDS:
        return (
            "excluded_document_or_manuscript_support_only",
            False,
            "The reviewed deposit was document-only or manuscript-supporting material rather than a reusable model dataset.",
        )
    if record_id in DERIVED_MEASUREMENTS_WITHOUT_PRIMARY_DATA_IDS:
        return (
            "excluded_derived_measurements_without_primary_data",
            False,
            "The deposit contained image-derived summary measurements without the underlying images or another independently useful primary modality.",
        )
    if record_id in MENDELEY_NOT_USEFUL_RECORD_IDS:
        return (
            "excluded_not_suitable_for_model_training_or_evaluation",
            False,
            "Author review found that the deposited material did not fit the retained model-development or evaluation boundary.",
        )
    return (
        "included_human_or_human_derived_model_resource",
        True,
        "The source and file review identified reusable human or human-derived images, signals, omics, measurements, annotations, or model targets.",
    )


def build(source_path: Path) -> dict[str, Any]:
    source = json.loads(source_path.read_text(encoding="utf-8"))
    source_records = source.get("records") or []
    source_ids = {str(record["record_id"]) for record in source_records}
    expected_exclusions = (
        MENDELEY_NOT_USEFUL_RECORD_IDS | MENDELEY_AUTHOR_REMOVED_UNCERTAIN_RECORD_IDS
    )
    if len(source_records) != 141 or len(source_ids) != 141:
        raise ValueError("The dated Mendeley source review must contain 141 records")
    missing = expected_exclusions - source_ids
    if missing:
        raise ValueError(
            f"Mendeley exclusions missing from source log: {sorted(missing)}"
        )

    rows: list[dict[str, Any]] = []
    for source_record in sorted(source_records, key=lambda item: item["record_id"]):
        record_id = str(source_record["record_id"])
        decision, included, reason = _decision(record_id)
        rows.append(
            {
                "record_id": record_id,
                "canonical_name": source_record["canonical_name"],
                "official_source_url": source_record["official_source_url"],
                "dataset_identifier": source_record["dataset_identifier"],
                "deposit_version": source_record["deposit_version"],
                "source_archive_state": source_record["source_archive_state"],
                "file_structure_reviewed": bool(
                    source_record.get("download_completed")
                ),
                "model_use_decision": decision,
                "headline_catalog_included": included,
                "reason": reason,
                "review_date": REVIEW_DATE,
            }
        )

    counts = Counter(row["model_use_decision"] for row in rows)
    retained = sum(bool(row["headline_catalog_included"]) for row in rows)
    if retained != 116:
        raise ValueError(f"Expected 116 retained Mendeley records, observed {retained}")
    return {
        "schema_version": "1.0",
        "review_date": REVIEW_DATE,
        "source_verification_log": source_path.name,
        "records_reviewed": len(rows),
        "headline_catalog_included": retained,
        "headline_catalog_excluded": len(rows) - retained,
        "not_useful_exclusion_count": len(MENDELEY_NOT_USEFUL_RECORD_IDS),
        "author_removed_uncertain_count": len(
            MENDELEY_AUTHOR_REMOVED_UNCERTAIN_RECORD_IDS
        ),
        "decision_counts": dict(sorted(counts.items())),
        "criteria": {
            "included": "Human or human-derived data with reusable model inputs, targets, measurements, signals, omics, or annotations.",
            "excluded": "Document-only material, manuscript-support tables, peripheral analyses, or derived imaging summaries without sufficient standalone model value.",
            "uncertain": "Records with unresolved value were excluded from the headline catalog at the author's direction.",
        },
        "temporary_dataset_files_retained": False,
        "credential_values_serialized": False,
        "participant_values_serialized": False,
        "records": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = build(args.source)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(
        json.dumps(payload, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "records_reviewed": payload["records_reviewed"],
                "headline_catalog_included": payload["headline_catalog_included"],
                "headline_catalog_excluded": payload["headline_catalog_excluded"],
                "decision_counts": payload["decision_counts"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
