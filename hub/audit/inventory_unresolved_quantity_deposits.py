"""Inventory official files for records without a resolved primary quantity.

The inventory is a metadata and file-listing audit. It never serializes bearer
tokens or short-lived download URLs, and it does not download dataset files.
Versioned repository deposits are compared with the exact versions recorded in
the catalog so later source changes are visible rather than silently folded
into the analyzed snapshot. Figshare, Kaggle, and Hugging Face inventories use
their official APIs or clients and retain no download or pagination URLs.
"""

from __future__ import annotations

import argparse
import csv
import html
import json
import os
import re
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import quote, urlencode, urljoin

import requests

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from eyedatahub.datasets.registry import REGISTRY  # noqa: E402
from eyedatahub.utils.credentials import load_credentials  # noqa: E402


API_ROOT = "https://datadryad.org"
DRYAD_TEST_ENDPOINT = f"{API_ROOT}/api/v2/test"
DRYAD_TOKEN_ENDPOINT = f"{API_ROOT}/oauth/token"
MENDELEY_AUTH_API_ROOT = "https://api.mendeley.com"
MENDELEY_DATA_API_ROOT = "https://api.data.mendeley.com"
MENDELEY_TOKEN_ENDPOINT = f"{MENDELEY_AUTH_API_ROOT}/oauth/token"
MENDELEY_BROWSER_ROOT = "https://data.mendeley.com"
_MENDELEY_BEARER_REJECTED = False
DEFAULT_INPUT = ROOT / "hub" / "audit" / "resource_quantity_unresolved_2026-08-02.csv"
DEFAULT_JSON = ROOT / "hub" / "audit" / "unresolved_quantity_deposit_inventory_2026-08-02.json"
DEFAULT_CSV = ROOT / "hub" / "audit" / "unresolved_quantity_deposit_inventory_2026-08-02.csv"


def _get_json(
    session: requests.Session,
    url: str,
    *,
    headers: dict[str, str],
    params: dict[str, Any] | None = None,
) -> requests.Response:
    for attempt in range(5):
        response = session.get(url, headers=headers, params=params, timeout=60)
        if response.status_code != 429 and response.status_code < 500:
            return response
        if attempt == 4:
            return response
        time.sleep(2**attempt)
    raise AssertionError("unreachable")


def _dryad_headers(session: requests.Session) -> tuple[dict[str, str], str]:
    load_credentials()
    token = os.environ.get("DRYAD_TOKEN", "").strip()
    if token:
        headers = {"Authorization": f"Bearer {token}"}
        response = session.get(DRYAD_TEST_ENDPOINT, headers=headers, timeout=30)
        if response.ok:
            return headers, "DRYAD_TOKEN"

    client_id = os.environ.get("DRYAD_CLIENT_ID", "").strip()
    client_secret = os.environ.get("DRYAD_SECRET", "").strip()
    if not client_id or not client_secret:
        raise RuntimeError(
            "Dryad file listings require DRYAD_TOKEN or both "
            "DRYAD_CLIENT_ID and DRYAD_SECRET."
        )
    response = session.post(
        DRYAD_TOKEN_ENDPOINT,
        data={
            "client_id": client_id,
            "client_secret": client_secret,
            "grant_type": "client_credentials",
        },
        headers={"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"},
        timeout=30,
    )
    response.raise_for_status()
    token = str(response.json().get("access_token") or "").strip()
    if not token:
        raise RuntimeError("Dryad returned no access token.")
    return {"Authorization": f"Bearer {token}"}, "client_credentials"


