"""Promote a completed private review proposal to a public decision ledger.

The input is a curator-facing JSON proposal under the ignored ``.audit-work``
directory.  The output contains only record-level decisions and public evidence.
It rejects credential-bearing fields, signed links, and local absolute paths so
that review ledgers can be committed without exposing workstation details.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any


WINDOWS_ABSOLUTE_PATH = re.compile(r"(?i)(?:^|[\"'])[a-z]:[\\/]")
POSIX_PRIVATE_PATH = re.compile(r"(?:^|[\"'])/(?:home|users|root|tmp)/")
SIGNED_URL_MARKERS = (
    "x-amz-signature=",
    "x-amz-credential=",
    "sig=",
    "signature=",
    "token=",
    "access_token=",
)
FORBIDDEN_KEY_FRAGMENTS = (
    "credential_value",
    "api_key",
    "access_token",
    "refresh_token",
    "client_secret",
    "password",
)


def _walk(value: Any, *, path: str = "root") -> None:
    if isinstance(value, dict):
        for key, item in value.items():
            lowered = str(key).lower()
            if any(fragment in lowered for fragment in FORBIDDEN_KEY_FRAGMENTS):
                raise ValueError(f"Forbidden credential-bearing field at {path}.{key}")
            _walk(item, path=f"{path}.{key}")
        return
    if isinstance(value, list):
        for index, item in enumerate(value):
            _walk(item, path=f"{path}[{index}]")
        return
    if not isinstance(value, str):
        return
    lowered = value.lower()
    if WINDOWS_ABSOLUTE_PATH.search(value) or POSIX_PRIVATE_PATH.search(value):
        raise ValueError(f"Local absolute path found at {path}")
    if any(marker in lowered for marker in SIGNED_URL_MARKERS):
        raise ValueError(f"Signed or credential-bearing URL found at {path}")


def promote(
    *,
    input_paths: list[Path],
    output_path: Path,
    records_key: str,
    id_field: str,
    decision_field: str,
    expected_count: int,
    passthrough_fields: list[str] | None = None,
) -> dict[str, Any]:
    sources = [
        json.loads(input_path.read_text(encoding="utf-8"))
        for input_path in input_paths
    ]
    record_batches = [source.get(records_key) for source in sources]
    if any(not isinstance(records, list) for records in record_batches):
        raise ValueError(f"Input field {records_key!r} must be a list")
    records = [record for batch in record_batches for record in batch]
    identifiers = [str(record.get(id_field) or "") for record in records]
    if len(records) != expected_count or len(set(identifiers)) != expected_count:
        raise ValueError(
            f"Expected {expected_count} unique rows, observed "
            f"{len(records)} rows and {len(set(identifiers))} identifiers"
        )
    if any(not identifier for identifier in identifiers):
        raise ValueError(f"Every row must contain {id_field!r}")
    if any(not record.get(decision_field) for record in records):
        raise ValueError(f"Every row must contain {decision_field!r}")
    _walk(records)

    payload = {
        "schema_version": "1.0",
        "review_date": max(
            str(source.get("review_date") or "") for source in sources
        ),
        "status": "completed_record_level_manual_review",
        "source_ledgers": [input_path.name for input_path in input_paths],
        "scope": [source.get("scope") for source in sources],
        "criteria": [
            source.get("criteria")
            for source in sources
            if source.get("criteria") is not None
        ],
        "record_count": len(records),
        "unique_record_ids": len(set(identifiers)),
        "decision_counts": dict(
            sorted(Counter(str(record[decision_field]) for record in records).items())
        ),
        "credential_values_serialized": False,
        "signed_or_download_urls_serialized": False,
        "local_absolute_paths_serialized": False,
        "participant_values_serialized": False,
        "records": sorted(records, key=lambda record: str(record[id_field])),
    }
    passthrough_fields = passthrough_fields or []
    for field in passthrough_fields:
        values = [source[field] for source in sources if field in source]
        if not values:
            raise ValueError(f"Requested passthrough field {field!r} is absent")
        if len(values) != 1:
            raise ValueError(
                f"Passthrough field {field!r} is ambiguous across multiple inputs"
            )
        _walk(values[0], path=f"passthrough.{field}")
        payload[field] = values[0]
    output_path.parent.mkdir(parents=True, exist_ok=True)
    temporary = output_path.with_suffix(output_path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(payload, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )
    temporary.replace(output_path)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, nargs="+", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--records-key", default="records")
    parser.add_argument("--id-field", default="record_id")
    parser.add_argument("--decision-field", default="decision")
    parser.add_argument("--expected-count", type=int, required=True)
    parser.add_argument(
        "--passthrough-field",
        action="append",
        default=[],
        help="Copy one safe top-level input field into the public artifact.",
    )
    args = parser.parse_args()
    payload = promote(
        input_paths=args.input,
        output_path=args.output,
        records_key=args.records_key,
        id_field=args.id_field,
        decision_field=args.decision_field,
        expected_count=args.expected_count,
        passthrough_fields=args.passthrough_field,
    )
    print(json.dumps({
        "record_count": payload["record_count"],
        "decision_counts": payload["decision_counts"],
    }, indent=2))


if __name__ == "__main__":
    main()
