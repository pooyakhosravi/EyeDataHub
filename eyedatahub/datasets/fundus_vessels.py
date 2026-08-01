"""Fundus vessel segmentation datasets: STARE, CHASE_DB1, HRF, FIVES, RAVIR."""
from __future__ import annotations

import gzip
import shutil
from pathlib import Path
from typing import List, Union

from eyedatahub.core.dataset import DatasetInfo, DatasetSample, EyeDataHubDataset
from eyedatahub.datasets.download_utils import (
    download_file,
    download_figshare,
    download_gdrive,
    extract_archive,
    print_manual_download_instructions,
)


# ---------------------------------------------------------------------------
# STARE
# ---------------------------------------------------------------------------

class STAREDataset(EyeDataHubDataset):
    """
    STARE: Structured Analysis of the Retina.

    20 fundus images with two sets of manual annotations.
    """

    _SUBDIR = "STARE"

    @staticmethod
    def _decompress_members(root: Path) -> None:
        for compressed in root.rglob("*.gz"):
            destination = compressed.with_suffix("")
            with gzip.open(compressed, "rb") as source:
                with destination.open("wb") as output:
                    shutil.copyfileobj(source, output)
            compressed.unlink()

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="stare",
            full_name="STARE: Structured Analysis of the Retina",
            description="20 fundus images with manual vessel segmentation (two annotators).",
            modality="fundus",
            tasks=["segmentation"],
            num_samples=20,
            splits=["all"],
            image_size=(700, 605),
            download_type="direct",
            download_url="https://cecas.clemson.edu/~ahoover/stare/",
            license="Research only",
            citation=(
                "Hoover et al., 'Locating blood vessels in retinal images by piece-wise "
                "threshold probing of a matched filter response', IEEE TMI 2000."
            ),
            tags=["vessel_segmentation", "fundus"],
            size_gb=0.02,
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return any(root.rglob("*.ppm")) or any(root.rglob("*.tif"))

    def download(self, data_dir: Union[str, Path]) -> None:
        root = Path(data_dir) / self._SUBDIR
        root.mkdir(parents=True, exist_ok=True)
        # The official HTTPS host currently presents a certificate chain that
        # is rejected by common Python CA bundles. The same official static
        # files are served over HTTP.
        base_url = "http://cecas.clemson.edu/~ahoover/stare/probing"

        # Images
        img_tar = root / "stare-images.tar"
        download_file(f"{base_url}/stare-images.tar", img_tar, desc="STARE images")
        extract_archive(img_tar, root / "images")
        img_tar.unlink(missing_ok=True)
        self._decompress_members(root / "images")

        # Labels (first annotator)
        lbl_tar = root / "labels-ah.tar"
        download_file(f"{base_url}/labels-ah.tar", lbl_tar, desc="STARE labels (ah)")
        extract_archive(lbl_tar, root / "labels_ah")
        lbl_tar.unlink(missing_ok=True)
        self._decompress_members(root / "labels_ah")

    def load(
        self, data_dir: Union[str, Path], split: str = "all"
    ) -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR
        images_dir = root / "images" if (root / "images").exists() else root
        labels_dir = root / "labels_ah" if (root / "labels_ah").exists() else root

        img_paths = sorted(
            list(images_dir.glob("*.ppm")) + list(images_dir.glob("*.tif"))
        )
        samples = []
        for img_path in img_paths:
            stem = img_path.stem
            # Label files have same stem but .ah.ppm or .tif extension
            label_candidates = (
                list(labels_dir.glob(f"{stem}.ah.ppm"))
                + list(labels_dir.glob(f"{stem}.ppm"))
                + list(labels_dir.glob(f"{stem}.png"))
            )
            mask_path = label_candidates[0] if label_candidates else ""
            samples.append(
                DatasetSample(
                    image_path=str(img_path),
                    label=str(mask_path),
                    sample_id=stem,
                    metadata={"split": split},
                )
            )
        return samples


