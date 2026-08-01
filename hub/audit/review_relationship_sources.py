"""Collect private source text and relationship candidates for catalog review.

This script performs metadata-only requests. It never downloads dataset files,
prints credential values, or writes authorization headers to its output. The
default output directory is under ``reports/``, which is gitignored because the
collected source text is working material rather than a public catalog artifact.

Usage::

    python hub/audit/review_relationship_sources.py
"""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import quote, urlparse

import requests
from dotenv import load_dotenv


ROOT = Path(__file__).resolve().parents[2]
CATALOG_PATH = ROOT / "hub" / "catalog.json"
DEFAULT_OUTPUT = ROOT / "reports" / "relationship_review" / "source_review.json"
REVIEW_DATE = "2026-08-01"
USER_AGENT = "EyeDataHub relationship review/0.3.0"
MAX_TEXT_CHARS = 250_000

GENERIC_ALIASES = {
    "adaptive optics",
    "amd",
    "cataract",
    "corneal",
    "data",
    "dataset",
    "diabetic retinopathy",
    "dme",
    "drive data",
    "eye",
    "fundus",
    "glaucoma",
    "image",
    "medical",
    "multimodal",
    "oct",
    "octa",
    "ophthalmology",
    "retina",
    "retinal",
    "segmentation",
    "surgical",
    "version",
}

ALIAS_OVERRIDES: dict[str, tuple[str, ...]] = {
    "aptos2019": ("APTOS 2019", "APTOS2019"),
    "brset": ("BRSET",),
    "cataract1k": ("Cataract-1K", "Cataract 1K"),
    "cataract_101": ("Cataract-101", "Cataract 101"),
    "chase_db1": ("CHASE_DB1", "CHASE-DB1", "CHASE DB1"),
    "deepdrid": ("DeepDRiD",),
    "drishti_gs": ("Drishti-GS", "Drishti GS"),
    "drive": ("DRIVE",),
    "e_ophtha": ("e-ophtha", "e_ophtha", "e-Ophtha"),
    "eyepacs": ("EyePACS",),
    "g1020": ("G1020",),
    "gamma": ("GAMMA",),
    "hrf": ("HRF",),
    "idrid": ("IDRiD", "IDRID"),
    "jsiec": ("JSIEC", "JSEIC"),
    "maples_dr": ("MAPLES-DR", "MAPLES DR"),
    "mbrset": ("mBRSET",),
    "messidor2": ("MESSIDOR-2", "MESSIDOR2"),
    "odir2019": ("ODIR-2019", "ODIR", "Ocular Disease Recognition"),
    "octa_500": ("OCTA-500", "OCTA_500"),
    "oimhs": ("OIMHS",),
    "palm": ("PALM",),
    "papila": ("PAPILA",),
    "refuge2018": ("REFUGE", "REFUGE1", "REFUGE 2018"),
    "rfmid": ("RFMiD",),
    "riga": ("RIGA",),
    "rite": ("RITE",),
    "roc": ("ROC",),
    "stare": ("STARE",),
    "sustech_sysu": ("SUSTech-SYSU",),
}


@dataclass
class Check:
    source_type: str
    url: str
    status: str
    text: str = ""
    title: str = ""
    version: str = ""
    file_names: tuple[str, ...] = ()
    related_identifiers: tuple[str, ...] = ()
    note: str = ""

    def public_dict(self) -> dict[str, Any]:
        return {
            "source_type": self.source_type,
            "url": self.url,
            "status": self.status,
            "title": self.title,
            "version": self.version,
            "file_names": list(self.file_names),
            "related_identifiers": list(self.related_identifiers),
            "note": self.note,
        }


