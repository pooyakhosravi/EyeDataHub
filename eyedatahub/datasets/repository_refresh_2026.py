"""Literature and repository additions verified through July 14, 2026.

The records in this module were checked against primary dataset landing pages,
repository APIs, and (where available) peer-reviewed data descriptors. Derived
benchmarks are retained only when they add a distinct annotation or evaluation
surface; their upstream dependencies are called out in ``notes``.
"""
from __future__ import annotations

from typing import Any

from eyedatahub.datasets.platform_2026 import PlatformDiscoveryDataset


REFRESH_RECORDS: list[dict[str, Any]] = [
    {
        "name": "soul_octa",
        "full_name": "SOUL: OCTA Human-Machine Collaborative Annotation Dataset",
        "description": (
            "Longitudinal OCT angiography projection maps with vessel labels, "
            "clinical text, and treatment/follow-up groupings."
        ),
        "modality": "octa",
        "tasks": ["segmentation", "classification", "progression_analysis"],
        "num_samples": 178,
        "download_type": "figshare",
        "download_url": "https://doi.org/10.6084/m9.figshare.24893358.v3",
        "license": "CC BY 4.0",
        "citation": (
            "Xue J, Feng Z, Zeng L, et al. Soul: An OCTA dataset based on "
            "Human Machine Collaborative Annotation Framework. Scientific "
            "Data. 2024;11. doi:10.1038/s41597-024-03665-7"
        ),
        "tags": [
            "octa",
            "vessel_segmentation",
            "longitudinal",
            "anti_vegf",
            "clinical_text",
            "figshare",
        ],
        "size_gb": 0.113,
        "notes": (
            "The six source-reported longitudinal subsets total 178 samples. "
            "The release includes raw images, vessel annotations, and clinical text."
        ),
        "source": {"id": "24893358"},
    },
    {
        "name": "periorbital_segmentation",
        "full_name": "Open-Source Periorbital Segmentation Dataset",
        "description": (
            "Cropped periorbital images with multi-structure masks for the iris, "
            "sclera, eyelid, caruncle, and eyebrow."
        ),
        "modality": "external_eye",
        "tasks": ["segmentation", "measurement"],
        "num_samples": 2842,
        "download_type": "zenodo",
        "download_url": "https://doi.org/10.5281/zenodo.13916845",
        "license": "CC BY 4.0",
        "citation": (
            "Nahass GR, Koehler E, Tomaras N, et al. Open-Source Periorbital "
            "Segmentation Dataset for Ophthalmic Applications. Ophthalmology "
            "Science. 2025;5:100757. doi:10.1016/j.xops.2025.100757"
        ),
        "tags": [
            "external_eye",
            "periorbital",
            "iris",
            "sclera",
            "eyelid",
            "multi_annotator",
            "derived",
            "zenodo",
        ],
        "size_gb": 0.190,
        "notes": (
            "Five annotators labeled crops derived from the Chicago Face "
            "Database and CelebAMask-HQ. The Zenodo record is CC BY 4.0, but "
            "users should also verify the terms of both upstream face datasets."
        ),
        "source": {"record": "13916845"},
    },
    {
        "name": "amd_dme_3d_oct",
        "full_name": "Comprehensive 3D OCT Dataset for AMD and DME",
        "description": (
            "Swept-source OCT volumes for AMD and DME with three-dimensional "
            "pigment epithelial detachment and intraretinal-fluid masks."
        ),
        "modality": "oct",
        "tasks": ["segmentation", "classification"],
        "num_samples": 224,
        "download_type": "figshare",
        "download_url": "https://doi.org/10.6084/m9.figshare.30582035.v1",
        "license": "CC BY 4.0",
        "citation": (
            "Huang W, Qin L, Xu M, et al. Comprehensive 3D Optical Coherence "
            "Tomography Dataset for AMD and DME: Facilitating Deep-Learning-"
            "Based 3D Segmentation. Scientific Data. 2026;13:224. "
            "doi:10.1038/s41597-025-06497-1"
        ),
        "tags": [
            "oct",
            "3d",
            "volume",
            "amd",
            "dme",
            "ped",
            "intraretinal_fluid",
            "figshare",
        ],
        "size_gb": 19.65,
        "notes": (
            "The release contains 122 AMD and 102 DME volumes. Of these, 104 "
            "volumes are labeled (62 AMD and 42 DME) and 120 are unlabeled."
        ),
        "source": {"id": "30582035"},
    },
    {
        "name": "syn_oct",
        "full_name": "SYN-OCT Synthetic Glaucoma OCT Dataset",
        "description": (
            "Synthetic circumpapillary OCT images for healthy and glaucomatous "
            "eyes with retinal-layer masks and RNFL thickness values."
        ),
        "modality": "oct",
        "tasks": ["classification", "segmentation", "regression"],
        "num_samples": 200000,
        "download_type": "zenodo",
        "download_url": "https://doi.org/10.5281/zenodo.17151869",
        "license": "CC BY 4.0",
        "citation": (
            "SYN-OCT: A synthetic dataset of ocular optical coherence "
            "tomography images from healthy and glaucoma eyes. Scientific "
            "Data. 2026. doi:10.1038/s41597-026-06946-5"
        ),
        "tags": [
            "oct",
            "synthetic",
            "glaucoma",
            "rnfl",
            "layer_segmentation",
            "zenodo",
        ],
        "size_gb": 3.255,
        "notes": (
            "Contains 100,000 synthetic glaucoma and 100,000 synthetic normal "
            "circumpapillary OCT images. No real patient images are released."
        ),
        "source": {"record": "17151869"},
    },
    {
        "name": "aroma_octa",
        "full_name": "AROMA Retinal OCTA Artifact Dataset",
        "description": (
            "Retinal OCTA scans labeled for artifact type, artifact severity, "
            "signal strength, and image quality."
        ),
        "modality": "octa",
        "tasks": ["quality_assessment", "classification", "grading"],
        "num_samples": 281,
        "download_type": "zenodo",
        "download_url": "https://doi.org/10.5281/zenodo.18258095",
        "license": "CC BY 4.0",
        "citation": (
            "Szwarcberg L, Anwer A, Gozlan A, et al. The AROMA Dataset for "
            "Automatic Detection of Artifact Type and Severity in Retinal "
            "Optical Coherence Tomography Angiography. Ophthalmic Research. "
            "2026. doi:10.1159/000551126"
        ),
        "tags": [
            "octa",
            "artifacts",
            "image_quality",
            "severity",
            "quality_control",
            "zenodo",
        ],
        "size_gb": 1.011,
        "notes": (
            "The source reports 281 scans from 115 patients. Fourteen en-face "
            "images per scan yield 3,934 derived images with seven artifact "
            "types graded on a four-level severity scale."
        ),
        "source": {"record": "18258095"},
    },
    {
        "name": "fociset_pamm",
        "full_name": "FociSet PAMM OCT Lesion Dataset",
        "description": (
            "SD-OCT B-scans with bounding-box and polygon annotations for "
            "paracentral acute middle maculopathy lesions."
        ),
        "modality": "oct",
        "tasks": ["detection", "segmentation"],
        "num_samples": 133,
        "download_type": "mendeley",
        "download_url": "https://data.mendeley.com/datasets/mkwxn7rjpm/2",
        "license": "CC BY 4.0",
        "citation": (
            "FociSet: A dataset for detection and segmentation of paracentral "
            "acute middle maculopathy lesions in OCT images. Data in Brief. "
            "2024;57:111121. doi:10.1016/j.dib.2024.111121"
        ),
        "tags": [
            "oct",
            "pamm",
            "lesion_detection",
            "yolo",
            "polygon_masks",
            "mendeley",
        ],
        "size_gb": None,
        "notes": (
            "Contains 133 OCT images with PAMM foci annotated in YOLO bounding-"
            "box and JSON polygon formats."
        ),
        "source": {"id": "mkwxn7rjpm", "version": 2},
    },
    {
        "name": "angioreport",
        "full_name": "AngioReport Fundus Angiography Report Dataset",
        "description": (
            "De-identified fluorescein and indocyanine-green angiography images "
            "paired with structured lesion descriptions and reports."
        ),
        "modality": "multimodal",
        "tasks": ["report_generation", "multilabel", "classification"],
        "num_samples": 55361,
        "download_type": "manual",
        "download_url": "https://tianchi.aliyun.com/dataset/170128",
        "license": "Unknown; competition data terms must be reviewed",
        "citation": (
            "Xu P, Chotcomwongse P, Zhang W, et al. AngioReport: Dataset and "
            "baseline methods for fundus angiography report generation. "
            "British Journal of Ophthalmology. 2025;109:1283-1288. "
            "doi:10.1136/bjo-2024-327006"
        ),
        "tags": [
            "ffa",
            "icga",
            "angiography",
            "reports",
            "image_text",
            "thailand",
            "tianchi",
        ],
        "size_gb": None,
        "notes": (
            "The paper reports 55,361 images from 1,691 patients and 3,179 "
            "eyes across 24 diagnostic conditions. Access is routed through "
            "the 2023 APTOS/Tianchi competition page; no clear dataset license "
            "was visible, so users must review current platform terms."
        ),
    },
    {
        "name": "belo",
        "full_name": "BELO Benchmark for Evaluating Language Models in Ophthalmology",
        "description": (
            "Expert-curated ophthalmology multiple-choice benchmark with "
            "rationales, assembled for held-out language-model evaluation."
        ),
        "modality": "text",
        "tasks": ["question_answering", "evaluation", "reasoning"],
        "num_samples": 900,
        "download_type": "manual",
        "download_url": "https://belo-dataset.vercel.app/",
        "license": "Unknown; mixed upstream question-bank terms",
        "citation": (
            "BELO: A Benchmark for Evaluation of Language Models in "
            "Ophthalmology. Ophthalmology Science. 2025:101050. "
            "doi:10.1016/j.xops.2025.101050"
        ),
        "tags": [
            "text",
            "mcqa",
            "llm",
            "benchmark",
            "reasoning",
            "evaluation_only",
        ],
        "size_gb": None,
        "notes": (
            "The 900 questions aggregate BCSC, BioASQ, MedMCQA, MedQA, and "
            "PubMedQA sources. The project page instructs users to request the "
            "held-out benchmark by email; verify every applicable source term."
        ),
    },
    {
        "name": "lmod_plus",
        "full_name": "LMOD+ Multimodal Ophthalmology Benchmark",
        "description": (
            "Composite multimodal ophthalmology benchmark with multi-granular "
            "anatomical, diagnostic, staging, demographic, and text annotations."
        ),
        "modality": "multimodal",
        "tasks": [
            "visual_question_answering",
            "classification",
            "grading",
            "detection",
        ],
        "num_samples": 32633,
        "download_type": "manual",
        "download_url": "https://kfzyqin.github.io/lmod_plus/",
        "license": "Mixed upstream licenses; verify each component",
        "citation": (
            "Qin Z, Liu Y, Yin Y, et al. LMOD+: A Comprehensive Multimodal "
            "Dataset and Benchmark for Developing and Evaluating Multimodal "
            "Large Language Models in Ophthalmology. ACM Transactions on "
            "Computing for Healthcare. 2026. doi:10.1145/3801746"
        ),
        "tags": [
            "multimodal",
            "mllm",
            "vqa",
            "benchmark",
            "composite",
            "derived",
        ],
        "size_gb": None,
        "notes": (
            "Integrates 32,633 instances from nine public datasets across five "
            "modalities and 12 conditions. It adds a distinct benchmark and "
            "annotation surface but does not replace the source datasets; "
            "license and redistribution terms remain component-specific."
        ),
    },
    {
        "name": "birdshot_wide",
        "full_name": "Birdshot-WIDE Widefield Fundus Dataset",
        "description": (
            "Longitudinal widefield fundus photographs from birdshot "
            "chorioretinitis eyes and age- and sex-matched controls."
        ),
        "modality": "uwf_fundus",
        "tasks": ["classification", "progression_analysis", "quality_assessment"],
        "num_samples": 6352,
        "download_type": "manual",
        "download_url": "https://doi.org/10.5281/zenodo.19474623",
        "license": "CC BY 4.0",
        "citation": (
            "Foulonneau T, Memmi C, Monnet D, Brezin AP, Vienne-Jumeau A. A "
            "Dataset of Widefield Fundus Images From Patients With Birdshot "
            "Chorioretinitis and Matched Control. Scientific Data. 2026. "
            "doi:10.1038/s41597-026-07494-8"
        ),
        "tags": [
            "uwf",
            "birdshot_chorioretinitis",
            "uveitis",
            "longitudinal",
            "controlled_access",
            "zenodo",
        ],
        "size_gb": None,
        "notes": (
            "Restricted Zenodo record requiring an access request. The source "
            "reports 5,042 images from 742 affected eyes and 1,310 images from "
            "742 matched control eyes; the birdshot cohort has a median 4.31-"
            "year follow-up. CC BY 4.0 does not remove the access agreement."
        ),
    },
    {
        "name": "goblet_cell_segmentation",
        "full_name": "Human Conjunctival Goblet Cell Segmentation Dataset",
        "description": (
            "Phase-contrast microscopy fields of cultured human conjunctival "
            "goblet cells with semantic and instance-compatible masks."
        ),
        "modality": "cell_microscopy",
        "tasks": ["segmentation", "counting"],
        "num_samples": 24,
        "download_type": "zenodo",
        "download_url": "https://doi.org/10.5281/zenodo.18642562",
        "license": "CC BY 4.0",
        "citation": (
            "Fineide FA, Bair J, Utheim TP, Riegler MA, Dartt DA. Development "
            "of Human Conjunctival Goblet Cell Segmentation Datasets to "
            "Improve Quantitation. Scientific Data. 2026. "
            "doi:10.1038/s41597-026-07309-w"
        ),
        "tags": [
            "conjunctiva",
            "goblet_cells",
            "phase_contrast",
            "cell_microscopy",
            "instance_segmentation",
            "zenodo",
        ],
        "size_gb": 0.514,
        "notes": (
            "The independent unit is 24 unpatched 2048x1536 fields with 65,108 "
            "cell instances. The release also contains 1,152 derivative 256x256 "
            "patches (75,597 counted instances because boundary cells can recur)."
        ),
        "source": {"record": "18642562"},
    },
    # Dryad search additions. Dryad publishes datasets under CC0.
    {
        "name": "dryad_gcc_glaucoma",
        "full_name": "Glaucoma Ganglion Cell Complex Clinical Dataset",
        "description": (
            "Eye-level demographics, clinical measurements, and SD-OCT-derived "
            "macular ganglion-cell-complex thickness for glaucoma assessment."
        ),
        "modality": "tabular",
        "tasks": ["classification", "regression"],
        "num_samples": 406,
        "download_type": "dryad",
        "download_url": "https://doi.org/10.5061/dryad.xwdbrv1tn",
        "license": "CC0 1.0",
        "citation": (
            "Poudel A, Gautam Adhikari P, Ghimire B, Thapa M. Diagnostic "
            "capability of ganglion cell complex thickness via spectral domain "
            "optical coherence tomography in glaucoma. Dryad. 2026. "
            "doi:10.5061/dryad.xwdbrv1tn"
        ),
        "tags": ["dryad", "glaucoma", "oct", "gcc", "nepal", "clinical"],
        "size_gb": 0.000013,
        "notes": (
            "Contains 406 eye-level rows from 203 participants (POAG, glaucoma "
            "suspect, and control). Both eyes can occur, so analyses must account "
            "for within-participant correlation."
        ),
        "source": {"doi": "10.5061/dryad.xwdbrv1tn"},
    },
    {
        "name": "dryad_glaucoma_rnfl_vf",
        "full_name": "RNFL and Visual-Field Glaucoma Diagnosis Dataset",
        "description": (
            "Clinical records combining retinal nerve fiber layer, visual-field, "
            "corneal-thickness, and intraocular-pressure features."
        ),
        "modality": "tabular",
        "tasks": ["classification"],
        "num_samples": 499,
        "download_type": "dryad",
        "download_url": "https://doi.org/10.5061/dryad.q6ft5",
        "license": "CC0 1.0",
        "citation": (
            "Development of machine learning models for diagnosis of glaucoma. "
            "Dryad. 2018. doi:10.5061/dryad.q6ft5"
        ),
        "tags": ["dryad", "glaucoma", "rnfl", "visual_field", "clinical"],
        "size_gb": 0.000032,
        "notes": (
            "The source reports 399 training/validation cases and 100 held-out "
            "test cases. The archive contains examination-record features rather "
            "than raw OCT or visual-field images."
        ),
        "source": {"doi": "10.5061/dryad.q6ft5"},
    },
    {
        "name": "dryad_namd_oct_quant",
        "full_name": "Moorfields nAMD Quantitative OCT Biomarker Dataset",
        "description": (
            "Anonymized clinical metadata and automated 3D OCT segmentation "
            "volumes for neovascular age-related macular degeneration."
        ),
        "modality": "tabular",
        "tasks": ["regression", "prognosis", "fairness_analysis"],
        "num_samples": 2966,
        "download_type": "dryad",
        "download_url": "https://doi.org/10.5061/dryad.2rbnzs7m4",
        "license": "CC0 1.0",
        "citation": (
            "Moraes G, Fu DJ, Wilson M, et al. Quantitative analysis of optical "
            "coherence tomography for neovascular age-related macular "
            "degeneration using deep learning. Dryad. 2020. "
            "doi:10.5061/dryad.2rbnzs7m4"
        ),
        "tags": [
            "dryad",
            "amd",
            "oct",
            "biomarkers",
            "clinical",
            "moorfields",
            "derived",
        ],
        "size_gb": 0.0032,
        "notes": (
            "Contains derived OCT feature volumes and metadata for 2,473 first-"
            "treated and 493 second-treated eyes. Raw OCT scans are not part of "
            "this Dryad release."
        ),
        "source": {"doi": "10.5061/dryad.2rbnzs7m4"},
    },
    {
        "name": "dryad_namd_visual_prediction",
        "full_name": "Moorfields nAMD Visual-Change Prediction Dataset",
        "description": (
            "Longitudinal quantitative OCT biomarkers and treatment-response "
            "variables for predicting visual acuity in neovascular AMD."
        ),
        "modality": "tabular",
        "tasks": ["regression", "prognosis"],
        "num_samples": 926,
        "download_type": "dryad",
        "download_url": "https://doi.org/10.5061/dryad.573n5tb5d",
        "license": "CC0 1.0",
        "citation": (
            "Predicting incremental and future visual change in neovascular "
            "age-related macular degeneration using deep learning. Dryad. 2021. "
            "doi:10.5061/dryad.573n5tb5d"
        ),
        "tags": [
            "dryad",
            "amd",
            "oct",
            "visual_acuity",
            "anti_vegf",
            "longitudinal",
            "derived",
        ],
        "size_gb": 0.0016,
        "notes": (
            "Primary analyses used 926 treatment-naive first-treated eyes from "
            "a larger Moorfields cohort. This resource overlaps the Moorfields "
            "AMD source cohort but exposes a distinct longitudinal prediction task."
        ),
        "source": {"doi": "10.5061/dryad.573n5tb5d"},
    },
    {
        "name": "dryad_functional_oct_alzheimer",
        "full_name": "Functional OCT Retinal Response Dataset",
        "description": (
            "Repeated light/dark SD-OCT acquisitions and retinal reflectivity "
            "profiles from healthy, neuromyelitis-optica, and Alzheimer groups."
        ),
        "modality": "oct",
        "tasks": ["classification", "registration", "regression"],
        "num_samples": None,
        "download_type": "dryad",
        "download_url": "https://doi.org/10.5061/dryad.msbcc2ftc",
        "license": "CC0 1.0",
        "citation": (
            "Bissig D, Zhou C, Le V, Bernard J. A practical approach to "
            "functional optical coherence tomography shows abnormal retinal "
            "responses in Alzheimer's disease. Dryad. 2020. "
            "doi:10.5061/dryad.msbcc2ftc"
        ),
        "tags": [
            "dryad",
            "oct",
            "functional_oct",
            "alzheimer",
            "light_response",
            "raw_images",
        ],
        "size_gb": 2.058,
        "notes": (
            "The release contains repeated acquisitions across four experiments; "
            "source groups include eight young adults, three participants with "
            "aquaporin-4 antibodies, 14 early-onset Alzheimer patients, and 14 "
            "age-matched controls. Group overlap is not assumed in num_samples. "
            "Dryad declines whole-version archive assembly for this record; "
            "EyeDataHub therefore directs users to the official landing page. "
            "Authenticated per-file API transfer is available when a user "
            "configures DRYAD_TOKEN."
        ),
        "acquisition_support": "guided_instructions_only",
        "loader_live_tested": False,
        "loader_test_date": "2026-07-30",
        "loader_test_scope": "live_archive_request",
        "loader_test_result": "whole_archive_refused_per_file_api_requires_token",
        "failure_reason": (
            "Dryad returned HTTP 405 for the whole-version archive and requires "
            "a bearer token for per-file API transfer."
        ),
        "source": {"doi": "10.5061/dryad.msbcc2ftc"},
    },
    {
        "name": "dryad_retinal_vein_cannulation",
        "full_name": "Autonomous Retinal Vein Cannulation Data and Code",
        "description": (
            "Surgical-microscope and intraoperative-OCT data for autonomous "
            "robotic retinal-vein cannulation in ex vivo porcine eyes."
        ),
        "modality": "multimodal",
        "tasks": ["classification", "navigation", "surgical_workflow"],
        "num_samples": 26,
        "download_type": "dryad",
        "download_url": "https://doi.org/10.5061/dryad.3ffbg79zd",
        "license": "CC0 1.0",
        "citation": (
            "Zhang P, Gehlbach P, Taylor R, Iordachita I, Kobilarov M. Data and "
            "code from: Deep learning-based autonomous retinal vein cannulation "
            "in ex vivo porcine eyes. Dryad. 2025. "
            "doi:10.5061/dryad.3ffbg79zd"
        ),
        "tags": [
            "dryad",
            "surgical_robotics",
            "ioct",
            "porcine",
            "ex_vivo",
            "retinal_vein",
        ],
        "size_gb": 7.511,
        "notes": (
            "Experiments used 20 static and six motion-simulated ex vivo porcine "
            "eyes. The large release contains model-training data and code."
        ),
        "source": {"doi": "10.5061/dryad.3ffbg79zd"},
    },
    {
        "name": "dryad_subretinal_robot",
        "full_name": "Head-Mounted Robot Subretinal Injection Dataset",
        "description": (
            "OCT screen recordings, annotated frames, and pressure data from "
            "robot-assisted subretinal injections in ex vivo porcine eyes."
        ),
        "modality": "multimodal",
        "tasks": ["segmentation", "surgical_workflow", "regression"],
        "num_samples": None,
        "download_type": "dryad",
        "download_url": "https://doi.org/10.5061/dryad.w0vt4b91w",
        "license": "CC0 1.0",
        "citation": (
            "Data and code from: Head-mounted surgical robots are an enabling "
            "technology for subretinal injections. Dryad. 2025. "
            "doi:10.5061/dryad.w0vt4b91w"
        ),
        "tags": [
            "dryad",
            "surgical_robotics",
            "subretinal_injection",
            "oct",
            "porcine",
            "ex_vivo",
        ],
        "size_gb": 2.481,
        "notes": (
            "All images and videos are from ex vivo porcine eyes. The repository "
            "also includes MATLAB bleb masks and pressure-sensor measurements."
        ),
        "source": {"doi": "10.5061/dryad.w0vt4b91w"},
    },
    {
        "name": "dryad_cornea_oct_pentacam",
        "full_name": "Corneal OCT and Pentacam Tomography Dataset",
        "description": (
            "Right-eye corneal OCT and rotating Scheimpflug tomography data with "
            "MATLAB code for automatic corneal-layer segmentation."
        ),
        "modality": "multimodal",
        "tasks": ["segmentation", "measurement", "registration"],
        "num_samples": None,
        "download_type": "dryad",
        "download_url": "https://doi.org/10.5061/dryad.tht76hf0c",
        "license": "CC0 1.0",
        "citation": (
            "Ran Z. Dataset for RSOS-211108. Dryad. 2021. "
            "doi:10.5061/dryad.tht76hf0c"
        ),
        "tags": [
            "dryad",
            "cornea",
            "anterior_segment_oct",
            "pentacam",
            "scheimpflug",
        ],
        "size_gb": 0.392,
        "notes": (
            "The source describes right-eye OCT and OCULUS Pentacam tomography "
            "plus custom segmentation code but does not expose a reliable record "
            "count in the repository metadata. Dryad declines whole-version "
            "archive assembly for this record; EyeDataHub therefore directs "
            "users to the official landing page. Authenticated per-file API "
            "transfer is available when a user configures DRYAD_TOKEN."
        ),
        "acquisition_support": "guided_instructions_only",
        "loader_live_tested": False,
        "loader_test_date": "2026-07-30",
        "loader_test_scope": "live_archive_request",
        "loader_test_result": "whole_archive_refused_per_file_api_requires_token",
        "failure_reason": (
            "Dryad returned HTTP 405 for the whole-version archive and requires "
            "a bearer token for per-file API transfer."
        ),
        "source": {"doi": "10.5061/dryad.tht76hf0c"},
    },
    {
        "name": "dryad_aoslo_rpe",
        "full_name": "AOSLO RPE Cell Morphometry and Cone Mosaic Dataset",
        "description": (
            "Adaptive-optics scanning-light-ophthalmoscopy montages and regions "
            "of interest for RPE morphometry and cone-to-RPE analysis."
        ),
        "modality": "adaptive_optics",
        "tasks": ["segmentation", "measurement"],
        "num_samples": 10,
        "download_type": "dryad",
        "download_url": "https://doi.org/10.5061/dryad.b41j15h",
        "license": "CC0 1.0",
        "citation": (
            "Human retinal pigment epithelium: in vivo cell morphometry, "
            "multispectral autofluorescence, and relationship to cone mosaic. "
            "Dryad. 2019. doi:10.5061/dryad.b41j15h"
        ),
        "tags": [
            "dryad",
            "adaptive_optics",
            "aoslo",
            "rpe",
            "cone_mosaic",
            "autofluorescence",
        ],
        "size_gb": 0.084,
        "notes": (
            "Contains one-eye data from 10 normal participants for short-wave "
            "autofluorescence and photoreceptor reflectance; infrared "
            "autofluorescence is available for seven participants with overlap."
        ),
        "source": {"doi": "10.5061/dryad.b41j15h"},
    },
    {
        "name": "dryad_uveal_melanoma_coog2",
        "full_name": "COOG2.1 Uveal Melanoma Prognostic Dataset",
        "description": (
            "Multicenter uveal-melanoma gene-expression, PRAME, clinical, and "
            "metastasis-free-survival data for prognostic modeling."
        ),
        "modality": "omics",
        "tasks": ["classification", "survival_analysis", "prognosis"],
        "num_samples": 1577,
        "download_type": "dryad",
        "download_url": "https://doi.org/10.5061/dryad.n8pk0p340",
        "license": "CC0 1.0",
        "citation": (
            "15-gene expression profile and PRAME as an integrated prognostic "
            "test for uveal melanoma: First report of Collaborative Ocular "
            "Oncology Group Study No. 2 (COOG2.1). Dryad. 2025. "
            "doi:10.5061/dryad.n8pk0p340"
        ),
        "tags": [
            "dryad",
            "uveal_melanoma",
            "gene_expression",
            "prame",
            "survival",
            "multicenter",
        ],
        "size_gb": 0.000084,
        "notes": (
            "Contains 1,577 subjects enrolled across 26 centers with a 15-gene "
            "expression profile, PRAME status, clinical variables, and follow-up."
        ),
        "source": {"doi": "10.5061/dryad.n8pk0p340"},
    },
]


REFRESH_DATASETS = [PlatformDiscoveryDataset(record) for record in REFRESH_RECORDS]
