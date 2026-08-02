"""Create a dated ophthalmology repository-search snapshot.

The public output records exact platform-native search syntax and public
candidate metadata. Credential values are read locally and are never written.
Dryad results are imported from the already adjudicated 1 August 2026 search;
the other repository searches are performed through their official APIs.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import shutil
import subprocess
import sys
import time
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Callable, TypeVar

import requests

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from eyedatahub.utils.credentials import load_credentials  # noqa: E402


DEFAULT_DRYAD = ROOT / "hub" / "audit" / "dryad_search_candidates_2026-08-01.json"
DEFAULT_JSON = ROOT / "hub" / "audit" / "repository_search_candidates_2026-08-02.json"
DEFAULT_CSV = ROOT / "hub" / "audit" / "repository_search_candidates_2026-08-02.csv"
FIGSHARE_API = "https://api.figshare.com/v2/articles/search"
MENDELEY_SEARCH = "https://data.mendeley.com/research-data/"

# Platform search engines differ. These concepts are expressed in the native
# syntax archived for each source below. Ambiguous abbreviations such as bare
# "OCT" and bare "iris" are intentionally not used.
SEARCH_CONCEPTS: dict[str, tuple[str, ...]] = {
    "ophthalmology": ("ophthalmology",),
    "ophthalmic": ("ophthalmic",),
    "retina": ("retina",),
    "retinal": ("retinal",),
    "fundus": ("fundus",),
    "glaucoma": ("glaucoma",),
    "cornea": ("cornea",),
    "corneal": ("corneal",),
    "ocular": ("ocular",),
    "cataract": ("cataract",),
    "optical_coherence_tomography": ("optical", "coherence", "tomography"),
    "optical_coherence_tomography_angiography": (
        "optical",
        "coherence",
        "tomography",
        "angiography",
    ),
    "octa": ("octa",),
    "diabetic_retinopathy": ("diabetic", "retinopathy"),
    "macular": ("macular",),
    "uveitis": ("uveitis",),
    "perimetry": ("perimetry",),
    "visual_field": ("visual", "field"),
    "slit_lamp": ("slit", "lamp"),
    "external_eye": ("external", "eye"),
    "anterior_segment": ("anterior", "segment"),
    "retinopathy_of_prematurity": ("retinopathy", "prematurity"),
    "thyroid_eye": ("thyroid", "eye"),
    "retinal_image": ("retinal", "image"),
    "eye_tracking": ("eye", "tracking"),
    "pupillometry": ("pupillometry",),
    "iris_recognition": ("iris", "recognition"),
    "periocular": ("periocular",),
    "oculomotor": ("oculomotor",),
}

FIGSHARE_RESOURCE_TERMS = (
    "dataset",
    "database",
    "benchmark",
    "collection",
    "cohort",
    "corpus",
)

T = TypeVar("T")

_QUOTED_LOCAL_PATH_RE = re.compile(
    r"(?i)(?P<quote>['\"])[A-Z]:\\(?:Users|workspace|temp|tmp)\\[^'\"\r\n]*(?P=quote)"
)
_UNQUOTED_LOCAL_PATH_RE = re.compile(
    r"(?i)\b[A-Z]:\\(?:Users|workspace|temp|tmp)\\[^\s,;<>|]+"
)


def _sanitize_public_value(value: Any) -> Any:
    """Remove local absolute paths before metadata is written publicly."""

    if isinstance(value, dict):
        return {key: _sanitize_public_value(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_sanitize_public_value(item) for item in value]
    if isinstance(value, tuple):
        return tuple(_sanitize_public_value(item) for item in value)
    if not isinstance(value, str):
        return value
    value = _QUOTED_LOCAL_PATH_RE.sub(
        lambda match: f"{match.group('quote')}<LOCAL_PATH>{match.group('quote')}",
        value,
    )
    return _UNQUOTED_LOCAL_PATH_RE.sub("<LOCAL_PATH>", value)


def _iso(value: Any) -> str | None:
    if value is None:
        return None
    if hasattr(value, "isoformat"):
        return str(value.isoformat())
    return str(value)


def _retry(call: Callable[[], T], *, attempts: int = 7) -> T:
    for attempt in range(attempts):
        try:
            return call()
        except requests.RequestException:
            if attempt == attempts - 1:
                raise
            time.sleep(min(2**attempt, 60))
    raise AssertionError("unreachable")


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(_sanitize_public_value(payload), indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )
    temporary.replace(path)


def _load_dryad(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    candidates = []
    for item in payload["candidates"]:
        candidates.append(
            {
                "platform": "dryad",
                "stable_id": item["doi"],
                "title": item.get("title"),
                "description": item.get("abstract"),
                "official_source_url": item.get("official_source_url"),
                "version": item.get("version_number"),
                "last_modified": item.get("last_modification_date"),
                "source_terms": item.get("license"),
                "query_hits": item.get("query_hits") or [],
                "public_metadata": {
                    "publication_date": item.get("publication_date"),
                    "storage_size_bytes": item.get("storage_size_bytes"),
                    "visibility": item.get("visibility"),
                    "related_works": item.get("related_works") or [],
                },
            }
        )
    return {
        "status": "archived_search_loaded",
        "search_date": payload.get("search_date"),
        "official_interface": payload.get("official_api_endpoint"),
        "query_syntax": payload.get("queries"),
        "query_result_counts": payload.get("query_result_counts"),
        "unique_hit_count": len(candidates),
        "result_set_complete": True,
        "candidates": candidates,
    }


def _kaggle_candidate(item: Any, query: str) -> dict[str, Any]:
    value = item.to_dict()
    tags = [tag.get("name") for tag in value.get("tags") or [] if tag.get("name")]
    return {
        "platform": "kaggle",
        "stable_id": value.get("ref"),
        "title": value.get("title"),
        "description": value.get("subtitle"),
        "official_source_url": value.get("url"),
        "version": value.get("currentVersionNumber"),
        "last_modified": value.get("lastUpdated"),
        "source_terms": value.get("licenseName"),
        "query_hits": [query],
        "public_metadata": {
            "tags": tags,
            "total_bytes": value.get("totalBytes"),
            "download_count": value.get("downloadCount"),
        },
    }


def _merge_candidate(
    candidates: dict[str, dict[str, Any]], candidate: dict[str, Any]
) -> None:
    stable_id = str(candidate.get("stable_id") or "").strip()
    if not stable_id:
        return
    if stable_id not in candidates:
        candidates[stable_id] = candidate
        return
    candidates[stable_id]["query_hits"] = sorted(
        set(candidates[stable_id]["query_hits"]) | set(candidate["query_hits"])
    )


def _search_kaggle() -> dict[str, Any]:
    from kaggle.api.kaggle_api_extended import KaggleApi

    api = KaggleApi()
    api.authenticate()
    candidates: dict[str, dict[str, Any]] = {}
    query_counts: dict[str, int] = {}
    capped_queries: list[str] = []
    for key, tokens in SEARCH_CONCEPTS.items():
        query = " ".join(tokens)
        returned = 0
        for page in range(1, 101):
            rows = _retry(
                lambda query=query, page=page: api.dataset_list(
                    search=query,
                    page=page,
                    sort_by="updated",
                )
                or []
            )
            rows = [row for row in rows if row is not None]
            returned += len(rows)
            for row in rows:
                _merge_candidate(candidates, _kaggle_candidate(row, key))
            if len(rows) < 20:
                break
        else:
            capped_queries.append(key)
        query_counts[key] = returned
        print(f"Kaggle {key}: {returned}")
    return {
        "status": "completed" if not capped_queries else "query_limit_reached",
        "search_date": date.today().isoformat(),
        "official_interface": "Kaggle API through kaggle-cli 2.2.3",
        "query_syntax": {
            key: " ".join(tokens) for key, tokens in SEARCH_CONCEPTS.items()
        },
        "query_result_counts": query_counts,
        "unique_hit_count": len(candidates),
        "result_set_complete": not capped_queries,
        "capped_queries": capped_queries,
        "candidates": [candidates[key] for key in sorted(candidates)],
    }


def _search_huggingface() -> dict[str, Any]:
    from huggingface_hub import HfApi

    token = os.environ.get("HF_TOKEN") or None
    api = HfApi(token=token)
    candidates: dict[str, dict[str, Any]] = {}
    query_counts: dict[str, int] = {}
    for key, tokens in SEARCH_CONCEPTS.items():
        query = " ".join(tokens)
        rows = list(api.list_datasets(search=query, limit=None, token=token))
        query_counts[key] = len(rows)
        for item in rows:
            candidate = {
                "platform": "huggingface",
                "stable_id": item.id,
                "title": item.id,
                "description": None,
                "official_source_url": f"https://huggingface.co/datasets/{item.id}",
                "version": item.sha,
                "last_modified": _iso(item.last_modified),
                "source_terms": next(
                    (
                        tag.removeprefix("license:")
                        for tag in item.tags or []
                        if tag.startswith("license:")
                    ),
                    None,
                ),
                "query_hits": [key],
                "public_metadata": {
                    "author": item.author,
                    "created_at": _iso(item.created_at),
                    "gated": item.gated,
                    "private": item.private,
                    "disabled": item.disabled,
                    "downloads": item.downloads,
                    "tags": item.tags or [],
                },
            }
            _merge_candidate(candidates, candidate)
        print(f"Hugging Face {key}: {len(rows)}")
    return {
        "status": "completed",
        "search_date": date.today().isoformat(),
        "official_interface": "huggingface_hub.HfApi.list_datasets",
        "query_syntax": {
            key: " ".join(tokens) for key, tokens in SEARCH_CONCEPTS.items()
        },
        "query_result_counts": query_counts,
        "unique_hit_count": len(candidates),
        "result_set_complete": True,
        "candidates": [candidates[key] for key in sorted(candidates)],
    }


def _figshare_query(tokens: tuple[str, ...]) -> str:
    concept = " AND ".join(f":title: {token}" for token in tokens)
    resources = " OR ".join(
        f":title: {resource}" for resource in FIGSHARE_RESOURCE_TERMS
    )
    return f"{concept} AND ({resources})"


def _search_figshare(session: requests.Session) -> dict[str, Any]:
    candidates: dict[str, dict[str, Any]] = {}
    query_counts: dict[str, int] = {}
    capped_queries: list[str] = []
    syntax: dict[str, str] = {}
    for key, tokens in SEARCH_CONCEPTS.items():
        query = _figshare_query(tokens)
        syntax[key] = query
        returned = 0
        for page in range(1, 12):
            def request() -> requests.Response:
                response = session.post(
                    FIGSHARE_API,
                    json={
                        "search_for": query,
                        "item_type": 3,
                        "page_size": 100,
                        "page": page,
                        "order": "published_date",
                        "order_direction": "asc",
                    },
                    timeout=60,
                )
                if response.status_code == 429 or response.status_code >= 500:
                    response.raise_for_status()
                return response

            response = _retry(request)
            response.raise_for_status()
            rows = response.json()
            returned += len(rows)
            for item in rows:
                stable_id = str(item.get("id") or "")
                candidate = {
                    "platform": "figshare",
                    "stable_id": stable_id,
                    "title": item.get("title"),
                    "description": item.get("description"),
                    "official_source_url": item.get("url_public_html"),
                    "version": item.get("version"),
                    "last_modified": item.get("modified_date"),
                    "source_terms": None,
                    "query_hits": [key],
                    "public_metadata": {
                        "doi": item.get("doi"),
                        "published_date": item.get("published_date"),
                        "defined_type": item.get("defined_type"),
                    },
                }
                _merge_candidate(candidates, candidate)
            if len(rows) < 100:
                break
        else:
            capped_queries.append(key)
        query_counts[key] = returned
        print(f"Figshare {key}: {returned}")
    return {
        "status": "completed" if not capped_queries else "query_limit_reached",
        "search_date": date.today().isoformat(),
        "official_interface": FIGSHARE_API,
        "query_syntax": syntax,
        "query_result_counts": query_counts,
        "unique_hit_count": len(candidates),
        "result_set_complete": not capped_queries,
        "capped_queries": capped_queries,
        "candidates": [candidates[key] for key in sorted(candidates)],
    }


def _concept_hits(text: str) -> list[str]:
    lowered = re.sub(r"[^a-z0-9]+", " ", text.lower())
    padded = f" {lowered} "
    hits = []
    for key, tokens in SEARCH_CONCEPTS.items():
        if all(f" {token} " in padded for token in tokens):
            hits.append(key)
    return hits


def _mendeley_state(page_text: str) -> dict[str, Any]:
    """Extract the public search state embedded by Mendeley Data Showcase."""

    marker = "window.__state = "
    start = page_text.find(marker)
    if start < 0:
        raise ValueError("Mendeley search response did not contain public state")
    start += len(marker)
    end = page_text.find("</script>", start)
    if end < 0:
        raise ValueError("Mendeley search response did not close public state")
    return json.loads(page_text[start:end])


def _mendeley_page(*, query: str, page: int) -> str:
    """Fetch one public search page with the system curl client.

    Mendeley Data's edge service rejects the Python ``requests`` TLS client
    even when the same public URL is available to a browser and curl. The
    command uses an argument vector, never a shell, and no credential.
    """

    curl = shutil.which("curl")
    if not curl:
        raise RuntimeError("curl is required for the public Mendeley search")
    result = subprocess.run(
        [
            curl,
            "--fail",
            "--silent",
            "--show-error",
            "--location",
            "--retry",
            "6",
            "--retry-all-errors",
            "--max-time",
            "60",
            "--get",
            MENDELEY_SEARCH,
            "--data-urlencode",
            f"query={query}",
            "--data-urlencode",
            "source_id=MENDELEY_DATA",
            "--data-urlencode",
            "data_type=dataset",
            "--data-urlencode",
            "page_size=100",
            "--data-urlencode",
            "sort=publication_date_asc",
            "--data-urlencode",
            f"page={page}",
        ],
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        timeout=420,
    )
    return result.stdout


def _search_mendeley() -> dict[str, Any]:
    """Search the public Mendeley Data Showcase without collecting credentials.

    The public search page exposes its returned records as JSON in
    ``window.__state``. Restricting ``source_id`` to ``MENDELEY_DATA`` prevents
    records federated from other repositories from being counted as Mendeley
    hits. Platform credentials remain a separate concern for file transfer.
    """

    candidates: dict[str, dict[str, Any]] = {}
    query_counts: dict[str, int] = {}
    examined_rows = 0
    for key, tokens in SEARCH_CONCEPTS.items():
        query = " ".join(tokens)
        page = 1
        query_seen: set[str] = set()
        expected_total: int | None = None
        while expected_total is None or len(query_seen) < expected_total:
            state = _mendeley_state(_mendeley_page(query=query, page=page))
            data = state.get("datasets", {}).get("data", {})
            rows = data.get("records") or []
            total = int(data.get("total_records") or 0)
            if expected_total is None:
                expected_total = total
                query_counts[key] = total
            if not rows:
                if len(query_seen) != total:
                    raise ValueError(
                        f"Mendeley {key} stopped at {len(query_seen)} of {total} rows"
                    )
                break
            for item in rows:
                stable_id = str(item.get("id") or "").strip()
                if not stable_id or stable_id in query_seen:
                    continue
                query_seen.add(stable_id)
                examined_rows += 1
                doi_values = item.get("doi") or []
                doi = doi_values[0] if doi_values else None
                candidate = {
                    "platform": "mendeley",
                    "stable_id": stable_id,
                    "title": item.get("title"),
                    "description": item.get("description"),
                    "official_source_url": item.get("url"),
                    "version": None,
                    "last_modified": item.get("publication_date"),
                    "source_terms": None,
                    "query_hits": [key],
                    "public_metadata": {
                        "doi": doi,
                        "publication_date": item.get("publication_date"),
                        "access": item.get("access"),
                        "categories": item.get("categories") or [],
                        "source": item.get("source", {}).get("name"),
                    },
                }
                _merge_candidate(candidates, candidate)
            page += 1
        if len(query_seen) != expected_total:
            raise ValueError(
                f"Mendeley {key} returned {len(query_seen)} of {expected_total} rows"
            )
        print(f"Mendeley {key}: {expected_total}")

    return {
        "status": "completed",
        "search_date": date.today().isoformat(),
        "official_interface": MENDELEY_SEARCH,
        "query_syntax": {
            key: {
                "query": " ".join(tokens),
                "source_id": "MENDELEY_DATA",
                "data_type": "dataset",
                "sort": "publication_date_asc",
            }
            for key, tokens in SEARCH_CONCEPTS.items()
        },
        "query_result_counts": dict(sorted(query_counts.items())),
        "search_rows_examined_before_cross_query_deduplication": examined_rows,
        "unique_hit_count": len(candidates),
        "result_set_complete": True,
        "credentials_used_for_search": False,
        "notes": (
            "Public metadata search did not require a credential. Credential "
            "requirements for file transfer are classified separately."
        ),
        "candidates": [candidates[key] for key in sorted(candidates)],
    }


def _write_csv(path: Path, sources: dict[str, dict[str, Any]]) -> None:
    fieldnames = (
        "platform",
        "stable_id",
        "title",
        "description",
        "official_source_url",
        "version",
        "last_modified",
        "source_terms",
        "query_hits",
        "public_metadata_json",
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for platform in sorted(sources):
            for candidate in sources[platform].get("candidates") or []:
                candidate = _sanitize_public_value(candidate)
                writer.writerow(
                    {
                        **{key: candidate.get(key) for key in fieldnames[:-2]},
                        "query_hits": "|".join(candidate.get("query_hits") or []),
                        "public_metadata_json": json.dumps(
                            candidate.get("public_metadata") or {},
                            ensure_ascii=True,
                            sort_keys=True,
                        ),
                    }
                )


def run(*, dryad_path: Path, platforms: set[str]) -> dict[str, Any]:
    load_credentials()
    session = requests.Session()
    session.headers["User-Agent"] = "EyeDataHub-catalog-audit/0.5.0"
    sources: dict[str, dict[str, Any]] = {}
    if "dryad" in platforms:
        sources["dryad"] = _load_dryad(dryad_path)
    if "kaggle" in platforms:
        sources["kaggle"] = _search_kaggle()
    if "huggingface" in platforms:
        sources["huggingface"] = _search_huggingface()
    if "figshare" in platforms:
        sources["figshare"] = _search_figshare(session)
    if "mendeley" in platforms:
        sources["mendeley"] = _search_mendeley()
    return {
        "schema_version": "1.0",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "search_snapshot_date": date.today().isoformat(),
        "scope": "Ophthalmology and ocular data-resource discovery",
        "platforms": sorted(platforms),
        "credential_values_serialized": False,
        "signed_or_temporary_urls_serialized": False,
        "search_concepts": {
            key: list(tokens) for key, tokens in SEARCH_CONCEPTS.items()
        },
        "sources": sources,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dryad", type=Path, default=DEFAULT_DRYAD)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--csv-out", type=Path, default=DEFAULT_CSV)
    parser.add_argument(
        "--preserve-unselected-from",
        type=Path,
        help=(
            "Existing search snapshot whose unselected platform results are "
            "preserved while the requested --platform searches are refreshed."
        ),
    )
    parser.add_argument(
        "--platform",
        action="append",
        choices=("dryad", "kaggle", "huggingface", "figshare", "mendeley"),
    )
    args = parser.parse_args()
    platforms = set(args.platform or ("dryad", "kaggle", "huggingface", "figshare", "mendeley"))
    payload = run(dryad_path=args.dryad, platforms=platforms)
    if args.preserve_unselected_from:
        previous = json.loads(
            args.preserve_unselected_from.read_text(encoding="utf-8")
        )
        preserved = {
            platform: result
            for platform, result in (previous.get("sources") or {}).items()
            if platform not in platforms
        }
        payload["sources"] = {
            **preserved,
            **payload["sources"],
        }
        payload["platforms"] = sorted(payload["sources"])
        payload["preserved_platforms"] = sorted(preserved)
    _write_json(args.json_out, payload)
    _write_csv(args.csv_out, payload["sources"])
    for platform, result in payload["sources"].items():
        print(
            f"{platform}: status={result['status']}; "
            f"unique_hits={result.get('unique_hit_count')}"
        )


if __name__ == "__main__":
    main()
