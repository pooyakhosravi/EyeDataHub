import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from eyedatahub.agent.planner import loader_status  # noqa: E402
from eyedatahub.core.relationships import RELATIONSHIP_EVIDENCE  # noqa: E402
from eyedatahub.datasets.registry import REGISTRY  # noqa: E402
from hub.docs.generate_dataset_pages import (  # noqa: E402
    build_datasets_root,
    build_modality_index,
    build_page,
    build_static_dataset_index,
)
from hub.docs.generate_llms_full import build as build_llms_full  # noqa: E402


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

    assert payload["summary"]["datasets"] == 475
    assert payload["summary"]["dataset_families"] == 470
    assert payload["summary"]["loaders_implemented"] == 72
    assert payload["summary"]["primary_categories"] == 18
    assert payload["summary"]["transfer_tested_routes"] == 54
    assert payload["facets"]["modality"]["fundus"] == 139
    assert payload["facets"]["modality"]["confocal"] == 6
    assert rows["airogs"]["loader_status"] == "implemented"
    assert rows["nd_iris_0405"]["loader_status"] == "metadata_only"
    assert rows["olives"]["modalities"] == ["oct", "fundus", "tabular"]
    assert rows["corn_collection"]["access_friction"] == "controlled_or_manual"
    assert rows["olives"]["item_count_unit"] == "b_scans"
    assert rows["olives"]["reported_quantities"][0]["unit"] == "b_scans"
    assert any(
        relationship["relationship_type"] == "derived_from"
        and relationship["target_name"] == "odir2019"
        and relationship["target_doc_path"] == "/datasets/odir2019"
        and relationship["evidence_url"].startswith("https://")
        for relationship in rows["aod"]["relationships"]
    )
    assert any(
        relationship["direction"] == "incoming"
        and relationship["target_name"] == "aod"
        for relationship in rows["odir2019"]["relationships"]
    )
    moorfields = rows["dryad_namd_oct_quant"]["relationships"]
    fellow_eye_links = [
        relationship
        for relationship in moorfields
        if relationship["relationship_type"] == "same_or_overlapping_cohort_as"
        and relationship["target_name"] == "dryad_moorfields_namd_fellow_eye"
    ]
    assert len(fellow_eye_links) == 1
    assert fellow_eye_links[0]["direction"] == "symmetric"
    assert payload["summary"]["documented_relationship_edges"] == len(RELATIONSHIP_EVIDENCE)
    assert payload["summary"]["datasets_with_documented_relationships"] > 0
    assert payload["facets"]["relationship_type"]["derived_from"] > 0
    assert payload["facets"]["resource_role"]["annotation_layer"] == 17
    assert rows["refuge2"]["dataset_family_id"] == "refuge2"
    assert rows["corn1500"]["dataset_family_id"] == "corn_collection"


def test_quantity_indexes_do_not_sum_unlike_primary_units():
    aod = REGISTRY.get_dataset("aod")
    odir = REGISTRY.get_dataset("odir2019")

    modality_page = build_modality_index("test", [aod, odir])
    root_page = build_datasets_root([aod, odir])

    assert "Primary quantity" in modality_page
    assert "14,813 images" in modality_page
    assert "8,000 participants" in modality_page
    assert "22,813 samples" not in modality_page
    assert "mixed source reported records" not in root_page
    assert "not summed across the catalog" in root_page
    assert "Primary reported quantity units" in root_page
    assert "`images`" in root_page
    assert "`participants`" in root_page


def test_llms_full_exposes_tasks_sources_access_and_loader_status(tmp_path: Path):
    output = build_llms_full(tmp_path)
    text = output.read_text(encoding="utf-8")

    assert "TASK=" in text
    assert "ACCESS=" in text
    assert "LOAD=implemented" in text
    assert "LOAD=metadata_only" in text
    assert "URL=https://" in text
    assert "324 with a primary reported quantity" in text
    assert "475 current records in 470 dataset families" in text
    assert "ROLE=annotation_layer" in text
    assert "N=69_b_scans" in text
    assert "mixed source records" not in text
    assert "ds.download(" not in text
