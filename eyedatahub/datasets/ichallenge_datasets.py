"""
iChallenge / HDMILab ophthalmic challenge datasets.

  PALM      Pathologic Myopia — fundus classification + segmentation
  AGE       Angle-closure Glaucoma Evaluation — AS-OCT classification
  ADAM      Age-related Macular Degeneration — fundus classification + segmentation
  REFUGE1   Retinal Fundus Glaucoma Challenge (multi-rater) — HuggingFace
  REFUGE2   REFUGE2 challenge — Kaggle mirror
  GAMMA     Glaucoma grAding froM ulti-Modality imAges — HuggingFace / Grand Challenge
  GOALS     Glaucoma OCT Layer Segmentation — Zenodo 6362363
"""
from __future__ import annotations

from pathlib import Path
from typing import List, Union

from eyedatahub.core.dataset import DatasetInfo, DatasetSample, EyeDataHubDataset
from eyedatahub.datasets.download_utils import (
    download_gdrive,
    download_kaggle,
    download_zenodo,
    extract_archive,
    print_manual_download_instructions,
)


# ─────────────────────────────────────────────────────────────────────────────
# PALM — Pathologic Myopia
# ─────────────────────────────────────────────────────────────────────────────

class PALMDataset(EyeDataHubDataset):
    """
    iChallenge-PM / PALM: Pathologic Myopia detection and lesion segmentation.

    1200 colour fundus images (400 train / 400 val / 400 test).
    Classification: PM vs. non-PM (50 / 50 split).
    Segmentation: optic disc, fovea location, patchy atrophy, retinal detachment.

    Direct download (Google Drive):
      https://drive.google.com/file/d/14XWD6kX0dVRfAyEc7FkZGKZibWEkvnyv/view
    License: Challenge data-use agreement (IEEE DataPort)
    """

    _SUBDIR = "palm"
    _GDRIVE_ID = "14XWD6kX0dVRfAyEc7FkZGKZibWEkvnyv"
    _GDRIVE_URL = "https://drive.google.com/file/d/14XWD6kX0dVRfAyEc7FkZGKZibWEkvnyv/view"

    CLASSES = ["non-PM", "PM"]

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="palm",
            full_name="PALM — iChallenge Pathologic Myopia",
            description=(
                "1200 fundus images for pathologic myopia classification and "
                "optic disc / lesion segmentation. 50 % PM / 50 % non-PM."
            ),
            modality="fundus",
            tasks=["classification", "segmentation"],
            num_samples=1200,
            splits=["train", "val", "test"],
            classes=self.CLASSES,
            num_classes=2,
            image_size=(2124, 2156),
            download_type="gdrive",
            download_url=self._GDRIVE_URL,
            license="Challenge data-use agreement (IEEE DataPort)",
            citation=(
                "Fu H. et al., 'PALM: Pathologic Myopia Challenge', "
                "MICCAI 2019 Workshop."
            ),
            tags=["fundus", "myopia", "classification", "segmentation", "ichallenge"],
            size_gb=1.5,
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return root.exists() and any(root.rglob("*.jpg"))

    def download(self, data_dir: Union[str, Path]) -> None:
        dest = Path(data_dir) / self._SUBDIR
        dest.mkdir(parents=True, exist_ok=True)
        archive = dest / "palm.zip"
        try:
            download_gdrive(self._GDRIVE_ID, archive)
            extract_archive(archive, dest)
            archive.unlink(missing_ok=True)
        except ImportError:
            print_manual_download_instructions(
                "PALM — Pathologic Myopia Challenge",
                self._GDRIVE_URL,
                dest,
                extra_notes=(
                    "Install gdown for automatic download: pip install gdown\n"
                    "Or download manually and extract into the destination directory.\n\n"
                    "Expected layout:\n"
                    "  palm/Train/\n"
                    "  palm/Val/\n"
                    "  palm/Test/\n"
                ),
            )
            raise RuntimeError("Install gdown for automatic PALM download: pip install gdown")

    def load(self, data_dir: Union[str, Path], split: str = "train") -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR
        split_dir = root / split.capitalize()
        if not split_dir.exists():
            split_dir = root
        images = sorted(split_dir.rglob("*.jpg")) + sorted(split_dir.rglob("*.png"))
        if not images:
            raise FileNotFoundError(f"No images in {split_dir}.")

        label_file = split_dir / "labels.csv"
        label_map: dict = {}
        if label_file.exists():
            import csv
            with open(label_file) as f:
                for row in csv.DictReader(f):
                    label_map[row.get("id", row.get("filename", ""))] = int(row.get("label", 0))

        return [
            DatasetSample(
                image_path=str(p),
                label=label_map.get(p.stem, label_map.get(p.name, None)),
                sample_id=p.stem,
            )
            for p in images
        ]