# ---------------------------------------------------------------------------
# CHASE_DB1
# ---------------------------------------------------------------------------

class CHASE_DB1Dataset(EyeDataHubDataset):
    """
    CHASE_DB1: Child Heart and Health Study in England, Database 1.

    28 retinal images from 14 children with two manual annotations each.
    """

    _SUBDIR = "CHASE_DB1"
    _CHASE_AV_URL = "https://researchinnovation.kingston.ac.uk/en/datasets/chase-av-retinal-vessel-reference-dataset/"
    _CHASE_DB1_URL = "https://researchinnovation.kingston.ac.uk/en/datasets/chasedb1-retinal-vessel-reference-dataset-4/"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="chase_db1",
            full_name="CHASE_DB1: Child Heart and Health Study in England",
            description="28 fundus images with manual vessel segmentations (two annotators).",
            modality="fundus",
            tasks=["segmentation"],
            num_samples=28,
            splits=["all"],
            image_size=(999, 960),
            download_type="manual",
            download_url=self._CHASE_DB1_URL,
            license="CC BY 4.0",
            citation=(
                "Owen et al., 'Measuring retinal vessel tortuosity in 10-year-old "
                "children: validation of the computer-assisted image analysis of the "
                "retina (CAIAR) program', Invest Ophthalmol Vis Sci 2009. "
                f"Data: {self._CHASE_DB1_URL}; CHASE-AV reference: {self._CHASE_AV_URL}"
            ),
            tags=["vessel_segmentation", "fundus", "pediatric"],
            size_gb=0.05,
            notes=(
                "Manual access only. Kingston landing pages: "
                f"CHASE_DB1: {self._CHASE_DB1_URL}; CHASE-AV: {self._CHASE_AV_URL}"
            ),
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return len(list(root.glob("Image_*.jpg"))) > 0

    def download(self, data_dir: Union[str, Path]) -> None:
        data_dir = Path(data_dir)
        print_manual_download_instructions(
            "CHASE_DB1 / CHASE-AV",
            self._CHASE_DB1_URL,
            data_dir / self._SUBDIR,
            extra_notes=(
                "Use the Kingston landing pages:\n"
                f"  CHASE_DB1: {self._CHASE_DB1_URL}\n"
                f"  CHASE-AV: {self._CHASE_AV_URL}\n"
                "Place all Image_*.jpg and Image_*_1stHO.png files into the directory."
            ),
        )
        raise RuntimeError("CHASE_DB1 requires manual download from Kingston Research Innovation.")

    def load(
        self, data_dir: Union[str, Path], split: str = "all"
    ) -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR
        img_paths = sorted(root.glob("Image_*.jpg"))
        samples = []
        for img_path in img_paths:
            stem = img_path.stem  # e.g. Image_01L
            mask_candidates = list(root.glob(f"{stem}_1stHO.png")) + list(
                root.glob(f"{stem}_1stHO.tif")
            )
            mask_path = mask_candidates[0] if mask_candidates else ""
            samples.append(
                DatasetSample(
                    image_path=str(img_path),
                    label=str(mask_path),
                    sample_id=stem,
                    metadata={"split": split},
                )
            )
        return samples


# ---------------------------------------------------------------------------
# HRF
# ---------------------------------------------------------------------------

