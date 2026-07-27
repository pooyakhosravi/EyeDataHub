"""
Ultra-widefield (UWF) fundus datasets.

Included:
  - TsukazakiUWF   : 13,047 UWF images, 8 multi-label disease categories (Tsukazaki Hospital)
  - UWFTumorDataset: UWF fundus images for intraocular tumor detection (Figshare 27986258)
  - OculoScopeDataset: ~16,530 UWF images, 38 disease categories (Fairer AI, Figshare)
  - DeepDRiDDataset: 2,000 regular + 256 UWF fundus, DR grading + quality (Zenodo 8248825)
  - UWFDRDataset   : UWF fundus DR grading from Reasoning-Enhanced VLM paper (GDrive)
"""
from __future__ import annotations

from pathlib import Path
from typing import List, Union

import pandas as pd

from eyedatahub.core.dataset import DatasetInfo, DatasetSample, EyeDataHubDataset
from eyedatahub.datasets.download_utils import (
    download_figshare,
    download_figshare_private,
    download_gdrive_folder,
    download_github_repo,
    download_zenodo,
    extract_archive,
    print_manual_download_instructions,
)


# ---------------------------------------------------------------------------
# Tsukazaki UWF Fundus Dataset (GitHub DateCazuki/Fundus_Diagnosis)
# ---------------------------------------------------------------------------

TSUKAZAKI_DISEASE_LABELS = [
    "AO",   # Artery Occlusion
    "AMD",  # Age-related Macular Degeneration
    "DR",   # Diabetic Retinopathy
    "Gla",  # Glaucoma
    "MH",   # Macular Hole
    "RD",   # Retinal Detachment
    "RP",   # Retinitis Pigmentosa
    "RVO",  # Retinal Vein Occlusion
]


