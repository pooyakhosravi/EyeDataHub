"""Visual field / perimetry datasets: UWHVF, GRAPE."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Union

import numpy as np

from eyedatahub.core.dataset import DatasetInfo, DatasetSample, EyeDataHubDataset
from eyedatahub.datasets.download_utils import (
    download_figshare_collection,
    download_file,
    extract_archive,
    print_manual_download_instructions,
)


# ---------------------------------------------------------------------------
# UWHVF — University of Washington Humphrey Visual Field
# ---------------------------------------------------------------------------


class UWHVFDataset(EyeDataHubDataset):
    """
    UWHVF: University of Washington Humphrey Visual Field Database.

    28,943 standard automated perimetry (SAP) visual field tests from the
    Humphrey Field Analyzer (HFA 24-2). Real-world clinical data with
    longitudinal follow-up for glaucoma progression research.

    Each sample contains:
      - Per-point threshold sensitivities (52 points, 24-2 pattern)
      - Mean deviation (MD) and pattern standard deviation (PSD)
      - Glaucoma diagnosis label
      - Eye laterality (OD/OS)

    Note: This dataset contains VF data (not images). The 'image' is a
    52-element array of threshold values. Models should accept numpy arrays.

    Reference:
        Boland et al., "The University of Washington Humphrey Visual Field
        database: A repository of perimetric data for clinical research",
        Ophthalmic Epidemiology 2022.
    """

    _SUBDIR = "uwhvf"
    _GITHUB_URL = "https://github.com/uw-biomedical-ml/uwhvf"
    # Repo default branch is `master`, not `main` — main.zip 404s.
    _DATA_URL = "https://github.com/uw-biomedical-ml/uwhvf/archive/refs/heads/master.zip"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="uwhvf",
            full_name="UWHVF: University of Washington Humphrey Visual Field",
            description=(
                "28,943 HFA 24-2 visual field tests with per-point sensitivities, "
                "MD/PSD indices, glaucoma labels, and longitudinal follow-up data. "
                "Input: 52-element sensitivity array (not an image)."
            ),
            modality="visual_field",
            tasks=["classification", "regression"],
            num_samples=28943,
            splits=["all"],
            classes=["Non-glaucoma", "Glaucoma"],
            num_classes=2,
            download_type="direct",
            download_url=self._DATA_URL,
            license="CC BY 4.0",
            citation=(
                "Boland et al., 'The University of Washington Humphrey Visual "
                "Field database', Ophthalmic Epidemiology 2022."
            ),
            tags=["visual_field", "glaucoma", "perimetry", "longitudinal", "non_image"],
            size_gb=0.05,
            notes=(
                "Non-imaging dataset. Samples are 52-element visual field arrays. "
                "Models must accept 1D/2D VF arrays, not RGB images."
            ),
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return (
            len(list(root.glob("**/*.csv"))) > 0
            or len(list(root.glob("**/*.json"))) > 0
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        root = Path(data_dir) / self._SUBDIR
        root.mkdir(parents=True, exist_ok=True)
        dest_zip = Path(data_dir) / "uwhvf.zip"
        try:
            download_file(self._DATA_URL, dest_zip, desc="UWHVF dataset")
            extract_archive(dest_zip, root)
            dest_zip.unlink(missing_ok=True)
        except Exception:
            print_manual_download_instructions(
                "UWHVF",
                self._GITHUB_URL,
                root,
                extra_notes=(
                    "Clone or download from GitHub:\n"
                    "  git clone https://github.com/uw-biomedical-ml/uwhvf\n"
                    "Place the data files under:\n"
                    "  uwhvf/data/*.csv  or  uwhvf/data/*.json"
                ),
            )
            raise

    def load(
        self, data_dir: Union[str, Path], split: str = "all"
    ) -> List[DatasetSample]:
        """
        Load visual field samples.

        Returns DatasetSample where:
          - image_path: path to CSV/JSON (used as identifier)
          - label: int (0=non-glaucoma, 1=glaucoma)
          - metadata: includes 'vf_array' (np.ndarray, shape 52) and 'md', 'psd'
        """
        import csv

        root = Path(data_dir) / self._SUBDIR

        # Find the main data file
        csv_files = list(root.glob("**/*.csv"))
        json_files = list(root.glob("**/*.json"))

        samples: List[DatasetSample] = []

        if csv_files:
            main_csv = sorted(csv_files)[0]
            with open(main_csv, newline="") as f:
                reader = csv.DictReader(f)
                for i, row in enumerate(reader):
                    try:
                        # VF sensitivity values: columns like td_1..td_52 or v1..v52
                        vf_cols = [k for k in row.keys() if k.lower().startswith(("td", "vf", "sens", "v")) and k[2:].isdigit()]
                        if not vf_cols:
                            vf_cols = [k for k in row.keys() if k.isdigit() or (k[1:].isdigit() and k[0] in "vVtT")]
                        vf_array = np.array([float(row[c]) for c in sorted(vf_cols)]) if vf_cols else np.zeros(52)

                        label_str = row.get("glaucoma", row.get("label", row.get("diagnosis", "0")))
                        label = 1 if str(label_str).lower() in ("1", "true", "yes", "glaucoma") else 0
                        md = float(row.get("md", row.get("MD", 0.0)))

                        samples.append(DatasetSample(
                            image_path=str(main_csv),
                            label=label,
                            sample_id=row.get("id", row.get("eye_id", str(i))),
                            metadata={
                                "vf_array": vf_array,
                                "md": md,
                                "psd": float(row.get("psd", row.get("PSD", 0.0))),
                                "eye": row.get("eye", row.get("laterality", "")),
                            },
                        ))
                    except (ValueError, KeyError):
                        continue

        elif json_files:
            main_json = sorted(json_files)[0]
            with open(main_json) as f:
                data: Any = json.load(f)
            records = data if isinstance(data, list) else data.get("records", data.get("data", []))
            for i, rec in enumerate(records):
                vf_array = np.array(rec.get("vf", rec.get("sensitivities", [0.0] * 52)), dtype=float)
                label = int(rec.get("glaucoma", rec.get("label", 0)))
                samples.append(DatasetSample(
                    image_path=str(main_json),
                    label=label,
                    sample_id=rec.get("id", str(i)),
                    metadata={
                        "vf_array": vf_array,
                        "md": float(rec.get("md", 0.0)),
                        "psd": float(rec.get("psd", 0.0)),
                    },
                ))
        else:
            raise FileNotFoundError(
                f"UWHVF data not found in {root}. "
                "Run `eyehub download --datasets uwhvf` first."
            )

        return samples


# ---------------------------------------------------------------------------
# GRAPE — Glaucoma Real-world Appraisal Progression Ensemble
# ---------------------------------------------------------------------------


class GRAPEDataset(EyeDataHubDataset):
    """
    GRAPE: Glaucoma Real-world Appraisal Progression Ensemble.

    Longitudinal multi-modal dataset from 263 eyes with 1,115 follow-up visits.
    Modalities: visual fields (HFA 24-2), color fundus photographs, OCT RNFL,
    IOP, CCT, and clinical annotations.

    Tasks:
    - VF progression prediction (regression)
    - Optic disc segmentation (from fundus)
    - Glaucoma staging (classification)

    Reference:
        Wen et al., "GRAPE: A Multi-modal Dataset for Glaucoma Progression
        Evaluation", Figshare 2022.
    """

    _SUBDIR = "grape"
    _FIGSHARE_URL = "https://doi.org/10.6084/m9.figshare.c.6406319"
    _FIGSHARE_COLLECTION_ID = "6406319"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="grape",
            full_name="GRAPE: Glaucoma Real-world Appraisal Progression Ensemble",
            description=(
                "263 eyes × 1,115 visits. Multi-modal: VF (HFA 24-2), fundus "
                "photographs, OCT RNFL, IOP, CCT. Labels: VF progression, "
                "OD segmentation, glaucoma stage."
            ),
            modality="multimodal",
            tasks=["regression", "segmentation", "classification"],
            num_samples=1115,
            splits=["all"],
            classes=["Stable", "Progressing"],
            num_classes=2,
            download_type="figshare",
            download_url=self._FIGSHARE_URL,
            license="CC0 1.0",
            citation=(
                "Wen et al., 'GRAPE: A multi-modal dataset for glaucoma progression ',"
                "Figshare collection 2022."
            ),
            tags=["glaucoma", "visual_field", "fundus", "oct", "longitudinal", "multimodal"],
            size_gb=1.5,
            notes=(
                "Multi-modal: contains fundus images, VF data, OCT measurements, "
                "and clinical metadata. Requires manual download from Figshare."
            ),
            modalities=["multimodal", "fundus", "oct", "visual_field", "tabular"],
            dataset_doi="10.6084/m9.figshare.c.6406319.v1",
            terms_scope="dataset_files",
            terms_evidence_url=self._FIGSHARE_URL,
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return (
            len(list(root.glob("**/*.jpg"))) > 50
            or len(list(root.glob("**/*.png"))) > 50
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        root = Path(data_dir) / self._SUBDIR
        download_figshare_collection(self._FIGSHARE_COLLECTION_ID, root)

    def load(
        self, data_dir: Union[str, Path], split: str = "all"
    ) -> List[DatasetSample]:
        """Load GRAPE samples (fundus image paths with associated VF/clinical data)."""
        import csv

        root = Path(data_dir) / self._SUBDIR

        # Discover fundus images
        img_dirs = [root / "fundus_images", root / "images", root]
        img_dir = next((d for d in img_dirs if d.exists()), root)

        # Load clinical data if available
        label_map: Dict[str, int] = {}
        meta_map: Dict[str, Dict] = {}
        for f in list(root.glob("**/*.csv")) + list(root.glob("**/*.xlsx")):
            try:
                import pandas as pd
                df = pd.read_excel(f) if f.suffix == ".xlsx" else pd.read_csv(f)
                for _, row in df.iterrows():
                    key = str(row.iloc[0])
                    prog_col = next((c for c in df.columns if "progress" in c.lower()), None)
                    if prog_col:
                        label_map[key] = int(row[prog_col])
                    meta_map[key] = row.to_dict()
                break
            except Exception:
                pass

        samples = []
        for img_path in sorted(img_dir.glob("*.jpg")) + sorted(img_dir.glob("*.png")):
            stem = img_path.stem
            label = label_map.get(stem, 0)
            meta = meta_map.get(stem, {})
            samples.append(DatasetSample(
                image_path=str(img_path),
                label=label,
                sample_id=stem,
                metadata={"split": split, **{k: str(v) for k, v in meta.items()}},
            ))
        return samples
