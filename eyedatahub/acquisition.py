"""Source-term preflight and explicit dataset acquisition.

Search and inspection APIs are read-only.  This module is the only supported
programmatic path that may invoke a dataset loader, and it does so only after an
explicit caller request and a deterministic preflight.
"""
from __future__ import annotations

import hashlib
import json
import os
import shutil
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

from eyedatahub import __version__
from eyedatahub.core.metadata import normalize_unknown


EXIT_SUCCESS = 0
EXIT_INVALID_REQUEST = 2
EXIT_MANUAL_BLOCKED = 3
EXIT_UNAVAILABLE = 4
EXIT_UNSUPPORTED = 5
EXIT_TRANSFER_FAILED = 6

MANIFEST_FILENAME = "eyedatahub-acquisition-manifest.json"

_CREDENTIAL_HINTS = {
    "kaggle": ["KAGGLE_USERNAME", "KAGGLE_KEY"],
    "huggingface": ["HF_TOKEN"],
    "physionet": ["PHYSIONET_USERNAME", "PHYSIONET_PASSWORD"],
    "zenodo": ["ZENODO_TOKEN"],
    "figshare": ["FIGSHARE_TOKEN"],
    "mendeley": ["MENDELEY_TOKEN"],
    "dataverse": ["DATAVERSE_TOKEN"],
}


@dataclass
class AcquisitionResult:
    """Structured result returned by preflight and acquisition operations."""

    record_id: str
    status: str
    exit_code: int
    dry_run: bool
    transfer_started: bool
    message: str
    preflight: Dict[str, Any]
    manifest_path: Optional[str] = None
    warnings: List[str] = field(default_factory=list)
    error_type: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return normalize_unknown(asdict(self))


def _authentication_category(info: Any) -> str:
    if info.access_friction == "anonymous_direct":
        return "none"
    if info.requires_manual_approval is True:
        return "manual_authorization"
    if info.requires_author_contact is True:
        return "author_correspondence"
    if info.requires_api_token is True:
        return "user_supplied_api_token"
    if info.requires_authentication is True:
        return "user_authenticated"
    return "unknown"


def _credential_state(info: Any) -> Dict[str, bool]:
    """Report only presence/absence; never expose credential values."""
    if info.access_friction == "anonymous_direct":
        return {}
    names = _CREDENTIAL_HINTS.get(info.loader_backend, [])
    return {name: bool(os.environ.get(name)) for name in names}


def _term_warnings(info: Any) -> List[str]:
    warnings: List[str] = [
        "EyeDataHub reports source documentation and is not legal advice.",
        "Technical availability does not establish permission or scientific suitability.",
    ]
    family = info.license_family
    if family in {
        "cc-by",
        "cc-by-sa",
        "cc-by-nc",
        "cc-by-nc-sa",
        "cc-by-nc-nd",
        "odc-by",
    }:
        warnings.append(
            "The normalized source label includes an attribution condition; consult the current source terms."
        )
    if family in {"cc-by-sa", "cc-by-nc-sa"}:
        warnings.append("The normalized source label includes a share-alike condition.")
    if family == "unknown" or info.terms_scope == "unknown":
        warnings.append(
            "Source terms or their scope are unknown; inspect the evidence URL before acquisition."
        )
    if family in {"cc-by-nc", "cc-by-nc-sa", "cc-by-nc-nd"}:
        warnings.append("The normalized source label includes a noncommercial restriction.")
    if family == "cc-by-nc-nd":
        warnings.append("The normalized source label includes a no-derivatives restriction.")
    if family == "research-only":
        warnings.append("The source-stated terms restrict use to research or an equivalent context.")
    if info.terms_scope in {"publication_only", "code_only", "mixed_components"}:
        warnings.append(
            "The recorded terms do not apply uniformly to every component; review component-level terms."
        )
    if info.requires_clickthrough is True:
        warnings.append(
            "The source requires user review or click-through; EyeDataHub does not accept terms for the user."
        )
    if info.requires_data_use_agreement is True:
        warnings.append("A source data-use agreement is recorded and must be completed outside EyeDataHub.")
    return warnings


