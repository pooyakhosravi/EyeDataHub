"""Age-related Macular Degeneration datasets: iChallenge-AMD."""
from __future__ import annotations

from pathlib import Path
from typing import List, Union

import pandas as pd

from eyedatahub.core.dataset import DatasetInfo, DatasetSample, EyeDataHubDataset
from eyedatahub.datasets.download_utils import print_manual_download_instructions


# ---------------------------------------------------------------------------
# iChallenge AMD
# ---------------------------------------------------------------------------

class iChallengeAMDDataset(EyeDataHubDataset):
    """
    iChallenge-AMD: Age-related Macular Degeneration Challenge Dataset.

    400 training + 400 test fundus images with AMD classification (normal,
    early AMD, intermediate AMD, advanced AMD) and lesion annotations.

    Organized by Baidu Research. Requires registration.
    """

    _SUBDIR = "ichallenge_amd"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="ichallenge_amd",
            full_name="iChallenge-AMD: Age-related Macular Degeneration",
            description=(
                "400 training fundus images with AMD classification (non-AMD vs AMD) "
                "and lesion annotations. Challenge dataset from ISBI 2020."
            ),
            modality="fundus",
            tasks=["classification"],
            num_samples=400,
            splits=["train", "test"],
            classes=["Non-AMD", "AMD"],
            num_classes=2,
            download_type="manual",
            download_url="https://amd.grand-challenge.org/download/",
            license="Research only — requires registration",
            citation=(
                "Fu et al., 'Age-Related Macular Degeneration and "
                "Pathologic Myopia Fundus Image Analysis Challenge', "
                "ISBI 2020."
            ),
            tags=["amd", "classification", "fundus"],
            size_gb=1.5,
            notes=(
                "Grand Challenge login is required:\n"
                "  https://amd.grand-challenge.org/download/\n"
                "The original Baidu BROAD portal has returned intermittent "
                "5xx errors since 2024. Alternative partial resource:\n"
                "- PaddleSeg optic-disc subset (~19 MB, direct HTTPS, "
                "no login): https://paddleseg.bj.bcebos.com/dataset/"
                "optic_disc_seg.zip\n"
                "The full 1.5 GB dataset is only via Grand Challenge or the "
                "Baidu portal."
            ),
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return len(list(root.glob("**/*.jpg"))) > 100 or len(list(root.glob("**/*.png"))) > 100

    def download(self, data_dir: Union[str, Path]) -> None:
        root = Path(data_dir) / self._SUBDIR
        print_manual_download_instructions(
            "iChallenge-AMD",
            "https://amd.grand-challenge.org/download/",
            root,
            extra_notes=(
                "1. Register or log in at https://amd.grand-challenge.org/download/\n"
                "2. Download the AMD training and test sets\n"
                "3. Extract and arrange:\n"
                "   ichallenge_amd/Training400/AMD/*.jpg\n"
                "   ichallenge_amd/Training400/Non-AMD/*.jpg\n"
                "   ichallenge_amd/Training400/Fovea_location.xlsx\n"
                "   ichallenge_amd/Testing400/Images/*.jpg"
            ),
        )
        raise RuntimeError("iChallenge-AMD requires manual download.")

    def load(
        self, data_dir: Union[str, Path], split: str = "train"
    ) -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR

        split_map = {"train": "Training400", "test": "Testing400"}
        split_dir = root / split_map.get(split, split)
        if not split_dir.exists():
            split_dir = root / split
        if not split_dir.exists():
            raise FileNotFoundError(f"iChallenge-AMD {split} directory not found: {root}")

        samples = []
        class_map = {"amd": 1, "non-amd": 0, "nonamd": 0, "normal": 0}

        # Training set has class subdirectories
        for cls_dir in sorted(split_dir.iterdir()):
            if not cls_dir.is_dir():
                continue
            label = class_map.get(cls_dir.name.lower().replace(" ", ""), -1)
            if label == -1:
                continue
            for img_path in sorted(cls_dir.glob("*.jpg")) + sorted(cls_dir.glob("*.png")):
                samples.append(
                    DatasetSample(
                        image_path=str(img_path),
                        label=label,
                        sample_id=img_path.stem,
                        metadata={"split": split, "class": cls_dir.name},
                    )
                )

        # Test set may have Images/ subdirectory (unlabeled or from labels CSV)
        if not samples:
            img_dir = split_dir / "Images" if (split_dir / "Images").exists() else split_dir
            for img_path in sorted(img_dir.glob("*.jpg")) + sorted(img_dir.glob("*.png")):
                samples.append(
                    DatasetSample(
                        image_path=str(img_path),
                        label=-1,
                        sample_id=img_path.stem,
                        metadata={"split": split},
                    )
                )
        return samples
