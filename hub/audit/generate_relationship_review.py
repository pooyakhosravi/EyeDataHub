"""Generate the complete record-relationship review and evidence exports.

The output contains one review row for every catalog record, one row per
confirmed directed relationship edge, and a compact list of upstream or
ambiguous cases that were deliberately not forced into the catalog graph.
No dataset files, credentials, signed URLs, or local paths are read or written.
"""

from __future__ import annotations

import csv
import json
import sys
from collections import Counter, defaultdict
from dataclasses import asdict
from pathlib import Path
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from eyedatahub import __version__  # noqa: E402
from eyedatahub.catalog import info_to_record  # noqa: E402
from eyedatahub.core.relationships import (  # noqa: E402
    RELATIONSHIP_DEFINITIONS,
    RELATIONSHIP_EVIDENCE,
    RELATIONSHIP_TYPES,
)
from eyedatahub.datasets.registry import REGISTRY  # noqa: E402
from hub.export_catalog import CATALOG_CUTOFF  # noqa: E402


AUDIT_DIR = ROOT / "hub" / "audit"
REVIEW_DATE = "2026-08-01"
REVIEW_PATH = AUDIT_DIR / f"resource_relationship_review_{REVIEW_DATE}.csv"
EDGE_PATH = AUDIT_DIR / f"resource_relationship_edges_{REVIEW_DATE}.csv"
UNRESOLVED_PATH = AUDIT_DIR / f"resource_relationship_unresolved_{REVIEW_DATE}.csv"
SUMMARY_PATH = AUDIT_DIR / f"resource_relationship_summary_{REVIEW_DATE}.json"


# These are real upstream or project relationships that cannot be expressed as
# an edge because the other resource is not a distinct EyeDataHub record, or
# because the public evidence does not identify exact containment.
EXTERNAL_OR_UNRESOLVED: dict[str, tuple[str, ...]] = {
    "amdnet23": ("ARIA", "DR_200", "Fundus Dataset",),
    "belo": ("BCSC", "BioASQ", "MedMCQA", "MedQA", "PubMedQA"),
    "casia_iris_v4": ("CASIA-IrisV3",),
    "chase_db1": ("CHASE study",),
    "coph100": ("RIDIRP database",),
    "corn_collection": ("CORN-1", "CORN-2", "CORN-3", "CORN-Complex"),
    "fundus_domain_generalization": ("ORIGA",),
    "fundus_report_dataset": ("OUWFD",),
    "hassan_composite_retina": ("Unresolved component-level provenance",),
    "intraretinal_cystoid_fluid": (
        "200 newly collected Institute of Ophthalmology test images",
    ),
    "lmod_plus": ("Harvard FairSeg", "CAU001", "CatDet2", "ORIGA"),
    "maples_dr": ("Original MESSIDOR",),
    "mm_retinal_reason": (
        "ARIA",
        "ORIGA",
        "Original MESSIDOR",
        "Retina (ambiguous source label)",
        "DR1-2",
        "ScarDat",
        "MPOS",
        "Glaucoma detection (ambiguous source label)",
    ),
    "multieye": ("MMC-AMD", "1000Fundus39Cat", "ARIA"),
    "mured": ("ARIA",),
    "ocular_chat_vqa": ("AREDS",),
    "ophora": ("Public YouTube ophthalmic narrative videos",),
    "periorbital_segmentation": ("Chicago Face Database", "CelebAMask-HQ"),
    "rao_fundus": ("Public web images",),
    "riga_plus": ("Original MESSIDOR",),
    "smdg": ("CRFO-v4", "DR-HAGIS", "LES-AV", "ORIGA-light", "sjchoi86-HRF"),
    "syn_oct": ("Private Singapore source scans",),
    "trend2_fundus": ("TREND project relationship without documented sample overlap",),
    "ubiris_v2": ("UBIRIS.v1",),
    "x_pcr": (
        "APTOS FFA 2023",
        "EyesPhotos",
        "Retina (ambiguous source label)",
        "RetCam source labeled images",
    ),
}


