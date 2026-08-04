"""Verify that every dataset's download_url is reachable.

For each registered dataset:
  1. HEAD the URL.
  2. If HEAD is unsupported / errors, fall back to GET with `Range: bytes=0-0`.
  3. Record status code + final URL after redirects + content-length.

Outputs a JSON report + a markdown summary. Fast (~a few seconds per URL
in parallel).

Run:
    python -m hub.audit.verify_urls --out hub/audit/url_report.json
    python -m hub.audit.verify_urls --md hub/audit/url_report.md
"""
from __future__ import annotations

import argparse
import concurrent.futures
import json
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import parse_qsl, urlparse, urlsplit, urlunsplit

import requests

import eyedatahub
from eyedatahub.datasets.registry import REGISTRY


# Use a realistic browser UA — many academic + Kaggle/Mendeley hosts
# block generic Python UAs with 403/404 even though the resource exists.
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)
TIMEOUT = 30  # seconds
CONCURRENCY = 8

SENSITIVE_QUERY_KEYS = {
    "access_token",
    "api_key",
    "credential",
    "key",
    "sig",
    "signature",
    "token",
}


def sanitize_public_url(url: str) -> str:
    """Remove signed or credential-bearing query strings from public reports."""
    parsed = urlsplit(str(url))
    query_keys = {key.lower() for key, _ in parse_qsl(parsed.query, keep_blank_values=True)}
    has_sensitive_query = any(
        key in SENSITIVE_QUERY_KEYS
        or key.startswith("x-amz-")
        or key.startswith("x-goog-")
        for key in query_keys
    )
    if not has_sensitive_query:
        return str(url)
    return urlunsplit((parsed.scheme, parsed.netloc, parsed.path, "", parsed.fragment))

STATUS_DEFINITIONS = {
    "ok": "HTTP 2xx response after redirects; technical reachability only.",
    "forbidden": "HTTP 403 response; often bot-blocked, browser-gated, or manually accessible.",
    "platform_or_browser_route": "The automated page probe was denied by a repository host; use the documented official API, client, or browser route. This is not a download failure and does not by itself establish that a user account is required.",
    "auth_required": "HTTP 401 or known access-controlled host requiring authentication.",
    "not_found": "HTTP 404 response; source-page review or replacement URL required.",
    "connect_error": "Connection failure during automated request.",
    "ssl_error": "TLS/SSL validation failure during automated request.",
    "timeout": "No response within configured timeout.",
    "server_error": "HTTP 5xx response from source host.",
    "http_*": "Other non-success HTTP response requiring source-page review.",
    "no_url": "No URL recorded in the catalog record.",
}


def check_url(url: str) -> dict[str, Any]:
    """Attempt HEAD then a Range GET, then a small streaming GET. Return status metadata."""
    if not url:
        return {"status": "no_url"}

    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
    }
    result: dict[str, Any] = {"url": url}

    def _record(r, method: str) -> None:
        result["method"] = method
        result["http_status"] = r.status_code
        result["final_url"] = sanitize_public_url(r.url)
        result["content_length"] = r.headers.get("content-length")

    try:
        # HEAD first — quickest.
        r = requests.head(url, headers=headers, timeout=TIMEOUT, allow_redirects=True)
        _record(r, "HEAD")

        # Many hosts refuse HEAD or return misleading codes — retry as GET.
        if r.status_code in (400, 401, 403, 404, 405, 501, 502, 503):
            r2 = requests.get(
                url,
                headers={**headers, "Range": "bytes=0-0"},
                timeout=TIMEOUT,
                allow_redirects=True,
                stream=True,
            )
            r2.close()
            _record(r2, "GET(Range)")

            # If still bad, do one final streaming GET without Range.
            if r2.status_code in (400, 401, 403, 404, 405, 416, 501, 502, 503):
                r3 = requests.get(
                    url,
                    headers=headers,
                    timeout=TIMEOUT,
                    allow_redirects=True,
                    stream=True,
                )
                # Read first 512 bytes then close to keep it fast.
                next(r3.iter_content(chunk_size=512), None)
                r3.close()
                _record(r3, "GET(stream)")

        result["status"] = _classify(result["http_status"], url)
    except requests.exceptions.SSLError as e:
        result["status"] = "ssl_error"
        result["error"] = str(e)[:200]
    except requests.exceptions.ConnectionError as e:
        result["status"] = "connect_error"
        result["error"] = str(e)[:200]
    except requests.exceptions.ReadTimeout:
        result["status"] = "timeout"
    except Exception as e:
        result["status"] = "other_error"
        result["error"] = f"{type(e).__name__}: {str(e)[:200]}"
    return result


def _classify(status: int, url: str) -> str:
    platform_hosts = (
        "datadryad.org",
        "data.mendeley.com",
        "figshare.com",
        "huggingface.co",
        "kaggle.com",
        "physionet.org",
        "zenodo.org",
    )
    if 200 <= status < 300:
        return "ok"
    if status in (301, 302, 303, 307, 308):
        return "redirect"
    if status == 401:
        return "auth_required"
    if status == 403:
        # Some hosts return 403 to bots — annotate rather than fail
        if any(host in url for host in platform_hosts):
            return "platform_or_browser_route"
        return "auth_required" if "physionet" in url or "ieee-dataport" in url else "forbidden"
    if status == 404:
        return "not_found"
    if status == 429:
        return "rate_limited"
    if status >= 500:
        return "server_error"
    return f"http_{status}"


