"""Generate one Docusaurus-compatible Markdown page per catalog record.

Reads the live REGISTRY (`eyedatahub.datasets.registry.REGISTRY`) and writes
`docs/datasets/<name>.md` for every registered dataset.

Each page contains:
  - Docusaurus frontmatter (id, title, sidebar_label, tags, description)
  - At-a-glance summary table (modality, tasks, counts, terms, access, support)
  - Overview + full description
  - Read-only preflight plus an explicit download command
  - Loader status and a Python example when a standard loader exists
  - Citation (BibTeX + APA in Tabs)
  - Source-term evidence, scope, and legal limitation
  - Related datasets (same modality)
  - Source URLs + upstream page + paper DOI

Run:
    python -m hub.docs.generate_dataset_pages

Or override output dir:
    python -m hub.docs.generate_dataset_pages --out ./website/docs/datasets/
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import urlparse

from eyedatahub.agent.planner import loader_status
from eyedatahub.core.dataset import EyeDataHubDataset
from eyedatahub.core.relationships import RELATIONSHIP_EVIDENCE
from eyedatahub.core.resource_identity import (
    RESOURCE_ROLE_DEFINITIONS,
    dataset_family_for,
    resource_role_for,
)
from eyedatahub.datasets.registry import REGISTRY


# ---------------------------------------------------------------------------
# Formatting helpers
# ---------------------------------------------------------------------------


LICENSE_SCREENING_LABEL: dict[str, str] = {
    "cc0": "Standard label without an explicit NC clause; not a permission finding",
    "cc-by": "Standard label without an explicit NC clause; not a permission finding",
    "cc-by-sa": "Standard label without an explicit NC clause; not a permission finding",
    "mit": "Standard label without an explicit NC clause; verify that it applies to data",
    "apache": "Standard label without an explicit NC clause; verify that it applies to data",
    "odc-by": "Standard label without an explicit NC clause; not a permission finding",
    "cc-by-nc": "Explicit noncommercial clause recorded; check source",
    "cc-by-nc-sa": "Explicit noncommercial clause recorded; check source",
    "cc-by-nc-nd": "Explicit noncommercial clause recorded; check source",
    "research-only": "Research or challenge restriction recorded; check source",
    "unknown": "Unknown or unclear; do not assume permission",
}


BACKEND_LABEL: dict[str, str] = {
    "direct": "Direct HTTP",
    "kaggle": "Kaggle",
    "figshare": "Figshare",
    "zenodo": "Zenodo",
    "mendeley": "Mendeley Data",
    "dryad": "Dryad",
    "dataverse": "Dataverse",
    "gdrive": "Google Drive",
    "huggingface": "HuggingFace Hub",
    "physionet": "PhysioNet",
    "synapse": "Synapse",
    "github": "GitHub",
    "manual": "Manual (upstream-gated)",
}


def sanitize_yaml(text: str) -> str:
    """Escape colons and double-quotes for YAML frontmatter values."""
    return text.replace('"', "'").replace("\n", " ").strip()


def mdx_escape(text: object) -> str:
    """Escape text that could be parsed as MDX/JSX in generated prose."""
    return (
        str(text)
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace("{", "&#123;")
        .replace("}", "&#125;")
    )


def mdx_table_cell(text: object) -> str:
    """Escape generated Markdown table cells."""
    return mdx_escape(text).replace("\n", " ").replace("|", "\\|")


def source_link(url: str) -> str:
    """Return a compact Markdown source link for generated docs."""
    escaped_url = mdx_escape(url)
    parsed = urlparse(url)
    host = parsed.netloc.lower().removeprefix("www.")
    path = parsed.path.strip("/")
    if host == "doi.org":
        label = escaped_url
    elif host == "figshare.com" and path.startswith("s/"):
        label = "Figshare private-share page"
    elif host:
        label = f"{host}/{path.split('/')[0]}" if path else host
    else:
        label = "Source page"
    return f"[{mdx_escape(label)}]({escaped_url})"


def format_quantity(count: int | None, unit: str) -> str:
    """Format one count without hiding its scientific unit."""
    if count is None:
        return "Not reported"
    label = (
        unit.replace("_", " ") if unit and unit != "unknown" else "unit not resolved"
    )
    return f"{count:,} {label}"


def documented_relationships(dataset: EyeDataHubDataset) -> list[dict[str, str]]:
    """Return outgoing and incoming curated catalog relationships."""
    record_id = dataset.info.name
    relationships: list[dict[str, str]] = []
    symmetric_types = {"mirror_of", "same_or_overlapping_cohort_as"}
    symmetric_seen: set[tuple[str, str]] = set()
    for edge in RELATIONSHIP_EVIDENCE:
        if edge.relationship_type in symmetric_types and record_id in {
            edge.source_record_id,
            edge.target_record_id,
        }:
            other = (
                edge.target_record_id
                if edge.source_record_id == record_id
                else edge.source_record_id
            )
            key = (edge.relationship_type, other)
            if key in symmetric_seen:
                continue
            symmetric_seen.add(key)
            relationships.append(
                {
                    "direction": "symmetric",
                    "type": edge.relationship_type,
                    "record_id": other,
                    "evidence_url": edge.evidence_url,
                    "evidence_summary": edge.evidence_summary,
                }
            )
            continue
        if edge.source_record_id == record_id:
            relationships.append(
                {
                    "direction": "outgoing",
                    "type": edge.relationship_type,
                    "record_id": edge.target_record_id,
                    "evidence_url": edge.evidence_url,
                    "evidence_summary": edge.evidence_summary,
                }
            )
        elif edge.target_record_id == record_id:
            relationships.append(
                {
                    "direction": "incoming",
                    "type": edge.relationship_type,
                    "record_id": edge.source_record_id,
                    "evidence_url": edge.evidence_url,
                    "evidence_summary": edge.evidence_summary,
                }
            )
    return sorted(
        relationships,
        key=lambda value: (value["direction"], value["type"], value["record_id"]),
    )


def reported_quantities_table(dataset: EyeDataHubDataset) -> str:
    """Render all reviewed quantities without summing unlike units."""
    entries = dataset.info.reported_quantities or []
    if not entries:
        return (
            "No reproducible primary item count was exposed for the cataloged "
            "source version."
        )
    lines = [
        "| Role | Count | Unit | Scope | Basis | Evidence |",
        "| --- | ---: | --- | --- | --- | --- |",
    ]
    for entry in entries:
        evidence = (
            source_link(entry["evidence_url"])
            if entry.get("evidence_url")
            else "Not reported"
        )
        scope = mdx_table_cell(entry["scope"])
        if entry.get("notes"):
            scope += f" {mdx_table_cell(entry['notes'])}"
        lines.append(
            f"| {'Primary' if entry['primary'] else 'Additional'} | "
            f"{entry['count']:,} | `{entry['unit']}` | {scope} | "
            f"`{entry['evidence_basis']}` | {evidence} |"
        )
    return "\n".join(lines)


def build_bibtex(dataset: EyeDataHubDataset) -> str:
    """Build a BibTeX entry from the dataset's citation string."""
    info = dataset.info
    key = re.sub(r"[^a-z0-9]+", "_", info.name.lower()).strip("_")
    citation = (info.citation or "").strip().rstrip(".") or f"{info.full_name}"
    # Try to extract year
    m = re.search(r"\b(19|20|21)\d{2}\b", citation)
    year = m.group(0) if m else ""
    return (
        "@misc{" + key + ",\n"
        f"  title  = {{ {info.full_name} }},\n"
        f"  note   = {{ {citation} }},\n"
        + (f"  year   = {{ {year} }},\n" if year else "")
        + (f"  url    = {{ {info.download_url} }},\n" if info.download_url else "")
        + "}"
    )


