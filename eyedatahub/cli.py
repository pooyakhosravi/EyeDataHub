"""EyeDataHub command-line interface."""
from __future__ import annotations

import json
from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
from pathlib import Path
from typing import Optional

import click
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from eyedatahub import __version__
from eyedatahub.catalog import citation_payload, dataset_to_record, search_datasets
from eyedatahub.core.metadata import (
    ACCESS_FRICTION_VALUES,
    ACQUISITION_SUPPORT_VALUES,
    AVAILABILITY_STATUS_VALUES,
    normalize_modality_label,
)

console = Console()

# ─────────────────────────── helpers ────────────────────────────────────────


def _get_registry():
    """Lazy import to speed up CLI startup."""
    from eyedatahub.datasets.registry import REGISTRY
    return REGISTRY


_MODALITY_ALIASES = {
    "uwf": "uwf_fundus",
    "uwf_fundus": "uwf_fundus",
    "octa": "octa",
    "ivcm": "confocal",
    "confocal": "confocal",
    "surgical": "surgical_video",
    "surgical_video": "surgical_video",
    "visual_fields": "visual_field",
    "visual_field": "visual_field",
    "external": "external_eye",
    "external_eye": "external_eye",
    "eyelid": "external_eye",
    "meibography": "external_eye",
    "conjunctiva": "external_eye",
    "cell_microscopy": "cell_microscopy",
    "cellular_microscopy": "cell_microscopy",
    "adaptive_optics": "adaptive_optics",
    "aoslo": "adaptive_optics",
    "omics": "omics",
    "genomics": "omics",
    "gaze": "eye_tracking",
    "eye_tracking": "eye_tracking",
    "eyetracking": "eye_tracking",
    "pupil": "eye_tracking",
    "iris": "iris_biometrics",
    "iris_biometrics": "iris_biometrics",
    "ocular_biometrics": "iris_biometrics",
    "biometrics": "iris_biometrics",
}


def _normalize_modality(modality: Optional[str]) -> Optional[str]:
    if not modality:
        return None
    return _MODALITY_ALIASES.get(modality.lower(), normalize_modality_label(modality))


def _resolve_datasets(datasets_str: str, modality_filter: Optional[str] = None):
    """
    Resolve the --datasets argument to a list of dataset instances.

    Accepts:
      - "all"  -> all registered datasets
      - "fundus" / "oct" / other modality names
      - comma-separated dataset names
    """
    registry = _get_registry()

    if datasets_str.lower() == "all":
        return registry.list_datasets(modality=modality_filter)

    # Check if it looks like a modality name or common modality alias.
    available_modalities = {
        modality
        for dataset in registry.list_datasets()
        for modality in dataset.info.modalities
    }
    key = datasets_str.lower()
    modality = _normalize_modality(key)
    if modality in available_modalities:
        return registry.list_datasets(modality=modality)

    # Comma-separated list of dataset names
    names = [n.strip() for n in datasets_str.split(",") if n.strip()]
    result = []
    for name in names:
        try:
            result.append(registry.get_dataset(name))
        except KeyError:
            console.print(f"[yellow]Warning: Dataset '{name}' not found in the catalog[/]")
    return result


def _filter_by_task(datasets, task_filter: str):
    """Filter datasets by task type."""
    if task_filter.lower() == "all":
        return datasets
    task = task_filter.lower()
    return [d for d in datasets if task in d.info.tasks]


def _filter_by_license(datasets, license_type: Optional[str]):
    """Filter datasets by license family or group."""
    if not license_type or license_type.lower() in ("any", "all"):
        return datasets
    from eyedatahub.core.dataset import license_matches_filter
    return [d for d in datasets if license_matches_filter(d.info.license, license_type)]


# ─────────────────────────── main group ─────────────────────────────────────