# ─────────────────────────────────────────────────────────────────────────────
# AGE — Angle-closure Glaucoma Evaluation (AS-OCT)
# ─────────────────────────────────────────────────────────────────────────────

class AGEDataset(EyeDataHubDataset):
    """
    AGE Challenge: Angle Closure Glaucoma Evaluation from AS-OCT.

    4800 anterior-segment OCT images from 199 patients.
    Task 1: angle closure classification (open / closed).
    Task 2: scleral spur localization.

    Direct download (Google Drive):
      https://drive.google.com/file/d/1Qlkqj74SW8DJRKdYL_-ApC_0H5Z7uyvr/view
    License: Challenge data-use agreement (IEEE DataPort)
    """

    _SUBDIR = "age_challenge"
    _GDRIVE_ID = "1Qlkqj74SW8DJRKdYL_-ApC_0H5Z7uyvr"
    _GDRIVE_URL = "https://drive.google.com/file/d/1Qlkqj74SW8DJRKdYL_-ApC_0H5Z7uyvr/view"

    CLASSES = ["open", "closed"]

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="age_challenge",
            full_name="AGE — Angle-Closure Glaucoma Evaluation Challenge (AS-OCT)",
            description=(
                "4800 AS-OCT images from 199 patients. Two tasks: angle closure "
                "classification and scleral spur localization."
            ),
            modality="oct",
            tasks=["classification"],
            num_samples=4800,
            splits=["train", "test"],
            classes=self.CLASSES,
            num_classes=2,
            download_type="gdrive",
            download_url=self._GDRIVE_URL,
            license="Challenge data-use agreement (IEEE DataPort)",
            citation=(
                "Fu H. et al., 'AGE Challenge: Angle Closure Glaucoma Evaluation', "
                "MICCAI 2019 Workshop."
            ),
            tags=["oct", "as_oct", "glaucoma", "angle_closure", "classification", "ichallenge"],
            size_gb=1.2,
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return root.exists() and any(root.rglob("*.jpg"))

    def download(self, data_dir: Union[str, Path]) -> None:
        dest = Path(data_dir) / self._SUBDIR
        dest.mkdir(parents=True, exist_ok=True)
        archive = dest / "age_challenge.zip"
        try:
            download_gdrive(self._GDRIVE_ID, archive)
            extract_archive(archive, dest)
            archive.unlink(missing_ok=True)
        except ImportError:
            print_manual_download_instructions(
                "AGE — Angle Closure Glaucoma Evaluation",
                self._GDRIVE_URL,
                dest,
                extra_notes=(
                    "Install gdown for automatic download: pip install gdown\n"
                    "Or download manually and extract into the destination directory.\n\n"
                    "Expected layout:\n"
                    "  age_challenge/Train/\n"
                    "  age_challenge/Test/"
                ),
            )
            raise RuntimeError("Install gdown for automatic AGE download: pip install gdown")

    def load(self, data_dir: Union[str, Path], split: str = "train") -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR
        images = sorted(
            p for ext in (".jpg", ".png", ".bmp")
            for p in root.rglob(f"*{ext}")
            if split.lower() in str(p).lower() or split == "all"
        ) or sorted(root.rglob("*.jpg"))
        if not images:
            raise FileNotFoundError(f"No images in {root}.")
        return [DatasetSample(image_path=str(p), label=None, sample_id=p.stem) for p in images]


# ─────────────────────────────────────────────────────────────────────────────
# ADAM — Age-related Macular Degeneration
# ─────────────────────────────────────────────────────────────────────────────

