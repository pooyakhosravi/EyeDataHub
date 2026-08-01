import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from eyedatahub.agent.planner import loader_status
from eyedatahub.datasets.registry import REGISTRY
from hub.docs.generate_dataset_pages import build_page, build_static_dataset_index
from hub.docs.generate_llms_full import build as build_llms_full


def test_generated_pages_report_loader_status_honestly():
    implemented = REGISTRY.get_dataset("airogs")
    metadata_only = REGISTRY.get_dataset("nd_iris_0405")

    assert loader_status(implemented) == "implemented"
    assert loader_status(metadata_only) == "metadata_only"

    implemented_page = build_page(implemented, REGISTRY.list_datasets())
    metadata_page = build_page(metadata_only, REGISTRY.list_datasets())

    assert "Standard loader included" in implemented_page
    assert "samples = ds.load" in implemented_page
    assert "from PIL import Image" not in implemented_page
    assert "Metadata and access only" in metadata_page
    assert "does not yet include a standard `DatasetSample` loader" in metadata_page
    assert "samples = ds.load" not in metadata_page


def test_dashboard_index_includes_loader_counts_and_status():
    payload = build_static_dataset_index(REGISTRY.list_datasets())
    rows = {row["name"]: row for row in payload["datasets"]}

    assert payload["summary"]["datasets"] == 251
    assert payload["summary"]["loaders_implemented"] == 75
    assert payload["summary"]["primary_categories"] == 18
    assert payload["summary"]["transfer_tested_routes"] == 52
    assert payload["facets"]["modality"]["fundus"] == 121
    assert payload["facets"]["modality"]["confocal"] == 5
    assert rows["airogs"]["loader_status"] == "implemented"
    assert rows["nd_iris_0405"]["loader_status"] == "metadata_only"
    assert rows["olives"]["modalities"] == ["oct", "fundus", "tabular"]
    assert rows["corn_collection"]["access_friction"] == "controlled_or_manual"


def test_llms_full_exposes_tasks_sources_access_and_loader_status(tmp_path: Path):
    output = build_llms_full(tmp_path)
    text = output.read_text(encoding="utf-8")

    assert "TASK=" in text
    assert "ACCESS=" in text
    assert "LOAD=implemented" in text
    assert "LOAD=metadata_only" in text
    assert "URL=https://" in text
    assert "ds.download(" not in text
