"""
STAGE Challenge (MICCAI 2023) — Structural-functional TrAnsition GlaucomatE.

Three tasks predicting visual field measurements from macular OCT images:
  Task 1: Mean Deviation (MD) prediction (scalar regression)
  Task 2: Sensitivity map prediction (52-point visual field, 0–100 dB)
  Task 3: Pattern Deviation Probability map prediction (52-point map)

Dataset access: https://aistudio.baidu.com/aistudio/competition/detail/968/0/introduction
Registration on Baidu AI Studio is required.

GitHub references:
  Task 1: https://github.com/Rebeccalomi/MICCAI2023-STAGE_Task1
  Task 2: https://github.com/lixiangcog/STAGE_baseline2
  Task 3: https://github.com/zhuolingli/MICCAI2023-Challenge-STAGE-TASK-3
"""
from __future__ import annotations

from pathlib import Path
from typing import Any, List, Optional, Union

import numpy as np
from PIL import Image

from eyedatahub.core.dataset import DatasetInfo, DatasetSample, EyeDataHubDataset
from eyedatahub.datasets.download_utils import print_manual_download_instructions

_STAGE_URL = "https://aistudio.baidu.com/aistudio/competition/detail/968/0/datasets"
_STAGE_NOTE = (
    "STAGE 2023 has NO public mirror (verified 2026-07). All 3 baseline\n"
    "repos + the MICCAI 2023 Springer chapter point to Baidu AI Studio\n"
    "as sole distribution. Automated download blocked by Baidu SSO.\n\n"
    "1. Register / log in at https://aistudio.baidu.com\n"
    "2. Join the STAGE challenge (comp 968) and accept the data agreement\n"
    "3. Download the dataset ZIP from the datasets tab\n"
    "4. Extract into the destination directory\n\n"
    "Expected layout after extraction:\n"
    "  <dest>/oct/           - OCT B-scan volumes\n"
    "  <dest>/task1_gt.xlsx  - Task 1 MD labels\n"
    "  <dest>/task2_GT_training.xlsx  - Task 2 sensitivity labels\n"
    "  <dest>/task3_gt.xlsx  - Task 3 probability labels\n"
)


class _STAGEBase(EyeDataHubDataset):
    """Shared helpers for all three STAGE task datasets."""

    _SUBDIR: str = "stage_challenge"

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return root.exists() and (
            any(root.rglob("*.jpg")) or
            any(root.rglob("*.png")) or
            any(root.rglob("*.nii")) or
            any(root.rglob("*.npy"))
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        dest = Path(data_dir) / self._SUBDIR
        print_manual_download_instructions(
            "STAGE Challenge (MICCAI 2023)",
            _STAGE_URL,
            dest,
            extra_notes=_STAGE_NOTE,
        )
        raise RuntimeError(
            "STAGE dataset requires manual download from Baidu AI Studio."
        )

    def _load_label_excel(
        self, excel_path: Path, id_col: str, label_col: Any
    ) -> dict:
        """Load an Excel label file into a {sample_id: label} dict."""
        try:
            import pandas as pd
            df = pd.read_excel(str(excel_path))
            if isinstance(label_col, list):
                return {
                    str(row[id_col]): row[label_col].values.tolist()
                    for _, row in df.iterrows()
                }
            return {str(row[id_col]): row[label_col] for _, row in df.iterrows()}
        except Exception:
            return {}

    def _image_paths(self, root: Path) -> List[Path]:
        exts = (".jpg", ".jpeg", ".png", ".tif", ".tiff", ".bmp")
        return sorted(p for ext in exts for p in root.rglob(f"*{ext}"))


# ---------------------------------------------------------------------------
# Task 1: Mean Deviation prediction
# ---------------------------------------------------------------------------

class STAGETask1Dataset(_STAGEBase):
    """
    STAGE Task 1: Predict glaucoma Mean Deviation (MD, in dB) from macular OCT.

    400 OCT volume samples; MD ranges from approximately −30 to 0 dB.
    Task: regression (lower MD = more severe glaucoma).
    """

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="stage_task1",
            full_name="STAGE 2023 Task 1 — Mean Deviation Prediction from OCT",
            description=(
                "400 macular OCT volumes; predict glaucoma Mean Deviation (MD, dB) "
                "from 24-2 Humphrey visual field test. Scalar regression task."
            ),
            modality="oct",
            tasks=["regression"],
            num_samples=400,
            splits=["train", "test"],
            download_type="manual",
            download_url=_STAGE_URL,
            license="Non-commercial research (Baidu AI Studio)",
            citation=(
                "MICCAI 2023 STAGE Challenge. "
                "https://aistudio.baidu.com/aistudio/competition/detail/968"
            ),
            tags=["oct", "glaucoma", "visual_field", "regression", "stage", "miccai2023"],
            size_gb=5.0,
            notes="Registration on Baidu AI Studio required. All 3 tasks share the same OCT volume set (~5 GB).",
        )

    def load(
        self, data_dir: Union[str, Path], split: str = "train"
    ) -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR
        images = self._image_paths(root)
        if not images:
            raise FileNotFoundError(
                f"No images found in {root}. "
                "Run: eyehub download --datasets stage_task1"
            )

        label_path = root / "task1_gt.xlsx"
        label_map = (
            self._load_label_excel(label_path, id_col="ID", label_col="MD")
            if label_path.exists() else {}
        )

        return [
            DatasetSample(
                image_path=str(p),
                label=label_map.get(p.stem, None),
                sample_id=p.stem,
                metadata={"task": "md_prediction"},
            )
            for p in images
        ]