class ADAMDataset(EyeDataHubDataset):
    """
    ADAM Challenge: Automatic Detection of Age-related Macular Degeneration.

    1200 fundus images (400 train / 400 val / 400 test).
    Tasks: AMD classification, optic disc & lesion segmentation, fovea localisation.
    Five lesion types: drusen, exudate, haemorrhage, scar, other.

    Direct download (Google Drive):
      https://drive.google.com/file/d/1Uz5x0aqXb0aecjzNWQ4522oCxaRDZxBt/view
    License: Challenge data-use agreement (IEEE DataPort)
    """

    _SUBDIR = "adam_challenge"
    _GDRIVE_ID = "1Uz5x0aqXb0aecjzNWQ4522oCxaRDZxBt"
    _GDRIVE_URL = "https://drive.google.com/file/d/1Uz5x0aqXb0aecjzNWQ4522oCxaRDZxBt/view"

    CLASSES = ["non-AMD", "AMD"]
    LESION_CLASSES = ["drusen", "exudate", "hemorrhage", "scar", "other"]

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="adam_challenge",
            full_name="ADAM — Automatic Detection of AMD Challenge",
            description=(
                "1200 fundus images for AMD classification, five-class lesion "
                "segmentation, fovea/optic disc localisation."
            ),
            modality="fundus",
            tasks=["classification", "segmentation"],
            num_samples=1200,
            splits=["train", "val", "test"],
            classes=self.CLASSES,
            num_classes=2,
            download_type="gdrive",
            download_url=self._GDRIVE_URL,
            license="Challenge data-use agreement (IEEE DataPort)",
            citation=(
                "Fang H. et al., 'ADAM Challenge: Detecting AMD from Fundus Images', "
                "IEEE TMI 2022."
            ),
            tags=["fundus", "amd", "classification", "segmentation", "ichallenge"],
            size_gb=1.5,
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return root.exists() and any(root.rglob("*.jpg"))

    def download(self, data_dir: Union[str, Path]) -> None:
        dest = Path(data_dir) / self._SUBDIR
        dest.mkdir(parents=True, exist_ok=True)
        archive = dest / "adam_challenge.zip"
        try:
            download_gdrive(self._GDRIVE_ID, archive)
            extract_archive(archive, dest)
            archive.unlink(missing_ok=True)
        except ImportError:
            print_manual_download_instructions(
                "ADAM — AMD Detection Challenge",
                self._GDRIVE_URL,
                dest,
                extra_notes=(
                    "Install gdown for automatic download: pip install gdown\n"
                    "Or download manually and extract into the destination directory.\n\n"
                    "Expected layout:\n"
                    "  adam_challenge/Train/{images,lesion_masks,optic_disc_masks}/\n"
                    "  adam_challenge/Train/fovea_location.xlsx"
                ),
            )
            raise RuntimeError("Install gdown for automatic ADAM download: pip install gdown")

    def load(self, data_dir: Union[str, Path], split: str = "train") -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR
        img_dir = root / split.capitalize() / "images"
        if not img_dir.exists():
            img_dir = root
        images = sorted(img_dir.rglob("*.jpg")) + sorted(img_dir.rglob("*.png"))
        if not images:
            raise FileNotFoundError(f"No images in {img_dir}.")

        label_file = root / split.capitalize() / "AMD_label.xlsx"
        label_map: dict = {}
        if label_file.exists():
            try:
                import pandas as pd
                df = pd.read_excel(str(label_file))
                id_col = df.columns[0]
                lbl_col = df.columns[1]
                label_map = {str(r[id_col]): int(r[lbl_col]) for _, r in df.iterrows()}
            except Exception:
                pass

        return [
            DatasetSample(
                image_path=str(p),
                label=label_map.get(p.stem, label_map.get(p.name, None)),
                sample_id=p.stem,
            )
            for p in images
        ]


# ─────────────────────────────────────────────────────────────────────────────
# REFUGE1 Multi-Rater
# ─────────────────────────────────────────────────────────────────────────────