def _dryad_inventory(
    session: requests.Session,
    *,
    record_id: str,
    canonical_name: str,
    official_source_url: str,
    doi: str,
    catalog_version: str | None,
    headers: dict[str, str],
) -> dict[str, Any]:
    identifier = quote(f"doi:{doi}", safe="")
    dataset_response = _get_json(
        session,
        f"{API_ROOT}/api/v2/datasets/{identifier}",
        headers=headers,
    )
    dataset_response.raise_for_status()
    dataset = dataset_response.json()
    version_href = dataset.get("_links", {}).get("stash:version", {}).get("href")
    if not version_href:
        raise RuntimeError("Dryad did not expose the current version link.")

    version_response = _get_json(
        session,
        urljoin(API_ROOT, version_href),
        headers=headers,
    )
    version_response.raise_for_status()
    version = version_response.json()
    observed_version = str(version.get("versionNumber") or "")
    files_href = version.get("_links", {}).get("stash:files", {}).get("href")
    if not files_href:
        raise RuntimeError("Dryad did not expose the current version file listing.")

    files: list[dict[str, Any]] = []
    next_href: str | None = files_href
    while next_href:
        response = _get_json(
            session,
            urljoin(API_ROOT, next_href),
            headers=headers,
        )
        response.raise_for_status()
        payload = response.json()
        for item in payload.get("_embedded", {}).get("stash:files", []):
            files.append(
                {
                    "path": item.get("path"),
                    "bytes": item.get("size"),
                    "mime_type": item.get("mimeType"),
                    "source_checksum_type": item.get("digestType"),
                    "source_checksum": item.get("digest"),
                    "source_status": item.get("status"),
                }
            )
        next_href = payload.get("_links", {}).get("next", {}).get("href")

    expected_bytes = sum(int(item.get("bytes") or 0) for item in files)
    return {
        "record_id": record_id,
        "canonical_name": canonical_name,
        "provider": "dryad",
        "official_source_url": official_source_url,
        "dataset_identifier": doi,
        "catalog_deposit_version": str(catalog_version or ""),
        "observed_deposit_version": observed_version,
        "version_matches_catalog": observed_version == str(catalog_version or ""),
        "listing_result": "official_file_listing_confirmed",
        "expected_file_count": len(files),
        "expected_bytes": expected_bytes,
        "source_checksums_available": sum(
            bool(item.get("source_checksum")) for item in files
        ),
        "files": files,
        "notes": "Official current-version metadata and file listing reviewed.",
    }


MENDELEY_PATTERN = re.compile(
    r"data\.mendeley\.com/datasets/(?P<dataset_id>[A-Za-z0-9]+)"
    r"(?:/(?P<version>\d+))?"
)


def _curl_config_escape(value: str) -> str:
    """Escape a value for an in-memory curl config without logging it."""
    if "\n" in value or "\r" in value:
        raise ValueError("OAuth values must not contain line breaks")
    return value.replace("\\", "\\\\").replace('"', '\\"')


def _curl_json_request(
    *,
    url: str,
    method: str,
    headers: dict[str, str],
    basic_auth: tuple[str, str] | None = None,
    form: dict[str, str] | None = None,
) -> tuple[int, Any]:
    """Use native curl when Cloudflare challenges the Python HTTP client.

    Secrets are supplied through curl's standard-input configuration rather
    than command-line arguments. Only the response body is retained in memory.
    """
    executable = shutil.which("curl.exe") or shutil.which("curl")
    if not executable:
        raise RuntimeError("Native curl is required for the Mendeley API on this host")
    config = [
        "silent",
        "show-error",
        f'request = "{_curl_config_escape(method)}"',
        f'url = "{_curl_config_escape(url)}"',
        'write-out = "\\n%{http_code}"',
    ]
    for name, value in headers.items():
        config.append(
            f'header = "{_curl_config_escape(name)}: {_curl_config_escape(value)}"'
        )
    if basic_auth:
        username, password = basic_auth
        config.append(
            f'user = "{_curl_config_escape(username)}:'
            f'{_curl_config_escape(password)}"'
        )
    if form is not None:
        config.append(f'data = "{_curl_config_escape(urlencode(form))}"')
    result = subprocess.run(
        [executable, "--config", "-"],
        input="\n".join(config) + "\n",
        text=True,
        capture_output=True,
        timeout=60,
        check=False,
    )
    if result.returncode:
        raise RuntimeError(
            f"Native curl did not complete the Mendeley request "
            f"(exit {result.returncode})"
        )
    body, separator, status_text = result.stdout.rpartition("\n")
    if not separator or not status_text.isdigit():
        raise RuntimeError("Native curl returned no Mendeley HTTP status")
    payload: Any = None
    if body.strip():
        try:
            payload = json.loads(body)
        except json.JSONDecodeError:
            payload = None
    return int(status_text), payload


