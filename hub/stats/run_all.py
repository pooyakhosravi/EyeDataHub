"""Run all descriptive-statistic scripts and write outputs to reports/figures/auto/.

Usage:
    python hub/stats/run_all.py [--metadata hub/metadata.json] [--out reports/figures/auto/]
"""
from __future__ import annotations

import argparse
import sys
import traceback
from pathlib import Path

from hub.stats import (
    demographics_coverage,
    geography,
    license_breakdown,
    modality_task_matrix,
    sample_size_distribution,
    scanner_diversity,
    source_platform_breakdown,
)


SCRIPTS = [
    ("license_breakdown", license_breakdown),
    ("source_platform_breakdown", source_platform_breakdown),
    ("modality_task_matrix", modality_task_matrix),
    ("geography", geography),
    ("scanner_diversity", scanner_diversity),
    ("sample_size_distribution", sample_size_distribution),
    ("demographics_coverage", demographics_coverage),
]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--metadata", default="hub/metadata.json")
    ap.add_argument("--out", default="reports/figures/auto/")
    args = ap.parse_args()

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    failures = []
    for name, mod in SCRIPTS:
        print(f"\n=== {name} ===")
        try:
            sys.argv = [name, "--metadata", args.metadata, "--out", str(out_dir)]
            mod.main()
        except Exception:
            print(f"FAILED: {name}")
            traceback.print_exc()
            failures.append(name)

    print(f"\nDone. {len(SCRIPTS) - len(failures)}/{len(SCRIPTS)} scripts succeeded.")
    if failures:
        print("Failed: " + ", ".join(failures))
        return 1
    print(f"Outputs in {out_dir}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
