"""Glaucoma detection/segmentation datasets: REFUGE2018, RIM-ONE, DRISHTI-GS, G1020, ORIGA, Harvard."""
from __future__ import annotations

from pathlib import Path
from typing import List, Union

import pandas as pd

from eyedatahub.core.dataset import DatasetInfo, DatasetSample, EyeDataHubDataset
from eyedatahub.datasets.download_utils import (
    download_dataverse,
    download_figshare,
    download_figshare_private,
    download_gdrive,
    download_gdrive_folder,
    download_kaggle,
    extract_archive,
    print_manual_download_instructions,
)


# ---------------------------------------------------------------------------
# REFUGE 2018
# ---------------------------------------------------------------------------

class REFUGE2018Dataset(EyeDataHubDataset):
    """
    REFUGE 2018: Retinal Fundus Glaucoma Challenge.

    1200 fundus images with glaucoma classification and optic disc/cup
    segmentation masks.
    """

    _SUBDIR = "refuge2018"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="refuge2018",
            full_name="REFUGE 2018: Retinal Fundus Glaucoma Challenge",
            description=(
                "1200 fundus images: 400 train, 400 val, 400 test. "
                "Labels: glaucoma/non-glaucoma + optic disc/cup segmentation."
            ),
            modality="fundus",
            tasks=["classification", "segmentation"],
            num_samples=1200,
            splits=["train", "val", "test"],
            classes=["Non-glaucoma", "Glaucoma"],
            num_classes=2,
            download_type="manual",
            download_url="https://refuge.grand-challenge.org/",
            license="Research only — requires Grand Challenge registration",
            citation=(
                "Orlando et al., 'REFUGE challenge: A unified framework for "
                "evaluating automated methods for glaucoma assessment from fundus "
                "photographs', MedIA 2020."
            ),
            tags=["glaucoma", "classification", "segmentation", "fundus"],
            size_gb=2.5,
            notes="Requires Grand Challenge account and challenge participation.",
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return len(list(root.glob("**/*.jpg"))) > 100

    def download(self, data_dir: Union[str, Path]) -> None:
        root = Path(data_dir) / self._SUBDIR
        print_manual_download_instructions(
            "REFUGE 2018",
            "https://refuge.grand-challenge.org/",
            root,
            extra_notes=(
                "Register on Grand Challenge and join the REFUGE challenge.\n"
                "Download and extract training, validation, and test sets.\n"
                "Expected structure:\n"
                "  refuge2018/Training400/Images/*.jpg\n"
                "  refuge2018/Training400/Disc_Cup_Masks/*.bmp\n"
                "  refuge2018/Training400/Glaucoma_label_training.xlsx\n"
                "  refuge2018/REFUGE-Validation400/Images/*.jpg\n"
                "  refuge2018/REFUGE-Test400/Images/*.jpg"
            ),
        )
        raise RuntimeError("REFUGE 2018 requires manual download.")

    def load(
        self, data_dir: Union[str, Path], split: str = "test"
    ) -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR

        split_map = {
            "train": "Training400",
            "val": "REFUGE-Validation400",
            "test": "REFUGE-Test400",
        }
        split_dir = root / split_map.get(split, split)
        img_dir = split_dir / "Images"
        if not img_dir.exists():
            img_dir = split_dir / "images"
        if not img_dir.exists():
            raise FileNotFoundError(f"REFUGE image directory not found: {split_dir}")

        # Load labels from Excel/CSV if available
        label_map: dict = {}
        label_files = (
            list(split_dir.glob("*.xlsx"))
            + list(split_dir.glob("*.csv"))
            + list(root.glob(f"*{split}*.xlsx"))
            + list(root.glob(f"*{split}*.csv"))
        )
        if label_files:
            try:
                if label_files[0].suffix == ".xlsx":
                    df = pd.read_excel(label_files[0])
                else:
                    df = pd.read_csv(label_files[0])
                id_col = df.columns[0]
                lbl_col = df.columns[1]
                for _, row in df.iterrows():
                    label_map[str(row[id_col])] = int(row[lbl_col])
            except Exception:
                pass

        mask_dir = split_dir / "Disc_Cup_Masks"
        if not mask_dir.exists():
            mask_dir = split_dir / "masks"

        samples = []
        for img_path in sorted(img_dir.glob("*.jpg")) + sorted(img_dir.glob("*.png")):
            stem = img_path.stem
            label = label_map.get(img_path.name, label_map.get(stem, 0))

            mask_candidates = list(mask_dir.glob(f"{stem}*.bmp")) + list(
                mask_dir.glob(f"{stem}*.png")
            ) if mask_dir.exists() else []
            mask_path = str(mask_candidates[0]) if mask_candidates else ""

            samples.append(
                DatasetSample(
                    image_path=str(img_path),
                    label=label,
                    sample_id=stem,
                    metadata={"split": split, "mask_path": mask_path},
                )
            )
        return samples


# ---------------------------------------------------------------------------
# RIM-ONE DL
# ---------------------------------------------------------------------------

