"""OCT (Optical Coherence Tomography) datasets: Kermany OCT, OCTID, OCT-Cirrus, OLIVES, Rasti."""
from __future__ import annotations

from pathlib import Path
from typing import List, Union

from eyedatahub.core.dataset import DatasetInfo, DatasetSample, EyeDataHubDataset
import pandas as pd

from eyedatahub.datasets.download_utils import (
    download_huggingface,
    download_kaggle,
    download_zenodo,
    extract_archive,
    print_manual_download_instructions,
)


# ---------------------------------------------------------------------------
# Kermany OCT 2018
# ---------------------------------------------------------------------------

KERMANY_CLASSES = ["CNV", "DME", "DRUSEN", "NORMAL"]


class KermanyOCTDataset(EyeDataHubDataset):
    """
    Kermany OCT 2018: Retinal OCT classification dataset.

    ~84,000 OCT images across 4 classes:
    - CNV: Choroidal Neovascularization
    - DME: Diabetic Macular Edema
    - DRUSEN: Drusen deposits (early AMD)
    - NORMAL: Healthy retina

    Available on Kaggle as 'paultimothymooney/kermany2018'.
    """

    _SUBDIR = "kermany_oct"
    _KAGGLE_SLUG = "paultimothymooney/kermany2018"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="kermany_oct",
            full_name="Kermany OCT 2018: Retinal OCT Image Classification",
            description=(
                "~84,000 retinal OCT B-scan images across 4 classes: CNV, DME, "
                "DRUSEN, NORMAL. Train: ~83,484 / Test: 1000."
            ),
            modality="oct",
            tasks=["classification"],
            num_samples=84484,
            splits=["train", "test", "val"],
            classes=KERMANY_CLASSES,
            num_classes=4,
            download_type="kaggle",
            download_url="https://www.kaggle.com/datasets/paultimothymooney/kermany2018",
            license="CC BY 4.0",
            citation=(
                "Kermany et al., 'Identifying medical diagnoses and treatable "
                "diseases by image-based deep learning', Cell 2018."
            ),
            tags=["oct", "classification", "cataract", "amd"],
            size_gb=6.0,
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        test_normal = root / "test" / "NORMAL"
        return test_normal.exists() and len(list(test_normal.glob("*.jpeg"))) > 0

    def download(self, data_dir: Union[str, Path]) -> None:
        dest = Path(data_dir) / self._SUBDIR
        try:
            download_kaggle(self._KAGGLE_SLUG, dest, is_competition=False)
        except Exception:
            print_manual_download_instructions(
                "Kermany OCT 2018",
                "https://www.kaggle.com/datasets/paultimothymooney/kermany2018",
                dest,
                extra_notes=(
                    "Expected structure after extraction:\n"
                    "  kermany_oct/train/CNV/*.jpeg\n"
                    "  kermany_oct/train/DME/*.jpeg\n"
                    "  kermany_oct/train/DRUSEN/*.jpeg\n"
                    "  kermany_oct/train/NORMAL/*.jpeg\n"
                    "  kermany_oct/test/CNV/*.jpeg  (250 images each)\n"
                    "  kermany_oct/test/DME/*.jpeg\n"
                    "  kermany_oct/test/DRUSEN/*.jpeg\n"
                    "  kermany_oct/test/NORMAL/*.jpeg"
                ),
            )
            raise

    def load(
        self, data_dir: Union[str, Path], split: str = "test"
    ) -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR

        # Kaggle download may place inside an extra 'OCT2017' subdirectory
        split_dir = root / split
        if not split_dir.exists():
            split_dir = root / "OCT2017" / split
        if not split_dir.exists():
            split_dir = root / "kermany2018" / "OCT2017" / split
        if not split_dir.exists():
            raise FileNotFoundError(
                f"Kermany OCT {split} directory not found under {root}. "
                "Run `eyehub download --datasets kermany_oct` first."
            )

        class_to_idx = {cls: i for i, cls in enumerate(KERMANY_CLASSES)}
        samples = []

        for cls_dir in sorted(split_dir.iterdir()):
            if not cls_dir.is_dir():
                continue
            cls_name = cls_dir.name.upper()
            label = class_to_idx.get(cls_name, -1)
            if label == -1:
                continue
            for img_path in sorted(cls_dir.glob("*.jpeg")) + sorted(cls_dir.glob("*.jpg")) + sorted(cls_dir.glob("*.png")):
                samples.append(
                    DatasetSample(
                        image_path=str(img_path),
                        label=label,
                        sample_id=img_path.stem,
                        metadata={"split": split, "class": cls_name},
                    )
                )
        return samples


# ---------------------------------------------------------------------------
# OCTID
# ---------------------------------------------------------------------------

OCTID_CLASSES = ["NORMAL", "AMD", "CSC", "DR", "MH"]


