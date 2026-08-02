"""Search the official Dryad API for ophthalmology data-resource candidates.

The output is a public, credential-free discovery log. Authentication values
are read from the local environment and are never serialized.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import time
from collections import defaultdict
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urljoin

import requests

from eyedatahub.datasets.registry import REGISTRY
from eyedatahub.utils.credentials import load_credentials


API_ROOT = "https://datadryad.org"
SEARCH_ENDPOINT = f"{API_ROOT}/api/v2/search"
TOKEN_ENDPOINT = f"{API_ROOT}/oauth/token"

DEFAULT_QUERIES = (
    "ophthalmology",
    "ophthalmic",
    "retina",
    "retinal",
    "fundus",
    '"optical coherence tomography"',
    "glaucoma",
    "cornea",
    "corneal",
    '"visual field"',
    "perimetry",
    "cataract",
    '"diabetic retinopathy"',
    "macular",
    "uveitis",
    "iris",
    "ocular",
    "orbit",
    '"thyroid eye"',
    '"retinopathy of prematurity"',
    "angiography",
    "OCTA",
    '"slit lamp"',
    '"external eye"',
    '"anterior segment"',
    '"retinal image"',
)


def _normalized_doi(value: str | None) -> str:
    text = (value or "").strip().lower()
    for prefix in ("https://doi.org/", "http://doi.org/", "doi:"):
        if text.startswith(prefix):
            text = text[len(prefix) :]
    return text.rstrip("/.")


def _get_token(session: requests.Session) -> tuple[str, str]:
    load_credentials()
    token = os.environ.get("DRYAD_TOKEN", "").strip()
    if token:
        return token, "DRYAD_TOKEN"

    client_id = os.environ.get("DRYAD_CLIENT_ID", "").strip()
    client_secret = os.environ.get("DRYAD_SECRET", "").strip()
    if not client_id or not client_secret:
        raise RuntimeError(
            "Set DRYAD_TOKEN or both DRYAD_CLIENT_ID and DRYAD_SECRET in the local environment."
        )
    response = session.post(
        TOKEN_ENDPOINT,
        data={
            "client_id": client_id,
            "client_secret": client_secret,
            "grant_type": "client_credentials",
        },
        timeout=30,
    )
    response.raise_for_status()
    token = str(response.json().get("access_token") or "").strip()
    if not token:
        raise RuntimeError("Dryad returned no access token.")
    return token, "client_credentials"


def _get_json(
    session: requests.Session,
    url: str,
    *,
    headers: dict[str, str],
    params: dict[str, Any] | None = None,
) -> dict[str, Any]:
    for attempt in range(4):
        response = session.get(url, headers=headers, params=params, timeout=60)
        if response.status_code != 429 and response.status_code < 500:
            response.raise_for_status()
            return response.json()
        if attempt == 3:
            response.raise_for_status()
        time.sleep(2**attempt)
    raise AssertionError("unreachable")


def _public_candidate(item: dict[str, Any]) -> dict[str, Any]:
    doi = _normalized_doi(item.get("identifier"))
    authors = []
    for author in item.get("authors") or []:
        authors.append(
            {
                "first_name": author.get("firstName"),
                "last_name": author.get("lastName"),
                "orcid": author.get("orcid"),
            }
        )
    related_works = []
    for work in item.get("relatedWorks") or []:
        related_works.append(
            {
                "relationship": work.get("relationship"),
                "identifier_type": work.get("identifierType"),
                "identifier": work.get("identifier"),
            }
        )
    return {
        "doi": doi,
        "official_source_url": f"https://doi.org/{doi}" if doi else None,
        "title": item.get("title"),
        "abstract": item.get("abstract"),
        "methods": item.get("methods"),
        "usage_notes": item.get("usageNotes"),
        "authors": authors,
        "publication_date": item.get("publicationDate"),
        "last_modification_date": item.get("lastModificationDate"),
        "license": item.get("license"),
        "storage_size_bytes": item.get("storageSize"),
        "version_number": item.get("versionNumber"),
        "version_status": item.get("versionStatus"),
        "visibility": item.get("visibility"),
        "related_works": related_works,
    }


def _catalog_doi_index() -> dict[str, list[str]]:
    index: dict[str, list[str]] = defaultdict(list)
    for dataset in REGISTRY.list_datasets():
        info = dataset.info
        values = (info.dataset_doi, info.download_url, info.canonical_resolver_url)
        for value in values:
            doi = _normalized_doi(value)
            if doi.startswith("10.") and info.name not in index[doi]:
                index[doi].append(info.name)
    return dict(index)


def search_dryad(queries: tuple[str, ...]) -> dict[str, Any]:
    session = requests.Session()
    token, authentication_source = _get_token(session)
    headers = {"Authorization": f"Bearer {token}"}
    test_response = session.get(
        f"{API_ROOT}/api/v2/test",
        headers=headers,
        timeout=30,
    )
    test_response.raise_for_status()

    candidates: dict[str, dict[str, Any]] = {}
    query_counts: dict[str, int] = {}
    for query in queries:
        url: str | None = SEARCH_ENDPOINT
        params: dict[str, Any] | None = {"q": query, "per_page": 100}
        returned = 0
        while url:
            payload = _get_json(session, url, headers=headers, params=params)
            params = None
            items = payload.get("_embedded", {}).get("stash:datasets", [])
            returned += len(items)
            for item in items:
                candidate = _public_candidate(item)
                doi = candidate["doi"]
                if not doi:
                    continue
                if doi not in candidates:
                    candidate["query_hits"] = []
                    candidates[doi] = candidate
                candidates[doi]["query_hits"].append(query)
            next_href = payload.get("_links", {}).get("next", {}).get("href")
            url = urljoin(API_ROOT, next_href) if next_href else None
        query_counts[query] = returned

    catalog_index = _catalog_doi_index()
    rows = []
    for doi in sorted(candidates):
        candidate = candidates[doi]
        candidate["query_hits"] = sorted(set(candidate["query_hits"]))
        candidate["already_cataloged_as"] = sorted(catalog_index.get(doi, []))
        rows.append(candidate)

    return {
        "schema_version": "1.0",
        "search_date": date.today().isoformat(),
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "official_api_endpoint": SEARCH_ENDPOINT,
        "authenticated_request": True,
        "authentication_source": authentication_source,
        "credential_values_serialized": False,
        "queries": list(queries),
        "query_result_counts": query_counts,
        "unique_candidate_count": len(rows),
        "exact_doi_matches_in_catalog": sum(
            bool(row["already_cataloged_as"]) for row in rows
        ),
        "candidates": rows,
    }


def _write_csv(path: Path, payload: dict[str, Any]) -> None:
    fieldnames = (
        "doi",
        "title",
        "publication_date",
        "version_number",
        "visibility",
        "license",
        "storage_size_bytes",
        "query_hits",
        "already_cataloged_as",
        "official_source_url",
        "abstract",
    )
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for candidate in payload["candidates"]:
            def csv_value(key: str) -> Any:
                value = candidate.get(key)
                if isinstance(value, list):
                    return "|".join(value)
                if isinstance(value, str):
                    return "\n".join(line.rstrip() for line in value.splitlines())
                return value

            writer.writerow(
                {key: csv_value(key) for key in fieldnames}
            )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--json-out",
        type=Path,
        default=Path("hub/audit/dryad_search_candidates.json"),
    )
    parser.add_argument(
        "--csv-out",
        type=Path,
        default=Path("hub/audit/dryad_search_candidates.csv"),
    )
    parser.add_argument("--query", action="append", dest="queries")
    args = parser.parse_args()

    queries = tuple(args.queries) if args.queries else DEFAULT_QUERIES
    payload = search_dryad(queries)
    args.json_out.parent.mkdir(parents=True, exist_ok=True)
    args.csv_out.parent.mkdir(parents=True, exist_ok=True)
    args.json_out.write_text(
        json.dumps(payload, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )
    _write_csv(args.csv_out, payload)
    print(
        f"Dryad search complete: {payload['unique_candidate_count']} unique results; "
        f"{payload['exact_doi_matches_in_catalog']} exact DOI matches already cataloged."
    )
    print(f"JSON: {args.json_out}")
    print(f"CSV: {args.csv_out}")


if __name__ == "__main__":
    main()