class RIMONEDLDataset(EyeDataHubDataset):
    """
    RIM-ONE DL: Retinal Image Analysis for glaucoma detection (deep learning split).

    485 fundus images: 313 normal, 172 glaucoma (with optic disc crops).

    Kaggle: https://www.kaggle.com/datasets/orvile/rim-one-retinal-dataset-for-assessing-glaucoma
    """

    _SUBDIR = "rimone_dl"
    # Primary mirror (full RIM-ONE retinal dataset)
    _KAGGLE_SLUG = "orvile/rim-one-retinal-dataset-for-assessing-glaucoma"
    # Fallback: original DL-split mirror
    _KAGGLE_SLUG_ALT = "andreabcolombo/rimone-dl"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="rimone_dl",
            full_name="RIM-ONE DL",
            description=(
                "485 fundus images (313 normal, 172 glaucoma) with optic disc "
                "region of interest crops for deep learning."
            ),
            modality="fundus",
            tasks=["classification"],
            num_samples=485,
            splits=["train", "test"],
            classes=["Normal", "Glaucoma"],
            num_classes=2,
            download_type="kaggle",
            download_url=f"https://www.kaggle.com/datasets/{self._KAGGLE_SLUG}",
            license="CC BY 4.0",
            citation=(
                "Fumero et al., 'RIM-ONE DL: A Unified Retinal Image Database "
                "for Assessing Glaucoma Using Deep Learning', Intl. Image "
                "Analysis and Ophthalmology 2020."
            ),
            tags=["glaucoma", "classification", "fundus"],
            size_gb=0.5,
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return len(list(root.glob("**/*.png"))) > 100 or len(list(root.glob("**/*.jpg"))) > 100

    def download(self, data_dir: Union[str, Path]) -> None:
        dest = Path(data_dir) / self._SUBDIR
        for slug in (self._KAGGLE_SLUG, self._KAGGLE_SLUG_ALT):
            try:
                download_kaggle(slug, dest, is_competition=False)
                return
            except Exception:
                continue
        print_manual_download_instructions(
            "RIM-ONE",
            f"https://www.kaggle.com/datasets/{self._KAGGLE_SLUG}",
            dest,
            extra_notes=(
                "Kaggle credentials required (KAGGLE_USERNAME + KAGGLE_KEY in .env).\n"
                "Alternative: http://rimone.es/\n"
                "Expected layout:\n"
                "  rimone_dl/train/Normal/\n"
                "  rimone_dl/train/Glaucoma/\n"
                "  rimone_dl/test/Normal/\n"
                "  rimone_dl/test/Glaucoma/"
            ),
        )
        raise RuntimeError("RIM-ONE download failed via Kaggle.")

    def load(
        self, data_dir: Union[str, Path], split: str = "test"
    ) -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR
        split_dir = root / split
        if not split_dir.exists():
            # Try flat structure
            split_dir = root

        class_map = {"normal": 0, "healthy": 0, "glaucoma": 1, "glaucomatous": 1}
        samples = []

        for cls_dir in sorted(split_dir.iterdir()):
            if not cls_dir.is_dir():
                continue
            label = class_map.get(cls_dir.name.lower(), -1)
            if label == -1:
                continue
            for img_path in sorted(cls_dir.glob("*.png")) + sorted(cls_dir.glob("*.jpg")):
                samples.append(
                    DatasetSample(
                        image_path=str(img_path),
                        label=label,
                        sample_id=img_path.stem,
                        metadata={"split": split, "class_name": cls_dir.name},
                    )
                )
        return samples


# ---------------------------------------------------------------------------
# DRISHTI-GS
# ---------------------------------------------------------------------------

class DRISHTIGSDataset(EyeDataHubDataset):
    """
    DRISHTI-GS: Optic Disc and Cup Segmentation Dataset.

    101 fundus images with optic disc and cup segmentation masks.

    Kaggle: https://www.kaggle.com/datasets/lokeshsaipureddi/drishtigs-retina-dataset-for-onh-segmentation
    """

    _SUBDIR = "drishti_gs"
    _KAGGLE_SLUG = "lokeshsaipureddi/drishtigs-retina-dataset-for-onh-segmentation"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="drishti_gs",
            full_name="DRISHTI-GS: Optic Disc and Cup Segmentation",
            description=(
                "101 fundus images annotated for optic disc and cup segmentation "
                "by 4 clinicians. Train/test: 50/51."
            ),
            modality="fundus",
            tasks=["segmentation"],
            num_samples=101,
            splits=["train", "test"],
            image_size=(2896, 1944),
            download_type="kaggle",
            download_url=f"https://www.kaggle.com/datasets/{self._KAGGLE_SLUG}",
            license="Research only",
            citation=(
                "Sivaswamy et al., 'Drishti-GS: Retinal image dataset for optic "
                "nerve head (ONH) segmentation', ISBI 2014."
            ),
            tags=["glaucoma", "segmentation", "optic_disc", "fundus"],
            size_gb=0.8,
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return len(list(root.glob("**/*.png"))) > 50

    def download(self, data_dir: Union[str, Path]) -> None:
        dest = Path(data_dir) / self._SUBDIR
        try:
            download_kaggle(self._KAGGLE_SLUG, dest, is_competition=False)
        except Exception:
            print_manual_download_instructions(
                "DRISHTI-GS",
                f"https://www.kaggle.com/datasets/{self._KAGGLE_SLUG}",
                dest,
                extra_notes=(
                    "Kaggle credentials required (KAGGLE_USERNAME + KAGGLE_KEY in .env).\n"
                    "Alternative: https://cvit.iiit.ac.in/projects/mip/drishti-gs/\n"
                    "Expected structure:\n"
                    "  drishti_gs/Drishti_gs1/Training/Images/*.png\n"
                    "  drishti_gs/Drishti_gs1/Training/GT/ODsegmentations/\n"
                    "  drishti_gs/Drishti_gs1/Test/Images/*.png\n"
                    "  drishti_gs/Drishti_gs1/Test/GT/ODsegmentations/"
                ),
            )
            raise

    def load(
        self, data_dir: Union[str, Path], split: str = "test"
    ) -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR

        split_map = {"train": "Training", "test": "Test"}
        split_name = split_map.get(split, split)

        base = root / "Drishti_gs1" / split_name
        if not base.exists():
            base = root / split_name
        if not base.exists():
            raise FileNotFoundError(f"DRISHTI-GS {split} directory not found: {root}")

        img_dir = base / "Images"
        seg_dir = base / "GT" / "ODsegmentations"

        samples = []
        for img_path in sorted(img_dir.glob("*.png")):
            stem = img_path.stem
            mask_candidates = list(seg_dir.glob(f"{stem}*.png"))
            mask_path = str(mask_candidates[0]) if mask_candidates else ""
            samples.append(
                DatasetSample(
                    image_path=str(img_path),
                    label=mask_path,
                    sample_id=stem,
                    metadata={"split": split},
                )
            )
        return samples


