"""Figure: heatmap of modality x task (cell = dataset count, annotated with image count).

Usage:
    python hub/stats/modality_task_matrix.py [--out reports/figures/auto/]
"""
from __future__ import annotations

import argparse
import csv
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from hub.stats._common import load_registry_metadata, save_both, setup_style


MODALITIES = ["fundus", "oct", "octa", "uwf_fundus", "visual_field", "confocal", "surgical_video", "multimodal"]
TASKS = ["classification", "grading", "segmentation", "multilabel", "regression", "progression", "quality"]


def compute(metadata: list[dict]) -> tuple[np.ndarray, np.ndarray]:
    """Returns (dataset_count_matrix, sample_count_matrix), both shape (len(MODALITIES), len(TASKS))."""
    counts = np.zeros((len(MODALITIES), len(TASKS)), dtype=int)
    samples = np.zeros((len(MODALITIES), len(TASKS)), dtype=float)

    for d in metadata:
        mod = d.get("modality", "")
        if mod not in MODALITIES:
            continue
        i = MODALITIES.index(mod)
        n = d.get("num_samples") or 0
        tasks = d.get("tasks", [])
        if isinstance(tasks, str):
            tasks = [tasks]
        for t in tasks:
            if t in TASKS:
                j = TASKS.index(t)
                counts[i, j] += 1
                samples[i, j] += n

    return counts, samples


def plot(counts: np.ndarray, samples: np.ndarray, out_dir: Path) -> None:
    setup_style()
    fig, ax = plt.subplots(figsize=(8, 4.5))

    masked = np.ma.masked_where(counts == 0, counts)
    im = ax.imshow(masked, cmap="Blues", aspect="auto")

    ax.set_xticks(range(len(TASKS)))
    ax.set_xticklabels(TASKS, rotation=30, ha="right")
    ax.set_yticks(range(len(MODALITIES)))
    ax.set_yticklabels(MODALITIES)
    ax.set_xlabel("Task")
    ax.set_ylabel("Imaging modality")
    ax.set_title("EyeDataHub coverage: datasets per (modality, task)")

    for i in range(len(MODALITIES)):
        for j in range(len(TASKS)):
            c = counts[i, j]
            if c:
                n = int(samples[i, j])
                label = f"{c}\n({n / 1000:.0f}K)" if n >= 1000 else f"{c}\n({n})"
                ax.text(j, i, label, ha="center", va="center", fontsize=8,
                        color="white" if c > counts.max() * 0.5 else "black")

    fig.colorbar(im, ax=ax, label="# datasets")
    save_both(fig, out_dir, "modality_task_matrix")


def write_csv(counts: np.ndarray, samples: np.ndarray, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    with (out_dir / "modality_task_matrix.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["modality"] + TASKS)
        for i, mod in enumerate(MODALITIES):
            w.writerow([mod] + [int(counts[i, j]) for j in range(len(TASKS))])
        w.writerow([])
        w.writerow(["modality (sample counts)"] + TASKS)
        for i, mod in enumerate(MODALITIES):
            w.writerow([mod] + [int(samples[i, j]) for j in range(len(TASKS))])


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--metadata", default=None, help="Ignored; modality/task statistics use the live registry.")
    ap.add_argument("--out", default="reports/figures/auto/")
    args = ap.parse_args()

    metadata = load_registry_metadata()
    counts, samples = compute(metadata)
    out_dir = Path(args.out)
    plot(counts, samples, out_dir)
    write_csv(counts, samples, out_dir)
    print(f"Wrote -> {out_dir}/modality_task_matrix.(png,svg,csv)")


if __name__ == "__main__":
    main()