class OCTIDDataset(EyeDataHubDataset):
    """
    OCTID: OCT Image Database.

    500 high-resolution OCT images across 5 classes:
    Normal, AMD, CSC (Central Serous Chorioretinopathy), DR, and MH (Macular Hole).

    From the Ophthalmology Department, University of Waterloo.
    """

    _SUBDIR = "octid"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="octid",
            full_name="OCTID: OCT Image Database",
            description=(
                "500 OCT images: NORMAL (206), AMD (50), CSC (128), DR (59), "
                "MH (57). High-resolution B-scans for 5-class classification."
            ),
            modality="oct",
            tasks=["classification"],
            num_samples=500,
            splits=["all"],
            classes=OCTID_CLASSES,
            num_classes=5,
            download_type="manual",
            download_url="https://borealisdata.ca/dataverse/OCTID",
            license="CC0 1.0 Universal",
            citation=(
                "Gholami et al., 'OCTID: Optical Coherence Tomography Image "
                "Database', Elsevier 2020."
            ),
            tags=["oct", "classification", "amd"],
            size_gb=0.3,
            notes=(
                "Freely available from Borealis Data Repository. "
                "No account required."
            ),
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return len(list(root.glob("**/*.bmp"))) > 50 or len(list(root.glob("**/*.png"))) > 50

    def download(self, data_dir: Union[str, Path]) -> None:
        root = Path(data_dir) / self._SUBDIR
        print_manual_download_instructions(
            "OCTID",
            "https://borealisdata.ca/dataverse/OCTID",
            root,
            extra_notes=(
                "Go to the Borealis Data Repository and download the OCTID dataset.\n"
                "No registration required — direct download available.\n"
                "Expected structure:\n"
                "  octid/NORMAL/*.bmp\n"
                "  octid/AMD/*.bmp\n"
                "  octid/CSC/*.bmp\n"
                "  octid/DR/*.bmp\n"
                "  octid/MH/*.bmp"
            ),
        )
        raise RuntimeError("OCTID requires manual download from Borealis Data.")

    def load(
        self, data_dir: Union[str, Path], split: str = "all"
    ) -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR

        class_to_idx = {cls: i for i, cls in enumerate(OCTID_CLASSES)}
        samples = []

        for cls_dir in sorted(root.iterdir()):
            if not cls_dir.is_dir():
                continue
            cls_name = cls_dir.name.upper()
            label = class_to_idx.get(cls_name, -1)
            if label == -1:
                continue
            for img_path in (
                sorted(cls_dir.glob("*.bmp"))
                + sorted(cls_dir.glob("*.png"))
                + sorted(cls_dir.glob("*.jpg"))
                + sorted(cls_dir.glob("*.tif"))
            ):
                samples.append(
                    DatasetSample(
                        image_path=str(img_path),
                        label=label,
                        sample_id=img_path.stem,
                        metadata={"split": split, "class": cls_name},
                    )
                )
        return samples


# ---------------------------------------------------------------------------
# AROI (Annotated Retinal OCT Images)
# ---------------------------------------------------------------------------

AROI_LAYERS = ["ILM", "NFL-IPL", "INL", "OPL", "ONL-ISM", "ISE", "OS-RPE", "RPE-BM"]
AROI_FLUIDS = ["IRF", "SRF", "PED"]