class REFUGE1MultiRaterDataset(EyeDataHubDataset):
    """
    REFUGE Multi-Rater: Glaucoma classification and optic disc/cup segmentation
    with annotations from multiple independent expert raters.

    1200 fundus images from REFUGE1 with multi-rater segmentation masks.
    Useful for uncertainty quantification and consensus modelling.

    Direct download — labels (Google Drive):
      https://drive.google.com/file/d/1TXTrZyaZ76faXek46pEzaYQmAejLf30d/view
    License: CC BY-NC-SA (check HuggingFace page for current terms)
    """

    _SUBDIR = "refuge1_multirater"
    _HF_REPO = "realslimman/REFUGE-MultiRater"
    # Google Drive link for the label / annotation archive
    _GDRIVE_LABELS_ID = "1TXTrZyaZ76faXek46pEzaYQmAejLf30d"
    _GDRIVE_LABELS_URL = (
        "https://drive.google.com/file/d/1TXTrZyaZ76faXek46pEzaYQmAejLf30d/view"
    )

    CLASSES = ["non-glaucoma", "glaucoma"]

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="refuge1_multirater",
            full_name="REFUGE Multi-Rater — Glaucoma with Multi-Expert Annotations",
            description=(
                "1200 fundus images from REFUGE1 with optic disc/cup segmentation "
                "masks annotated by multiple expert raters."
            ),
            modality="fundus",
            tasks=["classification", "segmentation"],
            num_samples=1200,
            splits=["train", "val", "test"],
            classes=self.CLASSES,
            num_classes=2,
            download_type="gdrive",
            download_url=self._GDRIVE_LABELS_URL,
            license="CC BY-NC-SA (see HuggingFace page)",
            citation=(
                "Orlando J.I. et al., 'REFUGE Challenge: A Unified Framework for "
                "Evaluating Automated Methods for Glaucoma Assessment from Fundus "
                "Photographs', MIA 2020."
            ),
            tags=["fundus", "glaucoma", "segmentation", "multi_rater", "refuge", "ichallenge"],
            size_gb=0.8,
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return root.exists() and any(root.rglob("*.jpg"))

    def download(self, data_dir: Union[str, Path]) -> None:
        dest = Path(data_dir) / self._SUBDIR
        dest.mkdir(parents=True, exist_ok=True)

        # 1. Download label archive from Google Drive
        try:
            archive = dest / "refuge1_multirater_labels.zip"
            download_gdrive(self._GDRIVE_LABELS_ID, archive)
            extract_archive(archive, dest)
            archive.unlink(missing_ok=True)
        except ImportError:
            print_manual_download_instructions(
                "REFUGE1 Multi-Rater (labels)",
                self._GDRIVE_LABELS_URL,
                dest,
                extra_notes="Install gdown for automatic download: pip install gdown",
            )
            raise RuntimeError("Install gdown: pip install gdown")

        # 2. Attempt to pull images via HuggingFace datasets (optional)
        try:
            from datasets import load_dataset  # type: ignore
            import json as _json
            ds = load_dataset(self._HF_REPO, cache_dir=str(dest))
            for split_name, split_ds in ds.items():
                split_dir = dest / split_name
                split_dir.mkdir(exist_ok=True)
                for i, sample in enumerate(split_ds):
                    img = sample.get("image") or sample.get("img")
                    if img is not None:
                        img.save(split_dir / f"{i:05d}.png")
                    label = sample.get("label", sample.get("glaucoma_label", None))
                    if label is not None:
                        (split_dir / f"{i:05d}.json").write_text(_json.dumps({"label": label}))
        except Exception:
            pass  # images from GDrive archive are enough for evaluation

    def load(self, data_dir: Union[str, Path], split: str = "train") -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR
        split_dir = root / split
        search_root = split_dir if split_dir.exists() else root
        images = sorted(search_root.rglob("*.jpg")) + sorted(search_root.rglob("*.png"))
        if not images:
            raise FileNotFoundError(f"No images in {search_root}.")

        import json
        samples = []
        for p in images:
            label = None
            label_f = p.with_suffix(".json")
            if label_f.exists():
                try:
                    label = json.loads(label_f.read_text()).get("label")
                except Exception:
                    pass
            samples.append(DatasetSample(image_path=str(p), label=label, sample_id=p.stem))
        return samples


# ─────────────────────────────────────────────────────────────────────────────
# REFUGE2
# ─────────────────────────────────────────────────────────────────────────────