@click.group()
@click.version_option(version=__version__, prog_name="eyehub")
def main():
    """
    EyeDataHub: source-term-aware ophthalmology dataset access tool.

    \b
    Quick start:
      pip install eyedatahub
      eyehub search --modality fundus --access anonymous_direct
      eyehub show airogs
      eyehub download airogs --dry-run
      eyehub cite airogs --type dataset --format bibtex

    Search, show, cite, JSON and MCP operations are read-only. Transfer starts
    only through an explicit non-dry-run download command. EyeDataHub never
    accepts source terms or agreements for a user and does not provide legal
    advice.
    """


# ─────────────────────────── list ───────────────────────────────────────────


@main.group()
def list():
    """List available datasets, tasks, or modalities."""


@list.command(name="datasets")
@click.option(
    "--modality",
    "-m",
    default=None,
    help=(
        "Filter by modality (fundus, oct, octa, uwf/uwf_fundus, "
        "confocal/ivcm, surgical_video, visual_field, external_eye/eyelid, "
        "cell_microscopy, adaptive_optics/aoslo, omics/genomics, multimodal)"
    ),
)
@click.option("--task", "-t", default=None, help="Filter by task (classification, segmentation, ...)")
@click.option(
    "--access",
    "access_friction",
    default=None,
    help="Filter by access friction (anonymous_direct, self_service_authenticated, controlled_or_manual, ...).",
)
@click.option(
    "--acquisition-support",
    default=None,
    help="Filter by acquisition support (standard_platform_supported, guided_instructions_only, ...).",
)
@click.option(
    "--license-type",
    "-l",
    default=None,
    help=(
        "Filter by license. Families: cc0, cc-by, cc-by-sa, mit, apache, odc-by, "
        "cc-by-nc, cc-by-nc-sa, cc-by-nc-nd, research-only, unknown. "
        "Groups: standard-no-nc, non-commercial."
    ),
)
@click.option(
    "--downloaded",
    is_flag=True,
    default=False,
    help="Show only datasets already downloaded",
)
@click.option(
    "--data-dir",
    default="~/.eyedatahub/data",
    show_default=True,
    help="Data root directory",
)
@click.option(
    "--json",
    "as_json",
    is_flag=True,
    default=False,
    help="Emit machine-readable JSON instead of a formatted table.",
)
def list_datasets(
    modality,
    task,
    license_type,
    access_friction,
    acquisition_support,
    downloaded,
    data_dir,
    as_json,
):
    """List all available datasets with metadata."""
    registry = _get_registry()
    data_root = Path(data_dir).expanduser()
    datasets = registry.list_datasets(modality=_normalize_modality(modality), task=task)
    datasets = _filter_by_license(datasets, license_type)
    if access_friction:
        datasets = [d for d in datasets if d.info.access_friction == access_friction]
    if acquisition_support:
        datasets = [d for d in datasets if d.info.acquisition_support == acquisition_support]
    datasets = sorted(datasets, key=lambda item: item.info.name)

    if as_json:
        import json
        out = []
        for ds in datasets:
            is_dl = ds.is_downloaded(data_root)
            if downloaded and not is_dl:
                continue
            out.append(dataset_to_record(ds, data_root))
        print(json.dumps(out, indent=2))
        return

    if not datasets:
        console.print("[yellow]No datasets found matching the filter.[/]")
        return

    table = Table(
        title=f"EyeDataHub Datasets ({len(datasets)} total)",
        show_header=True,
        header_style="bold cyan",
        show_lines=False,
    )
    table.add_column("Name", style="bold", min_width=12)
    table.add_column("Full Name", min_width=30)
    table.add_column("Modality", justify="center")
    table.add_column("Tasks", min_width=20)
    table.add_column("Samples", justify="right")
    table.add_column("Size", justify="right")
    table.add_column("Source terms", justify="center", min_width=12)
    table.add_column("Access", justify="center")
    table.add_column("Acquisition", justify="center")
    table.add_column("Status", justify="center")

    shown = 0
    for ds in datasets:
        info = ds.info
        is_dl = ds.is_downloaded(data_root)
        if downloaded and not is_dl:
            continue

        status = "[green]Downloaded[/]" if is_dl else "[dim]Not downloaded[/]"
        size_str = f"{info.size_gb:.1f} GB" if info.size_gb else "-"
        tasks_str = ", ".join(info.tasks)
        # Color-code license family
        family = info.license_family
        lic_display = info.license_display
        if family in ("cc0", "cc-by", "cc-by-sa", "mit", "apache", "odc-by"):
            lic_str = f"[green]{lic_display}[/]"
        elif family in ("cc-by-nc", "cc-by-nc-sa", "cc-by-nc-nd"):
            lic_str = f"[yellow]{lic_display}[/]"
        elif family == "research-only":
            lic_str = f"[red]{lic_display}[/]"
        else:
            lic_str = f"[dim]{lic_display}[/]"

        table.add_row(
            info.name,
            info.full_name[:45] + "..." if len(info.full_name) > 45 else info.full_name,
            info.modality,
            tasks_str,
            f"{info.num_samples:,}" if info.num_samples is not None else "?",
            size_str,
            lic_str,
            info.access_friction,
            info.acquisition_support,
            status,
        )
        shown += 1

    console.print(table)

    if shown == 0:
        console.print("[yellow]No downloaded datasets found. Run `eyehub download` first.[/]")
    else:
        console.print(
            f"\n[dim]Tip: inspect first with `eyehub download {datasets[0].info.name} --dry-run`.[/]"
        )