class AROIDataset(EyeDataHubDataset):
    """
    AROI: Annotated Retinal OCT Images database.

    1,136 OCT B-scans from 24 AMD patients with expert annotation of
    3 retinal fluid types (IRF, SRF, PED) and 3 retinal layer boundaries.

    Source: University of Zagreb / IPG Lab
    GDrive: https://drive.google.com/file/d/10Ys4xsw81evjHewZEvqHy4Kri0my8C2S/view
    """

    _SUBDIR = "aroi"
    _GDRIVE_ID = "10Ys4xsw81evjHewZEvqHy4Kri0my8C2S"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="aroi",
            full_name="AROI: Annotated Retinal OCT Images Database",
            description=(
                "1,136 OCT B-scans from 24 AMD patients. Expert annotations for "
                "3 retinal fluid types (IRF, SRF, PED) and 3 retinal layer "
                "boundaries for joint layer and fluid segmentation."
            ),
            modality="oct",
            tasks=["segmentation"],
            num_samples=1136,
            splits=["train", "test"],
            image_size=(768, 496),
            download_type="gdrive",
            download_url="https://drive.google.com/file/d/10Ys4xsw81evjHewZEvqHy4Kri0my8C2S/view",
            license="Research only — cite required papers (see citation field)",
            citation=(
                "M. Melinščak, M. Radmilović, Z. Vatavuk, S. Lončarić, "
                "'Annotated retinal optical coherence tomography images (AROI) database "
                "for joint retinal layer and fluid segmentation', "
                "Automatika, vol. 62, no. 3, pp. 375–385, Jul. 2021. "
                "doi:10.1080/00051144.2021.1973298 | "
                "M. Melinščak et al., 'AROI: Annotated Retinal OCT Images database', "
                "MIPRO 2021, pp. 400–405 | "
                "M. Melinščak, 'Attention-based U-net: Joint segmentation of layers "
                "and fluids from retinal OCT images', MIPRO 2023, pp. 391–396 | "
                "M. Melinščak, 'Enhancing Interpretability in Retinal OCT Analysis "
                "Using Grad-CAM: A Study on the AROI Dataset', MIPRO 2025, pp. 1433–1438."
            ),
            tags=["oct", "segmentation", "amd", "fluid", "layers"],
            size_gb=0.5,
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return len(list(root.glob("**/*.png"))) > 100

    def download(self, data_dir: Union[str, Path]) -> None:
        dest = Path(data_dir) / self._SUBDIR
        dest.mkdir(parents=True, exist_ok=True)
        archive = dest / "aroi.zip"
        try:
            from eyedatahub.datasets.download_utils import download_gdrive
            download_gdrive(self._GDRIVE_ID, archive)
            extract_archive(archive, dest)
            archive.unlink(missing_ok=True)
        except Exception:
            print_manual_download_instructions(
                "AROI",
                "https://drive.google.com/file/d/10Ys4xsw81evjHewZEvqHy4Kri0my8C2S/view",
                dest,
                extra_notes=(
                    "Requires: pip install gdown\n"
                    "Or download manually from the Google Drive link above.\n\n"
                    "Expected structure after extraction:\n"
                    "  aroi/patient_*/oct_images/*.png\n"
                    "  aroi/patient_*/fluid_masks/*.png"
                ),
            )
            raise

    def load(self, data_dir: Union[str, Path], split: str = "test") -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR
        img_paths = sorted(root.glob("**/oct_images/*.png")) + sorted(root.glob("**/*.png"))
        # Filter out mask files
        img_paths = [p for p in img_paths if "mask" not in p.parent.name.lower()]

        samples = []
        for img_path in img_paths:
            stem = img_path.stem
            patient_dir = img_path.parent.parent
            mask_dir = patient_dir / "fluid_masks"
            mask_path = ""
            if mask_dir.exists():
                candidates = list(mask_dir.glob(f"{stem}*.png"))
                mask_path = str(candidates[0]) if candidates else ""
            samples.append(DatasetSample(
                image_path=str(img_path),
                label=mask_path,
                sample_id=stem,
                metadata={"split": split, "patient": patient_dir.name},
            ))
        return samples


# ---------------------------------------------------------------------------
# DRAC 2022
# ---------------------------------------------------------------------------

DRAC_DR_GRADES = ["No DR", "Non-proliferative DR", "Proliferative DR"]


class DRAC22Dataset(EyeDataHubDataset):
    """
    DRAC 2022: Diabetic Retinopathy Analysis Challenge.

    174 OCTA images for:
    1. Lesion segmentation (intraretinal microvascular abnormalities, non-perfusion areas, neovascularization)
    2. Image quality assessment
    3. DR grading (3 classes)
    """

    _SUBDIR = "drac22"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="drac22",
            full_name="DRAC 2022: Diabetic Retinopathy Analysis Challenge",
            description=(
                "174 OCTA images for DR lesion segmentation (IRMA, NPA, NV), "
                "image quality assessment, and DR grading (3-class)."
            ),
            modality="octa",
            tasks=["segmentation", "classification", "grading"],
            num_samples=174,
            splits=["train", "test"],
            classes=DRAC_DR_GRADES,
            num_classes=3,
            download_type="zenodo",
            download_url="https://zenodo.org/records/10280359",
            license="CC BY 4.0",
            citation=(
                "Qin et al., 'DRAC: Diabetic Retinopathy Analysis Challenge with "
                "Ultra-Wide Optical Coherence Tomography Angiography Images', "
                "Medical Image Analysis 2024."
            ),
            tags=["octa", "dr", "segmentation", "classification"],
            size_gb=0.3,
            notes="Available from Grand Challenge after free registration.",
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return len(list(root.glob("**/*.png"))) > 50

    _ZENODO_ID = "10280359"

    def download(self, data_dir: Union[str, Path]) -> None:
        dest = Path(data_dir) / self._SUBDIR
        try:
            download_zenodo(self._ZENODO_ID, dest)
            for archive in list(dest.glob("*.zip")) + list(dest.glob("*.tar*")):
                extract_archive(archive, dest)
        except Exception:
            print_manual_download_instructions(
                "DRAC 2022",
                "https://zenodo.org/records/10280359",
                dest,
                extra_notes=(
                    "Download from Zenodo record 10280359 or Grand Challenge.\n"
                    "Expected structure:\n"
                    "  drac22/A. Segmentation/1. Original Images/a. Training Set/*.png\n"
                    "  drac22/A. Segmentation/2. Groundtruths/a. Training Set/1. Intraretinal Microvascular Abnormalities/*.png\n"
                    "  drac22/C. DR Grading/1. Original Images/a. Training Set/*.png\n"
                    "  drac22/C. DR Grading/2. Groundtruths/a. Training Set.csv"
                ),
            )
            raise

    def load(self, data_dir: Union[str, Path], split: str = "train") -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR
        split_name = "Training Set" if split == "train" else "Test Set"

        # Try DR grading subtask first
        grade_img_dir = root / "C. DR Grading" / "1. Original Images" / f"a. {split_name}"
        grade_csv = root / "C. DR Grading" / "2. Groundtruths" / f"a. {split_name}.csv"

        if grade_img_dir.exists():
            label_map = {}
            if grade_csv.exists():
                df = pd.read_csv(grade_csv)
                for _, row in df.iterrows():
                    label_map[str(row.iloc[0])] = int(row.iloc[1])

            samples = []
            for img_path in sorted(grade_img_dir.glob("*.png")):
                stem = img_path.stem
                label = label_map.get(img_path.name, label_map.get(stem, 0))
                samples.append(DatasetSample(
                    image_path=str(img_path),
                    label=label,
                    sample_id=stem,
                    metadata={"split": split, "task": "grading"},
                ))
            return samples

        # Fallback: return all images without labels
        all_imgs = list(root.glob("**/*.png"))
        return [DatasetSample(image_path=str(p), label=0, sample_id=p.stem) for p in sorted(all_imgs)]