def build_apa(dataset: EyeDataHubDataset) -> str:
    """Best-effort APA-style citation string."""
    info = dataset.info
    citation = (info.citation or info.full_name).strip()
    return citation


def backend_download_snippet(dataset: EyeDataHubDataset) -> tuple[str, str]:
    """Return side-effect-free preflight snippets for one catalog record."""
    info = dataset.info
    name = info.name
    shell = (
        f"# Read-only preflight\n"
        f"eyehub download {name} --data-dir ./data --dry-run --json\n\n"
        f"# Download, only when preflight reports supported behavior\n"
        f"eyehub download {name} --data-dir ./data"
    )

    py_lines = [
        "from eyedatahub.acquisition import preflight_dataset",
        "from eyedatahub.datasets.registry import REGISTRY",
        "",
        f"ds = REGISTRY.get_dataset('{name}')",
        "print(preflight_dataset(ds, './data'))  # no download",
    ]
    py = "\n".join(py_lines)

    if info.access_friction in {
        "controlled_or_manual",
        "author_contact",
        "model_to_data_or_secure_environment",
    }:
        shell = (
            f"# This route requires upstream human action; no transfer starts.\n"
            f"eyehub download {name} --data-dir ./data --dry-run --json\n"
            f"# Follow the official instructions shown by preflight."
        )
        py = (
            "from eyedatahub.acquisition import preflight_dataset\n"
            "from eyedatahub.datasets.registry import REGISTRY\n"
            "\n"
            f"ds = REGISTRY.get_dataset('{name}')\n"
            "print(preflight_dataset(ds, './data'))  # returns manual_access_blocked"
        )
    return shell, py


