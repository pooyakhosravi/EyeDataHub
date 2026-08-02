"""Enrich saved Figshare and Hugging Face candidate metadata for screening.

Only public metadata, public identifiers, file names, sizes, and source
checksums are retained. Download URLs, bearer tokens, and local paths are not
written. The output is checkpointed after every candidate and is resumable.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, TypeVar

import requests

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from eyedatahub.utils.credentials import load_credentials  # noqa: E402


DEFAULT_INPUT = ROOT / "hub" / "audit" / "repository_search_candidates_2026-08-02.json"
DEFAULT_OUTPUT = ROOT / "hub" / "audit" / "repository_candidate_details_2026-08-02.json"
DEFAULT_SCREENING = ROOT / "hub" / "audit" / "repository_screening_ledger_2026-08-02.csv"
T = TypeVar("T")

_CREDENTIAL_ASSIGNMENT_RE = re.compile(
    r"(?i)(?P<name>api[_-]?key|access[_-]?token|client[_-]?secret|password)"
    r"(?P<separator>\s*[:=]\s*)['\"][^'\"\r\n]{4,}['\"]"
)
_SIGNED_QUERY_RE = re.compile(
    r"(?i)(?P<name>x-goog-signature|x-amz-signature|signature)=[^&#\s'\"]+"
)
_QUOTED_LOCAL_PATH_RE = re.compile(
    r"(?i)(?P<quote>['\"])[A-Z]:\\(?:Users|workspace|temp|tmp)\\[^'\"\r\n]*(?P=quote)"
)
_UNQUOTED_LOCAL_PATH_RE = re.compile(
    r"(?i)\b[A-Z]:\\(?:Users|workspace|temp|tmp)\\[^\s,;<>|]+"
)


def _sanitize_public_value(value: Any) -> Any:
    """Redact credential examples, signed values, and local paths recursively."""

    if isinstance(value, dict):
        return {key: _sanitize_public_value(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_sanitize_public_value(item) for item in value]
    if isinstance(value, tuple):
        return tuple(_sanitize_public_value(item) for item in value)
    if not isinstance(value, str):
        return value
    value = _CREDENTIAL_ASSIGNMENT_RE.sub(
        lambda match: f"{match.group('name')}{match.group('separator')}\"<REDACTED>\"",
        value,
    )
    value = _SIGNED_QUERY_RE.sub(
        lambda match: f"{match.group('name')}=<REDACTED>", value
    )
    value = _QUOTED_LOCAL_PATH_RE.sub(
        lambda match: f"{match.group('quote')}<LOCAL_PATH>{match.group('quote')}",
        value,
    )
    return _UNQUOTED_LOCAL_PATH_RE.sub("<LOCAL_PATH>", value)


def _retry(call: Callable[[], T], *, attempts: int = 7) -> T:
    for attempt in range(attempts):
        try:
            return call()
        except requests.RequestException:
            if attempt == attempts - 1:
                raise
            time.sleep(min(2**attempt, 60))
    raise AssertionError("unreachable")


def _write(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(_sanitize_public_value(payload), indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )
    for attempt in range(20):
        try:
            temporary.replace(path)
            break
        except PermissionError:
            if attempt == 19:
                raise
            time.sleep(0.1)


def _figshare_detail(session: requests.Session, stable_id: str) -> dict[str, Any]:
    response = _retry(
        lambda: session.get(
            f"https://api.figshare.com/v2/articles/{stable_id}",
            timeout=60,
        )
    )
    if response.status_code in (403, 404, 410):
        return {
            "platform": "figshare",
            "stable_id": stable_id,
            "metadata_result": "public_detail_not_available",
            "http_status": response.status_code,
            "download_urls_serialized": False,
        }
    response.raise_for_status()
    item = response.json()
    files = []
    for file_item in item.get("files") or []:
        files.append(
            {
                "file_id": file_item.get("id"),
                "name": file_item.get("name"),
                "bytes": file_item.get("size"),
                "source_checksum_type": "md5"
                if file_item.get("computed_md5")
                else None,
                "source_checksum": file_item.get("computed_md5"),
                "is_link_only": file_item.get("is_link_only"),
            }
        )
    licence = item.get("license") or {}
    return {
        "platform": "figshare",
        "stable_id": stable_id,
        "metadata_result": "public_detail_confirmed",
        "title": item.get("title"),
        "description": item.get("description"),
        "doi": item.get("doi"),
        "resource_doi": item.get("resource_doi"),
        "resource_title": item.get("resource_title"),
        "references": item.get("references") or [],
        "tags": item.get("tags") or [],
        "categories": item.get("categories") or [],
        "defined_type": item.get("defined_type"),
        "published_date": item.get("published_date"),
        "modified_date": item.get("modified_date"),
        "version": item.get("version"),
        "source_terms": licence.get("name") or licence.get("url"),
        "file_count": len(files),
        "total_file_bytes": sum(int(file_item.get("bytes") or 0) for file_item in files),
        "files": files,
        "download_urls_serialized": False,
    }


def _jsonable(value: Any) -> Any:
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    if isinstance(value, dict):
        return {str(key): _jsonable(item) for key, item in value.items()}
    if isinstance(value, (list, tuple, set)):
        return [_jsonable(item) for item in value]
    if hasattr(value, "to_dict"):
        return _jsonable(value.to_dict())
    if hasattr(value, "isoformat"):
        return value.isoformat()
    return str(value)


def _huggingface_detail(api: Any, stable_id: str, token: str | None) -> dict[str, Any]:
    from huggingface_hub.utils import HfHubHTTPError

    try:
        item = api.dataset_info(
            stable_id,
            files_metadata=True,
            timeout=60,
            token=token,
        )
    except HfHubHTTPError as exc:
        status = exc.response.status_code if exc.response is not None else None
        if status in (401, 403, 404, 410):
            return {
                "platform": "huggingface",
                "stable_id": stable_id,
                "metadata_result": "public_detail_not_available",
                "http_status": status,
                "download_urls_serialized": False,
            }
        raise
    files = []
    for sibling in item.siblings or []:
        lfs = getattr(sibling, "lfs", None) or {}
        files.append(
            {
                "name": sibling.rfilename,
                "bytes": getattr(sibling, "size", None),
                "blob_id": getattr(sibling, "blob_id", None),
                "lfs_sha256": (
                    lfs.get("sha256")
                    if isinstance(lfs, dict)
                    else getattr(lfs, "sha256", None)
                ),
            }
        )
    return {
        "platform": "huggingface",
        "stable_id": stable_id,
        "metadata_result": "public_detail_confirmed",
        "title": item.id,
        "description": item.description,
        "citation": item.citation,
        "revision": item.sha,
        "created_at": _jsonable(item.created_at),
        "last_modified": _jsonable(item.last_modified),
        "private": item.private,
        "gated": item.gated,
        "disabled": item.disabled,
        "tags": item.tags or [],
        "card_data": _jsonable(item.card_data),
        "file_count": len(files),
        "files": files,
        "download_urls_serialized": False,
    }


def _kaggle_detail(api: Any, stable_id: str) -> dict[str, Any]:
    with tempfile.TemporaryDirectory(prefix="eyedatahub-kaggle-metadata-") as temp:
        try:
            _retry(lambda: api.dataset_metadata(stable_id, temp))
        except requests.HTTPError as exc:
            status = exc.response.status_code if exc.response is not None else None
            if status in (401, 403, 404, 410):
                return {
                    "platform": "kaggle",
                    "stable_id": stable_id,
                    "metadata_result": "official_metadata_not_available",
                    "http_status": status,
                    "download_urls_serialized": False,
                }
            raise
        metadata_files = sorted(Path(temp).glob("*.json"))
        if len(metadata_files) != 1:
            raise RuntimeError(
                f"Expected one Kaggle metadata file for {stable_id}; "
                f"received {len(metadata_files)}"
            )
        payload = json.loads(metadata_files[0].read_text(encoding="utf-8"))
    info = payload.get("info") or payload
    licences = info.get("licenses") or []
    licence_names = [
        str(item.get("name"))
        for item in licences
        if isinstance(item, dict) and item.get("name")
    ]
    return {
        "platform": "kaggle",
        "stable_id": stable_id,
        "metadata_result": "official_metadata_confirmed",
        "dataset_id": info.get("datasetId"),
        "title": info.get("title"),
        "description": info.get("description"),
        "owner_user": info.get("ownerUser"),
        "keywords": info.get("keywords") or [],
        "source_terms": "; ".join(licence_names) or None,
        "usability_rating": info.get("usabilityRating"),
        "total_views": info.get("totalViews"),
        "total_votes": info.get("totalVotes"),
        "total_downloads": info.get("totalDownloads"),
        "expected_update_frequency": info.get("expectedUpdateFrequency"),
        "download_urls_serialized": False,
    }


def run(
    *,
    input_path: Path,
    output_path: Path,
    platforms: set[str],
    screening_path: Path | None = None,
) -> dict[str, Any]:
    load_credentials()
    search = json.loads(input_path.read_text(encoding="utf-8"))
    if output_path.exists():
        report = json.loads(output_path.read_text(encoding="utf-8"))
    else:
        report = {
            "schema_version": "1.0",
            "generated_at_utc": None,
            "source_search_snapshot": input_path.name,
            "credential_values_serialized": False,
            "signed_or_download_urls_serialized": False,
            "records": [],
        }
    completed = {
        f"{item['platform']}:{item['stable_id']}": item
        for item in report["records"]
    }
    session = requests.Session()
    session.headers["User-Agent"] = "EyeDataHub-catalog-audit/0.5.0"
    hf_api = None
    kaggle_api = None
    hf_token = os.environ.get("HF_TOKEN") or None
    if "huggingface" in platforms:
        from huggingface_hub import HfApi

        hf_api = HfApi(token=hf_token)
    if "kaggle" in platforms:
        from kaggle.api.kaggle_api_extended import KaggleApi

        kaggle_api = KaggleApi()
        kaggle_api.authenticate()

    screening_pending: set[str] | None = None
    if screening_path is not None:
        import csv

        with screening_path.open(encoding="utf-8", newline="") as handle:
            screening_pending = {
                f"{row['platform']}:{row['stable_id']}"
                for row in csv.DictReader(handle)
                if row["final_decision"] == "manual_review_pending"
            }

    candidates = []
    for platform in sorted(platforms):
        candidates.extend(search["sources"][platform].get("candidates") or [])
    if screening_pending is not None:
        candidates = [
            candidate
            for candidate in candidates
            if f"{candidate['platform']}:{candidate['stable_id']}" in screening_pending
        ]
    for index, candidate in enumerate(candidates, start=1):
        platform = candidate["platform"]
        stable_id = str(candidate["stable_id"])
        key = f"{platform}:{stable_id}"
        if key in completed:
            print(f"[{index}/{len(candidates)}] {key}: already completed")
            continue
        print(f"[{index}/{len(candidates)}] {key}")
        if platform == "figshare":
            detail = _figshare_detail(session, stable_id)
        elif platform == "huggingface":
            detail = _huggingface_detail(hf_api, stable_id, hf_token)
        elif platform == "kaggle":
            detail = _kaggle_detail(kaggle_api, stable_id)
        else:
            raise RuntimeError(f"Unsupported enrichment platform: {platform}")
        completed[key] = detail
        report["records"] = [completed[item] for item in sorted(completed)]
        report["generated_at_utc"] = datetime.now(timezone.utc).isoformat()
        report["completed_record_count"] = len(completed)
        _write(output_path, report)
        time.sleep(0.1)
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument(
        "--platform",
        action="append",
        choices=("figshare", "huggingface", "kaggle"),
    )
    parser.add_argument(
        "--only-screening-pending",
        action="store_true",
        help="Enrich only rows currently marked manual_review_pending.",
    )
    parser.add_argument("--screening-ledger", type=Path, default=DEFAULT_SCREENING)
    args = parser.parse_args()
    report = run(
        input_path=args.input,
        output_path=args.output,
        platforms=set(args.platform or ("figshare", "huggingface")),
        screening_path=args.screening_ledger if args.only_screening_pending else None,
    )
    print(f"Enriched records: {report.get('completed_record_count', 0)}")


if __name__ == "__main__":
    main()