@main.command(name="search")
@click.argument("query", required=False)
@click.option("--modality", "modalities", multiple=True, help="Repeat to match any contained modality.")
@click.option("--task", "tasks", multiple=True, help="Repeat to require multiple tasks.")
@click.option(
    "--access",
    "access_values",
    multiple=True,
    type=click.Choice(sorted(ACCESS_FRICTION_VALUES), case_sensitive=False),
    help="Access-friction category.",
)
@click.option("--source-terms", "term_values", multiple=True, help="Normalized source-term family or group.")
@click.option(
    "--acquisition-support",
    "automation_values",
    multiple=True,
    type=click.Choice(sorted(ACQUISITION_SUPPORT_VALUES), case_sensitive=False),
    help="Acquisition-support category.",
)
@click.option(
    "--availability",
    "availability_values",
    multiple=True,
    type=click.Choice(sorted(AVAILABILITY_STATUS_VALUES), case_sensitive=False),
    help="Availability status.",
)
@click.option("--json", "as_json", is_flag=True, help="Emit deterministic JSON.")
def search_catalog(
    query,
    modalities,
    tasks,
    access_values,
    term_values,
    automation_values,
    availability_values,
    as_json,
):
    """Search the catalog without initiating a transfer."""
    results = search_datasets(
        _get_registry().list_datasets(),
        query=query,
        modalities=modalities,
        tasks=tasks,
        access_friction=access_values,
        source_terms=term_values,
        acquisition_support=automation_values,
        availability_status=availability_values,
    )
    if as_json:
        click.echo(json.dumps([dataset_to_record(item) for item in results], indent=2))
        return
    if not results:
        console.print("[yellow]No catalog records matched.[/]")
        return
    table = Table(title=f"EyeDataHub search ({len(results)} records)", header_style="bold cyan")
    table.add_column("Record")
    table.add_column("Primary category")
    table.add_column("Modalities")
    table.add_column("Access")
    table.add_column("Acquisition")
    table.add_column("Source terms")
    for dataset in results:
        info = dataset.info
        table.add_row(
            info.name,
            info.primary_category,
            ", ".join(info.modalities),
            info.access_friction,
            info.acquisition_support,
            info.license_family,
        )
    console.print(table)