class HRFDataset(EyeDataHubDataset):
    """
    HRF: High-Resolution Fundus Image Database.

    45 high-resolution fundus images (15 healthy, 15 DR, 15 glaucomatous)
    with manual vessel annotations.
    """

    _SUBDIR = "HRF"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="hrf",
            full_name="HRF: High-Resolution Fundus Image Database",
            description=(
                "45 high-resolution fundus images (healthy/DR/glaucoma) with "
                "manual vessel segmentation."
            ),
            modality="fundus",
            tasks=["segmentation"],
            num_samples=45,
            splits=["all"],
            image_size=(3504, 2336),
            download_type="manual",
            download_url="https://www5.cs.fau.de/research/data/fundus-images/",
            license="CC BY 4.0",
            citation=(
                "Budai et al., 'Robust vessel segmentation in fundus images', "
                "Intl Journal of Biomedical Imaging 2013."
            ),
            tags=["vessel_segmentation", "fundus", "high_resolution"],
            size_gb=0.5,
            notes="Requires manual download from FAU Erlangen-Nuremberg website.",
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return len(list(root.glob("images/*.jpg"))) > 0

    def download(self, data_dir: Union[str, Path]) -> None:
        root = Path(data_dir) / self._SUBDIR
        print_manual_download_instructions(
            "HRF",
            "https://www5.cs.fau.de/research/data/fundus-images/",
            root,
            extra_notes=(
                "Download all image files and manual segmentation masks.\n"
                "Expected layout:\n"
                "  HRF/images/*.jpg\n"
                "  HRF/manual/*.tif"
            ),
        )
        raise RuntimeError("HRF requires manual download.")

    def load(
        self, data_dir: Union[str, Path], split: str = "all"
    ) -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR
        images_dir = root / "images"
        manual_dir = root / "manual"

        samples = []
        for img_path in sorted(images_dir.glob("*.jpg")):
            stem = img_path.stem
            mask_candidates = list(manual_dir.glob(f"{stem}*.tif"))
            mask_path = mask_candidates[0] if mask_candidates else ""
            samples.append(
                DatasetSample(
                    image_path=str(img_path),
                    label=str(mask_path),
                    sample_id=stem,
                    metadata={"split": split},
                )
            )
        return samples


# ---------------------------------------------------------------------------
# FIVES
# ---------------------------------------------------------------------------

class FIVESDataset(EyeDataHubDataset):
    """
    FIVES: A Fundus Image Dataset for Artificial Intelligence based Vessel Segmentation.

    800 high-resolution color fundus images (2048x2048) with pixel-wise vessel
    segmentation masks. Covers normal, DR, AMD, and glaucoma cases.

    Published in Scientific Data (Nature), freely available on Figshare.
    """

    _SUBDIR = "fives"
    _FIGSHARE_ID = "19688169"
    _FIGSHARE_URL = "https://doi.org/10.6084/m9.figshare.19688169"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="fives",
            full_name="FIVES: Fundus Image Vessel Segmentation",
            description=(
                "800 high-resolution (2048x2048) fundus images with pixel-wise "
                "vessel segmentation. Covers normal, DR, AMD, glaucoma."
            ),
            modality="fundus",
            tasks=["segmentation"],
            num_samples=800,
            splits=["train", "test"],
            image_size=(2048, 2048),
            download_type="figshare",
            download_url=self._FIGSHARE_URL,
            license="CC BY 4.0",
            citation=(
                "Jin et al., 'FIVES: A Fundus Image Dataset for Artificial "
                "Intelligence based Vessel Segmentation', Scientific Data 2022."
            ),
            tags=["vessel_segmentation", "fundus", "high_resolution"],
            size_gb=1.1,
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return len(list(root.glob("**/*.png"))) > 100

    def download(self, data_dir: Union[str, Path]) -> None:
        root = Path(data_dir) / self._SUBDIR
        root.mkdir(parents=True, exist_ok=True)
        download_figshare(self._FIGSHARE_ID, root)
        for archive in list(root.glob("*.zip")) + list(root.glob("*.tar*")):
            extract_archive(archive, root)

    def load(self, data_dir: Union[str, Path], split: str = "test") -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR
        split_dirs = [
            candidate
            for candidate in root.rglob("*")
            if candidate.is_dir() and candidate.name.casefold() == split.casefold()
        ]
        split_dir = next(
            (
                candidate
                for candidate in split_dirs
                if (candidate / "Original").is_dir()
                or (candidate / "images").is_dir()
            ),
            split_dirs[0] if split_dirs else root,
        )

        img_dirs = [split_dir / "Original", split_dir / "images", split_dir]
        img_dir = next((d for d in img_dirs if d.exists()), split_dir)

        mask_dirs = [split_dir / "Ground truth", split_dir / "masks", split_dir / "GT"]
        mask_dir = next((d for d in mask_dirs if d.exists()), None)

        samples = []
        image_paths = sorted(img_dir.glob("*.png")) + sorted(img_dir.glob("*.jpg"))
        for img_path in image_paths:
            stem = img_path.stem
            mask_path = ""
            if mask_dir:
                candidates = list(mask_dir.glob(f"{stem}*.png")) + list(mask_dir.glob(f"{stem}*.tif"))
                mask_path = str(candidates[0]) if candidates else ""
            samples.append(DatasetSample(
                image_path=str(img_path),
                label=mask_path,
                sample_id=stem,
                metadata={"split": split},
            ))
        return samples


