"""Datasets recovered from the July 2026 fundus and OCT literature review.

The records in this module were checked against the registry by name, source
URL, DOI, cohort size, and annotation type. Derivative resources are included
only when they provide a distinct annotation or task. Records with unclear
terms retain an explicit ``Unknown`` license instead of inheriting the license
of a paper or a mirror.
"""
from __future__ import annotations

from typing import Any

from eyedatahub.datasets.platform_2026 import PlatformDiscoveryDataset


LITERATURE_RECORDS: list[dict[str, Any]] = [
    {
        "name": "agar300",
        "full_name": "AGAR300 Microaneurysm Fundus Image Dataset",
        "description": (
            "The first public AGAR300 release contains 28 color fundus images "
            "with microaneurysms, captured at a 45 degree field of view and "
            "2448 by 3264 pixel resolution."
        ),
        "modality": "fundus",
        "tasks": ["lesion_detection"],
        "num_samples": 28,
        "splits": ["all"],
        "classes": ["microaneurysm"],
        "num_classes": 1,
        "download_type": "manual",
        "download_url": (
            "https://ieee-dataport.org/open-access/"
            "diabetic-retinopathy-fundus-image-datasetagar300"
        ),
        "license": "CC BY 4.0",
        "citation": (
            "Derwin J, Shan P. Diabetic Retinopathy - Fundus Image Dataset "
            "(AGAR300). IEEE DataPort. 2020. doi:10.21227/fsnq-tn19"
        ),
        "tags": ["fundus", "diabetic_retinopathy", "microaneurysm", "ieee_dataport"],
        "notes": (
            "The source paper describes a larger 300 image clinical collection. "
            "The DOI record states that the public first release contains 28 "
            "images. All released images contain microaneurysms, and the release "
            "does not include spatial annotations. An IEEE DataPort account may "
            "be required to download it."
        ),
    },
    {
        "name": "drive",
        "full_name": "DRIVE: Digital Retinal Images for Vessel Extraction",
        "description": (
            "Forty color fundus photographs from a diabetic retinopathy "
            "screening program, divided into 20 training and 20 test images, "
            "with vessel reference annotations and field of view masks."
        ),
        "modality": "fundus",
        "tasks": ["segmentation"],
        "num_samples": 40,
        "splits": ["train", "test"],
        "classes": ["background", "vessel"],
        "num_classes": 2,
        "download_type": "manual",
        "download_url": "https://drive.grand-challenge.org/DRIVE/",
        "license": "Unknown; no named dataset license on the official page",
        "citation": (
            "Staal J, Abramoff MD, Niemeijer M, Viergever MA, van Ginneken B. "
            "Ridge-based vessel segmentation in color images of the retina. "
            "IEEE Trans Med Imaging. 2004;23:501-509. "
            "doi:10.1109/TMI.2004.825627"
        ),
        "tags": [
            "fundus",
            "vessels",
            "segmentation",
            "grand_challenge",
            "derived_annotation_available",
        ],
        "alternate_sources": [
            {
                "platform": "Dryad",
                "role": "derived_annotation",
                "url": "https://doi.org/10.5061/dryad.sf7m0cggh",
                "identifier": "10.5061/dryad.sf7m0cggh",
                "version": "9",
                "notes": (
                    "Vessel-tracing annotations and result tables derived from "
                    "DRIVE images; linked here rather than counted as another "
                    "independent dataset."
                ),
            }
        ],
        "notes": (
            "The official page reports 768 by 584 pixel images, one manual "
            "vessel segmentation for each training image, and hidden test "
            "references used by the evaluation server. A separate Dryad record "
            "provides a documented derived vessel-tracing annotation layer. "
            "Verify reuse terms with each source before redistribution."
        ),
    },
    {
        "name": "hei_med",
        "full_name": "HEI-MED: Hamilton Eye Institute Macular Edema Dataset",
        "description": (
            "A collection of 169 fundus photographs with expert exudate and "
            "bright lesion annotations, clinical metadata, optic nerve "
            "locations, vessel estimates, and image quality scores."
        ),
        "modality": "fundus",
        "tasks": ["segmentation", "classification", "quality"],
        "num_samples": 169,
        "splits": ["all"],
        "download_type": "github",
        "download_url": "https://github.com/lgiancaUTH/HEI-MED",
        "license": "Research only: non-commercial research use",
        "citation": (
            "Giancardo L, Meriaudeau F, Karnowski TP, et al. Exudate-based "
            "diabetic macular edema detection in fundus images using publicly "
            "available datasets. Med Image Anal. 2012;16:216-226. "
            "doi:10.1016/j.media.2011.07.004"
        ),
        "tags": ["fundus", "dme", "exudates", "segmentation", "github"],
        "size_gb": 0.32,
        "notes": (
            "The source README permits only non-commercial research use and "
            "requires citation. No SPDX license file is present."
        ),
        "source": {"repo": "lgiancaUTH/HEI-MED", "branch": "master"},
    },
    {
        "name": "dridb",
        "full_name": "DRiDB: Diabetic Retinopathy Image Database",
        "description": (
            "Fifty color fundus images with expert markings of diabetic "
            "retinopathy lesions, blood vessels, optic disc, and macula."
        ),
        "modality": "fundus",
        "tasks": ["segmentation", "lesion_detection", "classification"],
        "num_samples": 50,
        "splits": ["all"],
        "download_type": "manual",
        "download_url": "https://ipg.fer.hr/ipg/resources/image_database",
        "license": (
            "Research only: free for research and educational purposes; "
            "copying, redistribution, and unauthorized commercial use prohibited"
        ),
        "citation": (
            "Prentasic P, Loncaric S, Vatavuk Z, et al. Diabetic retinopathy "
            "image database (DRiDB): A new database for diabetic retinopathy "
            "screening programs research. ISPA. 2013:704-709. "
            "doi:10.1109/ISPA.2013.6703830"
        ),
        "tags": ["fundus", "diabetic_retinopathy", "lesions", "segmentation"],
        "notes": (
            "Access is requested by email from the official University of "
            "Zagreb page. The page requires citation of the listed paper when "
            "results use the dataset."
        ),
    },
    {
        "name": "eyeq",
        "full_name": "EyeQ Retinal Image Quality Assessment Dataset",
        "description": (
            "Quality labels for 28,792 EyePACS fundus images, graded as good, "
            "usable, or reject and divided into the original EyePACS train and "
            "test partitions."
        ),
        "modality": "fundus",
        "tasks": ["quality", "grading"],
        "num_samples": 28792,
        "splits": ["train", "test"],
        "classes": ["good", "usable", "reject"],
        "num_classes": 3,
        "download_type": "github",
        "download_url": "https://github.com/HzFu/EyeQ",
        "license": (
            "Unknown for released quality labels; code is CC BY-NC-SA 4.0"
        ),
        "citation": (
            "Fu H, Wang B, Shen J, et al. Evaluation of retinal image quality "
            "assessment networks in different color-spaces. MICCAI. 2019. "
            "doi:10.1007/978-3-030-32239-7_6"
        ),
        "tags": ["fundus", "image_quality", "grading", "eyepacs", "derivative"],
        "notes": (
            "EyeQ is a distinct annotation layer over EyePACS. The repository "
            "license covers the code but does not clearly license the quality "
            "labels. It does not provide the source images. Users must obtain "
            "EyePACS separately and comply with its terms."
        ),
        "source": {"repo": "HzFu/EyeQ", "branch": "master"},
    },
    {
        "name": "real_fundus",
        "full_name": "Real Fundus Clinical Image Restoration Benchmark",
        "description": (
            "One hundred twenty paired low quality and high quality clinical "
            "fundus photographs of the same eyes at 2560 by 2560 pixels for "
            "image restoration and enhancement research."
        ),
        "modality": "fundus",
        "tasks": ["restoration"],
        "num_samples": 120,
        "splits": ["all"],
        "download_type": "manual",
        "download_url": (
            "https://github.com/dengzhuo-AI/Real-Fundus/releases/tag/v.1.0.0"
        ),
        "license": "Unknown; no dataset license declared in the repository",
        "citation": (
            "Deng Z, Cai Y, Chen L, et al. RFormer: Transformer-based "
            "generative adversarial network for real fundus image restoration "
            "on a new clinical benchmark. IEEE J Biomed Health Inform. "
            "2022;26:4645-4655. doi:10.1109/JBHI.2022.3187103"
        ),
        "tags": ["fundus", "restoration", "image_quality", "paired_images"],
        "size_gb": 1.02,
        "notes": (
            "The public GitHub release contains the image archive. The paper "
            "describes a random 81/9/30 experimental split, but the release does "
            "not define distributed train, validation, and test partitions. No "
            "license file or dataset use terms were found."
        ),
    },
    {
        "name": "fiqs",
        "full_name": "FIQS: Fundus Image Quality Scores Dataset",
        "description": (
            "A set of 2,246 fundus images with continuous mean opinion scores "
            "from 0 to 100, three quality grades, and the individual scores of "
            "six ophthalmologists."
        ),
        "modality": "fundus",
        "tasks": ["quality", "grading", "regression"],
        "num_samples": 2246,
        "splits": ["all"],
        "classes": ["good", "usable", "reject"],
        "num_classes": 3,
        "download_type": "figshare",
        "download_url": "https://doi.org/10.6084/m9.figshare.28129847.v1",
        "license": "CC BY 4.0",
        "citation": (
            "Gong Z. FIQS Dataset (Fundus Image Quality Scores). Figshare. "
            "2025. doi:10.6084/m9.figshare.28129847.v1"
        ),
        "tags": ["fundus", "image_quality", "grading", "regression", "figshare"],
        "size_gb": 9.07,
        "notes": (
            "The deposit provides original resolution images, standardized "
            "1024 by 1024 versions, aggregate scores, and individual grader "
            "scores."
        ),
        "source": {"id": "28129847"},
    },
    {
        "name": "octa_macula_coronal",
        "full_name": "OCTA Macula Coronal Views",
        "description": (
            "A derived OCT angiography resource with 640 coronal PNG views for "
            "each of 129 subjects: 90 normal, 29 diabetic retinopathy, 5 AMD, "
            "and 5 choroidal neovascularization cases."
        ),
        "modality": "octa",
        "tasks": ["classification", "visualization"],
        "num_samples": 82560,
        "splits": ["all"],
        "classes": ["normal", "diabetic_retinopathy", "amd", "cnv"],
        "num_classes": 4,
        "download_type": "mendeley",
        "download_url": "https://data.mendeley.com/datasets/p5h7x55zw7/1",
        "license": "CC BY 4.0",
        "citation": (
            "Al-Hinnawi AR. OCTA Macula Coronal Views. Mendeley Data. 2023. "
            "doi:10.17632/p5h7x55zw7.1"
        ),
        "tags": ["octa", "macula", "coronal_views", "derived", "mendeley"],
        "notes": (
            "The sample count is the number of derived PNG views. They come "
            "from 129 subject-level OCTA scans, so analysis and splitting "
            "should remain grouped by subject."
        ),
        "source": {"id": "p5h7x55zw7", "version": 1},
    },
    {
        "name": "fang_sbsdi_oct",
        "full_name": "Duke Fang SBSDI Retinal OCT Dataset",
        "description": (
            "Human and human-derived paired retinal OCT images used to study "
            "sparse acquisition, denoising, interpolation, and reconstruction "
            "in healthy and non-neovascular AMD eyes."
        ),
        "modality": "oct",
        "tasks": ["reconstruction", "denoising"],
        "num_samples": 323,
        "splits": ["all"],
        "download_type": "manual",
        "download_url": "https://people.duke.edu/~sf59/Fang_TMI_2013.htm",
        "license": "Research only: academic research use",
        "citation": (
            "Fang L, Li S, McNabb RP, et al. Fast acquisition and "
            "reconstruction of optical coherence tomography images via sparse "
            "representation. IEEE Trans Med Imaging. 2013;32:2034-2049. "
            "doi:10.1109/TMI.2013.2271904"
        ),
        "tags": [
            "oct",
            "amd",
            "reconstruction",
            "denoising",
            "human",
            "human_derived_synthetic",
            "duke",
        ],
        "notes": (
            "The catalog scope is limited to the source archive's separately "
            "named human and human-derived components: 195 real-human TIFFs, "
            "108 human-derived synthetic TIFFs, and 20 human-derived "
            "dictionary-training TIFFs. Other source-archive components are "
            "outside this record's scope. The associated paper describes 28 "
            "eyes from 28 participants for the synthetic experiments and 13 "
            "participants for the real experiments."
        ),
        "size_gb": 0.45,
    },
    {
        "name": "duke_amd_chiu",
        "full_name": "Duke AMD Pathology OCT Segmentation Dataset",
        "description": (
            "Twenty OCT volumes with 220 selected B-scans from eyes with "
            "non-neovascular AMD, drusen, and geographic atrophy, including "
            "manual and automated pathology markings."
        ),
        "modality": "oct",
        "tasks": ["segmentation", "measurement"],
        "num_samples": 20,
        "splits": ["all"],
        "download_type": "manual",
        "download_url": "https://people.duke.edu/~sf59/Chiu_IOVS_2011_dataset.htm",
        "license": "Unknown; no named dataset license on the official page",
        "citation": (
            "Chiu SJ, Izatt JA, O'Connell RV, Winter KP, Toth CA, Farsiu S. "
            "Validated automatic segmentation of AMD pathology including "
            "drusen and geographic atrophy in SD-OCT images. Invest Ophthalmol "
            "Vis Sci. 2012;53:53-61. doi:10.1167/iovs.11-7640"
        ),
        "tags": ["oct", "amd", "drusen", "geographic_atrophy", "segmentation", "duke"],
        "size_gb": 0.54,
        "notes": (
            "The sample count is the 20-eye main validation cohort. The archive "
            "also contains ten reproducibility volumes acquired at 0 and 90 "
            "degrees and MATLAB display scripts. The source page does not state "
            "a named reuse license."
        ),
    },
    {
        "name": "maetschke_glaucoma_oct",
        "full_name": "OCT Volumes for Glaucoma Detection",
        "description": (
            "A set of 1,110 optic nerve head OCT volumes from 624 patients, "
            "including 847 scans with primary open angle glaucoma and 263 "
            "healthy scans."
        ),
        "modality": "oct",
        "tasks": ["classification"],
        "num_samples": 1110,
        "splits": ["train", "val", "test"],
        "classes": ["healthy", "primary_open_angle_glaucoma"],
        "num_classes": 2,
        "download_type": "zenodo",
        "download_url": "https://doi.org/10.5281/zenodo.1481223",
        "license": "CC BY-NC 4.0",
        "citation": (
            "Maetschke S, Antony B, Ishikawa H, Wollstein G, Schuman J, "
            "Garnavi R. A feature agnostic approach for glaucoma detection in "
            "OCT volumes. PLoS One. 2019;14:e0219126. "
            "doi:10.1371/journal.pone.0219126. "
            "Data: doi:10.5281/zenodo.1481223"
        ),
        "tags": ["oct", "glaucoma", "classification", "zenodo"],
        "size_gb": 0.43,
        "notes": (
            "The paper reports patient-grouped splits of 888 training, 112 "
            "validation, and 110 test scans. Volumes are stored as NumPy arrays."
        ),
        "source": {"record": "1481223"},
    },
    {
        "name": "ochid",
        "full_name": "OCHID: OCT Choroidal Image Dataset",
        "description": (
            "A collection of 640 retinal OCT images with expert choroidal "
            "region annotations for choroid segmentation."
        ),
        "modality": "oct",
        "tasks": ["segmentation"],
        "num_samples": 640,
        "splits": ["all"],
        "classes": ["background", "choroid"],
        "num_classes": 2,
        "download_type": "manual",
        "download_url": "https://imed.nimte.ac.cn/OCHID.html",
        "license": "Research only: academic research use by request",
        "citation": (
            "Yan Q, Gu Y, Zhao J, et al. Automatic choroid layer segmentation "
            "in OCT images via context efficient adaptive network. Appl Intell. "
            "2023;53:5554-5566. doi:10.1007/s10489-022-03723-w"
        ),
        "tags": ["oct", "choroid", "segmentation", "manual_access"],
        "notes": (
            "The official project page asks academic users to request the "
            "dataset by email. It does not provide a standard license."
        ),
    },
    {
        "name": "thoct1800",
        "full_name": "THOCT1800 Retinal OCT Dataset",
        "description": (
            "A collection of 1,800 preprocessed retinal OCT B-scans, with 600 "
            "images each for AMD, diabetic macular edema, and normal retina."
        ),
        "modality": "oct",
        "tasks": ["classification"],
        "num_samples": 1800,
        "splits": ["all"],
        "classes": ["amd", "dme", "normal"],
        "num_classes": 3,
        "download_type": "github",
        "download_url": "https://github.com/SJD095/OCT-Segmentation",
        "license": "Research only: research and educational use",
        "citation": (
            "THOCT1800 retinal OCT image dataset. OCT-Segmentation project. "
            "GitHub."
        ),
        "tags": ["oct", "amd", "dme", "classification", "github"],
        "notes": (
            "The official repository permits research and educational use and "
            "asks users to cite the project. No standard license file is present."
        ),
        "source": {"repo": "SJD095/OCT-Segmentation", "branch": "master"},
    },
    {
        "name": "vietai_retinal_disease",
        "full_name": "VietAI Retinal Disease Detection 2020",
        "description": (
            "A multilabel fundus classification challenge with 3,435 labeled "
            "training images and 350 test images covering six disease groups "
            "and normal findings."
        ),
        "modality": "fundus",
        "tasks": ["multilabel", "classification"],
        "num_samples": 3785,
        "splits": ["train", "test"],
        "classes": [
            "opacity",
            "diabetic_retinopathy",
            "glaucoma",
            "macular_edema",
            "macular_degeneration",
            "retinal_vein_occlusion",
            "normal",
        ],
        "num_classes": 7,
        "download_type": "kaggle",
        "download_url": (
            "https://www.kaggle.com/competitions/"
            "vietai-advance-retinal-disease-detection-2020/data"
        ),
        "license": "Kaggle competition rules",
        "citation": "VietAI Advance Course Retinal Disease Detection. Kaggle. 2020.",
        "tags": ["fundus", "multilabel", "retinal_disease", "kaggle"],
        "notes": (
            "Kaggle authentication and acceptance of the competition rules may "
            "be required. Derivative archives that mix these images with "
            "unverified sources were excluded from the registry."
        ),
        "source": {
            "dataset": "vietai-advance-retinal-disease-detection-2020",
            "is_competition": True,
        },
    },
]


LITERATURE_DATASETS = [
    PlatformDiscoveryDataset(record) for record in LITERATURE_RECORDS
]
