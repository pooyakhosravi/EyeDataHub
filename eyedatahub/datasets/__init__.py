"""EyeDataHub datasets package."""
# Import registry to trigger auto-registration of all built-in datasets
from eyedatahub.datasets.registry import REGISTRY, DatasetRegistry

__all__ = [
    "REGISTRY",
    "DatasetRegistry",
]
