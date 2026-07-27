"""Figure: log-scale histogram + cumulative coverage of EyeDataHub dataset sizes.

Usage:
    python hub/stats/sample_size_distribution.py [--out reports/figures/auto/]
"""
from __future__ import annotations

import argparse
import csv
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from hub.stats._common import load_registry_metadata, save_both, setup_style


def compute(metadata: list[dict]) -> tuple[np.ndarray, list[tuple[str, int]]]:
    sizes = []
    named = []
    for d in metadata:
        n = d.get("num_samples")
        if isinstance(n, (int, float)) and n > 0:
            sizes.append(int(n))
            named.append((d.get("name", "?"), int(n)))
    sizes = np.array(sorted(sizes))
    named.sort(key=lambda kv: -kv[1])
    return sizes, named


def plot(sizes: np.ndarray, out_dir: Path) -> None:
    setup_style()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.2))

    # Histogram (log-scale x)
    bins = np.logspace(np.log10(max(1, sizes.min())), np.log10(sizes.max() + 1), 25)
    ax1.hist(sizes, bins=bins, color="#1f77b4", edgecolor="white")
    ax1.set_xscale("log")
    ax1.set_xlabel("Samples per dataset (log scale)")
    ax1.set_ylabel("# datasets")
    ax1.set_title(f"Dataset size distribution (n = {len(sizes)})")
    median = int(np.median(sizes))
    ax1.axvline(median, color="red", linestyle="--", linewidth=1)
    ax1.text(median, ax1.get_ylim()[1] * 0.9, f" median = {median:,}",
             color="red", fontsize=9)

    # Cumulative coverage
    descending = np.sort(sizes)[::-1]
    cum = np.cumsum(descending) / descending.sum() * 100
    ax2.plot(range(1, len(cum) + 1), cum, color="#2ca02c", linewidth=2)
    ax2.set_xlabel("Top-N datasets (sorted by size)")
    ax2.set_ylabel("Cumulative coverage of all samples (%)")
    ax2.set_title("How concentrated is data in big datasets?")
    for pct in (50, 80, 90):
        n_needed = int(np.argmax(cum >= pct)) + 1
        ax2.axhline(pct, color="grey", linestyle=":", linewidth=0.7)
        ax2.text(len(cum) * 0.6, pct + 1, f"{pct}% covered by top-{n_needed}",
                 fontsize=8, color="grey")

    save_both(fig, out_dir, "sample_size_distribution")


def write_csv(named: list[tuple[str, int]], out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    with (out_dir / "sample_size_distribution.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["dataset", "samples"])
        w.writerows(named)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--metadata", default=None, help="Ignored; sample-size statistics use the live registry.")
    ap.add_argument("--out", default="reports/figures/auto/")
    args = ap.parse_args()

    metadata = load_registry_metadata()
    sizes, named = compute(metadata)
    out_dir = Path(args.out)
    plot(sizes, out_dir)
    write_csv(named, out_dir)
    total = sizes.sum()
    print(f"Datasets with reported sample counts: {len(sizes)}")
    print(f"Total samples: {total:,}")
    print(f"Median: {int(np.median(sizes)):,}; max: {sizes.max():,}; min: {sizes.min():,}")
    print(f"Wrote -> {out_dir}/sample_size_distribution.(png,svg,csv)")


if __name__ == "__main__":
    main()
