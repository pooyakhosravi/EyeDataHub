"""
EyeDataHub-Open → Hugging Face Hub uploader.

Reads the processed output from preprocess.py and pushes to:
  hf_username/EyeDataHub-Open

The final dataset is split by modality into HF configs (subsets):
  - fundus_vessels
  - fundus_dr
  - fundus_glaucoma
  - oct_classification
  - oct_segmentation
  - uwf_fundus
  - visual_field
  - multimodal

Usage:
    # Dry run (prints plan, no upload)
    python hub/build_hf_dataset.py --processed-dir ./eyedatahub_open_processed --dry-run

    # Upload
    python hub/build_hf_dataset.py \
        --processed-dir ./eyedatahub_open_processed \
        --repo-id your-hf-username/EyeDataHub-Open \
        --token $HF_TOKEN
"""
from __future__ import annotations

import argparse
import os
from pathlib import Path

import pandas as pd

from eyedatahub.utils.credentials import load_credentials

try:
    from datasets import Dataset, DatasetDict, Image
    from huggingface_hub import HfApi, create_repo
    HF_AVAILABLE = True
except ImportError:
    HF_AVAILABLE = False


# ---------------------------------------------------------------------------
# Config → modality mapping
# ---------------------------------------------------------------------------

MODALITY_CONFIGS: dict[str, list[str]] = {
    "fundus_vessels": [
        "chase_db1", "hrf", "fives",
    ],
    "fundus_dr": [
        "idrid", "ddr", "maples_dr", "deepdrid", "mmrdr",
    ],
    "fundus_glaucoma": [
        "airogs", "acrima", "g1020", "rimone_dl", "papila",
        "origa", "harvard_glaucoma",
    ],
    "fundus_other": [
        "jsiec", "rfmid", "odir2019", "toxofundus", "farfum_rop",
    ],
    "octa_dr": [
        "drac22",
    ],
    "oct_classification": [
        "kermany_oct", "octid", "oct_cirrus", "octdl", "nehut", "olives",
    ],
    "oct_segmentation": [
        "oimhs", "octave", "goals", "tian_oct",
    ],
    "uwf_fundus": [
        "oculoscope", "uwf_tumor",
    ],
    "visual_field": [
        "uwhvf",
    ],
    "multimodal": [
        "grape",
    ],
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _find_parquet(processed_dir: Path, dataset_name: str) -> Path | None:
    hits = list(processed_dir.rglob(f"{dataset_name}/metadata.parquet"))
    return hits[0] if hits else None


def _load_split_dict(processed_dir: Path, dataset_names: list[str]) -> dict[str, pd.DataFrame]:
    """Load and concatenate parquets for a list of dataset names."""
    dfs_by_split: dict[str, list[pd.DataFrame]] = {}
    for name in dataset_names:
        p = _find_parquet(processed_dir, name)
        if p is None:
            continue
        df = pd.read_parquet(p)
        for split, grp in df.groupby("split"):
            dfs_by_split.setdefault(split, []).append(grp.copy())

    combined: dict[str, pd.DataFrame] = {}
    for split, dfs in dfs_by_split.items():
        combined[split] = pd.concat(dfs, ignore_index=True)
    return combined


def _df_to_hf_dataset(df: pd.DataFrame, image_base: Path | None = None) -> Dataset:
    """Convert a DataFrame to a HF Dataset, embedding images if path column exists."""
    records = df.to_dict(orient="records")

    if image_base and "image_file" in df.columns:
        for r in records:
            img_path = r.get("image_file")
            if img_path and (image_base / img_path).exists():
                r["image"] = str(image_base / img_path)

    ds = Dataset.from_list(records)

    # Cast image column to HF Image feature for proper streaming
    if "image" in ds.column_names:
        ds = ds.cast_column("image", Image())

    return ds


def _resolve_image_base(processed_dir: Path, dataset_name: str) -> Path | None:
    p = _find_parquet(processed_dir, dataset_name)
    if p:
        return p.parent
    return None


# ---------------------------------------------------------------------------
# Dataset card
# ---------------------------------------------------------------------------

DATASET_CARD_TEMPLATE = """\
---
license: cc-by-4.0
task_categories:
  - image-classification
  - image-segmentation
language:
  - en
tags:
  - ophthalmology
  - retinal-imaging
  - fundus
  - OCT
  - medical-imaging
  - eyedatahub
pretty_name: EyeDataHub-Open
size_categories:
  - 100K<n<1M
configs:
{config_list}
---

# EyeDataHub-Open

A harmonised collection of **{n_datasets} open-licence ophthalmology datasets**
curated from the [EyeDataHub](https://github.com/pooyakhosravi/EyeDataHub) registry.

All datasets are licensed under CC BY 4.0, CC BY-SA 4.0, MIT, or CC0 —
suitable for **commercial and academic use**.

## Subsets / configs

| Config | Modality | Task | Datasets |
|--------|----------|------|----------|
| `fundus_vessels` | Fundus | Vessel segmentation | CHASE_DB1, HRF, FIVES |
| `fundus_dr` | Fundus | DR grading (0–4 ICDR) | IDRiD, DDR, MAPLES-DR, DeepDRiD, DRAC22, MMRDR |
| `fundus_glaucoma` | Fundus | Glaucoma binary referral | AIROGS, ACRIMA, G1020, RIM-ONE DL, PAPILA, ORIGA, Harvard Glaucoma |
| `fundus_other` | Fundus | Multi-disease / misc | JSIEC, RFMiD, ODIR-2019, ToxoFundus, FARFUM-ROP |
| `oct_classification` | OCT | Disease classification | Kermany, OCTID, OCT-Cirrus, OCTDL, NEH-UT, OLIVES |
| `oct_segmentation` | OCT | Layer/fluid segmentation | OIMHS, OCTAVE, GOALS, Tian |
| `uwf_fundus` | UWF Fundus | Classification | OculoScope, UWF Tumor |
| `visual_field` | Visual Field | VF regression/classification | UWHVF |
| `multimodal` | Multimodal | Glaucoma regression | GRAPE |

## Label harmonisation

All labels follow the unified schema defined in
[`hub/label_schema.json`](https://github.com/pooyakhosravi/EyeDataHub/blob/main/hub/label_schema.json):

- **DR grading**: 0–4 ICDR/ETDRS scale; grade 5 (ungradable) → `null`
- **Glaucoma**: binary (0 = non-referable, 1 = referable)
- **Vessel masks**: binary PNG (0 = background, 1 = vessel)
- **OCT classification**: 5-class (NORMAL / CNV / DME / DRUSEN / OTHER)

## Citation

If you use EyeDataHub-Open, please cite the individual datasets and EyeDataHub:

```
@misc{{eyedatahub2026,
  title  = {{EyeDataHub: A License-Aware Catalog and Downloader for Public Ophthalmic Imaging Datasets}},
  author = {{EyeDataHub Contributors}},
  year   = {{2026}},
  url    = {{https://github.com/pooyakhosravi/EyeDataHub}}
}}
```

See [DATASETS.md](https://github.com/pooyakhosravi/EyeDataHub/blob/main/DATASETS.md)
for per-dataset citations.
"""


def build_card(n_datasets: int, configs: list[str]) -> str:
    config_list = "\n".join(
        f"  - config_name: {c}\n    data_files: {c}/**" for c in configs
    )
    return DATASET_CARD_TEMPLATE.format(
        n_datasets=n_datasets,
        config_list=config_list,
    )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    load_credentials(login_huggingface=False)

    parser = argparse.ArgumentParser()
    parser.add_argument("--processed-dir", default="./eyedatahub_open_processed")
    parser.add_argument("--repo-id", default="YOUR_HF_USERNAME/EyeDataHub-Open",
                        help="HuggingFace repo id (username/repo-name)")
    parser.add_argument("--token", default=os.environ.get("HF_TOKEN"),
                        help="HuggingFace write token (or set HF_TOKEN in .env)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print plan without uploading")
    parser.add_argument("--config", default=None,
                        help="Upload only this config subset (e.g. fundus_dr)")
    parser.add_argument("--private", action="store_true",
                        help="Create as private repository")
    args = parser.parse_args()

    if not HF_AVAILABLE:
        print("ERROR: Install huggingface_hub and datasets:\n"
              "  pip install huggingface_hub datasets")
        return

    processed_dir = Path(args.processed_dir)
    if not processed_dir.exists():
        print(f"ERROR: processed_dir '{processed_dir}' does not exist.\n"
              "Run preprocess.py first.")
        return

    configs_to_run = (
        {args.config: MODALITY_CONFIGS[args.config]}
        if args.config and args.config in MODALITY_CONFIGS
        else MODALITY_CONFIGS
    )

    total_datasets = sum(len(v) for v in configs_to_run.values())
    print("\nEyeDataHub-Open HuggingFace builder")
    print(f"  Repo: {args.repo_id}")
    print(f"  Configs: {list(configs_to_run.keys())}")
    print(f"  Datasets: {total_datasets}")
    print(f"  Dry run: {args.dry_run}\n")

    if args.dry_run:
        for config, ds_names in configs_to_run.items():
            for name in ds_names:
                p = _find_parquet(processed_dir, name)
                status = "✓ ready" if p else "✗ missing (run preprocess.py)"
                print(f"  [{config}] {name}: {status}")
        return

    if not args.token:
        print("ERROR: provide --token or set HF_TOKEN in .env")
        return

    # Create repo
    api = HfApi(token=args.token)
    try:
        create_repo(
            repo_id=args.repo_id,
            repo_type="dataset",
            private=args.private,
            exist_ok=True,
            token=args.token,
        )
        print(f"Repo ready: https://huggingface.co/datasets/{args.repo_id}")
    except Exception as e:
        print(f"WARNING: could not create repo: {e}")

    # Upload dataset card
    card_text = build_card(
        n_datasets=total_datasets,
        configs=list(MODALITY_CONFIGS.keys()),
    )
    api.upload_file(
        path_or_fileobj=card_text.encode(),
        path_in_repo="README.md",
        repo_id=args.repo_id,
        repo_type="dataset",
        token=args.token,
    )
    print("Uploaded README.md (dataset card)")

    # Upload label schema
    schema_path = Path(__file__).parent / "label_schema.json"
    if schema_path.exists():
        api.upload_file(
            path_or_fileobj=schema_path,
            path_in_repo="label_schema.json",
            repo_id=args.repo_id,
            repo_type="dataset",
            token=args.token,
        )
        print("Uploaded label_schema.json")

    # Upload each config
    for config_name, ds_names in configs_to_run.items():
        print(f"\n── Config: {config_name} ──")

        available_names = [n for n in ds_names if _find_parquet(processed_dir, n)]
        if not available_names:
            print("  No processed data found — skipping")
            continue

        split_dfs = _load_split_dict(processed_dir, available_names)
        if not split_dfs:
            print("  Empty after loading parquets — skipping")
            continue

        hf_splits: dict[str, Dataset] = {}
        for split, df in split_dfs.items():
            print(f"  Building split '{split}' ({len(df):,} rows)…")
            # Try to find image base dir from first available dataset
            image_base = _resolve_image_base(processed_dir, available_names[0])
            hf_splits[split] = _df_to_hf_dataset(df, image_base=image_base)

        dd = DatasetDict(hf_splits)

        # Push to hub
        dd.push_to_hub(
            repo_id=args.repo_id,
            config_name=config_name,
            token=args.token,
            commit_message=f"Add {config_name} ({len(available_names)} datasets)",
        )
        print(f"  Pushed {config_name}: {list(hf_splits.keys())}")

    print(f"\nDone! View at: https://huggingface.co/datasets/{args.repo_id}")


if __name__ == "__main__":
    main()
