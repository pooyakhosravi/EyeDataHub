"""Source-term-aware ophthalmology dataset catalog and acquisition tool."""

__version__ = "0.2.2"
__author__ = "EyeDataHub Contributors"

# Load .env early so subsequent Kaggle / HuggingFace / PhysioNet /
# Zenodo API calls pick up user-supplied credentials.
from eyedatahub.utils.credentials import load_credentials as _load_credentials  # noqa: E402
_load_credentials()

from eyedatahub.core.dataset import (  # noqa: E402
    EyeDataHubDataset,
    DatasetInfo,
    DatasetSample,
    classify_license,
    license_matches_filter,
    license_short,
)
from eyedatahub.datasets.registry import REGISTRY  # noqa: E402

__all__ = [
    "EyeDataHubDataset",
    "DatasetInfo",
    "DatasetSample",
    "REGISTRY",
    "classify_license",
    "license_matches_filter",
    "license_short",
]
