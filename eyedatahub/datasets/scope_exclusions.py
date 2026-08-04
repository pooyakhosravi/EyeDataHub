"""Curated records retained in source history but excluded from the catalog.

The public registry is focused on human and human-derived resources that can
support ophthalmic model development or evaluation. It also exposes only the
current canonical record for a version chain or an unmodified alternate
deposit. Excluded records remain in their source modules and dated screening
ledgers so every decision is transparent and reversible.
"""

from __future__ import annotations


NONHUMAN_DRYAD_RECORD_IDS = frozenset(
    {
        "dryad_5xfad_retina_dlgn",
        "dryad_angle_closure_rabbit",
        "dryad_bbs1_retinal_degeneration",
        "dryad_biocular_eye_tracking",
        "dryad_canine_pra_cea_genotypes",
        "dryad_cone_synapse_computation",
        "dryad_d12d9f",
        "dryad_d1895r",
        "dryad_fungal_keratitis_azole_assay",
        "dryad_htr1b_mouse_retina",
        "dryad_ird_mouse_proteome",
        "dryad_j0707ztm",
        "dryad_macaque_cone_ratio",
        "dryad_mouse_all_optical_retina",
        "dryad_mouse_oct_beam_tilt",
        "dryad_mouse_pupil_masking_retinal_deg",
        "dryad_nhp_trachoma_immunity",
        "dryad_ocular_gvhd_mouse",
        "dryad_pk0p2ngzh",
        "dryad_primate_on_dsgc",
        "dryad_prpf31_gene_augmentation",
        "dryad_pzgmsbcmk",
        "dryad_q6rv0kz3",
        "dryad_q6w37t8b",
        "dryad_q83bk3jnw",
        "dryad_r4xgxd2nt",
        "dryad_r7sqv9sqs",
        "dryad_retinal_explant_metabolomics",
        "dryad_retinal_pufa_aging_mouse",
        "dryad_retinal_vasomotion",
        "dryad_retinal_vein_cannulation",
        "dryad_rhesus_maculopathy_metabolomics",
        "dryad_rn8pk0pmm",
        "dryad_rs2qp",
        "dryad_rv15dv4bv",
        "dryad_s1rn8pkhb",
        "dryad_spata7_canine_retinal_degeneration",
        "dryad_subretinal_fibrosis_adora2a",
        "dryad_subretinal_robot",
        "dryad_tb2rbp0cq",
        "dryad_tdz08kq8t",
        "dryad_vq83bk3s8",
        "dryad_vx0k6djwf",
        "dryad_w3r228143",
        "dryad_wdbrv15rj",
        "dryad_wstqjq2n5",
        "dryad_x95x69pmq",
        "dryad_xpnvx0kb6",
        "dryad_xwdbrv1kd",
        "dryad_z08kprrk3",
        "dryad_z08kprrk6",
        "dryad_z8w9ghx9f",
        "dryad_z8w9ghxpp",
        "dryad_zebrafish_crystallin_lens",
        "dryad_zebrafish_rpe_phagocytosis",
        "dryad_zebrafish_thrb_photoreceptors",
        "dryad_zkh1893nt",
        "dryad_zs7h44jd9",
    }
)


NOT_DISTINCT_MODEL_RESOURCE_IDS = frozenset(
    {
        "dryad_eye_head_visual_selection",
        "dryad_pg4f4qrwf",
        "dryad_rod_cone_dystrophy_genes",
    }
)


INSUFFICIENT_MODEL_EVIDENCE_IDS = frozenset(
    {
        "dryad_glaucoma_tears_mirna",
    }
)


RELATIONSHIP_ONLY_RESOURCE_IDS = frozenset(
    {
        "dryad_sf7m0cggh",
    }
)


DRYAD_SCOPE_EXCLUSIONS = {
    **{
        record_id: "nonhuman_or_nonhuman_derived"
        for record_id in NONHUMAN_DRYAD_RECORD_IDS
    },
    **{
        record_id: "not_distinct_sample_level_model_resource"
        for record_id in NOT_DISTINCT_MODEL_RESOURCE_IDS
    },
    **{
        record_id: "insufficient_observation_level_model_evidence"
        for record_id in INSUFFICIENT_MODEL_EVIDENCE_IDS
    },
    **{
        record_id: "relationship_only_not_independent_canonical_resource"
        for record_id in RELATIONSHIP_ONLY_RESOURCE_IDS
    },
}