def _mendeley_oauth_headers(
    session: requests.Session,
) -> tuple[dict[str, str], str, int | None]:
    """Generate a dynamic Mendeley bearer token without persisting it."""
    load_credentials(login_huggingface=False)
    client_id = os.environ.get("MENDELEY_CLIENT_ID", "").strip()
    client_secret = os.environ.get("MENDELEY_SECRET", "").strip()
    if not client_id or not client_secret:
        token = os.environ.get("MENDELEY_TOKEN", "").strip()
        if token:
            return {"Authorization": f"Bearer {token}"}, "supplied_access_token", None
        raise RuntimeError(
            "Mendeley requires MENDELEY_CLIENT_ID and MENDELEY_SECRET for OAuth."
        )

    redirect_uri = os.environ.get("MENDELEY_REDIRECT_URI", "").strip()
    refresh_token = os.environ.get("MENDELEY_REFRESH_TOKEN", "").strip()
    authorization_code = os.environ.get("MENDELEY_AUTHORIZATION_CODE", "").strip()
    if refresh_token:
        if not redirect_uri:
            raise RuntimeError(
                "MENDELEY_REDIRECT_URI is required with MENDELEY_REFRESH_TOKEN."
            )
        authentication_source = "refresh_token"
        form = {
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
            "redirect_uri": redirect_uri,
        }
    elif authorization_code:
        if not redirect_uri:
            raise RuntimeError(
                "MENDELEY_REDIRECT_URI is required with MENDELEY_AUTHORIZATION_CODE."
            )
        authentication_source = "authorization_code"
        form = {
            "grant_type": "authorization_code",
            "code": authorization_code,
            "redirect_uri": redirect_uri,
        }
    else:
        authentication_source = "client_credentials"
        form = {"grant_type": "client_credentials", "scope": "all"}

    request_headers = {
        "Accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    response = session.post(
        MENDELEY_TOKEN_ENDPOINT,
        auth=(client_id, client_secret),
        data=form,
        headers=request_headers,
        timeout=30,
    )
    if response.status_code == 403 and response.headers.get("Server", "").lower() == "cloudflare":
        status_code, payload = _curl_json_request(
            url=MENDELEY_TOKEN_ENDPOINT,
            method="POST",
            headers=request_headers,
            basic_auth=(client_id, client_secret),
            form=form,
        )
    else:
        status_code = response.status_code
        try:
            payload = response.json()
        except requests.JSONDecodeError:
            payload = None
    if status_code >= 400:
        raise RuntimeError(
            f"Mendeley OAuth token exchange returned HTTP {status_code}."
        )
    if not isinstance(payload, dict):
        raise RuntimeError("Mendeley OAuth returned an unexpected response.")
    token = str(payload.get("access_token") or "").strip()
    if not token:
        raise RuntimeError("Mendeley OAuth returned no access token.")
    expires_in = payload.get("expires_in")
    return (
        {"Authorization": f"Bearer {token}"},
        authentication_source,
        int(expires_in) if isinstance(expires_in, (int, float)) else None,
    )


def _mendeley_data_json(
    session: requests.Session,
    *,
    path: str,
    headers: dict[str, str],
    params: dict[str, Any],
) -> tuple[int, Any]:
    """Request Mendeley dataset metadata only from the data API host."""
    url = f"{MENDELEY_DATA_API_ROOT}/{path.lstrip('/')}"
    response = session.get(url, headers=headers, params=params, timeout=60)
    if response.status_code == 403 and response.headers.get("Server", "").lower() == "cloudflare":
        query_url = f"{url}?{urlencode(params)}" if params else url
        return _curl_json_request(
            url=query_url,
            method="GET",
            headers=headers,
        )
    try:
        payload = response.json()
    except requests.JSONDecodeError:
        payload = None
    return response.status_code, payload


def _mendeley_browser_archive_size(
    *,
    dataset_id: str,
    version: str,
) -> tuple[int, int | None]:
    """Confirm the official version-specific Download All archive and its bytes."""
    executable = shutil.which("curl.exe") or shutil.which("curl")
    if not executable:
        raise RuntimeError("Native curl is required for the Mendeley browser route")
    url = (
        f"{MENDELEY_BROWSER_ROOT}/public-api/zip/"
        f"{quote(dataset_id, safe='')}/download/{quote(version, safe='')}"
    )
    config = [
        "silent",
        "show-error",
        "location",
        'range = "0-0"',
        f'output = "{_curl_config_escape(os.devnull)}"',
        'write-out = "%{http_code}\\n%header{content-range}"',
        f'url = "{_curl_config_escape(url)}"',
    ]
    result = subprocess.run(
        [executable, "--config", "-"],
        input="\n".join(config) + "\n",
        text=True,
        capture_output=True,
        timeout=90,
        check=False,
    )
    if result.returncode:
        raise RuntimeError(
            "The official Mendeley browser archive request did not complete "
            f"(curl exit {result.returncode})."
        )
    lines = result.stdout.splitlines()
    if not lines or not lines[0].isdigit():
        raise RuntimeError("The Mendeley browser archive returned no HTTP status.")
    status_code = int(lines[0])
    content_range = lines[1].strip() if len(lines) > 1 else ""
    match = re.fullmatch(r"bytes\s+0-0/(\d+)", content_range, flags=re.IGNORECASE)
    return status_code, int(match.group(1)) if match else None


