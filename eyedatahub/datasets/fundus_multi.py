"""Multi-disease fundus datasets: RFMiD, ODIR-2019, JSIEC, Cataract, NEH-UT."""
from __future__ import annotations

from pathlib import Path
from typing import List, Union

import numpy as np
import pandas as pd

from eyedatahub.core.dataset import DatasetInfo, DatasetSample, EyeDataHubDataset
from eyedatahub.datasets.download_utils import (
    download_kaggle,
    download_mendeley,
    download_zenodo,
    extract_archive,
    print_manual_download_instructions,
)


# ---------------------------------------------------------------------------
# RFMiD (Retinal Fundus Multi-disease Image Dataset)
# ---------------------------------------------------------------------------

RFMID_CLASSES = [
    "Disease_Risk",
    "DR",
    "ARMD",
    "MH",
    "DN",
    "MYA",
    "BRVO",
    "TSLN",
    "ERM",
    "LS",
    "MS",
    "CSR",
    "ODC",
    "CRVO",
    "TV",
    "AH",
    "ODP",
    "ODE",
    "ST",
    "AION",
    "PT",
    "RT",
    "RS",
    "CRS",
    "EDN",
    "RPEC",
    "MHL",
    "RP",
    "other",
]


class RFMiDDataset(EyeDataHubDataset):
    """
    RFMiD: Retinal Fundus Multi-disease Image Dataset.

    3200 fundus images annotated for 45 retinal conditions, grouped into 29
    binary labels (multi-label classification).

    Available on Kaggle as 'andrewmvd/retinal-disease-classification'.
    """

    _SUBDIR = "rfmid"
    _KAGGLE_SLUG = "andrewmvd/retinal-disease-classification"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="rfmid",
            full_name="RFMiD: Retinal Fundus Multi-disease Image Dataset",
            description=(
                "3200 fundus images annotated for 45 retinal conditions. "
                "Used for multi-label disease classification."
            ),
            modality="fundus",
            tasks=["multilabel", "classification"],
            num_samples=3200,
            splits=["train", "val", "test"],
            classes=RFMID_CLASSES,
            num_classes=len(RFMID_CLASSES),
            download_type="kaggle",
            download_url="https://www.kaggle.com/datasets/andrewmvd/retinal-disease-classification",
            license="CC BY-SA 4.0",
            citation=(
                "Pachade et al., 'Retinal Fundus Multi-disease Image Dataset (RFMiD): "
                "A Dataset for Multi-Disease Detection Research', Data 2021."
            ),
            tags=["multi_disease", "multilabel", "fundus", "kaggle"],
            size_gb=1.5,
        )

    # Map logical split names to the folder names Kaggle actually creates
    _SPLIT_DIRS = {
        "train": ["Training_Set/Training_Set", "Training_Set", "train"],
        "val":   ["Evaluation_Set/Evaluation_Set", "Evaluation_Set", "val"],
        "test":  ["Test_Set/Test_Set", "Test_Set", "test"],
    }
    # Keywords in CSV filenames that identify each split
    _SPLIT_CSV_KEYWORDS = {
        "train": ["training", "train"],
        "val":   ["validation", "val"],
        "test":  ["testing", "test"],
    }

    def _split_root(self, root: Path, split: str) -> Path:
        """Return the first existing split directory candidate."""
        for rel in self._SPLIT_DIRS.get(split, [split]):
            p = root / rel
            if p.exists():
                return p
        return root / split  # fallback (may not exist)

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        # Accept either the Kaggle layout (Training_Set/…) or a flat layout (train/)
        return (
            len(list(root.glob("**/RFMiD_Training_Labels.csv"))) > 0
            or (len(list(root.glob("**/*.csv"))) > 0 and len(list(root.glob("**/*.png"))) > 0)
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        dest = Path(data_dir) / self._SUBDIR
        try:
            download_kaggle(self._KAGGLE_SLUG, dest, is_competition=False)
        except Exception:
            print_manual_download_instructions(
                "RFMiD",
                "https://www.kaggle.com/datasets/andrewmvd/retinal-disease-classification",
                dest,
                extra_notes=(
                    "Kaggle extracts to:\n"
                    "  rfmid/Training_Set/Training_Set/RFMiD_Training_Labels.csv\n"
                    "  rfmid/Training_Set/Training_Set/Training/*.png\n"
                    "  rfmid/Test_Set/Test_Set/RFMiD_Testing_Labels.csv\n"
                    "  rfmid/Test_Set/Test_Set/Test/*.png"
                ),
            )
            raise

    def load(
        self, data_dir: Union[str, Path], split: str = "train"
    ) -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR
        split_dir = self._split_root(root, split)

        # Locate CSV annotation file anywhere under split_dir
        csv_candidates = list(split_dir.glob("*.csv")) + list(split_dir.glob("**/*.csv"))
        if not csv_candidates:
            raise FileNotFoundError(f"No annotation CSV found under {split_dir}.")

        # Pick CSV whose name best matches this split
        keywords = self._SPLIT_CSV_KEYWORDS.get(split, [split])
        target_csv = None
        for p in csv_candidates:
            if any(kw in p.name.lower() for kw in keywords):
                target_csv = p
                break
        if target_csv is None:
            target_csv = csv_candidates[0]

        df = pd.read_csv(target_csv)
        id_col = df.columns[0]  # usually 'ID'

        # Identify disease columns
        disease_cols = [c for c in df.columns if c != id_col and c in RFMID_CLASSES]
        if not disease_cols:
            disease_cols = [c for c in df.columns[1:] if df[c].isin([0, 1]).all()]

        # Find image directory: search within split_dir recursively
        img_candidates = (
            list(split_dir.glob("**/*.png"))
            + list(split_dir.glob("**/*.jpg"))
        )
        if img_candidates:
            img_dir = img_candidates[0].parent
        else:
            img_dir = split_dir

        samples = []
        for _, row in df.iterrows():
            img_id = str(int(row[id_col]))
            multi_label = np.array([int(row[c]) for c in disease_cols], dtype=np.int32)

            for ext in [".png", ".jpg"]:
                img_path = img_dir / f"{img_id}{ext}"
                if img_path.exists():
                    samples.append(
                        DatasetSample(
                            image_path=str(img_path),
                            label=multi_label.tolist(),
                            sample_id=img_id,
                            metadata={
                                "split": split,
                                "disease_columns": disease_cols,
                            },
                        )
                    )
                    break
        return samples


# ---------------------------------------------------------------------------
# ODIR-2019
# ---------------------------------------------------------------------------

ODIR_CLASSES = [
    "Normal",
    "Diabetes",
    "Glaucoma",
    "Cataract",
    "AMD",
    "Hypertension",
    "Myopia",
    "Other",
]


class ODIR2019Dataset(EyeDataHubDataset):
    """
    ODIR-2019: Ocular Disease Intelligent Recognition.

    8000 fundus image pairs (left + right eye) with 8 disease labels
    for multi-label classification.

    Available on Kaggle as 'andrewmvd/ocular-disease-recognition-odir5k'.
    """

    _SUBDIR = "odir2019"
    _KAGGLE_SLUG = "andrewmvd/ocular-disease-recognition-odir5k"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="odir2019",
            full_name="ODIR-2019: Ocular Disease Intelligent Recognition",
            description=(
                "8000 patients (16000 fundus images, left + right eye) with "
                "8 disease labels for multi-label ocular disease classification."
            ),
            modality="fundus",
            tasks=["multilabel", "classification"],
            num_samples=8000,
            splits=["train", "test"],
            classes=ODIR_CLASSES,
            num_classes=8,
            download_type="kaggle",
            download_url="https://www.kaggle.com/datasets/andrewmvd/ocular-disease-recognition-odir5k",
            license="CC BY-SA 4.0",
            citation=(
                "Li et al., 'An Annotation-Free Restoration Network for "
                "Cataractous Fundus Images', arXiv 2021."
            ),
            tags=["multi_disease", "multilabel", "fundus", "kaggle"],
            size_gb=3.5,
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return len(list(root.glob("**/*.jpg"))) > 1000 or len(list(root.glob("**/*.png"))) > 1000

    def download(self, data_dir: Union[str, Path]) -> None:
        dest = Path(data_dir) / self._SUBDIR
        try:
            download_kaggle(self._KAGGLE_SLUG, dest, is_competition=False)
        except Exception:
            print_manual_download_instructions(
                "ODIR-2019",
                "https://www.kaggle.com/datasets/andrewmvd/ocular-disease-recognition-odir5k",
                dest,
                extra_notes=(
                    "Expected structure:\n"
                    "  odir2019/ODIR-5K/ODIR-5K/Training Images/*.jpg\n"
                    "  odir2019/ODIR-5K/data.xlsx (or full_df.csv)"
                ),
            )
            raise

    def load(
        self, data_dir: Union[str, Path], split: str = "train"
    ) -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR

        # Find annotation file
        xlsx_candidates = list(root.glob("**/*.xlsx"))
        csv_candidates = list(root.glob("**/*.csv"))
        ann_file = None
        for f in xlsx_candidates + csv_candidates:
            if "full" in f.name.lower() or "data" in f.name.lower() or "label" in f.name.lower():
                ann_file = f
                break
        if ann_file is None and (xlsx_candidates or csv_candidates):
            ann_file = (xlsx_candidates + csv_candidates)[0]
        if ann_file is None:
            raise FileNotFoundError(f"No annotation file found in {root}.")

        if ann_file.suffix == ".xlsx":
            df = pd.read_excel(ann_file)
        else:
            df = pd.read_csv(ann_file)

        # Detect columns
        label_cols = [c for c in df.columns if c in ODIR_CLASSES]
        if not label_cols:
            # Some versions have N, D, G, C, A, H, M, O columns
            short_map = {"N": "Normal", "D": "Diabetes", "G": "Glaucoma",
                         "C": "Cataract", "A": "AMD", "H": "Hypertension",
                         "M": "Myopia", "O": "Other"}
            label_cols = [c for c in df.columns if c in short_map]

        # Find image directories
        img_dirs = []
        for d in root.rglob("*"):
            if d.is_dir() and (
                "train" in d.name.lower() or "image" in d.name.lower()
            ):
                if len(list(d.glob("*.jpg"))) + len(list(d.glob("*.png"))) > 10:
                    img_dirs.append(d)

        samples = []
        for _, row in df.iterrows():
            left_fname = str(row.get("Left-Fundus", row.get("left_fundus", "")))
            right_fname = str(row.get("Right-Fundus", row.get("right_fundus", "")))
            multi_label = np.array(
                [int(row[c]) for c in label_cols], dtype=np.int32
            ).tolist()

            for fname in [left_fname, right_fname]:
                if not fname or fname == "nan":
                    continue
                found = False
                for img_dir in img_dirs:
                    img_path = img_dir / fname
                    if img_path.exists():
                        samples.append(
                            DatasetSample(
                                image_path=str(img_path),
                                label=multi_label,
                                sample_id=fname.split(".")[0],
                                metadata={"split": split},
                            )
                        )
                        found = True
                        break
                if not found:
                    # Try any directory in root
                    for img_path in root.rglob(fname):
                        samples.append(
                            DatasetSample(
                                image_path=str(img_path),
                                label=multi_label,
                                sample_id=fname.split(".")[0],
                                metadata={"split": split},
                            )
                        )
                        break
        return samples


# ---------------------------------------------------------------------------
# JSIEC (Joint Shantou International Eye Center fundus dataset)
# ---------------------------------------------------------------------------

JSIEC_CLASSES = [
    "0.0.Normal",
    "0.1.Tessellated fundus",
    "0.2.Large optic cup",
    "0.3.DR1",
    "1.0.DR2",
    "1.1.DR3",
    "10.0.Possible glaucoma",
    "10.1.Optic atrophy",
    "11.Severe hypertensive retinopathy",
    "12.Disc swelling and elevation",
    "13.Dragged Disc",
    "14.Congenital disc abnormality",
    "15.0.Retinitis pigmentosa",
    "15.1.Bietti crystalline dystrophy",
    "16.Peripheral retinal degeneration and break",
    "17.Myelinated nerve fiber",
    "18.Vitreous particles",
    "19.Fundus neoplasm",
    "2.0.BRVO",
    "2.1.CRVO",
    "20.Massive hard exudates",
    "21.Yellow-white spots-flecks",
    "22.Cotton-wool spots",
    "23.Vessel tortuosity",
    "24.Chorioretinal atrophy-coloboma",
    "25.Preretinal hemorrhage",
    "26.Fibrosis",
    "27.Laser Spots",
    "28.Silicon oil in eye",
    "29.0.Blur fundus without PDR",
    "29.1.Blur fundus with suspected PDR",
    "3.RAO",
    "4.Rhegmatogenous RD",
    "5.0.CSCR",
    "5.1.VKH disease",
    "6.Maculopathy",
    "7.ERM",
    "8.MH",
    "9.Pathological myopia",
]


class JSIECDataset(EyeDataHubDataset):
    """
    JSIEC: Joint Shantou International Eye Center fundus photo dataset.

    One thousand fundus images classified into 39 disease categories.
    Published with Nature Communications 2021.

    Zenodo record: 3477553
    """

    _SUBDIR = "jsiec"
    _ZENODO_ID = "3477553"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="jsiec",
            full_name="JSIEC Fundus Photo Dataset",
            description=(
                "1,000 fundus images spanning 39 ophthalmic disease categories "
                "from the Joint Shantou International Eye Center. "
                "Used for multi-class fundus disease classification."
            ),
            modality="fundus",
            tasks=["classification"],
            num_samples=1000,
            splits=["all"],
            classes=JSIEC_CLASSES,
            num_classes=len(JSIEC_CLASSES),
            download_type="zenodo",
            download_url="https://zenodo.org/record/3477553",
            license="Other open access (Zenodo; no standard license identifier)",
            citation=(
                "Cen et al., 'Automatic detection of 39 fundus diseases and conditions "
                "in retinal photographs using deep neural networks', "
                "Nature Communications 2021. doi:10.1038/s41467-021-25138-w. "
                "Data: doi:10.5281/zenodo.3477553"
            ),
            tags=["multi_disease", "fundus", "zenodo", "classification"],
            size_gb=0.4,
            notes=(
                "Zenodo labels the deposit as other open access but does not "
                "name a standard reuse license. Verify terms before redistribution."
            ),
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return sum(
            path.is_file()
            and path.suffix.casefold() in {".jpg", ".jpeg", ".png", ".tif", ".tiff"}
            for path in root.rglob("*")
        ) > 100

    def download(self, data_dir: Union[str, Path]) -> None:
        dest = Path(data_dir) / self._SUBDIR
        try:
            download_zenodo(self._ZENODO_ID, dest)
            # Extract any archives
            for archive in list(dest.glob("*.zip")) + list(dest.glob("*.tar*")):
                extract_archive(archive, dest)
        except Exception:
            print_manual_download_instructions(
                "JSIEC",
                "https://zenodo.org/record/3477553",
                dest,
                extra_notes=(
                    "Download the dataset archive from Zenodo and extract into "
                    f"{dest}.\n"
                    "Expected structure: jsiec/1000images/<class_folder>/<image>"
                ),
            )
            raise

    def load(
        self, data_dir: Union[str, Path], split: str = "all"
    ) -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR
        class_to_idx = {c: i for i, c in enumerate(JSIEC_CLASSES)}
        samples: List[DatasetSample] = []
        for class_name, label in class_to_idx.items():
            class_dirs = [
                path
                for path in root.rglob(class_name)
                if path.is_dir() and path.name == class_name
            ]
            for class_dir in class_dirs:
                for img_path in sorted(
                    path
                    for path in class_dir.rglob("*")
                    if path.is_file()
                    and path.suffix.casefold()
                    in {".jpg", ".jpeg", ".png", ".tif", ".tiff"}
                ):
                    samples.append(
                        DatasetSample(
                            image_path=str(img_path),
                            label=label,
                            sample_id="_".join(
                                img_path.relative_to(root).with_suffix("").parts
                            ),
                            metadata={"class_name": class_name, "split": split},
                        )
                    )
        return samples


# ---------------------------------------------------------------------------
# Cataract Dataset (Kaggle jr2ngb/cataractdataset)
# ---------------------------------------------------------------------------

CATARACT_CLASSES = [
    "Normal",
    "Cataract",
    "Glaucoma",
    "Retina Disease",
]


class CataractDataset(EyeDataHubDataset):
    """
    Cataract Dataset from Kaggle (jr2ngb/cataractdataset).

    601 fundus images across 4 categories: Normal, Cataract, Glaucoma,
    and Retina Disease. Useful for multi-class eye disease classification.
    """

    _SUBDIR = "cataract"
    _KAGGLE_SLUG = "jr2ngb/cataractdataset"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="cataract",
            full_name="Cataract Fundus Classification Dataset",
            description=(
                "601 fundus images in 4 classes: Normal, Cataract, Glaucoma, "
                "and Retina Disease. Intended for ocular disease classification."
            ),
            modality="fundus",
            tasks=["classification"],
            num_samples=601,
            splits=["train"],
            classes=CATARACT_CLASSES,
            num_classes=4,
            download_type="kaggle",
            download_url="https://www.kaggle.com/datasets/jr2ngb/cataractdataset",
            license="See Kaggle dataset page",
            citation="Kaggle dataset by jr2ngb (2019). https://www.kaggle.com/datasets/jr2ngb/cataractdataset",
            tags=["cataract", "fundus", "kaggle", "classification"],
            size_gb=0.1,
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
                "Cataract Dataset",
                "https://www.kaggle.com/datasets/jr2ngb/cataractdataset",
                dest,
                extra_notes=(
                    "Expected structure after extraction:\n"
                    "  cataract/<class_folder>/<image>.jpg\n"
                    "  class folders: 0_normal, 1_cataract, 2_glaucoma, 3_retina_disease"
                ),
            )
            raise

    def load(
        self, data_dir: Union[str, Path], split: str = "train"
    ) -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR

        # Class folder name patterns (Kaggle dataset uses numeric prefix)
        class_patterns = {
            "0": 0, "normal": 0,
            "1": 1, "cataract": 1,
            "2": 2, "glaucoma": 2,
            "3": 3, "retina": 3,
        }

        samples: List[DatasetSample] = []
        for class_dir in sorted(root.rglob("*")):
            if not class_dir.is_dir():
                continue
            name_lower = class_dir.name.lower()
            lbl = None
            for pat, idx in class_patterns.items():
                if name_lower.startswith(pat):
                    lbl = idx
                    break

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
                        metadata={"class_name": class_dir.name, "split": split},
                    )
                )

        return samples


