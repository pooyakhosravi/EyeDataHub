"""Dataset dates, with source evidence, date basis, and partial precision.

Curators prefer the original provider and may use a verified associated
publication as a fallback. Each entry records what its date represents.
Curated values ship with the package; reads are offline.
"""

from __future__ import annotations

import calendar
import json
import re
from datetime import date
from functools import lru_cache
from importlib.resources import files
from typing import Any
from urllib.parse import urlparse

PUBLICATION_DATE_FIELDS = (
    "publication_date",
    "publication_date_precision",
    "publication_date_source_url",
    "publication_date_source_field",
    "publication_date_scope",
    "publication_date_reviewed_on",
    "publication_date_notes",
)

PUBLICATION_DATE_SCOPE_LABELS = {
    "initial_public_release": "Initial dataset release",
    "repository_deposit": "Repository deposit",
    "associated_publication": "Associated publication",
}


def publication_date_basis(scope: str | None) -> str:
    """Human-readable meaning of a selected date."""
    return PUBLICATION_DATE_SCOPE_LABELS.get(scope, "Unknown")


def date_interval(value: str) -> tuple[date, date]:
    """Return inclusive bounds for a real ISO year, month, or calendar date."""
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}(?:-\d{2}){0,2}", value):
        raise ValueError("Use YYYY, YYYY-MM, or YYYY-MM-DD for publication dates.")
    parts = [int(part) for part in value.split("-")]
    year = parts[0]
    month = parts[1] if len(parts) >= 2 else 1
    start = date(year, month, parts[2] if len(parts) == 3 else 1)
    if len(parts) == 1:
        end = date(year, 12, 31)
    elif len(parts) == 2:
        end = date(year, month, calendar.monthrange(year, month)[1])
    else:
        end = start
    return start, end


def publication_date_errors(info: Any) -> list[str]:
    """Validate date/evidence coherence without manufacturing missing fields."""
    value = info.publication_date
    if value is None:
        return (
            ["publication date evidence requires publication_date"]
            if any(
                getattr(info, field) is not None
                for field in PUBLICATION_DATE_FIELDS[1:]
            )
            else []
        )
    errors = []
    try:
        date_interval(value)
    except (TypeError, ValueError):
        return ["publication_date must be a valid YYYY, YYYY-MM, or YYYY-MM-DD"]
    expected = {4: "year", 7: "month", 10: "day"}[len(value)]
    if info.publication_date_precision != expected:
        errors.append("publication_date_precision must match publication_date")
    source_url = info.publication_date_source_url
    try:
        parsed = urlparse(source_url if isinstance(source_url, str) else "")
    except ValueError:
        parsed = urlparse("")
    if (
        parsed.scheme not in {"https", "http"}
        or not parsed.netloc
        or parsed.username
        or parsed.password
    ):
        errors.append(
            "publication_date_source_url must be a public HTTP(S) evidence URL"
        )
    source_field = info.publication_date_source_field
    if not isinstance(source_field, str) or not source_field.strip():
        errors.append("publication_date_source_field is required for a known date")
    if info.publication_date_notes is not None and not isinstance(
        info.publication_date_notes, str
    ):
        errors.append("publication_date_notes must be a string or null")
    if not isinstance(info.publication_date_scope, str) or (
        info.publication_date_scope not in PUBLICATION_DATE_SCOPE_LABELS
    ):
        errors.append("publication_date_scope must name a supported date basis")
    elif info.publication_date_scope != "initial_public_release" and (
        not isinstance(info.publication_date_notes, str)
        or not info.publication_date_notes.strip()
    ):
        errors.append("publication_date_notes must explain the fallback date")
    try:
        reviewed = info.publication_date_reviewed_on
        if not isinstance(reviewed, str) or len(reviewed) != 10:
            raise ValueError
        date_interval(reviewed)
        if date_interval(value)[0] > date.fromisoformat(reviewed):
            errors.append("publication_date cannot be later than its review date")
    except ValueError:
        errors.append("publication_date_reviewed_on must be YYYY-MM-DD")
    return errors


@lru_cache(maxsize=1)
def reviewed_publication_dates() -> dict[str, dict[str, Any]]:
    """Read the packaged, source-checked date entries once, without network I/O."""
    resource = files("eyedatahub.core").joinpath("publication_dates.json")
    return json.loads(resource.read_text(encoding="utf-8"))["records"]


def enrich_publication_date(info: Any) -> None:
    """Apply a curated entry only if the dataset class supplied no date fields."""
    if not any(getattr(info, field) is not None for field in PUBLICATION_DATE_FIELDS):
        entry = reviewed_publication_dates().get(info.name, {})
        for field in PUBLICATION_DATE_FIELDS:
            setattr(info, field, entry.get(field))


def publication_fields(info: Any) -> dict[str, Any]:
    return {field: getattr(info, field) for field in PUBLICATION_DATE_FIELDS}
