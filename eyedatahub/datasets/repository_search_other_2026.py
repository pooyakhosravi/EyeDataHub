"""Reconciled Figshare, Kaggle, and Hugging Face additions (August 2026).

This module intentionally contains only canonical resources approved by the
dated source-confirmation and reconciliation ledgers.  Repository mirrors,
unreleased records, and Tobii scene components remain metadata relationships,
not independent catalog records.
"""
from __future__ import annotations

from typing import Any

from eyedatahub.datasets.platform_2026 import PlatformDiscoveryDataset


REVIEW_DATE = "2026-08-02"

PRIMARY_CATEGORY_BY_MODALITY = {
    "as_oct": "corneal_topography",
    "biometry": "tabular",
    "genomics": "omics",
    "iris": "iris_biometrics",
    "ivcm": "confocal",
    "microscopy": "cell_microscopy",
    "pupillometry": "eye_tracking",
    "slit_lamp": "external_eye",
}


def _record(
    *,
    name: str,
    full_name: str,
    description: str,
    modality: str,
    tasks: list[str],
    platform: str,
    stable_id: str,
    doi: str | None = None,
    version: str | None = None,
    quantity: tuple[int, str, str] | None = None,
    terms: str = "CC BY 4.0",
    publication_doi: str | None = None,
    notes: str = "",
    relationships: list[dict[str, str]] | None = None,
    alternate_sources: list[dict[str, str]] | None = None,
    controlled: bool = False,
    official_url: str | None = None,
) -> dict[str, Any]:
    """Create a conservative PlatformDiscoveryDataset metadata record."""
    if official_url is None:
        if doi:
            official_url = f"https://doi.org/{doi}"
        elif platform == "huggingface":
            official_url = f"https://huggingface.co/datasets/{stable_id}"
        else:
            official_url = f"https://www.kaggle.com/datasets/{stable_id}"
    unit = quantity[1] if quantity else ""
    quantities = []
    if quantity:
        count, unit, scope = quantity
        quantities = [{
            "count": count,
            "unit": unit,
            "scope": scope,
            "evidence_url": official_url,
            "evidence_basis": "official_source_description",
            "primary": True,
            "exactness": "exact",
            "review_date": REVIEW_DATE,
            "notes": "Source-stated quantity; repository file count is separate.",
        }]
    source: dict[str, str] = {"accepted_id": stable_id}
    if platform == "figshare":
        source["id"] = stable_id
    elif platform == "huggingface":
        source["repo"] = stable_id
    elif platform == "kaggle":
        source["dataset"] = stable_id
    dtype = "manual" if controlled else platform
    primary_category = PRIMARY_CATEGORY_BY_MODALITY.get(modality, modality)
    modalities = [primary_category]
    if modality != primary_category:
        modalities.append(modality)
    return {
        "name": name,
        "full_name": full_name,
        "description": description,
        "modality": primary_category,
        "primary_category": primary_category,
        "modalities": modalities,
        "tasks": tasks,
        "num_samples": quantity[0] if quantity else None,
        "splits": ["all"],
        "download_type": dtype,
        "download_url": official_url,
        "license": terms,
        "source_terms": terms,
        "terms_scope": "dataset_files",
        "terms_evidence_url": official_url,
        "citation": f"Repository dataset record. {doi or stable_id}.",
        "tags": [platform, modality, *tasks],
        "notes": notes,
        "item_count_unit": unit,
        "reported_quantities": quantities,
        "source_landing_page_url": official_url,
        "preferred_route_type": "official_repository",
        "preferred_route_url": official_url,
        "access_friction": (
            "controlled_or_manual" if controlled else "self_service_authenticated"
        ),
        "requires_registration": None if controlled else True,
        "requires_authentication": None if controlled else True,
        "requires_api_token": None if controlled else True,
        "requires_clickthrough": None,
        "requires_manual_approval": True if controlled else False,
        "requires_data_use_agreement": True if controlled else False,
        "requires_author_contact": True if controlled else False,
        "requires_payment": False,
        "availability_status": "available",
        "route_last_checked": REVIEW_DATE,
        "route_check_result": "official_metadata_and_file_listing_checked",
        "route_check_notes": "No data files were transferred during source confirmation.",
        "acquisition_support": "manual_access_blocked" if controlled else "standard_platform_supported",
        "repository_record_id": stable_id,
        "dataset_doi": doi,
        "associated_publication_doi": publication_doi,
        "resource_version": version,
        "canonical_resolver_url": official_url,
        "relationships": relationships or [],
        "alternate_sources": alternate_sources or [],
        "item_count_evidence_url": official_url if quantity else None,
        "modality_evidence_url": official_url,
        "task_evidence_url": official_url,
        "citation_evidence_url": official_url,
        "author_source_checked": True,
        "source_check_date": REVIEW_DATE,
        "source_check_status": "checked_against_official_repository",
        "access_check_status": "official_route_documented",
        "transfer_check_status": "not_run",
        "source": source,
    }


