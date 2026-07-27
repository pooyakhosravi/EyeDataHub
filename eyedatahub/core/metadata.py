"""Conservative metadata enrichment for catalog and acquisition records.

The historical EyeDataHub classes expose a compact ``DatasetInfo`` object.  This
module derives the richer, independent dimensions needed by the command-line
preflight and frozen scientific snapshots without pretending that missing
source information is false.  Explicit values supplied by a dataset class take
precedence over every derived value.
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional
from urllib.parse import urlparse


ACCESS_FRICTION_VALUES = {
    "anonymous_direct",
    "self_service_authenticated",
    "self_service_clickthrough",
    "controlled_or_manual",
    "author_contact",
    "model_to_data_or_secure_environment",
    "unavailable",
    "unverified",
}

ACQUISITION_SUPPORT_VALUES = {
    "end_to_end_tested",
    "transfer_tested_partial",
    "loader_implemented_not_live_tested",
    "standard_platform_supported",
    "guided_instructions_only",
    "manual_access_blocked",
    "unsupported",
    "unavailable",
}

AVAILABILITY_STATUS_VALUES = {"available", "unavailable", "unverified"}

TERMS_SCOPE_VALUES = {
    "dataset_files",
    "metadata_only",
    "code_only",
    "publication_only",
    "challenge_participation",
    "mixed_components",
    "unknown",
}

BOOL_OR_UNKNOWN_FIELDS = (
    "requires_registration",
    "requires_authentication",
    "requires_api_token",
    "requires_clickthrough",
    "requires_manual_approval",
    "requires_data_use_agreement",
    "requires_author_contact",
    "requires_payment",
)

STANDARD_PLATFORM_BACKENDS = {
    "zenodo",
    "figshare",
    "mendeley",
    "dryad",
    "kaggle",
    "huggingface",
    "physionet",
}

DIRECT_BACKENDS = {"direct", "github", "gdrive"}

# These records have a non-manual historical backend label but their current
# class only provides instructions.  Keeping them explicit prevents the paper
# and CLI from reporting an automated transfer that does not exist.
GUIDED_ONLY_SLUGS = {
    "airogs",
    "papila",
    "acrima",
    "harvard_gdp",
    "oculoscope",
    "uwf_dr",
    "tear_meniscus",
}

# Date-stamped acquisition evidence. These statuses describe exactly
# what was exercised for the catalog release; they are deliberately narrower
# than loader implementation or platform support.
PARTIAL_TRANSFER_TESTED_SLUGS = {
    "as_oct_keratitis",
    "coph100",
    "dryad_gcc_glaucoma",
    "fives",
    "grape",
    "jsiec",
    "mcoa",
    "migs_video",
    "mm_retinal_reason",
    "perg_ioba",
    "rvo_me",
    "tear_meniscus",
    "tom500",
}

END_TO_END_TESTED_SLUGS = {"ophthalwechat"}

# High-confidence route exceptions that cannot be recovered safely from the
# legacy ``download_type`` value alone.
ACCESS_OVERRIDES: Dict[str, Dict[str, Any]] = {
    "brset": {
        "access_friction": "controlled_or_manual",
        "requires_registration": True,
        "requires_authentication": True,
        "requires_clickthrough": True,
        "requires_manual_approval": True,
        "requires_data_use_agreement": True,
    },
    "mbrset": {
        "access_friction": "controlled_or_manual",
        "requires_registration": True,
        "requires_authentication": True,
        "requires_clickthrough": True,
        "requires_manual_approval": True,
        "requires_data_use_agreement": True,
    },
    "justraigs": {
        "access_friction": "self_service_clickthrough",
        "requires_registration": True,
        "requires_authentication": True,
        "requires_clickthrough": True,
        "requires_manual_approval": False,
        "requires_data_use_agreement": False,
    },
    "corn_pro": {
        "access_friction": "controlled_or_manual",
        "requires_registration": True,
        "requires_authentication": True,
        "requires_manual_approval": True,
        "requires_data_use_agreement": True,
    },
    # Current official routes checked for the dated catalog snapshot. These legacy
    # records use ``download_type=manual`` because no automated loader exists;
    # access friction is therefore recorded independently from automation.
    "agar300": {
        "access_friction": "self_service_authenticated",
        "requires_registration": True,
        "requires_authentication": True,
        "requires_api_token": False,
        "requires_clickthrough": False,
        "requires_manual_approval": False,
        "requires_data_use_agreement": False,
        "requires_author_contact": False,
        "requires_payment": False,
        "availability_status": "available",
        "route_check_result": "acquisition_route_verified",
    },
    "angioreport": {
        "access_friction": "self_service_clickthrough",
        "requires_registration": True,
        "requires_authentication": True,
        "requires_api_token": False,
        "requires_clickthrough": True,
        "requires_manual_approval": False,
        "requires_data_use_agreement": False,
        "requires_author_contact": False,
        "requires_payment": False,
        "availability_status": "available",
        "route_check_result": "acquisition_route_verified",
    },
    "casia_iris_v4": {
        "access_friction": "anonymous_direct",
        "requires_registration": False,
        "requires_authentication": False,
        "requires_api_token": False,
        "requires_clickthrough": False,
        "requires_manual_approval": False,
        "requires_data_use_agreement": False,
        "requires_author_contact": False,
        "requires_payment": False,
        "availability_status": "available",
        "route_check_result": "acquisition_route_verified",
    },
    "chase_db1": {
        "access_friction": "anonymous_direct",
        "requires_registration": False,
        "requires_authentication": False,
        "requires_api_token": False,
        "requires_clickthrough": False,
        "requires_manual_approval": False,
        "requires_data_use_agreement": False,
        "requires_author_contact": False,
        "requires_payment": False,
        "availability_status": "available",
        "route_check_result": "acquisition_route_verified",
    },
    "drive": {
        "access_friction": "self_service_authenticated",
        "requires_registration": True,
        "requires_authentication": True,
        "requires_api_token": False,
        "requires_clickthrough": False,
        "requires_manual_approval": False,
        "requires_data_use_agreement": False,
        "requires_author_contact": False,
        "requires_payment": False,
        "availability_status": "available",
        "route_check_result": "acquisition_route_verified",
    },
    "duke_amd_chiu": {
        "access_friction": "anonymous_direct",
        "requires_registration": False,
        "requires_authentication": False,
        "requires_api_token": False,
        "requires_clickthrough": False,
        "requires_manual_approval": False,
        "requires_data_use_agreement": False,
        "requires_author_contact": False,
        "requires_payment": False,
        "availability_status": "available",
        "route_check_result": "acquisition_route_verified",
    },
    "duke_rpedc": {
        "access_friction": "anonymous_direct",
        "requires_registration": False,
        "requires_authentication": False,
        "requires_api_token": False,
        "requires_clickthrough": False,
        "requires_manual_approval": False,
        "requires_data_use_agreement": False,
        "requires_author_contact": False,
        "requires_payment": False,
        "availability_status": "available",
        "route_check_result": "acquisition_route_verified",
    },
    "eth_xgaze": {
        "access_friction": "controlled_or_manual",
        "requires_registration": True,
        "requires_authentication": True,
        "requires_api_token": False,
        "requires_clickthrough": True,
        "requires_manual_approval": True,
        "requires_data_use_agreement": True,
        "requires_author_contact": False,
        "requires_payment": False,
        "geographic_or_institutional_restriction": "institutional_email_required",
        "availability_status": "available",
        "route_check_result": "acquisition_route_verified",
    },
    "fang_sbsdi_oct": {
        "access_friction": "anonymous_direct",
        "requires_registration": False,
        "requires_authentication": False,
        "requires_api_token": False,
        "requires_clickthrough": False,
        "requires_manual_approval": False,
        "requires_data_use_agreement": False,
        "requires_author_contact": False,
        "requires_payment": False,
        "availability_status": "available",
        "route_check_result": "acquisition_route_verified",
    },
    "hrf": {
        "access_friction": "anonymous_direct",
        "requires_registration": False,
        "requires_authentication": False,
        "requires_api_token": False,
        "requires_clickthrough": False,
        "requires_manual_approval": False,
        "requires_data_use_agreement": False,
        "requires_author_contact": False,
        "requires_payment": False,
        "availability_status": "available",
        "route_check_result": "acquisition_route_verified",
    },
    "ichallenge_oct": {
        "access_friction": "self_service_authenticated",
        "requires_registration": True,
        "requires_authentication": True,
        "requires_api_token": False,
        "requires_clickthrough": False,
        "requires_manual_approval": False,
        "requires_data_use_agreement": False,
        "requires_author_contact": False,
        "requires_payment": False,
        "availability_status": "available",
        "route_check_result": "acquisition_route_verified",
    },
    "insegcat": {
        "access_friction": "self_service_clickthrough",
        "requires_registration": False,
        "requires_authentication": False,
        "requires_api_token": False,
        "requires_clickthrough": True,
        "requires_manual_approval": False,
        "requires_data_use_agreement": False,
        "requires_author_contact": False,
        "requires_payment": False,
        "availability_status": "available",
        "route_check_result": "acquisition_route_verified",
    },
    "lmod_plus": {
        "access_friction": "anonymous_direct",
        "requires_registration": False,
        "requires_authentication": False,
        "requires_api_token": False,
        "requires_clickthrough": False,
        "requires_manual_approval": False,
        "requires_data_use_agreement": False,
        "requires_author_contact": False,
        "requires_payment": False,
        "availability_status": "available",
        "route_check_result": "acquisition_route_verified",
        "preferred_route_url": "https://yaleedu-my.sharepoint.com/",
        "preferred_route_type": "official_cloud_file_share",
    },
    "lpw": {
        "access_friction": "anonymous_direct",
        "requires_registration": False,
        "requires_authentication": False,
        "requires_api_token": False,
        "requires_clickthrough": False,
        "requires_manual_approval": False,
        "requires_data_use_agreement": False,
        "requires_author_contact": False,
        "requires_payment": False,
        "availability_status": "available",
        "route_check_result": "acquisition_route_verified",
    },
    "mpii_gaze": {
        "access_friction": "anonymous_direct",
        "requires_registration": False,
        "requires_authentication": False,
        "requires_api_token": False,
        "requires_clickthrough": False,
        "requires_manual_approval": False,
        "requires_data_use_agreement": False,
        "requires_author_contact": False,
        "requires_payment": False,
        "availability_status": "available",
        "route_check_result": "acquisition_route_verified",
    },
    "oct_cirrus": {
        "access_friction": "anonymous_direct",
        "requires_registration": False,
        "requires_authentication": False,
        "requires_api_token": False,
        "requires_clickthrough": False,
        "requires_manual_approval": False,
        "requires_data_use_agreement": False,
        "requires_author_contact": False,
        "requires_payment": False,
        "availability_status": "available",
        "route_check_result": "acquisition_route_verified",
    },
    "octa_500": {
        "access_friction": "author_contact",
        "requires_registration": True,
        "requires_authentication": True,
        "requires_api_token": False,
        "requires_clickthrough": False,
        "requires_manual_approval": False,
        "requires_data_use_agreement": False,
        "requires_author_contact": True,
        "requires_payment": False,
        "availability_status": "available",
        "route_check_result": "acquisition_route_verified",
    },
    "rasti_oct": {
        "access_friction": "anonymous_direct",
        "requires_registration": False,
        "requires_authentication": False,
        "requires_api_token": False,
        "requires_clickthrough": False,
        "requires_manual_approval": False,
        "requires_data_use_agreement": False,
        "requires_author_contact": False,
        "requires_payment": False,
        "availability_status": "available",
        "route_check_result": "acquisition_route_verified",
    },
    "refuge2018": {
        "access_friction": "controlled_or_manual",
        "requires_registration": True,
        "requires_authentication": True,
        "requires_api_token": False,
        "requires_clickthrough": True,
        "requires_manual_approval": True,
        "requires_data_use_agreement": False,
        "requires_author_contact": True,
        "requires_payment": False,
        "availability_status": "available",
        "route_check_result": "acquisition_route_verified",
    },
    "roc": {
        "access_friction": "anonymous_direct",
        "requires_registration": False,
        "requires_authentication": False,
        "requires_api_token": False,
        "requires_clickthrough": False,
        "requires_manual_approval": False,
        "requires_data_use_agreement": False,
        "requires_author_contact": False,
        "requires_payment": False,
        "availability_status": "available",
        "route_check_result": "acquisition_route_verified",
        "route_check_notes": "The former registration service is closed; the official page now exposes the image files directly.",
    },
    "stage_task1": {
        "access_friction": "self_service_clickthrough",
        "requires_registration": True,
        "requires_authentication": True,
        "requires_api_token": False,
        "requires_clickthrough": True,
        "requires_manual_approval": False,
        "requires_data_use_agreement": False,
        "requires_author_contact": False,
        "requires_payment": False,
        "geographic_or_institutional_restriction": "real_name_platform_verification_required",
        "availability_status": "available",
        "route_check_result": "acquisition_route_verified",
    },
    "stage_task2": {
        "access_friction": "self_service_clickthrough",
        "requires_registration": True,
        "requires_authentication": True,
        "requires_api_token": False,
        "requires_clickthrough": True,
        "requires_manual_approval": False,
        "requires_data_use_agreement": False,
        "requires_author_contact": False,
        "requires_payment": False,
        "geographic_or_institutional_restriction": "real_name_platform_verification_required",
        "availability_status": "available",
        "route_check_result": "acquisition_route_verified",
    },
    "stage_task3": {
        "access_friction": "self_service_clickthrough",
        "requires_registration": True,
        "requires_authentication": True,
        "requires_api_token": False,
        "requires_clickthrough": True,
        "requires_manual_approval": False,
        "requires_data_use_agreement": False,
        "requires_author_contact": False,
        "requires_payment": False,
        "geographic_or_institutional_restriction": "real_name_platform_verification_required",
        "availability_status": "available",
        "route_check_result": "acquisition_route_verified",
    },
}

_DOI_RE = re.compile(r"10\.\d{4,9}/[-._;()/:A-Z0-9]+", re.IGNORECASE)

# Explicit component modalities for resources containing more than one data
# type. ``primary_category`` remains a single navigation label, while
# ``modalities`` names every data type a user can retrieve from the resource.
COMPONENT_MODALITY_OVERRIDES: Dict[str, List[str]] = {
    "mmrdr": ["fundus", "oct", "uwf_fundus"],
    "grape": ["fundus", "oct", "visual_field", "tabular"],
    "gamma": ["fundus", "oct"],
    "harvard_fairvision": ["fundus", "oct"],
    "multieye": ["fundus", "oct"],
    "fovea": ["fundus", "surgical_video"],
    "slid": ["external_eye"],
    "eyecare_100k": [
        "fundus",
        "fundus_angiography",
        "fundus_autofluorescence",
        "oct",
        "ocular_ultrasound",
        "external_eye",
        "ct",
        "text",
    ],
    "erdes": ["ocular_ultrasound"],
    "mcoa": ["oct", "external_eye"],
    "tear_meniscus": ["external_eye", "infrared"],
    "tom500": ["orbital_mri", "tabular"],
    "mm_retinal_reason": [
        "fundus",
        "fundus_angiography",
        "oct",
        "text",
    ],
    "ocular_chat_vqa": ["text", "tabular"],
    "fairvlmed": ["fundus", "visual_field", "text", "tabular"],
    "oct_fundus_dme_dr_mexico": ["fundus", "oct"],
    "data_oct_fundus_glaucoma": ["fundus", "oct"],
    "hassan_composite_retina": ["fundus", "oct"],
    "uveitis_smote": ["external_eye", "tabular"],
    "jrc_multimodal_vessels": [
        "fundus",
        "fundus_angiography",
        "fundus_autofluorescence",
        "infrared",
    ],
    "dme_vqa": ["fundus", "text"],
    "dme_vqa_logical": ["fundus", "text"],
    "ut_fsocta": ["fundus", "octa"],
    "fprm_retina": [
        "fundus",
        "retinal_oximetry",
        "pupillometry",
        "tabular",
    ],
    "ophthalvqa": [
        "fundus",
        "fundus_angiography",
        "oct",
        "ocular_ultrasound",
        "external_eye",
        "text",
    ],
    "x_pcr": [
        "fundus",
        "fundus_angiography",
        "oct",
        "external_eye",
        "retcam",
        "text",
    ],
    "fundus_report_dataset": ["fundus", "uwf_fundus", "text"],
    "lmod_cataract_1k_cot": ["surgical_video", "text"],
    "ffa_ir": ["fundus", "fundus_angiography", "text"],
    "angioreport": ["fundus", "fundus_angiography", "text"],
    "lmod_plus": [
        "fundus",
        "oct",
        "external_eye",
        "surgical_video",
        "text",
        "tabular",
    ],
    "dryad_retinal_vein_cannulation": ["surgical_video", "oct"],
    "dryad_subretinal_robot": ["surgical_video", "oct", "tabular"],
    "dryad_cornea_oct_pentacam": ["oct", "corneal_topography"],
    "papila": ["fundus", "tabular"],
    "harvard_gdp": ["oct", "visual_field", "tabular"],
    "olives": ["oct", "fundus", "tabular"],
    "stage_task1": ["oct", "visual_field"],
    "stage_task2": ["oct", "visual_field"],
    "stage_task3": ["oct", "visual_field"],
    "oculoscope": ["uwf_fundus", "tabular"],
    "deepdrid": ["fundus", "uwf_fundus"],
    "ophora": ["surgical_video", "text"],
    "csdi": ["fundus", "text"],
    "deepeyenet": ["fundus", "text"],
    "eed_astig": ["external_eye", "tabular"],
    "leops_erg": ["electrophysiology", "tabular"],
    "perg_ioba": ["electrophysiology", "tabular"],
    "soul_octa": ["octa", "text", "tabular"],
    "dryad_glaucoma_rnfl_vf": ["tabular", "visual_field"],
    "dryad_namd_oct_quant": ["tabular", "oct"],
    "dryad_namd_visual_prediction": ["tabular", "oct"],
    "ophtho_readability": ["text", "tabular"],
}

_MODALITY_ALIASES = {
    "fundus": "fundus",
    "fundus photography": "fundus",
    "retinal photograph": "fundus",
    "retinal image": "fundus",
    "fundus angiography": "fundus_angiography",
    "fluorescein angiography": "fundus_angiography",
    "indocyanine green angiography": "fundus_angiography",
    "fundus autofluorescence": "fundus_autofluorescence",
    "oct": "oct",
    "optical coherence tomography": "oct",
    "octa": "octa",
    "optical coherence tomography angiography": "octa",
    "uwf": "uwf_fundus",
    "ultra-widefield": "uwf_fundus",
    "ultrawidefield": "uwf_fundus",
    "visual field": "visual_field",
    "perimetry": "visual_field",
    "external eye": "external_eye",
    "slit lamp": "external_eye",
    "ocular ultrasound": "ocular_ultrasound",
    "ultrasound biomicroscopy": "ocular_ultrasound",
    "orbital mri": "orbital_mri",
    "computed tomography": "ct",
    "infrared": "infrared",
    "retinal oximetry": "retinal_oximetry",
    "pupillary": "pupillometry",
    "retcam": "retcam",
    "retcam imaging": "retcam",
    "retinal imaging": "retinal_imaging",
    "ophthalmic imaging": "ophthalmic_imaging",
    "surgical video": "surgical_video",
    "video": "surgical_video",
    "confocal": "confocal",
    "ivcm": "confocal",
    "corneal topography": "corneal_topography",
    "adaptive optics": "adaptive_optics",
    "eye tracking": "eye_tracking",
    "gaze": "eye_tracking",
    "iris": "iris_biometrics",
    "electrophysiology": "electrophysiology",
    "omics": "omics",
    "text": "text",
    "tabular": "tabular",
    "cell microscopy": "cell_microscopy",
}


def normalize_modality_label(value: str) -> str:
    """Normalize a public modality label or alias to a catalog value."""
    cleaned = re.sub(r"[\s-]+", "_", (value or "").strip().lower())
    direct = {
        "optical_coherence_tomography": "oct",
        "fundus_photography": "fundus",
        "ultra_widefield": "uwf_fundus",
        "ultrawidefield": "uwf_fundus",
        "uwf": "uwf_fundus",
        "ivcm": "confocal",
        "slit_lamp": "external_eye",
        "ffa": "fundus_angiography",
        "icga": "fundus_angiography",
        "faf": "fundus_autofluorescence",
        "ubm": "ocular_ultrasound",
        "ocular_ultrasonography": "ocular_ultrasound",
        "mri": "orbital_mri",
        "pupil": "pupillometry",
        "surgical": "surgical_video",
        "gaze": "eye_tracking",
        "iris": "iris_biometrics",
        "genomics": "omics",
        "aoslo": "adaptive_optics",
    }
    return direct.get(cleaned, cleaned)


def _text(info: Any) -> str:
    values: Iterable[Any] = (
        getattr(info, "full_name", ""),
        getattr(info, "description", ""),
        getattr(info, "license", ""),
        getattr(info, "citation", ""),
        getattr(info, "notes", ""),
        " ".join(getattr(info, "tags", []) or []),
    )
    return " ".join(str(value) for value in values if value).lower()


def _contains(text: str, *patterns: str) -> bool:
    return any(pattern in text for pattern in patterns)


def _set_if_empty(info: Any, name: str, value: Any) -> None:
    current = getattr(info, name, None)
    if current is None or current == "" or current == []:
        setattr(info, name, value)


def _derive_modalities(info: Any, text: str) -> List[str]:
    primary = getattr(info, "primary_category", None) or info.modality
    found = {primary}
    if primary == "multimodal":
        for phrase, canonical in _MODALITY_ALIASES.items():
            pattern = r"(?<![a-z0-9])" + re.escape(phrase) + r"(?![a-z0-9])"
            if re.search(pattern, text) and canonical != "multimodal":
                found.add(canonical)
    return [primary] + sorted(found - {primary})


def _derive_item_unit(info: Any, text: str) -> str:
    description = (getattr(info, "description", "") or "").lower()
    patterns = (
        ("participants", ("participants", "patients", "subjects")),
        ("volumes", ("volumes", "3d volume", "oct volume")),
        ("videos", ("videos", "surgical cases", "procedures")),
        ("examinations", ("examinations", "exams", "visits")),
        ("signals", ("signals", "recordings", "traces")),
        ("records", ("records", "rows", "encounters")),
        ("text_items", ("reports", "questions", "answers", "documents", "abstracts")),
        ("images", ("images", "photographs", "frames", "scans", "b-scans")),
    )
    positions: List[tuple[int, str]] = []
    for unit, needles in patterns:
        for needle in needles:
            position = description.find(needle)
            if position >= 0:
                positions.append((position, unit))
    if positions:
        return min(positions)[1]
    return "unknown"


def _derive_route_type(backend: str, url: str) -> str:
    if backend in {"zenodo", "figshare", "mendeley", "dryad"}:
        return "official_repository"
    if backend in {"kaggle", "huggingface", "physionet"}:
        return "data_platform"
    if backend == "github":
        return "source_repository"
    if backend == "gdrive":
        return "cloud_file_share"
    host = urlparse(url).netloc.lower()
    if "grand-challenge" in host or "kaggle" in host:
        return "challenge_platform"
    if backend == "manual":
        return "documented_manual_route"
    return "official_direct"


def _derive_access(info: Any, text: str) -> Dict[str, Any]:
    backend = (getattr(info, "download_type", "") or "manual").lower()
    slug = getattr(info, "name", "")

    unavailable = _contains(
        text,
        "withdrawn",
        "no longer available",
        "no longer public",
        "route unavailable",
        "website unavailable",
        "link is dead",
    )
    author_contact = _contains(
        text,
        "contact author",
        "contact authors",
        "email request",
        "email the",
        "by email",
        "email from",
        "email access",
        "password by email",
        "author request",
        "available from the authors",
        "request the dataset by email",
    )
    dua = _contains(
        text,
        "data use agreement",
        "data-use agreement",
        "material transfer agreement",
    ) or bool(re.search(r"\bdua\b", text))
    approval = dua or _contains(
        text,
        "manual approval",
        "application required",
        "application-gated",
        "application form",
        "request form",
        "request access",
        "access request",
        "access by academic request",
        "requires approval",
        "approval-based",
        "institutional verification",
        "signed institutional",
        "committee review",
        "academic request",
        "form-gated",
        "restricted access",
        "files are restricted",
        "restricted zenodo",
        "synapse terms",
    )
    payment = True if _contains(text, "paid only", "purchase required", "access fee") else None
    if payment is None and _contains(
        text, "free registration", "free account", "no payment", "without charge"
    ):
        payment = False
    registration_marker = _contains(
        text,
        "requires registration",
        "registration required",
        "free registration",
        "account required",
        "login required",
        "requires an account",
        "requires account",
        "requires ieee dataport account",
        "account login",
    )
    clickthrough = _contains(
        text,
        "accept the",
        "agree to",
        "click-through",
        "clickthrough",
        "competition rules",
        "challenge terms",
        "challenge data-use",
        "kaggle competition",
    )
    secure = _contains(text, "model-to-data", "trusted research environment", "secure environment")

    if unavailable:
        friction = "unavailable"
    elif secure:
        friction = "model_to_data_or_secure_environment"
    elif author_contact:
        friction = "author_contact"
    elif approval:
        friction = "controlled_or_manual"
    elif clickthrough:
        friction = "self_service_clickthrough"
    elif registration_marker:
        friction = "self_service_authenticated"
    elif backend == "kaggle":
        friction = "self_service_authenticated"
    elif backend == "physionet" and _contains(text, "credentialed"):
        friction = "controlled_or_manual"
        approval = True
        dua = True
        clickthrough = True
    elif backend == "huggingface" and _contains(text, "gated", "token required"):
        friction = "self_service_authenticated"
    elif backend in STANDARD_PLATFORM_BACKENDS | DIRECT_BACKENDS:
        friction = "anonymous_direct"
    elif backend == "manual" and getattr(info, "download_url", None):
        # A manual loader does not necessarily mean controlled access.  Only
        # classify as anonymous when the source text explicitly describes a
        # public/direct route; otherwise preserve uncertainty.
        if _contains(
            text,
            "public ftp",
            "direct download",
            "public release",
            "public github release",
            "freely available",
            "no account required",
            "open-access project",
        ):
            friction = "anonymous_direct"
        else:
            friction = "unverified"
    else:
        friction = "unverified"

    if friction in {"anonymous_direct", "self_service_authenticated", "self_service_clickthrough"}:
        known_no_manual = True
        known_no_author = True
        known_no_payment = False if payment is True else True
    elif friction == "author_contact":
        known_no_manual = None
        known_no_author = False
        known_no_payment = None if payment is None else not payment
    elif friction == "controlled_or_manual":
        known_no_manual = False
        known_no_author = None if not author_contact else False
        known_no_payment = None if payment is None else not payment
    else:
        known_no_manual = None
        known_no_author = None
        known_no_payment = None if payment is None else not payment

    registration = registration_marker or friction in {
        "self_service_authenticated",
        "self_service_clickthrough",
    }
    authentication = registration
    api_token: Optional[bool]
    if backend in {"kaggle"}:
        api_token = True
    elif backend == "huggingface" and friction == "self_service_authenticated":
        api_token = True
    elif friction in {"anonymous_direct", "unavailable"}:
        api_token = False
    else:
        api_token = None

    if friction == "anonymous_direct":
        registration = False
        authentication = False
        clickthrough = False
        approval = False
        dua = False
        author_contact = False
        payment = False

    availability = "unavailable" if friction == "unavailable" else (
        "unverified" if friction == "unverified" else "available"
    )

    if friction == "unavailable":
        acquisition = "unavailable"
    elif friction in {
        "controlled_or_manual",
        "author_contact",
        "model_to_data_or_secure_environment",
    }:
        acquisition = "manual_access_blocked"
    elif slug in GUIDED_ONLY_SLUGS or backend == "manual":
        acquisition = "guided_instructions_only"
    elif backend in STANDARD_PLATFORM_BACKENDS:
        acquisition = "standard_platform_supported"
    elif backend in DIRECT_BACKENDS:
        acquisition = "loader_implemented_not_live_tested"
    else:
        acquisition = "unsupported"

    return {
        "access_friction": friction,
        "requires_registration": registration if friction != "unverified" else None,
        "requires_authentication": authentication if friction != "unverified" else None,
        "requires_api_token": api_token,
        "requires_clickthrough": clickthrough if friction != "unverified" else None,
        "requires_manual_approval": (not known_no_manual) if known_no_manual is not None else None,
        "requires_data_use_agreement": dua if friction != "unverified" else None,
        "requires_author_contact": (not known_no_author) if known_no_author is not None else None,
        "requires_payment": (not known_no_payment) if known_no_payment is not None else None,
        "geographic_or_institutional_restriction": "unknown",
        "availability_status": availability,
        "acquisition_support": acquisition,
    }


def _derive_terms_scope(info: Any, text: str) -> str:
    raw = (getattr(info, "license", "") or "").lower()
    if _contains(raw, "article", "publication") and _contains(raw, "unknown", "needs check"):
        return "publication_only"
    if _contains(raw, "deposited", "figshare files", "index files"):
        return "mixed_components"
    if _contains(raw, "mixed", "inherits", "component"):
        return "mixed_components"
    if _contains(raw, "challenge", "competition rules"):
        return "challenge_participation"
    if _contains(raw, "mit", "apache", "gpl", "lgpl"):
        # Software licences are not silently inherited by data files.
        return "unknown"
    if _contains(raw, "cc0", "cc by", "odc-by", "open data commons", "research only", "research use"):
        return "dataset_files"
    return "unknown"


def _clean_doi(value: str) -> str:
    return value.rstrip(".,;:)]}")


def extract_dois(value: str) -> List[str]:
    """Return deterministic, de-duplicated DOI strings from text."""
    found: List[str] = []
    for match in _DOI_RE.findall(value or ""):
        doi = _clean_doi(match).lower()
        if doi not in found:
            found.append(doi)
    return found


def _derive_identifiers(info: Any) -> Dict[str, Optional[str]]:
    url = getattr(info, "download_url", "") or ""
    citation = getattr(info, "citation", "") or ""
    backend = (getattr(info, "download_type", "") or "").lower()
    url_dois = extract_dois(url)
    citation_dois = extract_dois(citation)

    dataset_doi = getattr(info, "dataset_doi", None)
    publication_doi = getattr(info, "associated_publication_doi", None)
    if dataset_doi:
        dataset_doi = _clean_doi(str(dataset_doi)).lower()
    if publication_doi:
        publication_doi = _clean_doi(str(publication_doi)).lower()
    dataset_doi_prefixes = (
        "10.17632/",  # Mendeley Data
        "10.6084/",   # Figshare
        "10.5281/",   # Zenodo
        "10.5061/",   # Dryad
        "10.13026/",  # PhysioNet
    )
    repository_backends = {"zenodo", "figshare", "mendeley", "dryad", "physionet"}
    # A DOI in an official repository acquisition URL identifies the repository
    # object only when it is unambiguous.  Citation order is never used to guess
    # which of several DOI strings identifies the dataset.
    if dataset_doi:
        pass
    elif backend in repository_backends and len(url_dois) == 1:
        dataset_doi = url_dois[0]
    elif backend in repository_backends:
        repository_dois = [
            doi for doi in citation_dois if doi.startswith(dataset_doi_prefixes)
        ]
        if len(repository_dois) == 1:
            dataset_doi = repository_dois[0]
    elif (
        "doi.org" in url.lower()
        and backend not in {"manual", "direct"}
        and len(url_dois) == 1
    ):
        dataset_doi = url_dois[0]

    publication_candidates = [doi for doi in citation_dois if doi != dataset_doi]
    if publication_doi is None and len(publication_candidates) == 1:
        publication_doi = publication_candidates[0]

    path_parts = [part for part in urlparse(url).path.split("/") if part]
    repository_id: Optional[str] = None
    if path_parts:
        if backend in {"zenodo", "figshare", "mendeley", "dryad", "physionet", "huggingface", "kaggle"}:
            repository_id = "/".join(path_parts[-2:]) if len(path_parts) >= 2 else path_parts[-1]

    challenge_id: Optional[str] = None
    if _contains(url.lower(), "grand-challenge", "kaggle.com/competitions"):
        challenge_id = path_parts[-1] if path_parts else None

    canonical = f"https://doi.org/{dataset_doi}" if dataset_doi else (url or None)
    return {
        "dataset_doi": dataset_doi,
        "dataset_accession": None,
        "repository_record_id": repository_id,
        "associated_publication_doi": publication_doi,
        "software_doi": None,
        "challenge_identifier": challenge_id,
        "canonical_resolver_url": canonical,
    }


def _derive_relationships(info: Any) -> List[Dict[str, str]]:
    """Recover only explicit, high-confidence relationships from legacy tags."""
    relationships: List[Dict[str, str]] = []
    for tag in getattr(info, "tags", []) or []:
        if tag.startswith("derivative_of_"):
            relationships.append(
                {"type": "derived_from", "target": tag.removeprefix("derivative_of_")}
            )
        elif tag.startswith("duplicate_of_"):
            relationships.append(
                {"type": "mirror_of", "target": tag.removeprefix("duplicate_of_")}
            )
    return relationships


def enrich_dataset_info(info: Any) -> None:
    """Populate unset rich metadata fields on a ``DatasetInfo`` instance."""
    text = _text(info)
    backend = (getattr(info, "download_type", "") or "manual").lower()
    url = getattr(info, "download_url", None) or ""

    _set_if_empty(info, "primary_category", info.modality)
    _set_if_empty(info, "modalities", _derive_modalities(info, text))
    if info.name in COMPONENT_MODALITY_OVERRIDES:
        info.modalities = list(COMPONENT_MODALITY_OVERRIDES[info.name])
    _set_if_empty(info, "source_landing_page_url", url or None)
    _set_if_empty(info, "preferred_route_url", url or None)
    _set_if_empty(info, "preferred_route_type", _derive_route_type(backend, url))
    _set_if_empty(info, "source_terms", info.license)
    _set_if_empty(info, "terms_evidence_url", url or None)
    _set_if_empty(info, "terms_scope", _derive_terms_scope(info, text))
    _set_if_empty(info, "terms_component_notes", "Review the cited source for component-specific terms.")
    _set_if_empty(info, "item_count_unit", _derive_item_unit(info, text))
    _set_if_empty(info, "item_count_evidence_url", url or None)
    _set_if_empty(info, "modality_evidence_url", url or None)
    _set_if_empty(info, "task_evidence_url", url or None)
    _set_if_empty(info, "citation_evidence_url", url or None)

    for key, value in _derive_access(info, text).items():
        _set_if_empty(info, key, value)

    for key, value in ACCESS_OVERRIDES.get(info.name, {}).items():
        setattr(info, key, value)

    # Access restrictions take precedence over implementation metadata.  A
    # legacy loader label must never make a controlled or author-contact route
    # appear automatable.
    if info.availability_status == "unavailable":
        info.acquisition_support = "unavailable"
    elif info.access_friction in {
        "controlled_or_manual",
        "author_contact",
        "model_to_data_or_secure_environment",
    }:
        info.acquisition_support = "manual_access_blocked"
    elif info.name in PARTIAL_TRANSFER_TESTED_SLUGS:
        info.acquisition_support = "transfer_tested_partial"
    elif info.name in END_TO_END_TESTED_SLUGS:
        info.acquisition_support = "end_to_end_tested"

    _set_if_empty(info, "route_last_checked", "2026-07-21")
    if info.availability_status == "available":
        _set_if_empty(info, "route_check_result", "author_source_checked")
    elif info.availability_status == "unavailable":
        _set_if_empty(info, "route_check_result", "official_route_unavailable")
    else:
        _set_if_empty(info, "route_check_result", "insufficient_evidence")
    _set_if_empty(
        info,
        "route_check_notes",
        "Author-conducted source check; transfer completeness was evaluated separately.",
    )

    _set_if_empty(info, "loader_backend", backend)
    _set_if_empty(info, "loader_name", f"{backend}_loader")
    _set_if_empty(info, "loader_version", "0.2.2")
    _set_if_empty(info, "loader_live_tested", False)
    _set_if_empty(info, "loader_test_scope", "unit_or_mocked_only")
    _set_if_empty(info, "loader_test_result", "not_live_tested")
    _set_if_empty(info, "failure_reason", None)

    if info.name in PARTIAL_TRANSFER_TESTED_SLUGS:
        info.loader_live_tested = False
        info.loader_test_date = (
            "2026-07-25" if info.name == "migs_video" else "2026-07-21"
        )
        info.loader_test_scope = "official_metadata_or_file_listing"
        info.loader_test_result = "partial_route_test_passed"
        info.tested_command = "python hub/audit/validate_acquisition.py"
    elif info.name in END_TO_END_TESTED_SLUGS:
        info.loader_live_tested = True
        info.loader_test_date = "2026-07-21"
        info.loader_test_scope = "complete_official_deposit_transfer"
        info.loader_test_result = "complete_download_passed"
        info.tested_command = (
            "eyehub download ophthalwechat --data-dir <directory> --json"
        )

    for key, value in _derive_identifiers(info).items():
        _set_if_empty(info, key, value)

    _set_if_empty(info, "resource_version", None)
    _set_if_empty(info, "relationships", _derive_relationships(info))
    _set_if_empty(info, "author_source_checked", True)
    _set_if_empty(info, "source_check_date", "2026-07-21")
    _set_if_empty(info, "source_check_status", "checked_against_cited_source")
    _set_if_empty(info, "independent_audit_status", "not_independently_audited")
    _set_if_empty(info, "access_check_status", info.route_check_result)
    _set_if_empty(info, "transfer_check_status", info.loader_test_result)


def bool_or_unknown(value: Optional[bool]) -> str:
    """Serialize tri-state Boolean values for CSV output."""
    if value is True:
        return "true"
    if value is False:
        return "false"
    return "unknown"


def normalize_unknown(value: Any) -> Any:
    """Return a stable JSON-friendly representation without inventing values."""
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, tuple):
        return list(value)
    if isinstance(value, list):
        return [normalize_unknown(item) for item in value]
    if isinstance(value, dict):
        return {key: normalize_unknown(item) for key, item in value.items()}
    return value
