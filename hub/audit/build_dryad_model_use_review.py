"""Build the record-level Dryad human/model-use screening ledger.

This review is deliberately separate from route and download checks. A record
can be technically available while remaining outside the scientific boundary
of the headline catalog. The retained boundary is human participant data,
human-derived biological material, and synthetic or annotation resources that
are demonstrably derived from human data and contain reusable inputs, labels,
measurements, or annotations for model development or evaluation.

The input inventory contains official current-version Dryad metadata and file
listings for the 145 Dryad-backed records present at the start of this review.
Small deposits may also have a structural inspection result. No participant
values, credentials, signed URLs, or local paths are written to the outputs.
"""

from __future__ import annotations

import argparse
import csv
import html
import json
import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_INVENTORY = (
    ROOT / "hub" / "audit" / "dryad_model_use_inventory_2026-08-02.json"
)
DEFAULT_STRUCTURE = (
    ROOT / "hub" / "audit" / "dryad_model_use_structure_2026-08-02.json"
)
DEFAULT_CURATED_REVIEW = (
    ROOT / "hub" / "audit" / "dryad_model_use_decisions_2026-08-02.json"
)
DEFAULT_CSV = ROOT / "hub" / "audit" / "dryad_model_use_review_2026-08-02.csv"
DEFAULT_JSON = ROOT / "hub" / "audit" / "dryad_model_use_review_2026-08-02.json"

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from eyedatahub.datasets.scope_exclusions import (  # noqa: E402
    DRYAD_SCOPE_EXCLUSIONS,
    NONHUMAN_DRYAD_RECORD_IDS as EXCLUDED_NONHUMAN_IDS,
)


SPECIAL_POPULATION_EVIDENCE = {
    "dryad_vq83bk3s8": (
        "The associated eLife article identifies mouse as the research "
        "organism and describes the mouse On-Off direction-selective ganglion "
        "cell circuit."
    ),
    "dryad_rn8pk0pmm": (
        "The title foregrounds a human CRYGC mutation, but the official methods "
        "and deposited FASTQ/qPCR files describe a transgenic mouse model."
    ),
    "dryad_prpf31_gene_augmentation": (
        "The official deposit is a mouse-model study; its FASTQ files do not "
        "document a separable human component."
    ),
    "dryad_retinal_vein_cannulation": (
        "The official abstract describes autonomous cannulation experiments in "
        "ex vivo porcine eyes."
    ),
    "dryad_subretinal_robot": (
        "The official source describes robotic subretinal-injection experiments "
        "using ex vivo porcine eyes."
    ),
}


HUMAN_DERIVED_IDS = {
    "dryad_d1zd5s",
    "dryad_rao_multiomics",
    "dryad_vkh_apoe",
}
MIXED_SEPARABLE_HUMAN_IDS = {"dryad_clcc1_retinitis_pigmentosa"}
HUMAN_ANNOTATION_LAYER_IDS = {"dryad_sf7m0cggh"}


_TAG_RE = re.compile(r"<[^>]+>")
_SPACE_RE = re.compile(r"\s+")
_SENTENCE_RE = re.compile(r"(?<=[.!?])\s+")
_SPECIES_TERMS = (
    "mouse",
    "mice",
    "murine",
    "rat",
    "rabbit",
    "canine",
    "dog",
    "macaque",
    "primate",
    "zebrafish",
    "danio rerio",
    "porcine",
    "pig",
    "chick",
    "xenopus",
    "ground squirrel",
    "mole-rat",
    "starling",
    "animal",
    "vertebrate",
)


def _plain(value: Any) -> str:
    text = html.unescape(str(value or ""))
    text = _TAG_RE.sub(" ", text)
    return _SPACE_RE.sub(" ", text).strip()


def _species_label(record: dict[str, Any]) -> str:
    text = " ".join(
        _plain(record.get(field)).lower()
        for field in ("source_title", "source_abstract", "source_methods")
    )
    labels = (
        (("porcine", " pig "), "porcine_or_ex_vivo_porcine"),
        (("canine", " dog", "dogs"), "canine"),
        (("macaque", "non-human primate", "rhesus", "primate retina"), "nonhuman_primate"),
        (("zebrafish", "danio rerio"), "zebrafish"),
        (("xenopus",), "xenopus"),
        (("chick",), "chick"),
        (("rabbit",), "rabbit"),
        (("ground squirrel",), "ground_squirrel"),
        (("mole-rat",), "mole_rat"),
        (("starling",), "bird"),
        (("mouse", "mice", "murine"), "mouse"),
        ((" rat ", "rat retinal"), "rat"),
    )
    for terms, label in labels:
        if any(term in f" {text} " for term in terms):
            return label
    return "nonhuman_or_nonhuman_derived"


