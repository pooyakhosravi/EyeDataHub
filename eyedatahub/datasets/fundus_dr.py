"""Diabetic Retinopathy grading datasets: APTOS2019, MESSIDOR-2, IDRiD, DDR, EyePACS, BiDR, DRArranged, MMRDR."""
from __future__ import annotations

from pathlib import Path
from typing import List, Union

import pandas as pd

from eyedatahub.core.dataset import DatasetInfo, DatasetSample, EyeDataHubDataset
from eyedatahub.datasets.download_utils import (
    download_figshare,
    download_gdrive_folder,
    download_kaggle,
    extract_archive,
    print_manual_download_instructions,
)


# ---------------------------------------------------------------------------
# APTOS 2019 (Kaggle)
# ---------------------------------------------------------------------------

class APTOS2019Dataset(EyeDataHubDataset):
    """
    APTOS 2019 Blindness Detection (Kaggle competition).

    3662 training fundus images graded 0-4 for DR severity.
    """

    _SUBDIR = "aptos2019"
    _KAGGLE_SLUG = "aptos2019-blindness-detection"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="aptos2019",
            full_name="APTOS 2019 Blindness Detection",
            description=(
                "3662 fundus images from Aravind Eye Hospital, graded 0-4 for "
                "diabetic retinopathy severity."
            ),
            modality="fundus",
            tasks=["grading", "classification"],
            num_samples=3662,
            splits=["train"],
            classes=["No DR", "Mild", "Moderate", "Severe", "Proliferative DR"],
            num_classes=5,
            download_type="kaggle",
            download_url=f"https://www.kaggle.com/c/{self._KAGGLE_SLUG}",
            license="Competition rules apply",
            citation=(
                "Karthik et al., APTOS 2019 Blindness Detection. "
                "Kaggle competition, 2019."
            ),
            tags=["diabetic_retinopathy", "grading", "fundus", "kaggle"],
            size_gb=9.0,
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return (root / "train_images").exists() and (root / "train.csv").exists()

    def download(self, data_dir: Union[str, Path]) -> None:
        dest = Path(data_dir) / self._SUBDIR
        download_kaggle(self._KAGGLE_SLUG, dest, is_competition=True)

    def load(
        self, data_dir: Union[str, Path], split: str = "train"
    ) -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR

        csv_path = root / f"{split}.csv"
        if not csv_path.exists():
            # fallback: try the only csv available
            csvs = list(root.glob("*.csv"))
            if not csvs:
                raise FileNotFoundError(
                    f"No CSV found in {root}. Download APTOS2019 first."
                )
            csv_path = csvs[0]

        df = pd.read_csv(csv_path)
        images_dir = root / f"{split}_images"
        if not images_dir.exists():
            images_dir = root / "train_images"  # use train images as fallback

        samples = []
        for _, row in df.iterrows():
            img_id = str(row["id_code"])
            label = int(row["diagnosis"])
            img_path = images_dir / f"{img_id}.png"
            if not img_path.exists():
                img_path = images_dir / f"{img_id}.jpg"
            if img_path.exists():
                samples.append(
                    DatasetSample(
                        image_path=str(img_path),
                        label=label,
                        sample_id=img_id,
                        metadata={"split": split},
                    )
                )
        return samples


# ---------------------------------------------------------------------------
# MESSIDOR-2
# ---------------------------------------------------------------------------

