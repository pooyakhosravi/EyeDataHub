"""Build the completed manual decisions for the five-repository search.

The input ledgers are the public, record-level screening and canonical-
reconciliation artifacts.  The output is consumed by
``build_repository_screening_ledger.py`` so every non-Dryad record that
required manual review has a final, reproducible decision.

This file deliberately stores public identifiers and evidence summaries only.
It never reads credentials or serializes signed download URLs.
"""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
AUDIT = ROOT / "hub" / "audit"

MENDELEY_SCREEN = AUDIT / "mendeley_model_screen_decisions_2026-08-02.json"
FIGSHARE_SCREEN = AUDIT / "figshare_model_screen_decisions_2026-08-02.json"
OTHER_SCREEN = AUDIT / "kaggle_huggingface_model_screen_decisions_2026-08-02.json"
MENDELEY_RECONCILIATION = (
    AUDIT / "mendeley_canonical_reconciliation_2026-08-02.json"
)
OTHER_RECONCILIATION = (
    AUDIT / "figshare_kaggle_hf_canonical_reconciliation_2026-08-02.json"
)
OUTPUT = AUDIT / "repository_screening_overrides_2026-08-02.json"

EXPECTED_PLATFORM_COUNTS = {
    "figshare": 123,
    "huggingface": 78,
    "kaggle": 267,
    "mendeley": 751,
}

