"""Check that public release artifacts describe one scientific snapshot."""

from __future__ import annotations

import csv
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
RELEASE_VERSION = "0.7.0"
RELEASE_TAG = f"v{RELEASE_VERSION}"
RELEASE_DATE = "2026-08-04"
CATALOG_CUTOFF = "2026-08-02"
EXPECTED_RECORDS = 451
EXPECTED_FAMILIES = 446
EXPECTED_CATEGORIES = 18
EXPECTED_REPOSITORY_HITS = 18_737
EXPECTED_REPOSITORY_ELIGIBLE = 288
EXPECTED_QUANTITY_ROWS = 396
EXPECTED_BACKEND_GROUPS = {
    "source_link": 33,
    "platform_api_or_client": 350,
    "manual": 68,
}
EXPECTED_ACCESS_FRICTION = {
    "anonymous_direct": 47,
    "self_service_authenticated": 356,
    "self_service_clickthrough": 11,
    "controlled_or_manual": 29,
    "author_contact": 8,
}
PLATFORM_BACKENDS = {
    "dryad",
    "figshare",
    "huggingface",
    "kaggle",
    "mendeley",
    "physionet",
    "zenodo",
}
SOURCE_LINK_BACKENDS = {"direct", "gdrive", "github"}


def _load_json(root: Path, relative: str) -> Any:
    return json.loads((root / relative).read_text(encoding="utf-8"))


def _project_version(root: Path) -> str | None:
    text = (root / "pyproject.toml").read_text(encoding="utf-8")
    match = re.search(r'^version\s*=\s*"([^"]+)"', text, re.MULTILINE)
    return match.group(1) if match else None


def _package_version(root: Path) -> str | None:
    text = (root / "eyedatahub" / "__init__.py").read_text(encoding="utf-8")
    match = re.search(r'^__version__\s*=\s*"([^"]+)"', text, re.MULTILINE)
    return match.group(1) if match else None