class MESSIDOR2Dataset(EyeDataHubDataset):
    """
    MESSIDOR-2: Messidor Project dataset for DR grading.

    1748 fundus images graded for DR (0-3) and macular edema (0-2).
    Requires registration at ADCIS website.
    """

    _SUBDIR = "messidor2"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="messidor2",
            full_name="MESSIDOR-2",
            description=(
                "1748 fundus images with DR grading (0-3 Retinopathy Grade) "
                "and macular edema risk (0-2)."
            ),
            modality="fundus",
            tasks=["grading", "classification"],
            num_samples=1748,
            splits=["all"],
            classes=["Grade 0", "Grade 1", "Grade 2", "Grade 3"],
            num_classes=4,
            download_type="manual",
            download_url="https://www.adcis.net/en/third-party/messidor2/",
            license="Research only — requires registration",
            citation=(
                "Decencière et al., 'Feedback on a publicly distributed image "
                "database: the Messidor database', Image Analysis & Stereology 2014."
            ),
            tags=["diabetic_retinopathy", "grading", "fundus"],
            size_gb=3.0,
            notes="Free registration required at adcis.net before downloading.",
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return len(list(root.glob("**/*.tif"))) > 100

    def download(self, data_dir: Union[str, Path]) -> None:
        root = Path(data_dir) / self._SUBDIR
        print_manual_download_instructions(
            "MESSIDOR-2",
            "https://www.adcis.net/en/third-party/messidor2/",
            root,
            extra_notes=(
                "Register and download the MESSIDOR-2 archive.\n"
                "Extract so that TIFF images are at:\n"
                "  messidor2/<subset>/image.tif\n"
                "and the grading file messidor_data.csv is at:\n"
                "  messidor2/messidor_data.csv"
            ),
        )
        raise RuntimeError("MESSIDOR-2 requires manual download.")

    def load(
        self, data_dir: Union[str, Path], split: str = "all"
    ) -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR

        # Try to find the grading CSV (messidor_data.csv or annotations.csv)
        csv_candidates = list(root.glob("*.csv"))
        if not csv_candidates:
            raise FileNotFoundError(
                f"No CSV annotation file found in {root}. "
                "Place messidor_data.csv there."
            )

        df = pd.read_csv(csv_candidates[0])

        # Detect column names (varies by release)
        img_col = next(
            (c for c in df.columns if "image" in c.lower() or "file" in c.lower()),
            df.columns[0],
        )
        label_col = next(
            (c for c in df.columns if "retinopathy" in c.lower() or "grade" in c.lower() or "adjudicated" in c.lower()),
            df.columns[-1],
        )

        samples = []
        for _, row in df.iterrows():
            fname = str(row[img_col])
            label = int(row[label_col])
            img_candidates = list(root.rglob(fname)) + list(root.rglob(fname.replace(".tif", ".jpg")))
            if img_candidates:
                samples.append(
                    DatasetSample(
                        image_path=str(img_candidates[0]),
                        label=label,
                        sample_id=fname,
                        metadata={"split": split},
                    )
                )
        return samples


# ---------------------------------------------------------------------------
# IDRiD
# ---------------------------------------------------------------------------

class IDRiDDataset(EyeDataHubDataset):
    """
    IDRiD: Indian Diabetic Retinopathy Image Dataset.

    516 fundus images with DR grading, macular edema grading, and pixel-level
    lesion segmentation masks.
    """

    _SUBDIR = "idrid"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="idrid",
            full_name="IDRiD: Indian Diabetic Retinopathy Image Dataset",
            description=(
                "516 fundus images with DR grade (0-4), macular edema grade (0-2), "
                "and pixel-level lesion segmentation for 81 images."
            ),
            modality="fundus",
            tasks=["grading", "classification", "segmentation"],
            num_samples=516,
            splits=["train", "test"],
            classes=["Grade 0", "Grade 1", "Grade 2", "Grade 3", "Grade 4"],
            num_classes=5,
            download_type="manual",
            download_url="https://ieee-dataport.org/open-access/indian-diabetic-retinopathy-image-dataset-idrid",
            license="CC BY 4.0",
            citation=(
                "Porwal et al., 'Indian diabetic retinopathy image dataset (IDRiD): "
                "A database for diabetic retinopathy screening research', Data 2018."
            ),
            tags=["diabetic_retinopathy", "grading", "segmentation", "fundus"],
            size_gb=2.5,
            notes="Requires IEEE DataPort account (free).",
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return (root / "B. Disease Grading").exists() or (
            root / "disease_grading"
        ).exists()

    def download(self, data_dir: Union[str, Path]) -> None:
        root = Path(data_dir) / self._SUBDIR
        print_manual_download_instructions(
            "IDRiD",
            "https://ieee-dataport.org/open-access/indian-diabetic-retinopathy-image-dataset-idrid",
            root,
            extra_notes=(
                "Download all three tasks:\n"
                "  Task 1: Lesion Segmentation\n"
                "  Task 2: Disease Grading\n"
                "  Task 3: Optic Disc/Cup Segmentation\n"
                "Extract so the structure matches:\n"
                "  idrid/B. Disease Grading/a. Training Set/*.jpg\n"
                "  idrid/B. Disease Grading/b. Testing Set/*.jpg\n"
                "  idrid/B. Disease Grading/a. Training Set/Groundtruths/*.csv"
            ),
        )
        raise RuntimeError("IDRiD requires manual download.")

    def load(
        self, data_dir: Union[str, Path], split: str = "train"
    ) -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR

        # Support both original and simplified directory names
        grade_dir = root / "B. Disease Grading"
        if not grade_dir.exists():
            grade_dir = root / "disease_grading"
        if not grade_dir.exists():
            raise FileNotFoundError(f"Disease grading folder not found in {root}.")

        split_map = {
            "train": "a. Training Set",
            "test": "b. Testing Set",
        }
        split_folder = grade_dir / split_map.get(split, split)

        # Locate ground truth CSV
        gt_dir = split_folder / "Groundtruths"
        if not gt_dir.exists():
            gt_dir = split_folder

        csv_candidates = list(gt_dir.glob("*.csv"))
        if not csv_candidates:
            # Fall back to CSV in parent
            csv_candidates = list(grade_dir.glob("*.csv"))

        if not csv_candidates:
            raise FileNotFoundError(
                f"No grading CSV found for split '{split}'. "
                "Place the IDRiD grading CSV inside the split directory."
            )

        df = pd.read_csv(csv_candidates[0])
        img_col = df.columns[0]
        dr_col = next(
            (c for c in df.columns if "retinopathy" in c.lower() or "grade" in c.lower()),
            df.columns[1],
        )

        img_dir = split_folder
        samples = []
        for _, row in df.iterrows():
            img_id = str(row[img_col])
            label = int(row[dr_col])
            img_path = img_dir / f"{img_id}.jpg"
            if img_path.exists():
                samples.append(
                    DatasetSample(
                        image_path=str(img_path),
                        label=label,
                        sample_id=img_id,
                        metadata={"split": split},
                    )
                )
        return samples