# ---------------------------------------------------------------------------
# Retinal OCT-C8
# ---------------------------------------------------------------------------

OCT_C8_CLASSES = [
    "AMD", "Branch Retinal Artery Occlusion", "Branch Retinal Vein Occlusion",
    "Central Serous Chorioretinopathy", "Central Retinal Artery Occlusion",
    "Central Retinal Vein Occlusion", "Diabetic Macular Edema", "Macular Hole",
]


class RetinalOCTC8Dataset(EyeDataHubDataset):
    """
    Retinal OCT-C8: 8-class retinal OCT classification dataset.

    ~24,000 OCT images across 8 pathological categories from Kaggle.
    """

    _SUBDIR = "oct_c8"
    _KAGGLE_SLUG = "obulisainaren/retinal-oct-c8"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="oct_c8",
            full_name="Retinal OCT-C8: 8-Class OCT Classification",
            description=(
                "~24,000 retinal OCT images across 8 disease classes: AMD, BRAO, "
                "BRVO, CSC, CRAO, CRVO, DME, MH."
            ),
            modality="oct",
            tasks=["classification"],
            num_samples=24000,
            splits=["train", "val", "test"],
            classes=OCT_C8_CLASSES,
            num_classes=8,
            download_type="kaggle",
            download_url="https://www.kaggle.com/datasets/obulisainaren/retinal-oct-c8",
            license="See Kaggle dataset page",
            citation=(
                "Srinivasan et al., 'Fully automated detection of diabetic macular "
                "edema and dry age-related macular degeneration from optical "
                "coherence tomography images', Biomed. Opt. Express 2014."
            ),
            tags=["oct", "classification", "8-class"],
            size_gb=2.5,
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return len(list(root.glob("**/*.jpeg"))) > 500 or len(list(root.glob("**/*.jpg"))) > 500

    def download(self, data_dir: Union[str, Path]) -> None:
        dest = Path(data_dir) / self._SUBDIR
        try:
            download_kaggle(self._KAGGLE_SLUG, dest, is_competition=False)
        except Exception:
            print_manual_download_instructions(
                "Retinal OCT-C8",
                "https://www.kaggle.com/datasets/obulisainaren/retinal-oct-c8",
                dest,
            )
            raise

    def load(self, data_dir: Union[str, Path], split: str = "test") -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR
        split_dir = root / split
        if not split_dir.exists():
            split_dir = root

        class_to_idx = {c.upper().replace(" ", "_"): i for i, c in enumerate(OCT_C8_CLASSES)}
        # Also map short names
        short_map = {"AMD": 0, "BRAO": 1, "BRVO": 2, "CSC": 3, "CRAO": 4, "CRVO": 5, "DME": 6, "MH": 7}

        samples = []
        for cls_dir in sorted(split_dir.iterdir()):
            if not cls_dir.is_dir():
                continue
            label = short_map.get(cls_dir.name.upper(), class_to_idx.get(cls_dir.name.upper().replace(" ", "_"), -1))
            if label == -1:
                continue
            for img_path in sorted(cls_dir.glob("*.jpeg")) + sorted(cls_dir.glob("*.jpg")) + sorted(cls_dir.glob("*.png")):
                samples.append(DatasetSample(
                    image_path=str(img_path),
                    label=label,
                    sample_id=img_path.stem,
                    metadata={"split": split, "class": cls_dir.name},
                ))
        return samples


# ---------------------------------------------------------------------------
# OCTDL
# ---------------------------------------------------------------------------

