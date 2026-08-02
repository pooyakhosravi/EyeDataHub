"""Curated, source-supported relationships between catalog records.

The catalog contains resources rather than necessarily independent cohorts.
This module keeps record relationships in one reviewed location so the runtime
catalog, audit tables, and manuscript analyses use the same edges.  The public
``DatasetInfo.relationships`` field remains intentionally compact (type and
target); evidence and review notes are exposed by the audit exports.

Only relationships to another EyeDataHub record are encoded here.  Upstream
resources that are not cataloged, and plausible links that could not be
confirmed, are retained separately in ``hub/audit/generate_relationship_review.py``.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


RELATIONSHIP_TYPES = frozenset(
    {
        "derived_from",
        "subset_of",
        "version_of",
        "mirror_of",
        "component_of",
        "has_component",
        "replaces",
        "extension_of",
        "same_or_overlapping_cohort_as",
    }
)


RELATIONSHIP_DEFINITIONS = {
    "derived_from": (
        "The source record reuses data from the target and adds processing, "
        "annotations, labels, questions, representations, or benchmark structure."
    ),
    "subset_of": "The source record contains a documented proper subset of the target.",
    "version_of": (
        "The source record is a later named release that retains all or part of "
        "the earlier target release."
    ),
    "mirror_of": (
        "The source record republishes the same data payload or documented split "
        "as the target record."
    ),
    "component_of": "The source record is a named component of the target collection.",
    "has_component": "The source collection includes the named target record.",
    "replaces": "The source record explicitly supersedes the target record.",
    "extension_of": (
        "The source record extends the target project with additional data but is "
        "not documented as the same cohort or a complete replacement."
    ),
    "same_or_overlapping_cohort_as": (
        "The records are documented to share a cohort or source images, but exact "
        "containment cannot be established from public evidence."
    ),
}


@dataclass(frozen=True)
class RelationshipEvidence:
    """One reviewed directed relationship edge and its public evidence."""

    source_record_id: str
    relationship_type: str
    target_record_id: str
    evidence_url: str
    evidence_source_type: str
    evidence_summary: str
    confidence: str = "confirmed"
    review_date: str = "2026-08-01"
    notes: str = ""


def _edge(
    source: str,
    relationship_type: str,
    target: str,
    url: str,
    summary: str,
    *,
    evidence_source_type: str = "official_dataset_description",
    notes: str = "",
) -> RelationshipEvidence:
    return RelationshipEvidence(
        source_record_id=source,
        relationship_type=relationship_type,
        target_record_id=target,
        evidence_url=url,
        evidence_source_type=evidence_source_type,
        evidence_summary=summary,
        notes=notes,
    )


def _derived_many(
    source: str,
    targets: tuple[str, ...],
    url: str,
    summary: str,
    *,
    evidence_source_type: str = "official_dataset_description",
    notes: str = "",
) -> tuple[RelationshipEvidence, ...]:
    return tuple(
        _edge(
            source,
            "derived_from",
            target,
            url,
            summary,
            evidence_source_type=evidence_source_type,
            notes=notes,
        )
        for target in targets
    )


_MM_RETINAL_REASON_URL = (
    "https://huggingface.co/datasets/lxirich/MM-Retinal-Reason/"
    "tree/d6243baa82c0914dba3c6f43ca79fdbf856982ef"
)
_MULTIEYE_URL = "https://arxiv.org/abs/2412.09402"
_SMDG_URL = (
    "https://www.kaggle.com/datasets/deathtrooper/"
    "multichannel-glaucoma-benchmark-dataset"
)
_XPCR_URL = (
    "https://huggingface.co/datasets/Fantasy666/X-PCR/"
    "tree/06a318fd852230326386e3c6514d8a11b7a6b4af"
)


RELATIONSHIP_EVIDENCE: tuple[RelationshipEvidence, ...] = (
    # Direct mirrors, subsets, and annotation layers.
    _edge(
        "aod",
        "derived_from",
        "odir2019",
        "https://doi.org/10.17632/d73g6m8d5m.1",
        "The AOD deposit describes an augmented and preprocessed ODIR-5K resource.",
        evidence_source_type="official_repository_metadata",
    ),
    _edge(
        "aptos_arcade_onh_masks",
        "derived_from",
        "aptos2019",
        "https://zenodo.org/records/20711325",
        "The deposit supplies vascular-arcade and optic-nerve-head masks for APTOS 2019 images.",
        evidence_source_type="official_repository_metadata",
    ),
    _edge(
        "brset_mbrset_embeddings",
        "derived_from",
        "brset",
        "https://physionet.org/content/embedding-brset-mbrset/1.0.0/",
        "The PhysioNet record supplies precomputed representations for BRSET images.",
        evidence_source_type="official_repository_page",
    ),
    _edge(
        "brset_mbrset_embeddings",
        "derived_from",
        "mbrset",
        "https://physionet.org/content/embedding-brset-mbrset/1.0.0/",
        "The PhysioNet record supplies precomputed representations for mBRSET images.",
        evidence_source_type="official_repository_page",
    ),
    _edge(
        "cataract101_extended_labels",
        "derived_from",
        "cataract_101",
        "https://zenodo.org/records/4984167",
        "The deposit provides extended labels for the Cataract-101 videos.",
        evidence_source_type="official_repository_metadata",
    ),
    _edge(
        "cadis",
        "derived_from",
        "cataracts2017",
        "https://cataracts-semantic-segmentation2020.grand-challenge.org/",
        "CaDIS adds semantic segmentation labels to frames selected from CATARACTS videos.",
        evidence_source_type="official_challenge_page",
    ),
    _edge(
        "insegcat",
        "derived_from",
        "cataract_101",
        "https://ftp.itec.aau.at/datasets/ovid/InSegCat/",
        "InSegCat Dataset 1 selects and annotates frames from Cataract-101 videos.",
        evidence_source_type="official_project_page",
    ),
    _edge(
        "insegcat",
        "derived_from",
        "cadis",
        "https://ftp.itec.aau.at/datasets/ovid/InSegCat/",
        "InSegCat Dataset 2 converts CaDIS semantic masks to instance masks and boxes.",
        evidence_source_type="official_project_page",
    ),
    _edge(
        "lmod_cataract_1k",
        "derived_from",
        "cataract1k",
        "https://huggingface.co/datasets/mehti/LMOD-Cataract-1K",
        "The dataset card identifies Cataract-1K as the source of the processed surgical frames.",
        evidence_source_type="official_dataset_card",
    ),
    _edge(
        "lmod_cataract_1k_cot",
        "derived_from",
        "lmod_cataract_1k",
        "https://huggingface.co/datasets/mehti/LMOD-Cataract-1K-surgical-analysis-cot",
        "The dataset card identifies LMOD-Cataract-1K as its image source.",
        evidence_source_type="official_dataset_card",
    ),
    _edge(
        "dme_vqa",
        "derived_from",
        "idrid",
        "https://zenodo.org/records/6784358",
        "The DME VQA deposit identifies IDRiD images as source material.",
        evidence_source_type="official_repository_metadata",
    ),
    _edge(
        "dme_vqa",
        "derived_from",
        "e_ophtha",
        "https://zenodo.org/records/6784358",
        "The DME VQA deposit identifies e-ophtha images as source material.",
        evidence_source_type="official_repository_metadata",
    ),
    _edge(
        "dme_vqa_logical",
        "extension_of",
        "dme_vqa",
        "https://zenodo.org/records/7777849",
        "This release adds logical-relation annotations to the earlier DME VQA resource.",
        evidence_source_type="official_repository_metadata",
    ),
    _edge(
        "eyeq",
        "derived_from",
        "eyepacs",
        "https://github.com/HzFu/EyeQ",
        "EyeQ provides quality labels for 28,792 images from the EyePACS train and test partitions.",
        evidence_source_type="official_repository_readme",
    ),
    *_derived_many(
        "fundus_domain_generalization",
        ("refuge2", "drishti_gs", "riga"),
        "https://zenodo.org/records/8009107",
        "The official description states that the benchmark is based on the original REFUGE images, now represented by the current REFUGE2 record, plus Drishti-GS, ORIGA, and RIGA.",
        evidence_source_type="official_repository_metadata",
        notes="ORIGA is not a separate EyeDataHub record.",
    ),
    _edge(
        "fundus_report_dataset",
        "derived_from",
        "deepdrid",
        "https://huggingface.co/datasets/zzzzineun/fundus-report-dataset",
        "The dataset card reports 203 source images from DeepDRiD and 219 from OUWFD.",
        evidence_source_type="official_dataset_card",
        notes="OUWFD is not a separate EyeDataHub record.",
    ),
    _edge(
        "hrf_seg_plus",
        "derived_from",
        "hrf",
        "https://zenodo.org/records/16744782",
        "HRF-Seg+ adds multi-structure annotations to the 45 HRF images.",
        evidence_source_type="official_repository_metadata",
    ),
    _edge(
        "intraretinal_cystoid_fluid",
        "derived_from",
        "kermany_oct",
        "https://www.kaggle.com/datasets/zeeshanahmed13/intraretinal-cystoid-fluid",
        "The source states that 1,000 training images were selected from the Kermany Retinal OCT Images DME class; 200 test images were collected separately.",
        evidence_source_type="official_platform_metadata",
    ),
    _edge(
        "reta_benchmark",
        "derived_from",
        "idrid",
        "https://doi.org/10.6084/m9.figshare.16960855",
        "RETA reuses 81 images from the first IDRiD subset and adds vascular-tree annotations.",
        evidence_source_type="official_repository_metadata",
    ),
    *_derived_many(
        "retinal_vessel_robustness",
        ("drive", "stare", "chase_db1"),
        "https://zenodo.org/records/12659652",
        "The robustness benchmark contains augmented versions of DRIVE, STARE, and CHASE_DB1 images.",
        evidence_source_type="official_repository_metadata",
    ),
    _edge(
        "riga_plus",
        "derived_from",
        "riga",
        "https://zenodo.org/records/6325549",
        "RIGA+ is built from RIGA components plus the original MESSIDOR resource after duplicate removal.",
        evidence_source_type="official_repository_metadata",
        notes="The source says MESSIDOR, not MESSIDOR-2; no edge to messidor2 is encoded.",
    ),
    _edge(
        "rite",
        "derived_from",
        "drive",
        "https://medicine.uiowa.edu/eye/rite-dataset",
        "RITE adds artery, vein, and vessel-tree labels to the same 40 DRIVE images.",
        evidence_source_type="official_project_page",
    ),
    *_derived_many(
        "mured",
        ("stare", "rfmid"),
        "https://doi.org/10.17632/pc4mb3h8hz.1",
        "The MuReD description identifies STARE, RFMiD, and ARIA as image sources and applies post-processing.",
        evidence_source_type="official_repository_metadata",
        notes="ARIA is not a separate EyeDataHub record.",
    ),
    *_derived_many(
        "rao_fundus",
        ("rfmid", "jsiec"),
        "https://doi.org/10.17632/5428684j44.2",
        "The RAO source reports use of public web images plus RFMiD and JSIEC images.",
        evidence_source_type="official_repository_metadata",
    ),
    *_derived_many(
        "amdnet23",
        ("odir2019", "rfmid", "hrf"),
        "https://doi.org/10.17632/yj35kjgrv3.1",
        "AMDNet23 compiles preprocessed images from ODIR, RFMiD, HRF, ARIA, DR_200, and Fundus Dataset.",
        evidence_source_type="official_repository_metadata",
        notes="ARIA, DR_200, and Fundus Dataset are not separate EyeDataHub records.",
    ),
    _edge(
        "refuge1_multirater",
        "derived_from",
        "refuge2",
        "https://huggingface.co/datasets/realslimman/REFUGE-MultiRater",
        "The source provides seven-rater annotations for the 1,200 original REFUGE images incorporated into the current REFUGE2 release.",
        evidence_source_type="official_dataset_card",
    ),
    _edge(
        "rfmid2",
        "extension_of",
        "rfmid",
        "https://zenodo.org/records/7505822",
        "RFMiD 2.0 is described as an auxiliary dataset to the earlier RFMiD release, not as the same image cohort.",
        evidence_source_type="official_repository_metadata",
    ),
    _edge(
        "trend2_fundus",
        "extension_of",
        "trend_fundus",
        "https://zenodo.org/records/7678656",
        "TREND2 is described as an addition to the TREND portable-fundus resource.",
        evidence_source_type="official_repository_metadata",
    ),

    # Collection/component and documented overlap relationships.
    _edge(
        "corn_collection",
        "has_component",
        "corn1500",
        "https://zenodo.org/records/19689814",
        "The CORN collection lists CORN-1500 as one of its six component deposits.",
        evidence_source_type="official_repository_metadata",
    ),
    _edge(
        "corn1500",
        "component_of",
        "corn_collection",
        "https://zenodo.org/records/19689814",
        "CORN-1500 is a named component of the combined CORN collection.",
        evidence_source_type="official_repository_metadata",
    ),
    _edge(
        "corn_collection",
        "has_component",
        "corn_pro",
        "https://zenodo.org/records/19689814",
        "The CORN collection lists CORN-Pro as one of its six component deposits.",
        evidence_source_type="official_repository_metadata",
    ),
    _edge(
        "corn_pro",
        "component_of",
        "corn_collection",
        "https://zenodo.org/records/19689814",
        "CORN-Pro is a named component of the combined CORN collection.",
        evidence_source_type="official_repository_metadata",
    ),
    _edge(
        "ichallenge_oct",
        "has_component",
        "gamma",
        "http://hdmilab.cn/ichallenge",
        "The cataloged iChallenge OCT portal record explicitly includes the GAMMA multimodal challenge resource.",
        evidence_source_type="official_project_page",
    ),
    _edge(
        "gamma",
        "component_of",
        "ichallenge_oct",
        "http://hdmilab.cn/ichallenge",
        "GAMMA is one of the named resources exposed through the cataloged iChallenge OCT portal record.",
        evidence_source_type="official_project_page",
    ),
    _edge(
        "stage_task1",
        "same_or_overlapping_cohort_as",
        "stage_task2",
        "https://aistudio.baidu.com/aistudio/competition/detail/968/0/datasets",
        "STAGE Tasks 1 and 2 use the same 400 OCT volumes and expose different labels.",
        evidence_source_type="official_challenge_page",
    ),
    _edge(
        "stage_task2",
        "same_or_overlapping_cohort_as",
        "stage_task1",
        "https://aistudio.baidu.com/aistudio/competition/detail/968/0/datasets",
        "STAGE Tasks 1 and 2 use the same 400 OCT volumes and expose different labels.",
        evidence_source_type="official_challenge_page",
    ),
    _edge(
        "stage_task1",
        "same_or_overlapping_cohort_as",
        "stage_task3",
        "https://aistudio.baidu.com/aistudio/competition/detail/968/0/datasets",
        "STAGE Tasks 1 and 3 use the same 400 OCT volumes and expose different labels.",
        evidence_source_type="official_challenge_page",
    ),
    _edge(
        "stage_task3",
        "same_or_overlapping_cohort_as",
        "stage_task1",
        "https://aistudio.baidu.com/aistudio/competition/detail/968/0/datasets",
        "STAGE Tasks 1 and 3 use the same 400 OCT volumes and expose different labels.",
        evidence_source_type="official_challenge_page",
    ),
    _edge(
        "stage_task2",
        "same_or_overlapping_cohort_as",
        "stage_task3",
        "https://aistudio.baidu.com/aistudio/competition/detail/968/0/datasets",
        "STAGE Tasks 2 and 3 use the same 400 OCT volumes and expose different labels.",
        evidence_source_type="official_challenge_page",
    ),
    _edge(
        "stage_task3",
        "same_or_overlapping_cohort_as",
        "stage_task2",
        "https://aistudio.baidu.com/aistudio/competition/detail/968/0/datasets",
        "STAGE Tasks 2 and 3 use the same 400 OCT volumes and expose different labels.",
        evidence_source_type="official_challenge_page",
    ),
    _edge(
        "dryad_namd_oct_quant",
        "same_or_overlapping_cohort_as",
        "dryad_namd_visual_prediction",
        "https://doi.org/10.5061/dryad.2rbnzs7m4",
        "Both records draw from the Moorfields AMD database; public descriptions do not establish exact containment.",
        evidence_source_type="official_repository_metadata",
    ),
    _edge(
        "dryad_namd_visual_prediction",
        "same_or_overlapping_cohort_as",
        "dryad_namd_oct_quant",
        "https://doi.org/10.5061/dryad.573n5tb5d",
        "Both records draw from the Moorfields AMD database; public descriptions do not establish exact containment.",
        evidence_source_type="official_repository_metadata",
    ),
    _edge(
        "dryad_namd_oct_quant",
        "same_or_overlapping_cohort_as",
        "dryad_moorfields_namd_fellow_eye",
        "https://doi.org/10.5061/dryad.2rbnzs7m4",
        "The official records identify the Moorfields AMD database and overlapping treatment or extraction periods.",
        evidence_source_type="official_repository_metadata",
    ),
    _edge(
        "dryad_moorfields_namd_fellow_eye",
        "same_or_overlapping_cohort_as",
        "dryad_namd_oct_quant",
        "https://doi.org/10.5061/dryad.4mw6m906b",
        "The official records identify the Moorfields AMD database and overlapping treatment or extraction periods.",
        evidence_source_type="official_repository_metadata",
    ),
    _edge(
        "dryad_namd_visual_prediction",
        "same_or_overlapping_cohort_as",
        "dryad_moorfields_namd_fellow_eye",
        "https://doi.org/10.5061/dryad.573n5tb5d",
        "The official records identify the Moorfields AMD database and overlapping treatment or extraction periods.",
        evidence_source_type="official_repository_metadata",
    ),
    _edge(
        "dryad_moorfields_namd_fellow_eye",
        "same_or_overlapping_cohort_as",
        "dryad_namd_visual_prediction",
        "https://doi.org/10.5061/dryad.4mw6m906b",
        "The official records identify the Moorfields AMD database and overlapping treatment or extraction periods.",
        evidence_source_type="official_repository_metadata",
    ),
    _edge(
        "dryad_namd_oct_quant",
        "same_or_overlapping_cohort_as",
        "dryad_moorfields_amd_1_2_year",
        "https://doi.org/10.5061/dryad.2rbnzs7m4",
        "The official records identify the Moorfields AMD database and overlapping treatment or extraction periods.",
        evidence_source_type="official_repository_metadata",
    ),
    _edge(
        "dryad_moorfields_amd_1_2_year",
        "same_or_overlapping_cohort_as",
        "dryad_namd_oct_quant",
        "https://doi.org/10.5061/dryad.97r9289",
        "The official records identify the Moorfields AMD database and overlapping treatment or extraction periods.",
        evidence_source_type="official_repository_metadata",
    ),
    _edge(
        "dryad_namd_visual_prediction",
        "same_or_overlapping_cohort_as",
        "dryad_moorfields_amd_1_2_year",
        "https://doi.org/10.5061/dryad.573n5tb5d",
        "The official records identify the Moorfields AMD database and overlapping treatment or extraction periods.",
        evidence_source_type="official_repository_metadata",
    ),
    _edge(
        "dryad_moorfields_amd_1_2_year",
        "same_or_overlapping_cohort_as",
        "dryad_namd_visual_prediction",
        "https://doi.org/10.5061/dryad.97r9289",
        "The official records identify the Moorfields AMD database and overlapping treatment or extraction periods.",
        evidence_source_type="official_repository_metadata",
    ),
    _edge(
        "dryad_moorfields_namd_fellow_eye",
        "same_or_overlapping_cohort_as",
        "dryad_moorfields_amd_1_2_year",
        "https://doi.org/10.5061/dryad.4mw6m906b",
        "Both official deposits name the Moorfields AMD database and report overlapping 2008-2018 extraction windows.",
        evidence_source_type="official_repository_metadata",
    ),
    _edge(
        "dryad_moorfields_amd_1_2_year",
        "same_or_overlapping_cohort_as",
        "dryad_moorfields_namd_fellow_eye",
        "https://doi.org/10.5061/dryad.97r9289",
        "Both official deposits name the Moorfields AMD database and report overlapping 2008-2018 extraction windows.",
        evidence_source_type="official_repository_metadata",
    ),

    # Confirmed reused component in a multimodal release.
    _edge(
        "mmrdr",
        "derived_from",
        "ddr",
        "https://doi.org/10.1038/s41597-026-07005-9",
        "The MMRDR Data Descriptor identifies OIA-DDR as the source of its CFP images; MMRDR also adds independently collected OCT and UWF cohorts and new annotations.",
        evidence_source_type="associated_publication",
    ),

    # Large composite and repackaged resources.
    *_derived_many(
        "lmod_plus",
        ("cataract1k", "oimhs", "refuge2", "idrid", "g1020"),
        "https://kfzyqin.github.io/lmod_plus/",
        "The LMOD+ project page lists nine component datasets, including the five cataloged targets represented by these edges.",
        evidence_source_type="official_project_page",
        notes="Harvard FairSeg, CAU001, CatDet2, and ORIGA are not separate EyeDataHub records.",
    ),
    *_derived_many(
        "mm_retinal_reason",
        (
            "papila",
            "paraguay_dr",
            "aptos2019",
            "hrf",
            "deepdrid",
            "g1020",
            "palm",
            "drishti_gs",
            "chaksu",
            "hassan_composite_retina",
            "idrid",
            "rfmid",
            "stare",
            "roc",
            "sustech_sysu",
            "jichi",
            "eyepacs",
            "lag",
            "fives",
            "e_ophtha",
            "refuge2",
            "acrima",
            "ddr",
            "goals",
            "gamma",
            "stage_task1",
            "stage_task2",
            "oimhs",
            "octa_500",
            "kermany_oct",
            "duke_chiu_boe",
            "oct_c8",
            "octdl",
            "octid",
        ),
        _MM_RETINAL_REASON_URL,
        "The version-pinned official dataset card lists this record among the CFP or OCT sources used to construct MM-Retinal-Reason.",
        evidence_source_type="versioned_official_dataset_card",
        notes="Generic or non-cataloged names in the card were not forced to catalog targets.",
    ),
    *_derived_many(
        "multieye",
        (
            "rfmid",
            "rfmid2",
            "messidor2",
            "odir2019",
            "stare",
            "vietai_retinal_disease",
            "fives",
            "hassan_composite_retina",
            "ddr",
            "eyepacs",
            "kermany_oct",
            "octid",
            "goals",
        ),
        _MULTIEYE_URL,
        "The MultiEYE paper names this record as one of the public fundus or OCT sources assembled for the benchmark.",
        evidence_source_type="associated_publication",
        notes="MMC-AMD, 1000Fundus39Cat, and ARIA are not separate EyeDataHub records.",
    ),
    *_derived_many(
        "smdg",
        (
            "beh",
            "drishti_gs",
            "airogs",
            "fives",
            "g1020",
            "hrf",
            "jsiec",
            "odir2019",
            "papila",
            "refuge2",
        ),
        _SMDG_URL,
        "The official SMDG source table lists this catalog record among the 19 standardized source domains.",
        evidence_source_type="official_platform_metadata",
        notes="EyePACS-AIROGS is mapped to airogs, not the diabetic-retinopathy eyepacs record.",
    ),
    *_derived_many(
        "x_pcr",
        (
            "kermany_oct",
            "eyepacs",
            "oct_c8",
            "eye_disease_image_mendeley",
            "odir2019",
            "oimhs",
            "aptos2019",
            "harvard_gdp",
            "mured",
            "deepdrid",
            "jsiec",
            "rfmid2",
            "beh",
            "octid",
        ),
        _XPCR_URL,
        "Source labels in the version-pinned public X-PCR deposit identify this catalog record as upstream material.",
        evidence_source_type="versioned_official_deposit_metadata",
        notes="The 2023 APTOS angiography source is distinct from APTOS2019 and was not mapped to it.",
    ),
    *_derived_many(
        "glaucoma_expert_cot_refined",
        ("lag", "papila"),
        "https://huggingface.co/datasets/yuzhench/glaucoma-expert-cot-refined-1077",
        "The official dataset card identifies LAG and PAPILA as the source fundus resources paired with the refined glaucoma reasoning records.",
        evidence_source_type="official_dataset_card",
    ),
    *_derived_many(
        "higancnn_generated_glaucoma",
        ("acrima", "drishti_gs", "hrf"),
        "https://www.kaggle.com/datasets/hindsaud/datasets-higancnn-glaucoma-detection",
        "The official dataset description names ACRIMA, DRISHTI-GS, and HRF among the human fundus sources used to construct the synthetic glaucoma resource.",
        evidence_source_type="official_platform_metadata",
        notes="ORIGA-LIGHT and generic RIM-ONE remain external or edition-unresolved upstream sources.",
    ),
    _edge(
        "itec_iris_pupil",
        "derived_from",
        "cataract_101",
        "https://ftp.itec.aau.at/datasets/ovid/iris_pupil_seg/index.html",
        "The official ITEC page states that the annotated iris and pupil frames were selected from Cataract-101 surgery videos.",
        evidence_source_type="official_project_page",
    ),
    _edge(
        "mendeley_utilizing_responsive_web_portal_studying_disc",
        "derived_from",
        "drishti_gs",
        "https://data.mendeley.com/datasets/7xv5rzxgrh",
        "The Mendeley deposit is a distinct annotation and task layer built from DRISHTI-GS fundus images.",
        evidence_source_type="official_repository_metadata",
    ),
    _edge(
        "synthetic_retinal_oct_biomarkers",
        "derived_from",
        "kermany_oct",
        "https://huggingface.co/datasets/serag-ai/Synthetic-Ophthalmology-Images",
        "The official dataset card documents the Kermany retinal OCT collection as the source for the four synthetic diagnostic classes.",
        evidence_source_type="official_dataset_card",
    ),
)


def relationships_for(record_id: str) -> List[Dict[str, str]]:
    """Return stable compact relationships for one catalog record."""

    return [
        {"type": edge.relationship_type, "target": edge.target_record_id}
        for edge in RELATIONSHIP_EVIDENCE
        if edge.source_record_id == record_id
    ]


def evidence_by_record() -> Dict[str, List[RelationshipEvidence]]:
    """Index evidence edges by source record without importing the registry."""

    indexed: Dict[str, List[RelationshipEvidence]] = {}
    for edge in RELATIONSHIP_EVIDENCE:
        indexed.setdefault(edge.source_record_id, []).append(edge)
    return indexed
