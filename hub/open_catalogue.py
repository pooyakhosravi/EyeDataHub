"""
Generate open_licence_catalogue.json — the filtered EyeDataHub-Open subset.

Run:
    python hub/open_catalogue.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from eyedatahub.core.dataset import license_matches_filter
from eyedatahub.datasets.registry import REGISTRY


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _is_open(ds) -> bool:
    """Return True for CC BY*, MIT, CC0 / Public Domain, CC BY-SA."""
    li = ds.info.license
    return (
        license_matches_filter(li, "commercial-ok")
        or ds.info.license_family == "cc-by-sa"
    )


def _task_category(tasks: list[str]) -> str:
    """Broad task bucket for grouping."""
    if "segmentation" in tasks and "classification" in tasks:
        return "segmentation+classification"
    if "segmentation" in tasks:
        return "segmentation"
    if "grading" in tasks:
        return "grading"
    if "multilabel" in tasks:
        return "multilabel"
    if "regression" in tasks:
        return "regression"
    return "classification"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def build_catalogue(out_path: Path | None = None) -> list[dict]:
    datasets = REGISTRY.list_datasets()
    open_ds = [d for d in datasets if _is_open(d)]
    open_ds.sort(key=lambda d: (d.info.modality, d.info.name))

    records = []
    for ds in open_ds:
        i = ds.info
        records.append({
            "name": i.name,
            "full_name": i.full_name,
            "modality": i.modality,
            "tasks": i.tasks,
            "task_category": _task_category(i.tasks),
            "num_samples": i.num_samples,
            "size_gb": i.size_gb,
            "splits": i.splits,
            "num_classes": i.num_classes,
            "classes": i.classes,
            "license": i.license,
            "license_family": i.license_family,
            "download_type": i.download_type,
            "download_url": i.download_url,
            "citation": i.citation,
            "tags": i.tags,
            "notes": i.notes if i.notes else "",
            # placeholders filled by enrich_metadata.py
            "geography": None,
            "scanner_device": None,
            "demographics": {
                "age_range": None,
                "sex_distribution": None,
                "ethnicity": None,
                "num_patients": None
            },
        })

    if out_path is None:
        out_path = Path(__file__).parent / "open_licence_catalogue.json"

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        json.dumps(records, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"Wrote {len(records)} datasets -> {out_path}")
    return records


if __name__ == "__main__":
    build_catalogue()