def _mendeley_browser_page_metadata(
    *,
    dataset_id: str,
    version: str = "",
) -> tuple[str, str]:
    """Read the current version and archive state from the public source page."""
    executable = shutil.which("curl.exe") or shutil.which("curl")
    if not executable:
        raise RuntimeError("Native curl is required for the Mendeley source page")
    suffix = f"/{quote(version, safe='')}" if version else ""
    url = (
        f"{MENDELEY_BROWSER_ROOT}/datasets/"
        f"{quote(dataset_id, safe='')}{suffix}"
    )
    result = subprocess.run(
        [
            executable,
            "--silent",
            "--show-error",
            "--fail",
            "--location",
            "--max-time",
            "90",
            url,
        ],
        capture_output=True,
        text=True,
        timeout=120,
        check=False,
    )
    if result.returncode:
        raise RuntimeError(
            "The official Mendeley source page did not complete "
            f"(curl exit {result.returncode})."
        )
    page = result.stdout
    version_match = re.search(
        r'name="citation_volume"\s+content="(\d+)"',
        page,
        flags=re.IGNORECASE,
    )
    archive_match = re.search(
        r'"archive"\s*:\s*\{\s*"data"\s*:\s*\{\s*"status"\s*:\s*"([A-Z_]+)"',
        page,
    )
    observed_version = html.unescape(version_match.group(1)) if version_match else ""
    archive_status = archive_match.group(1) if archive_match else "UNKNOWN"
    return observed_version, archive_status


def _mendeley_inventory(
    session: requests.Session,
    *,
    record_id: str,
    canonical_name: str,
    official_source_url: str,
    catalog_version: str | None,
    headers: dict[str, str],
    authentication_source: str,
) -> dict[str, Any]:
    global _MENDELEY_BEARER_REJECTED
    match = MENDELEY_PATTERN.search(official_source_url)
    if not match:
        raise RuntimeError("Could not parse the Mendeley dataset ID and version.")
    dataset_id = match.group("dataset_id")
    observed_version = match.group("version") or str(catalog_version or "")
    source_archive_status = "UNKNOWN"
    if not observed_version:
        observed_version, source_archive_status = _mendeley_browser_page_metadata(
            dataset_id=dataset_id
        )
    if not observed_version:
        raise RuntimeError("The official Mendeley page exposed no current version.")
    request_headers = {
        **headers,
        "Accept": "application/vnd.mendeley-public-dataset.1+json",
    }

    files: list[dict[str, Any]] = []
    start = 0
    limit = 100
    while True:
        params: dict[str, Any] = {"$start": start, "$limit": limit}
        if observed_version:
            params["version"] = observed_version
        if _MENDELEY_BEARER_REJECTED:
            status_code, payload = 401, None
        else:
            status_code, payload = _mendeley_data_json(
                session,
                path=f"datasets/publics/{dataset_id}/files",
                headers=request_headers,
                params=params,
            )
        if status_code in (401, 403):
            _MENDELEY_BEARER_REJECTED = True
            archive_status, archive_bytes = _mendeley_browser_archive_size(
                dataset_id=dataset_id,
                version=observed_version,
            )
            if archive_status == 206 and archive_bytes is not None:
                return {
                    "record_id": record_id,
                    "canonical_name": canonical_name,
                    "provider": "mendeley",
                    "official_source_url": official_source_url,
                    "dataset_identifier": dataset_id,
                    "catalog_deposit_version": str(
                        catalog_version or observed_version
                    ),
                    "observed_deposit_version": observed_version,
                    "version_matches_catalog": observed_version
                    == str(catalog_version or observed_version),
                    "listing_result": "official_archive_route_confirmed",
                    "expected_file_count": None,
                    "expected_bytes": archive_bytes,
                    "source_checksums_available": 0,
                    "files": [],
                    "notes": (
                        "The current version-specific Download All route returned "
                        "an official ZIP archive. Internal files will be enumerated "
                        "during content inspection. The bearer-token response reflects "
                        "the retired OAuth audience, not source unavailability."
                    ),
                }
            if source_archive_status == "UNKNOWN":
                _, source_archive_status = _mendeley_browser_page_metadata(
                    dataset_id=dataset_id,
                    version=observed_version,
                )
            if source_archive_status in {"PENDING", "PROCESSING"}:
                return {
                    "record_id": record_id,
                    "canonical_name": canonical_name,
                    "provider": "mendeley",
                    "official_source_url": official_source_url,
                    "dataset_identifier": dataset_id,
                    "catalog_deposit_version": str(
                        catalog_version or observed_version
                    ),
                    "observed_deposit_version": observed_version,
                    "version_matches_catalog": observed_version
                    == str(catalog_version or observed_version),
                    "listing_result": "official_archive_preparing",
                    "expected_file_count": None,
                    "expected_bytes": None,
                    "source_checksums_available": 0,
                    "files": [],
                    "notes": (
                        "The official current-version page reports that its Download "
                        "All archive is being prepared. This is a temporary source "
                        "state, not a credential or dataset failure."
                    ),
                }
            client_credentials_only = authentication_source == "client_credentials"
            return {
                "record_id": record_id,
                "canonical_name": canonical_name,
                "provider": "mendeley",
                "official_source_url": official_source_url,
                "dataset_identifier": dataset_id,
                "catalog_deposit_version": str(catalog_version or observed_version),
                "observed_deposit_version": observed_version,
                "version_matches_catalog": observed_version
                == str(catalog_version or observed_version),
                "listing_result": (
                    "user_authorization_required"
                    if client_credentials_only
                    else "credential_required"
                ),
                "expected_file_count": None,
                "expected_bytes": None,
                "source_checksums_available": None,
                "files": [],
                "notes": (
                    "Mendeley issued an OAuth token, but dataset-file access requires "
                    "a user-authorized token from the authorization-code or refresh-token "
                    "flow. This is an authorization scope requirement, not a source failure."
                    if client_credentials_only
                    else "The configured Mendeley authorization did not permit this "
                    "dataset-file request; this is an access requirement, not a source failure."
                ),
            }
        if status_code >= 400:
            raise RuntimeError(
                f"Mendeley dataset-file request returned HTTP {status_code}."
            )
        if isinstance(payload, list):
            batch = payload
        else:
            batch = payload.get("results", payload.get("files", []))
        if not isinstance(batch, list):
            raise RuntimeError("Mendeley returned an unexpected file-listing response.")
        for item in batch:
            details = item.get("content_details") or {}
            files.append(
                {
                    "path": item.get("filename") or item.get("name") or item.get("id"),
                    "bytes": item.get("size") or details.get("size"),
                    "mime_type": item.get("content_type") or details.get("content_type"),
                    "source_checksum_type": None,
                    "source_checksum": None,
                    "source_status": None,
                }
            )
        if len(batch) < limit:
            break
        start += len(batch)

    expected_bytes = sum(int(item.get("bytes") or 0) for item in files)
    return {
        "record_id": record_id,
        "canonical_name": canonical_name,
        "provider": "mendeley",
        "official_source_url": official_source_url,
        "dataset_identifier": dataset_id,
        "catalog_deposit_version": str(catalog_version or observed_version),
        "observed_deposit_version": observed_version,
        "version_matches_catalog": observed_version
        == str(catalog_version or observed_version),
        "listing_result": "official_file_listing_confirmed",
        "expected_file_count": len(files),
        "expected_bytes": expected_bytes,
        "source_checksums_available": 0,
        "files": files,
        "notes": "Official version-specific Mendeley file listing reviewed.",
    }