def collect_consistency_errors(root: Path = ROOT) -> list[str]:
    errors: list[str] = []

    def check(condition: bool, message: str) -> None:
        if not condition:
            errors.append(message)

    catalog = _load_json(root, "hub/catalog.json")
    records = catalog["records"]
    record_ids = {row["record_id"] for row in records}
    families = {row["dataset_family_id"] for row in records}
    backends = Counter(row["loader_backend"] for row in records)
    friction = Counter(row["access_friction"] for row in records)

    check(catalog.get("catalog_version") == RELEASE_VERSION, "catalog version")
    check(catalog.get("catalog_search_cutoff") == CATALOG_CUTOFF, "catalog cutoff")
    check(catalog.get("record_count") == EXPECTED_RECORDS, "catalog record_count")
    check(len(records) == EXPECTED_RECORDS, "catalog records length")
    check(len(record_ids) == EXPECTED_RECORDS, "unique record identifiers")
    check(len(families) == EXPECTED_FAMILIES, "dataset-family count")
    check(
        catalog.get("primary_category_count") == EXPECTED_CATEGORIES,
        "primary-category count",
    )

    backend_groups = {
        "source_link": sum(backends[name] for name in SOURCE_LINK_BACKENDS),
        "platform_api_or_client": sum(backends[name] for name in PLATFORM_BACKENDS),
        "manual": backends["manual"],
    }
    check(backend_groups == EXPECTED_BACKEND_GROUPS, "backend route groups")
    check(
        {name: friction[name] for name in EXPECTED_ACCESS_FRICTION}
        == EXPECTED_ACCESS_FRICTION,
        "user-facing access requirements",
    )

    with (root / "hub/catalog.csv").open(encoding="utf-8", newline="") as handle:
        csv_rows = list(csv.DictReader(handle))
    check(len(csv_rows) == EXPECTED_RECORDS, "catalog CSV row count")
    check({row["record_id"] for row in csv_rows} == record_ids, "catalog CSV identity")

    identity = _load_json(root, "hub/audit/resource_identity_summary_2026-08-02.json")
    check(identity.get("catalog_version") == RELEASE_VERSION, "identity version")
    check(
        identity.get("current_catalog_record_count") == EXPECTED_RECORDS,
        "identity record count",
    )
    check(identity.get("dataset_family_count") == EXPECTED_FAMILIES, "identity families")

    quantity = _load_json(root, "hub/audit/resource_quantity_summary_2026-08-02.json")
    check(quantity.get("catalog_version") == RELEASE_VERSION, "quantity version")
    check(quantity.get("catalog_record_count") == EXPECTED_RECORDS, "quantity records")
    check(
        quantity.get("quantity_evidence_row_count") == EXPECTED_QUANTITY_ROWS,
        "quantity evidence rows",
    )

    screening = _load_json(root, "hub/audit/repository_screening_summary_2026-08-02.json")
    check(
        screening.get("catalog_record_count_at_screening") == EXPECTED_RECORDS,
        "screening catalog count",
    )
    overall = screening.get("overall_counts", {})
    check(overall.get("unique_search_hits") == EXPECTED_REPOSITORY_HITS, "search hits")
    check(
        overall.get("existing_catalog_record", 0)
        + overall.get("included_new_record", 0)
        == EXPECTED_REPOSITORY_ELIGIBLE,
        "eligible repository records",
    )

    access = _load_json(root, "hub/audit/access_verification_log_2026-08-02.json")
    check(access.get("record_count") == EXPECTED_RECORDS, "access-log record count")
    access_ids = {row["record_id"] for row in access.get("records", [])}
    check(access_ids == record_ids, "access-log record identity")

    url_report = _load_json(root, "hub/audit/url_report.json")
    check(url_report["summary"].get("total") == EXPECTED_RECORDS, "URL-audit count")
    check(
        url_report["metadata"].get("package_version") == RELEASE_VERSION,
        "URL-audit version",
    )

    check(_project_version(root) == RELEASE_VERSION, "pyproject version")
    check(_package_version(root) == RELEASE_VERSION, "package version")
    citation = (root / "CITATION.cff").read_text(encoding="utf-8")
    check(f'version: "{RELEASE_VERSION}"' in citation, "CITATION version")
    check(f'date-released: "{RELEASE_DATE}"' in citation, "CITATION release date")
    check("snapshot of 451" in citation, "CITATION record count")

    website_package = _load_json(root, "website/package.json")
    website_lock = _load_json(root, "website/package-lock.json")
    website_data = _load_json(root, "website/static/datasets.json")
    check(website_package.get("version") == RELEASE_VERSION, "website package version")
    check(website_lock.get("version") == RELEASE_VERSION, "website lock version")
    check(website_data.get("total") == EXPECTED_RECORDS, "website record count")

    required_text = {
        "README.md": (
            "Release 0.7.0 contains 451",
            "representing 446 narrowly defined dataset families",
            "33 use source-hosted file, Google Drive, or GitHub routes",
            "350 use repository or challenge-platform APIs or clients",
            "68 use manual, controlled, institutional, or author-contact procedures",
            "tests-146%20passing",
        ),
        "DATASETS.md": (
            "EyeDataHub 0.7.0 catalog",
            "| Current catalog records | 451 |",
            "| Narrowly defined dataset families | 446 |",
            "| Platform API or client routes | 350 |",
        ),
        "llms.txt": (
            "451 current ophthalmology data-resource records",
            "representing 446 narrowly defined dataset families",
        ),
        "website/README.md": ("451 in release 0.7.0",),
        "website/docusaurus.config.js": ("451 current ophthalmology data resources",),
        "CHANGELOG.md": ("## [0.7.0] - 2026-08-04",),
    }
    for relative, snippets in required_text.items():
        text = (root / relative).read_text(encoding="utf-8")
        for snippet in snippets:
            check(snippet in text, f"{relative}: {snippet}")

    current_public_text = "\n".join(
        (root / relative).read_text(encoding="utf-8")
        for relative in (
            "README.md",
            "DATASETS.md",
            "CITATION.cff",
            "llms.txt",
            "website/README.md",
            "website/docusaurus.config.js",
        )
    )
    for stale in ("475 current", "470 narrowly", "snapshot of 479"):
        check(stale not in current_public_text, f"stale public value: {stale}")

    return errors


def main() -> int:
    errors = collect_consistency_errors()
    if errors:
        print("Release consistency FAILED:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(
        f"Release consistency passed: {RELEASE_TAG}, {EXPECTED_RECORDS} records, "
        f"{EXPECTED_FAMILIES} families"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