# ---------------------------------------------------------------------------
# Task 2: Sensitivity map prediction
# ---------------------------------------------------------------------------

class STAGETask2Dataset(_STAGEBase):
    """
    STAGE Task 2: Predict 52-point visual field sensitivity map from OCT.

    Each label is a 52-element vector of sensitivity values (0–100 dB) at
    each of the 24-2 test locations (excluding the 2 blind-spot points).
    Task: multi-output regression.
    """

    # The 52 standard 24-2 visual field test point names (row-major, L→R)
    VF_POINTS = [f"VF_{i+1:02d}" for i in range(52)]

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="stage_task2",
            full_name="STAGE 2023 Task 2 — Visual Field Sensitivity Map Prediction",
            description=(
                "400 macular OCT volumes; predict 52-point Humphrey 24-2 "
                "visual field sensitivity map (0–100 dB per point). "
                "Multi-output regression."
            ),
            modality="oct",
            tasks=["regression"],
            num_samples=400,
            splits=["train", "test"],
            classes=self.VF_POINTS,
            num_classes=52,
            download_type="manual",
            download_url=_STAGE_URL,
            license="Non-commercial research (Baidu AI Studio)",
            citation=(
                "MICCAI 2023 STAGE Challenge. "
                "https://aistudio.baidu.com/aistudio/competition/detail/968"
            ),
            tags=["oct", "glaucoma", "visual_field", "regression", "stage", "miccai2023"],
            size_gb=5.0,
            notes="Labels in task2_GT_training.xlsx (52 columns per sample). All 3 tasks share the same OCT volume set.",
        )

    def load(
        self, data_dir: Union[str, Path], split: str = "train"
    ) -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR
        images = self._image_paths(root)
        if not images:
            raise FileNotFoundError(
                f"No images in {root}. Run: eyehub download --datasets stage_task2"
            )

        label_path = root / "task2_GT_training.xlsx"
        label_map: dict = {}
        if label_path.exists():
            try:
                import pandas as pd
                df = pd.read_excel(str(label_path))
                vf_cols = [c for c in df.columns if c not in ("ID", "id", "filename")]
                for _, row in df.iterrows():
                    sid = str(row.get("ID", row.get("id", row.iloc[0])))
                    label_map[sid] = row[vf_cols].values.astype(float).tolist()
            except Exception:
                pass

        return [
            DatasetSample(
                image_path=str(p),
                label=label_map.get(p.stem, None),
                sample_id=p.stem,
                metadata={"task": "sensitivity_map", "n_points": 52},
            )
            for p in images
        ]


# ---------------------------------------------------------------------------
# Task 3: Pattern Deviation Probability map prediction
# ---------------------------------------------------------------------------

class STAGETask3Dataset(_STAGEBase):
    """
    STAGE Task 3: Predict 52-point pattern deviation probability map from OCT.

    Each label is a 52-element vector where each value is the probability (0–1)
    of deviation at each 24-2 visual field location.
    Task: multi-output regression / binary classification per point.
    """

    VF_POINTS = [f"PD_{i+1:02d}" for i in range(52)]

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="stage_task3",
            full_name="STAGE 2023 Task 3 — Pattern Deviation Probability Map",
            description=(
                "400 macular OCT volumes; predict 52-point pattern deviation "
                "probability map from 24-2 Humphrey visual field test. "
                "Multi-output regression."
            ),
            modality="oct",
            tasks=["regression"],
            num_samples=400,
            splits=["train", "test"],
            classes=self.VF_POINTS,
            num_classes=52,
            download_type="manual",
            download_url=_STAGE_URL,
            license="Non-commercial research (Baidu AI Studio)",
            citation=(
                "MICCAI 2023 STAGE Challenge. "
                "https://aistudio.baidu.com/aistudio/competition/detail/968"
            ),
            tags=["oct", "glaucoma", "visual_field", "regression", "stage", "miccai2023"],
            size_gb=5.0,
        )

    def load(
        self, data_dir: Union[str, Path], split: str = "train"
    ) -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR
        images = self._image_paths(root)
        if not images:
            raise FileNotFoundError(
                f"No images in {root}. Run: eyehub download --datasets stage_task3"
            )

        label_path = root / "task3_gt.xlsx"
        label_map: dict = {}
        if label_path.exists():
            try:
                import pandas as pd
                df = pd.read_excel(str(label_path))
                pd_cols = [c for c in df.columns if c not in ("ID", "id", "filename")]
                for _, row in df.iterrows():
                    sid = str(row.get("ID", row.get("id", row.iloc[0])))
                    label_map[sid] = row[pd_cols].values.astype(float).tolist()
            except Exception:
                pass

        return [
            DatasetSample(
                image_path=str(p),
                label=label_map.get(p.stem, None),
                sample_id=p.stem,
                metadata={"task": "pattern_deviation_probability", "n_points": 52},
            )
            for p in images
        ]