def preflight_dataset(dataset: Any, data_dir: str | Path) -> Dict[str, Any]:
    """Return a side-effect-free acquisition plan for one catalog record."""
    info = dataset.info
    target = Path(data_dir).expanduser().resolve(strict=False)
    blocked_reason: Optional[str] = None
    exit_code = EXIT_SUCCESS
    status = "ready"

    if info.availability_status == "unavailable":
        status = "unavailable"
        exit_code = EXIT_UNAVAILABLE
        blocked_reason = info.failure_reason or "The official route was unavailable at the verification date."
    elif info.access_friction in {
        "controlled_or_manual",
        "author_contact",
        "model_to_data_or_secure_environment",
    } or info.acquisition_support == "manual_access_blocked":
        status = "manual_access_blocked"
        exit_code = EXIT_MANUAL_BLOCKED
        blocked_reason = (
            "This route requires authorization, an agreement, author contact, or a secure environment; "
            "EyeDataHub intentionally does not automate it."
        )
    elif info.acquisition_support == "guided_instructions_only":
        status = "guided_instructions_only"
        exit_code = EXIT_UNSUPPORTED
        blocked_reason = "Current official instructions are recorded, but no automated transfer is implemented."
    elif info.acquisition_support == "unsupported":
        status = "unsupported"
        exit_code = EXIT_UNSUPPORTED
        blocked_reason = "No supported automated transfer is implemented for this route."
    elif info.access_friction == "unverified" or info.availability_status == "unverified":
        status = "unverified"
        exit_code = EXIT_UNSUPPORTED
        blocked_reason = "The current official acquisition route is not verified sufficiently for automation."

    estimated_bytes = int(info.size_gb * (1024**3)) if info.size_gb else None
    family = info.license_family
    disk_free_bytes: Optional[int] = None
    disk_sufficient: Optional[bool] = None
    existing_parent = target
    while not existing_parent.exists() and existing_parent.parent != existing_parent:
        existing_parent = existing_parent.parent
    if existing_parent.exists() and existing_parent.is_dir():
        disk_free_bytes = shutil.disk_usage(existing_parent).free
        if estimated_bytes is not None:
            # Reserve 10% for archives, extraction overhead and manifests.
            disk_sufficient = disk_free_bytes >= int(estimated_bytes * 1.1)
            if disk_sufficient is False and exit_code == EXIT_SUCCESS:
                status = "insufficient_disk_space"
                exit_code = EXIT_INVALID_REQUEST
                blocked_reason = "Available disk space is below the recorded dataset size plus 10% overhead."

    return {
        "record_id": info.name,
        "canonical_name": info.full_name,
        "target_directory": str(target),
        "source_landing_page_url": info.source_landing_page_url,
        "preferred_route_type": info.preferred_route_type,
        "preferred_route_url": info.preferred_route_url,
        "availability_status": info.availability_status,
        "route_last_checked": info.route_last_checked,
        "route_check_result": info.route_check_result,
        "access_friction": info.access_friction,
        "access_requirements": {
            "requires_registration": info.requires_registration,
            "requires_authentication": info.requires_authentication,
            "requires_api_token": info.requires_api_token,
            "requires_clickthrough": info.requires_clickthrough,
            "requires_manual_approval": info.requires_manual_approval,
            "requires_data_use_agreement": info.requires_data_use_agreement,
            "requires_author_contact": info.requires_author_contact,
            "requires_payment": info.requires_payment,
            "geographic_or_institutional_restriction": info.geographic_or_institutional_restriction,
        },
        "source_terms": info.source_terms,
        "normalized_source_term_category": info.license_family,
        "terms_scope": info.terms_scope,
        "terms_evidence_url": info.terms_evidence_url,
        "source_term_flags": {
            "attribution_condition_recorded": family in {
                "cc-by", "cc-by-sa", "cc-by-nc", "cc-by-nc-sa", "cc-by-nc-nd", "odc-by"
            },
            "share_alike_condition_recorded": family in {"cc-by-sa", "cc-by-nc-sa"},
            "noncommercial_condition_recorded": family in {
                "cc-by-nc", "cc-by-nc-sa", "cc-by-nc-nd"
            },
            "no_derivatives_condition_recorded": family == "cc-by-nc-nd",
            "research_or_challenge_restriction_recorded": family == "research-only",
            "terms_or_scope_unknown": family == "unknown" or info.terms_scope == "unknown",
        },
        "acquisition_support": info.acquisition_support,
        "loader_backend": info.loader_backend,
        "loader_name": info.loader_name,
        "loader_version": info.loader_version,
        "authentication_category": _authentication_category(info),
        "credential_variables_present": _credential_state(info),
        "estimated_size_bytes": estimated_bytes,
        "disk_free_bytes": disk_free_bytes,
        "disk_sufficient": disk_sufficient,
        "status": status,
        "exit_code": exit_code,
        "automation_allowed": exit_code == EXIT_SUCCESS,
        "blocked_reason": blocked_reason,
        "warnings": _term_warnings(info),
        "explicit_command_required": True,
        "terms_accepted_by_eyedatahub": False,
    }


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _file_inventory(root: Path, *, checksums: bool) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    if not root.exists():
        return rows
    for path in sorted(item for item in root.rglob("*") if item.is_file()):
        if path.name in {MANIFEST_FILENAME, ".download_complete"}:
            continue
        row: Dict[str, Any] = {
            "path": path.relative_to(root).as_posix(),
            "size_bytes": path.stat().st_size,
            "sha256": _sha256(path) if checksums else None,
            "source_provided_checksum": None,
        }
        rows.append(row)
    return rows


