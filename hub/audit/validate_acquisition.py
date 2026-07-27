"""Validate official acquisition routes without downloading dataset files.

The live checks exercise repository metadata or file-listing endpoints.  They
therefore satisfy verification level 3 (``transfer_initiated`` in the release
protocol) but are deliberately reported as partial tests, never as complete
downloads.  Credentials are represented only by an authentication category;
their names and values are not written to the output.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import platform
import re
from contextlib import redirect_stderr, redirect_stdout
from datetime import date
from io import StringIO
from pathlib import Path
from typing import Any, Callable
from urllib.parse import quote

import requests

from eyedatahub import __version__
from eyedatahub.acquisition import acquire_dataset
from eyedatahub.datasets.registry import REGISTRY


CHECK_DATE = date.today().isoformat()
USER_AGENT = f"EyeDataHub/{__version__} acquisition-validation"
TIMEOUT = 30


FIGSHARE_ARTICLES = {
    "fives": "19688169",
    "coph100": "27061084",
    "tom500": "27133389",
    "mcoa": "28123088",
    "tear_meniscus": "28650536",
    "rvo_me": "29804435",
}
FIGSHARE_COLLECTIONS = {
    "as_oct_keratitis": "7036994",
    "grape": "6406319",
}


def _get(url: str, **kwargs: Any) -> requests.Response:
    headers = {"User-Agent": USER_AGENT, **kwargs.pop("headers", {})}
    response = requests.get(url, headers=headers, timeout=TIMEOUT, **kwargs)
    response.raise_for_status()
    return response


def _base_row(record_id: str, backend: str, test_type: str) -> dict[str, Any]:
    return {
        "test_id": f"live-{record_id}-{test_type}",
        "record_id": record_id,
        "backend": backend,
        "test_type": test_type,
        "verification_date": CHECK_DATE,
        "verification_level": "3_transfer_initiated",
        "test_scope": "official_metadata_or_file_listing_only",
        "complete_download_validated": "false",
        "dataset_files_transferred": 0,
        "authentication_state": "none",
        "result": "failed",
        "response_status": "",
        "resolved_destination": "",
        "item_count": "",
        "failure_or_limitation": "",
        "credentials_logged": "false",
        "terms_accepted_by_eyedatahub": "false",
        "environment": f"{platform.system()} | Python {platform.python_version()} | EyeDataHub {__version__}",
    }


def _execute(
    record_id: str,
    backend: str,
    test_type: str,
    operation: Callable[[], tuple[int | str, str, int]],
    *,
    authentication_state: str = "none",
) -> dict[str, Any]:
    row = _base_row(record_id, backend, test_type)
    row["authentication_state"] = authentication_state
    try:
        status, destination, count = operation()
        row.update(
            result="passed",
            response_status=status,
            resolved_destination=destination,
            item_count=count,
            failure_or_limitation=(
                "No dataset file was transferred; this validates only the current metadata or file-listing route."
            ),
        )
    except Exception as exc:  # frozen evidence preserves actionable failures
        row["failure_or_limitation"] = f"{type(exc).__name__}: {exc}"
    return row


def _figshare_article(article_id: str) -> tuple[int, str, int]:
    url = f"https://api.figshare.com/v2/articles/{article_id}/files"
    response = _get(url, headers={"Content-Type": "application/json"})
    files = response.json()
    if not files:
        raise RuntimeError("official Figshare article returned an empty file list")
    return response.status_code, response.url, len(files)


def _figshare_collection(collection_id: str) -> tuple[int, str, int]:
    url = f"https://api.figshare.com/v2/collections/{collection_id}/articles"
    response = _get(url, params={"page_size": 1000})
    articles = response.json()
    if not articles:
        raise RuntimeError("official Figshare collection returned no articles")
    file_count = 0
    for article in articles:
        file_count += len(
            _get(
                f"https://api.figshare.com/v2/articles/{article['id']}/files"
            ).json()
        )
    if not file_count:
        raise RuntimeError("collection articles returned no files")
    return response.status_code, response.url, file_count


def _zenodo(record_id: str) -> tuple[int, str, int]:
    response = _get(f"https://zenodo.org/api/records/{record_id}")
    files = response.json().get("files", [])
    if not files:
        raise RuntimeError("official Zenodo record returned no files")
    return response.status_code, response.url, len(files)


def _mendeley(dataset_id: str, version: int) -> tuple[int, str, int]:
    response = _get(
        f"https://api.data.mendeley.com/datasets/publics/{dataset_id}/files",
        headers={"Accept": "application/vnd.mendeley-public-dataset.1+json"},
        params={"version": version, "$start": 0, "$limit": 100},
    )
    files = response.json()
    if not files:
        raise RuntimeError("official Mendeley API returned no files")
    return response.status_code, response.url, len(files)


def _dryad(doi: str) -> tuple[int, str, int]:
    identifier = quote(f"doi:{doi}", safe="")
    response = _get(f"https://datadryad.org/api/v2/datasets/{identifier}")
    version_href = response.json().get("_links", {}).get("stash:version", {}).get("href")
    if not version_href:
        raise RuntimeError("Dryad dataset response did not identify a current version")
    version = _get(f"https://datadryad.org{version_href}")
    files_href = version.json().get("_links", {}).get("stash:files", {}).get("href")
    if not files_href:
        raise RuntimeError("Dryad version response did not identify files")
    files_response = _get(f"https://datadryad.org{files_href}")
    files = files_response.json().get("_embedded", {}).get("stash:files", [])
    if not files:
        raise RuntimeError("official Dryad API returned no files")
    return files_response.status_code, files_response.url, len(files)


def _huggingface(repo: str) -> tuple[int, str, int]:
    response = _get(f"https://huggingface.co/api/datasets/{repo}")
    siblings = response.json().get("siblings", [])
    if not siblings:
        raise RuntimeError("official Hugging Face API returned no repository files")
    return response.status_code, response.url, len(siblings)


def _github(owner_repo: str) -> tuple[int, str, int]:
    response = _get(f"https://api.github.com/repos/{owner_repo}/contents")
    contents = response.json()
    if not isinstance(contents, list) or not contents:
        raise RuntimeError("official GitHub API returned no repository contents")
    return response.status_code, response.url, len(contents)


def _physionet(slug: str, version: str) -> tuple[int, str, int]:
    response = _get(f"https://physionet.org/content/{slug}/{version}/")
    paths = set(re.findall(r'href="files/[^"?#]+', response.text))
    if not paths:
        # PhysioNet renders recursive file tables with direct versioned links.
        paths = set(re.findall(rf'href="/files/{re.escape(slug)}/{re.escape(version)}/[^"?#]+', response.text))
    if not paths:
        raise RuntimeError("PhysioNet page resolved but exposed no file listing")
    return response.status_code, response.url, len(paths)


def _kaggle_competition(slug: str) -> tuple[str, str, int]:
    if not (os.environ.get("KAGGLE_USERNAME") and os.environ.get("KAGGLE_KEY")):
        raise RuntimeError("explicit test credentials were not configured")
    with redirect_stdout(StringIO()), redirect_stderr(StringIO()):
        try:
            from kaggle import api
        except ImportError as exc:
            raise RuntimeError("optional kaggle client is not installed") from exc
        api.authenticate()
        files = list(api.competition_list_files(slug))
    if not files:
        raise RuntimeError("authenticated Kaggle API returned no competition files")
    return "authenticated_api_success", f"https://www.kaggle.com/competitions/{slug}/data", len(files)


def _preflight_case(record_id: str) -> dict[str, Any]:
    dataset = REGISTRY.get_dataset(record_id)
    result = acquire_dataset(dataset, Path(".eyedatahub-validation-unused"), dry_run=True)
    row = _base_row(record_id, dataset.info.loader_backend, "preflight_behavior")
    row.update(
        verification_level="software_behavior_test",
        test_scope="read_only_preflight_no_filesystem_write",
        authentication_state=result.preflight["authentication_category"],
        result="passed",
        response_status=result.status,
        resolved_destination=result.preflight.get("preferred_route_url") or "",
        item_count=0,
        failure_or_limitation=result.message,
    )
    return row


def _frozen_execution_rows(evidence_path: Path) -> list[dict[str, Any]]:
    evidence = json.loads(evidence_path.read_text(encoding="utf-8"))
    complete = evidence["complete_transfer"]
    repeated = evidence["repeated_invocation"]
    environment = evidence["environment"]
    source = REGISTRY.get_dataset(evidence["record_id"]).info.preferred_route_url
    complete_row = _base_row(evidence["record_id"], "figshare", "complete_download")
    complete_row.update(
        test_id="live-ophthalwechat-complete-download",
        verification_date=evidence["verification_date_local"],
        verification_level="4_complete_download_validated",
        test_scope="complete_official_figshare_deposit_transfer",
        complete_download_validated="true",
        dataset_files_transferred=complete["complete_official_deposit_files"],
        result="passed",
        response_status=complete["status"],
        resolved_destination=source,
        item_count=complete["complete_official_deposit_files"],
        failure_or_limitation=(
            "Public files were transferred solely to validate acquisition behavior; "
            "no participant-level scientific analysis was performed."
        ),
        environment=environment,
    )
    repeated_row = _base_row(evidence["record_id"], "figshare", "repeated_invocation")
    repeated_row.update(
        test_id="software-ophthalwechat-repeated-invocation",
        verification_date=evidence["verification_date_local"],
        verification_level="software_behavior_test",
        test_scope="existing_files_detected_without_retransfer",
        complete_download_validated="true",
        dataset_files_transferred=0,
        result="passed",
        response_status=repeated["status"],
        resolved_destination=source,
        item_count=complete["complete_official_deposit_files"],
        failure_or_limitation="Existing files were detected; no second transfer was initiated.",
        environment=environment,
    )
    return [complete_row, repeated_row]


def run_checks(execution_evidence: Path | None = None) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for record_id, article_id in FIGSHARE_ARTICLES.items():
        rows.append(
            _execute(record_id, "figshare", "file_listing", lambda value=article_id: _figshare_article(value))
        )
    for record_id, collection_id in FIGSHARE_COLLECTIONS.items():
        rows.append(
            _execute(record_id, "figshare", "collection_file_listing", lambda value=collection_id: _figshare_collection(value))
        )
    rows.extend(
        [
            _execute("jsiec", "zenodo", "file_listing", lambda: _zenodo("3477553")),
            _execute("migs_video", "zenodo", "file_listing", lambda: _zenodo("19438128")),
            _execute("octdl", "mendeley", "file_listing", lambda: _mendeley("sncdhf53xc", 4)),
            _execute("dryad_gcc_glaucoma", "dryad", "file_listing", lambda: _dryad("10.5061/dryad.xwdbrv1tn")),
            _execute("mm_retinal_reason", "huggingface", "file_listing", lambda: _huggingface("lxirich/MM-Retinal-Reason")),
            _execute("perg_ioba", "physionet", "file_listing", lambda: _physionet("perg-ioba-dataset", "1.0.0")),
            _execute(
                "aptos2019",
                "kaggle",
                "authenticated_file_listing",
                lambda: _kaggle_competition("aptos2019-blindness-detection"),
                authentication_state="user_supplied_api_credentials",
            ),
        ]
    )
    source_repository = _execute(
        "tsukazaki_uwf",
        "github",
        "source_repository_listing",
        lambda: _github("DateCazuki/Fundus_Diagnosis"),
    )
    source_repository.update(
        verification_level="2_acquisition_route_verified",
        test_scope="official_source_repository_listing_not_dataset_transfer",
        failure_or_limitation=(
            "The repository listing was reachable, but the represented dataset remains "
            "author-contact access and was not transferred."
        ),
    )
    rows.append(source_repository)
    rows.extend(_preflight_case(record_id) for record_id in [
        "fives",                 # anonymous supported route
        "aptos2019",            # authenticated/click-through route
        "ophthalmology_mcqa_v3",# unknown source terms warning
        "corn_pro",              # manual approval deliberately blocked
        "corn_collection",       # combined restricted collection deliberately blocked
        "migs_video",            # anonymous Zenodo route with supported preflight
    ])
    if execution_evidence is not None:
        rows.extend(_frozen_execution_rows(execution_evidence))
    return rows


def write_rows(rows: list[dict[str, Any]], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    fields = list(rows[0])
    with output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    output.with_suffix(".json").write_text(
        json.dumps(
            {
                "schema_version": "1.0",
                "generated_on": CHECK_DATE,
                "command": "python hub/audit/validate_acquisition.py --out <PATH>",
                "interpretation": (
                    "Live repository checks retrieved metadata or file listings only. "
                    "They are partial transfer tests and not complete dataset downloads."
                ),
                "results": rows,
            },
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--execution-evidence", type=Path)
    parser.add_argument(
        "--fail-on-test-failure",
        action="store_true",
        help="Return nonzero when a live external check fails.",
    )
    args = parser.parse_args()
    rows = run_checks(args.execution_evidence)
    write_rows(rows, args.out)
    passed = sum(row["result"] == "passed" for row in rows)
    print(f"acquisition validation: {passed}/{len(rows)} checks passed; {args.out}")
    if args.fail_on_test_failure and passed != len(rows):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