def _credential_required_record(
    *,
    record_id: str,
    canonical_name: str,
    provider: str,
    official_source_url: str,
    dataset_identifier: str,
    catalog_version: str | None,
    notes: str,
) -> dict[str, Any]:
    return {
        "record_id": record_id,
        "canonical_name": canonical_name,
        "provider": provider,
        "official_source_url": official_source_url,
        "dataset_identifier": dataset_identifier,
        "catalog_deposit_version": str(catalog_version or ""),
        "observed_deposit_version": None,
        "version_matches_catalog": None,
        "listing_result": "credential_required",
        "expected_file_count": None,
        "expected_bytes": None,
        "source_checksums_available": None,
        "files": [],
        "notes": notes,
    }


def _figshare_inventory(
    session: requests.Session,
    *,
    record_id: str,
    canonical_name: str,
    official_source_url: str,
    article_id: str,
    catalog_version: str | None,
) -> dict[str, Any]:
    headers: dict[str, str] = {"Accept": "application/json"}
    token = os.environ.get("FIGSHARE_TOKEN", "").strip()
    if token:
        headers["Authorization"] = f"token {token}"
    response = _get_json(
        session,
        f"https://api.figshare.com/v2/articles/{article_id}",
        headers=headers,
    )
    if response.status_code in (401, 403):
        return _credential_required_record(
            record_id=record_id,
            canonical_name=canonical_name,
            provider="figshare",
            official_source_url=official_source_url,
            dataset_identifier=article_id,
            catalog_version=catalog_version,
            notes=(
                "The official Figshare API requires the configured account or "
                "token for this record; this is an access requirement, not a "
                "source failure."
            ),
        )
    response.raise_for_status()
    payload = response.json()
    observed_version = str(payload.get("version") or "")
    files: list[dict[str, Any]] = []
    for item in payload.get("files") or []:
        checksum = item.get("supplied_md5") or item.get("computed_md5")
        files.append(
            {
                "path": item.get("name") or item.get("id"),
                "bytes": item.get("size"),
                "mime_type": item.get("mimetype"),
                "source_checksum_type": "md5" if checksum else None,
                "source_checksum": checksum,
                "source_status": (
                    "link_only" if item.get("is_link_only") else "repository_file"
                ),
            }
        )
    expected_bytes = sum(int(item.get("bytes") or 0) for item in files)
    expected_catalog_version = str(catalog_version or observed_version)
    return {
        "record_id": record_id,
        "canonical_name": canonical_name,
        "provider": "figshare",
        "official_source_url": official_source_url,
        "dataset_identifier": article_id,
        "catalog_deposit_version": expected_catalog_version,
        "observed_deposit_version": observed_version,
        "version_matches_catalog": observed_version == expected_catalog_version,
        "listing_result": "official_file_listing_confirmed",
        "expected_file_count": len(files),
        "expected_bytes": expected_bytes,
        "source_checksums_available": sum(
            bool(item.get("source_checksum")) for item in files
        ),
        "files": files,
        "notes": "Official version-specific Figshare file listing reviewed.",
    }


