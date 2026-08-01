"""
Ophthalmic surgical video datasets.

Included:
  - Cataract-1K  : 1000 cataract surgery videos, 10 phases + instrument seg (Synapse)
  - OphNet2024   : Large-scale multi-procedure ophthalmic surgical video dataset (HuggingFace)
  - OphoraDataset: 160,185 video clip-instruction pairs from 9,819 ophthalmic surgical videos
                   (HuggingFace General-Medical-AI/Ophora-160K, MICCAI 2025)
"""
from __future__ import annotations

from pathlib import Path
from typing import List, Union

import pandas as pd

from eyedatahub.core.dataset import DatasetInfo, DatasetSample, EyeDataHubDataset
from eyedatahub.datasets.download_utils import (
    download_github_repo,
    download_huggingface,
    print_manual_download_instructions,
)


# ---------------------------------------------------------------------------
# Cataract-1K (Synapse + GitHub)
# ---------------------------------------------------------------------------

CATARACT1K_PHASES = [
    "Incision",
    "Viscoelastic",
    "Capsulorhexis",
    "Hydrodissection",
    "Phacoemulsification",
    "Irrigation-Aspiration",
    "Capsule Polishing",
    "Lens Implant",
    "Viscoelastic Suction",
    "Tonifying-Antibiotics",
]


