"""
JustRAIGS: Just Referral AI Glaucoma Screening dataset.

101,442 gradable fundus images labeled as referable or non-referable
for glaucoma by expert graders from the Rotterdam Eye Hospital.

Image data provided by EyePACS LLC, Santa Cruz, CA.
Labels provided by the Rotterdam Ophthalmic Institute / Rotterdam Eye Hospital.

License: CC BY-NC-SA
Dataset page: https://zenodo.org/records/10035093
"""
from __future__ import annotations

from pathlib import Path
from typing import List, Union

import pandas as pd

from eyedatahub.core.dataset import DatasetInfo, DatasetSample, EyeDataHubDataset
from eyedatahub.datasets.download_utils import (
    download_zenodo,
    extract_archive,
    print_manual_download_instructions,
)

ZENODO_RECORD_ID = "10035093"

JUSTRAIGS_CLASSES = ["No Referable Glaucoma", "Referable Glaucoma"]


class JustRAIGSDataset(EyeDataHubDataset):
    """
    JustRAIGS: Just Referral AI Glaucoma Screening.

    101,442 gradable fundus images (EyePACS) labeled by Rotterdam Eye Hospital
    graders as referable (RG) or non-referable (NRG) for glaucoma.
    The training set is publicly available under CC BY-NC-SA.

    Zenodo record: 10035093
    """

    _SUBDIR = "justraigs"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="justraigs",
            full_name="JustRAIGS: Just Referral AI Glaucoma Screening Dataset",
            description=(
                "101,442 gradable fundus images labeled as referable (RG) or "
                "non-referable (NRG) for glaucoma. Image data from EyePACS LLC; "
                "labels from Rotterdam Eye Hospital expert graders."
            ),
            modality="fundus",
            tasks=["classification"],
            num_samples=101442,
            splits=["train"],
            classes=JUSTRAIGS_CLASSES,
            num_classes=2,
            download_type="zenodo",
            download_url=f"https://zenodo.org/records/{ZENODO_RECORD_ID}",
            license="CC BY-NC-ND 4.0",
            citation=(
                "Thakoor et al., 'JustRAIGS: Justify Your Artificial Intelligence "
                "Prediction for Referable or Not Referable Glaucoma Screening', "
                "MICCAI 2023. Zenodo: https://zenodo.org/records/10035093"
            ),
            tags=["glaucoma", "fundus", "zenodo", "screening", "classification"],
            size_gb=100.0,
            notes=(
                "Large dataset (~100 GB). The record is publicly accessible "
                "but downloading requires accepting the CC BY-NC-ND terms on "
                "the Zenodo page. Set ZENODO_TOKEN in .env if access is denied."
            ),
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        # Accept if we have a labels CSV and at least some images
        has_csv = len(list(root.glob("**/*.csv"))) > 0
        has_images = len(list(root.glob("**/*.jpg"))) > 100 or len(list(root.glob("**/*.png"))) > 100
        return has_csv and has_images

    def download(self, data_dir: Union[str, Path]) -> None:
        dest = Path(data_dir) / self._SUBDIR
        try:
            download_zenodo(ZENODO_RECORD_ID, dest)
            for archive in list(dest.glob("*.zip")) + list(dest.glob("*.tar*")):
                extract_archive(archive, dest)
        except PermissionError as e:
            print_manual_download_instructions(
                "JustRAIGS",
                f"https://zenodo.org/records/{ZENODO_RECORD_ID}",
                dest,
                extra_notes=(
                    str(e) + "\n\n"
                    "If download is blocked, add to your .env:\n"
                    "  ZENODO_TOKEN=your_token\n\n"
                    "Create a token at:\n"
                    "  https://zenodo.org/account/settings/applications/\n\n"
                    "Then accept the CC BY-NC-SA license at:\n"
                    f"  https://zenodo.org/records/{ZENODO_RECORD_ID}"
                ),
            )
            raise

    def load(
        self, data_dir: Union[str, Path], split: str = "train"
    ) -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR

        # JustRAIGS typically ships a CSV with columns:
        #   image_id (or filename), label (NRG/RG or 0/1), [grader columns...]
        csv_candidates = (
            list(root.glob("JustRAIGS*.csv"))
            + list(root.glob("*.csv"))
            + list(root.glob("**/*.csv"))
        )

        label_map: dict = {}
        if csv_candidates:
            df = pd.read_csv(csv_candidates[0])
            # Identify image ID column
            id_col = next(
                (c for c in df.columns if any(
                    kw in c.lower() for kw in ("image", "file", "id", "name")
                )),
                df.columns[0],
            )
            # Identify label column
            lbl_col = next(
                (c for c in df.columns if any(
                    kw in c.lower() for kw in ("label", "class", "glaucoma", "rg", "referable")
                )),
                df.columns[1] if len(df.columns) > 1 else None,
            )
            if lbl_col:
                for _, row in df.iterrows():
                    img_id = str(row[id_col]).strip()
                    raw = str(row[lbl_col]).strip().upper()
                    # NRG = 0, RG = 1; also handle "0"/"1" or "No"/"Yes"
                    if raw in ("RG", "1", "YES", "TRUE", "REFERABLE"):
                        lbl = 1
                    else:
                        lbl = 0
                    label_map[img_id] = lbl

        # Collect all images
        images = sorted(
            list(root.rglob("*.jpg"))
            + list(root.rglob("*.jpeg"))
            + list(root.rglob("*.png"))
        )
        if not images:
            raise FileNotFoundError(
                f"No images found in {root}. "
                "Run: eyehub download --datasets justraigs"
            )

        samples = []
        for img_path in images:
            # Try stem, then stem without extension, then filename
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


# Alias retained for existing imports.
Zenodo10035093Dataset = JustRAIGSDataset