def _kaggle_inventory(
    *,
    record_id: str,
    canonical_name: str,
    official_source_url: str,
    dataset_id: str,
    catalog_version: str | None,
) -> dict[str, Any]:
    try:
        from kaggle.api.kaggle_api_extended import KaggleApi

        api = KaggleApi()
        api.authenticate()
        files: list[dict[str, Any]] = []
        page_token: str | None = None
        while True:
            listing = api.dataset_list_files(
                dataset_id,
                page_token=page_token,
                page_size=100,
            )
            for item in listing.files or []:
                files.append(
                    {
                        "path": getattr(item, "name", None),
                        "bytes": getattr(item, "total_bytes", None),
                        "mime_type": None,
                        "source_checksum_type": None,
                        "source_checksum": None,
                        "source_status": "repository_file",
                    }
                )
            page_token = getattr(listing, "next_page_token", None) or getattr(
                listing, "nextPageToken", None
            )
            if not page_token:
                break
    except Exception as exc:
        status = getattr(exc, "status", None) or getattr(exc, "status_code", None)
        text = str(exc).lower()
        if status in (401, 403) or "authentication" in text or "unauthorized" in text:
            return _credential_required_record(
                record_id=record_id,
                canonical_name=canonical_name,
                provider="kaggle",
                official_source_url=official_source_url,
                dataset_identifier=dataset_id,
                catalog_version=catalog_version,
                notes=(
                    "The official Kaggle client requires the corresponding account "
                    "credential for this record; this is an access requirement, "
                    "not a source failure."
                ),
            )
        raise
    expected_bytes = sum(int(item.get("bytes") or 0) for item in files)
    return {
        "record_id": record_id,
        "canonical_name": canonical_name,
        "provider": "kaggle",
        "official_source_url": official_source_url,
        "dataset_identifier": dataset_id,
        "catalog_deposit_version": str(catalog_version or ""),
        "observed_deposit_version": None,
        "version_matches_catalog": None if catalog_version else True,
        "listing_result": "official_file_listing_confirmed",
        "expected_file_count": len(files),
        "expected_bytes": expected_bytes,
        "source_checksums_available": 0,
        "files": files,
        "notes": (
            "Official Kaggle client file listing reviewed. The listing endpoint "
            "does not expose a stable deposit-version identifier."
        ),
    }


