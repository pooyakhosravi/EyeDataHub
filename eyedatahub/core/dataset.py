"""Base dataset interface."""
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple, Union
from pathlib import Path
from PIL import Image
import numpy as np


# ---------------------------------------------------------------------------
# License classification helpers
# ---------------------------------------------------------------------------

# Map of canonical license families (lowercase keys for matching)
_LICENSE_FAMILIES: Dict[str, List[str]] = {
    # Standard source labels.  Classification does not determine permission
    # and terms scope is recorded independently.
    "cc0":          ["cc0", "public domain", "cc0 1.0"],
    "cc-by":        ["cc by 4.0", "cc by 3.0", "cc by 2.0", "cc by 1.0",
                     "creative commons attribution"],
    "cc-by-sa":     ["cc by-sa", "cc by-sa 4.0"],
    "mit":          ["mit license", "license: mit", " mit", "mit"],
    "apache":       ["apache-2.0", "apache 2.0", "apache license", "apache"],
    "odc-by":       ["odc-by", "open data commons attribution"],
    # Non-commercial Creative Commons
    "cc-by-nc":     ["cc by-nc 4.0", "cc by-nc 3.0", "cc by-nc 2.0"],
    "cc-by-nc-sa":  ["cc by-nc-sa", "cc by-nc-sa 4.0"],
    "cc-by-nc-nd":  ["cc by-nc-nd", "cc by-nc-nd 4.0"],
    # Explicit use restrictions stated by the source.
    "research-only": ["research only", "research use only", "research use",
                      "for research", "academic research", "non-commercial research",
                      "educational", "challenge-specific", "challenge data-use",
                      "non-commercial scientific use"],
    "unknown":      ["unknown", "see dataset page", "see huggingface",
                     "see dataset", "see kaggle", "see paper"],
}

# Broader groupings for the --license-type filter flag
_LICENSE_GROUPS: Dict[str, List[str]] = {
    # Descriptive grouping only: these normalized labels contain no explicit
    # noncommercial clause.  It is not a permission determination.
    "commercial-ok": ["cc0", "cc-by", "cc-by-sa", "mit", "apache", "odc-by"],
    "standard-no-nc": ["cc0", "cc-by", "cc-by-sa", "mit", "apache", "odc-by"],
    # Free but non-commercial
    "non-commercial": ["cc-by-nc", "cc-by-nc-sa", "cc-by-nc-nd"],
    # Backward-compatible legacy alias; public documentation uses descriptive
    # source-term labels instead of calling this group "open".
    "open": ["cc0", "cc-by", "cc-by-sa", "mit", "apache", "odc-by", "cc-by-nc", "cc-by-nc-sa", "cc-by-nc-nd"],
    # Fully restricted
    "research-only": ["research-only"],
    # Unknown / unclear
    "unknown": ["unknown"],
}

_EXPLICIT_UNCERTAINTY_MARKERS = (
    "unknown",
    "needs check",
    "verify",
    "mixed",
    "no license",
    "unclear",
)


def classify_license(license_str: str) -> str:
    """
    Return the canonical license-family key for *license_str*.

    Returns one of: cc0, cc-by, cc-by-sa, mit, apache, odc-by, cc-by-nc,
    cc-by-nc-sa, cc-by-nc-nd, research-only, unknown.
    """
    ls = license_str.lower()
    # Explicit uncertainty takes precedence over incidental license-like text.
    # For example, ``Unknown (article CC BY-NC-ND)`` describes an unknown
    # dataset license; the publication license must not be inherited by the
    # dataset record.
    if any(pattern in ls for pattern in _EXPLICIT_UNCERTAINTY_MARKERS):
        return "unknown"
    for family, patterns in _LICENSE_FAMILIES.items():
        if family == "unknown":
            continue
        if any(p in ls for p in patterns):
            return family
    return "unknown"


def license_matches_filter(license_str: str, filter_key: str) -> bool:
    """
    Return True if *license_str* belongs to the requested filter group.

    filter_key can be:
      - a family name  (cc-by, cc-by-nc, cc0, research-only, …)
      - a group name   (standard-no-nc, non-commercial)
      - "any" / "all"  — always True
    """
    if filter_key.lower() in ("any", "all", ""):
        return True
    family = classify_license(license_str)
    if filter_key.lower() == family:
        return True
    group = _LICENSE_GROUPS.get(filter_key.lower(), [])
    return family in group


def license_short(license_str: str) -> str:
    """Return a short display string for a license (≤ 16 chars)."""
    # MIT gets its own display before family lookup
    if license_str.strip().upper() == "MIT":
        return "MIT"
    family = classify_license(license_str)
    _DISPLAY = {
        "cc0":          "CC0",
        "cc-by":        "CC BY",
        "cc-by-sa":     "CC BY-SA",
        "mit":          "MIT",
        "apache":       "Apache",
        "odc-by":       "ODC-BY",
        "cc-by-nc":     "CC BY-NC",
        "cc-by-nc-sa":  "CC BY-NC-SA",
        "cc-by-nc-nd":  "CC BY-NC-ND",
        "research-only": "Research only",
        "unknown":      "?",
    }
    display = _DISPLAY.get(family, "?")
    # Preserve version if present
    import re
    m = re.search(r"\b(\d\.\d)\b", license_str)
    if m and family not in ("research-only", "unknown"):
        display = f"{display} {m.group(1)}"
    return display