# Important lexical or naming similarities that were reviewed and rejected.
# They are public so future curators do not accidentally reintroduce them.
REJECTED_CANDIDATES: dict[str, tuple[str, ...]] = {
    "airogs": (
        "The Rotterdam EyePACS name identifies an organization/source site; it does not establish reuse of the cataloged Kaggle EyePACS diabetic-retinopathy data.",
    ),
    "brset": (
        "BRSET and mBRSET are distinct cohorts; misleading PhysioNet parent-project markup is not treated as data lineage.",
    ),
    "cataract_lmm": (
        "The source describes a newly collected two-center cohort, not reuse of another cataloged cataract dataset.",
    ),
    "fairvlmed": (
        "No official source statement supports the previous claim that FairVLMed and Harvard-FairVision use the same cohort.",
    ),
    "fimd": (
        "FIMD follows the FIRE control-point annotation method but does not reuse FIRE images.",
    ),
    "hpmi": (
        "HPMI is compared with or described as complementary to PALM; no shared images are documented.",
    ),
    "justraigs": (
        "EyePACS LLC supplied the JustRAIGS images, but this does not identify them as the cataloged EyePACS diabetic-retinopathy competition data.",
    ),
    "maples_dr": (
        "MAPLES-DR uses original MESSIDOR images; the cataloged MESSIDOR-2 record is not substituted for that source.",
    ),
    "mbrset": (
        "mBRSET and BRSET were collected in different states with different cameras and are not treated as the same cohort.",
    ),
    "ochid": (
        "CORN and ROSE appear in navigation on the same project site; this is not evidence that OCHID reuses their data.",
    ),
    "ophora": (
        "Ophora uses public narrative videos and is not documented as a derivative of OphNet2024.",
    ),
    "riga_plus": (
        "RIGA+ cites original MESSIDOR, not MESSIDOR-2, so no edge to messidor2 is asserted.",
    ),
    "sics155": (
        "The SICS-155 source compares its phases with Cataract-101, CATARACTS, and CaDIS but describes a distinct recruited cohort.",
    ),
    "smdg": (
        "EyePACS-AIROGS is mapped to airogs, not to the cataloged diabetic-retinopathy eyepacs record.",
    ),
    "ut_fsocta": (
        "UT-FSOCTA uses the ROSE algorithm for processing; it does not state that ROSE dataset images were reused.",
    ),
    "x_pcr": (
        "The source label APTOS FFA 2023 is distinct from APTOS2019; only the separately labeled APTOS2019 rows are mapped to aptos2019.",
    ),
}


def _join(values: Iterable[str]) -> str:
    return "|".join(sorted(set(values)))


def _write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def validate_edges(records: dict[str, dict[str, Any]]) -> None:
    """Reject invalid, duplicate, or asymmetric curated edges."""

    seen: set[tuple[str, str, str]] = set()
    overlap_pairs: set[tuple[str, str]] = set()
    component_pairs: set[tuple[str, str]] = set()
    for edge in RELATIONSHIP_EVIDENCE:
        key = (edge.source_record_id, edge.relationship_type, edge.target_record_id)
        if key in seen:
            raise RuntimeError(f"Duplicate relationship edge: {key}")
        seen.add(key)
        if edge.relationship_type not in RELATIONSHIP_TYPES:
            raise RuntimeError(f"Unknown relationship type: {edge.relationship_type}")
        if edge.source_record_id not in records or edge.target_record_id not in records:
            raise RuntimeError(f"Relationship target or source is not cataloged: {key}")
        if edge.source_record_id == edge.target_record_id:
            raise RuntimeError(f"Self relationship is not allowed: {key}")
        if not edge.evidence_url.startswith(("http://", "https://")):
            raise RuntimeError(f"Relationship lacks a public evidence URL: {key}")
        if edge.relationship_type == "same_or_overlapping_cohort_as":
            overlap_pairs.add((edge.source_record_id, edge.target_record_id))
        if edge.relationship_type == "has_component":
            component_pairs.add((edge.source_record_id, edge.target_record_id))

    for source, target in overlap_pairs:
        inverse = (target, "same_or_overlapping_cohort_as", source)
        if inverse not in seen:
            raise RuntimeError(f"Missing symmetric overlap edge: {inverse}")
    for collection, component in component_pairs:
        inverse = (component, "component_of", collection)
        if inverse not in seen:
            raise RuntimeError(f"Missing component inverse edge: {inverse}")