def loader_snippet(dataset: EyeDataHubDataset) -> str:
    """Python snippet showing how to iterate samples once downloaded."""
    info = dataset.info
    split = "test" if "test" in (info.splits or []) else (info.splits or ["all"])[0]
    return (
        "from pathlib import Path\n"
        "from eyedatahub.datasets.registry import REGISTRY\n"
        "\n"
        "data_dir = Path('~/.eyedatahub/data').expanduser()\n"
        f"ds = REGISTRY.get_dataset('{info.name}')\n"
        f"samples = ds.load(data_dir, split='{split}')\n"
        "for s in samples[:5]:\n"
        "    print(s.sample_id, s.label, s.image_path)"
    )


def at_a_glance_table(dataset: EyeDataHubDataset) -> str:
    info = dataset.info
    resource_role = resource_role_for(info.name)
    dataset_family = dataset_family_for(info.name)
    tasks = ", ".join(info.tasks) if info.tasks else "Not reported"
    classes = ", ".join(info.classes) if info.classes else "Not reported"
    splits = ", ".join(info.splits) if info.splits else "Not reported"
    size = f"{info.size_gb} GB" if info.size_gb else "Not reported"
    samples = format_quantity(info.num_samples, info.item_count_unit)
    backend = BACKEND_LABEL.get(info.download_type, info.download_type)
    screening = LICENSE_SCREENING_LABEL.get(
        info.license_family, "Unknown; check source"
    )
    status = loader_status(dataset)
    loader_label = (
        "Standard loader included"
        if status == "implemented"
        else "Metadata and access only"
    )
    return (
        "| Field | Value |\n"
        "| --- | --- |\n"
        f"| **Short name** | `{info.name}` |\n"
        f"| **Full name** | {mdx_table_cell(info.full_name)} |\n"
        f"| **Primary category** | `{info.primary_category}` |\n"
        f"| **Resource role** | `{resource_role}` |\n"
        f"| **Dataset family** | `{dataset_family}` |\n"
        f"| **Contained modalities** | {mdx_table_cell(', '.join(info.modalities))} |\n"
        f"| **Tasks** | {mdx_table_cell(tasks)} |\n"
        f"| **Primary reported quantity** | {samples} |\n"
        f"| **Classes** | {info.num_classes if info.num_classes else 'Not reported'} ({mdx_table_cell(classes)}) |\n"
        f"| **Splits** | {mdx_table_cell(splits)} |\n"
        f"| **Size** | {size} |\n"
        f"| **Source-stated terms** | {mdx_table_cell(info.source_terms)} |\n"
        f"| **Normalized terms** | `{info.license_family}` |\n"
        f"| **Descriptive screening label** | {mdx_table_cell(screening)} |\n"
        f"| **Terms scope** | `{info.terms_scope}` |\n"
        f"| **Access friction** | `{info.access_friction}` |\n"
        f"| **Route backend** | {mdx_table_cell(backend)} |\n"
        f"| **Availability** | `{info.availability_status}` (checked {info.route_last_checked}) |\n"
        f"| **Acquisition support** | `{info.acquisition_support}` |\n"
        f"| **Legacy sample-loader status** | {loader_label} |\n"
    )


def related_datasets(
    current: EyeDataHubDataset,
    all_ds: list[EyeDataHubDataset],
    limit: int = 8,
    info_cache: dict[int, object] | None = None,
) -> list[EyeDataHubDataset]:
    """Return datasets sharing at least one contained modality."""
    current_info = (
        info_cache[id(current)] if info_cache is not None else current.info
    )
    current_modalities = set(current_info.modalities)
    peers = [
        d
        for d in all_ds
        if (
            info_cache[id(d)].name if info_cache is not None else d.info.name
        )
        != current_info.name
        and current_modalities.intersection(
            info_cache[id(d)].modalities if info_cache is not None else d.info.modalities
        )
    ]
    peers.sort(
        key=lambda d: (
            -len(
                current_modalities.intersection(
                    info_cache[id(d)].modalities
                    if info_cache is not None
                    else d.info.modalities
                )
            ),
            -(
                (info_cache[id(d)].num_samples if info_cache is not None else d.info.num_samples)
                or 0
            ),
            info_cache[id(d)].name if info_cache is not None else d.info.name,
        )
    )
    return peers[:limit]


