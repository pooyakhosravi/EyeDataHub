"""Run sequential download and loader smoke tests without retaining test data.

This audit is intentionally conservative:

* Existing files under the user's EyeDataHub data directory are read only.
* Surgical-video records and records hosted on Kaggle, Hugging Face, Zenodo,
  or Mendeley are excluded from transfer at the caller's request.
* Google Drive routes are checked as landing pages; dataset files are not
  requested.
* Every other preflight-approved transfer runs in its own scratch directory.
  The directory is removed after the structured result has been recorded.
* Manual, controlled, instructions-only, unavailable, and unsupported routes
  are recorded from preflight and are never passed to a downloader.

The parent process invokes one worker process per load or transfer test. This
keeps failures isolated, permits a per-record timeout, and allows interrupted
runs to resume from the JSON output.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import platform
import re
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import urlparse

import requests

from eyedatahub import __version__
from eyedatahub.acquisition import acquire_dataset, preflight_dataset
from eyedatahub.datasets.registry import REGISTRY


EXCLUDED_BACKENDS = {"kaggle", "huggingface", "zenodo", "mendeley"}
IGNORED_DATA_FILES = {".download_complete", "eyedatahub-acquisition-manifest.json"}
IMAGE_SUFFIXES = {
    ".bmp",
    ".gif",
    ".jpeg",
    ".jpg",
    ".png",
    ".ppm",
    ".tif",
    ".tiff",
    ".webp",
}
GOOGLE_HOSTS = {"drive.google.com", "docs.google.com"}
MAX_ROUTE_BODY_BYTES = 262_144
MAX_LOG_TAIL_CHARS = 8_000
USER_AGENT = f"EyeDataHub/{__version__} download-load-verification"
RETRY_ACQUISITION_STATUSES = {
    "failed",
    "transfer_incomplete",
    "not_run_worker_crash",
    "not_run_worker_timeout",
}
RETRY_LOAD_STATUSES = {
    "empty",
    "failed",
    "failed_image_decode",
    "failed_missing_sample_path",
}


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _safe_message(value: Any) -> str:
    """Redact configured credential values from diagnostic text."""
    text = str(value)
    names = {
        "KAGGLE_USERNAME",
        "KAGGLE_KEY",
        "HF_TOKEN",
        "ZENODO_TOKEN",
        "FIGSHARE_TOKEN",
        "MENDELEY_TOKEN",
        "DATAVERSE_TOKEN",
        "PHYSIONET_USERNAME",
        "PHYSIONET_PASSWORD",
    }
    for name in names:
        secret = os.environ.get(name)
        if secret and len(secret) >= 6:
            text = text.replace(secret, "<redacted>")
    return text


def _file_stats(root: Path, *, ignore_audit_files: bool = False) -> dict[str, Any]:
    """Return a metadata-only tree fingerprint without reading file contents."""
    digest = hashlib.sha256()
    count = 0
    size = 0
    errors: list[str] = []
    if not root.exists():
        return {
            "exists": False,
            "file_count": 0,
            "size_bytes": 0,
            "metadata_fingerprint": digest.hexdigest(),
            "errors": [],
        }
    try:
        files = sorted(path for path in root.rglob("*") if path.is_file())
    except Exception as exc:
        return {
            "exists": True,
            "file_count": 0,
            "size_bytes": 0,
            "metadata_fingerprint": "",
            "errors": [f"{type(exc).__name__}: {_safe_message(exc)}"],
        }
    for path in files:
        if ignore_audit_files and path.name in IGNORED_DATA_FILES:
            continue
        try:
            stat = path.stat()
            relative = path.relative_to(root).as_posix()
            digest.update(
                f"{relative}\0{stat.st_size}\0{stat.st_mtime_ns}\n".encode(
                    "utf-8", errors="surrogatepass"
                )
            )
            count += 1
            size += stat.st_size
        except Exception as exc:
            errors.append(f"{path}: {type(exc).__name__}: {_safe_message(exc)}")
    return {
        "exists": True,
        "file_count": count,
        "size_bytes": size,
        "metadata_fingerprint": digest.hexdigest(),
        "errors": errors,
    }


def _existing_snapshot(root: Path) -> dict[str, Any]:
    return {
        "root": str(root.resolve(strict=False)),
        "captured_at_utc": _utc_now(),
        "tree": _file_stats(root),
    }


def _load_smoke(dataset: Any, data_dir: Path) -> dict[str, Any]:
    """Call the public loader and validate one returned sample path."""
    info = dataset.info
    candidates: list[str] = []
    for split in list(info.splits or []) + ["all", "test", "train", "val"]:
        if split and split not in candidates:
            candidates.append(split)

    attempts: list[dict[str, Any]] = []
    saw_empty = False
    started = time.monotonic()
    for split in candidates:
        attempt_started = time.monotonic()
        try:
            samples = dataset.load(data_dir, split=split)
            if not isinstance(samples, list):
                samples = list(samples)
            elapsed = round(time.monotonic() - attempt_started, 3)
            if not samples:
                saw_empty = True
                attempts.append(
                    {
                        "split": split,
                        "status": "empty",
                        "sample_count": 0,
                        "elapsed_seconds": elapsed,
                    }
                )
                continue

            sample = samples[0]
            raw_path = str(getattr(sample, "image_path", "") or "")
            sample_path = Path(raw_path).expanduser() if raw_path else None
            if sample_path is not None and not sample_path.is_absolute():
                relative_candidate = data_dir / sample_path
                if relative_candidate.exists():
                    sample_path = relative_candidate
            path_exists = bool(sample_path and sample_path.exists())
            decode_status = "not_applicable"
            image_mode = None
            image_size = None
            if path_exists and sample_path and sample_path.suffix.lower() in IMAGE_SUFFIXES:
                try:
                    image = dataset.load_image(str(sample_path))
                    image.load()
                    image_mode = image.mode
                    image_size = list(image.size)
                    decode_status = "passed"
                    image.close()
                except Exception as exc:
                    decode_status = f"failed: {type(exc).__name__}: {_safe_message(exc)}"

            status = "passed"
            if not path_exists:
                status = "failed_missing_sample_path"
            elif decode_status.startswith("failed"):
                status = "failed_image_decode"
            return {
                "status": status,
                "implemented": True,
                "split": split,
                "sample_count": len(samples),
                "sample_path": str(sample_path) if sample_path else "",
                "sample_path_exists": path_exists,
                "image_decode_status": decode_status,
                "image_mode": image_mode,
                "image_size": image_size,
                "attempts": attempts,
                "elapsed_seconds": round(time.monotonic() - started, 3),
            }
        except NotImplementedError as exc:
            return {
                "status": "not_implemented",
                "implemented": False,
                "split": split,
                "sample_count": None,
                "sample_path": "",
                "sample_path_exists": None,
                "image_decode_status": "not_applicable",
                "attempts": attempts,
                "error_type": type(exc).__name__,
                "message": _safe_message(exc),
                "elapsed_seconds": round(time.monotonic() - started, 3),
            }
        except Exception as exc:
            attempts.append(
                {
                    "split": split,
                    "status": "failed",
                    "error_type": type(exc).__name__,
                    "message": _safe_message(exc),
                    "elapsed_seconds": round(time.monotonic() - attempt_started, 3),
                }
            )

    return {
        "status": "empty" if saw_empty else "failed",
        "implemented": True,
        "split": None,
        "sample_count": 0 if saw_empty else None,
        "sample_path": "",
        "sample_path_exists": None,
        "image_decode_status": "not_applicable",
        "attempts": attempts,
        "elapsed_seconds": round(time.monotonic() - started, 3),
    }


def _write_json_atomic(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    temporary.replace(path)


def _worker(record_id: str, data_dir: Path, result_path: Path, load_only: bool) -> int:
    payload: dict[str, Any] = {
        "record_id": record_id,
        "worker_started_at_utc": _utc_now(),
        "mode": "load_only" if load_only else "download_and_load",
        "data_dir": str(data_dir.resolve(strict=False)),
        "environment": (
            f"{platform.system()} {platform.release()} | "
            f"Python {platform.python_version()} | EyeDataHub {__version__}"
        ),
    }
    try:
        dataset = REGISTRY.get_dataset(record_id)
        if load_only:
            payload["acquisition"] = {
                "status": "not_run_existing_data_preserved",
                "transfer_started": False,
            }
            payload["load"] = _load_smoke(dataset, data_dir)
        else:
            result = acquire_dataset(
                dataset,
                data_dir,
                dry_run=False,
                force=False,
                checksums=False,
            )
            payload["acquisition"] = result.to_dict()
            dataset_root = dataset.sentinel_path(data_dir).parent
            payload["downloaded_tree"] = _file_stats(
                dataset_root, ignore_audit_files=True
            )
            if result.exit_code == 0 and dataset.is_downloaded(data_dir):
                payload["load"] = _load_smoke(dataset, data_dir)
            else:
                payload["load"] = {
                    "status": "not_run_acquisition_unsuccessful",
                    "implemented": None,
                }
    except BaseException as exc:
        payload["worker_error"] = {
            "error_type": type(exc).__name__,
            "message": _safe_message(exc),
        }
        payload.setdefault(
            "load",
            {"status": "not_run_worker_error", "implemented": None},
        )
    payload["worker_completed_at_utc"] = _utc_now()
    _write_json_atomic(result_path, payload)
    return 0


def _validate_scratch_root(path: Path) -> Path:
    resolved = path.resolve(strict=False)
    anchor = Path(resolved.anchor)
    if resolved == anchor or len(resolved.parts) < 3:
        raise ValueError(f"Scratch path is too broad: {resolved}")
    lowered = resolved.name.lower()
    if "eyedatahub" not in str(resolved).lower() or not lowered.startswith("run_"):
        raise ValueError(
            "Scratch path must be within an EyeDataHub-specific directory and "
            "its final component must start with 'run_'."
        )
    return resolved


def _safe_remove_tree(target: Path, scratch_root: Path) -> None:
    root = _validate_scratch_root(scratch_root)
    resolved = target.resolve(strict=False)
    if resolved == root or root not in resolved.parents:
        raise ValueError(f"Refusing to remove path outside scratch root: {resolved}")
    if target.is_symlink():
        raise ValueError(f"Refusing to recursively remove a symlink: {target}")
    if target.exists():
        shutil.rmtree(target)


def _terminate_owned_process(process: subprocess.Popen[Any]) -> str:
    if process.poll() is not None:
        return "already_exited"
    if os.name == "nt":
        result = subprocess.run(
            ["taskkill", "/PID", str(process.pid), "/T", "/F"],
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )
        return _safe_message((result.stdout or result.stderr).strip())
    process.terminate()
    try:
        process.wait(timeout=10)
        return "terminated"
    except subprocess.TimeoutExpired:
        process.kill()
        process.wait(timeout=10)
        return "killed"


def _invoke_worker(
    *,
    script: Path,
    record_id: str,
    data_dir: Path,
    work_root: Path,
    load_only: bool,
    timeout_seconds: int,
    resume_existing_work: bool = False,
) -> dict[str, Any]:
    work_dir = work_root / record_id
    if work_dir.exists() and not resume_existing_work:
        _safe_remove_tree(work_dir, work_root.parent)
    work_dir.mkdir(parents=True, exist_ok=resume_existing_work)
    result_path = work_dir / "result.json"
    log_path = work_dir / "worker.log"
    result_path.unlink(missing_ok=True)
    command = [
        sys.executable,
        str(script),
        "worker",
        "--record",
        record_id,
        "--data-dir",
        str(data_dir),
        "--result",
        str(result_path),
    ]
    if load_only:
        command.append("--load-only")

    environment = os.environ.copy()
    environment["PYTHONUNBUFFERED"] = "1"
    creationflags = (
        subprocess.CREATE_NEW_PROCESS_GROUP if os.name == "nt" else 0
    )
    timed_out = False
    termination = ""
    started = time.monotonic()
    with log_path.open("w", encoding="utf-8", errors="replace") as log:
        process = subprocess.Popen(
            command,
            cwd=str(Path.cwd()),
            env=environment,
            stdout=log,
            stderr=subprocess.STDOUT,
            creationflags=creationflags,
        )
        try:
            return_code = process.wait(timeout=timeout_seconds)
        except subprocess.TimeoutExpired:
            timed_out = True
            termination = _terminate_owned_process(process)
            return_code = process.wait(timeout=30)

    if result_path.exists():
        payload = json.loads(result_path.read_text(encoding="utf-8"))
    else:
        payload = {
            "record_id": record_id,
            "mode": "load_only" if load_only else "download_and_load",
            "acquisition": {
                "status": "not_run_worker_timeout"
                if timed_out
                else "not_run_worker_crash",
                "transfer_started": not load_only,
            },
            "load": {
                "status": "not_run_worker_timeout"
                if timed_out
                else "not_run_worker_crash",
                "implemented": None,
            },
        }
    payload["worker_return_code"] = return_code
    payload["worker_timed_out"] = timed_out
    payload["worker_termination"] = termination
    payload["worker_wall_seconds"] = round(time.monotonic() - started, 3)
    log_tail = log_path.read_text(encoding="utf-8", errors="replace")[
        -MAX_LOG_TAIL_CHARS:
    ]
    acquisition_status = payload.get("acquisition", {}).get("status", "")
    load_status = payload.get("load", {}).get("status", "")
    if (
        timed_out
        or return_code != 0
        or acquisition_status
        not in {"completed", "already_present", "not_run_existing_data_preserved"}
        or load_status
        not in {"passed", "empty", "not_implemented", "not_run_acquisition_unsuccessful"}
    ):
        payload["worker_log_tail"] = _safe_message(log_tail)

    cleanup_error = ""
    try:
        _safe_remove_tree(work_dir, work_root.parent)
        cleanup_status = "removed"
    except Exception as exc:
        cleanup_status = "failed"
        cleanup_error = f"{type(exc).__name__}: {_safe_message(exc)}"
    payload["scratch_cleanup"] = {
        "status": cleanup_status,
        "error": cleanup_error,
        "path": str(work_dir),
    }
    return payload


def _read_limited_body(response: requests.Response) -> bytes:
    chunks: list[bytes] = []
    total = 0
    for chunk in response.iter_content(chunk_size=16_384):
        if not chunk:
            continue
        remaining = MAX_ROUTE_BODY_BYTES - total
        chunks.append(chunk[:remaining])
        total += min(len(chunk), remaining)
        if total >= MAX_ROUTE_BODY_BYTES:
            break
    return b"".join(chunks)


def _route_check(record_id: str, url: str) -> dict[str, Any]:
    """Check a landing page without following an acquisition link."""
    started = time.monotonic()
    parsed = urlparse(url)
    result: dict[str, Any] = {
        "record_id": record_id,
        "checked_at_utc": _utc_now(),
        "requested_url": url,
        "dataset_transfer_started": False,
        "result": "failed",
    }
    try:
        with requests.get(
            url,
            headers={
                "User-Agent": USER_AGENT,
                "Accept": "text/html,application/xhtml+xml",
            },
            stream=True,
            allow_redirects=True,
            timeout=(20, 30),
        ) as response:
            body = _read_limited_body(response)
            text = body.decode(response.encoding or "utf-8", errors="replace")
            title_match = re.search(
                r"<title[^>]*>(.*?)</title>",
                text,
                flags=re.IGNORECASE | re.DOTALL,
            )
            title = (
                re.sub(r"\s+", " ", title_match.group(1)).strip()
                if title_match
                else ""
            )
            final_host = (urlparse(response.url).hostname or "").lower()
            lowered = text.lower()
            denial_markers = (
                "you need access",
                "request access",
                "file does not exist",
                "unable to access document",
                "sorry, the file you have requested does not exist",
            )
            denied = any(marker in lowered for marker in denial_markers)
            is_google = (parsed.hostname or "").lower() in GOOGLE_HOSTS
            if response.status_code >= 400:
                status = "failed_http"
            elif denied:
                status = "permission_or_missing"
            elif is_google and final_host not in GOOGLE_HOSTS:
                status = "unexpected_redirect"
            elif is_google:
                identifier_match = re.search(
                    r"(?:/d/|/folders/)([-_A-Za-z0-9]+)", url
                )
                identifier = identifier_match.group(1) if identifier_match else ""
                has_drive_context = (
                    "google drive" in lowered
                    or "drive.google.com" in lowered
                    or (identifier and identifier in text)
                )
                status = "passed_landing_page" if has_drive_context else "indeterminate_page"
            else:
                status = "passed_landing_page" if title or len(body) > 256 else "indeterminate_page"

            result.update(
                result=status,
                http_status=response.status_code,
                resolved_url=response.url,
                content_type=response.headers.get("content-type", ""),
                page_title=title,
                landing_page_bytes_read=len(body),
                google_drive_route=is_google,
                limitation=(
                    "Only the landing page was read; no file-download endpoint was requested."
                ),
            )
    except Exception as exc:
        result.update(
            error_type=type(exc).__name__,
            message=_safe_message(exc),
        )
    result["elapsed_seconds"] = round(time.monotonic() - started, 3)
    return result


def _classify(dataset: Any, scratch_root: Path) -> tuple[str, dict[str, Any]]:
    info = dataset.info
    preflight = preflight_dataset(dataset, scratch_root / "preflight")
    if "surgical_video" in set(info.modalities or []):
        return "excluded_surgical_video", preflight
    if info.download_type in EXCLUDED_BACKENDS:
        return "excluded_known_platform", preflight
    if info.download_type == "gdrive":
        return "route_check_only", preflight
    # The Duke loader currently tries a Kaggle mirror before its official
    # direct files. Do not invoke it in a run that explicitly excludes Kaggle.
    if info.name == "duke_chiu_boe":
        return "excluded_known_platform_dependency", preflight
    if not preflight["automation_allowed"]:
        return "preflight_blocked", preflight
    return "eligible_download", preflight


def _row_template(dataset: Any, scratch_root: Path, existing_root: Path) -> dict[str, Any]:
    info = dataset.info
    selection, preflight = _classify(dataset, scratch_root)
    existing_dataset_root = dataset.sentinel_path(existing_root).parent
    existing_stats = _file_stats(existing_dataset_root, ignore_audit_files=True)
    try:
        recognized = dataset.is_downloaded(existing_root)
    except Exception as exc:
        recognized = False
        existing_stats["recognition_error"] = (
            f"{type(exc).__name__}: {_safe_message(exc)}"
        )
    return {
        "record_id": info.name,
        "canonical_name": info.full_name,
        "modalities": list(info.modalities),
        "download_type": info.download_type,
        "selection": selection,
        "selection_reason": {
            "excluded_surgical_video": "record includes the surgical_video modality",
            "excluded_known_platform": (
                "Kaggle, Hugging Face, Zenodo, and Mendeley were excluded by request"
            ),
            "excluded_known_platform_dependency": (
                "the implemented loader attempts an excluded Kaggle mirror"
            ),
            "route_check_only": (
                "Google Drive and related represented routes are checked without transfer"
            ),
            "preflight_blocked": preflight.get("blocked_reason") or "",
            "eligible_download": "preflight permits explicit automated acquisition",
        }[selection],
        "estimated_size_gb": info.size_gb,
        "acquisition_support_before_test": info.acquisition_support,
        "preflight": {
            "status": preflight["status"],
            "exit_code": preflight["exit_code"],
            "automation_allowed": preflight["automation_allowed"],
            "preferred_route_url": preflight["preferred_route_url"],
            "access_friction": preflight["access_friction"],
            "availability_status": preflight["availability_status"],
            "loader_backend": preflight["loader_backend"],
            "loader_name": preflight["loader_name"],
        },
        "existing_data": {
            "root": str(existing_dataset_root.resolve(strict=False)),
            **existing_stats,
            "recognized_by_dataset": recognized,
            "preserved": True,
        },
        "route_check": {"status": "not_applicable"},
        "acquisition_test": {"status": "not_run"},
        "load_test": {"status": "not_run"},
        "record_completed": False,
    }


def _persist_report(
    output_json: Path,
    metadata: dict[str, Any],
    rows: dict[str, dict[str, Any]],
) -> None:
    ordered_rows = [rows[name] for name in sorted(rows)]
    payload = {"metadata": metadata, "results": ordered_rows}
    _write_json_atomic(output_json, payload)

    output_csv = output_json.with_suffix(".csv")
    fields = [
        "record_id",
        "canonical_name",
        "modalities",
        "download_type",
        "selection",
        "estimated_size_gb",
        "existing_file_count",
        "existing_recognized",
        "route_check_result",
        "acquisition_status",
        "transfer_started",
        "downloaded_file_count",
        "downloaded_size_bytes",
        "load_status",
        "load_split",
        "loaded_sample_count",
        "sample_path_exists",
        "image_decode_status",
        "scratch_cleanup_status",
        "record_completed",
    ]
    temporary = output_csv.with_suffix(".csv.tmp")
    with temporary.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in ordered_rows:
            acquisition = row.get("acquisition_test", {})
            load = row.get("load_test", {})
            downloaded = acquisition.get("downloaded_tree", {})
            writer.writerow(
                {
                    "record_id": row["record_id"],
                    "canonical_name": row["canonical_name"],
                    "modalities": "|".join(row["modalities"]),
                    "download_type": row["download_type"],
                    "selection": row["selection"],
                    "estimated_size_gb": row["estimated_size_gb"],
                    "existing_file_count": row["existing_data"]["file_count"],
                    "existing_recognized": row["existing_data"][
                        "recognized_by_dataset"
                    ],
                    "route_check_result": row.get("route_check", {}).get(
                        "result",
                        row.get("route_check", {}).get("status", ""),
                    ),
                    "acquisition_status": acquisition.get("status", ""),
                    "transfer_started": acquisition.get("transfer_started", ""),
                    "downloaded_file_count": downloaded.get("file_count", ""),
                    "downloaded_size_bytes": downloaded.get("size_bytes", ""),
                    "load_status": load.get("status", ""),
                    "load_split": load.get("split", ""),
                    "loaded_sample_count": load.get("sample_count", ""),
                    "sample_path_exists": load.get("sample_path_exists", ""),
                    "image_decode_status": load.get("image_decode_status", ""),
                    "scratch_cleanup_status": acquisition.get(
                        "scratch_cleanup", {}
                    ).get("status", ""),
                    "record_completed": row["record_completed"],
                }
            )
    temporary.replace(output_csv)


def _load_prior_rows(output_json: Path) -> dict[str, dict[str, Any]]:
    if not output_json.exists():
        return {}
    payload = json.loads(output_json.read_text(encoding="utf-8"))
    return {row["record_id"]: row for row in payload.get("results", [])}


def _row_needs_retry(row: dict[str, Any]) -> bool:
    acquisition = row.get("acquisition_test", {})
    load = row.get("load_test", {})
    if acquisition.get("status") in RETRY_ACQUISITION_STATUSES:
        return True
    if load.get("status") in RETRY_LOAD_STATUSES:
        return True
    downloaded = acquisition.get("downloaded_tree", {})
    return (
        acquisition.get("status") == "completed"
        and downloaded.get("file_count") == 0
    )


def _merge_worker_result(row: dict[str, Any], worker: dict[str, Any]) -> None:
    row["acquisition_test"] = dict(worker.get("acquisition", {}))
    row["acquisition_test"]["downloaded_tree"] = worker.get(
        "downloaded_tree", {}
    )
    row["acquisition_test"]["worker_return_code"] = worker.get(
        "worker_return_code"
    )
    row["acquisition_test"]["worker_timed_out"] = worker.get(
        "worker_timed_out"
    )
    row["acquisition_test"]["worker_wall_seconds"] = worker.get(
        "worker_wall_seconds"
    )
    row["acquisition_test"]["scratch_cleanup"] = worker.get(
        "scratch_cleanup", {}
    )
    if worker.get("worker_error"):
        row["acquisition_test"]["worker_error"] = worker["worker_error"]
    if worker.get("worker_log_tail"):
        row["acquisition_test"]["worker_log_tail"] = worker["worker_log_tail"]
    row["load_test"] = worker.get(
        "load", {"status": "not_run_worker_result_missing"}
    )


def _selection_counts(rows: Iterable[dict[str, Any]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for row in rows:
        key = row["selection"]
        counts[key] = counts.get(key, 0) + 1
    return dict(sorted(counts.items()))


def _run(args: argparse.Namespace) -> int:
    scratch_root = _validate_scratch_root(args.scratch_root)
    existing_root = args.existing_data_root.expanduser().resolve(strict=False)
    output_json = args.output.resolve(strict=False)
    output_json.parent.mkdir(parents=True, exist_ok=True)
    scratch_root.mkdir(parents=True, exist_ok=True)
    work_root = scratch_root / "work"
    work_root.mkdir(parents=True, exist_ok=True)

    before_snapshot = _existing_snapshot(existing_root)
    prior_rows = _load_prior_rows(output_json) if args.resume else {}
    retry_records = set(args.retry_record or [])
    force_download_records = set(args.force_download_record or [])
    resume_scratch_records = set(args.resume_scratch_record or [])
    catalog_names = set(REGISTRY.names())
    unknown_records = (
        retry_records | force_download_records | resume_scratch_records
    ) - catalog_names
    if unknown_records:
        raise ValueError(
            "Unknown record(s): " + ", ".join(sorted(unknown_records))
        )
    if (retry_records or args.retry_problems) and not prior_rows:
        raise ValueError(
            "Selective retry requires an existing output report. "
            "Run the full audit first."
        )
    if not resume_scratch_records.issubset(retry_records):
        raise ValueError(
            "--resume-scratch-record must also be named by --retry-record: "
            + ", ".join(sorted(resume_scratch_records - retry_records))
        )
    rows: dict[str, dict[str, Any]] = {}
    for dataset in sorted(
        REGISTRY.list_datasets(), key=lambda item: item.info.name
    ):
        fresh = _row_template(dataset, scratch_root, existing_root)
        prior = prior_rows.get(dataset.info.name)
        refresh = bool(
            prior
            and (
                dataset.info.name in retry_records
                or (args.retry_problems and _row_needs_retry(prior))
            )
        )
        rows[dataset.info.name] = (
            prior
            if prior and prior.get("record_completed") and not refresh
            else fresh
        )

    metadata: dict[str, Any] = {
        "schema_version": "1.0",
        "run_started_at_utc": _utc_now(),
        "run_completed_at_utc": None,
        "command": " ".join(sys.argv),
        "catalog_records": len(rows),
        "selection_counts": _selection_counts(rows.values()),
        "excluded_backends": sorted(EXCLUDED_BACKENDS),
        "surgical_video_excluded": True,
        "google_drive_dataset_transfer_performed": False,
        "scratch_root": str(scratch_root),
        "scratch_drive_free_bytes_at_start": shutil.disk_usage(scratch_root).free,
        "existing_data_snapshot_before": before_snapshot,
        "existing_data_snapshot_after": None,
        "existing_data_unchanged": None,
        "environment": (
            f"{platform.system()} {platform.release()} | "
            f"Python {platform.python_version()} | EyeDataHub {__version__}"
        ),
    }
    _persist_report(output_json, metadata, rows)
    script = Path(__file__).resolve()

    route_rows = [
        row
        for row in rows.values()
        if row["selection"] == "route_check_only"
        and not row.get("record_completed")
    ]
    for index, row in enumerate(route_rows, start=1):
        print(
            f"[route {index}/{len(route_rows)}] {row['record_id']}",
            flush=True,
        )
        url = row["preflight"]["preferred_route_url"]
        row["route_check"] = (
            _route_check(row["record_id"], url)
            if url
            else {
                "result": "failed_missing_route_url",
                "dataset_transfer_started": False,
            }
        )
        row["acquisition_test"] = {
            "status": "not_run_route_check_only",
            "transfer_started": False,
        }
        row["record_completed"] = True
        _persist_report(output_json, metadata, rows)

    existing_load_rows = [
        row
        for row in rows.values()
        if row["existing_data"]["file_count"] > 0
        and row["selection"] != "excluded_surgical_video"
        and row["load_test"].get("status") == "not_run"
    ]
    for index, row in enumerate(existing_load_rows, start=1):
        print(
            f"[existing load {index}/{len(existing_load_rows)}] "
            f"{row['record_id']}",
            flush=True,
        )
        worker = _invoke_worker(
            script=script,
            record_id=row["record_id"],
            data_dir=existing_root,
            work_root=work_root,
            load_only=True,
            timeout_seconds=args.load_timeout_seconds,
        )
        row["load_test"] = worker.get("load", {})
        row["existing_data"]["load_result"] = worker.get("load", {})
        row["existing_data"]["load_worker"] = {
            "worker_return_code": worker.get("worker_return_code"),
            "worker_timed_out": worker.get("worker_timed_out"),
            "worker_wall_seconds": worker.get("worker_wall_seconds"),
            "scratch_cleanup": worker.get("scratch_cleanup", {}),
        }
        if worker.get("worker_error"):
            row["existing_data"]["load_worker"]["worker_error"] = worker[
                "worker_error"
            ]
        if worker.get("worker_log_tail"):
            row["existing_data"]["load_worker"]["worker_log_tail"] = worker[
                "worker_log_tail"
            ]
        if (
            row["selection"] == "eligible_download"
            and row["existing_data"]["recognized_by_dataset"]
            and row["record_id"] not in force_download_records
        ):
            row["acquisition_test"] = {
                "status": "skipped_existing_data_preserved",
                "transfer_started": False,
            }
            row["record_completed"] = True
        elif row["selection"] not in {"eligible_download", "route_check_only"}:
            row["acquisition_test"] = {
                "status": "not_run_excluded_or_blocked",
                "transfer_started": False,
            }
            row["record_completed"] = True
        _persist_report(output_json, metadata, rows)

    for row in rows.values():
        if row["record_completed"]:
            continue
        if row["selection"] in {
            "excluded_surgical_video",
            "excluded_known_platform",
            "excluded_known_platform_dependency",
            "preflight_blocked",
        }:
            row["acquisition_test"] = {
                "status": "not_run_excluded_or_blocked",
                "transfer_started": False,
            }
            row["load_test"] = {
                "status": "not_run_no_existing_data",
                "implemented": None,
            }
            row["record_completed"] = True
    _persist_report(output_json, metadata, rows)

    download_rows = [
        row
        for row in rows.values()
        if row["selection"] == "eligible_download"
        and not row["record_completed"]
    ]
    download_rows.sort(
        key=lambda row: (
            row["estimated_size_gb"] is None,
            row["estimated_size_gb"] or 0,
            row["record_id"],
        )
    )
    for index, row in enumerate(download_rows, start=1):
        size = row["estimated_size_gb"]
        print(
            f"[download {index}/{len(download_rows)}] {row['record_id']} "
            f"(estimated {size if size is not None else 'unknown'} GiB)",
            flush=True,
        )
        record_data_dir = work_root / row["record_id"] / "data"
        worker = _invoke_worker(
            script=script,
            record_id=row["record_id"],
            data_dir=record_data_dir,
            work_root=work_root,
            load_only=False,
            timeout_seconds=args.download_timeout_seconds,
            resume_existing_work=(
                row["record_id"] in resume_scratch_records
            ),
        )
        _merge_worker_result(row, worker)
        row["record_completed"] = True
        print(
            f"  acquisition={row['acquisition_test'].get('status')} "
            f"load={row['load_test'].get('status')} "
            f"cleanup={row['acquisition_test'].get('scratch_cleanup', {}).get('status')}",
            flush=True,
        )
        _persist_report(output_json, metadata, rows)

    after_snapshot = _existing_snapshot(existing_root)
    unchanged = (
        before_snapshot["tree"]["metadata_fingerprint"]
        == after_snapshot["tree"]["metadata_fingerprint"]
        and before_snapshot["tree"]["file_count"]
        == after_snapshot["tree"]["file_count"]
        and before_snapshot["tree"]["size_bytes"]
        == after_snapshot["tree"]["size_bytes"]
    )
    metadata["existing_data_snapshot_after"] = after_snapshot
    metadata["existing_data_unchanged"] = unchanged
    metadata["scratch_drive_free_bytes_before_final_cleanup"] = shutil.disk_usage(
        scratch_root
    ).free
    metadata["run_completed_at_utc"] = _utc_now()
    metadata["completed_records"] = sum(
        bool(row["record_completed"]) for row in rows.values()
    )
    metadata["scratch_work_entries_remaining"] = [
        str(path) for path in work_root.iterdir()
    ]
    _persist_report(output_json, metadata, rows)

    if not metadata["scratch_work_entries_remaining"]:
        work_root.rmdir()
        if not any(scratch_root.iterdir()):
            scratch_root.rmdir()
            metadata["scratch_root_removed"] = True
        else:
            metadata["scratch_root_removed"] = False
    else:
        metadata["scratch_root_removed"] = False
    _persist_report(output_json, metadata, rows)

    failures = sum(
        row.get("acquisition_test", {}).get("status")
        in {
            "failed",
            "transfer_incomplete",
            "not_run_worker_crash",
            "not_run_worker_timeout",
        }
        for row in rows.values()
    )
    print(
        f"Completed {metadata['completed_records']}/{len(rows)} records; "
        f"transfer failures={failures}; existing data unchanged={unchanged}; "
        f"report={output_json}",
        flush=True,
    )
    return 0 if unchanged and metadata["completed_records"] == len(rows) else 1


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    run = subparsers.add_parser("run", help="Run or resume the full audit")
    run.add_argument("--scratch-root", type=Path, required=True)
    run.add_argument(
        "--existing-data-root",
        type=Path,
        default=Path.home() / ".eyedatahub" / "data",
    )
    run.add_argument("--output", type=Path, required=True)
    run.add_argument("--download-timeout-seconds", type=int, default=14_400)
    run.add_argument("--load-timeout-seconds", type=int, default=1_800)
    run.add_argument(
        "--retry-problems",
        action="store_true",
        help="Retry prior acquisition or loader failures only.",
    )
    run.add_argument(
        "--retry-record",
        action="append",
        default=[],
        help="Retry one named record from an existing report; repeat as needed.",
    )
    run.add_argument(
        "--force-download-record",
        action="append",
        default=[],
        help=(
            "For a retried record, run an isolated scratch transfer even when "
            "a preserved local copy already exists."
        ),
    )
    run.add_argument(
        "--resume-scratch-record",
        action="append",
        default=[],
        help=(
            "Resume an interrupted record directory already inside this exact "
            "scratch root. The record must also be supplied with "
            "--retry-record."
        ),
    )
    run.add_argument("--no-resume", dest="resume", action="store_false")
    run.set_defaults(resume=True)

    worker = subparsers.add_parser("worker", help=argparse.SUPPRESS)
    worker.add_argument("--record", required=True)
    worker.add_argument("--data-dir", type=Path, required=True)
    worker.add_argument("--result", type=Path, required=True)
    worker.add_argument("--load-only", action="store_true")
    return parser


def main() -> int:
    args = _parser().parse_args()
    if args.command == "worker":
        return _worker(args.record, args.data_dir, args.result, args.load_only)
    return _run(args)


if __name__ == "__main__":
    raise SystemExit(main())
