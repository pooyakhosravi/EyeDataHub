"""Generate llms-full.txt, a token-efficient full catalog for software clients.

Produces one compact catalog of every registered dataset with
name, modality, tasks, license family, access state, loader status,
download URL, and a one-line description. Optimized to fit
entire ophthalmic dataset landscape into an agent's context window.

Run:
    python -m hub.docs.generate_llms_full
"""
from __future__ import annotations

import argparse
from pathlib import Path

from eyedatahub.agent.planner import access_state, loader_status
from eyedatahub.core.resource_identity import dataset_family_for, resource_role_for
from eyedatahub.datasets.registry import REGISTRY


STANDARD_NO_NC = {"cc0", "cc-by", "cc-by-sa", "mit", "apache", "odc-by"}


def build(root: Path) -> Path:
    all_ds = sorted(REGISTRY.list_datasets(), key=lambda d: (d.info.modality, d.info.name))
    lines = [
        "# EyeDataHub full catalog snapshot",
        "",
        "> Token-efficient dump of the versioned EyeDataHub metadata for",
        "> software clients. One line per record. Regenerate with:",
        ">   python -m hub.docs.generate_llms_full",
        "",
        f"## Summary: {len(all_ds)} current records in "
        f"{len({dataset_family_for(d.info.name) for d in all_ds})} dataset families; "
        f"{sum(d.info.num_samples is not None for d in all_ds)} with a primary reported quantity; "
        f"{sum(d.info.size_gb or 0 for d in all_ds):.0f} GB",
        "",
        "## Legend",
        "",
        "- FAM: license family (cc0/cc-by/cc-by-sa/mit/apache/odc-by/cc-by-nc/cc-by-nc-sa/cc-by-nc-nd/research-only/unknown)",
        "- SNC: `Y` = source terms have no explicit noncommercial clause; this is not a permission finding",
        "- BAK: recorded access backend",
        "- ACCESS: human action, credentials or terms, or explicit download required",
        "- LOAD: `implemented` or `metadata_only`",
        "- ROLE: reviewed resource role",
        "- DFAM: narrow dataset-family identifier",
        "- PUB: initial public dataset release (YYYY, YYYY-MM, or YYYY-MM-DD); ? = unknown. Source evidence is available via eyehub show --json.",
        "",
        "## Format",
        "",
        "```",
        "<name> | <modality> | TASK=<tasks> | PUB=<initial_publication_date> | ROLE=<role> DFAM=<dataset_family> | FAM=<license_family> SNC=<y/n/?> | BAK=<backend> ACCESS=<state> LOAD=<status> | N=<reported_count and unit> | URL=<source> | <full_name>: <description>",
        "```",
        "",
    ]

    current_mod = None
    for d in all_ds:
        info = d.info
        if info.modality != current_mod:
            current_mod = info.modality
            lines.append(f"\n## Modality: {info.modality}\n")
        com = "Y" if info.license_family in STANDARD_NO_NC else (
            "?" if info.license_family == "unknown" else "N"
        )
        if info.num_samples is None:
            n = "?"
        else:
            unit = (info.item_count_unit or "unit_not_resolved").replace(" ", "_")
            n = f"{info.num_samples:,}_{unit}"
        tasks = ",".join(info.tasks or []) or "?"
        source = info.download_url or "?"
        lines.append(
            f"- `{info.name}` | {info.modality} | "
            f"TASK={tasks} | "
            f"PUB={info.publication_date or '?'} | "
            f"ROLE={resource_role_for(info.name)} "
            f"DFAM={dataset_family_for(info.name)} | "
            f"FAM={info.license_family} SNC={com} | "
            f"BAK={info.download_type} ACCESS={access_state(d)} "
            f"LOAD={loader_status(d)} | N={n} | URL={source} | "
            f"{info.full_name}: {info.description}"
        )

    lines += [
        "",
        "## Programmatic access",
        "",
        "```python",
        "from eyedatahub.datasets.registry import REGISTRY",
        "from eyedatahub.agent import build_fundus_foundation_plan",
        "",
        "# Inspect candidates without moving data",
        "ok = [d for d in REGISTRY.list_datasets() if d.info.license_family in ('cc0','cc-by','cc-by-sa','mit','apache','odc-by')]",
        "ds = REGISTRY.get_dataset('brset')",
        "print(ds.info)",
        "",
        "# Build a reviewable plan",
        "plan = build_fundus_foundation_plan(gaps=['glaucoma', 'amd'])",
        "```",
        "",
        "```bash",
        "eyehub search --access anonymous_direct --json",
        "eyehub show brset --json",
        "eyehub cite brset --type dataset --format bibtex",
        "eyehub download brset --dry-run --json",
        "```",
        "",
    ]

    out = root / "llms-full.txt"
    out.write_text("\n".join(lines), encoding="utf-8")
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", default=".", help="Repo root (llms-full.txt goes here)")
    args = ap.parse_args()
    path = build(Path(args.root))
    print(f"Wrote {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
