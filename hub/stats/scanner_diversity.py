"""Figure: scanner manufacturer distribution per modality.

Usage:
    python hub/stats/scanner_diversity.py [--metadata hub/metadata.json] [--out reports/figures/auto/]
"""
from __future__ import annotations

import argparse
import csv
import re
from collections import Counter, defaultdict
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from hub.stats._common import load_metadata, save_both, setup_style


MANUFACTURERS = [
    "Topcon", "Zeiss", "Heidelberg", "Optos", "Canon", "Nikon",
    "Optovue", "Kowa", "RetCam", "Humphrey", "Various", "Mixed",
]


def normalize(scanner_text: str) -> str:
    """Match scanner string to a known manufacturer or return 'Other'."""
    if not scanner_text or scanner_text == "not reported":
        return "Unknown"
    s = scanner_text.lower()
    for m in MANUFACTURERS:
        if m.lower() in s:
            return m if m not in ("Various", "Mixed") else "Mixed / Various"
    return "Other"


def compute(metadata: list[dict]) -> dict[str, Counter]:
    """Returns {modality: Counter(manufacturer -> count)}."""
    out = defaultdict(Counter)
    for d in metadata:
        mod = d.get("modality", "unknown")
        scanner = d.get("scanner_device", "")
        out[mod][normalize(scanner)] += 1
    return out


def plot(per_modality: dict[str, Counter], out_dir: Path) -> None:
    setup_style()
    modalities = [m for m in per_modality if sum(per_modality[m].values()) > 0]
    all_manufacturers = sorted(
        {man for counters in per_modality.values() for man in counters},
        key=lambda m: -sum(per_modality[mod].get(m, 0) for mod in modalities),
    )

    fig, ax = plt.subplots(figsize=(9, 5))
    bottom = np.zeros(len(modalities))
    cmap = plt.cm.tab20.colors
    for i, man in enumerate(all_manufacturers):
        vals = np.array([per_modality[mod].get(man, 0) for mod in modalities])
        ax.bar(modalities, vals, bottom=bottom, label=man, color=cmap[i % len(cmap)])
        bottom += vals

    ax.set_ylabel("# datasets")
    ax.set_xlabel("Modality")
    ax.set_title("Scanner manufacturer diversity across EyeDataHub datasets")
    ax.tick_params(axis="x", rotation=30)
    ax.legend(bbox_to_anchor=(1.02, 1), loc="upper left", fontsize=8)
    save_both(fig, out_dir, "scanner_diversity")


def write_csv(per_modality: dict[str, Counter], out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    rows = []
    for mod, counts in per_modality.items():
        for man, n in counts.items():
            rows.append((mod, man, n))
    rows.sort(key=lambda r: (r[0], -r[2]))
    with (out_dir / "scanner_diversity.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["modality", "manufacturer", "n_datasets"])
        w.writerows(rows)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--metadata", default="hub/metadata.json")
    ap.add_argument("--out", default="reports/figures/auto/")
    args = ap.parse_args()

    metadata = load_metadata(args.metadata)
    per_modality = compute(metadata)
    out_dir = Path(args.out)
    plot(per_modality, out_dir)
    write_csv(per_modality, out_dir)
    print(f"Wrote -> {out_dir}/scanner_diversity.(png,svg,csv)")


if __name__ == "__main__":
    main()
