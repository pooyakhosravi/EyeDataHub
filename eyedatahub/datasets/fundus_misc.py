"""
Miscellaneous fundus datasets: AOD, ToxoFundus, FARFUM-ROP.
"""
from __future__ import annotations

from pathlib import Path
from typing import List, Union

import pandas as pd

from eyedatahub.core.dataset import DatasetInfo, DatasetSample, EyeDataHubDataset
from eyedatahub.datasets.download_utils import (
    download_figshare,
    download_kaggle,
    extract_archive,
    print_manual_download_instructions,
)


# ---------------------------------------------------------------------------
# AOD: Augmented Ocular Diseases Dataset (Kaggle)
# ---------------------------------------------------------------------------

AOD_CLASSES = [
    "Normal",           # N
    "Diabetes",         # D
    "Glaucoma",         # G
    "Cataract",         # C
    "AMD",              # A — Age-related Macular Degeneration
    "Hypertension",     # H
    "Myopia",           # M
    "Other",            # O
]


class AODDataset(EyeDataHubDataset):
    """
    AOD: Augmented Ocular Diseases dataset.

    Augmented version of the ODIR-5K fundus dataset spanning 8 disease
    categories (Normal, Diabetes, Glaucoma, Cataract, AMD, Hypertension,
    Myopia, Other) with preprocessing (crop, resize, CLAHE) and augmentation.

    Kaggle: https://www.kaggle.com/datasets/nurmukhammed7/augemnted-ocular-diseases
    """

    _SUBDIR = "aod"
    _KAGGLE_SLUG = "nurmukhammed7/augemnted-ocular-diseases"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="aod",
            full_name="AOD: Augmented Ocular Diseases Dataset",
            description=(
                "Augmented ODIR-5K fundus photographs for 8-class ocular disease "
                "classification: Normal, Diabetes, Glaucoma, Cataract, AMD, "
                "Hypertension, Myopia, Other. Preprocessing includes CLAHE and "
                "standard augmentation."
            ),
            modality="fundus",
            tasks=["classification"],
            num_samples=14813,
            splits=["train", "test"],
            classes=AOD_CLASSES,
            num_classes=8,
            download_type="kaggle",
            download_url="https://www.kaggle.com/datasets/nurmukhammed7/augemnted-ocular-diseases",
            license="See Kaggle dataset page",
            citation=(
                "AOD Dataset. Kaggle. "
                "https://www.kaggle.com/datasets/nurmukhammed7/augemnted-ocular-diseases"
            ),
            tags=["multi_disease", "fundus", "kaggle", "classification", "augmented", "derivative_of_odir2019"],
            size_gb=2.0,
            notes=(
                "OVERLAP: AOD is an augmented variant of ODIR-2019 (already "
                "in EyeDataHub as `odir2019`). Preprocessing (CLAHE) and "
                "augmentation explain the 14,813 vs 16,000 image count "
                "delta. Kept because the augmented split appears in "
                "downstream benchmarks separately."
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
                "AOD",
                "https://www.kaggle.com/datasets/nurmukhammed7/augemnted-ocular-diseases",
                dest,
            )
            raise

    def load(
        self, data_dir: Union[str, Path], split: str = "train"
    ) -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR
        class_keywords = {
            "normal": 0, "healthy": 0,
            "diabet": 1, "_d_": 1,
            "glaucoma": 2, "_g_": 2,
            "cataract": 3, "_c_": 3,
            "amd": 4, "macular": 4, "degeneration": 4, "_a_": 4,
            "hypertension": 5, "_h_": 5,
            "myopia": 6, "_m_": 6,
            "other": 7, "_o_": 7,
        }

        # Filter by split directory if present
        split_root = root / split
        search_root = split_root if split_root.exists() else root

        samples: List[DatasetSample] = []
        for img_path in sorted(
            list(search_root.rglob("*.jpg"))
            + list(search_root.rglob("*.jpeg"))
            + list(search_root.rglob("*.png"))
        ):
            path_lower = str(img_path).lower()
            lbl = next(
                (v for k, v in class_keywords.items() if k in path_lower),
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
                "Run: eyehub download --datasets aod"
            )
        return samples


# ---------------------------------------------------------------------------
# ToxoFundus: Ocular Toxoplasmosis Fundus Images (Kaggle)
# ---------------------------------------------------------------------------