# ---------------------------------------------------------------------------
# DDR
# ---------------------------------------------------------------------------

class DDRDataset(EyeDataHubDataset):
    """
    DDR: Diabetic Retinopathy Detection & Grading Dataset.

    12,522 fundus images with DR grading and lesion-level annotations.
    """

    _SUBDIR = "ddr"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="ddr",
            full_name="DDR: Diabetic Retinopathy Detection & Grading",
            description=(
                "12522 fundus images with DR grading (0-5) and lesion-level "
                "segmentation annotations."
            ),
            modality="fundus",
            tasks=["grading", "classification"],
            num_samples=12522,
            splits=["train", "valid", "test"],
            classes=["No DR", "Mild", "Moderate", "Severe", "Proliferative", "Ungradable"],
            num_classes=6,
            download_type="gdrive",
            download_url="https://drive.google.com/drive/folders/1z6tSFmxW_aNayUqVxx6h6bY4kwGzUTEC",
            license="MIT",
            citation=(
                "Li et al., 'Diagnostic Assessment of Deep Learning Algorithms "
                "for Diabetic Retinopathy Screening', Information Sciences 2019. "
                "Data: https://github.com/nkicsl/DDR-dataset — "
                "GDrive: https://drive.google.com/drive/folders/1z6tSFmxW_aNayUqVxx6h6bY4kwGzUTEC"
            ),
            tags=["diabetic_retinopathy", "grading", "fundus"],
            size_gb=4.0,
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return len(list(root.glob("**/*.jpg"))) > 1000

    _GDRIVE_FOLDER_ID = "1z6tSFmxW_aNayUqVxx6h6bY4kwGzUTEC"

    def download(self, data_dir: Union[str, Path]) -> None:
        root = Path(data_dir) / self._SUBDIR
        root.mkdir(parents=True, exist_ok=True)
        download_gdrive_folder(self._GDRIVE_FOLDER_ID, root)

    def load(
        self, data_dir: Union[str, Path], split: str = "test"
    ) -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR
        grading_roots = [root]
        grading_roots.extend(
            candidate
            for candidate in root.rglob("DR_grading")
            if candidate.is_dir()
        )
        grading_root = next(
            (
                candidate
                for candidate in grading_roots
                if (candidate / split).is_dir()
            ),
            grading_roots[-1],
        )
        split_dir = grading_root / split
        img_dir = (
            split_dir / "image"
            if (split_dir / "image").is_dir()
            else split_dir
        )
        lbl_dir = split_dir / "label"

        if not img_dir.exists():
            raise FileNotFoundError(
                f"DDR {split} image directory not found below {grading_root}"
            )

        # Build label mapping from text files
        label_map: dict = {}
        split_label_file = grading_root / f"{split}.txt"
        if split_label_file.is_file():
            with split_label_file.open(encoding="utf-8") as handle:
                for line in handle:
                    parts = line.strip().split()
                    if len(parts) >= 2:
                        label_map[parts[0]] = int(parts[1])
        if lbl_dir.exists():
            for txt in lbl_dir.glob("*.txt"):
                with txt.open(encoding="utf-8") as handle:
                    for line in handle:
                        parts = line.strip().split()
                        if len(parts) >= 2:
                            label_map[parts[0]] = int(parts[1])

        samples = []
        image_paths = (
            sorted(img_dir.glob("*.jpg"))
            + sorted(img_dir.glob("*.jpeg"))
            + sorted(img_dir.glob("*.png"))
        )
        for img_path in image_paths:
            label = label_map.get(img_path.name, label_map.get(img_path.stem, -1))
            if label == -1:
                continue
            samples.append(
                DatasetSample(
                    image_path=str(img_path),
                    label=label,
                    sample_id=img_path.stem,
                    metadata={"split": split},
                )
            )
        return samples


# ---------------------------------------------------------------------------
# MAPLES-DR
# ---------------------------------------------------------------------------