class Cataract1KDataset(EyeDataHubDataset):
    """
    Cataract-1K: Large-Scale Cataract Surgery Video Dataset.

    1000 cataract surgery videos annotated for:
    - Surgical phase recognition (10 phases)
    - Instrument segmentation
    - Tool presence detection

    GitHub: https://github.com/Negin-Ghamsarian/Cataract-1K
    Data hosted on Synapse (registration required):
      https://www.synapse.org/#!Synapse:syn53404917
    """

    _SUBDIR = "cataract1k"
    _GITHUB_REPO = "Negin-Ghamsarian/Cataract-1K"
    _SYNAPSE_ID = "syn53404917"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="cataract1k",
            full_name="Cataract-1K: Large-Scale Cataract Surgery Video Dataset",
            description=(
                "1000 cataract surgery videos from multiple surgeons annotated "
                "for 10 surgical phases, instrument segmentation, and tool "
                "presence detection. First large-scale cataract surgical video dataset."
            ),
            modality="surgical_video",
            tasks=["phase_recognition", "segmentation", "detection"],
            num_samples=1000,
            splits=["train", "val", "test"],
            classes=CATARACT1K_PHASES,
            num_classes=10,
            download_type="manual",
            download_url="https://www.synapse.org/#!Synapse:syn53404917",
            license="Research only — see Synapse terms",
            citation=(
                "Ghamsarian N et al., 'Cataract-1K: Cataract Surgery Dataset "
                "for Domain Generalization of Surgical Workflow Analysis', "
                "IEEE TMI 2024. "
                "https://github.com/Negin-Ghamsarian/Cataract-1K"
            ),
            tags=["surgical_video", "cataract", "phase_recognition", "synapse"],
            size_gb=50.0,
            notes=(
                "Data hosted on Synapse (free registration required). "
                "Install synapseclient: pip install synapseclient. "
                "Then: synapse get syn53404917"
            ),
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return (
            len(list(root.glob("**/*.mp4"))) > 10
            or len(list(root.glob("**/*.avi"))) > 10
            or len(list(root.glob("**/*.png"))) > 500  # frame-extracted
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        dest = Path(data_dir) / self._SUBDIR
        dest.mkdir(parents=True, exist_ok=True)
        # Try synapseclient programmatic download
        try:
            import synapseclient
            syn = synapseclient.Synapse()
            syn.login(silent=True)
            syn.get(self._SYNAPSE_ID, downloadLocation=str(dest), ifcollision="overwrite.local")
            return
        except ImportError:
            pass
        except Exception:
            pass

        # Fallback: GitHub for annotations/code; data manual
        try:
            download_github_repo(self._GITHUB_REPO, dest, branch="main")
        except Exception:
            pass

        print_manual_download_instructions(
            "Cataract-1K",
            f"https://www.synapse.org/#!Synapse:{self._SYNAPSE_ID}",
            dest,
            extra_notes=(
                "Option 1 — synapseclient CLI:\n"
                "  pip install synapseclient\n"
                "  synapse login\n"
                f"  synapse get {self._SYNAPSE_ID} --downloadLocation {dest}\n\n"
                "Option 2 — web browser:\n"
                f"  Visit https://www.synapse.org/#!Synapse:{self._SYNAPSE_ID}\n"
                "  Register for free and download the dataset.\n\n"
                "Annotation code/scripts:\n"
                "  https://github.com/Negin-Ghamsarian/Cataract-1K"
            ),
        )
        raise RuntimeError(
            "Cataract-1K requires Synapse registration. See instructions above."
        )

    def load(
        self, data_dir: Union[str, Path], split: str = "train"
    ) -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR

        # Look for CSV phase annotations
        label_map: dict = {}
        csv_files = list(root.glob(f"*{split}*.csv")) + list(root.glob("**/*.csv"))
        if csv_files:
            df = pd.read_csv(csv_files[0])
            id_col = next(
                (c for c in df.columns if any(
                    kw in c.lower() for kw in ("video", "file", "id", "name", "frame")
                )), df.columns[0]
            )
            lbl_col = next(
                (c for c in df.columns if any(
                    kw in c.lower() for kw in ("phase", "label", "class", "step")
                )), df.columns[1] if len(df.columns) > 1 else None
            )
            if lbl_col:
                for _, row in df.iterrows():
                    label_map[str(row[id_col]).strip()] = row[lbl_col]

        # Collect video files or extracted frames
        videos = sorted(
            list(root.rglob("*.mp4"))
            + list(root.rglob("*.avi"))
            + list(root.rglob("*.mov"))
        )
        # Filter by split
        split_vids = [v for v in videos if split.lower() in str(v).lower()]
        if split_vids:
            videos = split_vids

        if videos:
            return [
                DatasetSample(
                    image_path=str(v),
                    label=label_map.get(v.stem),
                    sample_id=v.stem,
                    metadata={"split": split, "type": "video"},
                )
                for v in videos
            ]

        # If frames extracted
        frames = sorted(
            list(root.rglob("*.jpg"))
            + list(root.rglob("*.png"))
        )
        split_frames = [f for f in frames if split.lower() in str(f).lower()]
        if split_frames:
            frames = split_frames

        if not frames:
            raise FileNotFoundError(
                f"No videos or frames found in {root}. "
                "Run: eyehub download --datasets cataract1k"
            )
        return [
            DatasetSample(
                image_path=str(f),
                label=label_map.get(f.stem),
                sample_id=f.stem,
                metadata={"split": split, "type": "frame"},
            )
            for f in frames
        ]


# ---------------------------------------------------------------------------
# OphNet2024: Ophthalmic Surgical Video Dataset (HuggingFace)
# ---------------------------------------------------------------------------

OPHNET_PROCEDURE_CLASSES = [
    "Cataract Surgery",
    "Vitreoretinal Surgery",
    "Glaucoma Surgery",
    "Corneal Surgery",
    "Refractive Surgery",
    "Oculoplastic Surgery",
    "Strabismus Surgery",
    "Other",
]


class OphNet2024Dataset(EyeDataHubDataset):
    """
    OphNet2024: Large-Scale Ophthalmic Surgical Video Dataset.

    Multi-procedure ophthalmic surgical videos annotated for:
    - Procedure classification (8+ surgery types)
    - Surgical phase recognition
    - Instrument detection

    HuggingFace: https://huggingface.co/datasets/xioamiyh/OphNet2024
    """

    _SUBDIR = "ophnet2024"
    _HF_ID = "xioamiyh/OphNet2024"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="ophnet2024",
            full_name="OphNet2024: Ophthalmic Surgical Video Dataset",
            description=(
                "Large-scale multi-procedure ophthalmic surgical video dataset "
                "covering 66 surgery types, 102 phases, 150 operations (~285 h). "
                "1,969 untrimmed videos; 17,508 trimmed operation-level clips; "
                "14,674 trimmed phase-level clips across cataract, vitreoretinal, "
                "glaucoma, corneal, refractive, oculoplastic, and strabismus. "
                "743 videos have time-boundary annotations. ECCV 2024."
            ),
            modality="surgical_video",
            tasks=["classification", "phase_recognition", "detection"],
            num_samples=2278,
            splits=["train", "val", "test"],
            classes=OPHNET_PROCEDURE_CLASSES,
            num_classes=8,
            download_type="huggingface",
            download_url="https://huggingface.co/datasets/xioamiyh/OphNet2024",
            license="CC BY-NC-SA 4.0",
            citation=(
                "Hu M et al., 'OphNet: A Large-Scale Video Benchmark for Ophthalmic "
                "Surgical Workflow Understanding', ECCV 2024. arXiv:2406.07471. "
                "HuggingFace: https://huggingface.co/datasets/xioamiyh/OphNet2024 — "
                "GitHub: https://github.com/minghu0830/OphNet-benchmark"
            ),
            tags=["surgical_video", "multi_procedure", "huggingface", "phase_recognition", "eccv"],
            size_gb=583.0,
            notes=(
                "~583 GB total: untrimmed ~305 GB, trimmed operations ~139 GB, "
                "trimmed phases ~139 GB, features ~26 GB. "
                "num_samples = 2,278 source videos. "
                "May require HF_TOKEN for gated access. Set HF_TOKEN in .env. "
                "GitHub: https://github.com/minghu0830/OphNet-benchmark"
            ),
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return (
            len(list(root.glob("**/*.mp4"))) > 10
            or len(list(root.glob("**/*.avi"))) > 10
            or len(list(root.glob("**/*.json"))) > 10  # annotation files
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        dest = Path(data_dir) / self._SUBDIR
        try:
            download_huggingface(self._HF_ID, dest, repo_type="dataset")
        except Exception:
            print_manual_download_instructions(
                "OphNet2024",
                "https://huggingface.co/datasets/xioamiyh/OphNet2024",
                dest,
                extra_notes=(
                    "pip install huggingface_hub\n"
                    "huggingface-cli download xioamiyh/OphNet2024 --repo-type dataset\n\n"
                    "If access is restricted, set HF_TOKEN in .env:\n"
                    "  HF_TOKEN=hf_your_token_here"
                ),
            )
            raise

    def load(
        self, data_dir: Union[str, Path], split: str = "train"
    ) -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR

        label_map: dict = {}
        # Look for JSON or CSV annotations
        import json as _json
        for ann_path in list(root.glob(f"*{split}*.json")) + list(root.glob("**/*.json")):
            try:
                with open(ann_path) as f:
                    ann = _json.load(f)
                # OphNet typically uses COCO-style or simple dict annotations
                if isinstance(ann, list):
                    for item in ann:
                        vid_id = str(item.get("video_id", item.get("id", "")))
                        lbl = item.get("category_id", item.get("label"))
                        label_map[vid_id] = lbl
                elif isinstance(ann, dict):
                    for k, v in ann.items():
                        label_map[str(k)] = v.get("label") if isinstance(v, dict) else v
                if label_map:
                    break
            except Exception:
                pass

        videos = sorted(
            list(root.rglob("*.mp4"))
            + list(root.rglob("*.avi"))
            + list(root.rglob("*.mov"))
        )
        split_vids = [v for v in videos if split.lower() in str(v).lower()]
        if split_vids:
            videos = split_vids

        if not videos:
            raise FileNotFoundError(
                f"No videos found in {root}. "
                "Run: eyehub download --datasets ophnet2024"
            )
        return [
            DatasetSample(
                image_path=str(v),
                label=label_map.get(v.stem),
                sample_id=v.stem,
                metadata={"split": split},
            )
            for v in videos
        ]


# ---------------------------------------------------------------------------
# Ophora-160K: Ophthalmic Surgical Video Instruction Dataset (HuggingFace)
# ---------------------------------------------------------------------------

class OphoraDataset(EyeDataHubDataset):
    """
    Ophora-160K: Ophthalmic Surgical Video Instruction Dataset.

    162,185 video clip-instruction pair samples derived from 9,819
    ophthalmic surgical videos across multiple procedure types. Released
    alongside the Ophora text-guided surgical video generation model.

    HuggingFace: https://huggingface.co/datasets/General-Medical-AI/Ophora-160K
    GitHub:      https://github.com/uni-medical/Ophora
    Paper:       MICCAI 2025
    """

    _SUBDIR = "ophora"
    _HF_ID = "General-Medical-AI/Ophora-160K"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="ophora",
            full_name="Ophora-160K: Ophthalmic Surgical Video Instruction Dataset",
            description=(
                "162,185 video clip-instruction pair samples from 9,819 ophthalmic "
                "surgical videos, covering multiple procedure types. Designed for "
                "text-guided surgical video generation and understanding. "
                "Published at MICCAI 2025."
            ),
            modality="surgical_video",
            tasks=["classification", "phase_recognition"],
            num_samples=162185,
            item_count_unit="video_clip_instruction_pairs",
            splits=["train"],
            classes=None,
            num_classes=None,
            download_type="huggingface",
            download_url="https://huggingface.co/datasets/General-Medical-AI/Ophora-160K",
            license="Unknown — no license stated",
            citation=(
                "Ophora: Text-Guided Ophthalmic Surgical Video Generation. "
                "MICCAI 2025. arXiv:2505.07449. "
                "HuggingFace: https://huggingface.co/datasets/General-Medical-AI/Ophora-160K — "
                "GitHub: https://github.com/uni-medical/Ophora"
            ),
            tags=["surgical_video", "ophthalmic", "huggingface", "instruction", "miccai"],
            size_gb=500.0,
            notes=(
                "162,185 video clip-instruction pairs from 9,819 source videos "
                "(avg clip length ~5.5 s). Estimated ~500 GB total. "
                "Video clip-instruction pair dataset for text-guided surgical video "
                "generation. May require HF_TOKEN for gated access. Set in .env."
            ),
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return (
            len(list(root.glob("**/*.mp4"))) > 10
            or len(list(root.glob("**/*.json"))) > 10
            or (root / "data").exists()
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        dest = Path(data_dir) / self._SUBDIR
        try:
            download_huggingface(self._HF_ID, dest, repo_type="dataset")
        except Exception:
            print_manual_download_instructions(
                "Ophora-160K",
                "https://huggingface.co/datasets/General-Medical-AI/Ophora-160K",
                dest,
                extra_notes=(
                    "pip install huggingface_hub\n"
                    "huggingface-cli download General-Medical-AI/Ophora-160K "
                    "--repo-type dataset\n\n"
                    "If access is restricted, set HF_TOKEN in .env:\n"
                    "  HF_TOKEN=hf_your_token_here\n\n"
                    "GitHub: https://github.com/uni-medical/Ophora"
                ),
            )
            raise

    def load(
        self, data_dir: Union[str, Path], split: str = "train"
    ) -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR

        # Look for annotation JSON/CSV
        label_map: dict = {}
        import json as _json
        ann_files = (
            list(root.glob(f"*{split}*.json"))
            + list(root.glob("**/*.jsonl"))
            + list(root.glob("**/*.json"))
        )
        for ann_path in ann_files[:3]:
            try:
                with open(ann_path) as f:
                    # Handle JSONL
                    content = f.read().strip()
                    if content.startswith("["):
                        ann = _json.loads(content)
                    else:
                        ann = [_json.loads(line) for line in content.splitlines() if line.strip()]
                for item in ann:
                    vid_id = str(item.get("video_id", item.get("id", item.get("clip_id", ""))))
                    label_map[vid_id] = item.get("label", item.get("category"))
                if label_map:
                    break
            except Exception:
                pass

        videos = sorted(
            list(root.rglob("*.mp4"))
            + list(root.rglob("*.avi"))
            + list(root.rglob("*.mov"))
        )
        split_vids = [v for v in videos if split.lower() in str(v).lower()]
        if split_vids:
            videos = split_vids

        if not videos:
            raise FileNotFoundError(
                f"No videos found in {root}. "
                "Run: eyehub download --datasets ophora"
            )
        return [
            DatasetSample(
                image_path=str(v),
                label=label_map.get(v.stem),
                sample_id=v.stem,
                metadata={"split": split},
            )
            for v in videos
        ]
