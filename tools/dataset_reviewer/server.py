"""Local-only review server for the EyeDataHub catalog.

The server binds to 127.0.0.1, serves the small review interface in this
directory, and persists subjective review decisions outside the public catalog.
It uses only the Python standard library.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import os
import re
import threading
import webbrowser
from datetime import datetime, timezone
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlparse

try:
    from .model_data_screen import attach_model_data_screens
except ImportError:  # Direct execution from this directory.
    from model_data_screen import attach_model_data_screens


APP_ROOT = Path(__file__).resolve().parent
STATIC_ROOT = APP_ROOT / "static"
REPO_ROOT = APP_ROOT.parents[1]
CATALOG_PATH = REPO_ROOT / "hub" / "catalog.json"
REVIEW_PATH = REPO_ROOT / "data" / "internal_dataset_review_decisions.json"
REVIEW_BACKUP_PATH = REVIEW_PATH.with_suffix(".json.bak")
MANUSCRIPT_PATH = (
    REPO_ROOT
    / "paper"
    / "scientific-data"
    / "output"
    / "pdf"
    / "eyedatahub_scientific_data_manuscript.pdf"
)
SUPPLEMENT_PATH = (
    REPO_ROOT
    / "paper"
    / "scientific-data"
    / "output"
    / "pdf"
    / "eyedatahub_supplementary_information.pdf"
)

VALID_DECISIONS = {
    "",
    "include",
    "needs_review",
    "exclude",
    "duplicate_or_version",
}
MAX_BODY_BYTES = 1_000_000


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def load_catalog() -> dict:
    with CATALOG_PATH.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)
    records = payload.get("records", [])
    if not isinstance(records, list):
        raise ValueError("hub/catalog.json does not contain a records list")
    return attach_model_data_screens(payload, REPO_ROOT)


def catalog_sha256() -> str:
    digest = hashlib.sha256()
    with CATALOG_PATH.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def blank_review_document(catalog: dict) -> dict:
    return {
        "schema_version": "1.0",
        "catalog_version": catalog.get("catalog_version", "unknown"),
        "catalog_sha256": catalog_sha256(),
        "created_at": utc_now(),
        "updated_at": utc_now(),
        "custom_tags": [],
        "reviews": {},
    }


def load_reviews(catalog: dict | None = None) -> dict:
    catalog = catalog or load_catalog()
    if not REVIEW_PATH.exists():
        return blank_review_document(catalog)
    try:
        with REVIEW_PATH.open("r", encoding="utf-8") as handle:
            document = json.load(handle)
    except (OSError, json.JSONDecodeError):
        if REVIEW_BACKUP_PATH.exists():
            with REVIEW_BACKUP_PATH.open("r", encoding="utf-8") as handle:
                document = json.load(handle)
        else:
            raise
    document.setdefault("schema_version", "1.0")
    document.setdefault("custom_tags", [])
    document.setdefault("reviews", {})
    return document


def write_reviews(document: dict, catalog: dict) -> None:
    REVIEW_PATH.parent.mkdir(parents=True, exist_ok=True)
    document["catalog_version"] = catalog.get("catalog_version", "unknown")
    document["catalog_sha256"] = catalog_sha256()
    document["updated_at"] = utc_now()
    if REVIEW_PATH.exists():
        REVIEW_BACKUP_PATH.write_bytes(REVIEW_PATH.read_bytes())
    temporary = REVIEW_PATH.with_suffix(".json.tmp")
    with temporary.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(document, handle, indent=2, ensure_ascii=True, sort_keys=True)
        handle.write("\n")
        handle.flush()
        os.fsync(handle.fileno())
    temporary.replace(REVIEW_PATH)


def clean_text(value: object, max_length: int) -> str:
    text = str(value or "").strip()
    return text[:max_length]


def validate_review(payload: object) -> dict:
    if not isinstance(payload, dict):
        raise ValueError("Review body must be a JSON object")
    decision = clean_text(payload.get("decision"), 80)
    if decision not in VALID_DECISIONS:
        raise ValueError(f"Unsupported decision: {decision}")

    score = payload.get("score")
    if score in ("", None):
        score = None
    elif isinstance(score, bool) or not isinstance(score, int) or not 1 <= score <= 5:
        raise ValueError("Score must be an integer from 1 to 5 or null")

    raw_tags = payload.get("tags", [])
    if not isinstance(raw_tags, list):
        raise ValueError("Tags must be a list")
    tags = []
    for raw_tag in raw_tags[:50]:
        tag = clean_text(raw_tag, 80)
        if tag and tag not in tags:
            tags.append(tag)

    return {
        "decision": decision,
        "score": score,
        "tags": tags,
        "notes": clean_text(payload.get("notes"), 20_000),
        "reviewed_at": utc_now(),
    }


def safe_url(value: object) -> str:
    candidate = str(value or "").strip()
    if candidate.startswith(("https://", "http://")):
        return candidate
    return ""


DOI_PATTERN = re.compile(r"10\.\d{4,9}/[-._;()/:A-Z0-9]+", re.IGNORECASE)
URL_PATTERN = re.compile(r"https?://[^\s<>\"]+")


def publication_url(record: dict) -> str:
    doi = clean_text(record.get("associated_publication_doi"), 500)
    if doi:
        doi = doi.removeprefix("https://doi.org/").removeprefix("http://doi.org/")
        return f"https://doi.org/{doi}"

    citation = str(record.get("citation") or "")
    doi_match = DOI_PATTERN.search(citation)
    if doi_match:
        doi = doi_match.group(0).rstrip(".,;)")
        return f"https://doi.org/{doi}"

    citation_evidence = safe_url(record.get("citation_evidence_url"))
    source_urls = {
        safe_url(record.get("preferred_route_url")),
        safe_url(record.get("source_landing_page_url")),
        safe_url(record.get("download_url")),
    }
    if citation_evidence and citation_evidence not in source_urls:
        return citation_evidence

    for match in URL_PATTERN.findall(citation):
        candidate = match.rstrip(".,;)")
        if candidate not in source_urls:
            return candidate
    return ""


def source_url(record: dict) -> str:
    for field in (
        "preferred_route_url",
        "source_landing_page_url",
        "canonical_resolver_url",
        "download_url",
    ):
        value = safe_url(record.get(field))
        if value:
            return value
    return ""


def export_csv(catalog: dict, reviews: dict) -> bytes:
    buffer = io.StringIO(newline="")
    fields = [
        "record_id",
        "canonical_name",
        "dataset_family_id",
        "resource_role",
        "primary_category",
        "modalities",
        "tasks",
        "source_url",
        "publication_url",
        "screen_classification",
        "screen_suggested_action",
        "screen_rationale",
        "screen_source_evidence",
        "screen_suggested_modalities",
        "decision",
        "score",
        "review_tags",
        "review_notes",
        "reviewed_at",
    ]
    writer = csv.DictWriter(buffer, fieldnames=fields)
    writer.writeheader()
    saved = reviews.get("reviews", {})
    for record in catalog.get("records", []):
        record_id = str(record.get("record_id") or record.get("name") or "")
        review = saved.get(record_id, {})
        screen = record.get("internal_model_data_screen") or {}
        writer.writerow(
            {
                "record_id": record_id,
                "canonical_name": record.get("canonical_name") or record.get("full_name") or "",
                "dataset_family_id": record.get("dataset_family_id") or "",
                "resource_role": record.get("resource_role") or "",
                "primary_category": record.get("primary_category") or "",
                "modalities": "|".join(record.get("modalities") or []),
                "tasks": "|".join(record.get("tasks") or []),
                "source_url": source_url(record),
                "publication_url": publication_url(record),
                "screen_classification": screen.get("classification", ""),
                "screen_suggested_action": screen.get("suggested_action", ""),
                "screen_rationale": screen.get("rationale", ""),
                "screen_source_evidence": screen.get("source_evidence", ""),
                "screen_suggested_modalities": "|".join(
                    screen.get("suggested_modalities") or []
                ),
                "decision": review.get("decision", ""),
                "score": review.get("score", ""),
                "review_tags": "|".join(review.get("tags") or []),
                "review_notes": review.get("notes", ""),
                "reviewed_at": review.get("reviewed_at", ""),
            }
        )
    return buffer.getvalue().encode("utf-8-sig")


class ReviewHandler(BaseHTTPRequestHandler):
    server_version = "EyeDataHubReviewer/1.0"

    def log_message(self, format_string: str, *args: object) -> None:
        print(f"[{self.log_date_time_string()}] {format_string % args}")

    def send_bytes(
        self,
        body: bytes,
        content_type: str,
        status: HTTPStatus = HTTPStatus.OK,
        attachment_name: str | None = None,
    ) -> None:
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "no-referrer")
        self.send_header(
            "Content-Security-Policy",
            "default-src 'self'; script-src 'self'; style-src 'self'; "
            "img-src 'self' data:; connect-src 'self'; object-src 'none'; "
            "base-uri 'none'; frame-ancestors 'none'",
        )
        if attachment_name:
            self.send_header("Content-Disposition", f'attachment; filename="{attachment_name}"')
        self.end_headers()
        self.wfile.write(body)

    def send_json(self, payload: object, status: HTTPStatus = HTTPStatus.OK) -> None:
        body = json.dumps(payload, ensure_ascii=True).encode("utf-8")
        self.send_bytes(body, "application/json; charset=utf-8", status)

    def send_error_json(self, status: HTTPStatus, message: str) -> None:
        self.send_json({"error": message}, status)

    def do_GET(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)
        path = unquote(parsed.path)
        try:
            if path == "/api/catalog":
                catalog = load_catalog()
                self.send_json(
                    {
                        "schema_version": catalog.get("schema_version"),
                        "catalog_version": catalog.get("catalog_version"),
                        "catalog_search_cutoff": catalog.get("catalog_search_cutoff"),
                        "record_count": catalog.get("record_count"),
                        "primary_category_count": catalog.get("primary_category_count"),
                        "catalog_sha256": catalog_sha256(),
                        "records": catalog.get("records", []),
                    }
                )
                return
            if path == "/api/reviews":
                self.send_json(load_reviews())
                return
            if path == "/api/export/reviews.json":
                body = json.dumps(load_reviews(), indent=2, ensure_ascii=True).encode("utf-8")
                self.send_bytes(
                    body,
                    "application/json; charset=utf-8",
                    attachment_name="eyedatahub_internal_reviews.json",
                )
                return
            if path == "/api/export/reviews.csv":
                catalog = load_catalog()
                body = export_csv(catalog, load_reviews(catalog))
                self.send_bytes(
                    body,
                    "text/csv; charset=utf-8",
                    attachment_name="eyedatahub_internal_reviews.csv",
                )
                return
            if path == "/paper/manuscript.pdf":
                self.send_file(MANUSCRIPT_PATH, "application/pdf")
                return
            if path == "/paper/supplement.pdf":
                self.send_file(SUPPLEMENT_PATH, "application/pdf")
                return
            self.send_static(path)
        except FileNotFoundError:
            self.send_error_json(HTTPStatus.NOT_FOUND, "Requested file was not found")
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            self.send_error_json(HTTPStatus.INTERNAL_SERVER_ERROR, str(exc))

    def do_POST(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)
        path = unquote(parsed.path)
        try:
            length = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            self.send_error_json(HTTPStatus.BAD_REQUEST, "Invalid Content-Length")
            return
        if length <= 0 or length > MAX_BODY_BYTES:
            self.send_error_json(HTTPStatus.BAD_REQUEST, "Invalid request size")
            return
        try:
            payload = json.loads(self.rfile.read(length).decode("utf-8"))
            catalog = load_catalog()
            reviews = load_reviews(catalog)
            record_ids = {
                str(record.get("record_id") or record.get("name"))
                for record in catalog.get("records", [])
            }

            if path.startswith("/api/reviews/"):
                record_id = path.removeprefix("/api/reviews/").strip()
                if not record_id or record_id not in record_ids:
                    self.send_error_json(HTTPStatus.NOT_FOUND, "Unknown catalog record")
                    return
                review = validate_review(payload)
                is_empty = (
                    not review["decision"]
                    and review["score"] is None
                    and not review["tags"]
                    and not review["notes"]
                )
                if is_empty:
                    reviews["reviews"].pop(record_id, None)
                else:
                    reviews["reviews"][record_id] = review
                write_reviews(reviews, catalog)
                self.send_json(
                    {
                        "record_id": record_id,
                        "review": None if is_empty else review,
                        "updated_at": reviews["updated_at"],
                    }
                )
                return

            if path == "/api/settings/tags":
                if not isinstance(payload, dict) or not isinstance(payload.get("custom_tags"), list):
                    raise ValueError("custom_tags must be a list")
                custom_tags = []
                for raw_tag in payload["custom_tags"][:100]:
                    tag = clean_text(raw_tag, 80)
                    if tag and tag not in custom_tags:
                        custom_tags.append(tag)
                reviews["custom_tags"] = custom_tags
                write_reviews(reviews, catalog)
                self.send_json({"custom_tags": custom_tags, "updated_at": reviews["updated_at"]})
                return

            self.send_error_json(HTTPStatus.NOT_FOUND, "Unknown API endpoint")
        except (UnicodeDecodeError, json.JSONDecodeError, ValueError) as exc:
            self.send_error_json(HTTPStatus.BAD_REQUEST, str(exc))
        except OSError as exc:
            self.send_error_json(HTTPStatus.INTERNAL_SERVER_ERROR, str(exc))

    def send_file(self, path: Path, content_type: str) -> None:
        if not path.is_file():
            raise FileNotFoundError(path)
        self.send_bytes(path.read_bytes(), content_type)

    def send_static(self, request_path: str) -> None:
        relative = "index.html" if request_path in {"", "/"} else request_path.lstrip("/")
        candidate = (STATIC_ROOT / relative).resolve()
        if STATIC_ROOT.resolve() not in candidate.parents and candidate != STATIC_ROOT.resolve():
            self.send_error_json(HTTPStatus.FORBIDDEN, "Invalid path")
            return
        if not candidate.is_file():
            self.send_error_json(HTTPStatus.NOT_FOUND, "Page not found")
            return
        content_types = {
            ".html": "text/html; charset=utf-8",
            ".css": "text/css; charset=utf-8",
            ".js": "text/javascript; charset=utf-8",
            ".json": "application/json; charset=utf-8",
            ".png": "image/png",
        }
        self.send_bytes(candidate.read_bytes(), content_types.get(candidate.suffix, "application/octet-stream"))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the local EyeDataHub dataset reviewer")
    parser.add_argument("--host", default="127.0.0.1", help="Bind address; default is local only")
    parser.add_argument("--port", default=8765, type=int, help="Local port; default: 8765")
    parser.add_argument("--open", action="store_true", help="Open the reviewer in the default browser")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if not CATALOG_PATH.is_file():
        raise SystemExit(f"Catalog not found: {CATALOG_PATH}")
    server = ThreadingHTTPServer((args.host, args.port), ReviewHandler)
    url = f"http://{args.host}:{args.port}/"
    print(f"EyeDataHub review desk: {url}")
    print(f"Ratings autosave to: {REVIEW_PATH}")
    print("Press Ctrl+C to stop.")
    if args.open:
        threading.Timer(0.4, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