OCTDL_CLASSES = ["AMD", "DME", "ERM", "NO", "RAO", "RVO", "VID"]


class OCTDLDataset(EyeDataHubDataset):
    """
    OCTDL: OCT Deep Learning Dataset.

    2,000+ labeled OCT images for 7-class classification (AMD, DME, ERM,
    NO = normal, RAO, RVO, VID). Published in Scientific Data 2024.

    Mendeley Data: https://data.mendeley.com/datasets/sncdhf53xc/4
    """

    _SUBDIR = "octdl"
    _MENDELEY_ID = "sncdhf53xc"
    _MENDELEY_VERSION = 4
    _MENDELEY_URL = f"https://data.mendeley.com/datasets/{_MENDELEY_ID}/{_MENDELEY_VERSION}"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="octdl",
            full_name="OCTDL: OCT Deep Learning Dataset",
            description=(
                "2,000+ OCT images labeled for 7 conditions: AMD, DME, ERM, "
                "NO (normal), RAO, RVO, VID."
            ),
            modality="oct",
            tasks=["classification"],
            num_samples=2000,
            splits=["all"],
            classes=OCTDL_CLASSES,
            num_classes=7,
            download_type="mendeley",
            download_url=self._MENDELEY_URL,
            license="CC BY 4.0",
            citation=(
                "Kulyabin et al., 'OCTDL: Optical Coherence Tomography Dataset "
                "for Image-Based Deep Learning Methods', Scientific Data 2024."
            ),
            tags=["oct", "classification", "7-class"],
            size_gb=0.8,
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return len(list(root.glob("**/*.png"))) > 100 or len(list(root.glob("**/*.jpg"))) > 100

    def download(self, data_dir: Union[str, Path]) -> None:
        dest = Path(data_dir) / self._SUBDIR
        dest.mkdir(parents=True, exist_ok=True)
        # Try Mendeley auto-download first (no credentials needed)
        try:
            from eyedatahub.datasets.download_utils import download_mendeley
            download_mendeley(self._MENDELEY_ID, self._MENDELEY_VERSION, dest, extract=True)
            return
        except Exception:
            pass
        # Fallback: manual instructions with the canonical Mendeley page.
        print_manual_download_instructions(
            "OCTDL",
            self._MENDELEY_URL,
            dest,
            extra_notes=(
                "Canonical Mendeley Data record: "
                f"{self._MENDELEY_URL}\n\n"
                "Expected structure after extraction:\n"
                "  octdl/AMD/*.jpg\n  octdl/DME/*.jpg\n  octdl/ERM/*.jpg\n"
                "  octdl/NO/*.jpg\n  octdl/RAO/*.jpg\n  octdl/RVO/*.jpg\n"
                "  octdl/VID/*.jpg"
            ),
        )
        raise RuntimeError("OCTDL: Mendeley auto-download failed. See instructions above.")

    def load(self, data_dir: Union[str, Path], split: str = "all") -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR
        class_to_idx = {c: i for i, c in enumerate(OCTDL_CLASSES)}
        candidates = [root]
        candidates.extend(path for path in root.iterdir() if path.is_dir())
        class_root = max(
            candidates,
            key=lambda path: sum(
                (path / class_name).is_dir()
                for class_name in OCTDL_CLASSES
            ),
        )
        samples = []
        for cls_dir in sorted(class_root.iterdir()):
            if not cls_dir.is_dir():
                continue
            label = class_to_idx.get(cls_dir.name.upper(), -1)
            if label == -1:
                continue
            for img_path in sorted(cls_dir.glob("*.jpg")) + sorted(cls_dir.glob("*.png")):
                samples.append(DatasetSample(
                    image_path=str(img_path),
                    label=label,
                    sample_id=img_path.stem,
                    metadata={"class": cls_dir.name},
                ))
        return samples


# ---------------------------------------------------------------------------
# Duke Srinivasan retinal OCT dataset
# ---------------------------------------------------------------------------

OCT_CIRRUS_CLASSES = [
    "AMD",
    "DME",
    "Normal",
]


