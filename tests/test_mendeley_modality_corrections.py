import pytest

from eyedatahub.datasets.registry import REGISTRY


@pytest.mark.parametrize(
    ("record_id", "primary_category", "contained_modalities"),
    [
        (
            "mendeley_application_machine_learning_detecting_iron_deficiency",
            "external_eye",
            {"external_eye", "tabular"},
        ),
        (
            "mendeley_code_manuscript_fixational_eye_movements_as",
            "eye_tracking",
            {"eye_tracking", "tabular"},
        ),
        (
            "mendeley_conjunctival_melanoma_detection_using_deep_learning",
            "external_eye",
            {"external_eye", "tabular"},
        ),
        (
            "mendeley_cp_anemic_conjunctival_pallor_ghana",
            "external_eye",
            {"external_eye", "tabular"},
        ),
        (
            "mendeley_development_deep_learning_based_system_optic",
            "multimodal",
            {"ocular_ultrasound", "tabular"},
        ),
        (
            "mendeley_digital_holograms_rbcs_glaucoma_patients_healthy",
            "cell_microscopy",
            {"cell_microscopy", "tabular"},
        ),
        (
            "mendeley_electrooculography_eog_blink_analysis_ocular_fatigue",
            "electrophysiology",
            {"electrophysiology", "tabular"},
        ),
        (
            "mendeley_nuclear_cataract_database_biomedical_machine_learning",
            "external_eye",
            {"external_eye", "tabular"},
        ),
        (
            "mendeley_ocular_sebaceous_neoplasms",
            "external_eye",
            {"external_eye", "cell_microscopy", "tabular"},
        ),
        (
            "mendeley_red_lesion_localization_messidor_retinal_images",
            "fundus",
            {"fundus", "tabular"},
        ),
        (
            "mendeley_retinal_blood_vessel_segmentation_rop",
            "fundus",
            {"fundus", "tabular"},
        ),
        (
            "mendeley_sub_cone_visual_resolution_by_active",
            "adaptive_optics",
            {"adaptive_optics", "eye_tracking", "tabular"},
        ),
        (
            "mendeley_two_photon_excited_fluorescence_scanning_laser",
            "fundus",
            {"fundus", "retinal_imaging", "tabular"},
        ),
        (
            "mendeley_vivo_cone_photoreceptor_topography_human_foveola",
            "adaptive_optics",
            {"adaptive_optics", "tabular"},
        ),
    ],
)
def test_source_file_evidence_drives_modality_corrections(
    record_id, primary_category, contained_modalities
):
    info = REGISTRY.get_dataset(record_id).info
    assert info.primary_category == primary_category
    assert set(info.modalities) == contained_modalities
