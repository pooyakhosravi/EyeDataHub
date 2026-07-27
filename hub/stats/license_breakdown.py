"""Figure: dataset count by license family + commercial-OK percentage.

Produces:
    license_breakdown.png / .svg / .csv

Usage:
    python hub/stats/license_breakdown.py [--out reports/figures/auto/]
"""
from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt

from hub.stats._common import load_registry_metadata, save_both, setup_style


COMMERCIAL_OK = {"cc0", "cc-by", "cc-by-sa", "mit", "apache", "odc-by"}
NON_COMMERCIAL = {"cc-by-nc", "cc-by-nc-sa", "cc-by-nc-nd"}


def compute(metadata: list[dict]) -> tuple[Counter, dict[str, int]]:
    families = Counter(d.get("license_family", "unknown") for d in metadata)
    groups = {
        "commercial-ok": sum(c for f, c in families.items() if f in COMMERCIAL_OK),
        "non-commercial": sum(c for f, c in families.items() if f in NON_COMMERCIAL),
        "research-only": families.get("research-only", 0),
        "unknown": families.get("unknown", 0) + families.get("see-page", 0),
    }
    return families, groups


def plot(families: Counter, out_dir: Path) -> None:
    setup_style()
    fig, ax = plt.subplots(figsize=(7, 4))

    order = [
        "cc0",
        "cc-by",
        "cc-by-sa",
        "mit",
        "apache",
        "odc-by",
        "cc-by-nc",
        "cc-by-nc-sa",
        "cc-by-nc-nd",
        "research-only",
        "unknown",
    ]
    counts = [families.get(k, 0) for k in order]
    colors = (
        ["#2ca02c"] * 6  # commercial-OK = green
        + ["#ff7f0e"] * 3  # non-commercial = orange
        + ["#d62728"]  # research-only = red
        + ["#7f7f7f"]  # unknown = grey
    )

    bars = ax.bar(order, counts, color=colors)
    ax.set_ylabel("Number of datasets")
    ax.set_xlabel("License family")
    ax.set_title("EyeDataHub dataset licenses (n = {})".format(sum(counts)))
    ax.tick_params(axis="x", rotation=30)
    for bar, count in zip(bars, counts):
        if count:
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 0.5,
                str(count),
                ha="center",
                va="bottom",
                fontsize=9,
            )

    save_both(fig, out_dir, "license_breakdown")


def write_csv(families: Counter, groups: dict[str, int], out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    with (out_dir / "license_breakdown.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["license_family", "count"])
        for k, v in sorted(families.items(), key=lambda kv: -kv[1]):
            w.writerow([k, v])
        w.writerow([])
        w.writerow(["license_group", "count"])
        for k, v in groups.items():
            w.writerow([k, v])


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--metadata", default=None, help="Ignored; license statistics use the live registry.")
    ap.add_argument("--out", default="reports/figures/auto/")
    args = ap.parse_args()

    metadata = load_registry_metadata()
    families, groups = compute(metadata)
    out_dir = Path(args.out)
    plot(families, out_dir)
    write_csv(families, groups, out_dir)

    total = sum(families.values())
    pct_commercial = 100 * groups["commercial-ok"] / total if total else 0
    print(f"Total datasets: {total}")
    print(f"Commercial-OK: {groups['commercial-ok']} ({pct_commercial:.1f}%)")
    print(f"Non-commercial CC: {groups['non-commercial']}")
    print(f"Research-only: {groups['research-only']}")
    print(f"Unknown / see-page: {groups['unknown']}")
    print(f"Wrote -> {out_dir}/license_breakdown.(png,svg,csv)")


if __name__ == "__main__":
    main()
