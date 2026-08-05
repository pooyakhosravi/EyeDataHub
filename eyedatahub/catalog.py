"""Read-only catalog serialization, search and citation helpers."""
from __future__ import annotations

import re
from dataclasses import asdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence

from eyedatahub import __version__
from eyedatahub.core.dataset import license_matches_filter
from eyedatahub.core.metadata import normalize_modality_label, normalize_unknown
from eyedatahub.core.resource_identity import identity_fields_for


def info_to_record(info: Any) -> Dict[str, Any]:
    """Return the full stable machine-readable representation of a record."""
    payload = normalize_unknown(asdict(info))
    payload.update(
        {
            "record_id": info.name,
            "canonical_name": info.full_name,
            "primary_category": info.primary_category,
            "normalized_source_term_category": info.license_family,
            # Backward-compatible aliases retained for existing clients.
            "modality": info.modality,
            "license": info.license,
            "license_family": info.license_family,
            "download_type": info.download_type,
            "download_url": info.download_url,
            **identity_fields_for(info.name),
        }
    )
    return payload


def dataset_to_record(dataset: Any, data_dir: Optional[str | Path] = None) -> Dict[str, Any]:
    payload = info_to_record(dataset.info)
    if data_dir is not None:
        payload["downloaded"] = dataset.is_downloaded(Path(data_dir).expanduser())
    return payload


def search_datasets(
    datasets: Iterable[Any],
    *,
    query: Optional[str] = None,
    modalities: Sequence[str] = (),
    tasks: Sequence[str] = (),
    access_friction: Sequence[str] = (),
    source_terms: Sequence[str] = (),
    acquisition_support: Sequence[str] = (),
    availability_status: Sequence[str] = (),
) -> List[Any]:
    """Filter catalog records deterministically without initiating transfer."""
    canonical_modalities = {normalize_modality_label(value) for value in modalities if value}
    task_values = {value.strip().lower() for value in tasks if value}
    access_values = {value.strip().lower() for value in access_friction if value}
    automation_values = {value.strip().lower() for value in acquisition_support if value}
    availability_values = {value.strip().lower() for value in availability_status if value}
    term_values = {value.strip().lower() for value in source_terms if value}
    needle = (query or "").strip().casefold()

    results: List[Any] = []
    for dataset in datasets:
        info = dataset.info
        if canonical_modalities and not canonical_modalities.intersection(info.modalities):
            continue
        if task_values and not task_values.issubset({task.lower() for task in info.tasks}):
            continue
        if access_values and info.access_friction.lower() not in access_values:
            continue
        if automation_values and info.acquisition_support.lower() not in automation_values:
            continue
        if availability_values and info.availability_status.lower() not in availability_values:
            continue
        if term_values and not any(
            license_matches_filter(info.source_terms or info.license, value)
            for value in term_values
        ):
            continue
        if needle:
            haystack = " ".join(
                [
                    info.name,
                    info.full_name,
                    info.description,
                    " ".join(info.tags),
                    " ".join(info.tasks),
                    " ".join(info.modalities),
                ]
            ).casefold()
            if needle not in haystack:
                continue
        results.append(dataset)
    return sorted(results, key=lambda item: item.info.name)


def _bibtex_key(info: Any, suffix: str = "") -> str:
    base = re.sub(r"[^a-z0-9]+", "_", info.name.lower()).strip("_")
    return f"{base}{suffix}"


def citation_payload(info: Any) -> Dict[str, Any]:
    """Keep dataset, associated article and software citations distinct."""
    dataset_url = (
        f"https://doi.org/{info.dataset_doi}" if info.dataset_doi else info.canonical_resolver_url
    )
    dataset_plain = info.full_name
    if info.dataset_doi:
        dataset_plain += f". Dataset DOI: https://doi.org/{info.dataset_doi}."
    elif dataset_url:
        dataset_plain += f". Official source: {dataset_url}."

    dataset_bibtex = [
        f"@dataset{{{_bibtex_key(info)},",
        f"  title = {{{info.full_name}}},",
    ]
    if info.dataset_doi:
        dataset_bibtex.append(f"  doi = {{{info.dataset_doi}}},")
    if dataset_url:
        dataset_bibtex.append(f"  url = {{{dataset_url}}},")
    dataset_bibtex.append("}")

    article_plain = info.citation or None
    article_bibtex: Optional[str] = None
    if article_plain or info.associated_publication_doi:
        article_bibtex_lines = [
            f"@article{{{_bibtex_key(info, '_article')},",
            f"  title = {{{info.full_name} associated publication}},",
        ]
        if info.associated_publication_doi:
            article_bibtex_lines.append(
                f"  doi = {{{info.associated_publication_doi}}},"
            )
        if article_plain:
            article_bibtex_lines.append(f"  note = {{{article_plain.rstrip('.')}}},")
        article_bibtex_lines.append("}")
        article_bibtex = "\n".join(article_bibtex_lines)

    software_plain = (
        f"Khosravi P, Riazi Esfehani P, Browne AW, Xie X. "
        f"EyeDataHub software, version {__version__}. "
        "https://github.com/pooyakhosravi/EyeDataHub"
    )
    software_bibtex = "\n".join(
        [
            "@software{eyedatahub,",
            "  title = {EyeDataHub},",
            "  author = {Khosravi, Pooya and Riazi Esfehani, Parsa and Browne, Andrew W. and Xie, Xiaohui},",
            f"  version = {{{__version__}}},",
            "  url = {https://github.com/pooyakhosravi/EyeDataHub},",
            "}",
        ]
    )

    return {
        "record_id": info.name,
        "dataset": {
            "plain": dataset_plain,
            "bibtex": "\n".join(dataset_bibtex),
            "doi": info.dataset_doi,
            "accession": info.dataset_accession,
            "url": dataset_url,
        },
        "associated_article": {
            "plain": article_plain,
            "bibtex": article_bibtex,
            "doi": info.associated_publication_doi,
        },
        "software": {
            "plain": software_plain,
            "bibtex": software_bibtex,
            "doi": info.software_doi,
            "version": __version__,
        },
    }