# A final source-level review targeted records that an earlier title-based pass
# had labelled as alternate deposits without a supported canonical target.  The
# corrections below preserve only exact, source-documented relationships.  A
# familiar dataset name in a title is not sufficient evidence of payload
# identity or provenance.
RESIDUAL_IDENTITY_CORRECTIONS: dict[tuple[str, str], dict[str, Any]] = {
    ("figshare", "14416602"): {
        "final_decision": "excluded_not_distinct_reusable_resource",
        "canonical_record_ids": [],
        "relationship_type": "",
        "reason": (
            "The deposit contains a performance-metrics table for SA-Net, not "
            "reusable ophthalmic images, labels, or participant-level data."
        ),
    },
    ("huggingface", "AlexeyGHT/Fundus_CFP"): {
        "final_decision": "excluded_insufficient_source_metadata",
        "canonical_record_ids": [],
        "relationship_type": "",
        "reason": (
            "The 7,000 image/prompt rows are byte-identical to the public "
            "Yugant-S/Fundus_CFP copy, but neither source documents an upstream "
            "canonical resource."
        ),
    },
    ("huggingface", "BenchmarkDatasets/Diabetic_Retinopathy_Debrecen"): {
        "final_decision": "excluded_insufficient_source_metadata",
        "canonical_record_ids": [],
        "relationship_type": "",
        "reason": (
            "The card describes a tabular benchmark task but provides no source "
            "identifier or provenance linking it to a catalog resource."
        ),
    },
    ("huggingface", "jafermarq/retinamnist"): {
        "final_decision": "excluded_insufficient_source_metadata",
        "canonical_record_ids": [],
        "relationship_type": "",
        "reason": (
            "The repository exposes resized image configurations but no source "
            "card or provenance that identifies the upstream data."
        ),
    },
    ("huggingface", "RubySpeedy/Diabetic-Retinopathy-Kaggle"): {
        "final_decision": "excluded_insufficient_source_metadata",
        "canonical_record_ids": [],
        "relationship_type": "",
        "reason": (
            "The repository lists 35,126 images but supplies no source card or "
            "citation that establishes the underlying resource."
        ),
    },
    ("huggingface", "Tejaswini628/aptos-fundus-images"): {
        "final_decision": "excluded_insufficient_source_metadata",
        "canonical_record_ids": [],
        "relationship_type": "",
        "reason": (
            "The name and file layout suggest APTOS, but the public metadata does "
            "not explicitly document the upstream source."
        ),
    },
    ("huggingface", "WhoCares10/RetinaFundus"): {
        "final_decision": "excluded_duplicate_or_alternate_deposit",
        "canonical_record_ids": ["idrid"],
        "relationship_type": "subset_of",
        "reason": (
            "The official file listing explicitly identifies an IDRiD testing-set "
            "subset rather than a distinct resource."
        ),
    },
    ("huggingface", "Yugant-S/Fundus_CFP"): {
        "final_decision": "excluded_insufficient_source_metadata",
        "canonical_record_ids": [],
        "relationship_type": "",
        "reason": (
            "The payload is byte-identical to the public AlexeyGHT/Fundus_CFP "
            "copy, but neither source documents an upstream canonical resource."
        ),
    },
    ("kaggle", "agattadahalli/smdg-modified"): {
        "final_decision": "excluded_not_distinct_reusable_resource",
        "canonical_record_ids": ["smdg"],
        "relationship_type": "derived_from",
        "reason": (
            "The source identifies SMDG-19 and adds resized and brightened copies "
            "without a new cohort or annotation layer."
        ),
    },
    ("kaggle", "fahimaislam1812/myopia"): {
        "final_decision": "excluded_duplicate_or_alternate_deposit",
        "canonical_record_ids": ["palm"],
        "relationship_type": "mirror_of",
        "reason": (
            "The description explicitly identifies PALM and reproduces its "
            "1,200-image scope and annotations."
        ),
    },
    ("kaggle", "federicorausa/diabetic-retinopathy-debrecen"): {
        "final_decision": "excluded_insufficient_source_metadata",
        "canonical_record_ids": [],
        "relationship_type": "",
        "reason": (
            "The page refers to a Kaggle competition, but no current catalog "
            "record or source evidence establishes an exact payload identity."
        ),
    },
    ("kaggle", "ferdiu/nevart-eye-tracking"): {
        "final_decision": "excluded_insufficient_source_metadata",
        "canonical_record_ids": [],
        "relationship_type": "",
        "reason": (
            "The deprecated page points to a successor Kaggle record, but neither "
            "has an approved canonical identity or sufficient source provenance."
        ),
    },
    ("kaggle", "ferencjuhsz/refuge2-and-refuge2cross-dataset"): {
        "final_decision": "excluded_not_distinct_reusable_resource",
        "canonical_record_ids": ["refuge2"],
        "relationship_type": "has_component",
        "reason": (
            "The package contains a documented REFUGE2 component plus a Cross "
            "component whose provenance is not separately resolvable."
        ),
    },
    ("kaggle", "gunavenkatdoddi/eye-diseases-classification"): {
        "final_decision": "excluded_insufficient_source_metadata",
        "canonical_record_ids": [],
        "relationship_type": "",
        "reason": (
            "The description names several general sources but supplies no exact "
            "component versions, manifest, or authoritative source links."
        ),
    },
    ("kaggle", "hamza202404/drdm1-six-fundus-images-datasets-by-mian-hamza"): {
        "final_decision": "excluded_not_distinct_reusable_resource",
        "canonical_record_ids": [
            "eyepacs",
            "aptos2019",
            "ddr",
            "deepdrid",
            "idrid",
        ],
        "relationship_type": "derived_from",
        "reason": (
            "The source explicitly describes a selected and customized merge of "
            "five supported canonical fundus resources; its additional MESSIDOR "
            "reference is not specific enough to map to Messidor-2."
        ),
    },
    ("kaggle", "harshitkulkarni07/minor-project-dataset"): {
        "final_decision": "excluded_not_distinct_reusable_resource",
        "canonical_record_ids": ["eyepacs", "aptos2019", "idrid"],
        "relationship_type": "derived_from",
        "reason": (
            "The source explicitly combines EyePACS, APTOS-2019, and IDRiD and "
            "then downsamples and augments them."
        ),
    },
    ("kaggle", "ipythonx/retinal-vessel-segmentation"): {
        "final_decision": "excluded_not_distinct_reusable_resource",
        "canonical_record_ids": ["chase_db1", "drive", "hrf", "stare"],
        "relationship_type": "derived_from",
        "reason": (
            "The source explicitly packages CHASE_DB1, DRIVE, HRF, and STARE "
            "rather than introducing a new underlying collection."
        ),
    },
    ("kaggle", "javierleonelrojas/technische-fakultt-high-resolutiom-fundus"): {
        "final_decision": "excluded_duplicate_or_alternate_deposit",
        "canonical_record_ids": ["hrf"],
        "relationship_type": "mirror_of",
        "reason": (
            "The description links to the official High-Resolution Fundus image "
            "database and identifies the same resource."
        ),
    },
    ("kaggle", "jeremypoveda/fondo-del-ojo-normal-glaucoma-retinopatia"): {
        "final_decision": "excluded_not_distinct_reusable_resource",
        "canonical_record_ids": [
            "odir2019",
            "g1020",
            "beh",
            "drishti_gs",
            "fives",
            "hrf",
            "jsiec",
            "papila",
            "refuge2018",
            "acrima",
            "rimone_dl",
        ],
        "relationship_type": "derived_from",
        "reason": (
            "The source describes a union of the listed canonical glaucoma and "
            "fundus resources; vague or unresolved components were not mapped."
        ),
    },
    ("kaggle", "pradosh123/retinal-vessel-segmentation-combined"): {
        "final_decision": "excluded_not_distinct_reusable_resource",
        "canonical_record_ids": ["drive", "hrf", "chase_db1", "stare"],
        "relationship_type": "derived_from",
        "reason": (
            "The source explicitly combines DRIVE, HRF, CHASE_DB1, and STARE in "
            "repackaged train and test folders."
        ),
    },
    ("kaggle", "samriddhibagchi/ddr-dataset-credits-to-authors"): {
        "final_decision": "excluded_insufficient_source_metadata",
        "canonical_record_ids": [],
        "relationship_type": "",
        "reason": (
            "The page has an empty description, so its title alone cannot establish "
            "that the payload is the canonical DDR resource."
        ),
    },
    ("kaggle", "samriddhibagchi/unified-retinal-lesion-dataset"): {
        "final_decision": "excluded_insufficient_source_metadata",
        "canonical_record_ids": [],
        "relationship_type": "",
        "reason": (
            "The page provides no description, provenance, or manifest from which "
            "an underlying resource identity can be established."
        ),
    },
    ("kaggle", "shaowenhuang/octmnist-shaowen"): {
        "final_decision": "excluded_not_distinct_reusable_resource",
        "canonical_record_ids": [],
        "relationship_type": "mirror_of_external_unlisted_source",
        "reason": (
            "The counts and splits identify an OCTMNIST copy, but OCTMNIST is not "
            "represented by a current canonical catalog record."
        ),
    },
    ("kaggle", "soumicksarker/openeds-dataset"): {
        "final_decision": "excluded_not_distinct_reusable_resource",
        "canonical_record_ids": [],
        "relationship_type": "mirror_of_external_unlisted_source",
        "reason": (
            "The source reproduces OpenEDS cohort and subset counts, but OpenEDS is "
            "not represented by a current canonical catalog record."
        ),
    },
    ("kaggle", "sovitrath/drive-trainvalidation-split-dataset"): {
        "final_decision": "excluded_duplicate_or_alternate_deposit",
        "canonical_record_ids": ["drive"],
        "relationship_type": "derived_from",
        "reason": (
            "The source explicitly reorganizes DRIVE's 20 training and 20 test "
            "images into a train/validation split."
        ),
    },
    ("kaggle", "srinjoybhuiya/drive-retinal-vessel-segmentation-pixelwise"): {
        "final_decision": "excluded_insufficient_source_metadata",
        "canonical_record_ids": [],
        "relationship_type": "",
        "reason": (
            "The title and 20/20 CSV layout do not document the underlying images "
            "or establish their provenance."
        ),
    },
    ("kaggle", "sshikamaru/glaucoma-detection"): {
        "final_decision": "excluded_insufficient_source_metadata",
        "canonical_record_ids": [],
        "relationship_type": "",
        "reason": (
            "The page makes generic image and OCT claims without a named source, "
            "file inventory, or primary provenance."
        ),
    },
    ("kaggle", "subhajournal/drimdb-diabetic-retinopathy-images-database"): {
        "final_decision": "excluded_insufficient_source_metadata",
        "canonical_record_ids": [],
        "relationship_type": "",
        "reason": (
            "The page names DRIMDB but supplies no authoritative source link or "
            "payload evidence that supports an exact catalog target."
        ),
    },
    ("kaggle", "sunfish141/ddr-segmentation"): {
        "final_decision": "excluded_insufficient_source_metadata",
        "canonical_record_ids": ["ddr"],
        "relationship_type": "derived_from",
        "reason": (
            "The source names DDR, but the unavailable inventory and uploader-"
            "generated masks do not establish an exact mirror or a sufficiently "
            "documented distinct annotation resource."
        ),
    },
    ("kaggle", "tmtrnhelloworld/idridsplittedkeepimage"): {
        "final_decision": "excluded_duplicate_or_alternate_deposit",
        "canonical_record_ids": ["idrid"],
        "relationship_type": "derived_from",
        "reason": (
            "The source explicitly describes an 80/10/10 re-split of IDRiD without "
            "a distinct annotation or task layer."
        ),
    },
    ("kaggle", "umairinayat/retinal-vessel-segmentation-datasets"): {
        "final_decision": "excluded_not_distinct_reusable_resource",
        "canonical_record_ids": ["fives", "hrf", "chase_db1", "stare", "drive"],
        "relationship_type": "derived_from",
        "reason": (
            "The source explicitly packages five named canonical retinal-vessel "
            "datasets without an independent cohort or annotation layer."
        ),
    },
    ("kaggle", "varshinir1704/mini-project"): {
        "final_decision": "excluded_insufficient_source_metadata",
        "canonical_record_ids": [],
        "relationship_type": "",
        "reason": (
            "The empty description and unknown terms provide no evidence identifying "
            "an underlying ODIR or other canonical payload."
        ),
    },
    ("kaggle", "victorlemosml/refuge2"): {
        "final_decision": "excluded_duplicate_or_alternate_deposit",
        "canonical_record_ids": ["refuge2"],
        "relationship_type": "mirror_of",
        "reason": (
            "The description identifies the REFUGE2 challenge tasks without a "
            "distinct scientific data layer."
        ),
    },
    ("kaggle", "yakeworld126/openeds"): {
        "final_decision": "excluded_insufficient_source_metadata",
        "canonical_record_ids": [],
        "relationship_type": "",
        "reason": (
            "The page names OpenEDS and claims corrected labels but provides no "
            "primary release or payload evidence for the asserted corrections."
        ),
    },
    ("kaggle", "yxmauw/eye-disease-class-bg-rm"): {
        "final_decision": "excluded_insufficient_source_metadata",
        "canonical_record_ids": [],
        "relationship_type": "",
        "reason": (
            "The source documents background removal from a mixed external Kaggle "
            "composite whose component identities are not exactly resolvable."
        ),
    },
    ("kaggle", "zionfuo/drive2004"): {
        "final_decision": "excluded_duplicate_or_alternate_deposit",
        "canonical_record_ids": ["drive"],
        "relationship_type": "mirror_of",
        "reason": (
            "The source explicitly identifies the DRIVE database and official "
            "project page without adding a new data layer."
        ),
    },
}