def frontmatter(dataset: EyeDataHubDataset) -> str:
    info = dataset.info
    desc = sanitize_yaml(info.description or info.full_name)[:200]
    tags = (
        [info.primary_category]
        + list(info.modalities)
        + [info.license_family, info.download_type]
        + list(info.tasks or [])
    )
    relationships = documented_relationships(dataset)
    tags.append(f"resource-role-{resource_role_for(info.name).replace('_', '-')}")
    tags.append(f"dataset-family-{dataset_family_for(info.name).replace('_', '-')}")
    if relationships:
        tags.append("documented-relationship")
        tags.extend(f"relationship-{value['type']}" for value in relationships)
    if info.alternate_sources:
        tags.append("alternate-source")
        tags.extend(
            f"source-{value['platform'].strip().lower().replace(' ', '-')}"
            for value in info.alternate_sources
            if value.get("platform")
        )
        tags.extend(
            f"alternate-role-{value['role'].strip().lower().replace('_', '-')}"
            for value in info.alternate_sources
            if value.get("role")
        )
    tags = list(dict.fromkeys(tags))
    tag_list = ", ".join(f'"{t}"' for t in tags)
    return (
        "---\n"
        f"id: {info.name}\n"
        f'title: "{sanitize_yaml(info.full_name)}"\n'
        f"sidebar_label: {info.name}\n"
        f'description: "{desc}"\n'
        f"tags: [{tag_list}]\n"
        "---\n"
    )


# ---------------------------------------------------------------------------
# Page builder
# ---------------------------------------------------------------------------


def build_page(
    dataset: EyeDataHubDataset,
    all_ds: list[EyeDataHubDataset],
    *,
    info_cache: dict[int, object] | None = None,
    records_by_name: dict[str, EyeDataHubDataset] | None = None,
    family_members_by_id: dict[str, list[str]] | None = None,
) -> str:
    info = info_cache[id(dataset)] if info_cache is not None else dataset.info
    shell, py = backend_download_snippet(dataset)
    peers = related_datasets(dataset, all_ds, info_cache=info_cache)
    relationship_rows = documented_relationships(dataset)
    if records_by_name is None:
        records_by_name = {value.info.name: value for value in all_ds}
    family_id = dataset_family_for(info.name)
    if family_members_by_id is None:
        family_member_ids = [
            record_id
            for record_id in records_by_name
            if dataset_family_for(record_id) == family_id and record_id != info.name
        ]
    else:
        family_member_ids = [
            record_id
            for record_id in family_members_by_id.get(family_id, [])
            if record_id != info.name
        ]

    parts = [
        frontmatter(dataset),
        "",
        "import Tabs from '@theme/Tabs';",
        "import TabItem from '@theme/TabItem';",
        "",
        f"# {mdx_escape(info.full_name)}",
        "",
        mdx_escape(info.description or ""),
        "",
        "## At a glance",
        "",
        at_a_glance_table(dataset),
        "",
        "## Reported quantities",
        "",
        reported_quantities_table(dataset),
        "",
        (
            "Counts retain their source-reported units. Additional rows can "
            "describe components, paired items, or derivative copies and are not "
            "automatically added to the primary quantity."
        ),
        "",
    ]

    if info.notes:
        parts += [
            "## Notes",
            "",
            "> " + mdx_escape(info.notes).replace("\n", "\n> "),
            "",
        ]

    if family_member_ids:
        parts += [
            "## Dataset family",
            "",
            (
                f"This record belongs to `{family_id}`. Family links group "
                "documented collection/component records or exact task views; "
                "they do not imply independent cohorts."
            ),
            "",
        ]
        for member_id in sorted(family_member_ids):
            member = records_by_name[member_id]
            member_info = (
                info_cache[id(member)] if info_cache is not None else member.info
            )
            parts.append(
                f"- [{member_info.name}](./{member_info.name}.md): "
                f"{mdx_escape(member_info.full_name)} "
                f"(`{resource_role_for(member_info.name)}`)"
            )
        parts.append("")

    if relationship_rows:
        parts += [
            "## Documented relationships",
            "",
            (
                "These links record source-supported lineage or overlap, not merely "
                "similar modality tags."
            ),
            "",
        ]
        for relationship in relationship_rows:
            other = records_by_name[relationship["record_id"]]
            relation = relationship["type"].replace("_", " ")
            if relationship["direction"] == "outgoing":
                label = (
                    f"This record is `{relation}` "
                    f"[{other.info.name}](./{other.info.name}.md)"
                )
            elif relationship["direction"] == "incoming":
                label = (
                    f"[{other.info.name}](./{other.info.name}.md) is "
                    f"`{relation}` this record"
                )
            else:
                label = (
                    f"This record has a documented `{relation}` relationship with "
                    f"[{other.info.name}](./{other.info.name}.md)"
                )
            parts.append(
                f"- {label}: {mdx_escape(relationship['evidence_summary'])} "
                f"([evidence]({mdx_escape(relationship['evidence_url'])}))"
            )
        parts.append("")

    parts += [
        "## Access information and download",
        "",
        "<Tabs>",
        '  <TabItem value="cli" label="CLI" default>',
        "",
        "```bash",
        shell,
        "```",
        "",
        "  </TabItem>",
        '  <TabItem value="python" label="Python">',
        "",
        "```python",
        py,
        "```",
        "",
        "  </TabItem>",
        "</Tabs>",
        "",
    ]

    if info.download_url:
        parts += [
            f"**Upstream page:** {source_link(info.download_url)}",
            "",
        ]
    if info.alternate_sources:
        parts += [
            "## Other documented locations",
            "",
            (
                "These links identify alternate deposits, components, metadata "
                "records, mirrors, versions, or related derived materials. They "
                "do not create additional canonical catalog records."
            ),
            "",
        ]
        for source in info.alternate_sources:
            platform = mdx_escape(source.get("platform") or "Source")
            role = mdx_escape(
                (source.get("role") or "alternate_source").replace("_", " ")
            )
            identifier = mdx_escape(source.get("identifier") or "")
            version = mdx_escape(source.get("version") or "")
            label_details = ", ".join(
                value
                for value in (identifier, f"version {version}" if version else "")
                if value
            )
            label = f"{platform}: {role}"
            if label_details:
                label += f" ({label_details})"
            note = mdx_escape(source.get("notes") or "")
            suffix = f": {note}" if note else ""
            parts.append(
                f"- [{label}]({mdx_escape(source['url'])}){suffix}"
            )
        parts.append("")
    if info.terms_evidence_url:
        parts += [
            f"**Source-term evidence:** {source_link(info.terms_evidence_url)}",
            "",
        ]

    if loader_status(dataset) == "implemented":
        parts += [
            "## Loader example",
            "",
            "This entry includes a standard `DatasetSample` loader.",
            "",
            "```python",
            loader_snippet(dataset),
            "```",
            "",
        ]
    else:
        parts += [
            "## Loader status",
            "",
            (
                "This catalog record provides metadata and access instructions, "
                "but it does not yet include a standard `DatasetSample` loader. "
                "Inspect the source file structure or contribute a loader before "
                "using it in a training pipeline."
            ),
            "",
        ]

    parts += [
        "## Citation",
        "",
        "<Tabs>",
        '  <TabItem value="bibtex" label="BibTeX" default>',
        "",
        "```bibtex",
        build_bibtex(dataset),
        "```",
        "",
        "  </TabItem>",
        '  <TabItem value="apa" label="Plain text">',
        "",
        "```text",
        build_apa(dataset),
        "```",
        "",
        "  </TabItem>",
        "</Tabs>",
        "",
        "## Source-stated terms",
        "",
        f"- **Raw source string:** {mdx_escape(info.source_terms)}",
        f"- **Normalized category:** `{info.license_family}`",
        f"- **Apparent scope:** `{info.terms_scope}`",
        f"- **Descriptive screening label:** {LICENSE_SCREENING_LABEL.get(info.license_family, 'Unknown; check source')}",
        "",
        (
            "> :warning: Source-stated terms, scope, and normalized labels are "
            "curation metadata, not legal advice or a permission finding. Review "
            "the current official source before transfer or reuse."
        ),
        "",
    ]

    if peers:
        parts += [
            "## Similar resources by shared modality",
            "",
        ]
        for p in peers:
            parts += [
                f"- [{p.info.name}](./{p.info.name}.md): {mdx_escape(p.info.full_name)} "
                f"({format_quantity(p.info.num_samples, p.info.item_count_unit)}, "
                f"`{p.info.license_family}`)",
            ]
        parts.append("")

    return "\n".join(parts).rstrip() + "\n"


