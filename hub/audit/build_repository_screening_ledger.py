"""Build a reproducible cross-repository discovery-screening ledger.

The script combines the dated platform search snapshot, enriched public
metadata, the completed Dryad decision ledger, the current catalog, and a
small human-reviewed override file. It assigns every search hit one final
decision. Rows that cannot be decided conservatively remain explicitly
``manual_review_pending`` and are excluded from manuscript flow counts until
resolved.

Credential values, signed URLs, download URLs, and local paths are never
serialized.
"""

from __future__ import annotations

import argparse
import csv
import html
import json
import re
from collections import Counter
from datetime import date
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_SEARCH = ROOT / "hub" / "audit" / "repository_search_candidates_2026-08-02.json"
DEFAULT_DETAILS = (
    ROOT / "hub" / "audit" / "repository_candidate_details_2026-08-02.json"
)
DEFAULT_DRYAD = ROOT / "hub" / "audit" / "dryad_discovery_decisions_2026-08-01.csv"
DEFAULT_DRYAD_MODEL_REVIEW = (
    ROOT / "hub" / "audit" / "dryad_model_use_review_2026-08-02.csv"
)
DEFAULT_CATALOG = ROOT / "hub" / "catalog.csv"
DEFAULT_OVERRIDES = (
    ROOT / "hub" / "audit" / "repository_screening_overrides_2026-08-02.json"
)
DEFAULT_CSV = ROOT / "hub" / "audit" / "repository_screening_ledger_2026-08-02.csv"
DEFAULT_JSON = ROOT / "hub" / "audit" / "repository_screening_summary_2026-08-02.json"

FINAL_DECISIONS = {
    "existing_catalog_record",
    "included_new_record",
    "excluded_not_eye_or_ophthalmology",
    "excluded_duplicate_or_alternate_deposit",
    "excluded_not_distinct_reusable_resource",
    "excluded_insufficient_source_metadata",
    "excluded_nonhuman_or_nonhuman_derived",
    "excluded_not_suitable_for_model_training_or_evaluation",
    "manual_review_pending",
}

WORKFLOW_SOURCES = ("dryad", "mendeley", "kaggle", "figshare", "huggingface")


# These source records were retained during screening but were later resolved
# as source-history links under the current-version and canonical-copy policy.
# Keeping the decisions in code makes regeneration independent of the older
# human-review snapshot, which remains unchanged as a dated review artifact.
CURRENT_CANONICAL_POLICY = {
    "huggingface:yuzhench/glaucoma-expert-cot-raw-1077": {
        "final_decision": "excluded_duplicate_or_alternate_deposit",
        "canonical_record_id": "glaucoma_expert_cot_refined",
        "canonical_record_ids": ["glaucoma_expert_cot_refined"],
        "relationship_type": "previous_version",
        "reason": (
            "Earlier raw release preserved as a previous-version link on the "
            "current refined record."
        ),
        "decision_basis": "current_version_policy",
    },
    "kaggle:pkdarabi/diagnosis-of-diabetic-retinopathy": {
        "final_decision": "excluded_duplicate_or_alternate_deposit",
        "canonical_record_id": "eyepacs",
        "canonical_record_ids": ["eyepacs"],
        "relationship_type": "alternate_subset_repository_copy",
        "reason": (
            "Unmodified repackage of the 35,126-image EyePACS training split; "
            "preserved as an alternate repository link on EyePACS."
        ),
        "decision_basis": "canonical_copy_policy",
    },
}

_TAG_RE = re.compile(r"<[^>]+>")
_SPACE_RE = re.compile(r"\s+")
_WORD_RE = re.compile(r"[^a-z0-9]+")

_EYE_RE = re.compile(
    r"(?:"
    r"ophthalm|fundus|retina|retinal|retinopathy|glaucoma|cornea|corneal|"
    r"cataract|optical coherence tomograph|diabetic retinopathy|macular|"
    r"uveit|perimetr|slit lamp|anterior segment|retinopathy of prematurity|"
    r"optic disc|optic disk|optic nerve|choroid|vitre|iris recognition|"
    r"iris biometric|eye tracking|eyetracking|pupill|periocular|oculomotor|"
    r"ocular|eye disease|eye image|eye movement|eye gaze|gaze tracking|"
    r"visual field test|visual field progression|retinitis|myopia|"
    r"keratoconus|strabismus|amblyopia|refractive error|intraocular|"
    r"retinoblastoma|lacrimal|conjunctiv|eyelid|orbital mri|thyroid eye"
    r")",
    re.IGNORECASE,
)