def write_provenance_manifest(
    dataset: Any,
    data_dir: str | Path,
    *,
    transfer_status: str,
    checksums: bool = True,
) -> Path:
    """Write the acquisition provenance manifest beside acquired files."""
    info = dataset.info
    root = dataset.sentinel_path(data_dir).parent
    root.mkdir(parents=True, exist_ok=True)
    inventory = _file_inventory(root, checksums=checksums)
    payload = {
        "schema_version": "1.0",
        "record_id": info.name,
        "canonical_dataset_name": info.full_name,
        "eyedatahub_release_version": __version__,
        "tool_version": __version__,
        "loader": info.loader_name,
        "loader_backend": info.loader_backend,
        "loader_version": info.loader_version,
        "official_source_url": info.source_landing_page_url,
        "resolved_acquisition_url": info.preferred_route_url,
        "dataset_doi": info.dataset_doi,
        "dataset_accession": info.dataset_accession,
        "repository_record_identifier": info.repository_record_id,
        "associated_publication_doi": info.associated_publication_doi,
        "software_doi": info.software_doi,
        "challenge_identifier": info.challenge_identifier,
        "raw_source_stated_terms": info.source_terms,
        "normalized_source_term_category": info.license_family,
        "source_term_evidence_url": info.terms_evidence_url,
        "terms_scope": info.terms_scope,
        "acquisition_datetime_utc": datetime.now(timezone.utc).isoformat(),
        "authentication_category": _authentication_category(info),
        "acquired_files": inventory,
        "total_files": len(inventory),
        "total_size_bytes": sum(row["size_bytes"] for row in inventory),
        "checksums_calculated": checksums,
        "citation_guidance": info.citation,
        "warnings": _term_warnings(info),
        "transfer_status": transfer_status,
        "complete_or_partial": transfer_status,
        "third_party_data_redistributed_by_eyedatahub": False,
        "legal_advice": False,
    }
    destination = root / MANIFEST_FILENAME
    temporary = destination.with_suffix(".json.tmp")
    temporary.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    temporary.replace(destination)
    return destination


