"""Figure: dataset count by country/region (geographic bias check).

Usage:
    python hub/stats/geography.py [--metadata hub/metadata.json] [--out reports/figures/auto/]
"""
from __future__ import annotations

import argparse
import csv
import re
from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt

from hub.stats._common import load_metadata, save_both, setup_style


# Region aggregation for high-level bias check
REGIONS = {
    "China": "East Asia",
    "Japan": "East Asia",
    "Korea": "East Asia",
    "India": "South Asia",
    "Pakistan": "South Asia",
    "Bangladesh": "South Asia",
    "Iran": "Middle East",
    "USA": "North America",
    "Canada": "North America",
    "Mexico": "North America",
    "United Kingdom": "Europe",
    "Spain": "Europe",
    "Germany": "Europe",
    "Netherlands": "Europe",
    "France": "Europe",
    "Italy": "Europe",
    "Portugal": "Europe",
    "Switzerland": "Europe",
    "Poland": "Europe",
    "Singapore": "Southeast Asia",
    "Brazil": "Latin America",
    "Argentina": "Latin America",
    "Egypt": "Africa",
    "South Africa": "Africa",
    "Australia": "Oceania",
}


def extract_country(geography_text: str) -> str:
    """Parse the first country mentioned in the metadata's geography field."""
    if not geography_text or geography_text == "not reported":
        return "Unknown"
    # Geography fields are formatted like "China (Beijing — ...)" or "USA (Boston, MA — ...)"
    m = re.match(r"\s*([^(\n,]+?)(?:\s*\(|,|$)", geography_text)
    if not m:
        return "Unknown"
    country = m.group(1).strip()
    # Normalize common variants
    country = country.replace("United States", "USA")
    return country


def compute(metadata: list[dict]) -> tuple[Counter, Counter]:
    countries = Counter()
    regions = Counter()
    for d in metadata:
        c = extract_country(d.get("geography", ""))
        countries[c] += 1
        regions[REGIONS.get(c, "Other / Unknown")] += 1
    return countries, regions


def plot_countries(countries: Counter, out_dir: Path) -> None:
    setup_style()
    fig, ax = plt.subplots(figsize=(8, 5))

    top = countries.most_common(15)
    names = [c for c, _ in top]
    counts = [n for _, n in top]

    bars = ax.barh(names[::-1], counts[::-1], color="#1f77b4")
    ax.set_xlabel("Number of datasets")
    ax.set_title("EyeDataHub dataset origin - top 15 countries")
    for bar, c in zip(bars, counts[::-1]):
        ax.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height() / 2,
                str(c), va="center", fontsize=9)
    save_both(fig, out_dir, "geography_countries")


def plot_regions(regions: Counter, out_dir: Path) -> None:
    setup_style()
    fig, ax = plt.subplots(figsize=(7, 5))

    items = regions.most_common()
    labels = [k for k, _ in items]
    sizes = [v for _, v in items]
    total = sum(sizes)
    autopct = lambda p: f"{p:.0f}%\n({int(round(p * total / 100))})"
    ax.pie(sizes, labels=labels, autopct=autopct, startangle=90,
           wedgeprops={"edgecolor": "white", "linewidth": 1.5})
    ax.set_title(f"EyeDataHub dataset origin by region (n = {total})")

    save_both(fig, out_dir, "geography_regions")


def write_csv(countries: Counter, regions: Counter, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    with (out_dir / "geography.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["country", "count"])
        for k, v in countries.most_common():
            w.writerow([k, v])
        w.writerow([])
        w.writerow(["region", "count"])
        for k, v in regions.most_common():
            w.writerow([k, v])


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--metadata", default="hub/metadata.json")
    ap.add_argument("--out", default="reports/figures/auto/")
    args = ap.parse_args()

    metadata = load_metadata(args.metadata)
    countries, regions = compute(metadata)
    out_dir = Path(args.out)
    plot_countries(countries, out_dir)
    plot_regions(regions, out_dir)
    write_csv(countries, regions, out_dir)
    print(f"Countries represented: {len(countries)}")
    print("Regional balance:")
    for k, v in regions.most_common():
        print(f"  {k}: {v}")
    print(f"Wrote -> {out_dir}/geography_(countries,regions).(png,svg) + geography.csv")


if __name__ == "__main__":
    main()