_FALSE_EYE_RE = re.compile(
    r"(?:"
    r"retinaface|retinanet|retina net|re[ -]?tina.*mass spect|"
    r"iris flower|iris species|iris dataset$|iris classification$|"
    r"octane|octagon|octapod|octavian|octant|octal|"
    r"fish[ -]?eye|visual field robot|visual field by validity|"
    r"magnetic field|electric field|field experiment|"
    r"ocular lens of microscope|microscope ocular|"
    r"american english full.duplex|british english full.duplex"
    r")",
    re.IGNORECASE,
)

_SUPPLEMENT_RE = re.compile(
    r"(?:"
    r"^table\b|^data[ _-]?sheet\s*\d*\b|^datasheet\s*\d*\b|^additional file\b|"
    r"^supplementary material\b|^supplementary file\b|^checklist\b|"
    r"^performance (?:comparison|metrics)|^test performance\b|"
    r"^comparison of .* (?:results|accuracy|segmentation)|"
    r"^accuracy .* results|^results? (?:of|from|for)\b|"
    r"^odds ratios?\b|^hazard ratios?\b|^likelihood ratios?\b|"
    r"^incidence (?:and|rate)|^baseline characteristics\b|"
    r"^demographic (?:data|parameters)|^characteristics of\b|"
    r"^clinical characteristics\b|^ophthalmological characteristics\b|"
    r"^basic characteristic\b|^descriptive (?:statistics|summary)\b|"
    r"^relative risk\b|^spearman rank\b|^summary of\b|"
    r"^class distribution\b|^distribution of\b|^example of\b|"
    r"^general .* statistics\b|^coefficient of repeatability\b|"
    r"^cytokines detected\b|^heterozygous individuals\b|"
    r"^the mean magnitude\b|^retinal interventions\b|^initial present\b|"
    r"^explorative data\b|^all datasets are categorized\b|"
    r"^the effectiveness\b|^dataset s\d+\b|^s\d+ dataset\b|"
    r"^metadata record for:|^related work on\b|^comparative table\b|"
    r"systematic review|meta-analysis of (?:prospective |cohort )?studies"
    r")",
    re.IGNORECASE,
)

_TITLE_ALIASES: tuple[tuple[re.Pattern[str], str], ...] = tuple(
    (re.compile(pattern, re.IGNORECASE), record_id)
    for pattern, record_id in (
        (r"\bdrive\b.*(?:digital retinal|vessel extraction)", "drive"),
        (r"\bchase[ _-]?db1\b", "chase_db1"),
        (r"\bstare\b", "stare"),
        (r"\bhrf\b.*high resolution fundus|high resolution fundus.*\bhrf\b", "hrf"),
        (r"\bidrid\b|indian diabetic retinopathy image", "idrid"),
        (r"\baptos[ _-]?2019\b", "aptos2019"),
        (r"\bairogs\b", "airogs"),
        (r"\beyepacs\b", "eyepacs"),
        (r"\bmessidor[ _-]?2\b", "messidor2"),
        (r"\brim[ _-]?one\b", "rimone_dl"),
        (r"\bacrima\b", "acrima"),
        (r"\bg1020\b", "g1020"),
        (r"\brfmid\b", "rfmid"),
        (r"\bodir[ _-]?5k\b|ocular disease intelligent recognition", "odir2019"),
        (r"\boctdl\b", "octdl"),
        (r"\bkermany\b|ucsd.*retinal oct", "kermany_oct"),
        (r"pathologic myopia recognition|\bpalm\b.*fundus", "palm"),
        (r"\bpapila\b", "papila"),
        (r"hillel yaffe glaucoma|\bhygd\b", "hygd"),
        (r"\brvo[ _-]?me\b", "rvo_me"),
        (r"brazilian multilabel ophthalmological|\bbrset\b", "brset"),
        (r"\bolives\b", "olives"),
        (r"\bfives\b", "fives"),
        (r"\bmured\b", "mured"),
        (r"sustech[ _-]?sysu.*(?:exudate|retinopathy grading)", "sustech_sysu"),
        (r"\bcataract[ _-]?1k\b", "cataract1k"),
        (r"\bgazecapture\b", "gaze_capture"),
        (r"\bmm[ _-]?retinal[ _-]?reason\b", "mm_retinal_reason"),
        (r"ophthalmology[ _-]?pubmed[ _-]?corpus", "ophthalmology_pubmed_corpus"),
        (
            r"data on oct and fundus images|oct and fundus glaucoma",
            "data_oct_fundus_glaucoma",
        ),
        (r"retinal image dataset of infants and rop", "rop_ostrava"),
        (r"comprehensive 3d .*oct.*amd.*dme", "amd_dme_3d_oct"),
        (r"multimodal dataset.*corneal opacity|\bmcoa\b", "mcoa"),
        (r"optical coherence tomography image dataset.*wet amd", "amd_sd"),
    )
)