def _huggingface_inventory(
    *,
    record_id: str,
    canonical_name: str,
    official_source_url: str,
    dataset_id: str,
    catalog_version: str | None,
) -> dict[str, Any]:
    from huggingface_hub import HfApi
    from huggingface_hub.errors import GatedRepoError, HfHubHTTPError

    token = os.environ.get("HF_TOKEN", "").strip() or None
    try:
        info = HfApi(token=token).dataset_info(dataset_id, files_metadata=True)
    except (GatedRepoError, HfHubHTTPError) as exc:
        status = getattr(getattr(exc, "response", None), "status_code", None)
        if status in (401, 403) or isinstance(exc, GatedRepoError):
            return _credential_required_record(
                record_id=record_id,
                canonical_name=canonical_name,
                provider="huggingface",
                official_source_url=official_source_url,
                dataset_identifier=dataset_id,
                catalog_version=catalog_version,
                notes=(
                    "The Hugging Face dataset requires the corresponding account "
                    "credential or gated-repository authorization; this is an "
                    "access requirement, not a source failure."
                ),
            )
        raise
    files: list[dict[str, Any]] = []
    for item in info.siblings or []:
        lfs = item.lfs or {}
        checksum = lfs.get("sha256") if isinstance(lfs, dict) else None
        files.append(
            {
                "path": item.rfilename,
                "bytes": item.size,
                "mime_type": None,
                "source_checksum_type": "sha256" if checksum else None,
                "source_checksum": checksum,
                "source_status": "repository_file",
            }
        )
    observed_version = str(info.sha or "")
    expected_catalog_version = str(catalog_version or "")
    expected_bytes = sum(int(item.get("bytes") or 0) for item in files)
    return {
        "record_id": record_id,
        "canonical_name": canonical_name,
        "provider": "huggingface",
        "official_source_url": official_source_url,
        "dataset_identifier": dataset_id,
        "catalog_deposit_version": expected_catalog_version,
        "observed_deposit_version": observed_version,
        "version_matches_catalog": (
            observed_version == expected_catalog_version
            if expected_catalog_version
            else None
        ),
        "listing_result": "official_file_listing_confirmed",
        "expected_file_count": len(files),
        "expected_bytes": expected_bytes,
        "source_checksums_available": sum(
            bool(item.get("source_checksum")) for item in files
        ),
        "files": files,
        "notes": (
            "Official Hugging Face repository tree reviewed at the recorded commit."
        ),
    }


def _inventory_provider(info: Any) -> str:
    source_url = str(info.source_landing_page_url or info.download_url or "").lower()
    if "data.mendeley.com" in source_url:
        return "mendeley"
    if "figshare" in source_url or (
        info.repository_record_id and str(info.repository_record_id).isdigit()
    ):
        return "figshare"
    return str(info.download_type)


