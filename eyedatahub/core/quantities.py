"""Reviewed quantities reported for EyeDataHub catalog records.

The historical catalog exposed one ``num_samples`` value and one inferred unit.
That representation is retained for compatibility, but it cannot describe a
multimodal resource that reports, for example, both images and question-answer
pairs.  This module stores reviewed primary-count corrections and additional
source-reported quantities in one source-linked location.

Counts with different units are never added together.  A quantity describes
the source scope recorded in its ``scope`` field and may refer either to the
current official deposit or to a cohort described by the source.  Notes retain
important version, overlap, and duplication qualifications.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any, Dict, List, Optional


QUANTITY_UNITS = frozenset(
    {
        "annotated_images",
        "annotated_instances",
        "animal_models",
        "b_scans",
        "deposited_files",
        "documents",
        "embedding_vectors",
        "experimental_eyes",
        "experimental_animals",
        "examinations",
        "eyes",
        "frames",
        "families",
        "group_enrollments",
        "image_pairs",
        "image_references",
        "image_report_pairs",
        "images",
        "linked_image_rows",
        "longitudinal_samples",
        "measurement_rows",
        "mri_scans",
        "participants",
        "question_answer_pairs",
        "questions",
        "records",
        "rows",
        "sentence_pairs",
        "signals",
        "source_datasets",
        "surgeries",
        "text_items",
        "video_clip_instruction_pairs",
        "video_clips",
        "videos",
        "visual_field_tests",
        "visual_fields",
        "volumes",
    }
)

EVIDENCE_BASES = frozenset(
    {
        "associated_publication",
        "current_deposit_file_listing",
        "current_deposit_table",
        "derived_from_reported_components",
        "legacy_catalog_field",
        "official_source_description",
    }
)

# These values are part of the catalog's machine-readable quantity contract.
# Keep the vocabulary deliberately narrow: a source count should say whether it
# is exact, approximate, not assessed, or conflicts with another source rather
# than introducing an unstructured qualification string.
EXACTNESS_VALUES = frozenset(
    {
        "exact",
        "approximate",
        "not_assessed",
        "source_conflict",
    }
)

# ``record_id`` is intentionally internal to ``QuantityEvidence``.  Quantities
# are nested below their catalog record, so public JSON and CSV cells contain
# exactly these fields and do not duplicate the record identifier.
PUBLIC_QUANTITY_FIELDS = (
    "count",
    "unit",
    "scope",
    "evidence_url",
    "evidence_basis",
    "primary",
    "exactness",
    "review_date",
    "notes",
)


@dataclass(frozen=True)
class QuantityEvidence:
    """One count, its exact unit, scope, and public supporting evidence."""

    record_id: str
    count: int
    unit: str
    scope: str
    evidence_url: str
    evidence_basis: str
    primary: bool = False
    exactness: str = "exact"
    review_date: str = "2026-08-01"
    notes: str = ""

    def __post_init__(self) -> None:
        if not isinstance(self.count, int) or isinstance(self.count, bool) or self.count < 0:
            raise ValueError("Quantity counts must be non-negative")
        if self.unit not in QUANTITY_UNITS:
            raise ValueError(f"Unsupported quantity unit: {self.unit}")
        if self.evidence_basis not in EVIDENCE_BASES:
            raise ValueError(f"Unsupported evidence basis: {self.evidence_basis}")
        if self.exactness not in EXACTNESS_VALUES:
            raise ValueError(f"Unsupported exactness value: {self.exactness}")


def _q(
    record_id: str,
    count: int,
    unit: str,
    scope: str,
    evidence_url: str,
    *,
    basis: str = "official_source_description",
    primary: bool = False,
    exactness: str = "exact",
    notes: str = "",
    review_date: str = "2026-08-01",
) -> QuantityEvidence:
    return QuantityEvidence(
        record_id=record_id,
        count=count,
        unit=unit,
        scope=scope,
        evidence_url=evidence_url,
        evidence_basis=basis,
        primary=primary,
        exactness=exactness,
        review_date=review_date,
        notes=notes,
    )


QUANTITY_EVIDENCE: tuple[QuantityEvidence, ...] = (
    # Records whose historical primary count was missing or had an ambiguous unit.
    _q(
        "anterior_segment_smile",
        69,
        "eyes",
        "Source-described cohort: 69 eyes from 35 participants",
        "https://doi.org/10.21203/rs.3.rs-8639765/v1",
        basis="associated_publication",
        primary=True,
        notes="The current Mendeley v1 deposit does not expose an enumerable row count.",
    ),
    _q(
        "anterior_segment_smile",
        35,
        "participants",
        "Source-described cohort",
        "https://doi.org/10.21203/rs.3.rs-8639765/v1",
        basis="associated_publication",
    ),
    _q("bajwa_multi_eye", 300, "images", "Four-class image collection", "https://data.mendeley.com/datasets/rgwpd4m785/3", primary=True),
    _q("belo", 900, "questions", "Held-out multiple-choice benchmark", "https://belo-dataset.vercel.app/", primary=True),
    _q(
        "brset_mbrset_embeddings",
        53188,
        "embedding_vectors",
        "Rows across six model-specific CSV files",
        "https://physionet.org/content/embedding-brset-mbrset/1.0.0/",
        basis="derived_from_reported_components",
        primary=True,
        notes="Two BRSET files contain 16,266 rows each and four mBRSET files contain 5,164 rows each.",
    ),
    _q(
        "brset_mbrset_embeddings",
        21430,
        "images",
        "Distinct parent images represented by at least one embedding",
        "https://physionet.org/content/embedding-brset-mbrset/1.0.0/",
        basis="derived_from_reported_components",
        notes="This is 16,266 BRSET plus 5,164 mBRSET images; it is not a new image cohort.",
    ),
    _q("casia_iris_v4", 54601, "images", "Six CASIA-IrisV4 subsets", "https://hycasia.github.io/dataset/casia-irisv4/", primary=True),
    _q("cataract101_extended_labels", 101, "videos", "Cataract-101 videos receiving extended labels", "https://zenodo.org/records/4984167", primary=True),
    _q(
        "china_fundus_cimt",
        5806,
        "images",
        "PNG fundus images in the current Figshare version 1 deposit",
        "https://doi.org/10.6084/m9.figshare.27907056.v1",
        basis="current_deposit_file_listing",
        primary=True,
        review_date="2026-08-02",
        notes="The complete current deposit was inspected; both source MD5 values matched and the image archive contained 5,806 PNG files.",
    ),
    _q(
        "china_fundus_cimt",
        2,
        "deposited_files",
        "Files in the current Figshare version 1 deposit",
        "https://doi.org/10.6084/m9.figshare.27907056.v1",
        basis="current_deposit_file_listing",
        review_date="2026-08-02",
        notes="The deposit contains one JSON metadata file and one ZIP archive.",
    ),
    _q("coph100", 491, "image_pairs", "Registered infant fundus pairs", "https://doi.org/10.6084/m9.figshare.27061084.v1", primary=True),
    _q("coph100", 982, "images", "Images participating in 491 pairs", "https://doi.org/10.6084/m9.figshare.27061084.v1", basis="derived_from_reported_components"),
    _q("coph100", 100, "eyes", "Source-described infant eyes", "https://doi.org/10.6084/m9.figshare.27061084.v1"),
    _q("corneal_epithelium_confocal", 7, "participants", "Keratoconus patients with both-eye measurements", "https://data.mendeley.com/datasets/n3gky25brh/2", primary=True),
    _q("corneal_tomography_iol", 61, "eyes", "One structured row per eye", "https://data.mendeley.com/datasets/wddj7bh9p9/1", primary=True),
    _q("cornorb", 1454, "eyes", "Rows in the current clinical-data table", "https://zenodo.org/records/20542091", basis="current_deposit_table", primary=True),
    _q("dme_vqa", 13470, "question_answer_pairs", "Train, validation, and test QA pairs", "https://zenodo.org/records/6784358", basis="derived_from_reported_components", primary=True),
    _q("dme_vqa", 679, "images", "Train, validation, and test images", "https://zenodo.org/records/6784358", basis="derived_from_reported_components"),
    _q("dme_vqa_logical", 13470, "question_answer_pairs", "DME VQA pairs with added logical relations", "https://zenodo.org/records/7777849", primary=True, notes="The source states that this is the same DME VQA dataset with logical relations added."),
    _q("dme_vqa_logical", 679, "images", "Parent DME VQA images reused by this extension", "https://zenodo.org/records/7777849", notes="These images overlap completely with dme_vqa."),
    _q("dryad_aoslo_rpe", 10, "participants", "Normal participants in the primary cohort", "https://doi.org/10.5061/dryad.b41j15h", primary=True),
    _q("dryad_cornea_oct_pentacam", 52, "participants", "Participant directories represented in the corneal OCT component of Dryad version 5", "https://doi.org/10.5061/dryad.tht76hf0c", basis="current_deposit_file_listing", primary=True),
    _q("dryad_cornea_oct_pentacam", 208, "images", "Corneal OCT TIFF files in Dryad version 5", "https://doi.org/10.5061/dryad.tht76hf0c", basis="current_deposit_file_listing", notes="Four TIFF files occur in each of 52 participant directories."),
    _q("dryad_cornea_oct_pentacam", 102, "records", "Pentacam CSV tomography matrices in Dryad version 5", "https://doi.org/10.5061/dryad.tht76hf0c", basis="current_deposit_file_listing"),
    _q("dryad_cornea_oct_pentacam", 1, "deposited_files", "OCT_.zip in Dryad version 5", "https://doi.org/10.5061/dryad.tht76hf0c", basis="current_deposit_file_listing"),
    _q("dryad_functional_oct_alzheimer", 40, "participants", "Unique participant identifiers across the two deposited profile tables in Dryad version 6", "https://doi.org/10.5061/dryad.msbcc2ftc", basis="current_deposit_table", primary=True, notes="The Experiment 2 table has four participants, three of whom also occur in the Experiments 1, 3, and 4 table."),
    _q("dryad_functional_oct_alzheimer", 1370, "rows", "Processed retinal-reflectivity profile rows across the two deposited tables", "https://doi.org/10.5061/dryad.msbcc2ftc", basis="current_deposit_table"),
    _q("dryad_functional_oct_alzheimer", 432, "images", "ANALYZE-format .img objects in the Dryad version 6 archive", "https://doi.org/10.5061/dryad.msbcc2ftc", basis="current_deposit_file_listing", notes="This file count includes raw, manually marked, flattened, and spatially normalized representations and is not an independent acquisition count."),
    _q("dryad_functional_oct_alzheimer", 1, "deposited_files", "RAR archive in Dryad version 6", "https://doi.org/10.5061/dryad.msbcc2ftc", basis="current_deposit_file_listing"),
    _q("dryad_functional_oct_alzheimer", 8, "group_enrollments", "Healthy young-adult experiment", "https://doi.org/10.5061/dryad.msbcc2ftc"),
    _q("dryad_functional_oct_alzheimer", 3, "group_enrollments", "Aquaporin-4 antibody experiment", "https://doi.org/10.5061/dryad.msbcc2ftc"),
    _q("dryad_functional_oct_alzheimer", 14, "group_enrollments", "Early-onset Alzheimer group", "https://doi.org/10.5061/dryad.msbcc2ftc"),
    _q("dryad_functional_oct_alzheimer", 14, "group_enrollments", "Age-matched control group", "https://doi.org/10.5061/dryad.msbcc2ftc", notes="Group counts are not summed because cross-experiment overlap was not resolved."),
    _q(
        "dryad_rpgr_cone_rod_wes",
        1,
        "participants",
        "Proband represented by the paired whole-exome sequencing files",
        "https://doi.org/10.5061/dryad.5qfttdz5d",
        primary=True,
        review_date="2026-08-02",
        notes="The complete current Dryad version 2 deposit contains paired reads for one source-described proband.",
    ),
    _q(
        "dryad_rpgr_cone_rod_wes",
        2,
        "deposited_files",
        "Paired FASTQ files in the current Dryad version 2 deposit",
        "https://doi.org/10.5061/dryad.5qfttdz5d",
        basis="current_deposit_file_listing",
        review_date="2026-08-02",
        notes="Both source checksums matched during complete-deposit inspection.",
    ),
    _q("dryad_gcc_glaucoma", 406, "eyes", "Eye-level table rows", "https://doi.org/10.5061/dryad.xwdbrv1tn", primary=True),
    _q("dryad_gcc_glaucoma", 203, "participants", "Participants contributing 406 eye rows", "https://doi.org/10.5061/dryad.xwdbrv1tn"),
    _q("dryad_namd_visual_prediction", 926, "eyes", "Treatment-naive first-treated eyes in the primary analysis", "https://doi.org/10.5061/dryad.573n5tb5d", primary=True),
    _q("dryad_retinal_vein_cannulation", 26, "experimental_eyes", "Ex vivo porcine eyes", "https://doi.org/10.5061/dryad.3ffbg79zd", primary=True),
    _q("dryad_subretinal_robot", 21, "experimental_eyes", "Bleb-formation attempts in ex vivo porcine eyes", "https://doi.org/10.1126/scirobotics.adp7700", basis="associated_publication", primary=True, notes="The current deposit does not expose a reproducible frame or video count."),
    _q("dryad_uveal_melanoma_coog2", 1577, "participants", "Multicenter prognostic cohort", "https://doi.org/10.5061/dryad.n8pk0p340", primary=True),
    _q("erdes", 5381, "video_clips", "Ocular-ultrasound B-scan clips", "https://arxiv.org/abs/2503.04525", basis="associated_publication", primary=True),
    _q("eye_disease_image_mendeley", 5335, "images", "Original and augmented image collection", "https://data.mendeley.com/datasets/s9bfhswzjb/1", primary=True),
    _q("eyecatcher_visual_field", 440, "visual_field_tests", "Twenty participants by two eyes by eleven scheduled tests", "https://data.mendeley.com/datasets/swsfj47cxw/2", primary=True),
    _q("eyecatcher_visual_field", 20, "participants", "Home-monitoring cohort", "https://data.mendeley.com/datasets/swsfj47cxw/2"),
    _q("fang_sbsdi_oct", 323, "images", "TIFF images in the separately named human and human-derived components of the official source archive", "https://people.duke.edu/~sf59/Fang_TMI_2013.htm", basis="current_deposit_file_listing", primary=True, notes="Includes 195 real-human TIFFs, 108 human-derived synthetic TIFFs, and 20 human-derived dictionary-training TIFFs. Software, demonstrations, and nonhuman source-archive components are excluded."),
    _q("fang_sbsdi_oct", 41, "participants", "Twenty-eight eyes from 28 participants used for human-derived synthetic data and 13 participants used for real acquisitions", "https://doi.org/10.1109/TMI.2013.2271904", basis="associated_publication", notes="Participant groups are distinct in the associated paper."),
    _q("fimd", 70, "image_pairs", "Longitudinal retinal registration pairs", "https://data.mendeley.com/datasets/jkzsh6pcv4/1", primary=True),
    _q("fimd", 140, "images", "Images participating in 70 pairs", "https://data.mendeley.com/datasets/jkzsh6pcv4/1", basis="derived_from_reported_components"),
    _q("fundus_105k", 105000, "text_items", "Fundus-focused text corpus entries", "https://huggingface.co/datasets/PJMixers-Dev/Fundus-105K", primary=True),
    _q("fundus_cc_2_5m", 2500000, "text_items", "Multilingual fundus-related corpus entries", "https://huggingface.co/datasets/PJMixers-Dev/Fundus-CC-2.5M", primary=True),
    _q("fundus_domain_generalization", 1441, "images", "Five source domains after the documented train/test composition", "https://zenodo.org/records/8009107", basis="derived_from_reported_components", primary=True, notes="The images reuse REFUGE, Drishti-GS, ORIGA, and RIGA sources."),
    _q("fundus_report_dataset", 422, "image_report_pairs", "Fundus or UWF image-report rows", "https://huggingface.co/datasets/zzzzineun/fundus-report-dataset", primary=True),
    _q("ghana_eye_screening", 2494, "participants", "Participants completing questionnaire and clinical examination", "https://data.mendeley.com/datasets/mfv6sb5wyc/4", primary=True),
    _q(
        "gleam",
        3600,
        "images",
        "Three image modalities for each of 1,200 distinct samples in the all_samples directory",
        "https://www.kaggle.com/datasets/zhangyiyinge/gleam-dataset",
        basis="derived_from_reported_components",
        primary=True,
        review_date="2026-08-02",
        notes="The 4,320 additional JPG files under split directories repeat samples for model-development partitions and are not additional source images.",
    ),
    _q(
        "gleam",
        1200,
        "records",
        "Distinct tri-modal glaucoma samples",
        "https://www.kaggle.com/datasets/zhangyiyinge/gleam-dataset",
        review_date="2026-08-02",
        notes="Each sample contains one SLO image, one OCT thickness map, and one visual-field pattern-deviation map.",
    ),
    _q(
        "gleam",
        841,
        "participants",
        "Source-reported patient cohort",
        "https://www.kaggle.com/datasets/zhangyiyinge/gleam-dataset",
        review_date="2026-08-02",
    ),
    _q("goblet_cell_segmentation", 24, "images", "Unpatched microscopy fields", "https://doi.org/10.5281/zenodo.18642562", primary=True),
    _q("goblet_cell_segmentation", 1152, "images", "Derivative 256 by 256 patches", "https://doi.org/10.5281/zenodo.18642562", notes="Patches derive from the 24 primary fields and must not be added as independent source images."),
    _q("hrf_seg_plus", 45, "images", "HRF images receiving extended annotations", "https://zenodo.org/records/16744782", primary=True),
    _q("hassan_composite_retina", 64, "images", "Fundus component described by the associated publication", "https://doi.org/10.1016/B978-0-12-817438-8.00005-5", basis="associated_publication", notes="The count was not confirmed as the exact content of the cataloged Mendeley v4 archive."),
    _q("hassan_composite_retina", 2497, "b_scans", "OCT component described by the associated publication", "https://doi.org/10.1016/B978-0-12-817438-8.00005-5", basis="associated_publication", notes="The count was not confirmed as the exact content of the cataloged Mendeley v4 archive."),
    _q("insegcat", 5581, "annotated_images", "Current Dataset 1 v2 plus Dataset 2", "https://ftp.itec.aau.at/datasets/ovid/InSegCat/", basis="derived_from_reported_components", primary=True),
    _q("insegcat", 843, "annotated_images", "Dataset 1 v2, manually annotated Cataract-101 frames", "https://ftp.itec.aau.at/datasets/ovid/InSegCat/"),
    _q("insegcat", 4738, "annotated_images", "Dataset 2, CaDIS-derived annotations", "https://ftp.itec.aau.at/datasets/ovid/InSegCat/"),
    _q("irfdrd", 700, "images", "JPEG files in the three nested class archives", "https://zenodo.org/records/12552326", basis="current_deposit_file_listing", primary=True, notes="Archive listing resolves a conflicting class table in the source description: 153 healthy, 59 mild, 304 moderate, 99 severe, and 85 PDR files."),
    _q("jrc_multimodal_vessels", 120, "images", "Forty images in each of FA, FAF, and infrared subsets", "https://zenodo.org/records/17874693", basis="derived_from_reported_components", primary=True),
    _q("lmod_cataract_1k", 2256, "images", "Rows in the versioned Hugging Face deposit", "https://huggingface.co/datasets/mehti/LMOD-Cataract-1K", basis="current_deposit_table", primary=True),
    _q("lmod_cataract_1k_cot", 2256, "images", "PNG images in the versioned Hugging Face deposit", "https://huggingface.co/datasets/mehti/LMOD-Cataract-1K-surgical-analysis-cot", basis="current_deposit_file_listing", primary=True),
    _q("lmod_cataract_1k_cot", 11280, "question_answer_pairs", "Rows across five cross-validation train/validation fold pairs", "https://huggingface.co/datasets/mehti/LMOD-Cataract-1K-surgical-analysis-cot", basis="current_deposit_table", notes="The five folds repeat the 2,256 source images; 11,280 is not a unique-image count."),
    _q("lmod_plus", 32633, "annotated_instances", "Composite benchmark instances", "https://kfzyqin.github.io/lmod_plus/", primary=True),
    _q("mm_retinal_reason", 130, "question_answer_pairs", "Sixty basic and seventy complex reasoning records", "https://huggingface.co/datasets/lxirich/MM-Retinal-Reason/tree/d6243baa82c0914dba3c6f43ca79fdbf856982ef", basis="current_deposit_table", primary=True),
    _q("mm_retinal_reason", 227, "image_references", "Image references across the 130 reasoning records", "https://huggingface.co/datasets/lxirich/MM-Retinal-Reason/tree/d6243baa82c0914dba3c6f43ca79fdbf856982ef", basis="current_deposit_table", notes="Complex records can reference more than one image; references need not be unique images."),
    _q("mm_retinal_reason", 45, "source_datasets", "Public source datasets reported by the resource", "https://huggingface.co/datasets/lxirich/MM-Retinal-Reason/tree/d6243baa82c0914dba3c6f43ca79fdbf856982ef"),
    _q("mshf", 1302, "images", "Unique source images in the Original directory", "https://doi.org/10.6084/m9.figshare.21507564", basis="current_deposit_file_listing", primary=True),
    _q("mshf", 1302, "images", "Train/test analysis copies", "https://doi.org/10.6084/m9.figshare.21507564", basis="current_deposit_file_listing", notes="These are copies of the 1,302 source images and are not an additional cohort."),
    _q("ophthalmology_eqa_v3", 49300, "questions", "Explanatory or free-form ophthalmology questions", "https://huggingface.co/datasets/BaekSeungJu/Ophthalmology-EQA-v3", primary=True),
    _q("ophthalmology_mcqa_v3", 51745, "questions", "Multiple-choice ophthalmology questions", "https://huggingface.co/datasets/BaekSeungJu/Ophthalmology-MCQA-v3", primary=True),
    _q("ophthalmology_pubmed_corpus", 39794, "documents", "Ophthalmology-focused PubMed corpus records", "https://huggingface.co/datasets/BaekSeungJu/Ophthalmology-PubMed-Corpus", primary=True),
    _q("ophthalvqa", 600, "question_answer_pairs", "Rows in OphthalVQA.csv", "https://doi.org/10.6084/m9.figshare.25624917", basis="current_deposit_table", primary=True),
    _q("ophthalvqa", 60, "images", "JPG image files in the current deposit", "https://doi.org/10.6084/m9.figshare.25624917", basis="current_deposit_file_listing"),
    _q("ophthalwechat", 30120, "question_answer_pairs", "Rows in OphthalWeChat_QA.xlsx", "https://doi.org/10.6084/m9.figshare.29064149", basis="current_deposit_table", primary=True),
    _q("ophthalwechat", 3469, "linked_image_rows", "Rows in OphthalWeChat_image_information.xlsx", "https://doi.org/10.6084/m9.figshare.29064149", basis="current_deposit_table", notes="The deposit stores image links and identifiers, not image files; 3,403 URLs are unique."),
    _q("ophtho_readability", 139, "documents", "Data rows in the deposited workbook", "https://zenodo.org/records/16592100", basis="current_deposit_table", primary=True),
    _q("paired_retina", 399, "images", "Image rows in the current versioned Hugging Face deposit", "https://huggingface.co/datasets/smartretina2025/paired_retina/tree/9dc39ab4aebb3e25a7e9f409ad7b19fc14db73c5", basis="current_deposit_file_listing", primary=True, notes="The dataset card describes a planned 327-patient paired cohort, but the current deposit contains 399 images and is not a complete 654-image paired release."),
    _q("paired_retina", 327, "participants", "Cohort described by the dataset card", "https://huggingface.co/datasets/smartretina2025/paired_retina", notes="This source-described cohort is not fully represented in the current deposit."),
    _q("rbad", 40, "images", "Branching-angle benchmark images", "https://github.com/Retinal-Research/RBAD", primary=True),
    _q("reta_benchmark", 81, "images", "IDRiD-derived images with vascular-tree annotations", "https://doi.org/10.6084/m9.figshare.16960855", primary=True),
    _q("retinal_dr_longitudinal", 1115, "image_pairs", "Rows in corrected_manifest.csv", "https://huggingface.co/datasets/usama10/retinal-dr-longitudinal/tree/d6e13e91dae69f3080259afd478db92412c7f32d", basis="current_deposit_table", primary=True),
    _q("retinal_dr_longitudinal", 2428, "images", "JPG files in the current deposit", "https://huggingface.co/datasets/usama10/retinal-dr-longitudinal/tree/d6e13e91dae69f3080259afd478db92412c7f32d", basis="current_deposit_file_listing", notes="The deposit contains 1,250 baseline and 1,178 follow-up images; 2,230 participate in the corrected 1,115-pair manifest."),
    _q("retinal_dr_longitudinal", 572, "participants", "Unique patient IDs in corrected_manifest.csv", "https://huggingface.co/datasets/usama10/retinal-dr-longitudinal/tree/d6e13e91dae69f3080259afd478db92412c7f32d", basis="current_deposit_table"),
    _q("retinal_corrugations_oct", 69, "b_scans", "Baseline swept-source OCT scans described for the current Mendeley v2 deposit", "https://doi.org/10.1016/j.dib.2023.108920", basis="associated_publication", primary=True, exactness="source_conflict", notes="The article abstract and specifications table report 69 scans from 66 patients; one methods passage reports 66 assessed scans."),
    _q("retinal_corrugations_oct", 66, "participants", "Patients represented by the baseline SS-OCT cohort", "https://doi.org/10.1016/j.dib.2023.108920", basis="associated_publication"),
    _q("retinal_vessel_robustness", 13024, "images", "Files under the images directories in all three current archives", "https://zenodo.org/records/12659652", basis="current_deposit_file_listing", primary=True, notes="Includes 5,920 DRIVE, 4,144 CHASE, and 2,960 STARE original or augmented images; parent datasets overlap catalog records."),
    _q("rfmid2", 860, "images", "RFMiD 2.0 auxiliary images", "https://zenodo.org/records/7505822", primary=True),
    _q("riga_plus", 1461, "images", "TIF images in the RIGA directory of the current deposit", "https://zenodo.org/records/6325549", basis="current_deposit_file_listing", primary=True, notes="The source reports removal of six RIGA duplicates and cross-dataset duplicates with MESSIDOR."),
    _q("rocc", 165, "volumes", "OCT volumes in the challenge cohort", "https://rocc.grand-challenge.org/", primary=True),
    _q("rop_synthetic_mendeley", 5842, "images", "Source retinal fundus images", "https://data.mendeley.com/datasets/fscyyhg6vt/1", primary=True),
    _q("rop_synthetic_mendeley", 963, "participants", "Preterm infants contributing source images", "https://data.mendeley.com/datasets/fscyyhg6vt/1"),
    _q("ru_medical_texts_ophthalmology", 3473, "sentence_pairs", "Russian-English sentence or glossary pairs", "https://www.kaggle.com/datasets/cheshrcat/ru-medical-texts-ophtalmology", primary=True),
    _q("sics155", 155, "videos", "SICS surgical videos", "https://zenodo.org/records/19482928", primary=True),
    _q("soul_octa", 178, "longitudinal_samples", "Six source-reported longitudinal subsets", "https://doi.org/10.6084/m9.figshare.24893358.v3", primary=True, notes="The current archive contains 2,046 JPG assets including raw images and corresponding labels; these are not 2,046 independent samples."),
    _q("superccm_fineset", 210, "images", "Restricted fine-segmentation image set", "https://zenodo.org/records/17051148", primary=True),
    _q("trend2_fundus", 28, "images", "Primary color fundus images", "https://zenodo.org/records/7678656", primary=True),
    _q("thyroid_ophthalmopathy_external", 2, "deposited_files", "Artifacts listed by the current Mendeley v2 deposit", "https://data.mendeley.com/datasets/z7ys7r4bdn/2", basis="current_deposit_file_listing", notes="The source does not report the number of photographs inside dataset.zip."),
    _q("ut_fsocta", 112, "participants", "Subjects with aligned fundus and en-face OCTA data", "https://zenodo.org/records/6476639", primary=True),
    _q("ut_fsocta", 194, "images", "Full-field fundus JPG files in the current archive", "https://zenodo.org/records/6476639", basis="current_deposit_file_listing"),
    _q("ut_fsocta", 194, "images", "Full-field synthetic OCTA PNG files in the current archive", "https://zenodo.org/records/6476639", basis="current_deposit_file_listing", notes="Synthetic outputs derive from the fundus images and are not an independent cohort."),
    _q("ut_fsocta", 362, "images", "Cropped en-face OCTA PNG files in the current archive", "https://zenodo.org/records/6476639", basis="current_deposit_file_listing"),
    _q("uwhvf", 28943, "visual_field_tests", "HFA 24-2 tests", "https://github.com/uw-biomedical-ml/uwhvf", primary=True),
    _q("visual_field_testing_experiment", 78, "visual_fields", "Rows and distinct IDs in fields.csv", "https://www.kaggle.com/datasets/shozosaeki/visual-field-testing-experiment", basis="current_deposit_table", primary=True),
    _q("visual_field_testing_experiment", 15678, "measurement_rows", "Eye-guided measurement rows in display_results.csv", "https://www.kaggle.com/datasets/shozosaeki/visual-field-testing-experiment", basis="current_deposit_table"),
    _q("visual_field_testing_experiment", 4212, "measurement_rows", "Humphrey field-analyzer rows in hfa_results.csv", "https://www.kaggle.com/datasets/shozosaeki/visual-field-testing-experiment", basis="current_deposit_table"),

    # Source-backed corrections where the old text heuristic selected the wrong unit.
    _q("eyecare_100k", 102000, "question_answer_pairs", "Source-described VQA corpus", "https://github.com/DCDmllm/EyecareGPT", primary=True, exactness="approximate", notes="The dataset was described as pending release at the catalog cutoff."),
    _q("eyecare_100k", 58485, "images", "Source images represented by the VQA corpus", "https://github.com/DCDmllm/EyecareGPT", exactness="approximate"),
    _q("fprm_retina", 3361, "images", "Fundus photographs", "https://doi.org/10.1038/s41597-024-03690-6", basis="associated_publication", primary=True),
    _q("fprm_retina", 1683, "participants", "Participants contributing fundus photographs", "https://doi.org/10.1038/s41597-024-03690-6", basis="associated_publication"),
    _q("fprm_retina", 384, "participants", "Participants contributing additional multimodal imaging", "https://doi.org/10.1038/s41597-024-03690-6", basis="associated_publication", notes="This group is not added to the fundus cohort because overlap is not resolved here."),
    _q("gaze_capture", 2445504, "frames", "Labeled mobile-camera frames", "https://gazecapture.csail.mit.edu/", primary=True),
    _q("gaze_capture", 1474, "participants", "Crowdsourced participants", "https://gazecapture.csail.mit.edu/"),
    _q("gaze360", 172000, "frames", "Labeled panoramic-camera frames", "http://gaze360.csail.mit.edu/", primary=True, exactness="approximate"),
    _q("gaze360", 238, "participants", "Source-described participants", "http://gaze360.csail.mit.edu/"),
    _q("leops_erg", 9743, "signals", "Averaged ERG and oscillatory-potential waveforms", "https://data.mendeley.com/datasets/w3yx7hdds7/1", basis="derived_from_reported_components", primary=True),
    _q("leops_erg", 253, "participants", "Pediatric participants", "https://data.mendeley.com/datasets/w3yx7hdds7/1"),
    _q("leops_erg", 558, "images", "Electrode-position eye images", "https://data.mendeley.com/datasets/w3yx7hdds7/1"),
    _q("lpw", 130856, "frames", "Labeled eye-region images", "https://www.mpi-inf.mpg.de/departments/computer-vision-and-machine-learning/research/gaze-based-human-computer-interaction/labelled-pupils-in-the-wild-lpw", primary=True),
    _q("lpw", 66, "videos", "High-speed source videos", "https://www.mpi-inf.mpg.de/departments/computer-vision-and-machine-learning/research/gaze-based-human-computer-interaction/labelled-pupils-in-the-wild-lpw"),
    _q("lpw", 22, "participants", "Participants recorded in everyday locations", "https://www.mpi-inf.mpg.de/departments/computer-vision-and-machine-learning/research/gaze-based-human-computer-interaction/labelled-pupils-in-the-wild-lpw"),
    _q("multieye", 103959, "images", "Fundus and OCT images across the composite benchmark", "https://arxiv.org/abs/2412.09402", basis="derived_from_reported_components", primary=True, notes="Component source datasets overlap other catalog records."),
    _q("multieye", 58036, "images", "Fundus component", "https://arxiv.org/abs/2412.09402"),
    _q("multieye", 45923, "images", "OCT component", "https://arxiv.org/abs/2412.09402"),
    _q("oct_ms_jhu", 1715, "b_scans", "B-scans in 35 OCT volumes", "https://doi.org/10.1016/j.dib.2018.11.060", basis="associated_publication", primary=True),
    _q("oct_ms_jhu", 35, "volumes", "Spectralis OCT volumes", "https://doi.org/10.1016/j.dib.2018.11.060", basis="associated_publication"),
    _q("octa_macula_coronal", 82560, "images", "Derived coronal PNG views", "https://data.mendeley.com/datasets/p5h7x55zw7/1", basis="derived_from_reported_components", primary=True),
    _q("octa_macula_coronal", 129, "participants", "Subject-level OCTA scans", "https://data.mendeley.com/datasets/p5h7x55zw7/1"),
    _q("olives", 9408, "b_scans", "Biomarker-labeled OCT B-scans", "https://zenodo.org/records/7105232", primary=True),
    _q("olives", 1268, "images", "Paired fundus photographs", "https://zenodo.org/records/7105232"),
    _q("olives", 96, "eyes", "Longitudinal eye-level cohort", "https://zenodo.org/records/7105232"),
    _q("perg_ioba", 1354, "signals", "Transient pattern electroretinogram responses", "https://physionet.org/content/perg-ioba-dataset/1.0.0/", primary=True),
    _q("perg_ioba", 304, "participants", "Participants represented in 336 records", "https://physionet.org/content/perg-ioba-dataset/1.0.0/"),
    _q("rasti_oct", 4254, "b_scans", "Approximate B-scan count", "https://doi.org/10.1109/TMI.2017.2780115", basis="associated_publication", primary=True, exactness="approximate"),
    _q("rasti_oct", 148, "volumes", "Heidelberg Spectralis volumes", "https://doi.org/10.1109/TMI.2017.2780115", basis="associated_publication"),
    _q("real_fundus", 120, "image_pairs", "Matched low-quality and high-quality fundus pairs", "https://github.com/dengzhuo-AI/Real-Fundus", primary=True),
    _q("real_fundus", 240, "images", "Images participating in 120 restoration pairs", "https://github.com/dengzhuo-AI/Real-Fundus", basis="derived_from_reported_components"),

    # Collection-level and multimodal quantities that the single primary field cannot show.
    _q("corn_collection", 12931, "images", "Sum of six source-described CORN subsets", "https://zenodo.org/records/19689814", basis="derived_from_reported_components", primary=True, notes="Includes the separately cataloged CORN1500 and CORN-Pro components and must not be added as an independent cohort total."),
    _q("duke_rpedc", 38400, "b_scans", "B-scans derived from 384 participants", "https://people.duke.edu/~sf59/Srinivasan_BOE_2014_dataset.htm"),
    _q("odir2019", 16000, "images", "Left- and right-eye fundus images", "https://odir2019.grand-challenge.org/"),
    _q("ophnet2024", 1969, "videos", "Untrimmed videos", "https://huggingface.co/datasets/xioamiyh/OphNet2024"),
    _q("ophnet2024", 17508, "video_clips", "Trimmed operation-level clips", "https://huggingface.co/datasets/xioamiyh/OphNet2024"),
    _q("ophnet2024", 14674, "video_clips", "Trimmed phase-level clips", "https://huggingface.co/datasets/xioamiyh/OphNet2024"),
)


def explicit_quantities_for(record_id: str) -> List[QuantityEvidence]:
    """Return the reviewed explicit quantities for one record."""

    return [entry for entry in QUANTITY_EVIDENCE if entry.record_id == record_id]


def primary_quantity_for(record_id: str) -> Optional[QuantityEvidence]:
    """Return the reviewed primary-count override, if one exists."""

    matches = [entry for entry in explicit_quantities_for(record_id) if entry.primary]
    if len(matches) > 1:
        raise ValueError(f"Multiple primary quantities for {record_id}")
    return matches[0] if matches else None


def quantities_for(
    record_id: str,
    legacy_count: Optional[int],
    legacy_unit: str,
    legacy_evidence_url: Optional[str],
) -> List[Dict[str, Any]]:
    """Return stable public quantity dictionaries for one catalog record."""

    explicit = explicit_quantities_for(record_id)
    if not any(entry.primary for entry in explicit) and legacy_count is not None:
        unit = legacy_unit if legacy_unit in QUANTITY_UNITS else "records"
        explicit = [
            QuantityEvidence(
                record_id=record_id,
                count=int(legacy_count),
                unit=unit,
                scope="Primary quantity reported in the reviewed catalog source",
                evidence_url=legacy_evidence_url or "",
                evidence_basis="legacy_catalog_field",
                primary=True,
                exactness="not_assessed",
                notes=(
                    "The historical unit was not in the controlled quantity vocabulary; "
                    "this entry is retained as records."
                    if legacy_unit not in QUANTITY_UNITS
                    else ""
                ),
            ),
            *explicit,
        ]

    return [
        {key: asdict(entry)[key] for key in PUBLIC_QUANTITY_FIELDS}
        for entry in explicit
    ]


def unresolved_primary_record_ids(record_ids: List[str]) -> List[str]:
    """Return records for which no reviewed or legacy primary count exists."""

    explicit_primary = {
        entry.record_id for entry in QUANTITY_EVIDENCE if entry.primary
    }
    return sorted(record_id for record_id in record_ids if record_id not in explicit_primary)