def clean_text(value: Any) -> str:
    text = html.unescape(str(value or ""))
    text = re.sub(r"<script\b[^>]*>.*?</script>", " ", text, flags=re.I | re.S)
    text = re.sub(r"<style\b[^>]*>.*?</style>", " ", text, flags=re.I | re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", text).strip()[:MAX_TEXT_CHARS]


def request(
    url: str,
    *,
    headers: dict[str, str] | None = None,
    auth: tuple[str, str] | None = None,
    params: dict[str, Any] | None = None,
) -> requests.Response:
    safe_headers = {"User-Agent": USER_AGENT, "Accept": "application/json,text/plain,text/html"}
    safe_headers.update(headers or {})
    last_error: Exception | None = None
    for attempt in range(3):
        try:
            response = requests.get(
                url,
                headers=safe_headers,
                auth=auth,
                params=params,
                timeout=35,
            )
            if response.status_code not in {429, 500, 502, 503, 504}:
                return response
        except requests.RequestException as exc:
            last_error = exc
        time.sleep(1.5 * (attempt + 1))
    if last_error is not None:
        raise last_error
    return response


def bearer(name: str) -> dict[str, str]:
    value = os.getenv(name)
    return {"Authorization": f"Bearer {value}"} if value else {}


def datacite_check(doi: str) -> Check:
    url = f"https://api.datacite.org/dois/{quote(doi, safe='/')}"
    response = request(url)
    if not response.ok:
        return Check("datacite", url, f"http_{response.status_code}")
    attributes = response.json().get("data", {}).get("attributes", {})
    descriptions = " ".join(
        item.get("description", "") for item in attributes.get("descriptions", [])
    )
    titles = attributes.get("titles", [])
    related = tuple(
        str(item.get("relatedIdentifier", ""))
        for item in attributes.get("relatedIdentifiers", [])
        if item.get("relatedIdentifier")
    )
    return Check(
        "datacite",
        url,
        "confirmed",
        text=clean_text(descriptions),
        title=clean_text(titles[0].get("title", "") if titles else ""),
        version=clean_text(attributes.get("version", "")),
        related_identifiers=related,
    )


def huggingface_checks(repo_id: str) -> list[Check]:
    api_url = f"https://huggingface.co/api/datasets/{repo_id}"
    raw_url = f"https://huggingface.co/datasets/{repo_id}/raw/main/README.md"
    headers = bearer("HF_TOKEN")
    checks: list[Check] = []
    response = request(api_url, headers=headers)
    if response.ok:
        payload = response.json()
        card = payload.get("cardData") or {}
        text_parts = [payload.get("description", ""), json.dumps(card, ensure_ascii=False)]
        checks.append(
            Check(
                "huggingface_api",
                api_url,
                "confirmed",
                text=clean_text(" ".join(text_parts)),
                title=clean_text(payload.get("id", repo_id)),
                version=clean_text(payload.get("sha", "")),
                file_names=tuple(
                    str(item.get("rfilename", ""))
                    for item in payload.get("siblings", [])
                    if item.get("rfilename")
                ),
            )
        )
    else:
        checks.append(Check("huggingface_api", api_url, f"http_{response.status_code}"))
    response = request(raw_url, headers=headers)
    checks.append(
        Check(
            "huggingface_readme",
            raw_url,
            "confirmed" if response.ok else f"http_{response.status_code}",
            text=clean_text(response.text) if response.ok else "",
        )
    )
    return checks


def kaggle_check(slug: str) -> Check:
    url = f"https://www.kaggle.com/api/v1/datasets/view/{slug}"
    username = os.getenv("KAGGLE_USERNAME")
    key = os.getenv("KAGGLE_KEY")
    response = request(url, auth=(username, key) if username and key else None)
    if not response.ok:
        return Check("kaggle_api", url, f"http_{response.status_code}")
    payload = response.json()
    return Check(
        "kaggle_api",
        url,
        "confirmed",
        text=clean_text(" ".join(str(payload.get(key, "")) for key in ("title", "subtitle", "description"))),
        title=clean_text(payload.get("title", "")),
        version=clean_text(payload.get("currentVersionNumber", "")),
        file_names=tuple(
            str(item.get("name", ""))
            for item in payload.get("resources", [])
            if item.get("name")
        ),
    )


def zenodo_check(record_id: str) -> Check:
    url = f"https://zenodo.org/api/records/{record_id}"
    response = request(url, headers=bearer("ZENODO_TOKEN"))
    if not response.ok:
        return Check("zenodo_api", url, f"http_{response.status_code}")
    payload = response.json()
    metadata = payload.get("metadata", {})
    related = tuple(
        str(item.get("identifier", ""))
        for item in metadata.get("related_identifiers", [])
        if item.get("identifier")
    )
    return Check(
        "zenodo_api",
        url,
        "confirmed",
        text=clean_text(metadata.get("description", "")),
        title=clean_text(metadata.get("title", "")),
        version=clean_text(metadata.get("version", "")),
        file_names=tuple(
            str(item.get("key", "")) for item in payload.get("files", []) if item.get("key")
        ),
        related_identifiers=related,
    )


def figshare_check(record: dict[str, Any]) -> Check:
    url = str(record.get("source_landing_page_url") or "")
    match = re.search(r"(?:figshare[^/]*[/.]|m9\.figshare\.)(?:article\.)?(\d{5,})", url)
    if not match:
        match = re.search(r"figshare\.(\d{5,})", str(record.get("dataset_doi") or ""))
    if not match:
        return Check("figshare_api", url, "identifier_unavailable")
    record_id = match.group(1)
    headers = bearer("FIGSHARE_TOKEN")
    for kind in ("articles", "collections"):
        api_url = f"https://api.figshare.com/v2/{kind}/{record_id}"
        response = request(api_url, headers=headers)
        if not response.ok:
            continue
        payload = response.json()
        files = payload.get("files", [])
        return Check(
            f"figshare_{kind[:-1]}_api",
            api_url,
            "confirmed",
            text=clean_text(payload.get("description", "")),
            title=clean_text(payload.get("title", "")),
            version=clean_text(payload.get("version", "")),
            file_names=tuple(str(item.get("name", "")) for item in files if item.get("name")),
        )
    return Check("figshare_api", url, "metadata_unavailable")


def github_checks(url: str) -> list[Check]:
    match = re.search(r"github\.com/([^/]+)/([^/#?]+)", url)
    if not match:
        return []
    owner, repo = match.group(1), match.group(2).removesuffix(".git")
    headers = {"Accept": "application/vnd.github+json"}
    api_url = f"https://api.github.com/repos/{owner}/{repo}"
    readme_url = f"https://api.github.com/repos/{owner}/{repo}/readme"
    checks: list[Check] = []
    response = request(api_url, headers=headers)
    if response.ok:
        payload = response.json()
        checks.append(
            Check(
                "github_api",
                api_url,
                "confirmed",
                text=clean_text(payload.get("description", "")),
                title=clean_text(payload.get("full_name", "")),
                version=clean_text(payload.get("default_branch", "")),
            )
        )
    else:
        checks.append(Check("github_api", api_url, f"http_{response.status_code}"))
    response = request(readme_url, headers={**headers, "Accept": "application/vnd.github.raw+json"})
    checks.append(
        Check(
            "github_readme",
            readme_url,
            "confirmed" if response.ok else f"http_{response.status_code}",
            text=clean_text(response.text) if response.ok else "",
        )
    )
    return checks


def html_check(url: str, source_type: str) -> Check:
    response = request(url, headers={"Accept": "text/html,text/plain"})
    return Check(
        source_type,
        url,
        "confirmed" if response.ok else f"http_{response.status_code}",
        text=clean_text(response.text) if response.ok else "",
    )


def record_checks(record: dict[str, Any]) -> list[Check]:
    checks: list[Check] = []
    doi = record.get("dataset_doi")
    if doi and str(doi).lower() != "unknown":
        try:
            checks.append(datacite_check(str(doi)))
        except Exception as exc:  # network evidence must preserve failures
            checks.append(Check("datacite", str(doi), "request_failed", note=type(exc).__name__))

    backend = str(record.get("loader_backend") or record.get("download_type") or "")
    repository_id = str(record.get("repository_record_id") or "")
    source_url = str(record.get("source_landing_page_url") or "")
    try:
        if backend == "huggingface" and "/" in repository_id:
            checks.extend(huggingface_checks(repository_id))
        elif backend == "kaggle" and "/" in repository_id:
            checks.append(kaggle_check(repository_id))
        elif backend == "zenodo":
            match = re.search(r"(?:records/|zenodo:)(\d+)", repository_id or source_url)
            if match:
                checks.append(zenodo_check(match.group(1)))
        elif backend == "figshare":
            checks.append(figshare_check(record))
        elif backend == "github" or "github.com/" in source_url:
            checks.extend(github_checks(source_url))
        elif backend == "physionet" and source_url:
            checks.append(html_check(source_url, "physionet_page"))
        elif backend in {"manual", "direct"} and source_url:
            parsed = urlparse(source_url)
            if parsed.scheme in {"http", "https"} and not re.search(
                r"\.(?:zip|rar|7z|tar|gz|csv|json|xlsx?|mat|h5)(?:$|[?#])",
                parsed.path,
                re.I,
            ):
                checks.append(html_check(source_url, "source_page"))
    except Exception as exc:  # preserve the check without leaking request details
        checks.append(Check(f"{backend}_metadata", source_url, "request_failed", note=type(exc).__name__))
    return checks


def aliases_for(record: dict[str, Any]) -> tuple[str, ...]:
    record_id = str(record["record_id"])
    name = str(record["canonical_name"])
    aliases = set(ALIAS_OVERRIDES.get(record_id, ()))
    readable_id = record_id.replace("_", " ")
    if len(readable_id) >= 5:
        aliases.add(readable_id)
    lead = re.split(r"\s*(?::|\u2014)\s*", name, maxsplit=1)[0].strip()
    if len(lead) >= 5:
        aliases.add(lead)
    for token in re.findall(r"[A-Za-z][A-Za-z0-9+_-]{3,}", name):
        if token.isupper() or any(char.isdigit() for char in token):
            aliases.add(token)
    return tuple(
        sorted(
            {
                alias.strip()
                for alias in aliases
                if alias.strip().lower() not in GENERIC_ALIASES and len(alias.strip()) >= 4
            },
            key=lambda value: (-len(value), value.lower()),
        )
    )


def match_candidates(
    record: dict[str, Any],
    source_text: str,
    aliases: dict[str, tuple[str, ...]],
) -> list[dict[str, str]]:
    candidates: list[dict[str, str]] = []
    normalized = source_text.replace("_", " ")
    for target_id, target_aliases in aliases.items():
        if target_id == record["record_id"]:
            continue
        for alias in target_aliases:
            pattern = re.compile(rf"(?<![A-Za-z0-9]){re.escape(alias)}(?![A-Za-z0-9])", re.I)
            match = pattern.search(normalized)
            if not match:
                continue
            start = max(0, match.start() - 180)
            end = min(len(normalized), match.end() + 260)
            context = re.sub(r"\s+", " ", normalized[start:end]).strip()
            candidates.append(
                {
                    "target_record_id": target_id,
                    "matched_alias": alias,
                    "context": context,
                }
            )
            break
    return candidates


def review_record(record: dict[str, Any], aliases: dict[str, tuple[str, ...]]) -> dict[str, Any]:
    catalog_text = clean_text(
        " ".join(
            str(record.get(field) or "")
            for field in ("canonical_name", "description", "notes", "citation", "tags")
        )
    )
    checks = record_checks(record)
    source_text = clean_text(" ".join([catalog_text, *(check.text for check in checks)]))
    return {
        "record_id": record["record_id"],
        "canonical_name": record["canonical_name"],
        "primary_category": record.get("primary_category"),
        "loader_backend": record.get("loader_backend"),
        "official_source_url": record.get("source_landing_page_url"),
        "checks": [check.public_dict() for check in checks],
        "catalog_text": catalog_text,
        "source_text": source_text,
        "candidates": match_candidates(record, source_text, aliases),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--catalog", type=Path, default=CATALOG_PATH)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--workers", type=int, default=8)
    args = parser.parse_args()

    load_dotenv(ROOT / ".env")
    payload = json.loads(args.catalog.read_text(encoding="utf-8"))
    records = payload.get("records", payload)
    if len(records) != 251:
        raise RuntimeError(f"Expected 251 catalog records, found {len(records)}")
    aliases = {record["record_id"]: aliases_for(record) for record in records}

    reviewed: list[dict[str, Any]] = []
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
        futures = {executor.submit(review_record, record, aliases): record for record in records}
        for index, future in enumerate(as_completed(futures), start=1):
            reviewed.append(future.result())
            if index % 25 == 0 or index == len(records):
                print(f"reviewed metadata for {index}/{len(records)} records")

    reviewed.sort(key=lambda row: row["record_id"])
    output = {
        "schema_version": "1.0",
        "review_date": REVIEW_DATE,
        "catalog_record_count": len(records),
        "method": (
            "Catalog fields were combined with metadata-only official platform/API "
            "responses. Dataset files were not downloaded. Candidate links are lexical "
            "leads requiring curator confirmation, not accepted relationships."
        ),
        "credentials": (
            "User-supplied credentials were used only in request headers where available; "
            "no values, signed URLs, or authorization headers are retained."
        ),
        "records": reviewed,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    total_candidates = sum(len(row["candidates"]) for row in reviewed)
    confirmed_checks = sum(
        check["status"] == "confirmed" for row in reviewed for check in row["checks"]
    )
    print(
        f"wrote {args.output}; records={len(reviewed)} "
        f"confirmed_metadata_checks={confirmed_checks} candidates={total_candidates}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