# ---------------------------------------------------------------------------
# NEH-UT Retinal OCT Dataset (Mendeley 8kt969dhx6 v2)
# ---------------------------------------------------------------------------

NEHUT_CLASSES = [
    "Normal",
    "Drusen",
    "CNV",
]


class NEHUTDataset(EyeDataHubDataset):
    """
    NEH-UT Retinal OCT Dataset.

    Retinal OCT B-scans from Noor Eye Hospital. Available on Mendeley Data
    (dataset ID: 8kt969dhx6, version 2).
    """

    _SUBDIR = "nehut"
    _MENDELEY_ID = "8kt969dhx6"
    _MENDELEY_VERSION = 2

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="nehut",
            full_name="NEH-UT Retinal OCT Dataset",
            description=(
                "Retinal OCT B-scans from Noor Eye Hospital for classification "
                "of Normal, Drusen, and CNV (choroidal neovascularisation) cases. "
                "16,822 B-scans from 441 eyes (Normal 120 / Drusen 160 / CNV 161 eyes)."
            ),
            modality="oct",
            tasks=["classification"],
            num_samples=16822,
            splits=["all"],
            classes=NEHUT_CLASSES,
            num_classes=3,
            download_type="mendeley",
            download_url="https://data.mendeley.com/datasets/8kt969dhx6/2",
            license="CC BY 4.0",
            citation=(
                "Labeled Retinal OCT Dataset for Classification of Normal, Drusen, "
                "and CNV Cases. Mendeley Data, V2. doi:10.17632/8kt969dhx6.2"
            ),
            tags=["oct", "mendeley", "classification", "drusen", "cnv"],
            size_gb=3.65,
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
            download_mendeley(self._MENDELEY_ID, self._MENDELEY_VERSION, dest)
        except Exception:
            print_manual_download_instructions(
                "NEH-UT",
                f"https://data.mendeley.com/datasets/{self._MENDELEY_ID}/{self._MENDELEY_VERSION}",
                dest,
                extra_notes=(
                    "Download the dataset archive from Mendeley Data and "
                    f"extract into {dest}."
                ),
            )
            raise

    def load(
        self, data_dir: Union[str, Path], split: str = "all"
    ) -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR

        # Map common folder/file naming patterns to class indices
        keyword_map = {
            "normal": 0,
            "drusen": 1,
            "cnv": 2, "choroidal": 2, "neovascular": 2,
        }

        samples: List[DatasetSample] = []

        # Check for CSV annotation
        csv_files = list(root.glob("*.csv")) + list(root.glob("**/*.csv"))
        if csv_files:
            df = pd.read_csv(csv_files[0])
            columns = {c.casefold(): c for c in df.columns}
            img_col = next(
                (
                    columns[key]
                    for key in ("directory", "image", "filename", "file", "path")
                    if key in columns
                ),
                df.columns[0],
            )
            lbl_col = columns.get("label")
            class_col = columns.get("class")
            for _, row in df.iterrows():
                img_rel = str(row[img_col]).replace("\\", "/")
                img_path = root / img_rel
                if not img_path.exists():
                    candidates = list(root.rglob(Path(img_rel).name))
                    img_path = candidates[0] if candidates else img_path
                label_text = " ".join(
                    str(row[column]).casefold()
                    for column in (class_col, lbl_col)
                    if column and not pd.isna(row[column])
                )
                path_text = str(img_path).casefold()
                lbl = next(
                    (
                        idx
                        for keyword, idx in keyword_map.items()
                        if keyword in label_text or keyword in path_text
                    ),
                    None,
                )
                if lbl is None and lbl_col and not pd.isna(row[lbl_col]):
                    try:
                        numeric_label = int(row[lbl_col])
                        lbl = numeric_label if numeric_label in {0, 1, 2} else None
                    except (TypeError, ValueError):
                        pass
                samples.append(
                    DatasetSample(
                        image_path=str(img_path),
                        label=lbl,
                        sample_id="_".join(Path(img_rel).with_suffix("").parts),
                        metadata={
                            "split": split,
                            "patient_id": row.get(columns.get("patient id", ""), None),
                            "eye": row.get(columns.get("eye", ""), None),
                        },
                    )
                )
        else:
            # Walk directory tree; infer label from folder name
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

        return samples