# ---------------------------------------------------------------------------
# G1020
# ---------------------------------------------------------------------------

class G1020Dataset(EyeDataHubDataset):
    """
    G1020: A Benchmark Retinal Fundus Image Dataset for Glaucoma.

    1020 high-resolution fundus images with glaucoma labels and optic disc
    bounding box annotations.
    """

    _SUBDIR = "g1020"
    _KAGGLE_SLUG = "arnavjain1/glaucoma-datasets"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="g1020",
            full_name="G1020: Glaucoma Benchmark Fundus Dataset",
            description=(
                "1020 fundus images with binary glaucoma labels (697 normal, "
                "323 glaucoma), plus optic disc/cup annotations."
            ),
            modality="fundus",
            tasks=["classification"],
            num_samples=1020,
            splits=["all"],
            classes=["Non-glaucoma", "Glaucoma"],
            num_classes=2,
            download_type="kaggle",
            download_url="https://arxiv.org/abs/2006.09158",
            license="CC BY 4.0",
            citation=(
                "Bajwa et al., 'G1020: A Benchmark Retinal Fundus Image Dataset "
                "for Computer-Aided Glaucoma Detection', arXiv 2020."
            ),
            tags=["glaucoma", "classification", "fundus"],
            size_gb=2.0,
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return len(list(root.glob("**/*.jpg"))) > 100 or len(list(root.glob("**/*.png"))) > 100

    def download(self, data_dir: Union[str, Path]) -> None:
        dest = Path(data_dir) / self._SUBDIR
        try:
            download_kaggle(self._KAGGLE_SLUG, dest, is_competition=False)
        except Exception:
            print_manual_download_instructions(
                "G1020",
                "https://www.kaggle.com/datasets/arnavjain1/glaucoma-datasets",
                dest,
                extra_notes=(
                    "Alternatively, contact the authors via the paper:\n"
                    "https://arxiv.org/abs/2006.09158\n"
                    "Expected layout:\n"
                    "  g1020/images/*.jpg\n"
                    "  g1020/G1020.csv (columns: imageID, binaryLabels)"
                ),
            )
            raise

    def load(
        self, data_dir: Union[str, Path], split: str = "all"
    ) -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR

        csv_candidates = list(root.glob("*.csv")) + list(root.glob("**/*.csv"))
        if not csv_candidates:
            raise FileNotFoundError(f"No annotation CSV found in {root}.")

        df = pd.read_csv(csv_candidates[0])
        id_col = next(
            (c for c in df.columns if "image" in c.lower() or "id" in c.lower()),
            df.columns[0],
        )
        lbl_col = next(
            (c for c in df.columns if "label" in c.lower() or "glaucoma" in c.lower()),
            df.columns[-1],
        )

        img_dir = root / "images" if (root / "images").exists() else root

        samples = []
        for _, row in df.iterrows():
            img_id = str(row[id_col])
            label = int(row[lbl_col])
            for ext in [".jpg", ".png", ".jpeg"]:
                img_path = img_dir / f"{img_id}{ext}"
                if img_path.exists():
                    samples.append(
                        DatasetSample(
                            image_path=str(img_path),
                            label=label,
                            sample_id=img_id,
                            metadata={"split": split},
                        )
                    )
                    break
        return samples


# ---------------------------------------------------------------------------
# AIROGS
# ---------------------------------------------------------------------------