@list.command(name="tasks")
def list_tasks():
    """List all supported evaluation tasks and their metrics."""
    tasks_info = [
        (
            "classification",
            "Multi-class image classification",
            "Accuracy, Balanced Accuracy, Macro F1, AUC-ROC, Cohen Kappa",
        ),
        (
            "grading",
            "Ordinal severity grading (e.g. DR 0-4)",
            "All classification metrics + Quadratic Weighted Kappa, MAE",
        ),
        (
            "segmentation",
            "Binary pixel-level segmentation",
            "Dice, IoU, Pixel Accuracy, Sensitivity, Specificity",
        ),
        (
            "multilabel",
            "Multi-label disease classification",
            "Hamming Loss, Subset Accuracy, Macro F1, mAP, Per-class AUC",
        ),
        (
            "regression",
            "Continuous value prediction",
            "MAE, MSE, RMSE, R², Pearson r, Spearman r",
        ),
    ]

    table = Table(
        title="Supported Evaluation Tasks",
        show_header=True,
        header_style="bold cyan",
    )
    table.add_column("Task", style="bold")
    table.add_column("Description")
    table.add_column("Metrics computed")

    for task_type, desc, metrics in tasks_info:
        table.add_row(task_type, desc, metrics)

    console.print(table)


# ─────────────────────────── show ───────────────────────────────────────────