# ---------------------------------------------------------------------------
# Modality index pages
# ---------------------------------------------------------------------------


def build_modality_index(modality: str, datasets: list[EyeDataHubDataset]) -> str:
    """One landing page per contained-modality tag."""
    datasets = sorted(datasets, key=lambda d: -(d.info.num_samples or 0))
    total_gb = sum((d.info.size_gb or 0) for d in datasets)
    primary_quantity_count = sum(d.info.num_samples is not None for d in datasets)

    parts = [
        "---",
        f"id: {modality}-index",
        f'title: "{modality.replace("_", " ").title()} datasets"',
        f"sidebar_label: {modality}",
        f'description: "{len(datasets)} resources containing {modality} data in EyeDataHub."',
        "---",
        "",
        f"# {modality.replace('_', ' ').title()} datasets",
        "",
        (
            f"**{len(datasets)} datasets; {primary_quantity_count} with a primary "
            f"reported quantity; {total_gb:.1f} GB total** - this page indexes every EyeDataHub "
            f"resource tagged as containing `{modality}` data. A resource can "
            "appear on more than one modality page. Primary quantities retain "
            "their source-reported units and are not summed here."
        ),
        "",
        "| Name | Full name | Primary quantity | Size | License | Backend |",
        "| --- | --- | ---:| ---:| --- | --- |",
    ]
    for d in datasets:
        i = d.info
        n = format_quantity(i.num_samples, i.item_count_unit)
        size = f"{i.size_gb:.1f} GB" if i.size_gb else "Not reported"
        parts.append(
            f"| [`{i.name}`](./{i.name}.md) | {mdx_table_cell(i.full_name)} | {n} | {size} | "
            f"`{i.license_family}` | {BACKEND_LABEL.get(i.download_type, i.download_type)} |"
        )
    parts.append("")
    return "\n".join(parts).rstrip() + "\n"