class AIROGSDataset(EyeDataHubDataset):
    """
    AIROGS: AI for Robust Glaucoma Screening (Rotterdam EyePACS).

    ~113,893 color fundus images from ~60,357 subjects across ~500 sites.
    Training set available on Zenodo; labels: referable glaucoma / no referable
    glaucoma / ungradable.
    """

    _SUBDIR = "airogs"
    _ZENODO_URL = "https://zenodo.org/records/5793241"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="airogs",
            full_name="AIROGS: AI for Robust Glaucoma Screening",
            description=(
                "~113,893 color fundus images labelled as referable glaucoma "
                "(RG), no referable glaucoma (NRG), or ungradable. "
                "Large-scale, multi-ethnic, multi-site screening dataset."
            ),
            modality="fundus",
            tasks=["classification"],
            num_samples=113893,
            splits=["train", "test"],
            classes=["NRG", "RG"],
            num_classes=2,
            download_type="direct",
            download_url=self._ZENODO_URL,
            license="CC BY-NC-ND 4.0",
            citation=(
                "De Vente et al., 'AIROGS: Artificial Intelligence for Robust "
                "Glaucoma Screening Challenge', TMI 2023."
            ),
            tags=["glaucoma", "classification", "fundus", "screening", "large_scale"],
            size_gb=40.0,
            notes=(
                "Training set (~101k images) on Zenodo. Test set distributed "
                "through Grand Challenge. Requires free account for Grand Challenge."
            ),
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return len(list(root.glob("**/*.jpg"))) > 1000 or len(list(root.glob("**/*.png"))) > 1000

    def download(self, data_dir: Union[str, Path]) -> None:
        root = Path(data_dir) / self._SUBDIR
        print_manual_download_instructions(
            "AIROGS",
            self._ZENODO_URL,
            root,
            extra_notes=(
                "Training set (~40 GB) is on Zenodo:\n"
                "  https://zenodo.org/records/5793241\n"
                "Test set and full challenge data via:\n"
                "  https://airogs.grand-challenge.org/\n"
                "After downloading, place images and labels.csv under:\n"
                "  airogs/train/images/*.jpg\n"
                "  airogs/train/labels.csv  (columns: image_id, class)"
            ),
        )
        raise RuntimeError("AIROGS requires manual download (~40 GB).")

    def load(self, data_dir: Union[str, Path], split: str = "train") -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR
        split_dir = root / split
        if not split_dir.exists():
            split_dir = root

        csv_candidates = list(split_dir.glob("*.csv")) + list(root.glob("*.csv"))
        if not csv_candidates:
            raise FileNotFoundError(f"No annotation CSV found in {root}.")

        df = pd.read_csv(csv_candidates[0])
        id_col = next((c for c in df.columns if "image" in c.lower() or "id" in c.lower()), df.columns[0])
        lbl_col = next((c for c in df.columns if "class" in c.lower() or "label" in c.lower()), df.columns[-1])
        class_map = {"nrg": 0, "rg": 1, "no referable glaucoma": 0, "referable glaucoma": 1}

        img_dir = split_dir / "images" if (split_dir / "images").exists() else split_dir
        samples = []
        for _, row in df.iterrows():
            img_id = str(row[id_col])
            label = class_map.get(str(row[lbl_col]).lower(), 0)
            for ext in [".jpg", ".jpeg", ".png"]:
                img_path = img_dir / f"{img_id}{ext}"
                if img_path.exists():
                    samples.append(DatasetSample(
                        image_path=str(img_path),
                        label=label,
                        sample_id=img_id,
                        metadata={"split": split, "class_str": str(row[lbl_col])},
                    ))
                    break
        return samples


# ---------------------------------------------------------------------------
# PAPILA
# ---------------------------------------------------------------------------

class PAPILADataset(EyeDataHubDataset):
    """
    PAPILA: Glaucoma dataset with fundus images and clinical data.

    488 fundus images (both eyes from 244 patients) with optic disc/cup
    segmentation masks, glaucoma stage labels, and clinical metadata.
    """

    _SUBDIR = "papila"
    _ZENODO_URL = "https://zenodo.org/records/6379970"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="papila",
            full_name="PAPILA: Glaucoma Fundus Dataset with Clinical Data",
            description=(
                "488 fundus images from 244 patients (both eyes). Expert OD/OC "
                "segmentation, glaucoma stage, IOP, and clinical metadata."
            ),
            modality="fundus",
            tasks=["classification", "segmentation"],
            num_samples=488,
            splits=["all"],
            classes=["Healthy", "Glaucoma suspect", "Glaucoma"],
            num_classes=3,
            download_type="direct",
            download_url=self._ZENODO_URL,
            license="CC BY 4.0",
            citation=(
                "Kovalyk et al., 'PAPILA: Dataset with fundus images and clinical "
                "data of both eyes of the same patient for glaucoma assessment', "
                "Scientific Data 2022."
            ),
            tags=["glaucoma", "classification", "segmentation", "fundus", "clinical"],
            size_gb=0.4,
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return len(list(root.glob("**/*.jpg"))) > 50 or len(list(root.glob("**/*.png"))) > 50

    def download(self, data_dir: Union[str, Path]) -> None:
        root = Path(data_dir) / self._SUBDIR
        root.mkdir(parents=True, exist_ok=True)
        print_manual_download_instructions(
            "PAPILA",
            self._ZENODO_URL,
            root,
            extra_notes=(
                "Download from Zenodo (free, no login required):\n"
                "  https://zenodo.org/records/6379970\n"
                "Expected structure:\n"
                "  papila/FundusImages/RET*.jpg\n"
                "  papila/SegmentationAnnotations/RET*_OD.png\n"
                "  papila/ClinicalData/patient_data.xlsx"
            ),
        )
        raise RuntimeError("PAPILA requires manual download from Zenodo.")

    def load(self, data_dir: Union[str, Path], split: str = "all") -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR

        img_dirs = [root / "FundusImages", root / "images", root]
        img_dir = next((d for d in img_dirs if d.exists()), root)

        seg_dir = root / "SegmentationAnnotations" if (root / "SegmentationAnnotations").exists() else None

        # Try to load clinical labels
        label_map = {}
        for csv_path in list(root.glob("**/*.xlsx")) + list(root.glob("**/*.csv")):
            try:
                df = pd.read_excel(csv_path) if csv_path.suffix == ".xlsx" else pd.read_csv(csv_path)
                for col in df.columns:
                    if "diagnosis" in col.lower() or "glaucoma" in col.lower() or "label" in col.lower():
                        for _, row in df.iterrows():
                            key = str(row[df.columns[0]])
                            label_map[key] = int(row[col]) if str(row[col]).isdigit() else 0
                break
            except Exception:
                pass

        samples = []
        for img_path in sorted(img_dir.glob("*.jpg")) + sorted(img_dir.glob("*.png")):
            stem = img_path.stem
            label = label_map.get(stem, label_map.get(img_path.name, 0))
            mask_path = ""
            if seg_dir:
                candidates = list(seg_dir.glob(f"{stem}_OD*.png")) + list(seg_dir.glob(f"{stem}*.png"))
                mask_path = str(candidates[0]) if candidates else ""
            samples.append(DatasetSample(
                image_path=str(img_path),
                label=label,
                sample_id=stem,
                metadata={"split": split, "mask_path": mask_path},
            ))
        return samples