@main.command(name="show")
@click.argument("name", type=str)
@click.option(
    "--copy",
    type=click.Choice(["cli", "python", "bibtex", "apa", "url"]),
    default=None,
    help="Print ONLY the requested snippet - pipe to clipboard, e.g. `eyehub show brset --copy cli | pbcopy`.",
)
@click.option(
    "--json",
    "as_json",
    is_flag=True,
    default=False,
    help="Emit full dataset metadata as JSON. Composes with --copy=none.",
)
@click.option(
    "--data-dir",
    default="~/.eyedatahub/data",
    show_default=True,
    help="Data root - used to check download status",
)
def show_dataset(name, copy, as_json, data_dir):
    """Show full detail for a single dataset, with copyable snippets.

    \b
    Examples:
      eyehub show brset
      eyehub show brset --copy cli | clip     (Windows)
      eyehub show brset --copy bibtex >> refs.bib
    """
    registry = _get_registry()
    data_root = Path(data_dir).expanduser()

    try:
        ds = registry.get_dataset(name)
    except KeyError:
        console.print(f"[red]Dataset '{name}' not found in the catalog.[/]")
        near = [n for n in registry.names() if name.lower() in n.lower() or n.lower() in name.lower()]
        if near:
            console.print(f"[yellow]Did you mean:[/] {', '.join(near[:8])}")
        raise SystemExit(1)

    info = ds.info

    # Copyable snippets preserve the explicit preflight and acquisition boundary.
    cli_snip = (
        f"eyehub download {info.name} --dry-run\n"
        f"eyehub download {info.name}"
    )
    if info.acquisition_support in {
        "manual_access_blocked",
        "guided_instructions_only",
        "unsupported",
        "unavailable",
    }:
        cli_snip = (
            f"# EyeDataHub will not automate this represented route.\n"
            f"eyehub download {info.name} --dry-run\n"
            f"# Official source: {info.preferred_route_url or info.source_landing_page_url}"
        )
    data_dir_literal = repr(str(data_dir))
    py_snip = (
        "from pathlib import Path\n"
        "from eyedatahub.acquisition import acquire_dataset, preflight_dataset\n"
        "from eyedatahub.datasets.registry import REGISTRY\n"
        f"ds = REGISTRY.get_dataset('{info.name}')\n"
        f"data_dir = Path({data_dir_literal}).expanduser()\n"
        "plan = preflight_dataset(ds, data_dir)  # read-only\n"
        "result = acquire_dataset(ds, data_dir)  # explicit transfer request"
    )
    citations = citation_payload(info)
    bibtex = citations["dataset"]["bibtex"]
    apa = citations["dataset"]["plain"]
    url = info.download_url or ""

    # --copy mode: emit ONLY the snippet, no rich formatting.
    if copy:
        text = {
            "cli": cli_snip,
            "python": py_snip,
            "bibtex": bibtex,
            "apa": apa,
            "url": url,
        }[copy]
        # print() bypasses rich so shell-piping works cleanly.
        print(text)
        return

    # --json mode: full metadata + copy snippets in a single object.
    if as_json:
        import json
        payload = dataset_to_record(ds, data_root)
        payload["citations"] = citations
        payload["snippets"] = {
            "cli": cli_snip,
            "python": py_snip,
            "bibtex": bibtex,
            "apa": apa,
            "url": url,
        }
        print(json.dumps(payload, indent=2))
        return

    # Full rich display
    from rich import box

    header = Panel(
        f"[bold cyan]{info.full_name}[/]\n"
        f"[dim]{info.description or ''}[/]",
        title=f"eyehub:{info.name}",
        border_style="cyan",
        box=box.ROUNDED,
    )
    console.print(header)

    # At-a-glance table
    tbl = Table(show_header=False, box=box.MINIMAL, padding=(0, 1))
    tbl.add_column("Field", style="bold")
    tbl.add_column("Value")
    tbl.add_row("Short name", f"[bold]{info.name}[/]")
    tbl.add_row("Primary category", info.primary_category)
    tbl.add_row("Modalities", ", ".join(info.modalities))
    tbl.add_row("Tasks", ", ".join(info.tasks) if info.tasks else "-")
    tbl.add_row(
        "Samples",
        f"{info.num_samples:,}" if info.num_samples else "-",
    )
    tbl.add_row("Classes", str(info.num_classes) if info.num_classes else "-")
    tbl.add_row("Splits", ", ".join(info.splits) if info.splits else "-")
    tbl.add_row("Size", f"{info.size_gb:.1f} GB" if info.size_gb else "-")
    tbl.add_row("Source-stated terms", info.source_terms or "unknown")
    tbl.add_row("Normalized source-term category", info.license_family)
    tbl.add_row("Terms scope", info.terms_scope)
    tbl.add_row("Terms evidence", info.terms_evidence_url or "unknown")
    tbl.add_row("Access friction", info.access_friction)
    tbl.add_row("Availability", info.availability_status)
    tbl.add_row("Route checked", info.route_last_checked or "unknown")
    tbl.add_row("Acquisition support", info.acquisition_support)
    tbl.add_row("Loader backend", info.loader_backend)
    tbl.add_row("Manual approval", str(info.requires_manual_approval).lower() if info.requires_manual_approval is not None else "unknown")
    tbl.add_row("Author contact", str(info.requires_author_contact).lower() if info.requires_author_contact is not None else "unknown")
    tbl.add_row("Payment", str(info.requires_payment).lower() if info.requires_payment is not None else "unknown")
    tbl.add_row(
        "Status",
        "[green]Downloaded[/]" if ds.is_downloaded(data_root) else "[dim]Not downloaded[/]",
    )
    if info.download_url:
        tbl.add_row("URL", info.download_url)
    console.print(tbl)

    if info.notes:
        console.print(Panel(info.notes, title="Notes", border_style="yellow", box=box.MINIMAL))

    console.print(
        Panel(
            f"[bold]CLI[/]\n[green]{cli_snip}[/]\n\n"
            f"[bold]Python[/]\n[green]{py_snip}[/]",
            title="Copy-paste: preflight and explicit acquisition",
            border_style="blue",
            box=box.MINIMAL,
        )
    )

    console.print(
        Panel(
            f"[bold]BibTeX[/]\n[green]{bibtex}[/]\n\n"
            f"[bold]Plain text[/]\n[green]{apa}[/]",
            title="Copy-paste: citation",
            border_style="magenta",
            box=box.MINIMAL,
        )
    )

    console.print(
        "\n[dim]Tip: pipe a snippet directly to clipboard, e.g. "
        f"[bold]eyehub show {info.name} --copy bibtex[/] "
        "for BibTeX only, or [bold]--copy cli/python/apa/url[/]."
    )


