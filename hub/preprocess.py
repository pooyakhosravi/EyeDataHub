"""
EyeDataHub-Open — data harmonisation pipeline.

For each open-licence dataset that is already downloaded, this script:
  1. Reads raw images + labels using the EyeDataHub dataset API
  2. Applies the label harmonisation schema from label_schema.json
  3. Writes a per-dataset Parquet sidecar (metadata + labels)
  4. Copies / converts images to a canonical PNG layout

Output layout  (under --out-dir, default ./eyedatahub_open_processed/):
  <out_dir>/
    fundus/
      vessel_segmentation/
        chase_db1/
          images/   *.png
          masks/    *.png        # 0=bg, 1=vessel
          metadata.parquet
        ...
      dr_grading/
        idrid/
          images/   *.png
          metadata.parquet       # columns: sample_id, dr_grade, split
      glaucoma/
        airogs/
          ...
    oct/
      classification/
        kermany_oct/
          ...
      layer_segmentation/
        ...
    ...

Usage:
    python hub/preprocess.py --data-dir ~/.eyedatahub/data --out-dir ./eyedatahub_open_processed
    python hub/preprocess.py --dataset idrid --data-dir ~/.eyedatahub/data
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import numpy as np
import pandas as pd
from PIL import Image
from tqdm import tqdm

from eyedatahub.core.dataset import license_matches_filter
from eyedatahub.datasets.registry import REGISTRY

# ---------------------------------------------------------------------------
# Label harmonisation maps (mirrors label_schema.json)
# ---------------------------------------------------------------------------

DR_MAPS: dict[str, dict[Any, int | None]] = {
    "aptos2019":  {0: 0, 1: 1, 2: 2, 3: 3, 4: 4},
    "idrid":      {0: 0, 1: 1, 2: 2, 3: 3, 4: 4},
    "ddr":        {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: None},
    "maples_dr":  {0: 0, 1: 1, 2: 2, 3: 3, 4: 4},
    "deepdrid":   {0: 0, 1: 1, 2: 2, 3: 3, 4: 4},
    "drac22":     {0: 0, 1: 2, 2: 4},
    "mmrdr":      {0: 0, 1: 1, 2: 2, 3: 3, 4: 4},
}

GLAUCOMA_MAPS: dict[str, dict[Any, int]] = {
    "airogs":         {"NRG": 0, "RG": 1, 0: 0, 1: 1},
    "g1020":          {0: 0, 1: 1},
    "acrima":         {"Glaucoma": 1, "No_Glaucoma": 0, 0: 0, 1: 1},
    "rimone_dl":      {"Glaucoma": 1, "Normal": 0, 0: 0, 1: 1},
    "papila":         {"Normal": 0, "Glaucoma": 1, "Suspect": 1, 0: 0, 1: 1},
    "origa":          {0: 0, 1: 1},
    "harvard_glaucoma": {0: 0, 1: 1},
}

OCT_MAPS: dict[str, dict[Any, int]] = {
    "kermany_oct": {"NORMAL": 0, "CNV": 1, "DME": 2, "DRUSEN": 3},
    "octid":       {"NORMAL": 0, "CNV": 1, "DME": 2, "AMD": 3,
                    "DR": 2, "CSR": 4, "MH": 4, "TSR_SRF": 4},
    "oct_cirrus":  {"NORMAL": 0, "DME": 2, "AMD": 3},
    "octdl":       {"NORMAL": 0, "CNV": 1, "DME": 2, "DRUSEN": 3,
                    "MH": 4, "CSR": 4, "AO": 4},
    "nehut":       {"Normal": 0, "CNV": 1, "DME": 2, "DRUSEN": 3},
}

VESSEL_DATASETS = {"chase_db1", "hrf", "fives"}
GLAUCOMA_DATASETS = set(GLAUCOMA_MAPS.keys())
DR_DATASETS = set(DR_MAPS.keys()) - {"drac22"}  # drac22 is OCTA, separate path
OCTA_DATASETS = {"drac22"}
OCT_CLASS_DATASETS = set(OCT_MAPS.keys()) | {"olives"}  # olives is OCT multilabel


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _is_open(ds) -> bool:
    li = ds.info.license
    return (
        license_matches_filter(li, "commercial-ok")
        or ds.info.license_family == "cc-by-sa"
    )


def _task_subdir(name: str) -> str:
    if name in VESSEL_DATASETS:
        return "fundus/vessel_segmentation"
    if name in GLAUCOMA_DATASETS:
        return "fundus/glaucoma"
    if name in DR_DATASETS:
        return "fundus/dr_grading"
    if name in OCTA_DATASETS:
        return "octa/dr_grading"
    if name in OCT_CLASS_DATASETS:
        return "oct/classification"
    if name in {"oimhs", "octave", "goals", "tian_oct"}:
        return "oct/layer_segmentation"
    if name == "uwhvf":
        return "visual_field"
    if name in {"oculoscope", "uwf_tumor"}:
        return "uwf_fundus"
    if name == "grape":
        return "multimodal"
    return "fundus/other"


def _save_image(img: Image.Image, dst: Path, max_long_edge: int = 1024) -> None:
    """Save PIL image as PNG, downscaling if wider/taller than max_long_edge."""
    w, h = img.size
    if max(w, h) > max_long_edge:
        scale = max_long_edge / max(w, h)
        img = img.resize((int(w * scale), int(h * scale)), Image.LANCZOS)
    img.save(dst, format="PNG", optimize=False)


def _normalize_mask(mask_arr: np.ndarray) -> np.ndarray:
    """Ensure mask is binary uint8 (0/1)."""
    if mask_arr.max() > 1:
        mask_arr = (mask_arr > 127).astype(np.uint8)
    return mask_arr.astype(np.uint8)


# ---------------------------------------------------------------------------
# Per-task processors
# ---------------------------------------------------------------------------

def process_vessel_segmentation(ds, samples, out_base: Path) -> pd.DataFrame:
    img_dir = out_base / "images"
    msk_dir = out_base / "masks"
    img_dir.mkdir(parents=True, exist_ok=True)
    msk_dir.mkdir(parents=True, exist_ok=True)

    rows = []
    for s in tqdm(samples, desc=f"  {ds.info.name} images"):
        sid = s.sample_id or Path(s.image_path).stem
        img = Image.open(s.image_path).convert("RGB")
        _save_image(img, img_dir / f"{sid}.png")

        mask_path = s.label  # DatasetSample.label holds mask path for seg datasets
        if isinstance(mask_path, str) and Path(mask_path).exists():
            mask_arr = ds.load_mask(mask_path)
            mask_arr = _normalize_mask(mask_arr)
            Image.fromarray(mask_arr * 255, mode="L").save(msk_dir / f"{sid}.png")
            has_mask = True
        elif isinstance(mask_path, np.ndarray):
            mask_arr = _normalize_mask(mask_path)
            Image.fromarray(mask_arr * 255, mode="L").save(msk_dir / f"{sid}.png")
            has_mask = True
        else:
            has_mask = False

        rows.append({
            "sample_id": sid,
            "image_file": f"images/{sid}.png",
            "mask_file": f"masks/{sid}.png" if has_mask else None,
            "split": s.metadata.get("split", "all"),
            "dataset": ds.info.name,
        })

    return pd.DataFrame(rows)


def process_dr_grading(ds, samples, out_base: Path) -> pd.DataFrame:
    img_dir = out_base / "images"
    img_dir.mkdir(parents=True, exist_ok=True)
    label_map = DR_MAPS.get(ds.info.name, {})

    rows = []
    for s in tqdm(samples, desc=f"  {ds.info.name} images"):
        sid = s.sample_id or Path(s.image_path).stem
        img = Image.open(s.image_path).convert("RGB")
        _save_image(img, img_dir / f"{sid}.png")

        raw_label = s.label
        unified_grade = label_map.get(raw_label, raw_label if isinstance(raw_label, int) else None)

        rows.append({
            "sample_id": sid,
            "image_file": f"images/{sid}.png",
            "dr_grade_raw": raw_label,
            "dr_grade": unified_grade,  # 0-4, None = ungradable
            "split": s.metadata.get("split", "all"),
            "dataset": ds.info.name,
        })

    return pd.DataFrame(rows)


def process_glaucoma(ds, samples, out_base: Path) -> pd.DataFrame:
    img_dir = out_base / "images"
    img_dir.mkdir(parents=True, exist_ok=True)
    label_map = GLAUCOMA_MAPS.get(ds.info.name, {})

    rows = []
    for s in tqdm(samples, desc=f"  {ds.info.name} images"):
        sid = s.sample_id or Path(s.image_path).stem
        img = Image.open(s.image_path).convert("RGB")
        _save_image(img, img_dir / f"{sid}.png")

        raw = s.label
        unified = label_map.get(raw, int(raw) if isinstance(raw, (int, float)) else None)
        cdr = s.metadata.get("cdr", None)

        rows.append({
            "sample_id": sid,
            "image_file": f"images/{sid}.png",
            "glaucoma_label_raw": raw,
            "glaucoma": unified,   # 0 = non-referable, 1 = referable
            "cdr": cdr,
            "split": s.metadata.get("split", "all"),
            "dataset": ds.info.name,
        })

    return pd.DataFrame(rows)


def process_oct_classification(ds, samples, out_base: Path) -> pd.DataFrame:
    img_dir = out_base / "images"
    img_dir.mkdir(parents=True, exist_ok=True)
    label_map = OCT_MAPS.get(ds.info.name, {})

    CLASS_NAMES = ["NORMAL", "CNV", "DME", "DRUSEN", "OTHER"]

    rows = []
    for s in tqdm(samples, desc=f"  {ds.info.name} images"):
        sid = s.sample_id or Path(s.image_path).stem
        img = Image.open(s.image_path).convert("RGB")
        _save_image(img, img_dir / f"{sid}.png")

        raw = s.label
        unified = label_map.get(raw, int(raw) if isinstance(raw, int) else None)
        class_name = CLASS_NAMES[unified] if isinstance(unified, int) and unified < len(CLASS_NAMES) else str(raw)

        rows.append({
            "sample_id": sid,
            "image_file": f"images/{sid}.png",
            "label_raw": raw,
            "label": unified,
            "class_name": class_name,
            "split": s.metadata.get("split", "all"),
            "dataset": ds.info.name,
        })

    return pd.DataFrame(rows)


def process_generic(ds, samples, out_base: Path) -> pd.DataFrame:
    """Passthrough: save images, keep raw labels as-is."""
    img_dir = out_base / "images"
    img_dir.mkdir(parents=True, exist_ok=True)

    rows = []
    for s in tqdm(samples, desc=f"  {ds.info.name} images"):
        sid = s.sample_id or Path(s.image_path).stem
        try:
            img = Image.open(s.image_path).convert("RGB")
            _save_image(img, img_dir / f"{sid}.png")
            img_ok = True
        except Exception as e:
            print(f"    Warning: could not open {s.image_path}: {e}")
            img_ok = False

        rows.append({
            "sample_id": sid,
            "image_file": f"images/{sid}.png" if img_ok else None,
            "label": str(s.label) if not isinstance(s.label, (int, float, type(None))) else s.label,
            "split": s.metadata.get("split", "all"),
            "dataset": ds.info.name,
            **{k: v for k, v in s.metadata.items() if k not in ("split",)},
        })

    return pd.DataFrame(rows)


# ---------------------------------------------------------------------------
# Router
# ---------------------------------------------------------------------------

def process_dataset(ds, data_dir: Path, out_dir: Path, split: str = "test") -> None:
    name = ds.info.name
    subdir = _task_subdir(name)
    out_base = out_dir / subdir / name
    out_base.mkdir(parents=True, exist_ok=True)

    print(f"\n[{name}] Loading split='{split}' …")
    try:
        samples = ds.load(data_dir, split=split)
    except Exception as e:
        print(f"  ERROR loading {name}: {e}")
        return

    if not samples:
        print(f"  No samples returned for split='{split}'")
        return

    print(f"  {len(samples)} samples")

    if name in VESSEL_DATASETS:
        df = process_vessel_segmentation(ds, samples, out_base)
    elif name in DR_DATASETS:
        df = process_dr_grading(ds, samples, out_base)
    elif name in GLAUCOMA_DATASETS:
        df = process_glaucoma(ds, samples, out_base)
    elif name in OCT_CLASS_DATASETS:
        df = process_oct_classification(ds, samples, out_base)
    else:
        df = process_generic(ds, samples, out_base)

    parquet_path = out_base / "metadata.parquet"
    df.to_parquet(parquet_path, index=False)
    csv_path = out_base / "metadata.csv"
    df.to_csv(csv_path, index=False)
    print(f"  Wrote {len(df)} rows -> {parquet_path.relative_to(out_dir)}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="EyeDataHub-Open harmonisation pipeline")
    parser.add_argument("--data-dir", default="~/.eyedatahub/data",
                        help="Root directory where datasets are downloaded")
    parser.add_argument("--out-dir", default="./eyedatahub_open_processed",
                        help="Output directory for processed data")
    parser.add_argument("--dataset", default=None,
                        help="Process only this dataset name (default: all open-licence)")
    parser.add_argument("--split", default="test",
                        help="Dataset split to process (default: test)")
    parser.add_argument("--all-splits", action="store_true",
                        help="Process all available splits")
    args = parser.parse_args()

    data_root = Path(args.data_dir).expanduser()
    out_root = Path(args.out_dir)
    out_root.mkdir(parents=True, exist_ok=True)

    datasets = REGISTRY.list_datasets()
    open_ds = [d for d in datasets if _is_open(d)]

    if args.dataset:
        open_ds = [d for d in open_ds if d.info.name == args.dataset]
        if not open_ds:
            print(f"Dataset '{args.dataset}' not found or not open-licence.")
            return

    # Filter to downloaded only
    available = [d for d in open_ds if d.is_downloaded(data_root)]
    skipped = [d.info.name for d in open_ds if not d.is_downloaded(data_root)]

    if skipped:
        print(f"\nSkipping {len(skipped)} not-yet-downloaded datasets: {', '.join(skipped)}")

    print(f"\nProcessing {len(available)} datasets -> {out_root}\n")

    for ds in available:
        splits_to_run = ds.info.splits if args.all_splits else [args.split]
        for split in splits_to_run:
            if split in ds.info.splits:
                process_dataset(ds, data_root, out_root, split=split)

    # Write combined index
    all_parquets = list(out_root.rglob("metadata.parquet"))
    if all_parquets:
        dfs = []
        for p in all_parquets:
            df = pd.read_parquet(p)
            df["parquet_source"] = str(p.relative_to(out_root))
            dfs.append(df)
        combined = pd.concat(dfs, ignore_index=True)
        combined.to_parquet(out_root / "index.parquet", index=False)
        combined.to_csv(out_root / "index.csv", index=False)
        print(f"\nCombined index: {len(combined):,} rows -> {out_root}/index.parquet")


if __name__ == "__main__":
    main()
