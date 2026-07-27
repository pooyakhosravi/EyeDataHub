"""Major gaze, pupil, and iris benchmarks verified through July 14, 2026.

This bounded refresh closes two conspicuous taxonomy gaps in the registry.  It
uses institutional project pages or primary dataset papers as the source of
record and keeps access manual where registration, a request, an agreement, or
an FTP client is required.  A public landing page is not treated as evidence of
an open license; unclear terms remain explicitly ``Unknown``.
"""
from __future__ import annotations

from typing import Any

from eyedatahub.datasets.platform_2026 import PlatformDiscoveryDataset


GAZE_IRIS_RECORDS: list[dict[str, Any]] = [
    {
        "name": "gaze_capture",
        "full_name": "GazeCapture Mobile Eye-Tracking Dataset",
        "description": (
            "Crowdsourced iPhone and iPad face videos with screen-fixation "
            "coordinates for appearance-based mobile gaze estimation."
        ),
        "modality": "eye_tracking",
        "tasks": ["gaze_estimation", "regression"],
        "num_samples": 2_445_504,
        "download_type": "manual",
        "download_url": "https://gazecapture.csail.mit.edu/dataset.php",
        "license": "Unknown; registration required and source terms must be checked",
        "citation": (
            "Krafka K, Khosla A, Kellnhofer P, et al. Eye Tracking for "
            "Everyone. CVPR. 2016:2176-2184. arXiv:1606.05814"
        ),
        "tags": [
            "eye_tracking",
            "gaze",
            "mobile",
            "iphone",
            "ipad",
            "face_video",
            "registration",
        ],
        "size_gb": None,
        "notes": (
            "The primary paper reports 2,445,504 frames with fixation locations "
            "from 1,474 participants. The official site requires account "
            "registration; verify the current agreement before reuse."
        ),
    },
    {
        "name": "gaze360",
        "full_name": "Gaze360 Physically Unconstrained Gaze Dataset",
        "description": (
            "Indoor and outdoor panoramic-camera recordings with continuous "
            "three-dimensional gaze labels across wide head poses and distances."
        ),
        "modality": "eye_tracking",
        "tasks": ["gaze_estimation", "regression"],
        "num_samples": 172_000,
        "download_type": "manual",
        "download_url": "https://gaze360.csail.mit.edu/",
        "license": "Unknown; registration required and source terms must be checked",
        "citation": (
            "Kellnhofer P, Recasens A, Stent S, Matusik W, Torralba A. "
            "Gaze360: Physically Unconstrained Gaze Estimation in the Wild. "
            "ICCV. 2019:6912-6921. arXiv:1910.10088"
        ),
        "tags": [
            "eye_tracking",
            "gaze",
            "3d_gaze",
            "video",
            "indoor",
            "outdoor",
            "registration",
        ],
        "size_gb": None,
        "notes": (
            "The project reports 238 participants; the benchmark is commonly "
            "reported as 172,000 labeled frames. Access uses registration, and "
            "the public landing page does not state a standard reuse license."
        ),
    },
    {
        "name": "eth_xgaze",
        "full_name": "ETH-XGaze Extreme-Pose Gaze Estimation Dataset",
        "description": (
            "High-resolution multi-camera face images with calibrated gaze "
            "targets, extreme head poses, and varied illumination."
        ),
        "modality": "eye_tracking",
        "tasks": ["gaze_estimation", "regression"],
        "num_samples": 1_083_492,
        "download_type": "manual",
        "download_url": "https://ait.ethz.ch/xgaze",
        "license": "CC BY-NC-SA 4.0 with additional dataset conditions",
        "citation": (
            "Zhang X, Park S, Beeler T, Bradley D, Tang S, Hilliges O. "
            "ETH-XGaze: A Large Scale Dataset for Gaze Estimation under "
            "Extreme Head Pose and Gaze Variation. ECCV. 2020."
        ),
        "tags": [
            "eye_tracking",
            "gaze",
            "3d_gaze",
            "multi_camera",
            "head_pose",
            "controlled_access",
        ],
        "size_gb": 130.0,
        "notes": (
            "Contains 1,083,492 images from 110 participants. The official page "
            "offers approximately 130 GB 224-pixel face patches, 497 GB "
            "448-pixel patches, or about 7 TB of raw images on request. The "
            "linked completed license adds conditions to CC BY-NC-SA 4.0."
        ),
    },
    {
        "name": "mpii_gaze",
        "full_name": "MPIIGaze Appearance-Based Gaze Estimation Dataset",
        "description": (
            "Longitudinal laptop-camera images captured during natural daily "
            "use with gaze targets, face geometry, and normalized views."
        ),
        "modality": "eye_tracking",
        "tasks": ["gaze_estimation", "regression"],
        "num_samples": 213_659,
        "download_type": "manual",
        "download_url": (
            "https://www.mpi-inf.mpg.de/de/departments/computer-vision-and-"
            "machine-learning/research/gaze-based-human-computer-interaction/"
            "appearance-based-gaze-estimation-in-the-wild"
        ),
        "license": "CC BY-NC-SA 4.0; non-commercial scientific use only",
        "citation": (
            "Zhang X, Sugano Y, Fritz M, Bulling A. Appearance-Based Gaze "
            "Estimation in the Wild. CVPR. 2015:4511-4520."
        ),
        "tags": [
            "eye_tracking",
            "gaze",
            "laptop",
            "longitudinal",
            "in_the_wild",
            "non_commercial",
        ],
        "size_gb": 2.1,
        "notes": (
            "The institutional page reports 213,659 images from 15 participants "
            "collected over more than three months and provides a 2.1 GB "
            "download for non-commercial scientific use."
        ),
    },
    {
        "name": "lpw",
        "full_name": "LPW Labelled Pupils in the Wild",
        "description": (
            "High-speed head-mounted eye-region videos with pupil-center "
            "annotations under varied indoor, outdoor, eyewear, and lighting conditions."
        ),
        "modality": "eye_tracking",
        "tasks": ["pupil_detection", "landmark_detection"],
        "num_samples": 130_856,
        "download_type": "manual",
        "download_url": (
            "https://www.mpi-inf.mpg.de/de/departments/computer-vision-and-"
            "machine-learning/research/gaze-based-human-computer-interaction/"
            "labelled-pupils-in-the-wild-lpw/"
        ),
        "license": "Non-commercial research use only",
        "citation": (
            "Tonsen M, Zhang X, Sugano Y, Bulling A. Labelled Pupils in the "
            "Wild: A Dataset for Studying Pupil Detection in Unconstrained "
            "Environments. ETRA. 2016:139-142. doi:10.1145/2857491.2857520"
        ),
        "tags": [
            "eye_tracking",
            "pupil",
            "head_mounted",
            "video",
            "indoor",
            "outdoor",
            "non_commercial",
        ],
        "size_gb": 2.4,
        "notes": (
            "The institutional page reports 66 videos and 130,856 images from "
            "22 participants. It explicitly limits use to non-commercial "
            "scientific purposes."
        ),
    },
    {
        "name": "teyed",
        "full_name": "TEyeD Real-World Eye-Tracking Dataset",
        "description": (
            "Head-mounted eye images with pupil, iris, eyelid, eyeball, gaze, "
            "landmark, segmentation, and eye-movement annotations."
        ),
        "modality": "eye_tracking",
        "tasks": [
            "gaze_estimation",
            "segmentation",
            "landmark_detection",
            "classification",
        ],
        "num_samples": 20_666_096,
        "download_type": "manual",
        "download_url": "https://arxiv.org/abs/2102.02115",
        "license": "Unknown; public FTP is described in the paper but no license is stated",
        "citation": (
            "Fuhl W, Kasneci G, Kasneci E. TEyeD: Over 20 Million Real-World "
            "Eye Images with Rich 2D and 3D Annotations. arXiv:2102.02115. 2021."
        ),
        "tags": [
            "eye_tracking",
            "gaze",
            "pupil",
            "iris",
            "eyelid",
            "head_mounted",
            "vr",
            "ar",
            "ftp",
        ],
        "size_gb": None,
        "notes": (
            "The paper reports 20,666,096 open- or closed-eye frames and also "
            "200,977 no-eye frames, collected with seven trackers. It documents "
            "anonymous FTP access at nephrit.cs.uni-tuebingen.de using user "
            "TEyeDUser, but does not state a standard dataset license; confirm "
            "availability and terms before use."
        ),
    },
    {
        "name": "casia_iris_v4",
        "full_name": "CASIA-IrisV4 Iris Image Database",
        "description": (
            "Six near-infrared or synthetic iris subsets spanning close-range, "
            "lamp variation, twins, distance, large-scale, and synthetic recognition."
        ),
        "modality": "iris_biometrics",
        "tasks": ["biometric_recognition", "classification"],
        "num_samples": 54_601,
        "download_type": "manual",
        "download_url": "https://hycasia.github.io/dataset/casia-irisv4/",
        "license": "Public domain; source access terms apply",
        "citation": (
            "Chinese Academy of Sciences Institute of Automation. CASIA Iris "
            "Image Database Version 4.0. Dataset documentation."
        ),
        "tags": [
            "iris",
            "biometrics",
            "near_infrared",
            "synthetic",
            "twins",
            "public_domain",
        ],
        "size_gb": 1.86,
        "notes": (
            "The project documentation mirror reports 54,601 images from "
            "more than 1,800 genuine and 1,000 virtual subjects, with possible "
            "subject overlap across four subsets, and describes the release as "
            "public domain. The linked download service may require login."
        ),
    },
    {
        "name": "ubiris_v2",
        "full_name": "UBIRIS.v2 Noisy Visible-Wavelength Iris Database",
        "description": (
            "Visible-light iris images captured at a distance and on the move "
            "with realistic blur, reflection, occlusion, pose, and illumination noise."
        ),
        "modality": "iris_biometrics",
        "tasks": ["biometric_recognition", "classification"],
        "num_samples": 11_102,
        "download_type": "manual",
        "download_url": "https://iris.di.ubi.pt/index.html",
        "license": "Unknown; request access and verify UBIRIS.v2-specific terms",
        "citation": (
            "Proenca H, Filipe S, Santos R, Oliveira J, Alexandre LA. The "
            "UBIRIS.v2: A Database of Visible Wavelength Iris Images Captured "
            "On-the-Move and At-a-Distance. IEEE TPAMI. 2010;32:1529-1535."
        ),
        "tags": [
            "iris",
            "biometrics",
            "visible_light",
            "at_distance",
            "on_the_move",
            "noisy",
            "request_access",
        ],
        "size_gb": None,
        "notes": (
            "The official readme reports 11,102 images from 261 participants "
            "and 522 irises. The site states that UBIRIS.v1 is public and that "
            "newer UBIPr derivatives use CC BY-NC-SA 4.0, but it does not make "
            "the same license statement for UBIRIS.v2; terms are therefore unknown."
        ),
    },
    {
        "name": "nd_iris_0405",
        "full_name": "ND-IRIS-0405 Iris Image Dataset",
        "description": (
            "Longitudinal near-infrared iris images with subject, eye, age, sex, "
            "and ethnicity metadata used in ICE iris-recognition evaluations."
        ),
        "modality": "iris_biometrics",
        "tasks": ["biometric_recognition", "classification", "demographic_analysis"],
        "num_samples": 64_980,
        "download_type": "manual",
        "download_url": "https://tsapps.nist.gov/BDbC/Search/Details/371",
        "license": "Research use under a signed institutional data license agreement",
        "citation": (
            "Bowyer KW, Flynn PJ. The ND-IRIS-0405 Iris Image Dataset. "
            "arXiv:1606.04853. 2016."
        ),
        "tags": [
            "iris",
            "biometrics",
            "near_infrared",
            "longitudinal",
            "demographics",
            "license_agreement",
        ],
        "size_gb": None,
        "notes": (
            "The current NIST catalog record reports 64,980 images from 356 "
            "participants and 712 irises. Access requires an institutional "
            "license signed by an authorized representative; approval and "
            "download instructions are issued by Notre Dame."
        ),
    },
]


GAZE_IRIS_DATASETS = [
    PlatformDiscoveryDataset(record) for record in GAZE_IRIS_RECORDS
]