def _population_evidence(record: dict[str, Any]) -> str:
    record_id = record["record_id"]
    if record_id in SPECIAL_POPULATION_EVIDENCE:
        return SPECIAL_POPULATION_EVIDENCE[record_id]
    text = " ".join(
        _plain(record.get(field))
        for field in ("source_title", "source_abstract", "source_methods")
    )
    for sentence in _SENTENCE_RE.split(text):
        lowered = sentence.lower()
        if any(term in lowered for term in _SPECIES_TERMS):
            return sentence[:500]
    return _plain(record.get("source_title"))[:500]


def _structure_rows(path: Path) -> dict[str, dict[str, Any]]:
    if not path.exists():
        return {}
    payload = json.loads(path.read_text(encoding="utf-8"))
    return {row["record_id"]: row for row in payload.get("records") or []}


def _structure_summary(record: dict[str, Any] | None) -> str:
    if not record or not record.get("complete_deposit_downloaded_for_structure_review"):
        return "official_current_version_file_listing_reviewed"
    kinds = Counter(
        str(item.get("structure", {}).get("kind") or "unknown")
        for item in record.get("files") or []
    )
    return "complete_small_deposit_structure_reviewed: " + ", ".join(
        f"{key}={value}" for key, value in sorted(kinds.items())
    )


def _source_origin(record_id: str) -> str:
    if record_id in EXCLUDED_NONHUMAN_IDS:
        return "nonhuman_or_nonhuman_derived"
    if record_id == "dryad_eye_head_visual_selection":
        return "human_aggregate_visual_behavior_summary"
    if record_id in {
        "dryad_pg4f4qrwf",
        "dryad_rod_cone_dystrophy_genes",
    }:
        return "human_related_literature_or_database_analysis"
    if record_id in MIXED_SEPARABLE_HUMAN_IDS:
        return "mixed_with_separable_human_component"
    if record_id in HUMAN_DERIVED_IDS:
        return "human_participants_or_human_derived_biological_material"
    if record_id in HUMAN_ANNOTATION_LAYER_IDS:
        return "annotation_layer_derived_from_human_data"
    return "human_participant_or_patient_data"


PUBLIC_DECISION_LABELS = {
    "include_model_resource": "included_human_or_human_derived_model_resource",
    "exclude_nonhuman": "excluded_nonhuman_or_nonhuman_derived",
    "exclude_analysis_only": "excluded_analysis_only",
    "exclude_not_ophthalmic_model_resource": (
        "excluded_not_suitable_for_model_training_or_evaluation"
    ),
    "duplicate_or_relationship_only": "excluded_relationship_only_resource",
    "insufficient_evidence": "excluded_insufficient_model_use_evidence",
}