class TsukazakiUWFDataset(EyeDataHubDataset):
    """
    Tsukazaki Hospital Ultra-Widefield Fundus Dataset.

    13,047 UWF fundus images (Optos, 200° field) annotated with 8 binary
    disease labels. Associated with Scientific Data 2024 paper.

    GitHub: https://github.com/DateCazuki/Fundus_Diagnosis
    Note: Full dataset restricted due to data export regulations;
          a public subset (healthy + RP) may be available on Figshare.
    """

    _SUBDIR = "tsukazaki_uwf"
    _GITHUB_REPO = "DateCazuki/Fundus_Diagnosis"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="tsukazaki_uwf",
            full_name="Tsukazaki Hospital UWF Fundus Dataset",
            description=(
                "13,047 ultra-widefield fundus photographs (Optos, 200° FOV) "
                "from Tsukazaki Hospital, annotated with 8 binary disease labels: "
                "AO, AMD, DR, Glaucoma, MH, RD, RP, RVO. "
                "Associated with Scientific Data 2024."
            ),
            modality="uwf_fundus",
            tasks=["multilabel", "classification"],
            num_samples=13047,
            splits=["train", "test"],
            classes=TSUKAZAKI_DISEASE_LABELS,
            num_classes=8,
            download_type="github",
            download_url="https://github.com/DateCazuki/Fundus_Diagnosis",
            license="Research only — contact authors for data access",
            citation=(
                "Nagasawa T et al., 'Automatic detection of multiple retinal diseases "
                "in ultra-widefield fundus images using deep learning', "
                "Nature Machine Intelligence 2022. "
                "https://www.nature.com/articles/s42256-022-00566-5 — "
                "Data: https://github.com/DateCazuki/Fundus_Diagnosis"
            ),
            tags=["uwf", "fundus", "multilabel", "multi_disease", "github"],
            size_gb=15.0,
            notes=(
                "Full dataset is subject to Japanese export restrictions. "
                "Contact the authors for access. A public subset may be "
                "available via the GitHub repo or linked Figshare."
            ),
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return (
            len(list(root.glob("**/*.jpg"))) > 100
            or len(list(root.glob("**/*.png"))) > 100
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        dest = Path(data_dir) / self._SUBDIR
        try:
            download_github_repo(self._GITHUB_REPO, dest, branch="main")
        except Exception:
            try:
                download_github_repo(self._GITHUB_REPO, dest, branch="master")
            except Exception:
                print_manual_download_instructions(
                    "Tsukazaki UWF",
                    "https://github.com/DateCazuki/Fundus_Diagnosis",
                    dest,
                    extra_notes=(
                        "The full image dataset requires contacting the authors.\n"
                        "Clone the repo for annotations/labels:\n"
                        "  git clone https://github.com/DateCazuki/Fundus_Diagnosis\n"
                        "Then place images under:\n"
                        f"  {dest}/images/<split>/"
                    ),
                )
                raise

    def load(
        self, data_dir: Union[str, Path], split: str = "train"
    ) -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR

        # Look for annotation CSV (repo typically has a labels file)
        csv_candidates = (
            list(root.glob("*labels*.csv"))
            + list(root.glob("*annotation*.csv"))
            + list(root.glob("**/*.csv"))
        )

        label_map: dict = {}
        if csv_candidates:
            df = pd.read_csv(csv_candidates[0])
            id_col = df.columns[0]
            disease_cols = [c for c in df.columns if c in TSUKAZAKI_DISEASE_LABELS]
            if not disease_cols:
                disease_cols = [
                    c for c in df.columns[1:]
                    if set(df[c].dropna().unique()).issubset({0, 1})
                ]
            for _, row in df.iterrows():
                img_id = str(row[id_col]).strip()
                label_map[img_id] = [int(row[c]) for c in disease_cols]

        images = sorted(
            list(root.rglob("*.jpg"))
            + list(root.rglob("*.jpeg"))
            + list(root.rglob("*.png"))
        )
        # Filter by split if subdirectory structure supports it
        if split != "all":
            filtered = [p for p in images if split.lower() in str(p).lower()]
            if filtered:
                images = filtered

        if not images:
            raise FileNotFoundError(
                f"No images found in {root}. "
                "Run: eyehub download --datasets tsukazaki_uwf"
            )

        samples = []
        for img_path in images:
            lbl = label_map.get(img_path.stem) or label_map.get(img_path.name)
            samples.append(
                DatasetSample(
                    image_path=str(img_path),
                    label=lbl,
                    sample_id=img_path.stem,
                    metadata={"split": split},
                )
            )
        return samples


# ---------------------------------------------------------------------------
# UWF Intraocular Tumor Dataset (Figshare 27986258)
# ---------------------------------------------------------------------------

UWF_TUMOR_CLASSES = [
    "Normal",
    "Choroidal Hemangioma",         # CH
    "Retinal Capillary Hemangioma",  # RCH
    "Choroidal Osteoma",             # CO
    "Retinoblastoma",                # RB
    "Uveal Melanoma",                # UM
]


class UWFTumorDataset(EyeDataHubDataset):
    """
    Ultra-Widefield Fundus Intraocular Tumor Dataset.

    2,031 UWF fundus images annotated by 3 expert annotators across 6 categories:
    Normal, Choroidal Hemangioma (CH), Retinal Capillary Hemangioma (RCH),
    Choroidal Osteoma (CO), Retinoblastoma (RB), and Uveal Melanoma (UM).
    Images are split 8:1:1 (train/val/test) via stratified sampling.

    Figshare: https://doi.org/10.6084/m9.figshare.27986258
    """

    _SUBDIR = "uwf_tumor"
    _FIGSHARE_ID = "27986258"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="uwf_tumor",
            full_name="UWF Fundus Intraocular Tumor Dataset",
            description=(
                "2,031 ultra-widefield fundus images for AI-assisted intraocular "
                "tumor detection and classification. Six categories: Normal, "
                "Choroidal Hemangioma (CH), Retinal Capillary Hemangioma (RCH), "
                "Choroidal Osteoma (CO), Retinoblastoma (RB), Uveal Melanoma (UM). "
                "Annotated by 3 experts; split 8:1:1 (stratified)."
            ),
            modality="uwf_fundus",
            tasks=["classification"],
            num_samples=2031,
            splits=["train", "val", "test"],
            classes=UWF_TUMOR_CLASSES,
            num_classes=6,
            download_type="figshare",
            download_url="https://doi.org/10.6084/m9.figshare.27986258",
            license="CC BY 4.0",
            citation=(
                "UWF Intraocular Tumor Dataset. Scientific Data 2025. "
                "https://www.nature.com/articles/s41597-025-05864-2 — "
                "Figshare: https://doi.org/10.6084/m9.figshare.27986258"
            ),
            tags=["uwf", "fundus", "tumor", "figshare", "classification"],
            size_gb=2.0,
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return (
            len(list(root.glob("**/*.jpg"))) > 20
            or len(list(root.glob("**/*.png"))) > 20
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        dest = Path(data_dir) / self._SUBDIR
        try:
            download_figshare(self._FIGSHARE_ID, dest)
        except Exception:
            print_manual_download_instructions(
                "UWF Intraocular Tumor",
                f"https://doi.org/10.6084/m9.figshare.{self._FIGSHARE_ID}",
                dest,
                extra_notes=(
                    "Download the dataset archive from Figshare article "
                    f"{self._FIGSHARE_ID} and extract into {dest}."
                ),
            )
            raise

    def load(
        self, data_dir: Union[str, Path], split: str = "train"
    ) -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR

        keyword_map = {
            "normal": 0,
            "choroidal_hemangioma": 1, "ch_": 1,
            "retinal_capillary": 2, "rch": 2,
            "osteoma": 3, "co_": 3,
            "retinoblastoma": 4, "rb_": 4,
            "melanoma": 5, "uveal": 5, "um_": 5,
        }

        # Check for CSV first
        csv_files = list(root.glob("*.csv")) + list(root.glob("**/*.csv"))
        if csv_files:
            df = pd.read_csv(csv_files[0])
            img_col = next(
                (c for c in df.columns if any(
                    kw in c.lower() for kw in ("image", "file", "path", "name")
                )), df.columns[0]
            )
            lbl_col = next(
                (c for c in df.columns if any(
                    kw in c.lower() for kw in ("label", "class", "category", "type")
                )), df.columns[1] if len(df.columns) > 1 else None
            )
            samples = []
            for _, row in df.iterrows():
                img_rel = str(row[img_col])
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

        # Infer labels from directory/file names
        samples = []
        for img_path in sorted(
            list(root.rglob("*.jpg"))
            + list(root.rglob("*.jpeg"))
            + list(root.rglob("*.png"))
        ):
            path_lower = str(img_path).lower()
            lbl = next(
                (idx for kw, idx in keyword_map.items() if kw in path_lower),
                None,
            )
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
                "Run: eyehub download --datasets uwf_tumor"
            )
        return samples


# ---------------------------------------------------------------------------
# OculoScope Dataset (Fairer AI in Ophthalmology, Figshare private share)
# ---------------------------------------------------------------------------

# Partial list of known OculoScope diseases used for path-based label inference
_OCULOSCOPE_KNOWN_CLASSES = [
    "Normal",
    "Diabetic Retinopathy", "Glaucoma", "AMD",
    "Retinal Vein Occlusion", "Retinal Artery Occlusion",
    "Retinal Detachment", "Epiretinal Membrane", "Macular Hole",
    "Myopia", "Hypertensive Retinopathy", "Retinitis Pigmentosa",
]


class OculoScopeDataset(EyeDataHubDataset):
    """
    OculoScope: Fairer AI in Ophthalmology Dataset.

    16,530 UWF fundus images from 8,405+ patients spanning 38 ophthalmic
    diseases and 67 fundus features across ages 0–90. Released with the
    FairerOPTH study on mitigating sex and age bias in ophthalmic AI.

    Reference: Nature Communications 2024
    Figshare private share: https://figshare.com/s/926c2c2ef9e77ab5eb9d
    """

    _SUBDIR = "oculoscope"
    _FIGSHARE_SHARE_TOKEN = "926c2c2ef9e77ab5eb9d"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="oculoscope",
            full_name="OculoScope: Fairer AI in Ophthalmology Dataset",
            description=(
                "16,530 ultra-widefield fundus images from 8,405+ patients "
                "(age 0–90) annotated for 38 ophthalmic diseases and 67 fundus "
                "features. Released alongside the FairerOPTH study on sexism and "
                "ageism in ophthalmic AI (Nature Communications 2024)."
            ),
            modality="uwf_fundus",
            tasks=["classification", "multilabel"],
            num_samples=16530,
            splits=["train", "test"],
            classes=None,   # 38 diseases × 67 features — see dataset CSV for full list
            num_classes=38,
            download_type="figshare",
            download_url="https://figshare.com/s/926c2c2ef9e77ab5eb9d",
            license="CC BY 4.0",
            citation=(
                "FairerOPTH Study — OculoScope Dataset. Nature Communications 2024. "
                "https://www.nature.com/articles/s41467-024-48972-0 — "
                "Data: https://figshare.com/s/926c2c2ef9e77ab5eb9d"
            ),
            tags=["uwf", "fundus", "figshare", "multi_disease", "fairness"],
            size_gb=20.0,
            notes=(
                "Also annotates 67 fine-grained fundus features in addition to "
                "38 disease-level labels. Full class list in dataset CSV."
            ),
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return (
            len(list(root.glob("**/*.jpg"))) > 100
            or len(list(root.glob("**/*.png"))) > 100
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        dest = Path(data_dir) / self._SUBDIR
        try:
            download_figshare_private(self._FIGSHARE_SHARE_TOKEN, dest)
        except Exception:
            print_manual_download_instructions(
                "OculoScope",
                f"https://figshare.com/s/{self._FIGSHARE_SHARE_TOKEN}",
                dest,
                extra_notes=(
                    "Visit the Figshare private share link and download manually.\n"
                    f"Extract the archive into: {dest}"
                ),
            )
            raise

    def load(
        self, data_dir: Union[str, Path], split: str = "train"
    ) -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR

        # OculoScope typically ships with a label CSV
        csv_candidates = (
            list(root.glob("*label*.csv"))
            + list(root.glob("*annotation*.csv"))
            + list(root.glob("**/*.csv"))
        )

        if csv_candidates:
            df = pd.read_csv(csv_candidates[0])
            id_col = next(
                (c for c in df.columns if any(
                    kw in c.lower() for kw in ("image", "file", "id", "path")
                )), df.columns[0]
            )
            lbl_col = next(
                (c for c in df.columns if any(
                    kw in c.lower() for kw in ("label", "class", "disease", "category")
                )), df.columns[1] if len(df.columns) > 1 else None
            )
            split_col = next(
                (c for c in df.columns if "split" in c.lower()), None
            )

            samples = []
            for _, row in df.iterrows():
                if split_col and str(row[split_col]).lower() != split.lower():
                    continue
                img_rel = str(row[id_col])
                img_path = root / img_rel
                if not img_path.exists():
                    candidates = list(root.rglob(Path(img_rel).name))
                    img_path = candidates[0] if candidates else img_path
                lbl = row[lbl_col] if lbl_col else None
                if isinstance(lbl, str):
                    lbl_lower = lbl.lower()
                    lbl = next(
                        (i for i, c in enumerate(_OCULOSCOPE_KNOWN_CLASSES) if c.lower() in lbl_lower),
                        None,
                    )
                samples.append(
                    DatasetSample(
                        image_path=str(img_path),
                        label=lbl,
                        sample_id=Path(img_rel).stem,
                        metadata={"split": split},
                    )
                )
            return samples

        # Fallback: class-named subdirectories
        samples = []
        for class_dir in sorted(root.iterdir()):
            if not class_dir.is_dir():
                continue
            lbl = next(
                (i for i, c in enumerate(_OCULOSCOPE_KNOWN_CLASSES)
                 if c.lower().replace(" ", "_") in class_dir.name.lower()),
                None,
            )
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
                        metadata={"class_dir": class_dir.name, "split": split},
                    )
                )
        if not samples:
            raise FileNotFoundError(
                f"No images found in {root}. "
                "Run: eyehub download --datasets oculoscope"
            )
        return samples