MAPLES_DR_BIOMARKERS = [
    "Microaneurysms", "Hemorrhages", "ExudatesHard", "ExudatesSoft",
    "OpticDisc", "OpticCup", "Vessels", "Macula",
    "IRMA", "Neovascularization",
]


class MAPLESDRDataset(EyeDataHubDataset):
    """
    MAPLES-DR: Montreal Annotation Project for Lesion and Structure Evaluation in DR.

    198 MESSIDOR fundus images re-annotated with pixel-wise segmentation maps
    for 10 anatomical and pathological biomarkers, plus revised DR and ME diagnoses.
    """

    _SUBDIR = "maples_dr"
    _FIGSHARE_ID = "24328660"
    _FIGSHARE_URL = "https://doi.org/10.6084/m9.figshare.24328660"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="maples_dr",
            full_name="MAPLES-DR: Montreal Annotation Project for DR",
            description=(
                "198 fundus images (from MESSIDOR) with pixel-wise segmentation "
                "for 10 biomarkers (lesions + structures) + DR and ME severity grades."
            ),
            modality="fundus",
            tasks=["segmentation", "grading", "classification"],
            num_samples=198,
            splits=["train", "test"],
            classes=["No DR", "Mild DR", "Moderate DR", "Severe DR", "PDR"],
            num_classes=5,
            download_type="figshare",
            download_url=self._FIGSHARE_URL,
            license="CC BY 4.0",
            citation=(
                "Morin et al., 'MAPLES-DR: MESSIDOR Annotation Project for Lesion "
                "and Structures Evaluation in Diabetic Retinopathy', Scientific Data 2024."
            ),
            tags=["dr", "segmentation", "lesions", "fundus", "multi_task"],
            size_gb=0.5,
            notes="Segmentation maps for 10 retinal biomarkers.",
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return len(list(root.glob("**/*.png"))) > 50

    def download(self, data_dir: Union[str, Path]) -> None:
        root = Path(data_dir) / self._SUBDIR
        try:
            download_figshare(self._FIGSHARE_ID, root)
            for archive in list(root.glob("*.zip")) + list(root.glob("*.tar*")):
                extract_archive(archive, root)
        except Exception:
            print_manual_download_instructions(
                "MAPLES-DR",
                self._FIGSHARE_URL,
                root,
                extra_notes=(
                    "Download from Figshare (free, no login required):\n"
                    f"  {self._FIGSHARE_URL}\n"
                    "Expected structure:\n"
                    "  maples_dr/images/*.jpg\n"
                    "  maples_dr/segmentation/Microaneurysms/*.png\n"
                    "  maples_dr/segmentation/Hemorrhages/*.png\n"
                    "  maples_dr/grades.csv  (columns: image_id, DR_grade, ME_grade)"
                ),
            )
            raise

    def load(self, data_dir: Union[str, Path], split: str = "test") -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR

        img_dirs = [root / "images", root]
        img_dir = next((d for d in img_dirs if d.exists()), root)

        label_map = {}
        for csv_path in list(root.glob("*.csv")):
            try:
                df = pd.read_csv(csv_path)
                id_col = df.columns[0]
                grade_col = next((c for c in df.columns if "dr" in c.lower() or "grade" in c.lower()), df.columns[1])
                for _, row in df.iterrows():
                    label_map[str(row[id_col])] = int(row[grade_col])
                break
            except Exception:
                pass

        samples = []
        for img_path in sorted(img_dir.glob("*.jpg")) + sorted(img_dir.glob("*.png")):
            stem = img_path.stem
            label = label_map.get(stem, label_map.get(img_path.name, 0))
            samples.append(DatasetSample(
                image_path=str(img_path),
                label=label,
                sample_id=stem,
                metadata={"split": split},
            ))
        return samples


# ---------------------------------------------------------------------------
# EyePACS
# ---------------------------------------------------------------------------