def acquire_dataset(
    dataset: Any,
    data_dir: str | Path,
    *,
    dry_run: bool = False,
    force: bool = False,
    checksums: bool = True,
) -> AcquisitionResult:
    """Run preflight and, only when explicitly requested, invoke one loader."""
    info = dataset.info
    plan = preflight_dataset(dataset, data_dir)
    warnings = list(plan["warnings"])

    if dry_run:
        return AcquisitionResult(
            record_id=info.name,
            status=plan["status"],
            exit_code=plan["exit_code"],
            dry_run=True,
            transfer_started=False,
            message=plan["blocked_reason"] or "Preflight completed; an explicit non-dry-run command is required.",
            preflight=plan,
            warnings=warnings,
        )

    if not plan["automation_allowed"]:
        return AcquisitionResult(
            record_id=info.name,
            status=plan["status"],
            exit_code=plan["exit_code"],
            dry_run=False,
            transfer_started=False,
            message=plan["blocked_reason"] or "Acquisition is blocked by preflight.",
            preflight=plan,
            warnings=warnings,
        )

    target = Path(data_dir).expanduser()
    if target.exists() and not target.is_dir():
        return AcquisitionResult(
            record_id=info.name,
            status="invalid_destination",
            exit_code=EXIT_INVALID_REQUEST,
            dry_run=False,
            transfer_started=False,
            message=f"Destination exists and is not a directory: {target}",
            preflight=plan,
            warnings=warnings,
            error_type="NotADirectoryError",
        )
    target.mkdir(parents=True, exist_ok=True)

    if not force and (dataset.sentinel_path(target).exists() or dataset.is_downloaded(target)):
        if not dataset.sentinel_path(target).exists():
            dataset.mark_downloaded(target)
        manifest = write_provenance_manifest(
            dataset, target, transfer_status="existing_complete", checksums=checksums
        )
        return AcquisitionResult(
            record_id=info.name,
            status="already_present",
            exit_code=EXIT_SUCCESS,
            dry_run=False,
            transfer_started=False,
            message="Dataset files were already present; provenance manifest refreshed.",
            preflight=plan,
            manifest_path=str(manifest),
            warnings=warnings,
        )

    try:
        dataset.download(target)
        if not dataset.is_downloaded(target):
            return AcquisitionResult(
                record_id=info.name,
                status="transfer_incomplete",
                exit_code=EXIT_TRANSFER_FAILED,
                dry_run=False,
                transfer_started=True,
                message="The loader returned, but the dataset-specific completion check did not pass.",
                preflight=plan,
                warnings=warnings,
                error_type="IncompleteTransfer",
            )
        dataset.mark_downloaded(target)
        manifest = write_provenance_manifest(
            dataset, target, transfer_status="complete", checksums=checksums
        )
        return AcquisitionResult(
            record_id=info.name,
            status="completed",
            exit_code=EXIT_SUCCESS,
            dry_run=False,
            transfer_started=True,
            message="Transfer completed and a provenance manifest was written.",
            preflight=plan,
            manifest_path=str(manifest),
            warnings=warnings,
        )
    except KeyboardInterrupt:
        return AcquisitionResult(
            record_id=info.name,
            status="interrupted",
            exit_code=EXIT_TRANSFER_FAILED,
            dry_run=False,
            transfer_started=True,
            message="Transfer was interrupted; no completion sentinel was written.",
            preflight=plan,
            warnings=warnings,
            error_type="KeyboardInterrupt",
        )
    except Exception as exc:  # loader errors are converted to stable CLI results
        return AcquisitionResult(
            record_id=info.name,
            status="failed",
            exit_code=EXIT_TRANSFER_FAILED,
            dry_run=False,
            transfer_started=True,
            message=str(exc),
            preflight=plan,
            warnings=warnings,
            error_type=type(exc).__name__,
        )
