"""Figure: dataset count by source/download platform.

Produces:
    source_platform_breakdown.png / .svg / .csv

Usage:
    python hub/stats/source_platform_breakdown.py [--out reports/figures/auto/]
"""
from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

import matplotlib.pyplot as plt

from hub.stats._common import load_registry_metadata, save_both, setup_style


PLATFORM_LABELS = {
    "mendeley": "Mendeley",
    "zenodo": "Zenodo",
    "kaggle": "Kaggle",
    "huggingface": "Hugging Face",
    "physionet": "PhysioNet",
    "figshare": "Figshare",
    "gdrive": "Google Drive",
    "github": "GitHub",
    "grand-challenge": "Grand Challenge",
    "baidu": "Baidu AI Studio",
    "ieee-dataport": "IEEE DataPort",
    "osf": "OSF",
    "manual": "Manual / gated",
    "direct": "Other direct",
}


def classify_platform(row: dict) -> str:
    download_type = (row.get("download_type") or "").lower()
    url = row.get("download_url") or ""
    host = urlparse(url).netloc.lower()
    full_url = url.lower()

    if "grand-challenge.org" in host:
        return "grand-challenge"
    if "aistudio.baidu.com" in host:
        return "baidu"
    if "ieee-dataport.org" in host:
        return "ieee-dataport"
    if "osf.io" in host:
        return "osf"

    if download_type in PLATFORM_LABELS:
        return download_type
    if "drive.google.com" in host:
        return "gdrive"
    if "github.com" in host or "githubusercontent.com" in host:
        return "github"
    if "huggingface.co" in host:
        return "huggingface"
    if "zenodo.org" in host:
        return "zenodo"
    if "mendeley.com" in host:
        return "mendeley"
    if "kaggle.com" in host:
        return "kaggle"
    if "figshare.com" in host:
        return "figshare"
    if "physionet.org" in host:
        return "physionet"
    if "grand-challenge" in full_url:
        return "grand-challenge"
    return "direct" if download_type == "direct" else "manual"


def compute(metadata: list[dict]) -> Counter:
    return Counter(classify_platform(row) for row in metadata)


def plot(counts: Counter, out_dir: Path) -> None:
    setup_style()
    ordered = sorted(counts.items(), key=lambda kv: (-kv[1], PLATFORM_LABELS.get(kv[0], kv[0])))
    keys = [k for k, _ in ordered]
    values = [v for _, v in ordered]
    labels = [PLATFORM_LABELS.get(k, k) for k in keys]

    fig_height = max(4.4, 0.38 * len(labels) + 1.2)
    fig, ax = plt.subplots(figsize=(7.2, fig_height))
    colors = [
        "#3b7a57",
        "#4c78a8",
        "#f58518",
        "#54a24b",
        "#b279a2",
        "#e45756",
        "#72b7b2",
        "#ff9da6",
        "#9d755d",
        "#bab0ac",
    ]
    bars = ax.barh(labels, values, color=[colors[i % len(colors)] for i in range(len(values))])
    ax.invert_yaxis()
    ax.set_xlabel("Datasets in registry")
    ax.set_ylabel("Primary source or access platform")
    ax.set_title(f"EyeDataHub source-platform coverage (n = {sum(values)})")

    for bar, value in zip(bars, values):
        y = bar.get_y() + bar.get_height() / 2
        ax.text(value + 0.4, y, str(value), va="center", ha="left", fontsize=9)

    ax.set_xlim(0, max(values) + 8)
    ax.tick_params(axis="y", labelsize=9)
    fig.subplots_adjust(left=0.34, right=0.95)
    save_both(fig, out_dir, "source_platform_breakdown")


def write_csv(counts: Counter, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    with (out_dir / "source_platform_breakdown.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["platform", "count"])
        for key, count in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])):
            w.writerow([PLATFORM_LABELS.get(key, key), count])


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--metadata", default=None, help="Ignored; uses the live registry.")
    ap.add_argument("--out", default="reports/figures/auto/")
    args = ap.parse_args()

    metadata = load_registry_metadata()
    counts = compute(metadata)
    out_dir = Path(args.out)
    plot(counts, out_dir)
    write_csv(counts, out_dir)

    print(f"Total datasets: {sum(counts.values())}")
    for key, count in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])):
        print(f"{PLATFORM_LABELS.get(key, key)}: {count}")
    print(f"Wrote -> {out_dir}/source_platform_breakdown.(png,svg,csv)")


if __name__ == "__main__":
    main()