class EyePACSDataset(EyeDataHubDataset):
    """
    EyePACS: Diabetic Retinopathy Detection (Kaggle 2015 competition).

    ~88,000 fundus images graded 0–4 for DR severity (train set).
    The largest publicly available DR grading dataset.

    Kaggle competition: https://www.kaggle.com/c/diabetic-retinopathy-detection
    License: Kaggle competition rules (research / non-commercial use)

    Note: This is a very large dataset (~89 GB). Partial download via
    --subset is not supported through the Kaggle API; the full download
    will be initiated.
    """

    _SUBDIR = "eyepacs"
    _KAGGLE_SLUG = "diabetic-retinopathy-detection"

    CLASSES = ["No DR", "Mild", "Moderate", "Severe", "Proliferative DR"]

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="eyepacs",
            full_name="EyePACS — Diabetic Retinopathy Detection (Kaggle 2015)",
            description=(
                "~88,000 fundus images graded 0–4 for DR severity. "
                "Largest public DR dataset; competition images from EyePACS clinics."
            ),
            modality="fundus",
            tasks=["grading", "classification"],
            num_samples=88702,
            splits=["train", "test"],
            classes=self.CLASSES,
            num_classes=5,
            download_type="kaggle",
            download_url="https://www.kaggle.com/c/diabetic-retinopathy-detection",
            license="Kaggle competition rules (non-commercial research)",
            citation=(
                "EyePACS / California Healthcare Foundation. "
                "'Diabetic Retinopathy Detection', Kaggle Competition, 2015."
            ),
            tags=["diabetic_retinopathy", "grading", "fundus", "large_scale", "kaggle"],
            size_gb=89.0,
            notes="Very large (~89 GB). Kaggle competition account and acceptance of rules required.",
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return (root / "train.csv").exists() or (root / "trainLabels.csv").exists()

    def download(self, data_dir: Union[str, Path]) -> None:
        dest = Path(data_dir) / self._SUBDIR
        try:
            download_kaggle(self._KAGGLE_SLUG, dest, is_competition=True)
        except Exception:
            print_manual_download_instructions(
                "EyePACS — Diabetic Retinopathy Detection",
                "https://www.kaggle.com/c/diabetic-retinopathy-detection",
                dest,
                extra_notes=(
                    "Kaggle competition credentials required.\n"
                    "  1. Accept competition rules on Kaggle\n"
                    "  2. Set KAGGLE_USERNAME + KAGGLE_KEY in .env\n"
                    "  3. Re-run: eyehub download --datasets eyepacs\n\n"
                    "Warning: ~89 GB download."
                ),
            )
            raise

    def load(self, data_dir: Union[str, Path], split: str = "train") -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR

        # Labels CSV: trainLabels.csv has columns image,level
        label_file = root / "trainLabels.csv"
        if not label_file.exists():
            label_file = root / "train.csv"

        label_map: dict = {}
        if label_file.exists():
            df = pd.read_csv(label_file)
            id_col = next((c for c in df.columns if "image" in c.lower()), df.columns[0])
            lbl_col = next((c for c in df.columns if "level" in c.lower() or "label" in c.lower()), df.columns[1])
            for _, row in df.iterrows():
                label_map[str(row[id_col])] = int(row[lbl_col])

        img_dir = root / f"{split}" if (root / f"{split}").exists() else root
        images = sorted(img_dir.rglob("*.jpeg")) + sorted(img_dir.rglob("*.jpg")) + sorted(img_dir.rglob("*.png"))

        return [
            DatasetSample(
                image_path=str(p),
                label=label_map.get(p.stem, label_map.get(p.name, None)),
                sample_id=p.stem,
                metadata={"split": split},
            )
            for p in images
        ]


# ---------------------------------------------------------------------------
# Shared DR grade list
# ---------------------------------------------------------------------------

DR_GRADES = ["No DR", "Mild DR", "Moderate DR", "Severe DR", "Proliferative DR"]


# ---------------------------------------------------------------------------
# BiDR: Diagnosis of Diabetic Retinopathy (Kaggle pkdarabi)
# ---------------------------------------------------------------------------