# ---------------------------------------------------------------------------
# Datasets landing page
# ---------------------------------------------------------------------------


def build_datasets_root(all_ds: list[EyeDataHubDataset]) -> str:
    """Top-level datasets landing page: totals + link to each modality."""
    from collections import Counter

    total_gb = sum((d.info.size_gb or 0) for d in all_ds)
    by_mod = Counter(modality for d in all_ds for modality in d.info.modalities)
    by_primary = Counter(d.info.primary_category for d in all_ds)
    by_fam = Counter(d.info.license_family for d in all_ds)
    by_backend = Counter(d.info.download_type for d in all_ds)
    by_quantity_unit = Counter(
        d.info.item_count_unit or "unknown"
        for d in all_ds
        if d.info.num_samples is not None
    )

    parts = [
        "---",
        "id: datasets-index",
        'title: "All datasets"',
        "sidebar_label: All datasets",
        "slug: /datasets",
        "---",
        "",
        "# All datasets in EyeDataHub",
        "",
        (
            f"**{len(all_ds)} catalog records; "
            f"{by_quantity_unit.total()} with a primary reported quantity; "
            f"{total_gb:.1f} GB reported; "
            f"{by_backend.total() - by_backend.get('manual', 0)} nonmanual access routes**"
        ),
        "",
        "Each resource has one primary category for navigation and one or more "
        "contained-modality tags. Counts below overlap because a resource with "
        "fundus photographs and OCT is included under both modalities. Primary "
        "quantities retain their source-reported units on each resource page; "
        "they are not summed across the catalog.",
        "",
        "## By contained modality",
        "",
        "| Modality | Count | Landing |",
        "| --- | ---:| --- |",
    ]
    for mod, count in sorted(by_mod.items(), key=lambda kv: -kv[1]):
        parts.append(f"| `{mod}` | {count} | [{mod}](./{mod}-index.md) |")

    parts += [
        "",
        "## By primary category",
        "",
        "| Primary category | Count |",
        "| --- | ---:|",
    ]
    for category, count in sorted(by_primary.items(), key=lambda kv: -kv[1]):
        parts.append(f"| `{category}` | {count} |")

    parts += [
        "",
        "## By license family",
        "",
        "| Family | Count |",
        "| --- | ---:|",
    ]
    for fam, count in sorted(by_fam.items(), key=lambda kv: -kv[1]):
        parts.append(f"| `{fam}` | {count} |")

    parts += [
        "",
        "## By download backend",
        "",
        "| Backend | Count |",
        "| --- | ---:|",
    ]
    for be, count in sorted(by_backend.items(), key=lambda kv: -kv[1]):
        parts.append(f"| `{be}` | {count} |")

    parts += [
        "",
        "## Primary reported quantity units",
        "",
        "| Unit | Records reporting this primary quantity |",
        "| --- | ---:|",
    ]
    for unit, count in sorted(by_quantity_unit.items(), key=lambda kv: (-kv[1], kv[0])):
        parts.append(f"| `{unit}` | {count} |")

    parts.append("")
    return "\n".join(parts).rstrip() + "\n"


# ---------------------------------------------------------------------------
# Sidebars manifest (Docusaurus sidebars.js)
# ---------------------------------------------------------------------------


def build_sidebars_js(
    by_primary_category: dict[str, list[EyeDataHubDataset]],
    modality_names: list[str],
) -> str:
    """Emit a JS file exporting a Docusaurus sidebar structure."""
    lines = [
        "// Auto-generated by hub/docs/generate_dataset_pages.py",
        "// Do not edit by hand; run the generator again to refresh.",
        "",
        "module.exports = {",
        "  datasetsSidebar: [",
        "    'intro',",
        "    {",
        "      type: 'category',",
        "      label: 'Guides',",
        "      collapsed: false,",
        "      items: [",
        "        'guides/install',",
        "        'guides/cli',",
        "        'guides/python',",
        "        'guides/agentic',",
        "        'guides/dataset-exploration',",
        "      ],",
        "    },",
        "    'datasets/datasets-index',",
        "    'url-audit',",
        "    {",
        "      type: 'category',",
        "      label: 'Browse by contained modality',",
        "      collapsed: true,",
        "      items: [",
    ]
    for mod in modality_names:
        lines.append(f"        'datasets/{mod}-index',")
    lines += [
        "      ],",
        "    },",
        "    {",
        "      type: 'category',",
        "      label: 'Datasets by primary category',",
        "      collapsed: false,",
        "      items: [",
    ]
    for category in sorted(by_primary_category.keys()):
        items = sorted(by_primary_category[category], key=lambda d: d.info.name)
        lines.append("        {")
        lines.append("          type: 'category',")
        lines.append(f"          label: '{category.replace('_', ' ').title()}',")
        lines.append("          collapsed: true,")
        lines.append("          items: [")
        for d in items:
            lines.append(f"            'datasets/{d.info.name}',")
        lines.append("          ],")
        lines.append("        },")
    lines += [
        "      ],",
        "    },",
        "  ],",
        "};",
    ]
    return "\n".join(lines) + "\n"