_FAMILY_TO_COMMERCIAL = {
    "cc0": "No explicit noncommercial clause in the normalized source label",
    "cc-by": "No explicit noncommercial clause in the normalized source label",
    "cc-by-sa": "No explicit noncommercial clause in the normalized source label",
    "mit": "Software-style term; verify whether it applies to dataset files",
    "apache": "Software-style term; verify whether it applies to dataset files",
    "odc-by": "No explicit noncommercial clause in the normalized source label",
    "cc-by-nc": "Normalized source label includes noncommercial terms",
    "cc-by-nc-sa": "Normalized source label includes noncommercial terms",
    "cc-by-nc-nd": "Normalized source label includes noncommercial and no-derivatives terms",
    "research-only": "Source-stated research-use restriction",
    "unknown": "Unknown; inspect the source evidence",
}


def _commercial_from_family(family: str) -> str:
    """Backward-compatible label that makes no permission determination."""
    return _FAMILY_TO_COMMERCIAL.get(family, "Unknown; inspect the source evidence")


def _build_bibtex(info) -> str:
    """Minimal BibTeX from a DatasetInfo - same shape as the docs generator."""
    import re
    key = re.sub(r"[^a-z0-9]+", "_", info.name.lower()).strip("_")
    citation = (info.citation or "").strip().rstrip(".") or info.full_name
    m = re.search(r"\b(19|20|21)\d{2}\b", citation)
    year = m.group(0) if m else ""
    lines = [
        "@misc{" + key + ",",
        f"  title  = {{ {info.full_name} }},",
        f"  note   = {{ {citation} }},",
    ]
    if year:
        lines.append(f"  year   = {{ {year} }},")
    if info.download_url:
        lines.append(f"  url    = {{ {info.download_url} }},")
    lines.append("}")
    return "\n".join(lines)


@main.command(name="cite")
@click.argument("name")
@click.option(
    "--type",
    "citation_type",
    type=click.Choice(["dataset", "article", "software", "all"]),
    default="dataset",
    show_default=True,
    help="Select the identifier-bearing object to cite.",
)
@click.option(
    "--format",
    "output_format",
    type=click.Choice(["plain", "bibtex", "json"]),
    default="plain",
    show_default=True,
)
def cite_dataset(name, citation_type, output_format):
    """Export dataset, associated-article, and software citations separately."""
    try:
        info = _get_registry().get_dataset(name).info
    except KeyError as exc:
        raise click.ClickException(str(exc)) from exc
    payload = citation_payload(info)
    if output_format == "json" or citation_type == "all":
        selected = payload if citation_type == "all" else payload[
            "associated_article" if citation_type == "article" else citation_type
        ]
        click.echo(json.dumps(selected, indent=2))
        return
    key = "associated_article" if citation_type == "article" else citation_type
    value = payload[key].get(output_format)
    if not value:
        raise click.ClickException(
            f"No {citation_type} {output_format} citation is recorded for '{name}'."
        )
    click.echo(value)


@main.group(name="agent")
def agent():
    """Build machine-readable plans for bounded agent workflows."""