def audit_all() -> list[dict[str, Any]]:
    datasets = REGISTRY.list_datasets()
    findings: list[dict[str, Any]] = []

    def _worker(ds):
        info = ds.info
        check = check_url(info.download_url or "")
        return {
            "name": info.name,
            "modality": info.modality,
            "download_type": info.download_type,
            "download_url": info.download_url,
            **check,
        }

    with concurrent.futures.ThreadPoolExecutor(max_workers=CONCURRENCY) as pool:
        for f in pool.map(_worker, datasets):
            findings.append(f)
    return findings


def summarize(findings: list[dict]) -> dict[str, Any]:
    from collections import Counter

    by_status = Counter(f.get("status", "?") for f in findings)
    review_statuses = {
        "not_found",
        "connect_error",
        "ssl_error",
        "other_error",
        "server_error",
        "timeout",
    }
    broken = [
        f for f in findings
        if f.get("status") in review_statuses or str(f.get("status", "")).startswith("http_")
    ]
    return {
        "total": len(findings),
        "by_status": dict(by_status.most_common()),
        "broken_count": len(broken),
        "broken": [{"name": f["name"], "status": f["status"], "url": f["download_url"]} for f in broken],
    }


def _git_value(*args: str) -> str | None:
    try:
        value = subprocess.check_output(
            ["git", *args],
            cwd=Path(__file__).resolve().parents[2],
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
        return value or None
    except Exception:
        return None


def audit_metadata(elapsed: float) -> dict[str, Any]:
    dirty = _git_value("status", "--short", "--untracked-files=no")
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "elapsed_seconds": round(elapsed, 1),
        "command": " ".join([Path(sys.executable).name, "-m", "hub.audit.verify_urls"]),
        "package": "eyedatahub",
        "package_version": eyedatahub.__version__,
        "git_commit": _git_value("rev-parse", "HEAD"),
        "git_dirty": bool(dirty),
        "user_agent": USER_AGENT,
        "timeout_seconds": TIMEOUT,
        "concurrency": CONCURRENCY,
        "status_definitions": STATUS_DEFINITIONS,
    }


def _markdown_url(url: str | None) -> str:
    if not url:
        return "-"
    parsed = urlparse(str(url))
    host = parsed.netloc.lower().removeprefix("www.")
    if host == "doi.org":
        label = str(url)
    elif host:
        path = parsed.path.strip("/")
        label = f"{host}/{path.split('/')[0]}" if path else host
    else:
        label = "Source"
    return f"[{label}]({url})"


def markdown_report(findings: list[dict], summary: dict, metadata: dict) -> str:
    lines = [
        "# EyeDataHub URL Audit Report",
        "",
        f"- **Total datasets checked**: {summary['total']}",
        f"- **Broken URLs**: {summary['broken_count']}",
        f"- **Generated at**: {metadata['generated_at']}",
        f"- **EyeDataHub version**: {metadata['package_version']}",
        f"- **Git commit**: {metadata.get('git_commit') or 'unknown'}",
        f"- **Git dirty**: {metadata['git_dirty']}",
        f"- **Timeout / concurrency**: {metadata['timeout_seconds']} s / {metadata['concurrency']}",
        "",
        "## Status distribution",
        "",
        "| Status | Count |",
        "| --- | ---:|",
    ]
    for status, count in summary["by_status"].items():
        lines.append(f"| {status} | {count} |")
    lines.append("")
    lines += [
        "## Status definitions",
        "",
        "| Status | Definition |",
        "| --- | --- |",
    ]
    for status, definition in metadata["status_definitions"].items():
        lines.append(f"| `{status}` | {definition} |")
    lines.append("")
    if summary["broken"]:
        lines += [
            "## Broken / unreachable",
            "",
            "| Dataset | Status | URL |",
            "| --- | --- | --- |",
        ]
        for b in summary["broken"]:
            lines.append(f"| `{b['name']}` | `{b['status']}` | {_markdown_url(b['url'])} |")
        lines.append("")
    lines += [
        "## All findings",
        "",
        "| Dataset | Backend | Status | HTTP | Source URL |",
        "| --- | --- | --- | ---:| --- |",
    ]
    for f in sorted(findings, key=lambda x: (x.get("status", ""), x["name"])):
        status = f.get("status", "?")
        http = f.get("http_status", "-")
        source_url = f.get("download_url") or f.get("final_url")
        lines.append(
            f"| `{f['name']}` | `{f['download_type']}` | `{status}` | {http} | {_markdown_url(source_url)} |"
        )
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", default="hub/audit/url_report.json")
    ap.add_argument("--md", default="hub/audit/url_report.md")
    args = ap.parse_args()

    t0 = time.time()
    findings = audit_all()
    elapsed = time.time() - t0
    summary = summarize(findings)
    metadata = audit_metadata(elapsed)

    out_json = Path(args.out)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(
        json.dumps({"metadata": metadata, "summary": summary, "findings": findings}, indent=2),
        encoding="utf-8",
    )

    Path(args.md).write_text(markdown_report(findings, summary, metadata), encoding="utf-8")

    print(f"Checked {summary['total']} URLs in {elapsed:.1f}s")
    print(f"Broken: {summary['broken_count']}")
    print(f"Status: {summary['by_status']}")
    print(f"Reports: {out_json} + {args.md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
