"""Inventory the separable human components of the Duke Fang SBSDI archive.

The source ZIP mixes human, human-derived synthetic, nonhuman, software, and
demonstration components. This audit reads only the remote ZIP directory by
HTTP range request. It does not download or retain image content.
"""

from __future__ import annotations

import argparse
import json
import struct
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import requests


ROOT = Path(__file__).resolve().parents[2]
SOURCE_PAGE = "https://people.duke.edu/~sf59/Fang_TMI_2013.htm"
ARCHIVE_URL = (
    "https://people.duke.edu/~sf59/Datasets/Final_Publication_2013_SBSDI.zip"
)
DEFAULT_OUTPUT = (
    ROOT / "hub" / "audit" / "fang_sbsdi_component_inventory_2026-08-02.json"
)
TAIL_BYTES = 131_072


def _range_get(
    session: requests.Session,
    url: str,
    start: int,
    end: int,
) -> bytes:
    response = session.get(
        url,
        headers={"Range": f"bytes={start}-{end}"},
        timeout=60,
    )
    response.raise_for_status()
    if response.status_code != 206:
        raise RuntimeError("The source server did not honor the ZIP range request")
    return response.content


def _remote_zip_listing(url: str) -> tuple[str, int, list[dict[str, Any]]]:
    session = requests.Session()
    response = session.head(url, allow_redirects=True, timeout=30)
    response.raise_for_status()
    resolved_url = response.url
    archive_bytes = int(response.headers["content-length"])
    tail_start = max(0, archive_bytes - TAIL_BYTES)
    tail = _range_get(session, resolved_url, tail_start, archive_bytes - 1)
    end_position = tail.rfind(b"PK\x05\x06")
    if end_position < 0:
        raise RuntimeError("ZIP end-of-central-directory record was not found")
    end_record = tail[end_position : end_position + 22]
    (
        signature,
        disk_number,
        directory_disk,
        entries_on_disk,
        entry_count,
        directory_bytes,
        directory_offset,
        _comment_bytes,
    ) = struct.unpack("<4s4H2LH", end_record)
    if signature != b"PK\x05\x06" or disk_number or directory_disk:
        raise RuntimeError("Unsupported split or malformed source ZIP")
    if entries_on_disk != entry_count:
        raise RuntimeError("Source ZIP directory entry count is inconsistent")
    directory = _range_get(
        session,
        resolved_url,
        directory_offset,
        directory_offset + directory_bytes - 1,
    )

    entries: list[dict[str, Any]] = []
    position = 0
    for index in range(entry_count):
        values = struct.unpack_from("<4s6H3L5H2L", directory, position)
        if values[0] != b"PK\x01\x02":
            raise RuntimeError(f"Malformed ZIP central entry {index + 1}")
        flags = values[3]
        uncompressed_bytes = values[9]
        filename_bytes = values[10]
        extra_bytes = values[11]
        comment_bytes = values[12]
        encoded_name = directory[
            position + 46 : position + 46 + filename_bytes
        ]
        name = encoded_name.decode(
            "utf-8" if flags & 0x800 else "cp437",
            errors="replace",
        )
        position += 46 + filename_bytes + extra_bytes + comment_bytes
        entries.append(
            {
                "path": name,
                "uncompressed_bytes": uncompressed_bytes,
                "is_directory": name.endswith("/"),
            }
        )
    if position != len(directory):
        raise RuntimeError("ZIP central-directory length is inconsistent")
    return resolved_url, archive_bytes, entries


def _component(path: str) -> str:
    if "/For real experiments on Humans/" in path:
        return "real_human_images"
    if "/For synthetic experiments/" in path:
        return "human_derived_synthetic_images"
    if "/Images for Dictionaries and Mapping leraning/" in path:
        return "human_derived_dictionary_training_images"
    if "/For real experiments on Mouse/" in path:
        return "nonhuman_images_excluded_from_catalog_scope"
    return "software_models_and_demonstration_files"


def build(url: str) -> dict[str, Any]:
    resolved_url, archive_bytes, entries = _remote_zip_listing(url)
    files = [entry for entry in entries if not entry["is_directory"]]
    components: list[dict[str, Any]] = []
    for component_name in sorted({_component(entry["path"]) for entry in files}):
        component_files = [
            entry for entry in files if _component(entry["path"]) == component_name
        ]
        extensions = Counter(
            Path(entry["path"]).suffix.lower() or "[none]"
            for entry in component_files
        )
        components.append(
            {
                "component": component_name,
                "file_count": len(component_files),
                "uncompressed_bytes": sum(
                    entry["uncompressed_bytes"] for entry in component_files
                ),
                "file_extensions": dict(sorted(extensions.items())),
            }
        )

    scoped_names = {
        "real_human_images",
        "human_derived_synthetic_images",
        "human_derived_dictionary_training_images",
    }
    scoped = [row for row in components if row["component"] in scoped_names]
    scoped_image_count = sum(row["file_count"] for row in scoped)
    scoped_uncompressed_bytes = sum(row["uncompressed_bytes"] for row in scoped)
    if scoped_image_count != 323:
        raise RuntimeError(
            f"Expected 323 scoped human or human-derived images, observed "
            f"{scoped_image_count}"
        )
    return {
        "schema_version": "1.0",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "record_id": "fang_sbsdi_oct",
        "official_source_page": SOURCE_PAGE,
        "resolved_archive_url": resolved_url,
        "archive_bytes": archive_bytes,
        "archive_entry_count": len(entries),
        "archive_file_count": len(files),
        "catalog_scope": (
            "Separately named real-human, human-derived synthetic, and "
            "human-derived dictionary-training image components."
        ),
        "catalog_scoped_image_count": scoped_image_count,
        "catalog_scoped_uncompressed_bytes": scoped_uncompressed_bytes,
        "components": components,
        "archive_content_downloaded": False,
        "remote_zip_directory_reviewed": True,
        "local_dataset_files_retained": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url", default=ARCHIVE_URL)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = build(args.url)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    temporary = args.output.with_suffix(args.output.suffix + ".tmp")
    temporary.write_text(
        json.dumps(payload, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )
    temporary.replace(args.output)
    print(
        f"Inventoried {payload['archive_file_count']} files; "
        f"{payload['catalog_scoped_image_count']} human or human-derived "
        "images are in catalog scope."
    )


if __name__ == "__main__":
    main()