def _curated_rows(path: Path) -> dict[str, dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    records = payload.get("records") or []
    rows = {str(record["record_id"]): record for record in records}
    if len(records) != 145 or len(rows) != 145:
        raise ValueError("The curated Dryad decision ledger must contain 145 rows")
    unknown = sorted(
        {
            str(record.get("decision") or "")
            for record in records
        }
        - set(PUBLIC_DECISION_LABELS)
    )
    if unknown:
        raise ValueError(f"Unknown curated Dryad decisions: {unknown}")
    return rows


def _decision(record: dict[str, Any]) -> tuple[str, bool, str]:
    decision = str(record["decision"])
    return (
        PUBLIC_DECISION_LABELS[decision],
        decision == "include_model_resource",
        str(record["concise_record_specific_reason"]),
    )


def _write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    fields = [
        "record_id",
        "canonical_name",
        "dataset_doi",
        "source_version",
        "source_title",
        "expected_file_count",
        "expected_bytes",
        "source_data_origin",
        "population_scope",
        "population_evidence",
        "file_review_level",
        "structure_summary",
        "data_granularity",
        "plausible_model_use",
        "evidence_basis",
        "model_use_decision",
        "headline_catalog_included",
        "reason",
        "related_catalog_record_ids_or_names",
        "confidence",
        "review_date",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(payload, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )
    temporary.replace(path)


def build(
    *, inventory_path: Path, structure_path: Path, curated_review_path: Path
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    inventory = json.loads(inventory_path.read_text(encoding="utf-8"))
    structures = _structure_rows(structure_path)
    curated = _curated_rows(curated_review_path)
    inventory_records = inventory.get("records") or []
    inventory_ids = {record["record_id"] for record in inventory_records}
    excluded_ids = set(DRYAD_SCOPE_EXCLUSIONS)

    if len(EXCLUDED_NONHUMAN_IDS) != 58:
        raise ValueError("The curated nonhuman Dryad set must contain 58 records")
    if len(excluded_ids) != 63:
        raise ValueError("The complete Dryad scope-exclusion set must contain 63 records")
    if len(inventory_ids) != 145:
        raise ValueError("This dated review requires exactly 145 unique Dryad records")
    if set(curated) != inventory_ids:
        raise ValueError("Curated Dryad decisions and source inventory IDs differ")
    missing = excluded_ids - inventory_ids
    if missing:
        raise ValueError(f"Curated exclusions missing from inventory: {sorted(missing)}")

    rows: list[dict[str, Any]] = []
    for record in sorted(inventory_records, key=lambda item: item["record_id"]):
        record_id = record["record_id"]
        structure = structures.get(record_id)
        curated_row = curated[record_id]
        outcome, included, reason = _decision(curated_row)
        origin = _source_origin(record_id)
        rows.append(
            {
                "record_id": record_id,
                "canonical_name": record["canonical_name"],
                "dataset_doi": record["dataset_identifier"],
                "source_version": record["observed_deposit_version"],
                "source_title": _plain(record.get("source_title")),
                "expected_file_count": record["expected_file_count"],
                "expected_bytes": record["expected_bytes"],
                "source_data_origin": origin,
                "population_scope": (
                    _species_label(record)
                    if record_id in EXCLUDED_NONHUMAN_IDS
                    else origin
                ),
                "population_evidence": _population_evidence(record),
                "file_review_level": (
                    structure.get("inspection_level")
                    if structure
                    else record["listing_result"]
                ),
                "structure_summary": _structure_summary(structure),
                "data_granularity": curated_row["data_granularity"],
                "plausible_model_use": curated_row["plausible_model_use"],
                "evidence_basis": curated_row["evidence_basis"],
                "model_use_decision": outcome,
                "headline_catalog_included": included,
                "reason": reason,
                "related_catalog_record_ids_or_names": curated_row.get(
                    "related_catalog_record_ids_or_names", ""
                ),
                "confidence": curated_row["confidence"],
                "review_date": date.today().isoformat(),
            }
        )

    counts = Counter(row["model_use_decision"] for row in rows)
    included_count = sum(row["headline_catalog_included"] for row in rows)
    if included_count != 82:
        raise ValueError(f"Expected 82 retained Dryad records, observed {included_count}")
    summary = {
        "schema_version": "1.0",
        "review_date": date.today().isoformat(),
        "source_inventory": inventory_path.name,
        "source_structure_review": structure_path.name,
        "source_curated_decisions": curated_review_path.name,
        "records_reviewed": len(rows),
        "headline_catalog_included": included_count,
        "headline_catalog_excluded": len(rows) - included_count,
        "decision_counts": dict(sorted(counts.items())),
        "criteria": {
            "included": (
                "Human participant data, human-derived biological material, or "
                "human-derived annotations containing reusable inputs, labels, "
                "measurements, or annotations for model development or evaluation."
            ),
            "mixed_data": (
                "A mixed deposit is included only when its human component is "
                "separately identifiable."
            ),
            "excluded_nonhuman": (
                "Animal-only, nonhuman-primate, ex vivo nonhuman, or nonhuman-"
                "derived material without a separable human component."
            ),
            "excluded_not_distinct": (
                "Aggregate article results, literature/database analysis outputs, "
                "or generic gaze summaries that do not form a distinct sample-level "
                "model-development or evaluation resource."
            ),
        },
        "complete_small_deposit_structure_reviews": sum(
            bool(structures.get(row["record_id"], {}).get(
                "complete_deposit_downloaded_for_structure_review"
            ))
            for row in rows
        ),
        "included_complete_deposit_structure_reviews": sum(
            row["headline_catalog_included"]
            and bool(
                structures.get(row["record_id"], {}).get(
                    "complete_deposit_downloaded_for_structure_review"
                )
            )
            for row in rows
        ),
        "included_official_file_listing_reviews": sum(
            row["headline_catalog_included"]
            and not bool(
                structures.get(row["record_id"], {}).get(
                    "complete_deposit_downloaded_for_structure_review"
                )
            )
            for row in rows
        ),
        "official_current_version_file_listings_reviewed": len(rows),
        "local_dataset_files_retained": False,
        "credential_values_serialized": False,
        "signed_or_download_urls_serialized": False,
        "participant_values_serialized": False,
        "records": rows,
    }
    return rows, summary


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inventory", type=Path, default=DEFAULT_INVENTORY)
    parser.add_argument("--structure", type=Path, default=DEFAULT_STRUCTURE)
    parser.add_argument(
        "--curated-review", type=Path, default=DEFAULT_CURATED_REVIEW
    )
    parser.add_argument("--csv-out", type=Path, default=DEFAULT_CSV)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    args = parser.parse_args()
    rows, summary = build(
        inventory_path=args.inventory,
        structure_path=args.structure,
        curated_review_path=args.curated_review,
    )
    _write_csv(args.csv_out, rows)
    _write_json(args.json_out, summary)
    print(json.dumps({
        "records_reviewed": summary["records_reviewed"],
        "headline_catalog_included": summary["headline_catalog_included"],
        "headline_catalog_excluded": summary["headline_catalog_excluded"],
        "decision_counts": summary["decision_counts"],
    }, indent=2))


if __name__ == "__main__":
    main()