class REFUGE2Dataset(EyeDataHubDataset):
    """
    REFUGE2: Retinal Fundus Glaucoma Challenge 2.

    2000 fundus images (1200 from REFUGE1 + 800 new).
    Tasks: glaucoma classification, optic disc/cup segmentation, fovea localisation.

    Direct download (Google Drive):
      https://drive.google.com/file/d/1DspRzDqypeBOxZnWPQxmXprNVmJwkBRJ/view
    Kaggle mirror: https://www.kaggle.com/datasets/victorlemosml/refuge2
    License:       Research use (Grand Challenge)
    """

    _SUBDIR = "refuge2"
    _GDRIVE_ID = "1DspRzDqypeBOxZnWPQxmXprNVmJwkBRJ"
    _GDRIVE_URL = "https://drive.google.com/file/d/1DspRzDqypeBOxZnWPQxmXprNVmJwkBRJ/view"
    _KAGGLE_SLUG = "victorlemosml/refuge2"

    CLASSES = ["non-glaucoma", "glaucoma"]

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="refuge2",
            full_name="REFUGE2 — Retinal Fundus Glaucoma Challenge 2",
            description=(
                "2000 fundus images for glaucoma classification, optic disc/cup "
                "segmentation, and fovea localisation. Extends REFUGE1."
            ),
            modality="fundus",
            tasks=["classification", "segmentation"],
            num_samples=2000,
            splits=["train", "val", "test"],
            classes=self.CLASSES,
            num_classes=2,
            download_type="gdrive",
            download_url=self._GDRIVE_URL,
            license="Research use (Grand Challenge)",
            citation=(
                "Fang H. et al., 'REFUGE2 Challenge: Treasure for Multi-Domain "
                "Learning in Glaucoma Assessment', MIA 2022."
            ),
            tags=["fundus", "glaucoma", "classification", "segmentation", "refuge", "ichallenge"],
            size_gb=1.2,
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return root.exists() and any(root.rglob("*.jpg"))

    def download(self, data_dir: Union[str, Path]) -> None:
        dest = Path(data_dir) / self._SUBDIR
        dest.mkdir(parents=True, exist_ok=True)
        # Try Google Drive first (no credentials needed)
        try:
            archive = dest / "refuge2.zip"
            download_gdrive(self._GDRIVE_ID, archive)
            extract_archive(archive, dest)
            archive.unlink(missing_ok=True)
            return
        except ImportError:
            pass  # gdown not installed — fall through to Kaggle
        # Fallback: Kaggle mirror
        try:
            download_kaggle(self._KAGGLE_SLUG, dest, is_competition=False)
        except Exception:
            print_manual_download_instructions(
                "REFUGE2",
                self._GDRIVE_URL,
                dest,
                extra_notes=(
                    "Option A (easiest): pip install gdown, then re-run.\n"
                    "Option B: Kaggle credentials in .env "
                    "(KAGGLE_USERNAME + KAGGLE_KEY)."
                ),
            )
            raise

    def load(self, data_dir: Union[str, Path], split: str = "train") -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR
        images = sorted(
            p for ext in (".jpg", ".png")
            for p in root.rglob(f"*{ext}")
            if split.lower() in str(p).lower()
        ) or sorted(p for ext in (".jpg", ".png") for p in root.rglob(f"*{ext}"))
        if not images:
            raise FileNotFoundError(f"No images in {root}.")
        return [DatasetSample(image_path=str(p), label=None, sample_id=p.stem) for p in images]


# ─────────────────────────────────────────────────────────────────────────────
# GAMMA — Glaucoma grading from Multi-Modality images
# ─────────────────────────────────────────────────────────────────────────────