class OCTCirrusDataset(EyeDataHubDataset):
    """Duke Srinivasan retinal OCT dataset from the 2014 study."""

    _SUBDIR = "oct_cirrus"
    _URL = "https://people.duke.edu/~sf59/Srinivasan_BOE_2014_dataset.htm"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="oct_cirrus",
            full_name="Duke Srinivasan Retinal OCT Dataset",
            description=(
                "Forty-five retinal OCT volumes acquired with a Spectralis "
                "system: 15 dry AMD, 15 diabetic macular edema, and 15 normal "
                "volumes. The official Duke release provides the study data."
            ),
            modality="oct",
            tasks=["classification"],
            num_samples=45,
            splits=["all"],
            classes=OCT_CIRRUS_CLASSES,
            num_classes=3,
            download_type="manual",
            download_url=self._URL,
            license=(
                "Research only: research and educational use; commercialization "
                "and redistribution prohibited"
            ),
            citation=(
                "Srinivasan PP, Kim LA, Mettu PS, et al. Fully automated "
                "detection of diabetic macular edema and dry age-related "
                "macular degeneration from optical coherence tomography images. "
                "Biomed Opt Express. 2014;5:3568-3577. "
                "doi:10.1364/BOE.5.003568"
            ),
            tags=["oct", "classification", "amd", "dme", "duke", "spectralis"],
            size_gb=0.58,
            notes=(
                "The source permits research and educational use but prohibits "
                "commercialization and redistribution. The sample count records "
                "45 volumes; the loader emits their 3,231 B-scans."
            ),
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return (
            len(list(root.glob("**/*.jpg"))) > 20
            or len(list(root.glob("**/*.png"))) > 20
            or len(list(root.glob("**/*.bmp"))) > 20
            or len(list(root.glob("**/*.tif"))) > 20
            or len(list(root.glob("**/*.tiff"))) > 20
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        dest = Path(data_dir) / self._SUBDIR
        print_manual_download_instructions(
            "Duke Srinivasan Retinal OCT",
            self._URL,
            dest,
            extra_notes=(
                "Read the source terms, download the archive from the Duke "
                f"page, and extract it into {dest}."
            ),
        )
        raise RuntimeError(
            "Duke Srinivasan Retinal OCT requires manual download. "
            "See the instructions above."
        )

    def load(
        self, data_dir: Union[str, Path], split: str = "all"
    ) -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR
        class_to_idx = {c.lower(): i for i, c in enumerate(OCT_CIRRUS_CLASSES)}

        samples = []
        for img_path in sorted(
            list(root.rglob("*.jpg"))
            + list(root.rglob("*.jpeg"))
            + list(root.rglob("*.png"))
            + list(root.rglob("*.bmp"))
            + list(root.rglob("*.tif"))
            + list(root.rglob("*.tiff"))
        ):
            path_lower = str(img_path).lower()
            relative_path = img_path.relative_to(root)
            lbl = next(
                (idx for cls_name, idx in class_to_idx.items() if cls_name in path_lower),
                None,
            )
            samples.append(
                DatasetSample(
                    image_path=str(img_path),
                    label=lbl,
                    sample_id="_".join(relative_path.with_suffix("").parts),
                    metadata={
                        "split": split,
                        "volume": relative_path.parent.as_posix(),
                    },
                )
            )
        return samples



# ---------------------------------------------------------------------------
# OLIVES: Ophthalmic Labels for Investigating Visual Eye Semantics
# ---------------------------------------------------------------------------

OLIVES_BIOMARKERS = [
    "Fluid",
    "Hard Exudate",
    "Soft Exudate",
    "Drusen",
    "Scar",
    "Laser Scar",
    "Fibrovascular PED",
    "Serous PED",
]


class OLIVESDataset(EyeDataHubDataset):
    """
    OLIVES: Ophthalmic Labels for Investigating Visual Eye Semantics.

    Longitudinal OCT dataset pairing retinal B-scan images with 8 binary
    biomarker labels (fluid, drusen, scarring, PED, etc.) from AMD/DME
    patients across multiple clinical visits. Also includes fundus photos
    and BCVA/CST clinical measures.

    HuggingFace: https://huggingface.co/datasets/gOLIVES/OLIVES_Dataset
    Zenodo:      https://zenodo.org/records/7105232
    """

    _SUBDIR = "olives"
    _ZENODO_ID = "7105232"
    _HF_ID = "gOLIVES/OLIVES_Dataset"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="olives",
            full_name="OLIVES: Ophthalmic Labels for Investigating Visual Eye Semantics",
            description=(
                "Longitudinal OCT + fundus dataset from AMD/DME patients across "
                "multiple clinical visits. 9,408 OCT B-scans have biomarker labels "
                "for 8 categories (fluid, drusen, scarring, PED variants, etc.); "
                "78,000+ images include clinical measurements (BCVA, CST). "
                "Also includes 1,268 paired fundus photographs."
            ),
            modality="oct",
            tasks=["multilabel", "classification"],
            num_samples=9408,
            splits=["train", "val", "test"],
            classes=OLIVES_BIOMARKERS,
            num_classes=8,
            download_type="zenodo",
            download_url="https://zenodo.org/records/7105232",
            license="CC BY 4.0",
            citation=(
                "Prabhushankar M et al., 'OLIVES Dataset: Ophthalmic Labels for "
                "Investigating Visual Eye Semantics', NeurIPS Datasets & Benchmarks 2022. "
                "https://zenodo.org/records/7105232"
            ),
            tags=["oct", "amd", "dme", "multilabel", "zenodo", "longitudinal"],
            size_gb=20.0,
            notes=(
                "9,408 biomarker-labelled B-scans from 96 patients (6 clinical visits × "
                "49 B-scans/visit). Full OCT volume set ~62,000 B-scans. "
                "Also available on HuggingFace: gOLIVES/OLIVES_Dataset. "
                "Contains paired fundus photos and clinical metadata."
            ),
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return (
            len(list(root.glob("**/*.png"))) > 100
            or len(list(root.glob("**/*.jpg"))) > 100
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        dest = Path(data_dir) / self._SUBDIR
        # Try Zenodo first (no auth needed)
        try:
            download_zenodo(self._ZENODO_ID, dest)
            for archive in list(dest.glob("*.zip")) + list(dest.glob("*.tar*")):
                extract_archive(archive, dest)
            return
        except Exception as e:
            print(f"[OLIVES] Zenodo download failed ({e}), trying HuggingFace...")
        # Fallback: HuggingFace
        try:
            download_huggingface(self._HF_ID, dest, repo_type="dataset")
        except Exception:
            print_manual_download_instructions(
                "OLIVES",
                "https://zenodo.org/records/7105232",
                dest,
                extra_notes=(
                    "Also available at:\n"
                    "  https://huggingface.co/datasets/gOLIVES/OLIVES_Dataset\n"
                    "  pip install huggingface_hub && huggingface-cli download gOLIVES/OLIVES_Dataset"
                ),
            )
            raise

    def load(
        self, data_dir: Union[str, Path], split: str = "train"
    ) -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR

        # OLIVES ships with train/val/test CSVs listing image paths + biomarker columns
        csv_candidates = (
            list(root.glob(f"*{split}*.csv"))
            + list(root.glob(f"**/*{split}*.csv"))
            + list(root.glob("*.csv"))
            + list(root.glob("**/*.csv"))
        )

        if csv_candidates:
            df = pd.read_csv(csv_candidates[0])
            id_col = next(
                (c for c in df.columns if any(
                    kw in c.lower() for kw in ("image", "file", "path", "oct")
                )), df.columns[0]
            )
            biomarker_cols = [c for c in df.columns if c in OLIVES_BIOMARKERS]
            if not biomarker_cols:
                biomarker_cols = [
                    c for c in df.columns[1:]
                    if df[c].dropna().isin([0, 1]).all()
                ]
            samples = []
            for _, row in df.iterrows():
                img_rel = str(row[id_col])
                img_path = root / img_rel
                if not img_path.exists():
                    candidates = list(root.rglob(Path(img_rel).name))
                    img_path = candidates[0] if candidates else img_path
                lbl = (
                    [int(row[c]) for c in biomarker_cols]
                    if biomarker_cols else None
                )
                samples.append(
                    DatasetSample(
                        image_path=str(img_path),
                        label=lbl,
                        sample_id=Path(img_rel).stem,
                        metadata={"split": split, "biomarkers": biomarker_cols},
                    )
                )
            return samples

        # Fallback: collect all OCT images
        images = sorted(
            list(root.rglob("*.png"))
            + list(root.rglob("*.jpg"))
        )
        if not images:
            raise FileNotFoundError(
                f"No images found in {root}. "
                "Run: eyehub download --datasets olives"
            )
        return [
            DatasetSample(
                image_path=str(p),
                label=None,
                sample_id=p.stem,
                metadata={"split": split},
            )
            for p in images
        ]


# ---------------------------------------------------------------------------
# Rasti OCT Classification Dataset (Rabbani Lab / Noor Eye Hospital, Tehran)
# ---------------------------------------------------------------------------

RASTI_CLASSES = ["Normal", "AMD", "DME"]


class RastiDataset(EyeDataHubDataset):
    """
    Rasti (Rabbani) OCT Classification Dataset.

    148 Heidelberg Spectralis SD-OCT volumes (~4,254 B-scans) from Noor Eye
    Hospital, Tehran. Three-class volume-level classification: Normal (50),
    AMD (48), DME (50). Variable B-scan counts per volume (19/25/31/61 slices).

    Password-protected Google Drive archive:
      Main archive: https://drive.google.com/file/d/1Rv82F7CjPveyONdy1YbRHh05emCb6_Eu
    DME labels:    https://drive.google.com/file/d/1ocxB44TiiInE-jnt8Go6XQNmFwdTxOyN
    AMD labels:    https://drive.google.com/file/d/1yaNiK40QL_s7fgMLM98l_F3TCMwFERnP

    Paper: IEEE TMI 37(4):1024–1034 (2018) — doi:10.1109/TMI.2017.2780115
    """

    _SUBDIR = "rasti_oct"
    _GDRIVE_MAIN_ID = "1Rv82F7CjPveyONdy1YbRHh05emCb6_Eu"
    _GDRIVE_DME_LABELS = "1ocxB44TiiInE-jnt8Go6XQNmFwdTxOyN"
    _GDRIVE_AMD_LABELS = "1yaNiK40QL_s7fgMLM98l_F3TCMwFERnP"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="rasti_oct",
            full_name="Rasti OCT Dataset (Noor Eye Hospital, Tehran)",
            description=(
                "148 Heidelberg Spectralis SD-OCT volumes (~4,254 B-scans) "
                "for 3-class volume-level classification: Normal (50 volumes), "
                "AMD (48 volumes), DME (50 volumes). "
                "Variable B-scans per volume: 19, 25, 31, or 61 slices. "
                "Acquired at Noor Eye Hospital, Tehran, Iran."
            ),
            modality="oct",
            tasks=["classification"],
            num_samples=4254,
            splits=["train"],
            classes=RASTI_CLASSES,
            num_classes=3,
            download_type="manual",
            download_url=(
                "https://drive.google.com/file/d/"
                "1Rv82F7CjPveyONdy1YbRHh05emCb6_Eu"
            ),
            license="Research use only",
            citation=(
                "Rasti R et al., 'Macular OCT Classification Using a Multi-Scale "
                "Convolutional Neural Network Ensemble', "
                "IEEE Transactions on Medical Imaging 37(4):1024–1034 (2018). "
                "doi:10.1109/TMI.2017.2780115"
            ),
            tags=["oct", "classification", "amd", "dme", "gdrive", "manual"],
            size_gb=2.0,
            notes=(
                "The Google Drive archive is password-protected. Obtain the "
                "current archive password from the official source and download manually:\n"
                "  Main archive: https://drive.google.com/file/d/"
                "1Rv82F7CjPveyONdy1YbRHh05emCb6_Eu\n"
                "  DME labels:   https://drive.google.com/file/d/"
                "1ocxB44TiiInE-jnt8Go6XQNmFwdTxOyN\n"
                "  AMD labels:   https://drive.google.com/file/d/"
                "1yaNiK40QL_s7fgMLM98l_F3TCMwFERnP\n"
                "Label files flag 'suspicious' B-scans (≥50% threshold) "
                "within each volume."
            ),
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return (
            len(list(root.rglob("*.tif*"))) > 50
            or len(list(root.rglob("*.png"))) > 50
            or len(list(root.rglob("*.jpg"))) > 50
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        dest = Path(data_dir) / self._SUBDIR
        print_manual_download_instructions(
            "Rasti OCT",
            f"https://drive.google.com/file/d/{self._GDRIVE_MAIN_ID}",
            dest,
            extra_notes=(
                "The Google Drive archive is password-protected. Obtain the current "
                "archive password from the official source.\n\n"
                "Step 1 - Download main archive:\n"
                f"  https://drive.google.com/file/d/{self._GDRIVE_MAIN_ID}\n\n"
                "Step 2 - Download label files:\n"
                f"  DME labels: https://drive.google.com/file/d/{self._GDRIVE_DME_LABELS}\n"
                f"  AMD labels: https://drive.google.com/file/d/{self._GDRIVE_AMD_LABELS}\n\n"
                f"Step 3 - Extract archive and label files into:\n  {dest}\n\n"
                "Dataset is also described on Hossein Rabbani's lab website:\n"
                "  https://hrabbani.site123.me/available-datasets"
            ),
        )
        raise RuntimeError(
            "Rasti OCT requires password-protected manual download. "
            "See instructions above."
        )

    def load(
        self, data_dir: Union[str, Path], split: str = "train"
    ) -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR

        # Build volume-level label map from label files if present
        label_map: dict = {}
        for condition, label_idx in [("DME", 2), ("AMD", 1), ("Normal", 0)]:
            for label_file in list(root.glob(f"*{condition}*")) + list(
                root.glob(f"*{condition.lower()}*")
            ):
                if label_file.suffix in (".txt", ".csv", ".xlsx"):
                    try:
                        import pandas as pd
                        if label_file.suffix == ".xlsx":
                            df = pd.read_excel(str(label_file))
                        else:
                            df = pd.read_csv(str(label_file), header=None)
                        for val in df.iloc[:, 0].dropna():
                            label_map[str(val).strip()] = label_idx
                    except Exception:
                        pass

        # Collect images; infer class from path if no label map
        images = sorted(
            list(root.rglob("*.tif"))
            + list(root.rglob("*.tiff"))
            + list(root.rglob("*.png"))
            + list(root.rglob("*.jpg"))
        )

        class_kw = {"normal": 0, "amd": 1, "dme": 2}

        samples = []
        for p in images:
            path_lower = str(p).lower()
            lbl = label_map.get(p.stem) or label_map.get(p.name)
            if lbl is None:
                lbl = next(
                    (idx for kw, idx in class_kw.items() if kw in path_lower),
                    None,
                )
            samples.append(
                DatasetSample(
                    image_path=str(p),
                    label=lbl,
                    sample_id=p.stem,
                    metadata={"split": split},
                )
            )

        if not samples:
            raise FileNotFoundError(
                f"No images found in {root}. "
                "Run: eyehub download --datasets rasti_oct "
                "(password-protected manual download required)"
            )
        return samples