# ---------------------------------------------------------------------------
# ORIGA
# ---------------------------------------------------------------------------

class ORIGADataset(EyeDataHubDataset):
    """
    ORIGA: Retinal Fundus Glaucoma Image Dataset.

    650 fundus images (482 normal, 168 glaucoma) with optic disc and cup
    segmentation masks manually annotated by trained professionals.

    Figshare: https://doi.org/10.6084/m9.figshare.24549217
    License:  CC BY 4.0
    """

    _SUBDIR = "origa"
    _FIGSHARE_ARTICLE_ID = "24549217"
    _FIGSHARE_FILE_ID = "43119880"
    _FIGSHARE_URL = "https://doi.org/10.6084/m9.figshare.24549217"

    CLASSES = ["Normal", "Glaucoma"]

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="origa",
            full_name="ORIGA — Retinal Fundus Glaucoma Image Dataset",
            description=(
                "650 fundus images (482 normal, 168 glaucoma) with expert "
                "optic disc/cup segmentation masks."
            ),
            modality="fundus",
            tasks=["classification", "segmentation"],
            num_samples=650,
            splits=["all"],
            classes=self.CLASSES,
            num_classes=2,
            download_type="figshare",
            download_url=self._FIGSHARE_URL,
            license="CC BY 4.0",
            citation=(
                "Zhang Z. et al., 'ORIGA-light: An online retinal fundus image "
                "database for glaucoma analysis and research', EMBC 2010."
            ),
            tags=["glaucoma", "classification", "segmentation", "optic_disc", "fundus"],
            size_gb=0.6,
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return root.exists() and (
            len(list(root.rglob("*.jpg"))) + len(list(root.rglob("*.png"))) > 100
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        dest = Path(data_dir) / self._SUBDIR
        dest.mkdir(parents=True, exist_ok=True)
        try:
            download_figshare(
                self._FIGSHARE_ARTICLE_ID,
                dest,
                filename=None,
                extract=True,
            )
        except Exception as e:
            print_manual_download_instructions(
                "ORIGA — Retinal Fundus Glaucoma Dataset",
                self._FIGSHARE_URL,
                dest,
                extra_notes=(
                    f"Error: {e}\n\n"
                    "Direct Figshare download:\n"
                    f"  {self._FIGSHARE_URL}\n"
                    "Expected layout after extraction:\n"
                    "  origa/images/*.jpg (or *.png)\n"
                    "  origa/masks/ (segmentation masks)"
                ),
            )
            raise

    def load(self, data_dir: Union[str, Path], split: str = "all") -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR

        # Locate images
        img_dirs = [root / "images", root / "Images", root / "fundus", root]
        img_dir = next((d for d in img_dirs if d.exists() and any(d.glob("*.jpg"))), root)

        images = sorted(img_dir.rglob("*.jpg")) + sorted(img_dir.rglob("*.png"))
        images = [p for p in images if "mask" not in p.name.lower() and "seg" not in p.name.lower()]

        # Locate masks (optic disc / cup)
        mask_dir = next(
            (root / d for d in ("masks", "Masks", "OD_masks", "segmentation") if (root / d).exists()),
            None,
        )

        # Load labels from CSV/Excel if available
        label_map: dict = {}
        for label_file in list(root.rglob("*.csv")) + list(root.rglob("*.xlsx")):
            try:
                df = pd.read_excel(label_file) if label_file.suffix == ".xlsx" else pd.read_csv(label_file)
                for _, row in df.iterrows():
                    key = str(row.iloc[0]).replace(".jpg", "").replace(".png", "")
                    for col in df.columns[1:]:
                        val = str(row[col]).lower()
                        if "glau" in val or val in ("1", "g", "true"):
                            label_map[key] = 1
                            break
                        elif "norm" in val or val in ("0", "n", "false"):
                            label_map[key] = 0
                            break
                if label_map:
                    break
            except Exception:
                pass

        samples = []
        for img_path in images:
            stem = img_path.stem
            label = label_map.get(stem, label_map.get(img_path.name, None))
            mask_path = ""
            if mask_dir:
                cands = list(mask_dir.glob(f"{stem}*.png")) + list(mask_dir.glob(f"{stem}*.bmp"))
                mask_path = str(cands[0]) if cands else ""
            samples.append(DatasetSample(
                image_path=str(img_path),
                label=label,
                sample_id=stem,
                metadata={"mask_path": mask_path},
            ))
        return samples


# ---------------------------------------------------------------------------
# Harvard Glaucoma Fundus
# ---------------------------------------------------------------------------

class HarvardGlaucomaFundusDataset(EyeDataHubDataset):
    """
    Harvard Glaucoma Fundus Image Dataset.

    ~1000 fundus images for glaucoma detection from Harvard Medical School
    / Massachusetts Eye and Ear.

    Harvard Dataverse: doi:10.7910/DVN/1YRRAC
    License: CC0 (Public Domain)
    """

    _SUBDIR = "harvard_glaucoma"
    _PERSISTENT_ID = "doi:10.7910/DVN/1YRRAC"
    _DATAVERSE_URL = "https://doi.org/10.7910/DVN/1YRRAC"

    CLASSES = ["Non-glaucoma", "Glaucoma"]

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="harvard_glaucoma",
            full_name="Harvard Glaucoma Fundus Image Dataset",
            description=(
                "Fundus images for glaucoma detection from Harvard Medical "
                "School / Mass Eye and Ear. Binary glaucoma classification."
            ),
            modality="fundus",
            tasks=["classification"],
            num_samples=1000,
            splits=["all"],
            classes=self.CLASSES,
            num_classes=2,
            download_type="direct",
            download_url=self._DATAVERSE_URL,
            license="CC0 1.0 (Public Domain)",
            citation=(
                "Luo X. et al., 'Harvard Glaucoma Detection and Progression "
                "Dataset', Harvard Dataverse, doi:10.7910/DVN/1YRRAC, 2023."
            ),
            tags=["glaucoma", "classification", "fundus", "harvard"],
            size_gb=1.5,
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return root.exists() and (
            len(list(root.rglob("*.jpg"))) + len(list(root.rglob("*.png"))) > 100
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        dest = Path(data_dir) / self._SUBDIR
        dest.mkdir(parents=True, exist_ok=True)
        try:
            download_dataverse(self._PERSISTENT_ID, dest)
        except Exception as e:
            print_manual_download_instructions(
                "Harvard Glaucoma Fundus Dataset",
                self._DATAVERSE_URL,
                dest,
                extra_notes=(
                    f"Error: {e}\n\n"
                    "Visit the Harvard Dataverse page and download manually.\n"
                    "Optional: set DATAVERSE_TOKEN in .env for authenticated access."
                ),
            )
            raise

    def load(self, data_dir: Union[str, Path], split: str = "all") -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR

        images = sorted(root.rglob("*.jpg")) + sorted(root.rglob("*.png"))
        images = [p for p in images if "mask" not in p.name.lower()]

        label_map: dict = {}
        for label_file in list(root.rglob("*.csv")) + list(root.rglob("*.xlsx")):
            try:
                df = pd.read_excel(label_file) if label_file.suffix == ".xlsx" else pd.read_csv(label_file)
                for _, row in df.iterrows():
                    key = str(row.iloc[0]).replace(".jpg", "").replace(".png", "")
                    for col in df.columns[1:]:
                        val = str(row[col]).lower().strip()
                        if val in ("1", "glaucoma", "g", "true", "yes"):
                            label_map[key] = 1
                            break
                        elif val in ("0", "normal", "n", "false", "no"):
                            label_map[key] = 0
                            break
                if label_map:
                    break
            except Exception:
                pass

        # Infer labels from directory structure if no CSV
        if not label_map:
            class_map = {"glaucoma": 1, "glaucomatous": 1, "normal": 0, "non-glaucoma": 0, "healthy": 0}
            for img_path in images:
                for part in img_path.parts:
                    if part.lower() in class_map:
                        label_map[img_path.stem] = class_map[part.lower()]
                        break

        return [
            DatasetSample(
                image_path=str(p),
                label=label_map.get(p.stem, label_map.get(p.name, None)),
                sample_id=p.stem,
            )
            for p in images
        ]


# ---------------------------------------------------------------------------
# ACRIMA (Figshare private share c2d31f850af14c5b5232)
# ---------------------------------------------------------------------------

class ACRIMADataset(EyeDataHubDataset):
    """
    ACRIMA: glaucomatous and normal optic disc fundus image database.

    705 optic disc-centred fundus photographs: 396 normal and 309 glaucoma,
    from Hospital Clinico San Carlos, Madrid. Annotated by expert glaucoma
    specialists. Images are 2048 x 1536 px colour fundus crops.

    Figshare private share: https://figshare.com/s/c2d31f850af14c5b5232
    """

    _SUBDIR = "acrima"
    _FIGSHARE_TOKEN = "c2d31f850af14c5b5232"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="acrima",
            full_name="ACRIMA: Glaucoma Optic Disc Fundus Database",
            description=(
                "705 optic disc-centred fundus photographs (396 normal + 309 "
                "glaucoma) from Hospital Clinico San Carlos. Expert-annotated "
                "binary glaucoma classification."
            ),
            modality="fundus",
            tasks=["classification"],
            num_samples=705,
            splits=["train"],
            classes=["Normal", "Glaucoma"],
            num_classes=2,
            download_type="figshare",
            download_url="https://figshare.com/s/c2d31f850af14c5b5232",
            license="CC BY 4.0",
            citation=(
                "Diaz-Pinto et al., 'Retinal Image Synthesis and Semi-Supervised "
                "Learning for Glaucoma Assessment', IEEE TMI 2019. "
                "Data: https://figshare.com/s/c2d31f850af14c5b5232"
            ),
            tags=["glaucoma", "fundus", "figshare", "classification", "optic_disc"],
            size_gb=0.5,
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
            download_figshare_private(self._FIGSHARE_TOKEN, dest)
        except Exception:
            print_manual_download_instructions(
                "ACRIMA",
                f"https://figshare.com/s/{self._FIGSHARE_TOKEN}",
                dest,
                extra_notes=(
                    "Visit the Figshare private share and download manually.\n"
                    "Expected structure:\n"
                    "  acrima/Glaucoma/*.jpg\n"
                    "  acrima/Non-Glaucoma/*.jpg"
                ),
            )
            raise

    def load(
        self, data_dir: Union[str, Path], split: str = "train"
    ) -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR
        class_map = {
            "glaucoma": 1, "glaucomatous": 1,
            "non-glaucoma": 0, "normal": 0, "healthy": 0,
        }
        samples = []
        for img_path in sorted(
            list(root.rglob("*.jpg"))
            + list(root.rglob("*.jpeg"))
            + list(root.rglob("*.png"))
        ):
            path_lower = "/".join(img_path.parts).lower()
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
                "Run: eyehub download --datasets acrima"
            )
        return samples


# ---------------------------------------------------------------------------
# BEH Dataset (GDrive file 1YdZm-sioiAbTdBRy4oej1q6tZL8Baft7)
# ---------------------------------------------------------------------------

class BEHDataset(EyeDataHubDataset):
    """
    BEH Glaucoma Dataset (Blood-vessel, optic-disc, and optic-cup segmentation).

    Fundus photographs collected at Bangladesh Eye Hospital (BEH) for
    deep-learning-based glaucoma detection. Binary classification (normal /
    glaucoma) with companion vessel/cup/disc segmentation masks.

    GitHub: https://github.com/mirtanvirislam/Deep-Learning-Based-Glaucoma-Detection-with-Cropped-Optic-Cup-and-Disc-and-Blood-Vessel-Segmentation
    GDrive: https://drive.google.com/file/d/1YdZm-sioiAbTdBRy4oej1q6tZL8Baft7
    """

    _SUBDIR = "beh"
    _GDRIVE_ID = "1YdZm-sioiAbTdBRy4oej1q6tZL8Baft7"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="beh",
            full_name="BEH: Bangladesh Eye Hospital Glaucoma Dataset",
            description=(
                "Fundus photographs from Bangladesh Eye Hospital for glaucoma "
                "detection. Includes optic cup/disc crops and vessel segmentation "
                "masks alongside binary glaucoma/normal labels."
            ),
            modality="fundus",
            tasks=["classification", "segmentation"],
            num_samples=634,
            splits=["train", "test"],
            classes=["Normal", "Glaucoma"],
            num_classes=2,
            download_type="gdrive",
            download_url="https://drive.google.com/file/d/1YdZm-sioiAbTdBRy4oej1q6tZL8Baft7",
            license="Research only",
            citation=(
                "Islam MT et al., 'Deep Learning-Based Glaucoma Detection with "
                "Cropped Optic Cup and Disc and Blood Vessel Segmentation', "
                "IEEE Access 2022. "
                "https://github.com/mirtanvirislam/Deep-Learning-Based-Glaucoma-Detection-with-Cropped-Optic-Cup-and-Disc-and-Blood-Vessel-Segmentation"
            ),
            tags=["glaucoma", "fundus", "gdrive", "classification", "segmentation"],
            size_gb=0.3,
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return (
            len(list(root.glob("**/*.jpg"))) > 10
            or len(list(root.glob("**/*.png"))) > 10
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        dest = Path(data_dir) / self._SUBDIR
        dest.mkdir(parents=True, exist_ok=True)
        archive = dest / "beh.zip"
        try:
            download_gdrive(self._GDRIVE_ID, archive)
            extract_archive(archive, dest)
            archive.unlink(missing_ok=True)
        except Exception:
            print_manual_download_instructions(
                "BEH",
                f"https://drive.google.com/file/d/{self._GDRIVE_ID}",
                dest,
            )
            raise

    def load(
        self, data_dir: Union[str, Path], split: str = "train"
    ) -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR
        class_map = {
            "glaucoma": 1, "g_": 1, "_g/": 1,
            "normal": 0, "n_": 0, "_n/": 0, "non": 0,
        }
        all_imgs = sorted(
            list(root.rglob("*.jpg"))
            + list(root.rglob("*.jpeg"))
            + list(root.rglob("*.png"))
        )
        # Exclude segmentation mask images (typically in a masks/ subdirectory)
        imgs = [p for p in all_imgs if "mask" not in str(p).lower()]

        # Filter by split directory
        split_imgs = [p for p in imgs if split.lower() in str(p).lower()]
        if split_imgs:
            imgs = split_imgs

        if not imgs:
            raise FileNotFoundError(
                f"No images found in {root}. "
                "Run: eyehub download --datasets beh"
            )

        samples = []
        for img_path in imgs:
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
        return samples


# ---------------------------------------------------------------------------
# Harvard GDP: Glaucoma Detection and Progression (GDrive)
# ---------------------------------------------------------------------------

class HarvardGDPDataset(EyeDataHubDataset):
    """
    Harvard GDP: Glaucoma Detection and Progression Dataset.

    1,000 patients with longitudinal OCT RNFLT maps (225×225 px) plus
    visual field measurements and demographics. Provides binary glaucoma
    detection labels and 6 progression forecasting definitions.
    First publicly available glaucoma progression dataset.

    GitHub:  https://github.com/Harvard-Ophthalmology-AI-Lab/Harvard-GDP
    GDrive:  https://drive.google.com/drive/folders/1JMi_HCql113uc9X0DOaMkNfEWfxaDlEz
    """

    _SUBDIR = "harvard_gdp"
    _GDRIVE_FOLDER_ID = "1JMi_HCql113uc9X0DOaMkNfEWfxaDlEz"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="harvard_gdp",
            full_name="Harvard GDP: Glaucoma Detection and Progression Dataset",
            description=(
                "1,000 patients with OCT RNFLT maps (225×225), visual field "
                "measurements, and demographics for glaucoma detection (binary) "
                "and longitudinal progression forecasting (6 definitions). "
                "First public glaucoma progression dataset from Harvard Ophthalmology AI Lab."
            ),
            modality="oct",
            tasks=["classification", "progression"],
            num_samples=1000,
            splits=["train", "val", "test"],
            classes=["Non-Glaucoma", "Glaucoma"],
            num_classes=2,
            download_type="gdrive",
            download_url="https://drive.google.com/drive/folders/1JMi_HCql113uc9X0DOaMkNfEWfxaDlEz",
            license="CC BY-NC-ND 4.0",
            citation=(
                "Luo Z et al., 'Glaucoma Progression Prediction Using Retinal "
                "Thickness via Deep Learning', arXiv 2308.13411, 2023. "
                "https://github.com/Harvard-Ophthalmology-AI-Lab/Harvard-GDP"
            ),
            tags=["glaucoma", "oct", "rnflt", "gdrive", "progression", "longitudinal"],
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
        except Exception:
            print_manual_download_instructions(
                "Harvard GDP",
                f"https://drive.google.com/drive/folders/{self._GDRIVE_FOLDER_ID}",
                dest,
                extra_notes="Requires: pip install gdown",
            )
            raise

    def load(
        self, data_dir: Union[str, Path], split: str = "train"
    ) -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR

        label_map: dict = {}
        for csv_path in list(root.glob("*.csv")) + list(root.glob("**/*.csv")):
            try:
                df = pd.read_csv(csv_path)
                id_col = next(
                    (c for c in df.columns if any(
                        kw in c.lower() for kw in ("image", "file", "id", "name")
                    )), df.columns[0]
                )
                lbl_col = next(
                    (c for c in df.columns if any(
                        kw in c.lower() for kw in ("label", "glaucoma", "class", "grade")
                    )), None
                )
                split_col = next(
                    (c for c in df.columns if "split" in c.lower()), None
                )
                if not lbl_col:
                    continue
                for _, row in df.iterrows():
                    if split_col and str(row[split_col]).lower() != split.lower():
                        continue
                    img_id = str(row[id_col]).strip()
                    raw = str(row[lbl_col]).strip().lower()
                    if raw in ("1", "glaucoma", "true", "yes", "g"):
                        lbl = 1
                    elif raw in ("0", "normal", "false", "no", "n", "non-glaucoma"):
                        lbl = 0
                    else:
                        try:
                            lbl = int(float(raw))
                        except ValueError:
                            lbl = None
                    label_map[img_id] = lbl
                if label_map:
                    break
            except Exception:
                pass

        images = sorted(
            list(root.rglob("*.jpg"))
            + list(root.rglob("*.jpeg"))
            + list(root.rglob("*.png"))
        )
        # Filter by split if directories are named accordingly
        split_imgs = [p for p in images if split.lower() in str(p).lower()]
        if split_imgs:
            images = split_imgs

        if not images:
            raise FileNotFoundError(
                f"No images found in {root}. "
                "Run: eyehub download --datasets harvard_gdp"
            )

        return [
            DatasetSample(
                image_path=str(p),
                label=label_map.get(p.stem, label_map.get(p.name)),
                sample_id=p.stem,
                metadata={"split": split},
            )
            for p in images
        ]