class GAMMADataset(EyeDataHubDataset):
    """
    GAMMA: Glaucoma grAding froM ulti-Modality imAges.

    300 paired fundus + 3D OCT volume samples from 276 Chinese patients.
    Tasks: glaucoma grading (Normal / Early / Advanced), OD/OC segmentation,
    fovea localisation.

    Direct download (Google Drive):
      https://drive.google.com/file/d/1thJDE1_TR-xa8f3H-0PwPpDxun7rV8Sw/view
    Grand Challenge: https://gamma.grand-challenge.org/
    License:      CC BY-NC-ND
    """

    _SUBDIR = "gamma"
    _GDRIVE_ID = "1thJDE1_TR-xa8f3H-0PwPpDxun7rV8Sw"
    _GDRIVE_URL = "https://drive.google.com/file/d/1thJDE1_TR-xa8f3H-0PwPpDxun7rV8Sw/view"
    _HF_REPO = "ctmedtech/GAMMA"

    CLASSES = ["Normal", "Early", "Advanced"]

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="gamma",
            full_name="GAMMA — Glaucoma Grading from Multi-Modality Images",
            description=(
                "300 paired fundus + 3D OCT volumes. Glaucoma grading into "
                "Normal / Early / Advanced plus OD/OC segmentation and fovea location."
            ),
            modality="multimodal",
            tasks=["grading", "classification", "segmentation"],
            num_samples=300,
            splits=["train", "test"],
            classes=self.CLASSES,
            num_classes=3,
            download_type="gdrive",
            download_url=self._GDRIVE_URL,
            license="CC BY-NC-ND",
            citation=(
                "Wu J. et al., 'GAMMA Challenge: Glaucoma Grading from Multi-Modality "
                "Imaging', MIA 2023."
            ),
            tags=[
                "fundus", "oct", "glaucoma", "grading", "segmentation",
                "multimodal", "gamma", "ichallenge",
            ],
            size_gb=5.0,
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return root.exists() and (
            any(root.rglob("*.jpg")) or any(root.rglob("*.png"))
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        dest = Path(data_dir) / self._SUBDIR
        dest.mkdir(parents=True, exist_ok=True)
        # Try Google Drive first
        try:
            archive = dest / "gamma.zip"
            download_gdrive(self._GDRIVE_ID, archive)
            extract_archive(archive, dest)
            archive.unlink(missing_ok=True)
            return
        except ImportError:
            pass  # gdown not installed — fall through to HuggingFace
        # Fallback: HuggingFace datasets library
        try:
            from datasets import load_dataset  # type: ignore
            import json as _json
            print(f"Downloading GAMMA from HuggingFace ({self._HF_REPO})...")
            ds = load_dataset(self._HF_REPO, cache_dir=str(dest))
            for split_name, split_ds in ds.items():
                split_dir = dest / split_name
                split_dir.mkdir(exist_ok=True)
                for i, sample in enumerate(split_ds):
                    img = sample.get("image") or sample.get("fundus")
                    if img is not None:
                        img.save(split_dir / f"{i:04d}_fundus.png")
                    label = sample.get("label", sample.get("glaucoma_grade", None))
                    meta = {k: v for k, v in sample.items() if k not in ("image", "fundus")}
                    (split_dir / f"{i:04d}.json").write_text(_json.dumps({
                        "label": label,
                        **{k: str(v) for k, v in meta.items() if not hasattr(v, "save")},
                    }))
            print(f"GAMMA saved to {dest}")
        except ImportError:
            print_manual_download_instructions(
                "GAMMA Challenge",
                self._GDRIVE_URL,
                dest,
                extra_notes=(
                    "Option A (easiest): pip install gdown, then re-run.\n"
                    "Option B: pip install datasets, then re-run.\n"
                    "Alternative: https://gamma.grand-challenge.org/"
                ),
            )
            raise RuntimeError("Install gdown or datasets: pip install gdown")

    def load(self, data_dir: Union[str, Path], split: str = "train") -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR
        split_dir = root / split
        search = split_dir if split_dir.exists() else root
        images = sorted(search.rglob("*.jpg")) + sorted(search.rglob("*.png"))
        if not images:
            raise FileNotFoundError(f"No images in {search}.")

        import json
        samples = []
        for p in images:
            label = None
            lf = p.with_suffix(".json")
            if not lf.exists():
                lf = p.parent / (p.stem.split("_")[0] + ".json")
            if lf.exists():
                try:
                    label = json.loads(lf.read_text()).get("label")
                except Exception:
                    pass
            samples.append(DatasetSample(image_path=str(p), label=label, sample_id=p.stem))
        return samples


# ─────────────────────────────────────────────────────────────────────────────
# GOALS — Glaucoma OCT Analysis and Layer Segmentation
# ─────────────────────────────────────────────────────────────────────────────

class GOALSDataset(EyeDataHubDataset):
    """
    GOALS: Glaucoma OCT Analysis and Layer Segmentation (MICCAI 2022).

    300 circumpapillary OCT images.
    Task 1: Layer segmentation — RNFL, GCIPL, choroid.
    Task 2: Glaucoma classification (binary).

    Direct download (Google Drive):
      https://drive.google.com/file/d/1P1cLm9_Pwq4fum4lB1-LGUayO-NMvF5I/view
    Zenodo mirror: https://zenodo.org/records/6362363
    License: CC BY 4.0
    """

    _SUBDIR = "goals"
    _GDRIVE_ID = "1P1cLm9_Pwq4fum4lB1-LGUayO-NMvF5I"
    _GDRIVE_URL = "https://drive.google.com/file/d/1P1cLm9_Pwq4fum4lB1-LGUayO-NMvF5I/view"
    _BAIDU_URL = "https://aistudio.baidu.com/competition/detail/783/0/introduction"
    _ZENODO_RECORD = "6362363"

    LAYER_CLASSES = ["RNFL", "GCIPL", "Choroid"]
    GLAUCOMA_CLASSES = ["non-glaucoma", "glaucoma"]

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="goals",
            full_name="GOALS — Glaucoma OCT Layer Segmentation (MICCAI 2022)",
            description=(
                "300 circumpapillary OCT images. RNFL/GCIPL/choroid layer "
                "segmentation plus binary glaucoma classification."
            ),
            modality="oct",
            tasks=["segmentation", "classification"],
            num_samples=300,
            splits=["train", "test"],
            classes=self.LAYER_CLASSES,
            num_classes=3,
            download_type="gdrive",
            download_url=self._BAIDU_URL,
            license="CC BY 4.0",
            citation=(
                "Fang H. et al., 'GOALS Challenge: A Large-Scale OCT Image "
                "Dataset for Glaucoma Analysis', MICCAI 2022 Workshop."
            ),
            tags=["oct", "glaucoma", "segmentation", "layers", "goals", "ichallenge"],
            size_gb=0.5,
            notes=(
                f"Primary challenge page: {self._BAIDU_URL}. "
                f"Automated downloader still tries the known Google Drive mirror "
                f"({self._GDRIVE_URL}) and then Zenodo record {self._ZENODO_RECORD}."
            ),
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return root.exists() and (
            any(root.rglob("*.jpg")) or
            any(root.rglob("*.png")) or
            any(root.rglob("*.bmp"))
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        dest = Path(data_dir) / self._SUBDIR
        dest.mkdir(parents=True, exist_ok=True)
        # Try Google Drive first (no credentials needed)
        try:
            archive = dest / "goals.zip"
            download_gdrive(self._GDRIVE_ID, archive)
            extract_archive(archive, dest)
            archive.unlink(missing_ok=True)
            return
        except ImportError:
            pass  # gdown not installed — fall through to Zenodo
        # Fallback: Zenodo
        try:
            download_zenodo(self._ZENODO_RECORD, dest)
        except Exception as e:
            print_manual_download_instructions(
                "GOALS Challenge",
                self._GDRIVE_URL,
                dest,
                extra_notes=(
                    f"Error: {e}\n\n"
                    "Option A (easiest): pip install gdown, then re-run.\n"
                    f"Challenge page: {self._BAIDU_URL}\n"
                    "Option B: Zenodo URL:\n"
                    f"  https://zenodo.org/records/{self._ZENODO_RECORD}\n"
                    "If the Zenodo record is restricted, add ZENODO_TOKEN to .env."
                ),
            )
            raise

    def load(self, data_dir: Union[str, Path], split: str = "train") -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR
        image_directories = [
            path
            for path in root.rglob("*")
            if path.is_dir()
            and path.name.casefold() == "image"
            and "__macosx" not in {part.casefold() for part in path.parts}
        ]
        images = sorted(
            path
            for directory in image_directories
            for path in directory.iterdir()
            if path.is_file()
            and path.suffix.casefold() in {".jpg", ".jpeg", ".png", ".bmp"}
            and not path.name.startswith("._")
        )
        if not images:
            images = sorted(
                path
                for path in root.rglob("*")
                if path.is_file()
                and path.suffix.casefold() in {".jpg", ".jpeg", ".png", ".bmp"}
                and "__macosx"
                not in {part.casefold() for part in path.parts}
                and not path.name.startswith("._")
                and "mask" not in path.stem.casefold()
                and "label" not in path.stem.casefold()
            )
        if not images:
            raise FileNotFoundError(f"No images in {root}.")

        # Labels often stored in a CSV alongside images
        label_map: dict = {}
        for csv_candidate in root.rglob("*.csv"):
            try:
                import csv
                with open(csv_candidate) as f:
                    for row in csv.DictReader(f):
                        sid = row.get("id", row.get("filename", row.get("image_id", "")))
                        lbl = row.get("label", row.get("glaucoma", None))
                        if sid and lbl is not None:
                            label_map[str(sid).replace(".jpg", "").replace(".png", "")] = int(lbl)
                if label_map:
                    break
            except Exception:
                continue

        return [
            DatasetSample(
                image_path=str(p),
                label=label_map.get(p.stem, None),
                sample_id=p.stem,
            )
            for p in images
            if split.lower() in str(p).lower() or split == "all"
        ] or [
            DatasetSample(image_path=str(p), label=label_map.get(p.stem), sample_id=p.stem)
            for p in images
        ]