# ---------------------------------------------------------------------------
# RAVIR
# ---------------------------------------------------------------------------

class RAVIRDataset(EyeDataHubDataset):
    """
    RAVIR: Retinal Artery/Vein segmentation in Infrared Reflectance imaging.

    42 infrared reflectance fundus images with artery and vein segmentation masks.
    Available from the RAVIR Grand Challenge.
    """

    _SUBDIR = "ravir"
    _GDRIVE_ID = "1ZlZoSStvE9VCRq3bJiGhQH931EF0h3hh"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="ravir",
            full_name="RAVIR: Retinal Artery/Vein Segmentation in IR",
            description=(
                "42 infrared reflectance fundus images with separate artery "
                "and vein segmentation masks. 23 train / 19 test."
            ),
            modality="fundus",
            tasks=["segmentation"],
            num_samples=42,
            splits=["train", "test"],
            image_size=(768, 768),
            download_type="gdrive",
            download_url="https://ravir.grand-challenge.org/data/",
            license="Research only",
            citation=(
                "Hatamizadeh et al., 'RAVIR: A Dataset and Methodology for the "
                "Semantic Segmentation and Quantitative Analysis of Retinal "
                "Arteries and Veins in Infrared Reflectance Imaging', JBHI 2022."
            ),
            tags=["vessel_segmentation", "artery_vein", "infrared", "fundus"],
            size_gb=0.05,
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return len(list(root.glob("**/*.png"))) > 10

    def download(self, data_dir: Union[str, Path]) -> None:
        dest = Path(data_dir) / self._SUBDIR
        dest.mkdir(parents=True, exist_ok=True)
        archive = dest / "ravir.zip"
        try:
            download_gdrive(self._GDRIVE_ID, archive)
            extract_archive(archive, dest)
            archive.unlink(missing_ok=True)
        except Exception:
            print_manual_download_instructions(
                "RAVIR",
                "https://ravir.grand-challenge.org/data/",
                dest,
                extra_notes=(
                    "Expected structure:\n"
                    "  ravir/training/training_images/*.png\n"
                    "  ravir/training/training_masks/*.png\n"
                    "  ravir/test/test_images/*.png"
                ),
            )
            raise

    def load(self, data_dir: Union[str, Path], split: str = "test") -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR
        split_name = "training" if split == "train" else split
        img_dir = root / split_name / f"{split_name}_images"
        if not img_dir.exists():
            img_dir = root / split / "images"
        if not img_dir.exists():
            img_dir = root / split
        if not img_dir.exists():
            raise FileNotFoundError(f"RAVIR {split} images not found under {root}.")

        mask_dir = root / split_name / f"{split_name}_masks"
        if not mask_dir.exists():
            mask_dir = None

        samples = []
        for img_path in sorted(img_dir.glob("*.png")) + sorted(img_dir.glob("*.tif")):
            stem = img_path.stem
            mask_path = ""
            if mask_dir:
                candidates = list(mask_dir.glob(f"{stem}*.png"))
                mask_path = str(candidates[0]) if candidates else ""
            samples.append(DatasetSample(
                image_path=str(img_path),
                label=mask_path,
                sample_id=stem,
                metadata={"split": split},
            ))
        return samples