@dataclass
class DatasetInfo:
    """Metadata about a dataset."""
    name: str
    full_name: str
    description: str
    modality: str  # "fundus", "oct", "visual_field", "slit_lamp", "multimodal"
    tasks: List[str]  # list of: "classification", "segmentation", "grading", "multilabel", "regression"
    num_samples: Optional[int]
    splits: List[str]  # ["train", "val", "test"] or subset
    classes: Optional[List[str]] = None
    num_classes: Optional[int] = None
    image_size: Optional[Tuple[int, int]] = None  # typical image size
    download_type: str = "direct"  # direct, named repository backend, or manual
    download_url: Optional[str] = None
    license: str = "Unknown"
    citation: str = ""
    tags: List[str] = field(default_factory=list)
    size_gb: Optional[float] = None  # approximate download size in GB
    notes: str = ""

    # Rich catalog and acquisition metadata.  These fields remain optional at
    # class-definition time so historical dataset classes stay compatible;
    # ``__post_init__`` fills conservative values and preserves unknowns.
    primary_category: str = ""
    modalities: List[str] = field(default_factory=list)
    item_count_unit: str = ""
    source_landing_page_url: Optional[str] = None
    preferred_route_type: str = ""
    preferred_route_url: Optional[str] = None
    access_friction: str = ""
    requires_registration: Optional[bool] = None
    requires_authentication: Optional[bool] = None
    requires_api_token: Optional[bool] = None
    requires_clickthrough: Optional[bool] = None
    requires_manual_approval: Optional[bool] = None
    requires_data_use_agreement: Optional[bool] = None
    requires_author_contact: Optional[bool] = None
    requires_payment: Optional[bool] = None
    geographic_or_institutional_restriction: str = "unknown"
    availability_status: str = ""
    route_last_checked: Optional[str] = None
    route_check_result: str = ""
    route_check_notes: str = ""
    acquisition_support: str = ""
    loader_backend: str = ""
    loader_name: str = ""
    loader_version: Optional[str] = None
    loader_live_tested: Optional[bool] = None
    loader_test_date: Optional[str] = None
    loader_test_scope: str = ""
    loader_test_result: str = ""
    tested_command: Optional[str] = None
    failure_reason: Optional[str] = None
    source_terms: Optional[str] = None
    terms_evidence_url: Optional[str] = None
    terms_scope: str = ""
    terms_component_notes: str = ""
    dataset_doi: Optional[str] = None
    dataset_accession: Optional[str] = None
    repository_record_id: Optional[str] = None
    associated_publication_doi: Optional[str] = None
    software_doi: Optional[str] = None
    challenge_identifier: Optional[str] = None
    resource_version: Optional[str] = None
    canonical_resolver_url: Optional[str] = None
    relationships: List[Dict[str, str]] = field(default_factory=list)
    item_count_evidence_url: Optional[str] = None
    modality_evidence_url: Optional[str] = None
    task_evidence_url: Optional[str] = None
    citation_evidence_url: Optional[str] = None
    author_source_checked: Optional[bool] = None
    source_check_date: Optional[str] = None
    source_check_status: str = ""
    independent_audit_status: str = ""
    access_check_status: str = ""
    transfer_check_status: str = ""

    def __post_init__(self) -> None:
        from eyedatahub.core.metadata import enrich_dataset_info

        enrich_dataset_info(self)

    @property
    def license_family(self) -> str:
        """Canonical license family key (e.g. 'cc-by', 'research-only')."""
        return classify_license(self.license)

    @property
    def license_display(self) -> str:
        """Short display string for the license (≤ 18 chars)."""
        return license_short(self.license)


@dataclass
class DatasetSample:
    """A single sample from a dataset."""
    image_path: str
    label: Any  # int, List[int], np.ndarray (mask), float
    sample_id: str = ""
    metadata: Dict[str, Any] = field(default_factory=dict)


class EyeDataHubDataset(ABC):
    """
    Base class for all EyeDataHub datasets.

    Each dataset must implement:
    - info: DatasetInfo property
    - is_downloaded(data_dir): check if data is present
    - download(data_dir): download and extract data
    - load(data_dir, split): return list of DatasetSample
    """

    # Sentinel filename written after a successful download so that subsequent
    # runs skip straight past the (potentially slow) is_downloaded() check.
    _SENTINEL = ".download_complete"

    def sentinel_path(self, data_dir: Union[str, Path]) -> Path:
        """Return the path to this dataset's download-complete sentinel file."""
        subdir = getattr(self, "_SUBDIR", self.info.name)
        return Path(data_dir).expanduser() / subdir / self._SENTINEL

    def mark_downloaded(self, data_dir: Union[str, Path]) -> None:
        """Write the sentinel file to indicate a successful download."""
        import datetime
        sp = self.sentinel_path(data_dir)
        sp.parent.mkdir(parents=True, exist_ok=True)
        sp.write_text(
            f"downloaded: {datetime.datetime.now().isoformat()}\n"
            f"dataset: {self.info.name}\n"
        )

    @property
    @abstractmethod
    def info(self) -> DatasetInfo:
        """Return dataset metadata."""
        pass

    @abstractmethod
    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        """Check if the dataset is already downloaded."""
        pass

    @abstractmethod
    def download(self, data_dir: Union[str, Path]) -> None:
        """Download and extract the dataset to data_dir."""
        pass

    @abstractmethod
    def load(self, data_dir: Union[str, Path], split: str = "test") -> List[DatasetSample]:
        """
        Load dataset samples.

        Args:
            data_dir: Root data directory
            split: One of the dataset's available splits

        Returns:
            List of DatasetSample objects
        """
        pass

    def load_image(self, path: str) -> Image.Image:
        """Load an image from path."""
        return Image.open(path).convert("RGB")

    def load_mask(self, path: str) -> np.ndarray:
        """Load a binary mask from path."""
        img = Image.open(path).convert("L")
        arr = np.array(img)
        return (arr > 127).astype(np.uint8)