class ToxoFundusDataset(EyeDataHubDataset):
    """
    ToxoFundus: Ocular Toxoplasmosis Fundus Image Dataset.

    Fundus photographs for binary classification of active vs. inactive
    ocular toxoplasmosis lesions, including normal controls.

    Kaggle: https://www.kaggle.com/datasets/nafin59/ocular-toxoplasmosis-fundus-images-dataset
    """

    _SUBDIR = "toxofundus"
    _KAGGLE_SLUG = "nafin59/ocular-toxoplasmosis-fundus-images-dataset"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="toxofundus",
            full_name="ToxoFundus: Ocular Toxoplasmosis Fundus Dataset",
            description=(
                "Fundus photographs for ocular toxoplasmosis detection: "
                "active toxoplasmosis, inactive (scarred) lesions, and normal. "
                "~412 images total (adult + pediatric cases)."
            ),
            modality="fundus",
            tasks=["classification"],
            num_samples=412,
            splits=["train", "test"],
            classes=["Normal", "Active Toxoplasmosis", "Inactive Toxoplasmosis"],
            num_classes=3,
            download_type="kaggle",
            download_url="https://www.kaggle.com/datasets/nafin59/ocular-toxoplasmosis-fundus-images-dataset",
            license="CC BY 4.0",
            citation=(
                "Nafisi & Sadri, 'ToxoFundus: Ocular Toxoplasmosis Fundus Image Dataset', "
                "Data in Brief 2023. "
                "Zenodo: https://zenodo.org/records/5156953 — "
                "Kaggle: https://www.kaggle.com/datasets/nafin59/ocular-toxoplasmosis-fundus-images-dataset"
            ),
            tags=["toxoplasmosis", "fundus", "kaggle", "classification", "infection"],
            size_gb=0.2,
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
            download_kaggle(self._KAGGLE_SLUG, dest, is_competition=False)
        except Exception:
            print_manual_download_instructions(
                "ToxoFundus",
                "https://www.kaggle.com/datasets/nafin59/ocular-toxoplasmosis-fundus-images-dataset",
                dest,
            )
            raise

    def load(
        self, data_dir: Union[str, Path], split: str = "train"
    ) -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR
        class_map = {
            "normal": 0, "healthy": 0,
            "active": 1,
            "inactive": 2, "scar": 2, "healed": 2,
        }

        split_root = root / split
        search_root = split_root if split_root.exists() else root

        samples = []
        for img_path in sorted(
            list(search_root.rglob("*.jpg"))
            + list(search_root.rglob("*.jpeg"))
            + list(search_root.rglob("*.png"))
        ):
            path_lower = str(img_path).lower()
            lbl = next(
                (v for k, v in class_map.items() if k in path_lower),
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
                "Run: eyehub download --datasets toxofundus"
            )
        return samples


# ---------------------------------------------------------------------------
# FARFUM-ROP: Retinopathy of Prematurity (Figshare collection 6721269 v2)
# ---------------------------------------------------------------------------

ROP_CLASSES = [
    "Normal",
    "Pre-Plus",
    "Plus",
]


class FARFUMROPDataset(EyeDataHubDataset):
    """
    FARFUM-ROP: Fundus Annotation Repository for Retinopathy of Prematurity.

    1,533 wide-field fundus images from 68 preterm infants (<2000 g,
    <34 weeks) collected in Iran (April 2016–May 2019). Annotated by
    5 expert ophthalmologists for plus disease assessment: Normal, Pre-Plus,
    and Plus. Available via Figshare collection 6721269 version 2.

    Reference: Scientific Data 2024
    Figshare: https://doi.org/10.6084/m9.figshare.c.6721269
    """

    _SUBDIR = "farfum_rop"
    # Figshare collections require fetching article IDs from the collection
    # The article IDs are fetched via the Figshare collections API
    _FIGSHARE_COLLECTION_ID = "6721269"
    _FIGSHARE_COLLECTION_VERSION = 2

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="farfum_rop",
            full_name="FARFUM-ROP: Fundus Annotation Repository for Retinopathy of Prematurity",
            description=(
                "Wide-field fundus images from premature infants for ROP staging "
                "(Stages 1–5 + Plus Disease). Expert-annotated for AI-assisted "
                "ROP diagnosis and screening."
            ),
            modality="fundus",
            tasks=["classification"],
            num_samples=1533,
            splits=["train", "test"],
            classes=ROP_CLASSES,
            num_classes=3,
            download_type="figshare",
            download_url="https://doi.org/10.6084/m9.figshare.c.6721269",
            license="CC BY 4.0",
            citation=(
                "Riazi-Esfahani H et al., 'FARFUM-RoP: A dataset for machine "
                "learning-based plus disease diagnosis in retinopathy of prematurity', "
                "Scientific Data 2024. "
                "https://doi.org/10.6084/m9.figshare.c.6721269"
            ),
            tags=["rop", "fundus", "figshare", "classification", "pediatric"],
            size_gb=1.0,
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return (
            len(list(root.glob("**/*.jpg"))) > 20
            or len(list(root.glob("**/*.png"))) > 20
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        import requests
        dest = Path(data_dir) / self._SUBDIR
        dest.mkdir(parents=True, exist_ok=True)

        try:
            # Fetch article IDs from the Figshare collections API
            coll_url = (
                f"https://api.figshare.com/v2/collections/"
                f"{self._FIGSHARE_COLLECTION_ID}/articles"
                f"?version={self._FIGSHARE_COLLECTION_VERSION}&page_size=100"
            )
            resp = requests.get(coll_url, timeout=30)
            resp.raise_for_status()
            articles = resp.json()
            if not articles:
                raise RuntimeError("Empty article list from Figshare collection API")
            for article in articles:
                article_id = article.get("id")
                if article_id:
                    download_figshare(str(article_id), dest)
            # Extract any archives
            for archive in list(dest.glob("*.zip")) + list(dest.glob("*.tar*")):
                extract_archive(archive, dest)
        except Exception:
            print_manual_download_instructions(
                "FARFUM-ROP",
                "https://doi.org/10.6084/m9.figshare.c.6721269",
                dest,
                extra_notes=(
                    "Visit the Figshare collection page and download each article.\n"
                    f"Extract into: {dest}"
                ),
            )
            raise

    def load(
        self, data_dir: Union[str, Path], split: str = "train"
    ) -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR
        stage_kw = {
            "normal": 0, "healthy": 0,
            "pre-plus": 1, "pre_plus": 1, "preplus": 1,
            "plus": 2,
        }

        # CSV annotation
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
                    kw in c.lower() for kw in ("label", "stage", "class", "rop")
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

        # Directory/filename-based label inference
        samples = []
        for img_path in sorted(
            list(root.rglob("*.jpg"))
            + list(root.rglob("*.jpeg"))
            + list(root.rglob("*.png"))
        ):
            path_lower = str(img_path).lower()
            lbl = next(
                (v for k, v in stage_kw.items() if k in path_lower),
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
                "Run: eyehub download --datasets farfum_rop"
            )
        return samples