def generate() -> tuple[Path, Path, Path, Path]:
    records = {
        dataset.info.name: info_to_record(dataset.info)
        for dataset in REGISTRY.list_datasets()
    }
    if len(records) != 251:
        raise RuntimeError(f"Expected 251 catalog records, found {len(records)}")
    validate_edges(records)

    outgoing: dict[str, list[Any]] = defaultdict(list)
    incoming: dict[str, list[Any]] = defaultdict(list)
    edge_rows: list[dict[str, Any]] = []
    for edge in sorted(
        RELATIONSHIP_EVIDENCE,
        key=lambda value: (
            value.source_record_id,
            value.relationship_type,
            value.target_record_id,
        ),
    ):
        outgoing[edge.source_record_id].append(edge)
        incoming[edge.target_record_id].append(edge)
        edge_rows.append(
            {
                **asdict(edge),
                "source_canonical_name": records[edge.source_record_id]["canonical_name"],
                "target_canonical_name": records[edge.target_record_id]["canonical_name"],
                "catalog_version": __version__,
            }
        )

    review_rows: list[dict[str, Any]] = []
    unresolved_rows: list[dict[str, Any]] = []
    for record_id, record in sorted(records.items()):
        record_outgoing = outgoing.get(record_id, [])
        record_incoming = incoming.get(record_id, [])
        external = EXTERNAL_OR_UNRESOLVED.get(record_id, ())
        rejected = REJECTED_CANDIDATES.get(record_id, ())
        if record_outgoing or record_incoming:
            outcome = "confirmed_catalog_relationship"
        elif external:
            outcome = "external_or_unresolved_relationship_only"
        else:
            outcome = "no_documented_catalog_relationship_identified"

        review_rows.append(
            {
                "record_id": record_id,
                "canonical_name": record["canonical_name"],
                "primary_category": record["primary_category"],
                "catalog_version": __version__,
                "catalog_search_cutoff": CATALOG_CUTOFF,
                "relationship_review_date": REVIEW_DATE,
                "official_source_url": record.get("source_landing_page_url") or "",
                "source_check_status": record.get("source_check_status") or "unknown",
                "review_outcome": outcome,
                "outgoing_relationship_count": len(record_outgoing),
                "outgoing_relationship_types": _join(
                    edge.relationship_type for edge in record_outgoing
                ),
                "outgoing_target_record_ids": _join(
                    edge.target_record_id for edge in record_outgoing
                ),
                "incoming_relationship_count": len(record_incoming),
                "incoming_source_record_ids": _join(
                    edge.source_record_id for edge in record_incoming
                ),
                "evidence_urls": _join(
                    edge.evidence_url for edge in (*record_outgoing, *record_incoming)
                ),
                "external_or_unresolved_sources": _join(external),
                "rejected_candidate_notes": " | ".join(rejected),
                "review_scope": (
                    "Same-data, subset, version, mirror, component, replacement, "
                    "extension, derivation, and documented cohort-overlap links "
                    "to other catalog records."
                ),
                "reviewer": "EyeDataHub authors",
            }
        )

        for source_name in external:
            unresolved_rows.append(
                {
                    "record_id": record_id,
                    "canonical_name": record["canonical_name"],
                    "item": source_name,
                    "status": "upstream_not_cataloged_or_exact_mapping_unresolved",
                    "official_source_url": record.get("source_landing_page_url") or "",
                    "review_date": REVIEW_DATE,
                    "notes": (
                        "Preserved outside the catalog graph; no target record was "
                        "invented or substituted."
                    ),
                }
            )
        for note in rejected:
            unresolved_rows.append(
                {
                    "record_id": record_id,
                    "canonical_name": record["canonical_name"],
                    "item": "rejected candidate",
                    "status": "reviewed_not_a_data_relationship",
                    "official_source_url": record.get("source_landing_page_url") or "",
                    "review_date": REVIEW_DATE,
                    "notes": note,
                }
            )

    if len(review_rows) != 251:
        raise RuntimeError(f"Relationship review has {len(review_rows)} rows, expected 251")

    _write_csv(REVIEW_PATH, review_rows, list(review_rows[0]))
    _write_csv(EDGE_PATH, edge_rows, list(edge_rows[0]))
    _write_csv(UNRESOLVED_PATH, unresolved_rows, list(unresolved_rows[0]))

    type_counts = Counter(edge.relationship_type for edge in RELATIONSHIP_EVIDENCE)
    outcome_counts = Counter(row["review_outcome"] for row in review_rows)
    participating_records = set(outgoing) | set(incoming)
    symmetric_overlap_pairs = {
        tuple(sorted((edge.source_record_id, edge.target_record_id)))
        for edge in RELATIONSHIP_EVIDENCE
        if edge.relationship_type == "same_or_overlapping_cohort_as"
    }
    summary = {
        "schema_version": "1.0",
        "catalog_version": __version__,
        "catalog_search_cutoff": CATALOG_CUTOFF,
        "relationship_review_date": REVIEW_DATE,
        "catalog_record_count": len(records),
        "reviewed_record_count": len(review_rows),
        "directed_relationship_edge_count": len(RELATIONSHIP_EVIDENCE),
        "records_participating_in_confirmed_relationships": len(participating_records),
        "records_with_outgoing_relationships": len(outgoing),
        "records_with_incoming_relationships": len(incoming),
        "unique_symmetric_overlap_pairs": len(symmetric_overlap_pairs),
        "relationship_counts_by_type": dict(sorted(type_counts.items())),
        "review_outcomes": dict(sorted(outcome_counts.items())),
        "unresolved_or_external_item_count": sum(
            len(values) for values in EXTERNAL_OR_UNRESOLVED.values()
        ),
        "reviewed_rejected_candidate_count": sum(
            len(values) for values in REJECTED_CANDIDATES.values()
        ),
        "relationship_definitions": RELATIONSHIP_DEFINITIONS,
        "counting_note": (
            "Relationship edges are directed. Inverse component edges and both "
            "directions of symmetric cohort-overlap edges are included. Counts "
            "therefore describe catalog assertions, not independent cohorts."
        ),
        "third_party_dataset_files_included": False,
    }
    SUMMARY_PATH.write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(
        f"Wrote {len(review_rows)} review rows, {len(edge_rows)} directed edges, "
        f"and {len(unresolved_rows)} unresolved/rejected rows."
    )
    return REVIEW_PATH, EDGE_PATH, UNRESOLVED_PATH, SUMMARY_PATH


if __name__ == "__main__":
    generate()