@agent.command(name="plan-fundus-foundation")
@click.option(
    "--license-type",
    default="standard-no-nc",
    show_default=True,
    type=click.Choice(
        ["standard-no-nc", "non-commercial", "research-only", "unknown", "any"],
        case_sensitive=False,
    ),
    help="License filter applied to pretraining and validation candidates.",
)
@click.option(
    "--max-pretraining-datasets",
    default=8,
    show_default=True,
    type=click.IntRange(1, 50),
    help="Maximum number of datasets in the proposed pretraining pool.",
)
@click.option(
    "--gap",
    "gaps",
    multiple=True,
    help=(
        "Disease or task gap to cover with held-out datasets. Repeat this "
        "option for multiple gaps."
    ),
)
@click.option(
    "--max-validation-per-gap",
    default=3,
    show_default=True,
    type=click.IntRange(1, 10),
    help="Maximum held-out dataset candidates returned for each gap.",
)
@click.option(
    "--include-manual",
    is_flag=True,
    default=False,
    help="Include candidates that require manual or approval-based access.",
)
@click.option(
    "--output",
    type=click.Path(path_type=Path, dir_okay=False),
    default=None,
    help="Write the JSON plan to a file instead of standard output.",
)
def plan_fundus_foundation(
    license_type,
    max_pretraining_datasets,
    gaps,
    max_validation_per_gap,
    include_manual,
    output,
):
    """Plan a fundus foundation-model dataset and evaluation loop."""
    from eyedatahub.agent.planner import build_fundus_foundation_plan

    plan = build_fundus_foundation_plan(
        license_type=license_type,
        max_pretraining_datasets=max_pretraining_datasets,
        gaps=gaps or None,
        max_validation_per_gap=max_validation_per_gap,
        include_manual=include_manual,
    )
    rendered = json.dumps(plan, indent=2)
    if output is None:
        click.echo(rendered)
        return
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(rendered + "\n", encoding="utf-8")
    console.print(f"[green]Wrote agent plan to {output}[/]")


# ─────────────────────────── download ───────────────────────────────────────


def _print_preflight(plan: dict) -> None:
    """Render the operational preflight without exposing credential values."""
    from rich import box

    table = Table(show_header=False, box=box.MINIMAL, padding=(0, 1))
    table.add_column("Field", style="bold")
    table.add_column("Value")
    table.add_row("Record", plan["record_id"])
    table.add_row("Official source", plan["source_landing_page_url"] or "unknown")
    table.add_row("Preferred route", plan["preferred_route_url"] or "unknown")
    table.add_row("Access friction", plan["access_friction"])
    table.add_row("Availability", plan["availability_status"])
    table.add_row("Route check", f"{plan['route_last_checked'] or 'unknown'} ({plan['route_check_result']})")
    table.add_row("Source-stated terms", plan["source_terms"] or "unknown")
    table.add_row("Terms scope", plan["terms_scope"])
    table.add_row("Terms evidence", plan["terms_evidence_url"] or "unknown")
    table.add_row("Acquisition support", plan["acquisition_support"])
    table.add_row("Loader", f"{plan['loader_backend']} / {plan['loader_name']}")
    requirements = plan["access_requirements"]
    for label, key in (
        ("Registration", "requires_registration"),
        ("Authentication", "requires_authentication"),
        ("API token", "requires_api_token"),
        ("Click-through", "requires_clickthrough"),
        ("Manual approval", "requires_manual_approval"),
        ("Data-use agreement", "requires_data_use_agreement"),
        ("Author contact", "requires_author_contact"),
        ("Payment", "requires_payment"),
    ):
        value = requirements[key]
        table.add_row(label, "unknown" if value is None else str(value).lower())
    table.add_row("Preflight status", plan["status"])
    if plan["blocked_reason"]:
        table.add_row("Blocked reason", plan["blocked_reason"])
    console.print(table)
    for warning in plan["warnings"]:
        console.print(f"[yellow]Warning:[/] {warning}")
    console.print(
        "[dim]EyeDataHub does not accept source terms or agreements and does not provide legal advice.[/]"
    )


@main.command(name="preflight")
@click.argument("name")
@click.option(
    "--data-dir",
    default="~/.eyedatahub/data",
    show_default=True,
    help="Prospective destination; no directory is created.",
)
@click.option("--json", "as_json", is_flag=True, help="Emit structured JSON.")
def preflight_command(name, data_dir, as_json):
    """Inspect source terms, requirements and loader behavior without transfer."""
    from eyedatahub.acquisition import acquire_dataset

    try:
        dataset = _get_registry().get_dataset(name)
    except KeyError as exc:
        raise click.ClickException(str(exc)) from exc
    result = acquire_dataset(dataset, data_dir, dry_run=True)
    if as_json:
        click.echo(json.dumps(result.to_dict(), indent=2))
    else:
        _print_preflight(result.preflight)
    if result.exit_code:
        raise SystemExit(result.exit_code)