# The 45 ``new_canonical_record`` rows plus the ITEC canonical resource whose
# Kaggle candidate is an ``alternate_source_to_new`` route.
OTHER_REPOSITORY_RECORDS: list[dict[str, Any]] = [
    _record(name="sustech_sysu_corneal_ulcers", full_name="SUSTech-SYSU Corneal Ulcer Dataset", description="Human corneal-ulcer clinical images and labels.", modality="external_eye", tasks=["classification"], platform="figshare", stable_id="10247501", doi="10.6084/m9.figshare.10247501.v1", version="1"),
    _record(name="visual_field_test_perception", full_name="Visual Field Test Perception Dataset", description="Human visual-field perception observations.", modality="visual_field", tasks=["measurement"], platform="figshare", stable_id="12443594", doi="10.6084/m9.figshare.12443594.v2", version="2"),
    _record(name="cyp1b1_poag_genotypes", full_name="CYP1B1 Primary Open-Angle Glaucoma Genotype Dataset", description="Human POAG genotype observations.", modality="genomics", tasks=["classification"], platform="figshare", stable_id="16545561", doi="10.25451/flinders.16545561.v1", version="1"),
    _record(name="dual_scheimpflug_ss_oct_biometry", full_name="Dual Scheimpflug and Swept-Source OCT Biometry Dataset", description="Human ocular-biometry measurements from dual Scheimpflug and swept-source OCT instruments.", modality="biometry", tasks=["measurement"], platform="figshare", stable_id="16828996", doi="10.6084/m9.figshare.16828996.v1", version="1"),
    _record(name="retinal_optic_flow_locomotion", full_name="Retinal Optic Flow and Locomotion Dataset", description="Human retinal optic-flow and locomotion observations.", modality="eye_tracking", tasks=["measurement"], platform="figshare", stable_id="17113883", doi="10.25452/figshare.plus.17113883.v1", version="1"),
    _record(name="pimd_visual_preference_eye_tracking", full_name="PIMD Visual Preference Eye-Tracking Dataset", description="Human eye-tracking observations from a visual-preference study.", modality="eye_tracking", tasks=["measurement"], platform="figshare", stable_id="19598133", doi="10.1371/journal.pone.0266176.s010", version="1"),
    _record(name="asd_eye_tracking", full_name="Autism Spectrum Disorder Eye-Tracking Dataset", description="Human eye-tracking observations from an ASD study.", modality="eye_tracking", tasks=["measurement"], platform="figshare", stable_id="20113592", doi="10.6084/m9.figshare.20113592.v1", version="1"),
    _record(name="retinal_photoplethysmography_rnfl", full_name="Retinal Photoplethysmography and RNFL Dataset", description="Human retinal photoplethysmography and retinal-nerve-fiber-layer measurements.", modality="oct", tasks=["measurement"], platform="figshare", stable_id="21197173", doi="10.6084/m9.figshare.21197173.v1", version="1"),
    _record(name="hesc_rpe_electrical_excitability", full_name="hESC-Derived RPE Electrical Excitability Dataset", description="Human embryonic-stem-cell-derived RPE electrophysiology data.", modality="electrophysiology", tasks=["measurement"], platform="figshare", stable_id="22246969", doi="10.6084/m9.figshare.22246969.v2", version="2", publication_doi="10.1186/s12915-023-01559-5"),
    _record(name="pupillometry_eeg_fmri_salience", full_name="Pupillometry, EEG, and fMRI Salience Dataset", description="Human synchronized pupillometry, EEG, and fMRI salience measurements.", modality="pupillometry", tasks=["measurement"], platform="figshare", stable_id="22518010", doi="10.6084/m9.figshare.22518010.v1", version="1"),
    _record(name="cataract_iol_biometry_outcomes", full_name="Cataract IOL Biometry and Outcomes Dataset", description="Human cataract-surgery biometry and clinical outcome measurements.", modality="biometry", tasks=["measurement"], platform="figshare", stable_id="22736687", doi="10.6084/m9.figshare.22736687.v1", version="1"),
    _record(name="parkinsons_outer_retinal_structure", full_name="Parkinson Disease Outer Retinal Structure and Function Dataset", description="Retinal structure, electrophysiology, and visual-perception measurements from Parkinson disease and comparison participants.", modality="oct", tasks=["measurement", "classification"], platform="figshare", stable_id="24138420", doi="10.26188/24138420.v2", version="2"),
    _record(name="slid_e", full_name="SLID-E Slit-Lamp Image Dataset for Epiphora", description="Slit-lamp photographs with expert epiphora-severity labels.", modality="slit_lamp", tasks=["classification"], platform="figshare", stable_id="26172919", doi="10.6084/m9.figshare.26172919.v2", version="2", quantity=(2999,"images","Source reports 2,999 slit-lamp photographs from 1,563 patients."), notes="Distinct from the cataloged SLID resource."),
    _record(name="casia2_keratometric_astigmatism", full_name="CASIA2 Keratometric Astigmatism Dataset", description="Human anterior-segment OCT keratometric-astigmatism measurements.", modality="as_oct", tasks=["measurement"], platform="figshare", stable_id="26395018", doi="10.6084/m9.figshare.26395018.v1", version="1"),
    _record(name="china_fundus_cimt", full_name="China Fundus and Carotid Intima-Media Thickness Dataset", description="Human fundus and carotid intima-media-thickness measurements.", modality="fundus", tasks=["measurement"], platform="figshare", stable_id="27907056", doi="10.6084/m9.figshare.27907056.v1", version="1"),
    _record(name="spectrosense_pupil_light_exposure", full_name="SpectroSense Pupil Light Exposure Dataset", description="Human pupil and light-exposure measurements.", modality="pupillometry", tasks=["measurement"], platform="figshare", stable_id="28176839", doi="10.6084/m9.figshare.28176839.v1", version="1"),
    _record(name="corneal_nerve_parkinsons", full_name="Corneal Nerve Parkinson Disease Dataset", description="Human corneal-nerve measurements in Parkinson disease study participants.", modality="ivcm", tasks=["measurement"], platform="figshare", stable_id="28189571", doi="10.6084/m9.figshare.28189571.v1", version="1"),
    _record(name="casia2_as_oct_repeatability", full_name="CASIA2 Anterior-Segment OCT Repeatability Dataset", description="Human CASIA2 anterior-segment OCT repeatability measurements.", modality="as_oct", tasks=["measurement"], platform="figshare", stable_id="29302664", doi="10.6084/m9.figshare.29302664.v1", version="1"),
    _record(name="hesc_retinal_organoid_early_differentiation", full_name="hESC-Derived Retinal Organoid Early Differentiation Imaging Dataset", description="Time-series bright-field imaging of human embryonic-stem-cell-derived retinal organoid aggregates.", modality="microscopy", tasks=["classification", "measurement"], platform="figshare", stable_id="30102802", doi="10.6084/m9.figshare.30102802.v1", version="1", notes="Source reports 384 aggregates imaged across days 6–30; no catalog quantity is asserted because the source unit is outside the controlled vocabulary."),
    _record(name="rop_vl", full_name="ROP-VL Retinopathy of Prematurity Vision-Language Dataset", description="Color fundus photographs paired with biological metadata and structured descriptions for retinopathy of prematurity.", modality="fundus", tasks=["classification", "image_text"], platform="figshare", stable_id="30143461", doi="10.6084/m9.figshare.30143461.v1", version="1", quantity=(2020,"images","Source reports 2,020 color fundus photographs from 1,116 infants."), notes="Current official metadata has no references or source-image relationship. FARFUM-ROP and ROP Ostrava are cataloged ROP resources, but no internal edge is asserted."),
    _record(name="post_glaucoma_surgery_ptosis_strabismus", full_name="Post-Glaucoma-Surgery Ptosis and Strabismus Dataset", description="De-identified human glaucoma-surgery clinical records with postoperative ptosis and strabismus outcomes.", modality="tabular", tasks=["classification", "measurement"], platform="figshare", stable_id="30491856", doi="10.1371/journal.pone.0335074.s001", version="1", publication_doi="10.1371/journal.pone.0335074", quantity=(705,"records","Source reports 705 glaucoma-surgery clinical records.")),
    _record(name="natural_scene_eye_tracking_collection", full_name="Natural-Scene Tobii Eye-Tracking Collection", description="Tobii Pro Glasses 3 natural-scene viewing recordings with gaze, IMU, event, video, and snapshot files.", modality="eye_tracking", tasks=["gaze_estimation", "measurement"], platform="figshare", stable_id="30520733", doi="10.6084/m9.figshare.30520733.v1", version="1", notes="Collection-level anchor. Official components include 30520775, 30520829, 30520892, 30520925, and 30520979. The public file listings for 30520775 and 30520892 are byte-identical Indoor Scene 3 deposits.", alternate_sources=[{"platform":"figshare","role":"component_deposit","url":"https://figshare.com/articles/dataset/30520775","identifier":"30520775","version":"1","notes":"Indoor Scene 3 component; official file listing is byte-identical to 30520892."},{"platform":"figshare","role":"component_deposit","url":"https://figshare.com/articles/dataset/30520829","identifier":"30520829","version":"1","notes":"Outdoor Scene 1 component."},{"platform":"figshare","role":"component_deposit","url":"https://figshare.com/articles/dataset/30520892","identifier":"30520892","version":"1","notes":"Indoor Scene 3 component; duplicate payload of 30520775."},{"platform":"figshare","role":"component_deposit","url":"https://figshare.com/articles/dataset/30520925","identifier":"30520925","version":"1","notes":"Outdoor Scene 2 component."},{"platform":"figshare","role":"component_deposit","url":"https://figshare.com/articles/dataset/30520979","identifier":"30520979","version":"1","notes":"Outdoor Scene 3 component."}]),
    _record(name="parkinsons_directional_oct", full_name="Parkinson Disease Directional OCT Dataset", description="Processed outer-retinal thickness and reflectance measurements from a Parkinson disease directional-OCT study.", modality="oct", tasks=["measurement"], platform="figshare", stable_id="30750011", doi="10.26188/30750011.v1", version="1", notes="Distinct deposit. Possible study or cohort overlap with Figshare 24138420 remains unresolved, so no catalog relationship is asserted."),
    _record(name="mpxv_ocular_manifestations_south_kivu", full_name="MPXV Ocular Manifestations South Kivu Dataset", description="Human clinical ocular-manifestation data from four South-Kivu health zones.", modality="tabular", tasks=["classification", "measurement"], platform="figshare", stable_id="31364760", doi="10.1371/journal.pgph.0005971.s001", version="1", publication_doi="10.1371/journal.pgph.0005971"),
    _record(name="tunisian_retinal_oct_multidisease", full_name="Tunisian Retinal OCT Multi-Disease Dataset", description="Clinically acquired retinal OCT images for AMD, DME, rhegmatogenous retinal detachment, and normal classification.", modality="oct", tasks=["classification"], platform="figshare", stable_id="31385596", doi="10.6084/m9.figshare.31385596.v3", version="3", controlled=True, notes="Official record has no public files; access is by approved signed data-use agreement."),
    _record(name="ocular_generalized_myasthenia_korea", full_name="Ocular and Generalized Myasthenia Gravis Korea Dataset", description="Anonymized South Korean cohort clinical, serologic, electrophysiologic, thymic, and treatment data.", modality="tabular", tasks=["classification", "measurement"], platform="figshare", stable_id="31981347", doi="10.6084/m9.figshare.31981347.v1", version="1"),
    _record(name="binocular_fundus_images", full_name="Binocular Fundus Image Dataset", description="Paired left- and right-eye fundus images.", modality="fundus", tasks=["classification"], platform="figshare", stable_id="31981557", doi="10.6084/m9.figshare.31981557.v1", version="1", quantity=(2885,"image_pairs","Source reports 2,885 paired binocular fundus samples."), notes="Labels and detailed cohort provenance are limited to the source description."),
    _record(name="glaucoma_oct_fundus", full_name="Glaucoma Detection Dataset with OCT and Fundus Images", description="De-identified per-patient glaucoma fundus/OCT images with processed labels and annotated spreadsheet.", modality="fundus", tasks=["classification"], platform="figshare", stable_id="32051124", doi="10.6084/m9.figshare.32051124.v1", version="1"),
    _record(name="anterior_uveitis_corneal_endothelium", full_name="Anterior Uveitis Corneal Endothelium Dataset", description="De-identified anterior-uveitis corneal-endothelial parameters and related variables.", modality="tabular", tasks=["measurement"], platform="figshare", stable_id="32054064", doi="10.6084/m9.figshare.32054064.v1", version="1"),
    _record(name="fd3611", full_name="FD3611 Multi-Class Color Fundus Image Dataset", description="Clinically validated color fundus photographs from routine ophthalmic examinations with expert disease annotations.", modality="fundus", tasks=["classification"], platform="figshare", stable_id="32086296", doi="10.6084/m9.figshare.32086296.v1", version="1", quantity=(3611,"images","Source reports 3,611 color fundus photographs.")),
    _record(name="aqp4_optic_neuritis_oct_layers", full_name="AQP4 Optic Neuritis OCT Layers Dataset", description="Peripapillary RNFL and segmented-macular OCT measurements in optic-neuritis cohorts and healthy controls.", modality="oct", tasks=["measurement", "classification"], platform="figshare", stable_id="3209908", doi="10.6084/m9.figshare.3209908.v1", version="1"),
    _record(name="puwf_av", full_name="PUWF-AV Pediatric Ultra-Widefield Fundus Artery-Vein Dataset", description="Pediatric ultra-widefield fundus images with professional artery-vein segmentation annotations.", modality="fundus", tasks=["segmentation"], platform="figshare", stable_id="32509329", doi="10.6084/m9.figshare.32509329.v1", version="1", quantity=(60,"images","Source reports 60 ultra-widefield fundus images.")),
    _record(name="slp_vld", full_name="SLP-VLD Anonymized Slit-Lamp Vision-Language Dataset", description="Anonymized slit-lamp photographs with English clinical annotations and vision-language conversations.", modality="slit_lamp", tasks=["classification", "image_text"], platform="figshare", stable_id="32576697", doi="10.6084/m9.figshare.32576697.v3", version="3", quantity=(2228,"images","Source reports 2,228 slit-lamp photographs."), alternate_sources=[{"platform":"figshare","role":"previous_version","url":"https://figshare.com/articles/dataset/32592837","identifier":"32592837","version":"","notes":"Alternate deposit."},{"platform":"figshare","role":"previous_version","url":"https://figshare.com/articles/dataset/32593101","identifier":"32593101","version":"","notes":"Alternate deposit."},{"platform":"figshare","role":"previous_version","url":"https://figshare.com/articles/dataset/32593173","identifier":"32593173","version":"","notes":"Alternate deposit."}]),
    _record(name="cataract_lenstar_biometric_symmetry", full_name="Cataract LenStar Biometric Symmetry Dataset", description="Bilateral LenStar biometrics from a human cataract population.", modality="biometry", tasks=["measurement"], platform="figshare", stable_id="32833895", doi="10.6084/m9.figshare.32833895.v1", version="1"),
    _record(name="pco_namd", full_name="PCO-nAMD Paired CFP and OCT Dataset", description="Paired color-fundus/OCT images with expert MNV subtype labels and treatment-response follow-up.", modality="fundus", tasks=["classification", "prediction"], platform="figshare", stable_id="32873501", doi="10.6084/m9.figshare.32873501.v1", version="1", quantity=(654,"image_pairs","Source reports 654 paired CFP/OCT images from 327 patients.")),
    _record(name="central_retinal_vessel_trunk_oag", full_name="Central Retinal Vessel Trunk Open-Angle Glaucoma Dataset", description="Central retinal vessel-trunk and OCT-related measurements in open-angle glaucoma eyes.", modality="tabular", tasks=["measurement"], platform="figshare", stable_id="3917574", doi="10.1371/journal.pone.0158443.s001", version="1", publication_doi="10.1371/journal.pone.0158443", quantity=(205,"eyes","Source reports 205 open-angle-glaucoma eyes.")),
    _record(name="doomgan_ocular_morphs", full_name="DOOMGAN Ocular Morph-Attack Dataset", description="Synthetic visible-spectrum ocular biometric morph images generated from documented human VISOB source imagery.", modality="iris", tasks=["classification"], platform="huggingface", stable_id="BharathK333/DOOMGAN-Ocular-Morphs", terms="MIT", quantity=(10000,"images","Source reports 10,000 morphed PNG images."), notes="Synthetic derivative of VISOB; upstream VISOB is not a current catalog record."),
    _record(name="synthetic_retinal_oct_biomarkers", full_name="Synthetic Retinal OCT Biomarker Dataset", description="Synthetic OCT images for the four Kermany diagnostic classes.", modality="oct", tasks=["classification"], platform="huggingface", stable_id="serag-ai/Synthetic-Ophthalmology-Images", terms="Unknown; no dataset license stated", publication_doi="10.3389/frai.2024.1454441", relationships=[{"type":"derived_from","target":"kermany_oct"}], notes="Synthetic derivative of the cataloged Kermany OCT dataset; source reports four class archives but no image count."),
    _record(name="glaucoma_expert_cot_raw", full_name="Glaucoma Expert Chain-of-Thought Raw Dataset", description="Fundus cases paired with six-step glaucoma reasoning reports.", modality="fundus", tasks=["classification", "image_text"], platform="huggingface", stable_id="yuzhench/glaucoma-expert-cot-raw-1077", terms="Other; source-image terms apply", quantity=(1074,"image_report_pairs","Source reports 1,074 fundus cases with JSONL reasoning records."), relationships=[{"type":"derived_from","target":"lag"},{"type":"derived_from","target":"papila"}]),
    _record(name="glaucoma_expert_cot_refined", full_name="Glaucoma Expert Chain-of-Thought Refined Dataset", description="Revised glaucoma reasoning reports paired with the documented source fundus cases.", modality="fundus", tasks=["classification", "image_text"], platform="huggingface", stable_id="yuzhench/glaucoma-expert-cot-refined-1077", terms="Other; source-image terms apply", quantity=(1074,"image_report_pairs","Source reports 1,074 fundus cases with refined JSONL reasoning records."), relationships=[{"type":"derived_from","target":"lag"},{"type":"derived_from","target":"papila"}], notes="Current refined release. The earlier raw reasoning release is retained as version history and is not counted separately.", alternate_sources=[{"platform":"huggingface","role":"previous_version","url":"https://huggingface.co/datasets/yuzhench/glaucoma-expert-cot-raw-1077","identifier":"yuzhench/glaucoma-expert-cot-raw-1077","version":"raw","notes":"Earlier reasoning release superseded by the refined record."}]),
    _record(name="itec_iris_pupil", full_name="ITEC Iris and Pupil Segmentation Dataset", description="Human cataract-surgery video frames with iris and pupil pixel masks.", modality="surgical_video", tasks=["segmentation"], platform="kaggle", stable_id="arwabasal/itec-iris-and-pupil-segmentation", terms="Scientific-research-only; noncommercial use", publication_doi="10.1109/ISBIWorkshops50223.2020.9153367", quantity=(82,"frames","Official ITEC source reports 82 annotated frames from 35 cataract-surgery videos."), relationships=[{"type":"derived_from","target":"cataract_101"}], controlled=True, official_url="https://ftp.itec.aau.at/datasets/ovid/iris_pupil_seg/index.html", notes="The official ITEC agreement route is canonical. Kaggle is an alternate mirror, not the controlling source.", alternate_sources=[{"platform":"kaggle","role":"mirror","url":"https://www.kaggle.com/datasets/arwabasal/itec-iris-and-pupil-segmentation","identifier":"arwabasal/itec-iris-and-pupil-segmentation","version":"","notes":"Non-authoritative alternate route."}]),
    _record(name="brasil_glaucoma_brg", full_name="Brazil Glaucoma (BrG) Dataset", description="Portable/smartphone fundus photographs of Brazilian glaucoma and non-glaucoma volunteers.", modality="fundus", tasks=["classification"], platform="kaggle", stable_id="clerimar/brasil-glaucoma-brg", terms="CC BY-NC 4.0", publication_doi="10.3390/healthcare10122345", quantity=(2000,"images","Source article reports 2,000 fundus images from 1,000 volunteers."), notes="Kaggle description gives a conflicting image count; the source article quantity is retained."),
    _record(name="retinal_oct_octa_two_subjects_processed", full_name="Processed Retinal OCT and OCTA Two-Subject Dataset", description="Processed human OCT/OCTA data including segmentations and ETDRS-grid materials.", modality="octa", tasks=["segmentation", "measurement"], platform="kaggle", stable_id="cnzakimuena/retinal-oct-and-octa-data-3", notes="Source describes processed 3 × 3 mm OCTA/OCT data for two subjects; no catalog quantity is asserted because the source unit is not controlled."),
    _record(name="higancnn_generated_glaucoma", full_name="HiGANCNN Generated Glaucoma Dataset", description="Synthetic glaucoma/normal fundus images with documented human source collections.", modality="fundus", tasks=["classification"], platform="kaggle", stable_id="hindsaud/datasets-higancnn-glaucoma-detection", terms="Unknown", quantity=(30000,"images","Source reports 30,000 generated eye images."), relationships=[{"type":"derived_from","target":"acrima"},{"type":"derived_from","target":"drishti_gs"},{"type":"derived_from","target":"hrf"}], notes="Source also names ORIGA-LIGHT and generic RIM-ONE. The catalog has RIM-ONE DL, but public evidence does not establish that exact release; no edge is asserted for either external source."),
    _record(name="hybridgaze", full_name="HybridGaze Dataset", description="Synchronized human eye-tracking, webcam eye images, facial landmarks, and gaze annotations.", modality="eye_tracking", tasks=["gaze_estimation"], platform="kaggle", stable_id="michachwesiuk/hybridgaze", terms="GNU Free Documentation License 1.3", publication_doi="10.24425/ijet.2026.157892", notes="Source exposes one HDF5 gaze-estimation dataset; no participant/frame count is stated."),
    _record(name="gleam", full_name="GLEAM Multimodal Glaucoma Staging Dataset", description="SLO, circumpapillary OCT, and visual-field pattern-deviation maps with four-class glaucoma labels.", modality="oct", tasks=["classification", "staging"], platform="kaggle", stable_id="zhangyiyinge/gleam-dataset", terms="CC BY-NC-ND 4.0", notes="Source reports 1,200 tri-modal samples from 841 patients. Complete-deposit inspection confirmed three unique images per sample; copies under split directories are not counted again."),
]


ACCEPTED_SOURCE_IDS = tuple(record["source"]["accepted_id"] for record in OTHER_REPOSITORY_RECORDS)
OTHER_REPOSITORY_DATASETS = [PlatformDiscoveryDataset(record) for record in OTHER_REPOSITORY_RECORDS]