_DERIVATIVE_RE = re.compile(
    r"(?:"
    r"resized|preprocess|augmented|balanced|cropped|grayscale|"
    r"tfrecord|organized|arranged|reorganized|formatted|filtered|"
    r"combined (?:dataset|fundus|dr )|merged dataset|dataset collection|"
    r"collection of .*datasets|copy of|mirror of|subset of|"
    r"from the .* dataset|derived from|repackag|oversampl|"
    r"train unzipped|test unzipped|model weights|checkpoint|"
    r"inference results|fine[ -]?tuned|source code|code only"
    r")",
    re.IGNORECASE,
)

_INSUFFICIENT_TITLE_RE = re.compile(
    r"^(?:dataset\d*|data\d*|retina\d*|retinal data|fundus|ocular|"
    r"glaucoma|cataract|diabetic retinopathy|eye disease|test|final dataset)$",
    re.IGNORECASE,
)


def _plain(value: Any) -> str:
    text = html.unescape(str(value or ""))
    text = _TAG_RE.sub(" ", text)
    text = text.replace("_", " ").replace("-", " ")
    return _SPACE_RE.sub(" ", text).strip()


def _normalized(value: Any) -> str:
    return _WORD_RE.sub(" ", _plain(value).lower()).strip()


def _write_json(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(value, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )
    temporary.replace(path)


def _write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "platform",
        "stable_id",
        "title",
        "official_source_url",
        "search_date",
        "query_hits",
        "source_terms",
        "metadata_result",
        "file_count",
        "final_decision",
        "canonical_record_id",
        "canonical_record_ids",
        "relationship_type",
        "reason",
        "decision_basis",
        "review_date",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def _load_catalog(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    return rows


def _normalized_url(value: Any) -> str:
    return str(value or "").strip().lower().rstrip("/")


def _normalized_doi_family(value: Any) -> str:
    doi = _normalized_url(value)
    doi = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", doi)
    if doi.startswith("10.6084/m9.figshare."):
        doi = re.sub(r"\.v\d+$", "", doi)
    elif doi.startswith("10.17632/"):
        doi = re.sub(r"\.\d+$", "", doi)
    return doi


def _repository_token(value: Any) -> str:
    token = _normalized_url(value)
    if not token:
        return ""
    token = re.sub(r"^https?://[^/]+/", "", token)
    return token


def _catalog_match(
    candidate: dict[str, Any],
    detail: dict[str, Any],
    catalog: list[dict[str, str]],
) -> str:
    # A publication DOI is deliberately excluded. A paper and its Figshare
    # supplementary tables can share that DOI without being the same dataset.
    candidate_urls = {
        _normalized_url(candidate.get("official_source_url")),
    }
    candidate_urls.discard("")
    candidate_dois = {
        _normalized_doi_family(detail.get("doi")),
        _normalized_doi_family(candidate.get("public_metadata", {}).get("doi")),
    }
    candidate_dois.discard("")
    stable_id = _repository_token(candidate.get("stable_id"))

    for row in catalog:
        row_urls = {
            _normalized_url(row.get(field))
            for field in (
                "download_url",
                "source_landing_page_url",
                "preferred_route_url",
                "canonical_resolver_url",
            )
        }
        row_urls.discard("")
        if candidate_urls.intersection(row_urls):
            return row["record_id"]

        row_doi = _normalized_doi_family(row.get("dataset_doi"))
        if row_doi and row_doi in candidate_dois:
            return row["record_id"]

        row_repository_id = _repository_token(row.get("repository_record_id"))
        if stable_id and row_repository_id and stable_id == row_repository_id:
            return row["record_id"]

        if stable_id and any(
            _repository_token(url).endswith(stable_id) for url in row_urls
        ):
            return row["record_id"]
    return ""


def _dryad_decisions(path: Path) -> dict[str, dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    mapped: dict[str, dict[str, str]] = {}
    for row in rows:
        source = row["final_decision"]
        if source == "existing_catalog_record":
            decision = "existing_catalog_record"
        elif source == "included_new_record":
            # These records are already present in the current catalog.
            decision = "existing_catalog_record"
        elif source == "excluded_out_of_scope_or_false_positive":
            decision = "excluded_not_eye_or_ophthalmology"
        elif source == "excluded_duplicate_or_upstream_terms":
            decision = "excluded_duplicate_or_alternate_deposit"
        elif source == "excluded_insufficient_reusable_ophthalmic_data":
            decision = "excluded_not_distinct_reusable_resource"
        else:
            raise ValueError(f"Unknown Dryad decision: {source}")
        mapped[row["doi"].lower()] = {
            "final_decision": decision,
            "canonical_record_id": row.get("final_catalog_slug")
            or row.get("matched_existing_record")
            or "",
            "canonical_record_ids": [
                value
                for value in [
                    row.get("final_catalog_slug")
                    or row.get("matched_existing_record")
                    or ""
                ]
                if value
            ],
            "relationship_type": row.get("relationship_type") or "",
            "reason": row.get("reason") or "",
            "decision_basis": "completed_dryad_record_review",
        }
    return mapped


def _dryad_model_use_decisions(path: Path) -> dict[str, dict[str, Any]]:
    """Load the later human/model-use review for Dryad records."""
    with path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    decisions: dict[str, dict[str, Any]] = {}
    for row in rows:
        doi = row["dataset_doi"].lower()
        if doi in decisions:
            raise ValueError(f"Duplicate Dryad model-use DOI: {doi}")
        included = row["headline_catalog_included"].strip().lower() == "true"
        decision = row["model_use_decision"]
        if included and decision != "included_human_or_human_derived_model_resource":
            raise ValueError(f"Inconsistent included Dryad decision: {doi}")
        excluded_mapping = {
            "excluded_nonhuman_or_nonhuman_derived": (
                "excluded_nonhuman_or_nonhuman_derived"
            ),
            "excluded_analysis_only": (
                "excluded_not_suitable_for_model_training_or_evaluation"
            ),
            "excluded_not_suitable_for_model_training_or_evaluation": (
                "excluded_not_suitable_for_model_training_or_evaluation"
            ),
            "excluded_relationship_only_resource": (
                "excluded_duplicate_or_alternate_deposit"
            ),
            "excluded_insufficient_model_use_evidence": (
                "excluded_insufficient_source_metadata"
            ),
        }
        if not included and decision not in excluded_mapping:
            raise ValueError(f"Unknown excluded Dryad model-use decision: {decision}")
        decisions[doi] = {
            "included": included,
            "final_decision": (
                "existing_catalog_record" if included else excluded_mapping[decision]
            ),
            "record_id": row["record_id"],
            "reason": row["reason"],
        }
    return decisions


def _load_overrides(path: Path) -> dict[str, dict[str, Any]]:
    if not path.exists():
        return {}
    payload = json.loads(path.read_text(encoding="utf-8"))
    overrides = payload.get("overrides") or []
    result: dict[str, dict[str, Any]] = {}
    for item in overrides:
        key = f"{item['platform']}:{item['stable_id']}"
        if item["final_decision"] not in FINAL_DECISIONS:
            raise ValueError(f"Invalid final decision for {key}")
        canonical_ids = item.get("canonical_record_ids")
        if canonical_ids is not None and (
            not isinstance(canonical_ids, list)
            or not all(isinstance(value, str) and value for value in canonical_ids)
        ):
            raise ValueError(f"Invalid canonical_record_ids for {key}")
        if key in result:
            raise ValueError(f"Duplicate override for {key}")
        result[key] = item
    return result


def _automatic_decision(
    candidate: dict[str, Any],
    detail: dict[str, Any],
    catalog_match: str,
) -> dict[str, str]:
    if catalog_match:
        return {
            "final_decision": "existing_catalog_record",
            "canonical_record_id": catalog_match,
            "canonical_record_ids": [catalog_match],
            "relationship_type": "same_resource",
            "reason": "The platform identifier or DOI is already represented by this catalog record.",
            "decision_basis": "identifier_match",
        }

    platform = str(candidate["platform"])
    title = _plain(candidate.get("title"))
    description = _plain(detail.get("description") or candidate.get("description"))
    tags = _plain(" ".join(candidate.get("public_metadata", {}).get("tags") or []))
    card = _plain(json.dumps(detail.get("card_data") or {}, ensure_ascii=True))
    combined = _SPACE_RE.sub(" ", f"{title} {description} {tags} {card}").strip()

    for pattern, record_id in _TITLE_ALIASES:
        if pattern.search(title):
            return {
                "final_decision": "excluded_duplicate_or_alternate_deposit",
                "canonical_record_id": record_id,
                "canonical_record_ids": [record_id],
                "relationship_type": "alternate_deposit_or_mirror",
                "reason": "The platform record names a resource already represented by the canonical catalog record.",
                "decision_basis": "reviewed_title_alias",
            }

    eye_match = bool(_EYE_RE.search(combined))
    false_match = bool(_FALSE_EYE_RE.search(combined))
    if not eye_match or (false_match and len(_EYE_RE.findall(combined)) <= 1):
        return {
            "final_decision": "excluded_not_eye_or_ophthalmology",
            "canonical_record_id": "",
            "relationship_type": "",
            "reason": "Public title and metadata do not describe an eye or ophthalmology data resource.",
            "decision_basis": "conservative_metadata_screen",
        }

    if platform == "figshare" and _SUPPLEMENT_RE.search(title):
        return {
            "final_decision": "excluded_not_distinct_reusable_resource",
            "canonical_record_id": "",
            "relationship_type": "",
            "reason": "The record is an article table, supplementary result, metadata-only record, or review output rather than a distinct reusable data resource.",
            "decision_basis": "resource_type_screen",
        }

    if platform in {"kaggle", "huggingface"} and _DERIVATIVE_RE.search(combined):
        return {
            "final_decision": "excluded_not_distinct_reusable_resource",
            "canonical_record_id": "",
            "relationship_type": "candidate_derivative_or_mirror",
            "reason": "Metadata describes a preprocessing variant, ordinary subset, composite packaging, model output, or other derived representation without a separately reviewed annotation or scientific contribution.",
            "decision_basis": "derived_resource_screen",
        }

    if (_INSUFFICIENT_TITLE_RE.match(_normalized(title)) and len(description) < 80) or (
        not description and not detail.get("card_data")
    ):
        return {
            "final_decision": "excluded_insufficient_source_metadata",
            "canonical_record_id": "",
            "relationship_type": "",
            "reason": "The public record does not expose enough provenance or scientific description to establish a distinct reusable resource.",
            "decision_basis": "metadata_completeness_screen",
        }

    return {
        "final_decision": "manual_review_pending",
        "canonical_record_id": "",
        "relationship_type": "",
        "reason": "The record appears eye-related and requires source-level eligibility and duplicate review.",
        "decision_basis": "manual_review_queue",
    }


def build(
    *,
    search_path: Path,
    details_path: Path,
    dryad_path: Path,
    dryad_model_review_path: Path,
    catalog_path: Path,
    overrides_path: Path,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    search = json.loads(search_path.read_text(encoding="utf-8"))
    details_payload = json.loads(details_path.read_text(encoding="utf-8"))
    details = {
        f"{item['platform']}:{item['stable_id']}": item
        for item in details_payload.get("records") or []
    }
    catalog = _load_catalog(catalog_path)
    dryad = _dryad_decisions(dryad_path)
    dryad_model_review = _dryad_model_use_decisions(dryad_model_review_path)
    overrides = _load_overrides(overrides_path)
    rows: list[dict[str, Any]] = []

    for platform in sorted(search["sources"]):
        source = search["sources"][platform]
        for candidate in source.get("candidates") or []:
            stable_id = str(candidate["stable_id"])
            key = f"{platform}:{stable_id}"
            detail = details.get(key, {})
            if platform == "dryad":
                decision = dryad[stable_id.lower()]
                model_use = dryad_model_review.get(stable_id.lower())
                if model_use and not model_use["included"]:
                    decision = {
                        "final_decision": model_use["final_decision"],
                        "canonical_record_id": model_use["record_id"],
                        "canonical_record_ids": [model_use["record_id"]],
                        "relationship_type": "screened_catalog_scope_exclusion",
                        "reason": model_use["reason"],
                        "decision_basis": "completed_dryad_human_model_use_review",
                    }
            else:
                match = _catalog_match(candidate, detail, catalog)
                decision = _automatic_decision(candidate, detail, match)
            if key in overrides:
                override = overrides[key]
                canonical_ids = list(override.get("canonical_record_ids") or [])
                if not canonical_ids and override.get("canonical_record_id"):
                    canonical_ids = [override["canonical_record_id"]]
                decision = {
                    "final_decision": override["final_decision"],
                    "canonical_record_id": override.get("canonical_record_id", "")
                    or (canonical_ids[0] if canonical_ids else ""),
                    "canonical_record_ids": canonical_ids,
                    "relationship_type": override.get("relationship_type", ""),
                    "reason": override["reason"],
                    "decision_basis": "human_reviewed_override",
                }
            if key in CURRENT_CANONICAL_POLICY:
                decision = dict(CURRENT_CANONICAL_POLICY[key])
            rows.append(
                {
                    "platform": platform,
                    "stable_id": stable_id,
                    "title": _plain(candidate.get("title")),
                    "official_source_url": candidate.get("official_source_url") or "",
                    "search_date": source.get("search_date") or "",
                    "query_hits": json.dumps(candidate.get("query_hits") or []),
                    "source_terms": detail.get("source_terms")
                    or candidate.get("source_terms")
                    or "",
                    "metadata_result": detail.get("metadata_result")
                    or "search_metadata_confirmed",
                    "file_count": detail.get("file_count")
                    if detail.get("file_count") is not None
                    else "",
                    **decision,
                    "canonical_record_ids": json.dumps(
                        decision.get("canonical_record_ids")
                        or (
                            [decision["canonical_record_id"]]
                            if decision.get("canonical_record_id")
                            else []
                        ),
                        ensure_ascii=True,
                    ),
                    "review_date": date.today().isoformat(),
                }
            )

    rows.sort(key=lambda row: (row["platform"], row["stable_id"].lower()))
    platform_counts: dict[str, dict[str, int]] = {}
    for platform in sorted(search["sources"]):
        subset = [row for row in rows if row["platform"] == platform]
        platform_counts[platform] = {
            "unique_search_hits": len(subset),
            **dict(sorted(Counter(row["final_decision"] for row in subset).items())),
        }
    source_search_status = {
        platform: {
            "status": search["sources"].get(platform, {}).get("status"),
            "result_set_complete": bool(
                search["sources"].get(platform, {}).get("result_set_complete")
            ),
            "unique_search_hits": (
                search["sources"].get(platform, {}).get("unique_hit_count")
            ),
        }
        for platform in WORKFLOW_SOURCES
    }
    all_requested_searches_complete = all(
        source["result_set_complete"] for source in source_search_status.values()
    )
    manual_review_complete = not any(
        row["final_decision"] == "manual_review_pending" for row in rows
    )
    summary = {
        "schema_version": "1.0",
        "search_snapshot": search_path.name,
        "screening_ledger": DEFAULT_CSV.name,
        "review_date": date.today().isoformat(),
        "catalog_record_count_at_screening": len(catalog),
        "workflow_sources": list(WORKFLOW_SOURCES),
        "source_search_status": source_search_status,
        "platform_counts": platform_counts,
        "overall_counts": {
            "unique_search_hits": len(rows),
            **dict(sorted(Counter(row["final_decision"] for row in rows).items())),
        },
        "all_requested_searches_complete": all_requested_searches_complete,
        "manual_review_complete": manual_review_complete,
        "manuscript_flow_ready": (
            all_requested_searches_complete and manual_review_complete
        ),
        "credential_values_serialized": False,
        "signed_or_download_urls_serialized": False,
        "interpretation": (
            "Counts are direct row counts. A credential_required source means that its "
            "search awaits the required platform credential; it is not an acquisition "
            "failure. Manuscript flow figures must not be generated while "
            "manuscript_flow_ready is false."
        ),
    }
    return rows, summary


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--search", type=Path, default=DEFAULT_SEARCH)
    parser.add_argument("--details", type=Path, default=DEFAULT_DETAILS)
    parser.add_argument("--dryad", type=Path, default=DEFAULT_DRYAD)
    parser.add_argument(
        "--dryad-model-review", type=Path, default=DEFAULT_DRYAD_MODEL_REVIEW
    )
    parser.add_argument("--catalog", type=Path, default=DEFAULT_CATALOG)
    parser.add_argument("--overrides", type=Path, default=DEFAULT_OVERRIDES)
    parser.add_argument("--csv-out", type=Path, default=DEFAULT_CSV)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    args = parser.parse_args()
    rows, summary = build(
        search_path=args.search,
        details_path=args.details,
        dryad_path=args.dryad,
        dryad_model_review_path=args.dryad_model_review,
        catalog_path=args.catalog,
        overrides_path=args.overrides,
    )
    _write_csv(args.csv_out, rows)
    _write_json(args.json_out, summary)
    print(json.dumps(summary["overall_counts"], indent=2))


if __name__ == "__main__":
    main()