@main.command()
@click.argument("resource", required=False)
@click.option(
    "--datasets",
    "datasets_option",
    "-d",
    default=None,
    help='Backward-compatible comma-separated record names, modality, or "all".',
)
@click.option(
    "--data-dir",
    default="~/.eyedatahub/data",
    show_default=True,
    help="Directory to store downloaded datasets",
)
@click.option(
    "--force",
    is_flag=True,
    default=False,
    help="Re-download even if already present",
)
@click.option(
    "--dry-run",
    is_flag=True,
    default=False,
    help="Display the complete preflight and start no transfer.",
)
@click.option(
    "--no-checksums",
    is_flag=True,
    default=False,
    help="Do not calculate local SHA-256 values in the provenance manifest.",
)
@click.option(
    "--json",
    "as_json",
    is_flag=True,
    default=False,
    help="Emit a valid structured result on success or failure.",
)
@click.option(
    "--license-type",
    "-l",
    default=None,
    help=(
        "Only download datasets matching this license. "
        "Families: cc0, cc-by, cc-by-sa, mit, apache, odc-by, cc-by-nc, cc-by-nc-sa, "
        "cc-by-nc-nd, research-only. "
        "Groups: standard-no-nc, non-commercial."
    ),
)
def download(
    resource,
    datasets_option,
    data_dir,
    force,
    dry_run,
    no_checksums,
    as_json,
    license_type,
):
    """Explicitly acquire supported resources from their official sources."""
    from eyedatahub.acquisition import acquire_dataset

    if resource and datasets_option:
        raise click.UsageError("Use either the RESOURCE argument or --datasets, not both.")
    selector = resource or datasets_option
    if not selector:
        raise click.UsageError(
            "Specify one record (for example `eyehub download fives --dry-run`) "
            "or use --datasets explicitly."
        )

    target_datasets = _resolve_datasets(selector)
    target_datasets = _filter_by_license(target_datasets, license_type)
    if not target_datasets:
        if as_json:
            click.echo(json.dumps({"status": "no_match", "exit_code": 2, "results": []}, indent=2))
            raise SystemExit(2)
        raise click.ClickException("No catalog records matched the request.")

    results = []
    for dataset in sorted(target_datasets, key=lambda item: item.info.name):
        if as_json:
            capture_out = StringIO()
            capture_err = StringIO()
            with redirect_stdout(capture_out), redirect_stderr(capture_err):
                result = acquire_dataset(
                    dataset,
                    data_dir,
                    dry_run=dry_run,
                    force=force,
                    checksums=not no_checksums,
                )
        else:
            result = acquire_dataset(
                dataset,
                data_dir,
                dry_run=dry_run,
                force=force,
                checksums=not no_checksums,
            )
        results.append(result)

    exit_code = max(result.exit_code for result in results)
    if as_json:
        payload = {
            "command": "download",
            "dry_run": dry_run,
            "transfer_requested": not dry_run,
            "exit_code": exit_code,
            "results": [result.to_dict() for result in results],
        }
        click.echo(json.dumps(payload, indent=2))
    else:
        for result in results:
            console.print(Panel(f"[bold]{result.record_id}[/]: {result.message}", title=result.status))
            _print_preflight(result.preflight)
            if result.manifest_path:
                console.print(f"[green]Provenance manifest:[/] {result.manifest_path}")
        if dry_run:
            console.print("[bold]Dry run complete: no transfer was started.[/]")
    if exit_code:
        raise SystemExit(exit_code)



if __name__ == "__main__":
    main()
