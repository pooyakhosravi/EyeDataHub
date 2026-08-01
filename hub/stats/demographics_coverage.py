"""Figure: % of datasets reporting age / sex / ethnicity / patient count.

Highlights the metadata reporting gap that EyeDataHub can help quantify.

Usage:
    python hub/stats/demographics_coverage.py [--metadata hub/metadata.json] [--out reports/figures/auto/]
"""
from __future__ import annotations

import argparse
import csv
from pathlib import Path

import matplotlib.pyplot as plt

from hub.stats._common import load_metadata, save_both, setup_style


FIELDS = [
    ("age_range", "Age range"),
    ("sex_distribution", "Sex distribution"),
    ("ethnicity", "Ethnicity"),
    ("num_patients", "Patient count"),
]


def is_reported(value) -> bool:
    if value is None:
        return False
    if isinstance(value, (int, float)):
        return value > 0
    s = str(value).strip().lower()
    return bool(s) and s not in ("not reported", "unknown", "n/a", "nan", "")


def compute(metadata: list[dict]) -> dict[str, float]:
    out = {}
    n = len(metadata)
    for key, _ in FIELDS:
        reported = sum(
            1 for d in metadata if is_reported(d.get("demographics", {}).get(key) if "demographics" in d else d.get(key))
        )
        out[key] = 100 * reported / n if n else 0
    return out


def plot(percentages: dict[str, float], out_dir: Path) -> None:
    setup_style()
    fig, ax = plt.subplots(figsize=(7, 4))

    labels = [label for _, label in FIELDS]
    values = [percentages[key] for key, _ in FIELDS]
    colors = ["#2ca02c" if v >= 50 else "#ff7f0e" if v >= 25 else "#d62728" for v in values]

    bars = ax.bar(labels, values, color=colors)
    ax.set_ylabel("% datasets reporting field")
    ax.set_ylim(0, 100)
    ax.set_title("Demographic metadata coverage across EyeDataHub datasets")
    for bar, v in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1.5,
                f"{v:.0f}%", ha="center", fontsize=10)
    ax.axhline(50, color="grey", linestyle="--", linewidth=0.8)
    save_both(fig, out_dir, "demographics_coverage")


def write_csv(percentages: dict[str, float], out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    with (out_dir / "demographics_coverage.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["field", "label", "pct_reported"])
        for key, label in FIELDS:
            w.writerow([key, label, round(percentages[key], 1)])


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--metadata", default="hub/metadata.json")
    ap.add_argument("--out", default="reports/figures/auto/")
    args = ap.parse_args()

    metadata = load_metadata(args.metadata)
    percentages = compute(metadata)
    out_dir = Path(args.out)
    plot(percentages, out_dir)
    write_csv(percentages, out_dir)
    print("Demographic-field coverage:")
    for key, label in FIELDS:
        print(f"  {label}: {percentages[key]:.0f}%")
    print(f"Wrote -> {out_dir}/demographics_coverage.(png,svg,csv)")


if __name__ == "__main__":
    main()