def build_static_dataset_index(all_ds: list[EyeDataHubDataset]) -> dict:
    """Return dashboard-friendly dataset and summary metadata."""
    records_by_name = {dataset.info.name: dataset for dataset in all_ds}
    rows = []
    for d in sorted(all_ds, key=lambda ds: ds.info.name):
        i = d.info
        relationships = []
        for relationship in documented_relationships(d):
            related = records_by_name[relationship["record_id"]].info
            relationships.append(
                {
                    "direction": relationship["direction"],
                    "relationship_type": relationship["type"],
                    "target_name": related.name,
                    "target_full_name": related.full_name,
                    "target_doc_path": f"/datasets/{related.name}",
                    "evidence_url": relationship["evidence_url"],
                    "evidence_summary": relationship["evidence_summary"],
                }
            )
        rows.append(
            {
                "name": i.name,
                "full_name": i.full_name,
                "description": i.description,
                "modality": i.modality,
                "primary_category": i.primary_category,
                "modalities": list(i.modalities),
                "tasks": list(i.tasks or []),
                "samples": i.num_samples,
                "item_count_unit": i.item_count_unit,
                "reported_quantities": list(i.reported_quantities or []),
                "alternate_sources": list(i.alternate_sources or []),
                "relationships": relationships,
                "resource_role": resource_role_for(i.name),
                "resource_role_definition": RESOURCE_ROLE_DEFINITIONS[
                    resource_role_for(i.name)
                ],
                "dataset_family_id": dataset_family_for(i.name),
                "size_gb": i.size_gb,
                "license": i.license,
                "license_family": i.license_family,
                "source_terms": i.source_terms,
                "terms_scope": i.terms_scope,
                "terms_evidence_url": i.terms_evidence_url,
                "download_type": i.download_type,
                "download_url": i.download_url,
                "access_friction": i.access_friction,
                "availability_status": i.availability_status,
                "route_last_checked": i.route_last_checked,
                "acquisition_support": i.acquisition_support,
                "loader_status": loader_status(d),
                "doc_path": f"/datasets/{i.name}",
                "citation": i.citation,
                "notes": i.notes,
            }
        )

    by_primary_category = Counter(row["primary_category"] for row in rows)
    by_modality = Counter(modality for row in rows for modality in row["modalities"])
    by_access = Counter(row["access_friction"] for row in rows)
    by_acquisition = Counter(row["acquisition_support"] for row in rows)
    by_license = Counter(row["license_family"] for row in rows)
    by_backend = Counter(row["download_type"] for row in rows)
    by_relationship_type = Counter(
        relationship.relationship_type for relationship in RELATIONSHIP_EVIDENCE
    )
    by_resource_role = Counter(row["resource_role"] for row in rows)
    total_gb = sum(row["size_gb"] or 0 for row in rows)
    nonmanual_routes = sum(1 for row in rows if row["download_type"] != "manual")
    loaders_implemented = sum(
        1 for row in rows if row["loader_status"] == "implemented"
    )
    standard_no_nc = {
        "cc0",
        "cc-by",
        "cc-by-sa",
        "mit",
        "apache",
        "odc-by",
    }

    return {
        "generated_by": "hub.docs.generate_dataset_pages",
        "total": len(rows),
        "summary": {
            "datasets": len(rows),
            "dataset_families": len(
                {row["dataset_family_id"] for row in rows}
            ),
            "primary_quantities_reported": sum(
                1 for row in rows if row["samples"] is not None
            ),
            "reported_quantity_entries": sum(
                len(row["reported_quantities"]) for row in rows
            ),
            "size_gb": round(total_gb, 1),
            "nonmanual_routes": nonmanual_routes,
            "loaders_implemented": loaders_implemented,
            "commercial_ok": sum(
                1 for row in rows if row["license_family"] in standard_no_nc
            ),
            "modalities": len(by_modality),
            "primary_categories": len(by_primary_category),
            "anonymous_routes": by_access["anonymous_direct"],
            "authenticated_or_clickthrough_routes": (
                by_access["self_service_authenticated"]
                + by_access["self_service_clickthrough"]
            ),
            "controlled_routes": by_access["controlled_or_manual"],
            "author_contact_routes": by_access["author_contact"],
            "transfer_tested_routes": (
                by_acquisition["end_to_end_tested"]
                + by_acquisition["transfer_tested_partial"]
            ),
            "text_or_qa": sum(
                1
                for row in rows
                if row["modality"] == "text"
                or any("question" in t or "report" in t for t in row["tasks"])
            ),
            "documented_relationship_edges": len(RELATIONSHIP_EVIDENCE),
            "datasets_with_documented_relationships": sum(
                1 for row in rows if row["relationships"]
            ),
            "relationship_types": len(by_relationship_type),
            "annotation_layers": by_resource_role["annotation_layer"],
            "derivative_datasets": by_resource_role["derivative_dataset"],
            "component_datasets": by_resource_role["component_dataset"],
            "collections": by_resource_role["collection"],
        },
        "facets": {
            "modality": dict(sorted(by_modality.items())),
            "license_family": dict(sorted(by_license.items())),
            "download_type": dict(sorted(by_backend.items())),
            "relationship_type": dict(sorted(by_relationship_type.items())),
            "resource_role": dict(sorted(by_resource_role.items())),
        },
        "datasets": rows,
    }


