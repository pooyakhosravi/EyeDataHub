"""Shared loaders + plot styling for hub/stats/ scripts."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt


def load_metadata(metadata_path: str | Path) -> list[dict[str, Any]]:
    """Load enriched dataset metadata from hub/metadata.json."""
    path = Path(metadata_path)
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def load_registry_metadata() -> list[dict[str, Any]]:
    """Return lightweight metadata for every dataset in the live registry."""
    from eyedatahub.datasets.registry import REGISTRY

    rows: list[dict[str, Any]] = []
    for ds in REGISTRY.list_datasets():
        info = ds.info
        rows.append(
            {
                "name": info.name,
                "full_name": info.full_name,
                "modality": info.modality,
                "tasks": list(info.tasks or []),
                "num_samples": info.num_samples,
                "size_gb": info.size_gb,
                "license": info.license,
                "license_family": info.license_family,
                "download_type": info.download_type,
                "download_url": info.download_url,
            }
        )
    return rows


def setup_style() -> None:
    """Apply a consistent matplotlib style for paper figures."""
    plt.rcParams.update(
        {
            "figure.dpi": 150,
            "savefig.dpi": 300,
            "savefig.bbox": "tight",
            "font.family": "sans-serif",
            "font.size": 10,
            "axes.titlesize": 11,
            "axes.labelsize": 10,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.grid": True,
            "grid.alpha": 0.3,
            "grid.linestyle": "--",
        }
    )


def save_both(fig, out_dir: str | Path, basename: str) -> tuple[Path, Path]:
    """Save figure as both PNG (raster) and SVG (vector). Returns the paths."""
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    png = out_dir / f"{basename}.png"
    svg = out_dir / f"{basename}.svg"
    fig.savefig(png)
    fig.savefig(svg)
    plt.close(fig)
    return png, svg