SCREEN_DECISION_MAP = {
    "duplicate_or_alternate": "excluded_duplicate_or_alternate_deposit",
    "exclude_insufficient": "excluded_insufficient_source_metadata",
    "exclude_nonhuman": "excluded_nonhuman_or_nonhuman_derived",
    "exclude_not_model_resource": (
        "excluded_not_suitable_for_model_training_or_evaluation"
    ),
    "exclude_not_ophthalmology": "excluded_not_eye_or_ophthalmology",
}

CONFIRMATION_DECISION_MAP = {
    "duplicate_or_alternate": "excluded_duplicate_or_alternate_deposit",
    "exclude_insufficient": "excluded_insufficient_source_metadata",
    "exclude_nonhuman": "excluded_nonhuman_or_nonhuman_derived",
    "exclude_not_model_resource": (
        "excluded_not_suitable_for_model_training_or_evaluation"
    ),
    # One Mendeley row passed the source-level screen but was rejected during
    # canonical review because it contains figure panels rather than a reusable
    # observation-level resource.
    "confirmed_include_new": (
        "excluded_not_suitable_for_model_training_or_evaluation"
    ),
}


def _load_records(path: Path) -> list[dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    rows = payload.get("records")
    if not isinstance(rows, list):
        raise ValueError(f"{path.name} does not contain a records list")
    return rows


def _reconciliation_index() -> dict[tuple[str, str], dict[str, Any]]:
    indexed: dict[tuple[str, str], dict[str, Any]] = {}
    for row in _load_records(MENDELEY_RECONCILIATION):
        indexed[("mendeley", str(row["stable_id"]))] = row
    for row in _load_records(OTHER_RECONCILIATION):
        indexed[(str(row["platform"]), str(row["stable_id"]))] = row
    if len(indexed) != 199:
        raise ValueError(f"Expected 199 reconciled candidates, observed {len(indexed)}")
    return indexed


def _canonical_target(row: dict[str, Any]) -> str:
    value = row.get("canonical_target") or row.get("proposed_canonical_slug") or ""
    return str(value).strip()


def _initial_duplicate_targets(
    row: dict[str, Any],
    stable_to_canonical: dict[str, str],
) -> list[str]:
    targets = row.get("relationship_targets") or []
    if isinstance(targets, str):
        targets = [targets]
    translated: list[str] = []
    for target in targets:
        token = str(target).strip()
        mapped = stable_to_canonical.get(token, token)
        if mapped and mapped not in translated:
            translated.append(mapped)

    # Figshare proposals store concise relationship strings instead of a
    # separate target array.  Only explicit, unambiguous catalog identifiers
    # are promoted here; uncertain prose stays in the reason field.
    relationship = str(row.get("relationships") or "")
    explicit_figshare_targets = {
        "14416602": [],
        "19081862": ["aptos2019"],
        "22212787": ["fire"],
        "24549217": ["acrima", "refuge2018"],
        "30520775": ["natural_scene_eye_tracking_collection"],
        "32592837": ["slp_vld"],
        "32593101": ["slp_vld"],
        "32593173": ["slp_vld"],
    }
    if row.get("stable_id") in explicit_figshare_targets:
        translated = explicit_figshare_targets[str(row["stable_id"])]
    elif relationship.startswith("component_of:"):
        translated = [relationship.split(":", 1)[1].split(";", 1)[0].strip()]
    return translated


def _reason(row: dict[str, Any], final_decision: str) -> str:
    for field in ("concise_reason", "reason", "rationale"):
        value = str(row.get(field) or "").strip()
        if value:
            return value
    defaults = {
        "excluded_duplicate_or_alternate_deposit": (
            "Record-level review identified an alternate deposit, mirror, "
            "component, or ordinary repackaging rather than a new canonical resource."
        ),
        "excluded_insufficient_source_metadata": (
            "The public source did not provide enough current evidence to establish "
            "a distinct reusable resource."
        ),
        "excluded_nonhuman_or_nonhuman_derived": (
            "The source describes nonhuman data without a separable human or "
            "human-derived component."
        ),
        "excluded_not_suitable_for_model_training_or_evaluation": (
            "The deposit does not contain observation-level data or a distinct "
            "annotation layer suitable for model development or evaluation."
        ),
        "excluded_not_eye_or_ophthalmology": (
            "The source is not an eye or ophthalmology data resource."
        ),
    }
    return defaults[final_decision]


def build() -> dict[str, Any]:
    reconciliation = _reconciliation_index()
    stable_to_canonical = {
        stable_id: _canonical_target(row)
        for (_, stable_id), row in reconciliation.items()
        if _canonical_target(row)
    }

    batches: list[tuple[str | None, list[dict[str, Any]]]] = [
        ("mendeley", _load_records(MENDELEY_SCREEN)),
        ("figshare", _load_records(FIGSHARE_SCREEN)),
        (None, _load_records(OTHER_SCREEN)),
    ]
    overrides: list[dict[str, Any]] = []

    for fixed_platform, rows in batches:
        for row in rows:
            platform = fixed_platform or str(row["platform"])
            stable_id = str(row["stable_id"])
            screen_decision = str(row["decision"])
            key = (platform, stable_id)
            targets: list[str] = []
            relationship_type = ""

            if screen_decision == "include_new":
                if key not in reconciliation:
                    raise ValueError(f"Missing reconciliation for {platform}:{stable_id}")
                reconciled = reconciliation[key]
                action = str(reconciled["canonical_action"])
                target = _canonical_target(reconciled)
                if action in {"new_canonical_record", "alternate_source_to_new"}:
                    if not target:
                        raise ValueError(f"Missing canonical target for {platform}:{stable_id}")
                    final_decision = "included_new_record"
                    targets = [target]
                    relationship_type = (
                        "canonical_resource"
                        if action == "new_canonical_record"
                        else "alternate_source_for_new_canonical_resource"
                    )
                elif action in {"alternate_source_to_existing", "relationship_only"}:
                    final_decision = "excluded_duplicate_or_alternate_deposit"
                    targets = [target] if target else []
                    relationship_type = str(
                        reconciled.get("relationship_type")
                        or "alternate_deposit_or_component"
                    )
                elif action == "exclude_after_reconciliation":
                    confirmation = str(reconciled["source_confirmation"])
                    final_decision = str(
                        reconciled.get("final_screening_decision")
                        or CONFIRMATION_DECISION_MAP[confirmation]
                    )
                    relationship_type = ""
                else:
                    raise ValueError(f"Unknown reconciliation action: {action}")
                source_for_reason = reconciled
            else:
                final_decision = SCREEN_DECISION_MAP[screen_decision]
                source_for_reason = row
                if final_decision == "excluded_duplicate_or_alternate_deposit":
                    targets = _initial_duplicate_targets(row, stable_to_canonical)
                    relationship_type = str(
                        row.get("relationship_type")
                        or "alternate_deposit_or_repackaging"
                    )

            override: dict[str, Any] = {
                "platform": platform,
                "stable_id": stable_id,
                "final_decision": final_decision,
                "canonical_record_ids": targets,
                "relationship_type": relationship_type,
                "reason": _reason(source_for_reason, final_decision),
            }
            if targets:
                override["canonical_record_id"] = targets[0]
            overrides.append(override)

    override_by_key = {
        (row["platform"], row["stable_id"]): row for row in overrides
    }
    missing_corrections = sorted(
        set(RESIDUAL_IDENTITY_CORRECTIONS) - set(override_by_key)
    )
    if missing_corrections:
        raise ValueError(
            "Residual identity corrections reference missing rows: "
            f"{missing_corrections}"
        )
    for key, correction in RESIDUAL_IDENTITY_CORRECTIONS.items():
        override = override_by_key[key]
        override.update(correction)
        targets = list(correction["canonical_record_ids"])
        if targets:
            override["canonical_record_id"] = targets[0]
        else:
            override.pop("canonical_record_id", None)

    keys = [(row["platform"], row["stable_id"]) for row in overrides]
    if len(overrides) != 1219 or len(set(keys)) != 1219:
        raise ValueError(
            f"Expected 1,219 unique manual decisions, observed {len(overrides)} "
            f"rows and {len(set(keys))} keys"
        )
    platform_counts = Counter(row["platform"] for row in overrides)
    if dict(sorted(platform_counts.items())) != EXPECTED_PLATFORM_COUNTS:
        raise ValueError(f"Unexpected platform coverage: {dict(platform_counts)}")
    if any(row["final_decision"] == "manual_review_pending" for row in overrides):
        raise ValueError("Completed override ledger contains a pending decision")

    payload = {
        "schema_version": "2.0",
        "review_date": "2026-08-02",
        "status": "completed_record_level_manual_review",
        "scope": (
            "Human or human-derived eye and ophthalmology resources containing "
            "observation-level data or a distinct annotation layer suitable for "
            "model development or evaluation."
        ),
        "input_record_count": 1219,
        "platform_counts": dict(sorted(platform_counts.items())),
        "decision_counts": dict(
            sorted(Counter(row["final_decision"] for row in overrides).items())
        ),
        "credential_values_serialized": False,
        "signed_or_download_urls_serialized": False,
        "local_absolute_paths_serialized": False,
        "overrides": sorted(
            overrides, key=lambda row: (row["platform"], row["stable_id"].lower())
        ),
    }
    temporary = OUTPUT.with_suffix(OUTPUT.suffix + ".tmp")
    temporary.write_text(
        json.dumps(payload, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )
    temporary.replace(OUTPUT)
    return payload


if __name__ == "__main__":
    result = build()
    print(
        json.dumps(
            {
                "input_record_count": result["input_record_count"],
                "platform_counts": result["platform_counts"],
                "decision_counts": result["decision_counts"],
            },
            indent=2,
        )
    )
