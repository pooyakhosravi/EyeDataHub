"""Write the complete EyeDataHub catalog to stable JSON and CSV exports."""

from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any

from eyedatahub import __version__
from eyedatahub.catalog import info_to_record
from eyedatahub.datasets.registry import REGISTRY


CATALOG_CUTOFF = "2026-08-02"
CATALOG_RECORD_COUNT = 475


def _csv_value(value: Any) -> Any:
    if isinstance(value, (list, dict)):
        return json.dumps(value, ensure_ascii=False, sort_keys=True)
    return value


def export_catalog(out_dir: Path | None = None) -> tuple[Path, Path]:
    """Export all records without filtering by source terms or access route."""
    target = out_dir or Path(__file__).resolve().parent
    target.mkdir(parents=True, exist_ok=True)

    records = [
        info_to_record(dataset.info)
        for dataset in sorted(REGISTRY.list_datasets(), key=lambda item: item.info.name)
    ]
    if len(records) != CATALOG_RECORD_COUNT:
        raise RuntimeError(
            f"Expected {CATALOG_RECORD_COUNT} records, found {len(records)}"
        )
    payload = {
        "schema_version": "1.0",
        "catalog_version": __version__,
        "catalog_search_cutoff": CATALOG_CUTOFF,
        "record_count": len(records),
        "primary_category_count": len({record["primary_category"] for record in records}),
        "scope": "complete_catalog",
        "third_party_dataset_files_included": False,
        "records": records,
    }

    json_path = target / "catalog.json"
    csv_path = target / "catalog.csv"
    json_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    fieldnames = list(records[0]) if records else []
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for record in records:
            writer.writerow({key: _csv_value(record.get(key)) for key in fieldnames})

    print(f"Wrote {len(records)} complete catalog records to {json_path} and {csv_path}")
    return json_path, csv_path


if __name__ == "__main__":
    export_catalog()
