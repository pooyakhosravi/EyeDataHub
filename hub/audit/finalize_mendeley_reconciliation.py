"""Apply the final conservative human-provenance review to Mendeley rows.

Three records passed the initial title/file-listing screen but did not provide
enough public source evidence to confirm that the deposited observations were
human or human-derived.  They therefore remain in the search ledger and are
excluded from the canonical catalog rather than being inferred into scope.
"""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "hub" / "audit" / "mendeley_canonical_reconciliation_2026-08-02.json"

WITHHELD: dict[str, str] = {
    "2wxnrd832j": (
        "The source lists AMD OCT/fundus material but does not explicitly confirm "
        "human or human-derived provenance in the reviewed public evidence."
    ),
    "6rxy66854k": (
        "The source lists refractive-status and corneal-biomechanics observations "
        "but does not explicitly confirm human provenance in the reviewed evidence."
    ),
    "vcv2893vyz": (
        "The indexed description implies geographic-atrophy cases but does not "
        "explicitly establish human provenance or the deposited row structure."
    ),
}


def finalize(path: Path = PATH) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    rows = payload["records"]
    indexed = {str(row["stable_id"]): row for row in rows}
    missing = sorted(set(WITHHELD) - set(indexed))
    if missing:
        raise ValueError(f"Missing Mendeley reconciliation rows: {missing}")

    for stable_id, reason in WITHHELD.items():
        row = indexed[stable_id]
        original_action = row.get("canonical_action")
        if original_action not in {"new_canonical_record", "exclude_after_reconciliation"}:
            raise ValueError(
                f"Unexpected original action for {stable_id}: {original_action}"
            )
        row.update(
            {
                "canonical_action": "exclude_after_reconciliation",
                "canonical_target": None,
                "relationship_type": None,
                "related_targets": [],
                "concise_reason": reason,
                "confidence": "High",
                "final_screening_decision": (
                    "excluded_insufficient_source_metadata"
                ),
            }
        )

    payload["decision_counts"] = dict(
        sorted(Counter(str(row["canonical_action"]) for row in rows).items())
    )
    payload["post_reconciliation_amendments"] = [
        {
            "stable_id": stable_id,
            "final_screening_decision": "excluded_insufficient_source_metadata",
            "reason": reason,
        }
        for stable_id, reason in sorted(WITHHELD.items())
    ]
    unresolved = [
        value
        for value in payload.get("unresolved_mappings", [])
        if not str(value).startswith("2wxnrd832j:")
    ]
    payload["unresolved_mappings"] = unresolved
    payload["status"] = "completed_canonical_reconciliation"

    expected = {
        "alternate_source_to_existing": 1,
        "exclude_after_reconciliation": 29,
        "new_canonical_record": 110,
    }
    if payload["decision_counts"] != expected:
        raise ValueError(
            f"Unexpected final Mendeley reconciliation counts: "
            f"{payload['decision_counts']}"
        )

    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(payload, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )
    temporary.replace(path)
    return payload


if __name__ == "__main__":
    result = finalize()
    print(json.dumps(result["decision_counts"], indent=2))
