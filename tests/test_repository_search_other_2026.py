from eyedatahub.datasets.repository_search_other_2026 import (
    ACCEPTED_SOURCE_IDS,
    OTHER_REPOSITORY_RECORDS,
)


EXPECTED_ACCEPTED_SOURCE_IDS = {
    "10247501", "12443594", "16545561", "16828996", "17113883",
    "19598133", "20113592", "21197173", "22246969", "22518010",
    "22736687", "24138420", "26172919", "26395018", "27907056",
    "28176839", "28189571", "29302664", "30102802", "30143461",
    "30491856", "30520733", "30750011", "31364760", "31385596",
    "31981347", "31981557", "32051124", "32054064", "32086296",
    "3209908", "32509329", "32576697", "32833895", "32873501",
    "3917574", "BharathK333/DOOMGAN-Ocular-Morphs",
    "serag-ai/Synthetic-Ophthalmology-Images",
    "yuzhench/glaucoma-expert-cot-raw-1077",
    "yuzhench/glaucoma-expert-cot-refined-1077",
    "arwabasal/itec-iris-and-pupil-segmentation",
    "clerimar/brasil-glaucoma-brg",
    "cnzakimuena/retinal-oct-and-octa-data-3",
    "hindsaud/datasets-higancnn-glaucoma-detection",
    "michachwesiuk/hybridgaze", "zhangyiyinge/gleam-dataset",
}


def test_reconciled_source_id_accounting_is_exact():
    assert set(ACCEPTED_SOURCE_IDS) == EXPECTED_ACCEPTED_SOURCE_IDS
    assert len(ACCEPTED_SOURCE_IDS) == 46
    assert len(set(ACCEPTED_SOURCE_IDS)) == 46


def test_reconciled_record_slugs_are_unique():
    slugs = [record["name"] for record in OTHER_REPOSITORY_RECORDS]
    assert len(slugs) == 46
    assert len(slugs) == len(set(slugs))
    assert "natural_scene_eye_tracking_outdoor_1" not in slugs
    assert "natural_scene_eye_tracking_indoor_3" not in slugs


def test_follow_up_preserves_only_supported_relationships_and_components():
    by_name = {record["name"]: record for record in OTHER_REPOSITORY_RECORDS}

    assert by_name["rop_vl"]["relationships"] == []
    component_ids = {
        source["identifier"]
        for source in by_name["natural_scene_eye_tracking_collection"][
            "alternate_sources"
        ]
    }
    assert component_ids == {
        "30520775",
        "30520829",
        "30520892",
        "30520925",
        "30520979",
    }
    higan_targets = {
        relationship["target"]
        for relationship in by_name["higancnn_generated_glaucoma"]["relationships"]
    }
    assert higan_targets == {"acrima", "drishti_gs", "hrf"}