class BiDRDataset(EyeDataHubDataset):
    """
    BiDR: Diabetic Retinopathy Diagnosis Dataset.

    Balanced fundus image dataset for 5-class DR grading, available on Kaggle.
    Includes images across all five ICDR DR severity levels.

    Kaggle: https://www.kaggle.com/datasets/pkdarabi/diagnosis-of-diabetic-retinopathy
    """

    _SUBDIR = "bidr"
    _KAGGLE_SLUG = "pkdarabi/diagnosis-of-diabetic-retinopathy"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="bidr",
            full_name="BiDR: Diabetic Retinopathy Diagnosis Dataset",
            description=(
                "35,126 fundus images for 5-class diabetic retinopathy grading "
                "(No DR: 25,810 / Mild: 2,443 / Moderate: 5,292 / Severe: 873 / "
                "Proliferative: 708). Available via Kaggle."
            ),
            modality="fundus",
            tasks=["grading", "classification"],
            num_samples=35126,
            splits=["train", "test"],
            classes=DR_GRADES,
            num_classes=5,
            download_type="kaggle",
            download_url="https://www.kaggle.com/datasets/pkdarabi/diagnosis-of-diabetic-retinopathy",
            license="See Kaggle dataset page",
            citation=(
                "BiDR Dataset. Kaggle. "
                "https://www.kaggle.com/datasets/pkdarabi/diagnosis-of-diabetic-retinopathy"
            ),
            tags=["dr", "fundus", "kaggle", "grading", "duplicate_of_eyepacs"],
            size_gb=1.0,
            notes=(
                "OVERLAP: BiDR is a Kaggle re-upload of the EyePACS Kaggle "
                "2015 competition TRAIN split (35,126 images). Already in "
                "EyeDataHub as `eyepacs` (full 88,702 train+test) and also as "
                "`dr_arranged` (Tianchi mirror of the same train split). "
                "Kept for users who specifically reference the BiDR slug."
            ),
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return (
            len(list(root.glob("**/*.jpg"))) > 50
            or len(list(root.glob("**/*.png"))) > 50
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        dest = Path(data_dir) / self._SUBDIR
        try:
            download_kaggle(self._KAGGLE_SLUG, dest, is_competition=False)
        except Exception:
            print_manual_download_instructions(
                "BiDR",
                "https://www.kaggle.com/datasets/pkdarabi/diagnosis-of-diabetic-retinopathy",
                dest,
            )
            raise

    def load(
        self, data_dir: Union[str, Path], split: str = "train"
    ) -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR

        # Expect class-named subdirectories or a CSV
        csv_files = list(root.glob("*.csv")) + list(root.glob("**/*.csv"))
        if csv_files:
            df = pd.read_csv(csv_files[0])
            id_col = next(
                (c for c in df.columns if any(
                    kw in c.lower() for kw in ("image", "file", "id")
                )), df.columns[0]
            )
            lbl_col = next(
                (c for c in df.columns if any(
                    kw in c.lower() for kw in ("label", "grade", "level", "dr")
                )), df.columns[1] if len(df.columns) > 1 else None
            )
            samples = []
            for _, row in df.iterrows():
                img_rel = str(row[id_col])
                img_path = root / img_rel
                if not img_path.exists():
                    candidates = list(root.rglob(Path(img_rel).name))
                    img_path = candidates[0] if candidates else img_path
                lbl = int(row[lbl_col]) if lbl_col else None
                samples.append(
                    DatasetSample(
                        image_path=str(img_path),
                        label=lbl,
                        sample_id=Path(img_rel).stem,
                        metadata={"split": split},
                    )
                )
            return samples

        # Class directory layout: 0_No_DR, 1_Mild, etc.
        grade_kw = {"0": 0, "no_dr": 0, "no dr": 0,
                    "1": 1, "mild": 1,
                    "2": 2, "moderate": 2,
                    "3": 3, "severe": 3,
                    "4": 4, "proliferative": 4}
        samples = []
        for class_dir in sorted(root.rglob("*")):
            if not class_dir.is_dir():
                continue
            dname = class_dir.name.lower()
            lbl = next((v for k, v in grade_kw.items() if dname.startswith(k)), None)
            for img_path in sorted(
                list(class_dir.glob("*.jpg"))
                + list(class_dir.glob("*.jpeg"))
                + list(class_dir.glob("*.png"))
            ):
                samples.append(
                    DatasetSample(
                        image_path=str(img_path),
                        label=lbl,
                        sample_id=img_path.stem,
                        metadata={"split": split},
                    )
                )
        if not samples:
            raise FileNotFoundError(
                f"No images found in {root}. "
                "Run: eyehub download --datasets bidr"
            )
        return samples


# ---------------------------------------------------------------------------
# Diabetic Retinopathy Arranged (Tianchi/Aliyun dataset 93926)
# ---------------------------------------------------------------------------

class DRArrangedDataset(EyeDataHubDataset):
    """
    Diabetic Retinopathy Arranged Dataset (Tianchi / Aliyun, dataset 93926).

    An organised version of a DR fundus image collection annotated with
    5-class ICDR grading, hosted on the Alibaba Tianchi data platform.
    Requires free registration at https://tianchi.aliyun.com.

    URL: https://tianchi.aliyun.com/dataset/93926
    """

    _SUBDIR = "dr_arranged"
    _TIANCHI_URL = "https://tianchi.aliyun.com/dataset/93926"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="dr_arranged",
            full_name="Diabetic Retinopathy Arranged Dataset (Tianchi 93926)",
            description=(
                "35,126 fundus images organised for 5-class DR severity grading "
                "(ICDR grades 0-4): No DR 25,810 / Mild 2,443 / Moderate 5,292 / "
                "Severe 873 / Proliferative 708. Hosted on Alibaba Tianchi."
            ),
            modality="fundus",
            tasks=["grading", "classification"],
            num_samples=35126,
            splits=["train", "test"],
            classes=DR_GRADES,
            num_classes=5,
            download_type="manual",
            download_url="https://tianchi.aliyun.com/dataset/93926",
            license="CC BY-NC-SA 4.0",
            citation=(
                "Diabetic Retinopathy Arranged Dataset. "
                "Tianchi Open Datasets, dataset ID 93926. "
                "https://tianchi.aliyun.com/dataset/93926"
            ),
            tags=["dr", "fundus", "manual", "grading", "duplicate_of_eyepacs"],
            size_gb=8.0,
            notes=(
                "OVERLAP: This is the EyePACS Kaggle 2015 competition TRAIN "
                "split (35,126 images) mirrored on Tianchi. Same content as "
                "`bidr` (Kaggle mirror) and a strict subset of `eyepacs` "
                "(full 88,702). Kept for users who specifically reference "
                "the Tianchi 93926 mirror.\n"
                "Requires free registration at https://tianchi.aliyun.com. "
                "Log in → Datasets → 93926 → Download."
            ),
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return (
            len(list(root.glob("**/*.jpg"))) > 50
            or len(list(root.glob("**/*.png"))) > 50
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        dest = Path(data_dir) / self._SUBDIR
        print_manual_download_instructions(
            "DR Arranged (Tianchi 93926)",
            self._TIANCHI_URL,
            dest,
            extra_notes=(
                "1. Register / log in at https://tianchi.aliyun.com\n"
                "2. Navigate to Datasets → ID 93926\n"
                "3. Download the archive and extract into:\n"
                f"   {dest}"
            ),
        )
        raise RuntimeError(
            "DR Arranged dataset requires manual download from Tianchi. "
            "See instructions above."
        )

    def load(
        self, data_dir: Union[str, Path], split: str = "train"
    ) -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR
        grade_kw = {"0": 0, "no": 0, "1": 1, "mild": 1,
                    "2": 2, "moderate": 2, "3": 3, "severe": 3,
                    "4": 4, "proliferative": 4}

        # CSV first
        csv_files = list(root.glob("*.csv")) + list(root.glob("**/*.csv"))
        if csv_files:
            df = pd.read_csv(csv_files[0])
            id_col = next(
                (c for c in df.columns if any(
                    kw in c.lower() for kw in ("image", "file", "id")
                )), df.columns[0]
            )
            lbl_col = next(
                (c for c in df.columns if any(
                    kw in c.lower() for kw in ("label", "grade", "level", "dr")
                )), df.columns[1] if len(df.columns) > 1 else None
            )
            samples = []
            for _, row in df.iterrows():
                img_rel = str(row[id_col])
                img_path = root / img_rel
                if not img_path.exists():
                    candidates = list(root.rglob(Path(img_rel).name))
                    img_path = candidates[0] if candidates else img_path
                lbl = int(row[lbl_col]) if lbl_col else None
                samples.append(
                    DatasetSample(
                        image_path=str(img_path),
                        label=lbl,
                        sample_id=Path(img_rel).stem,
                        metadata={"split": split},
                    )
                )
            return samples

        # Directory layout
        samples = []
        for class_dir in sorted(root.rglob("*")):
            if not class_dir.is_dir():
                continue
            dname = class_dir.name.lower()
            lbl = next((v for k, v in grade_kw.items() if dname.startswith(k)), None)
            for img_path in sorted(
                list(class_dir.glob("*.jpg"))
                + list(class_dir.glob("*.jpeg"))
                + list(class_dir.glob("*.png"))
            ):
                samples.append(
                    DatasetSample(
                        image_path=str(img_path),
                        label=lbl,
                        sample_id=img_path.stem,
                        metadata={"split": split},
                    )
                )
        if not samples:
            raise FileNotFoundError(
                f"No images found in {root}. "
                "Run: eyehub download --datasets dr_arranged"
            )
        return samples


# ---------------------------------------------------------------------------
# MMRDR: Multi-Modal Retinal Diabetic Retinopathy Dataset (Figshare 29423747)
# ---------------------------------------------------------------------------

class MMRDRDataset(EyeDataHubDataset):
    """
    MMRDR: Multi-Modal Retinal Diabetic Retinopathy Dataset.

    A multi-modal fundus dataset for DR detection and severity assessment,
    comprising color fundus photographs (CFP), optical coherence tomography
    (OCT) scans, and ultra-widefield (UWF) fundus images. Curated for
    cross-modal analysis and DR grading studies.

    Figshare: https://doi.org/10.6084/m9.figshare.29423747
    GitHub:   https://github.com/Vladimirovich2019/MMRDR_Evaluation
    Paper:    Nature Scientific Data (2026)
    """

    _SUBDIR = "mmrdr"
    _FIGSHARE_ID = "29423747"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="mmrdr",
            full_name="MMRDR: Multi-Modal Retinal Diabetic Retinopathy Dataset",
            description=(
                "Multi-modal DR dataset combining color fundus photographs (CFP), "
                "OCT B-scans, and ultra-widefield (UWF) fundus images, annotated "
                "for DR detection and severity grading. Published in Nature "
                "Scientific Data 2026."
            ),
            modality="multimodal",
            tasks=["grading", "classification"],
            num_samples=24460,
            splits=["train", "test"],
            classes=DR_GRADES,
            num_classes=5,
            download_type="figshare",
            download_url="https://doi.org/10.6084/m9.figshare.29423747",
            license="CC BY 4.0",
            citation=(
                "MMRDR: Multi-Modal Retinal Diabetic Retinopathy Dataset. "
                "Nature Scientific Data 2026. "
                "Figshare: https://doi.org/10.6084/m9.figshare.29423747 — "
                "GitHub: https://github.com/Vladimirovich2019/MMRDR_Evaluation"
            ),
            tags=["dr", "fundus", "oct", "uwf", "multimodal", "figshare", "grading"],
            size_gb=18.61,
            notes=(
                "Contains 24,460 images across CFP, OCT, and UWF modalities. "
                "The source-reported unit is images rather than unique patients. "
                "Evaluation code: https://github.com/Vladimirovich2019/MMRDR_Evaluation"
            ),
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return (
            len(list(root.glob("**/*.jpg"))) > 50
            or len(list(root.glob("**/*.png"))) > 50
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        dest = Path(data_dir) / self._SUBDIR
        try:
            download_figshare(self._FIGSHARE_ID, dest)
            first_parts = sorted(dest.glob("*.zip.001"))
            for first_part in first_parts:
                prefix = first_part.name[:-4]
                parts = sorted(
                    dest.glob(f"{prefix}.[0-9][0-9][0-9]"),
                    key=lambda path: int(path.suffix[1:]),
                )
                numbers = [int(path.suffix[1:]) for path in parts]
                if numbers != list(range(1, max(numbers) + 1)):
                    raise RuntimeError(
                        f"MMRDR split archive is incomplete: {numbers}"
                    )
                combined = dest / prefix
                with combined.open("wb") as output:
                    for part in parts:
                        with part.open("rb") as source:
                            while chunk := source.read(16 * 1024 * 1024):
                                output.write(chunk)
                extract_archive(combined, dest)
                combined.unlink(missing_ok=True)
                for part in parts:
                    part.unlink(missing_ok=True)
            for archive in list(dest.glob("*.zip")) + list(dest.glob("*.tar*")):
                extract_archive(archive, dest)
        except Exception:
            print_manual_download_instructions(
                "MMRDR",
                f"https://doi.org/10.6084/m9.figshare.{self._FIGSHARE_ID}",
                dest,
                extra_notes=(
                    "Download from Figshare article 29423747 and extract into:\n"
                    f"  {dest}\n\n"
                    "Evaluation code:\n"
                    "  https://github.com/Vladimirovich2019/MMRDR_Evaluation"
                ),
            )
            raise

    def load(
        self, data_dir: Union[str, Path], split: str = "train"
    ) -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR

        # Build label map from CSV if available
        label_map: dict = {}
        csv_files = list(root.glob("*.csv")) + list(root.glob("**/*.csv"))
        if csv_files:
            df = pd.read_csv(csv_files[0])
            id_col = next(
                (c for c in df.columns if any(
                    kw in c.lower() for kw in ("image", "file", "id", "name")
                )), df.columns[0]
            )
            lbl_col = next(
                (c for c in df.columns if any(
                    kw in c.lower() for kw in ("label", "grade", "dr", "level")
                )), df.columns[1] if len(df.columns) > 1 else None
            )
            split_col = next((c for c in df.columns if "split" in c.lower()), None)
            for _, row in df.iterrows():
                if split_col and str(row[split_col]).lower() != split.lower():
                    continue
                lbl = int(row[lbl_col]) if lbl_col else None
                label_map[str(row[id_col]).strip()] = lbl

        images = sorted(
            list(root.rglob("*.jpg"))
            + list(root.rglob("*.jpeg"))
            + list(root.rglob("*.png"))
        )
        if split != "all":
            filtered = [p for p in images if split.lower() in str(p).lower()]
            if filtered:
                images = filtered

        if not images:
            raise FileNotFoundError(
                f"No images found in {root}. "
                "Run: eyehub download --datasets mmrdr"
            )

        grade_kw = {"0": 0, "no_dr": 0, "no dr": 0,
                    "1": 1, "mild": 1,
                    "2": 2, "moderate": 2,
                    "3": 3, "severe": 3,
                    "4": 4, "proliferative": 4}

        samples = []
        for img_path in images:
            lbl = label_map.get(img_path.stem) or label_map.get(img_path.name)
            if lbl is None:
                path_lower = str(img_path).lower()
                lbl = next(
                    (v for k, v in grade_kw.items() if k in path_lower),
                    None,
                )
            # Determine modality from path
            path_lower = str(img_path).lower()
            if "oct" in path_lower:
                sub_modality = "oct"
            elif "uwf" in path_lower or "ultra" in path_lower:
                sub_modality = "uwf"
            else:
                sub_modality = "cfp"
            samples.append(
                DatasetSample(
                    image_path=str(img_path),
                    label=lbl,
                    sample_id=img_path.stem,
                    metadata={"split": split, "sub_modality": sub_modality},
                )
            )
        return samples