# ---------------------------------------------------------------------------
# Entrypoint
# ---------------------------------------------------------------------------


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", default="website/docs", help="Docusaurus docs root")
    args = ap.parse_args()

    out_root = Path(args.out)
    datasets_dir = out_root / "datasets"
    datasets_dir.mkdir(parents=True, exist_ok=True)

    all_ds = REGISTRY.list_datasets()
    info_cache = {id(dataset): dataset.info for dataset in all_ds}
    records_by_name = {
        info_cache[id(dataset)].name: dataset for dataset in all_ds
    }
    family_members_by_id: dict[str, list[str]] = defaultdict(list)
    for record_id in records_by_name:
        family_members_by_id[dataset_family_for(record_id)].append(record_id)
    by_primary_category: dict[str, list[EyeDataHubDataset]] = defaultdict(list)
    by_modality: dict[str, list[EyeDataHubDataset]] = defaultdict(list)
    for d in all_ds:
        by_primary_category[d.info.primary_category].append(d)
        for modality in d.info.modalities:
            by_modality[modality].append(d)

    expected_stems = {
        *(d.info.name for d in all_ds),
        *(f"{mod}-index" for mod in by_modality),
        "index",
    }
    removed_stale = 0
    for page_path in datasets_dir.glob("*.md"):
        if page_path.stem not in expected_stems:
            page_path.unlink()
            removed_stale += 1

    # Per-dataset pages
    for d in all_ds:
        page = build_page(
            d,
            all_ds,
            info_cache=info_cache,
            records_by_name=records_by_name,
            family_members_by_id=family_members_by_id,
        )
        (datasets_dir / f"{d.info.name}.md").write_text(page, encoding="utf-8")

    # Modality index pages
    for mod, ds_list in by_modality.items():
        page = build_modality_index(mod, ds_list)
        (datasets_dir / f"{mod}-index.md").write_text(page, encoding="utf-8")

    # Datasets landing
    (datasets_dir / "index.md").write_text(
        build_datasets_root(all_ds), encoding="utf-8"
    )

    # Sidebars.js next to docs root
    sidebars = build_sidebars_js(
        by_primary_category,
        sorted(by_modality),
    )
    sidebars_path = out_root.parent / "sidebars.js"
    sidebars_path.write_text(sidebars, encoding="utf-8")

    # Static JSON consumed by the Docusaurus dashboard/explorer.
    static_dir = out_root.parent / "static"
    static_dir.mkdir(parents=True, exist_ok=True)
    dataset_json_path = static_dir / "datasets.json"
    dataset_json_path.write_text(
        json.dumps(build_static_dataset_index(all_ds), indent=2),
        encoding="utf-8",
    )

    # Publish the latest dated source-link audit with the generated docs.
    repo_root = Path(__file__).resolve().parents[2]
    audit_json = repo_root / "hub" / "audit" / "url_report.json"
    audit_markdown = repo_root / "hub" / "audit" / "url_report.md"
    if audit_json.is_file() and audit_markdown.is_file():
        (static_dir / "url_report.json").write_bytes(audit_json.read_bytes())
        frontmatter = (
            "---\n"
            "id: url-audit\n"
            'title: "URL audit"\n'
            "sidebar_label: URL audit\n"
            'description: "Latest EyeDataHub source-link audit generated by GitHub Actions."\n'
            "---\n\n"
        )
        (out_root / "url-audit.md").write_text(
            frontmatter + audit_markdown.read_text(encoding="utf-8"),
            encoding="utf-8",
        )

    print(f"Wrote {len(all_ds)} dataset pages + {len(by_modality)} modality indexes")
    print(f"Removed {removed_stale} stale dataset pages")
    print(f"Root: {datasets_dir}")
    print(f"Sidebars: {sidebars_path}")
    print(f"Dashboard data: {dataset_json_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