# ---------------------------------------------------------------------------
# DeepDRiD (Zenodo 8248825)
# ---------------------------------------------------------------------------

DEEPDRID_DR_GRADES = [
    "No DR",
    "Mild NPDR",
    "Moderate NPDR",
    "Severe NPDR",
    "Proliferative DR",
]

DEEPDRID_QUALITY_LABELS = ["Ungradable", "Gradable"]


class DeepDRiDDataset(EyeDataHubDataset):
    """
    DeepDRiD: Diabetic Retinopathy Grading and Image Quality Estimation Challenge.

    2,000 regular fundus images (500 patients, dual-field) + 256 ultra-widefield
    fundus images for DR severity grading (5 ICDR grades) and image quality
    assessment (gradable/ungradable).

    Zenodo record: 8248825
    Reference: https://github.com/deepdrdoc/DeepDRiD
    """

    _SUBDIR = "deepdrid"
    _ZENODO_ID = "8248825"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="deepdrid",
            full_name="DeepDRiD: Diabetic Retinopathy Grading and Image Quality Dataset",
            description=(
                "2,000 regular fundus images (500 patients × 2 fields × 2 eyes) "
                "plus 256 ultra-widefield fundus images labeled for DR severity "
                "(ICDR grades 0-4) and image quality assessment (gradable/ungradable). "
                "From the DeepDRiD challenge (MICCAI 2020 / ISBI 2020)."
            ),
            modality="fundus",
            tasks=["grading", "classification", "quality"],
            num_samples=2256,
            splits=["train", "val", "test"],
            classes=DEEPDRID_DR_GRADES,
            num_classes=5,
            download_type="zenodo",
            download_url="https://zenodo.org/records/8248825",
            license="CC BY-SA 4.0",
            citation=(
                "Liu R et al., 'DeepDRiD: Diabetic Retinopathy—Grading and Image "
                "Quality Estimation Challenge', Patterns 2022. "
                "Zenodo: https://zenodo.org/records/8248825"
            ),
            tags=["dr", "fundus", "uwf", "zenodo", "grading", "quality"],
            size_gb=3.0,
            notes=(
                "Contains both regular fundus (2000 images in dual-field pairs) "
                "and ultra-widefield fundus (256 images). "
                "Labels CSV includes DR grade (0-4) and quality score."
            ),
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return (
            len(list(root.glob("**/*.jpg"))) > 100
            or len(list(root.glob("**/*.png"))) > 100
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        dest = Path(data_dir) / self._SUBDIR
        try:
            download_zenodo(self._ZENODO_ID, dest)
            for archive in list(dest.glob("*.zip")) + list(dest.glob("*.tar*")):
                extract_archive(archive, dest)
        except Exception:
            print_manual_download_instructions(
                "DeepDRiD",
                "https://zenodo.org/records/8248825",
                dest,
                extra_notes=(
                    "Download from Zenodo record 8248825.\n"
                    "Expected structure after extraction:\n"
                    "  deepdrid/regular_fundus_images/train/a_regular_fundus/*.jpg\n"
                    "  deepdrid/regular_fundus_images/train/b_regular_fundus/*.jpg\n"
                    "  deepdrid/regular-fundus-training-labels.csv\n"
                    "  deepdrid/ultra-widefield_images/train/*.jpg\n"
                    "  deepdrid/ultra-widefield-training-labels.csv"
                ),
            )
            raise

    def load(
        self, data_dir: Union[str, Path], split: str = "train"
    ) -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR

        # Map split name to expected path fragment
        split_dir_map = {
            "train": "train",
            "val":   ["val", "validation", "online_val"],
            "test":  ["test", "offline_val"],
        }
        split_dirs = split_dir_map.get(split, [split])
        if isinstance(split_dirs, str):
            split_dirs = [split_dirs]

        # ----- Load labels from CSV -----
        # Try regular fundus label CSV first
        label_map: dict = {}
        csv_keywords = {
            "train": ["training", "train"],
            "val":   ["val", "validation", "online"],
            "test":  ["test", "offline"],
        }
        for csv_path in list(root.glob("**/*.csv")):
            if any(kw in csv_path.name.lower() for kw in csv_keywords.get(split, [split])):
                df = pd.read_csv(csv_path)
                # Expected columns: image_path (or patient_id/image_id), DR_level, quality
                id_col = next(
                    (c for c in df.columns if any(
                        kw in c.lower() for kw in ("image", "file", "path", "id")
                    )), df.columns[0]
                )
                dr_col = next(
                    (c for c in df.columns if "dr" in c.lower() or "level" in c.lower() or "grade" in c.lower()),
                    None,
                )
                qual_col = next(
                    (c for c in df.columns if "quality" in c.lower() or "gradab" in c.lower()),
                    None,
                )
                for _, row in df.iterrows():
                    img_id = str(row[id_col]).strip()
                    lbl = int(row[dr_col]) if dr_col and not pd.isna(row.get(dr_col, float("nan"))) else None
                    quality = int(row[qual_col]) if qual_col and not pd.isna(row.get(qual_col, float("nan"))) else None
                    label_map[img_id] = {"dr_grade": lbl, "quality": quality}

        # ----- Collect images for this split -----
        images = []
        for sd in split_dirs:
            images.extend(root.rglob(f"*{sd}*/**/*.jpg"))
            images.extend(root.rglob(f"*{sd}*/**/*.jpeg"))
            images.extend(root.rglob(f"*{sd}*/**/*.png"))
        if not images:
            # Fall back to all images
            images = (
                list(root.rglob("*.jpg"))
                + list(root.rglob("*.jpeg"))
                + list(root.rglob("*.png"))
            )

        if not images:
            raise FileNotFoundError(
                f"No images found in {root}. "
                "Run: eyehub download --datasets deepdrid"
            )

        samples = []
        for img_path in sorted(set(images)):
            meta = label_map.get(img_path.stem) or label_map.get(img_path.name) or {}
            dr_grade = meta.get("dr_grade")
            quality = meta.get("quality")
            # Determine if this is UWF or regular from path
            is_uwf = "ultra" in str(img_path).lower() or "uwf" in str(img_path).lower()
            samples.append(
                DatasetSample(
                    image_path=str(img_path),
                    label=dr_grade,
                    sample_id=img_path.stem,
                    metadata={
                        "split": split,
                        "quality": quality,
                        "is_uwf": is_uwf,
                    },
                )
            )
        return samples


# ---------------------------------------------------------------------------
# UWF DR Reasoning Dataset (Google Drive folder)
# ---------------------------------------------------------------------------

UWFDR_CLASSES = [
    "No DR",
    "Mild DR",
    "Moderate DR",
    "Severe DR",
    "Proliferative DR",
]


class UWFDRDataset(EyeDataHubDataset):
    """
    UWF Fundus DR Grading Dataset from the Reasoning-Enhanced VLM paper.

    Ultra-widefield fundus images for diabetic retinopathy detection and
    grading, released alongside the paper:
    'Reasoning-Enhanced Vision-Language Model for Interpretable Diabetic
    Retinopathy Detection in Ultra-Wide-Field Fundus Images' (Springer 2024).

    Google Drive folder: https://drive.google.com/drive/folders/1wOqM-O_amSwMdli4OlFnGpf4hslPgDNu
    """

    _SUBDIR = "uwf_dr"
    _GDRIVE_FOLDER_ID = "1wOqM-O_amSwMdli4OlFnGpf4hslPgDNu"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="uwf_dr",
            full_name="UWF DR Reasoning Dataset",
            description=(
                "Ultra-widefield fundus photographs for diabetic retinopathy "
                "grading (5-level ICDR scale). Released alongside the "
                "Reasoning-Enhanced VLM paper for interpretable UWF DR detection. "
                "Related to the UWF4DR 2024 MICCAI challenge (~495 images across "
                "image quality and DR grading tasks)."
            ),
            modality="uwf_fundus",
            tasks=["grading", "classification"],
            num_samples=495,
            splits=["train", "val", "test"],
            classes=UWFDR_CLASSES,
            num_classes=5,
            download_type="gdrive",
            download_url="https://drive.google.com/drive/folders/1wOqM-O_amSwMdli4OlFnGpf4hslPgDNu",
            license="Research only — see paper terms",
            citation=(
                "Reasoning-Enhanced Vision-Language Model for Interpretable "
                "Diabetic Retinopathy Detection in Ultra-Wide-Field Fundus Images. "
                "OMIA 2025 (MICCAI Workshop), Springer. "
                "DOI: 10.1007/978-3-032-10351-2_12"
            ),
            tags=["uwf", "fundus", "dr", "gdrive", "grading"],
            size_gb=2.0,
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
            download_gdrive_folder(self._GDRIVE_FOLDER_ID, dest)
            # Extract any archives
            for archive in list(dest.glob("*.zip")) + list(dest.rglob("*.zip")):
                extract_archive(archive, dest)
        except Exception:
            print_manual_download_instructions(
                "UWF DR",
                f"https://drive.google.com/drive/folders/{self._GDRIVE_FOLDER_ID}",
                dest,
                extra_notes=(
                    "Open the Google Drive folder link and download the files manually.\n"
                    f"Extract into: {dest}\n"
                    "Requires: pip install gdown"
                ),
            )
            raise

    def load(
        self, data_dir: Union[str, Path], split: str = "train"
    ) -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR

        # Build label map from CSV if present
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
                    kw in c.lower() for kw in ("label", "grade", "dr", "class")
                )), df.columns[1] if len(df.columns) > 1 else None
            )
            if lbl_col:
                for _, row in df.iterrows():
                    label_map[str(row[id_col]).strip()] = int(row[lbl_col])

        # Collect all images
        images = sorted(
            list(root.rglob("*.jpg"))
            + list(root.rglob("*.jpeg"))
            + list(root.rglob("*.png"))
        )
        # Filter by split if directory structure uses it
        if split != "all":
            filtered = [p for p in images if split.lower() in str(p).lower()]
            if filtered:
                images = filtered

        if not images:
            raise FileNotFoundError(
                f"No images found in {root}. "
                "Run: eyehub download --datasets uwf_dr"
            )

        # Grade keywords for path-based label inference
        grade_keywords = {
            "no_dr": 0, "grade0": 0, "0_no": 0,
            "mild": 1, "grade1": 1, "1_mild": 1,
            "moderate": 2, "grade2": 2, "2_mod": 2,
            "severe": 3, "grade3": 3, "3_sev": 3,
            "proliferative": 4, "grade4": 4, "4_pro": 4,
        }

        samples = []
        for img_path in images:
            lbl = label_map.get(img_path.stem) or label_map.get(img_path.name)
            if lbl is None:
                path_lower = str(img_path).lower()
                lbl = next(
                    (idx for kw, idx in grade_keywords.items() if kw in path_lower),
                    None,
                )
            samples.append(
                DatasetSample(
                    image_path=str(img_path),
                    label=lbl,
                    sample_id=img_path.stem,
                    metadata={"split": split},
                )
            )
        return samples