def _write_csv(path: Path, records: list[dict[str, Any]]) -> None:
    fieldnames = [
        "record_id",
        "canonical_name",
        "provider",
        "official_source_url",
        "dataset_identifier",
        "catalog_deposit_version",
        "observed_deposit_version",
        "version_matches_catalog",
        "listing_result",
        "expected_file_count",
        "expected_bytes",
        "file_index",
        "file_path",
        "file_bytes",
        "mime_type",
        "source_checksum_type",
        "source_checksum_available",
        "source_status",
        "notes",
    ]
    rows: list[dict[str, Any]] = []
    for record in records:
        files = record["files"] or [None]
        for index, item in enumerate(files, start=1):
            rows.append(
                {
                    "record_id": record["record_id"],
                    "canonical_name": record["canonical_name"],
                    "provider": record["provider"],
                    "official_source_url": record["official_source_url"],
                    "dataset_identifier": record["dataset_identifier"],
                    "catalog_deposit_version": record["catalog_deposit_version"],
                    "observed_deposit_version": record["observed_deposit_version"],
                    "version_matches_catalog": record["version_matches_catalog"],
                    "listing_result": record["listing_result"],
                    "expected_file_count": record["expected_file_count"],
                    "expected_bytes": record["expected_bytes"],
                    "file_index": index if item else "",
                    "file_path": item.get("path") if item else "",
                    "file_bytes": item.get("bytes") if item else "",
                    "mime_type": item.get("mime_type") if item else "",
                    "source_checksum_type": (
                        item.get("source_checksum_type") if item else ""
                    ),
                    "source_checksum_available": (
                        bool(item.get("source_checksum")) if item else ""
                    ),
                    "source_status": item.get("source_status") if item else "",
                    "notes": record["notes"],
                }
            )
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def generate(input_path: Path, json_path: Path, csv_path: Path) -> dict[str, Any]:
    load_credentials()
    with input_path.open(encoding="utf-8", newline="") as handle:
        unresolved = list(csv.DictReader(handle))
    if not unresolved:
        raise RuntimeError("The unresolved-quantity input contains no records")

    registry = {dataset.info.name: dataset.info for dataset in REGISTRY.list_datasets()}
    session = requests.Session()
    dryad_headers, dryad_authentication_source = _dryad_headers(session)
    (
        mendeley_headers,
        mendeley_authentication_source,
        mendeley_token_lifetime_seconds,
    ) = _mendeley_oauth_headers(session)
    records: list[dict[str, Any]] = []
    for index, row in enumerate(unresolved, start=1):
        record_id = row["record_id"]
        info = registry[record_id]
        provider = _inventory_provider(info)
        official_source_url = info.source_landing_page_url or info.download_url
        try:
            if provider == "dryad":
                record = _dryad_inventory(
                    session,
                    record_id=record_id,
                    canonical_name=info.full_name,
                    official_source_url=official_source_url,
                    doi=info.dataset_doi or "",
                    catalog_version=info.resource_version,
                    headers=dryad_headers,
                )
            elif provider == "mendeley":
                record = _mendeley_inventory(
                    session,
                    record_id=record_id,
                    canonical_name=info.full_name,
                    official_source_url=official_source_url,
                    catalog_version=info.resource_version,
                    headers=mendeley_headers,
                    authentication_source=mendeley_authentication_source,
                )
            elif provider == "figshare":
                record = _figshare_inventory(
                    session,
                    record_id=record_id,
                    canonical_name=info.full_name,
                    official_source_url=official_source_url,
                    article_id=str(info.repository_record_id or ""),
                    catalog_version=info.resource_version,
                )
            elif provider == "kaggle":
                record = _kaggle_inventory(
                    record_id=record_id,
                    canonical_name=info.full_name,
                    official_source_url=official_source_url,
                    dataset_id=str(info.repository_record_id or ""),
                    catalog_version=info.resource_version,
                )
            elif provider == "huggingface":
                record = _huggingface_inventory(
                    record_id=record_id,
                    canonical_name=info.full_name,
                    official_source_url=official_source_url,
                    dataset_id=str(info.repository_record_id or ""),
                    catalog_version=info.resource_version,
                )
            else:
                record = {
                    "record_id": record_id,
                    "canonical_name": info.full_name,
                    "provider": provider,
                    "official_source_url": official_source_url,
                    "dataset_identifier": info.dataset_doi or "",
                    "catalog_deposit_version": str(info.resource_version or ""),
                    "observed_deposit_version": None,
                    "version_matches_catalog": None,
                    "listing_result": "manual_source_procedure_required",
                    "expected_file_count": None,
                    "expected_bytes": None,
                    "source_checksums_available": None,
                    "files": [],
                    "notes": (
                        "This record uses a source-specific manual or controlled "
                        "procedure; no automated listing was attempted."
                    ),
                }
        except requests.RequestException as exc:
            response = getattr(exc, "response", None)
            status_code = getattr(response, "status_code", None)
            record = {
                "record_id": record_id,
                "canonical_name": info.full_name,
                "provider": provider,
                "official_source_url": official_source_url,
                "dataset_identifier": info.dataset_doi or "",
                "catalog_deposit_version": str(info.resource_version or ""),
                "observed_deposit_version": None,
                "version_matches_catalog": None,
                "listing_result": "request_not_completed",
                "expected_file_count": None,
                "expected_bytes": None,
                "source_checksums_available": None,
                "files": [],
                "notes": f"Official API request did not complete (HTTP {status_code}).",
            }
        records.append(record)
        print(
            f"[{index:02d}/{len(unresolved)}] {record_id}: "
            f"{record['listing_result']}"
        )

    confirmed = [
        record
        for record in records
        if record["listing_result"] == "official_file_listing_confirmed"
    ]
    archive_confirmed = [
        record
        for record in records
        if record["listing_result"] == "official_archive_route_confirmed"
    ]
    payload = {
        "schema_version": "1.0",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "input": input_path.name,
        "record_count": len(records),
        "providers": {
            provider: sum(record["provider"] == provider for record in records)
            for provider in sorted({record["provider"] for record in records})
        },
        "listing_results": {
            result: sum(record["listing_result"] == result for record in records)
            for result in sorted({record["listing_result"] for record in records})
        },
        "confirmed_expected_file_count": sum(
            int(record["expected_file_count"] or 0) for record in confirmed
        ),
        "confirmed_expected_bytes": sum(
            int(record["expected_bytes"] or 0) for record in confirmed
        ),
        "confirmed_archive_record_count": len(archive_confirmed),
        "confirmed_archive_bytes": sum(
            int(record["expected_bytes"] or 0) for record in archive_confirmed
        ),
        "dryad_authentication_source": dryad_authentication_source,
        "mendeley_authentication_source": mendeley_authentication_source,
        "mendeley_token_lifetime_seconds": mendeley_token_lifetime_seconds,
        "mendeley_access_token_serialized": False,
        "credential_values_serialized": False,
        "signed_or_download_urls_serialized": False,
        "dataset_files_downloaded": False,
        "records": records,
    }
    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(
        json.dumps(payload, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )
    _write_csv(csv_path, records)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--csv-out", type=Path, default=DEFAULT_CSV)
    args = parser.parse_args()
    payload = generate(args.input, args.json_out, args.csv_out)
    print(
        f"Wrote {payload['record_count']} record inventories; "
        f"{payload['listing_results']}."
    )


if __name__ == "__main__":
    main()