# The complete Mendeley subset was reviewed again after the official current
# deposits were downloaded and their file structures were inspected. These
# records remain in their source modules and dated audit logs, but they are not
# part of the headline catalog because they do not meet the retained
# human/model-use boundary.
MENDELEY_NOT_USEFUL_RECORD_IDS = frozenset(
    {
        "chronic_corneal_disorders",
        "corneal_parameters_kc",
        "mendeley_anterior_segment_optical_coherence_tomography_angiography",
        "mendeley_clinical_application_cyanoacrylate_tissue_adhesive_pediatric",
        "mendeley_clinical_assessment_scleral_canal_expansion_glaucoma",
        "mendeley_comparison_cervical_ocular_vestibular_evoked_myogenic",
        "mendeley_comparison_two_novel_comfilcon_contact_lens",
        "mendeley_cost_effectiveness_limited_vitrectomy_vision_degrading",
        "mendeley_difference_retinal_nerve_fiber_layer_thickness",
        "mendeley_effect_prednisone_plus_either_adalimumab_or",
        "mendeley_effects_implantable_collamer_lens_icl_implantation",
        "mendeley_improved_retinal_displacement_quantification_between_retinal",
        "mendeley_keratoconus_ukraine_children",
        "mendeley_long_term_results_using_gelatin_microfistulae",
        "mendeley_microvascular_changes_poag_after_npds",
        "mendeley_performance_corneal_vs_scleral_rigid_gas",
        "mendeley_peripapillary_retinal_nerve_fiber_layer_thinning",
        "mendeley_radial_peripapillary_capillary_density_as_predictive",
        "mendeley_selective_laser_trabeculoplasty_patients_angle_recession",
        "mendeley_vivo_analysis_comparison_anterior_segment_structures",
    }
)


MENDELEY_AUTHOR_REMOVED_UNCERTAIN_RECORD_IDS = frozenset(
    {
        "mendeley_comparison_clinical_outcomes_visual_quality_visual",
        "mendeley_fundus_autofluorescence_premature_infants",
        "mendeley_human_mesenchymal_stem_cells_derived_adipose",
        "mendeley_imaging_retinal_choroidal_vasculature_using_spatio",
        "mendeley_spatio_temporal_optical_coherence_tomography_provides",
    }
)


MENDELEY_SCOPE_EXCLUSIONS = {
    **{
        record_id: "not_suitable_for_model_training_or_evaluation"
        for record_id in MENDELEY_NOT_USEFUL_RECORD_IDS
    },
    **{
        record_id: "excluded_after_author_review_due_to_uncertain_scope"
        for record_id in MENDELEY_AUTHOR_REMOVED_UNCERTAIN_RECORD_IDS
    },
}


# Earlier releases remain documented as ``previous_version`` links on the
# retained current record. They are not separate catalog records.
SUPERSEDED_VERSION_RECORD_IDS = frozenset(
    {
        "glaucoma_expert_cot_raw",
        "refuge2018",
    }
)


# BiDR and the Tianchi arranged record both repackage the same 35,126-image
# EyePACS training split without a distinct annotation or scientific object.
# Their routes remain documented on the canonical EyePACS record.
DUPLICATE_OR_SUBSET_MIRROR_RECORD_IDS = frozenset(
    {
        "bidr",
        "dr_arranged",
    }
)


CATALOG_SCOPE_EXCLUSIONS = {
    **DRYAD_SCOPE_EXCLUSIONS,
    **MENDELEY_SCOPE_EXCLUSIONS,
    **{
        record_id: "superseded_by_current_version"
        for record_id in SUPERSEDED_VERSION_RECORD_IDS
    },
    **{
        record_id: "unmodified_duplicate_or_subset_mirror"
        for record_id in DUPLICATE_OR_SUBSET_MIRROR_RECORD_IDS
    },
}


if len(NONHUMAN_DRYAD_RECORD_IDS) != 58:
    raise RuntimeError("Expected 58 reviewed nonhuman Dryad records")
if len(DRYAD_SCOPE_EXCLUSIONS) != 63:
    raise RuntimeError("Expected 63 reviewed Dryad scope exclusions")
if len(MENDELEY_NOT_USEFUL_RECORD_IDS) != 20:
    raise RuntimeError("Expected 20 reviewed Mendeley model-use exclusions")
if len(MENDELEY_AUTHOR_REMOVED_UNCERTAIN_RECORD_IDS) != 5:
    raise RuntimeError("Expected 5 author-removed uncertain Mendeley records")
if len(MENDELEY_SCOPE_EXCLUSIONS) != 25:
    raise RuntimeError("Expected 25 reviewed Mendeley scope exclusions")
if len(CATALOG_SCOPE_EXCLUSIONS) != 92:
    raise RuntimeError("Expected 92 total catalog exclusions")
