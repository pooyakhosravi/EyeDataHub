"""Download, verify, inventory, and delete deposits lacking a primary quantity.

Files are acquired through official version-specific repository routes. Source
checksums are compared when supplied. Archive members and simple tabular
structures are inventoried without extracting the deposit. Each local file is
deleted immediately after its inventory is recorded. The resumable public
report contains no credentials, signed URLs, or local paths.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tarfile
import time
import zipfile
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from typing import Any, Iterable
from urllib.parse import quote, urljoin
from xml.etree import ElementTree

import requests

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from hub.audit.inventory_unresolved_quantity_deposits import (  # noqa: E402
    API_ROOT,
    MENDELEY_BROWSER_ROOT,
    _dryad_headers,
    _get_json,
)


DEFAULT_INVENTORY = (
    ROOT / "hub" / "audit" / "unresolved_quantity_deposit_inventory_2026-08-02.json"
)
DEFAULT_OUTPUT = (
    ROOT / "hub" / "audit" / "unresolved_quantity_content_inventory_2026-08-02.json"
)
DEFAULT_WORK_DIR = ROOT / ".audit-work" / "unresolved-quantity"
ARCHIVE_SUFFIXES = (
    ".tar.gz",
    ".tar.bz2",
    ".tar.xz",
    ".tgz",
    ".tbz2",
    ".txz",
    ".tar",
    ".zip",
)
TABULAR_SUFFIXES = {".csv", ".tsv", ".txt"}


def _suffix(path: str) -> str:
    lowered = path.lower()
    for suffix in (
        ".fastq.gz",
        ".fq.gz",
        ".nii.gz",
        ".vcf.gz",
        ".csv.gz",
        ".tsv.gz",
        *ARCHIVE_SUFFIXES,
    ):
        if lowered.endswith(suffix):
            return suffix
    return PurePosixPath(lowered).suffix or "[none]"


def _safe_name(path: str, index: int) -> str:
    name = PurePosixPath(path).name or f"file-{index}"
    safe = "".join(character if character.isalnum() or character in ".-_" else "_" for character in name)
    return f"{index:04d}-{safe}"


def _summarize_members(members: Iterable[tuple[str, int]]) -> dict[str, Any]:
    extension_counts: Counter[str] = Counter()
    top_level_counts: Counter[str] = Counter()
    total_bytes = 0
    file_count = 0
    for raw_name, size in members:
        name = raw_name.replace("\\", "/").lstrip("/")
        if not name or name.endswith("/"):
            continue
        file_count += 1
        total_bytes += int(size or 0)
        extension_counts[_suffix(name)] += 1
        parts = PurePosixPath(name).parts
        if parts:
            top_level_counts[parts[0]] += 1
    return {
        "content_file_count": file_count,
        "content_uncompressed_bytes": total_bytes,
        "content_extensions": dict(sorted(extension_counts.items())),
        "top_level_entries": dict(top_level_counts.most_common(50)),
    }


def _inspect_zip(path: Path) -> dict[str, Any]:
    with zipfile.ZipFile(path) as archive:
        members = [(item.filename, item.file_size) for item in archive.infolist()]
        encrypted = sum(bool(item.flag_bits & 0x1) for item in archive.infolist())
    return {"format": "zip", "encrypted_entries": encrypted, **_summarize_members(members)}


def _inspect_tar(path: Path) -> dict[str, Any]:
    with tarfile.open(path, mode="r:*") as archive:
        members = [(item.name, item.size) for item in archive if item.isfile()]
    return {"format": "tar", **_summarize_members(members)}


def _inspect_xlsx(path: Path) -> dict[str, Any]:
    namespace = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
    sheets: list[dict[str, Any]] = []
    with zipfile.ZipFile(path) as archive:
        worksheet_names = sorted(
            name
            for name in archive.namelist()
            if name.startswith("xl/worksheets/sheet") and name.endswith(".xml")
        )
        for worksheet_name in worksheet_names:
            rows = 0
            max_columns = 0
            with archive.open(worksheet_name) as handle:
                for _, element in ElementTree.iterparse(handle, events=("end",)):
                    if element.tag == f"{namespace}row":
                        rows += 1
                        max_columns = max(
                            max_columns,
                            sum(child.tag == f"{namespace}c" for child in element),
                        )
                        element.clear()
            sheets.append(
                {
                    "worksheet_part": PurePosixPath(worksheet_name).name,
                    "rows_including_header": rows,
                    "maximum_populated_columns": max_columns,
                }
            )
    return {"format": "xlsx", "worksheets": sheets}


def _inspect_delimited(path: Path, suffix: str) -> dict[str, Any]:
    delimiter = "\t" if suffix == ".tsv" else ","
    nonempty_rows = 0
    maximum_columns = 0
    with path.open("r", encoding="utf-8-sig", errors="replace", newline="") as handle:
        if suffix == ".txt":
            for line in handle:
                if line.strip():
                    nonempty_rows += 1
            return {"format": "text", "nonempty_lines": nonempty_rows}
        reader = csv.reader(handle, delimiter=delimiter)
        for row in reader:
            if any(cell.strip() for cell in row):
                nonempty_rows += 1
                maximum_columns = max(maximum_columns, len(row))
    return {
        "format": "delimited_text",
        "rows_including_header": nonempty_rows,
        "maximum_columns": maximum_columns,
    }


def _inspect_gzip(path: Path, suffix: str) -> dict[str, Any]:
    result: dict[str, Any] = {"format": "gzip", "contained_suffix": suffix[:-3]}
    if suffix not in {".csv.gz", ".tsv.gz"}:
        return result
    delimiter = "\t" if suffix == ".tsv.gz" else ","
    rows = 0
    maximum_columns = 0
    with gzip.open(path, "rt", encoding="utf-8-sig", errors="replace", newline="") as handle:
        reader = csv.reader(handle, delimiter=delimiter)
        for row in reader:
            if any(cell.strip() for cell in row):
                rows += 1
                maximum_columns = max(maximum_columns, len(row))
    result.update(rows_including_header=rows, maximum_columns=maximum_columns)
    return result


def _inspect_file(path: Path, source_path: str) -> dict[str, Any]:
    suffix = _suffix(source_path)
    try:
        if suffix == ".xlsx":
            return _inspect_xlsx(path)
        if suffix == ".zip":
            return _inspect_zip(path)
        if suffix in ARCHIVE_SUFFIXES:
            return _inspect_tar(path)
        if suffix in TABULAR_SUFFIXES:
            return _inspect_delimited(path, suffix)
        if suffix.endswith(".gz"):
            return _inspect_gzip(path, suffix)
        return {"format": "single_file", "content_suffix": suffix}
    except (OSError, ValueError, EOFError, tarfile.TarError, zipfile.BadZipFile) as exc:
        return {
            "format": "inspection_not_completed",
            "content_suffix": suffix,
            "reason": type(exc).__name__,
        }


def _hash_name(source_type: str | None) -> str | None:
    normalized = (source_type or "").strip().lower().replace("-", "")
    return normalized if normalized in hashlib.algorithms_available else None


def _download_file(
    session: requests.Session,
    *,
    url: str,
    headers: dict[str, str],
    destination: Path,
    expected_bytes: int,
    source_checksum_type: str | None,
    source_checksum: str | None,
) -> dict[str, Any]:
    part = destination.with_suffix(destination.suffix + ".part")
    transferred = 0
    for attempt in range(7):
        existing = part.stat().st_size if part.exists() else 0
        request_headers = dict(headers)
        if existing:
            request_headers["Range"] = f"bytes={existing}-"
        try:
            response = session.get(
                url,
                headers=request_headers,
                stream=True,
                timeout=(30, 300),
            )
            if response.status_code == 401:
                raise PermissionError("Dryad bearer token expired during transfer.")
            if response.status_code == 429 or response.status_code >= 500:
                if attempt == 6:
                    response.raise_for_status()
                retry_after = response.headers.get("Retry-After", "").strip()
                delay = float(retry_after) if retry_after.isdigit() else 2**attempt
                response.close()
                print(f"      source throttled the request; retrying in {delay:.0f} s")
                time.sleep(min(delay, 120))
                continue
            response.raise_for_status()
            append = existing > 0 and response.status_code == 206
            if not append:
                existing = 0
            mode = "ab" if append else "wb"
            transferred = existing
            last_report = time.monotonic()
            with part.open(mode) as handle:
                for chunk in response.iter_content(chunk_size=8 * 1024 * 1024):
                    if not chunk:
                        continue
                    handle.write(chunk)
                    transferred += len(chunk)
                    if time.monotonic() - last_report >= 30:
                        print(
                            f"      {transferred / 1_000_000_000:.2f} GB transferred"
                        )
                        last_report = time.monotonic()
            response.close()
            break
        except requests.RequestException:
            if attempt == 6:
                raise
            delay = 2**attempt
            print(f"      transfer interrupted; resuming in {delay} s")
            time.sleep(delay)
    else:
        raise AssertionError("unreachable")
    if transferred != expected_bytes:
        raise RuntimeError(
            f"Transferred {transferred} bytes; expected {expected_bytes} bytes."
        )
    part.replace(destination)

    local_sha256 = hashlib.sha256()
    source_hasher_name = _hash_name(source_checksum_type)
    source_hasher = hashlib.new(source_hasher_name) if source_hasher_name else None
    with destination.open("rb") as handle:
        for chunk in iter(lambda: handle.read(8 * 1024 * 1024), b""):
            local_sha256.update(chunk)
            if source_hasher is not None:
                source_hasher.update(chunk)
    source_matched = None
    if source_checksum and source_hasher is not None:
        source_matched = source_hasher.hexdigest().lower() == source_checksum.lower()
        if not source_matched:
            raise RuntimeError("The acquired file did not match the source checksum.")
    return {
        "acquired_bytes": transferred,
        "local_sha256": local_sha256.hexdigest(),
        "source_checksum_matched": source_matched,
    }


def _current_dryad_files(
    session: requests.Session,
    *,
    doi: str,
    expected_version: str,
    headers: dict[str, str],
) -> list[dict[str, Any]]:
    identifier = quote(f"doi:{doi}", safe="")
    dataset_response = _get_json(
        session,
        f"{API_ROOT}/api/v2/datasets/{identifier}",
        headers=headers,
    )
    dataset_response.raise_for_status()
    version_href = (
        dataset_response.json().get("_links", {}).get("stash:version", {}).get("href")
    )
    version_response = _get_json(
        session,
        urljoin(API_ROOT, version_href),
        headers=headers,
    )
    version_response.raise_for_status()
    version = version_response.json()
    observed_version = str(version.get("versionNumber") or "")
    if observed_version != expected_version:
        raise RuntimeError(
            f"Dryad version changed from catalog v{expected_version} to v{observed_version}."
        )
    files_href = version.get("_links", {}).get("stash:files", {}).get("href")
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
        files.extend(payload.get("_embedded", {}).get("stash:files", []))
        next_href = payload.get("_links", {}).get("next", {}).get("href")
    return files


def _figshare_headers() -> dict[str, str]:
    headers = {"Accept": "application/json"}
    token = os.environ.get("FIGSHARE_TOKEN", "").strip()
    if token:
        headers["Authorization"] = f"token {token}"
    return headers


def _current_figshare_files(
    session: requests.Session,
    *,
    article_id: str,
    expected_version: str,
    headers: dict[str, str],
) -> list[dict[str, Any]]:
    response = _get_json(
        session,
        f"https://api.figshare.com/v2/articles/{article_id}",
        headers=headers,
    )
    response.raise_for_status()
    payload = response.json()
    observed_version = str(payload.get("version") or "")
    if expected_version and observed_version != expected_version:
        raise RuntimeError(
            "Figshare version changed from catalog "
            f"v{expected_version} to v{observed_version}."
        )
    return list(payload.get("files") or [])


def _write_report(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(payload, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )
    temporary.replace(path)


def _process_record(
    session: requests.Session,
    *,
    record: dict[str, Any],
    headers: dict[str, str],
    work_dir: Path,
) -> dict[str, Any]:
    record_id = record["record_id"]
    record_dir = (work_dir / record_id).resolve()
    if not record_dir.is_relative_to(work_dir.resolve()):
        raise RuntimeError("Record work directory escaped the configured audit directory.")
    record_dir.mkdir(parents=True, exist_ok=True)
    live_files = _current_dryad_files(
        session,
        doi=record["dataset_identifier"],
        expected_version=record["catalog_deposit_version"],
        headers=headers,
    )
    expected = {item["path"]: item for item in record["files"]}
    if {item.get("path") for item in live_files} != set(expected):
        raise RuntimeError("The current official file listing differs from the inventory.")

    file_results: list[dict[str, Any]] = []
    content_extensions: Counter[str] = Counter()
    acquired_bytes = 0
    matched_checksums = 0
    for index, item in enumerate(live_files, start=1):
        source_path = str(item.get("path") or f"file-{index}")
        expected_item = expected[source_path]
        destination = (record_dir / _safe_name(source_path, index)).resolve()
        if not destination.is_relative_to(record_dir):
            raise RuntimeError("Dryad file path escaped the record work directory.")
        download_href = item.get("_links", {}).get("stash:download", {}).get("href")
        if not download_href:
            raise RuntimeError(f"Dryad exposed no download route for file {index}.")
        print(
            f"    [{index}/{len(live_files)}] {source_path} "
            f"({int(expected_item['bytes']) / 1_000_000:.1f} MB)"
        )
        transfer = _download_file(
            session,
            url=urljoin(API_ROOT, download_href),
            headers=headers,
            destination=destination,
            expected_bytes=int(expected_item["bytes"]),
            source_checksum_type=expected_item.get("source_checksum_type"),
            source_checksum=expected_item.get("source_checksum"),
        )
        inspection = _inspect_file(destination, source_path)
        acquired_bytes += transfer["acquired_bytes"]
        matched_checksums += transfer["source_checksum_matched"] is True
        if "content_extensions" in inspection:
            content_extensions.update(inspection["content_extensions"])
        else:
            content_extensions[_suffix(source_path)] += 1
        file_results.append(
            {
                "file_index": index,
                "source_path": source_path,
                "expected_bytes": int(expected_item["bytes"]),
                **transfer,
                "inspection": inspection,
                "temporary_file_deleted": True,
            }
        )
        destination.unlink()

    try:
        record_dir.rmdir()
    except OSError:
        pass
    return {
        "record_id": record_id,
        "canonical_name": record["canonical_name"],
        "provider": "dryad",
        "official_source_url": record["official_source_url"],
        "dataset_identifier": record["dataset_identifier"],
        "deposit_version": record["catalog_deposit_version"],
        "inspection_date": datetime.now(timezone.utc).date().isoformat(),
        "acquisition_method": "official_dryad_per_file_api",
        "download_completed": True,
        "expected_file_count": record["expected_file_count"],
        "acquired_file_count": len(file_results),
        "expected_bytes": record["expected_bytes"],
        "acquired_bytes": acquired_bytes,
        "source_checksums_available": record["source_checksums_available"],
        "source_checksums_matched": matched_checksums,
        "content_extensions": dict(sorted(content_extensions.items())),
        "files": file_results,
        "temporary_dataset_files_retained": False,
        "credentials_serialized": False,
        "download_urls_serialized": False,
    }


def _process_figshare_record(
    session: requests.Session,
    *,
    record: dict[str, Any],
    headers: dict[str, str],
    work_dir: Path,
) -> dict[str, Any]:
    record_id = record["record_id"]
    record_dir = (work_dir / record_id).resolve()
    if not record_dir.is_relative_to(work_dir.resolve()):
        raise RuntimeError("Record work directory escaped the configured audit directory.")
    record_dir.mkdir(parents=True, exist_ok=True)
    live_files = _current_figshare_files(
        session,
        article_id=str(record["dataset_identifier"]),
        expected_version=str(record["catalog_deposit_version"] or ""),
        headers=headers,
    )
    if not live_files and int(record.get("expected_file_count") or 0) == 0:
        try:
            record_dir.rmdir()
        except OSError:
            pass
        return {
            "record_id": record_id,
            "canonical_name": record["canonical_name"],
            "provider": "figshare",
            "official_source_url": record["official_source_url"],
            "dataset_identifier": record["dataset_identifier"],
            "deposit_version": record["catalog_deposit_version"],
            "inspection_date": datetime.now(timezone.utc).date().isoformat(),
            "acquisition_method": "official_figshare_per_file_api",
            "download_completed": True,
            "deposit_contains_no_files": True,
            "expected_file_count": 0,
            "acquired_file_count": 0,
            "expected_bytes": 0,
            "acquired_bytes": 0,
            "source_checksums_available": 0,
            "source_checksums_matched": 0,
            "content_extensions": {},
            "files": [],
            "temporary_dataset_files_retained": False,
            "credentials_serialized": False,
            "download_urls_serialized": False,
        }
    expected = {item["path"]: item for item in record["files"]}
    if {item.get("name") for item in live_files} != set(expected):
        raise RuntimeError("The current official Figshare listing differs from the inventory.")

    file_results: list[dict[str, Any]] = []
    content_extensions: Counter[str] = Counter()
    acquired_bytes = 0
    matched_checksums = 0
    for index, item in enumerate(live_files, start=1):
        source_path = str(item.get("name") or f"file-{index}")
        expected_item = expected[source_path]
        destination = (record_dir / _safe_name(source_path, index)).resolve()
        if not destination.is_relative_to(record_dir):
            raise RuntimeError("Figshare file path escaped the record work directory.")
        download_url = item.get("download_url")
        if not download_url:
            raise RuntimeError(f"Figshare exposed no download route for file {index}.")
        checksum = item.get("supplied_md5") or item.get("computed_md5")
        print(
            f"    [{index}/{len(live_files)}] {source_path} "
            f"({int(expected_item['bytes']) / 1_000_000:.1f} MB)"
        )
        transfer = _download_file(
            session,
            url=download_url,
            headers=headers,
            destination=destination,
            expected_bytes=int(expected_item["bytes"]),
            source_checksum_type="md5" if checksum else None,
            source_checksum=checksum,
        )
        inspection = _inspect_file(destination, source_path)
        acquired_bytes += transfer["acquired_bytes"]
        matched_checksums += transfer["source_checksum_matched"] is True
        if "content_extensions" in inspection:
            content_extensions.update(inspection["content_extensions"])
        else:
            content_extensions[_suffix(source_path)] += 1
        file_results.append(
            {
                "file_index": index,
                "source_path": source_path,
                "expected_bytes": int(expected_item["bytes"]),
                **transfer,
                "inspection": inspection,
                "temporary_file_deleted": True,
            }
        )
        destination.unlink()

    try:
        record_dir.rmdir()
    except OSError:
        pass
    return {
        "record_id": record_id,
        "canonical_name": record["canonical_name"],
        "provider": "figshare",
        "official_source_url": record["official_source_url"],
        "dataset_identifier": record["dataset_identifier"],
        "deposit_version": record["catalog_deposit_version"],
        "inspection_date": datetime.now(timezone.utc).date().isoformat(),
        "acquisition_method": "official_figshare_per_file_api",
        "download_completed": True,
        "deposit_contains_no_files": False,
        "expected_file_count": record["expected_file_count"],
        "acquired_file_count": len(file_results),
        "expected_bytes": record["expected_bytes"],
        "acquired_bytes": acquired_bytes,
        "source_checksums_available": record["source_checksums_available"],
        "source_checksums_matched": matched_checksums,
        "content_extensions": dict(sorted(content_extensions.items())),
        "files": file_results,
        "temporary_dataset_files_retained": False,
        "credentials_serialized": False,
        "download_urls_serialized": False,
    }


def _process_kaggle_record(
    *,
    record: dict[str, Any],
    work_dir: Path,
) -> dict[str, Any]:
    from kaggle.api.kaggle_api_extended import KaggleApi

    record_id = record["record_id"]
    record_dir = (work_dir / record_id).resolve()
    if not record_dir.is_relative_to(work_dir.resolve()):
        raise RuntimeError("Record work directory escaped the configured audit directory.")
    record_dir.mkdir(parents=True, exist_ok=True)
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files(
        record["dataset_identifier"],
        path=str(record_dir),
        force=True,
        quiet=True,
        unzip=False,
    )
    archives = list(record_dir.glob("*.zip"))
    if len(archives) != 1:
        raise RuntimeError("The Kaggle client did not produce one dataset archive.")
    archive_path = archives[0].resolve()
    if not archive_path.is_relative_to(record_dir):
        raise RuntimeError("Kaggle archive escaped the record work directory.")
    with zipfile.ZipFile(archive_path) as archive:
        members = {
            item.filename.replace("\\", "/"): item.file_size
            for item in archive.infolist()
            if not item.is_dir()
        }
        corrupt_member = archive.testzip()
    if corrupt_member:
        raise RuntimeError("The Kaggle archive failed its ZIP integrity check.")
    expected = {
        str(item["path"]).replace("\\", "/"): int(item.get("bytes") or 0)
        for item in record["files"]
    }
    if members != expected:
        raise RuntimeError("The Kaggle archive contents differ from the API inventory.")
    local_sha256 = hashlib.sha256()
    with archive_path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(8 * 1024 * 1024), b""):
            local_sha256.update(chunk)
    transferred_bytes = archive_path.stat().st_size
    inspection = _inspect_zip(archive_path)
    archive_path.unlink()
    try:
        record_dir.rmdir()
    except OSError:
        pass
    return {
        "record_id": record_id,
        "canonical_name": record["canonical_name"],
        "provider": "kaggle",
        "official_source_url": record["official_source_url"],
        "dataset_identifier": record["dataset_identifier"],
        "deposit_version": record["catalog_deposit_version"],
        "inspection_date": datetime.now(timezone.utc).date().isoformat(),
        "acquisition_method": "official_kaggle_client_dataset_archive",
        "download_completed": True,
        "expected_file_count": record["expected_file_count"],
        "acquired_file_count": len(members),
        "expected_bytes": record["expected_bytes"],
        "acquired_bytes": sum(members.values()),
        "transferred_archive_bytes": transferred_bytes,
        "source_checksums_available": 0,
        "source_checksums_matched": 0,
        "local_archive_sha256": local_sha256.hexdigest(),
        "content_extensions": inspection["content_extensions"],
        "archive_inspection": inspection,
        "files": [],
        "temporary_dataset_files_retained": False,
        "credentials_serialized": False,
        "download_urls_serialized": False,
    }


def _download_mendeley_archive(
    *,
    dataset_id: str,
    version: str,
    destination: Path,
    expected_bytes: int,
) -> dict[str, Any]:
    """Download one official Mendeley Download All archive without exposing redirects."""
    curl = shutil.which("curl")
    if not curl:
        raise RuntimeError("curl is required for the official Mendeley archive route.")
    part = destination.with_suffix(destination.suffix + ".part")
    url = (
        f"{MENDELEY_BROWSER_ROOT}/public-api/zip/"
        f"{quote(dataset_id, safe='')}/download/{quote(version, safe='')}"
    )
    command = [
        curl,
        "--location",
        "--fail",
        "--silent",
        "--show-error",
        "--retry",
        "6",
        "--retry-all-errors",
        "--retry-delay",
        "2",
        "--connect-timeout",
        "30",
        "--speed-limit",
        "1024",
        "--speed-time",
        "300",
        "--continue-at",
        "-",
        "--output",
        str(part),
        url,
    ]
    process = subprocess.Popen(
        command,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
        text=True,
    )
    last_report = time.monotonic()
    while process.poll() is None:
        time.sleep(2)
        if time.monotonic() - last_report >= 30:
            transferred = part.stat().st_size if part.exists() else 0
            print(
                "      "
                f"{transferred / 1_000_000_000:.2f} of "
                f"{expected_bytes / 1_000_000_000:.2f} GB transferred",
                flush=True,
            )
            last_report = time.monotonic()
    stderr = process.stderr.read() if process.stderr is not None else ""
    if process.returncode:
        # Curl errors can contain a temporary redirect URL. Do not copy stderr
        # into the exception or public report.
        raise RuntimeError(
            f"The official Mendeley archive request failed (curl exit "
            f"{process.returncode}; diagnostic length {len(stderr)})."
        )
    transferred = part.stat().st_size if part.exists() else 0
    if transferred != expected_bytes:
        raise RuntimeError(
            f"Transferred {transferred} bytes; expected {expected_bytes} bytes."
        )
    part.replace(destination)
    local_sha256 = hashlib.sha256()
    with destination.open("rb") as handle:
        for chunk in iter(lambda: handle.read(8 * 1024 * 1024), b""):
            local_sha256.update(chunk)
    return {
        "transferred_archive_bytes": transferred,
        "local_archive_sha256": local_sha256.hexdigest(),
    }


def _process_mendeley_record(
    *,
    record: dict[str, Any],
    work_dir: Path,
) -> dict[str, Any]:
    record_id = record["record_id"]
    record_dir = (work_dir / record_id).resolve()
    if not record_dir.is_relative_to(work_dir.resolve()):
        raise RuntimeError("Record work directory escaped the configured audit directory.")
    record_dir.mkdir(parents=True, exist_ok=True)
    archive_path = (record_dir / "official-download-all.zip").resolve()
    if not archive_path.is_relative_to(record_dir):
        raise RuntimeError("Mendeley archive escaped the record work directory.")
    expected_bytes = int(record["expected_bytes"])
    transfer = _download_mendeley_archive(
        dataset_id=str(record["dataset_identifier"]),
        version=str(record["catalog_deposit_version"]),
        destination=archive_path,
        expected_bytes=expected_bytes,
    )
    with zipfile.ZipFile(archive_path) as archive:
        corrupt_member = archive.testzip()
    if corrupt_member:
        raise RuntimeError("The Mendeley archive failed its ZIP integrity check.")
    inspection = _inspect_zip(archive_path)
    archive_path.unlink()
    try:
        record_dir.rmdir()
    except OSError:
        pass
    return {
        "record_id": record_id,
        "canonical_name": record["canonical_name"],
        "provider": "mendeley",
        "official_source_url": record["official_source_url"],
        "dataset_identifier": record["dataset_identifier"],
        "deposit_version": record["catalog_deposit_version"],
        "inspection_date": datetime.now(timezone.utc).date().isoformat(),
        "acquisition_method": "official_mendeley_browser_download_all",
        "download_completed": True,
        "archive_integrity_confirmed": True,
        "expected_file_count": None,
        "acquired_file_count": inspection["content_file_count"],
        "expected_bytes": expected_bytes,
        "acquired_bytes": transfer["transferred_archive_bytes"],
        "archive_uncompressed_bytes": inspection["content_uncompressed_bytes"],
        "source_checksums_available": 0,
        "source_checksums_matched": 0,
        "local_archive_sha256": transfer["local_archive_sha256"],
        "content_extensions": inspection["content_extensions"],
        "archive_inspection": inspection,
        "files": [],
        "temporary_dataset_files_retained": False,
        "credentials_serialized": False,
        "download_urls_serialized": False,
    }
def run(
    *,
    inventory_path: Path,
    output_path: Path,
    work_dir: Path,
    max_record_bytes: int | None,
    record_ids: set[str],
    providers: set[str] | None = None,
) -> dict[str, Any]:
    inventory = json.loads(inventory_path.read_text(encoding="utf-8"))
    selected = [
        record
        for record in inventory["records"]
        if (
            (
                record["provider"] in {"dryad", "figshare", "kaggle"}
                and record["listing_result"] == "official_file_listing_confirmed"
            )
            or (
                record["provider"] == "mendeley"
                and record["listing_result"] == "official_archive_route_confirmed"
            )
        )
        and (not providers or record["provider"] in providers)
        and (not record_ids or record["record_id"] in record_ids)
        and (
            max_record_bytes is None
            or int(record["expected_bytes"] or 0) <= max_record_bytes
        )
    ]
    selected.sort(key=lambda record: int(record.get("expected_bytes") or 0))
    missing = record_ids - {record["record_id"] for record in selected}
    if missing:
        raise RuntimeError(f"Requested records were not eligible: {sorted(missing)}")

    if output_path.exists():
        report = json.loads(output_path.read_text(encoding="utf-8"))
    else:
        report = {
            "schema_version": "1.0",
            "generated_at_utc": None,
            "source_inventory": inventory_path.name,
            "credential_values_serialized": False,
            "signed_or_download_urls_serialized": False,
            "temporary_dataset_files_retained": False,
            "records": [],
        }
    completed = {
        record["record_id"]: record
        for record in report["records"]
        if record.get("download_completed")
    }
    source_inventories = set(report.get("source_inventories") or [])
    if report.get("source_inventory"):
        source_inventories.add(report["source_inventory"])
    source_inventories.add(inventory_path.name)
    report["source_inventories"] = sorted(source_inventories)
    session = requests.Session()
    headers: dict[str, str] = {}
    authentication_source = report.get("dryad_authentication_source", "not_used")
    pending_dryad = any(
        record["provider"] == "dryad" and record["record_id"] not in completed
        for record in selected
    )
    if pending_dryad:
        headers, authentication_source = _dryad_headers(session)
    figshare_headers = _figshare_headers()
    report["dryad_authentication_source"] = authentication_source
    work_dir.mkdir(parents=True, exist_ok=True)

    for index, record in enumerate(selected, start=1):
        record_id = record["record_id"]
        if record_id in completed:
            print(f"[{index:02d}/{len(selected)}] {record_id}: already completed")
            continue
        print(
            f"[{index:02d}/{len(selected)}] {record_id}: "
            f"{int(record['expected_bytes']) / 1_000_000_000:.3f} GB"
        )
        try:
            if record["provider"] == "dryad":
                result = _process_record(
                    session,
                    record=record,
                    headers=headers,
                    work_dir=work_dir,
                )
            elif record["provider"] == "figshare":
                result = _process_figshare_record(
                    session,
                    record=record,
                    headers=figshare_headers,
                    work_dir=work_dir,
                )
            elif record["provider"] == "kaggle":
                result = _process_kaggle_record(record=record, work_dir=work_dir)
            else:
                result = _process_mendeley_record(
                    record=record,
                    work_dir=work_dir,
                )
        except PermissionError:
            if record["provider"] != "dryad":
                raise
            headers, authentication_source = _dryad_headers(session)
            report["dryad_authentication_source"] = authentication_source
            result = _process_record(
                session,
                record=record,
                headers=headers,
                work_dir=work_dir,
            )
        completed[record_id] = result
        report["records"] = [completed[key] for key in sorted(completed)]
        report["generated_at_utc"] = datetime.now(timezone.utc).isoformat()
        report["completed_record_count"] = len(completed)
        report["completed_file_count"] = sum(
            item["acquired_file_count"] for item in completed.values()
        )
        report["completed_bytes"] = sum(
            item["acquired_bytes"] for item in completed.values()
        )
        providers = sorted({item["provider"] for item in completed.values()})
        report["completed_records_by_provider"] = {
            provider: sum(
                item["provider"] == provider for item in completed.values()
            )
            for provider in providers
        }
        report["completed_bytes_by_provider"] = {
            provider: sum(
                item["acquired_bytes"]
                for item in completed.values()
                if item["provider"] == provider
            )
            for provider in providers
        }
        _write_report(output_path, report)
        print("    completed; temporary files deleted")
    mendeley_ready = [
        record
        for record in inventory["records"]
        if record["provider"] == "mendeley"
        and record["listing_result"] == "official_archive_route_confirmed"
    ]
    mendeley_preparing = [
        record["record_id"]
        for record in inventory["records"]
        if record["provider"] == "mendeley"
        and record["listing_result"] == "official_archive_preparing"
    ]
    mendeley_controlled = [
        record["record_id"]
        for record in inventory["records"]
        if record["provider"] == "mendeley"
        and record["listing_result"] == "controlled_access_required"
    ]
    mendeley_source_blocked = [
        record["record_id"]
        for record in inventory["records"]
        if record["provider"] == "mendeley"
        and record["listing_result"] in {"source_blocked", "source_blocked_by_author"}
    ]
    report["mendeley_ready_archive_count"] = len(mendeley_ready)
    report["mendeley_completed_archive_count"] = sum(
        item["provider"] == "mendeley" for item in completed.values()
    )
    report["mendeley_source_archive_preparing_records"] = sorted(
        mendeley_preparing
    )
    report["mendeley_controlled_access_records"] = sorted(mendeley_controlled)
    report["mendeley_source_blocked_records"] = sorted(mendeley_source_blocked)
    report["generated_at_utc"] = datetime.now(timezone.utc).isoformat()
    _write_report(output_path, report)
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inventory", type=Path, default=DEFAULT_INVENTORY)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--work-dir", type=Path, default=DEFAULT_WORK_DIR)
    parser.add_argument("--max-record-bytes", type=int)
    parser.add_argument("--record-id", action="append", default=[])
    parser.add_argument("--provider", action="append", default=[])
    args = parser.parse_args()
    report = run(
        inventory_path=args.inventory,
        output_path=args.output,
        work_dir=args.work_dir,
        max_record_bytes=args.max_record_bytes,
        record_ids=set(args.record_id),
        providers=set(args.provider),
    )
    print(
        f"Content inventory contains {report.get('completed_record_count', 0)} "
        f"completed records and {report.get('completed_bytes', 0)} acquired bytes."
    )


if __name__ == "__main__":
    main()
