"""Dataset registry — single source of truth for all EyeDataHub datasets."""

from __future__ import annotations

from typing import Dict, List, Optional
from urllib.parse import urlparse

from eyedatahub.core.dataset import EyeDataHubDataset
from eyedatahub.core.metadata import (
    ACCESS_FRICTION_VALUES,
    ACQUISITION_SUPPORT_VALUES,
    AVAILABILITY_STATUS_VALUES,
    TERMS_SCOPE_VALUES,
    normalize_modality_label,
)
from eyedatahub.core.quantities import (
    EVIDENCE_BASES,
    EXACTNESS_VALUES,
    PUBLIC_QUANTITY_FIELDS,
    QUANTITY_UNITS,
)
from eyedatahub.datasets.scope_exclusions import CATALOG_SCOPE_EXCLUSIONS


ALTERNATE_SOURCE_ROLES = {
    "alternate_deposit",
    "component_deposit",
    "derived_annotation",
    "metadata_record",
    "mirror",
    "previous_version",
    "repository_copy",
}
ALTERNATE_SOURCE_FIELDS = {
    "platform",
    "role",
    "url",
    "identifier",
    "version",
    "notes",
}


class DatasetRegistry:
    """
    Singleton registry for all EyeDataHub datasets.

    Datasets are registered once on import and can be looked up by name
    or filtered by modality / task / tag.
    """

    _instance: Optional["DatasetRegistry"] = None

    def __init__(self) -> None:
        self._datasets: Dict[str, EyeDataHubDataset] = {}

    @classmethod
    def get(cls) -> "DatasetRegistry":
        """Return the global registry singleton."""
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    # ------------------------------------------------------------------
    # Registration
    # ------------------------------------------------------------------

    def register(self, dataset: EyeDataHubDataset) -> None:
        """Register a dataset instance under its info.name (lowercased)."""
        key = dataset.info.name.lower()
        if key in self._datasets:
            existing = self._datasets[key]
            raise ValueError(
                f"Duplicate dataset slug '{key}': "
                f"{existing.__class__.__name__} and {dataset.__class__.__name__}"
            )
        self._datasets[key] = dataset

    def validation_errors(self) -> List[str]:
        """Return deterministic schema and consistency errors for the registry."""
        from eyedatahub.core.publication_dates import publication_date_errors

        errors: List[str] = []
        for key, dataset in self._datasets.items():
            info = dataset.info
            prefix = f"{key}:"
            errors.extend(f"{prefix} {error}" for error in publication_date_errors(info))
            if key != info.name.lower():
                errors.append(f"{prefix} registry key does not match info.name")
            if info.name != info.name.lower():
                errors.append(f"{prefix} slug must be lowercase")
            for field_name in (
                "name",
                "full_name",
                "description",
                "modality",
                "download_type",
                "license",
            ):
                if not getattr(info, field_name):
                    errors.append(f"{prefix} {field_name} is required")
            if not info.tasks or any(not task for task in info.tasks):
                errors.append(f"{prefix} at least one non-empty task is required")
            if info.num_samples is not None and (
                not isinstance(info.num_samples, int) or info.num_samples <= 0
            ):
                errors.append(
                    f"{prefix} num_samples must be a positive integer or None"
                )
            quantities = info.reported_quantities
            if not isinstance(quantities, list):
                errors.append(f"{prefix} reported_quantities must be a list")
                quantities = []
            primary_quantities = []
            for quantity_index, quantity in enumerate(quantities, start=1):
                quantity_prefix = f"{prefix} reported_quantities[{quantity_index}]"
                if not isinstance(quantity, dict):
                    errors.append(f"{quantity_prefix} must be an object")
                    continue
                if set(quantity) != set(PUBLIC_QUANTITY_FIELDS):
                    errors.append(
                        f"{quantity_prefix} does not match the quantity schema"
                    )
                    continue
                count = quantity["count"]
                if not isinstance(count, int) or isinstance(count, bool) or count < 0:
                    errors.append(
                        f"{quantity_prefix}.count must be a non-negative integer"
                    )
                if quantity["unit"] not in QUANTITY_UNITS:
                    errors.append(
                        f"{quantity_prefix}.unit is not in the controlled vocabulary"
                    )
                if quantity["evidence_basis"] not in EVIDENCE_BASES:
                    errors.append(f"{quantity_prefix}.evidence_basis is invalid")
                if quantity["exactness"] not in EXACTNESS_VALUES:
                    errors.append(f"{quantity_prefix}.exactness is invalid")
                if not isinstance(quantity["primary"], bool):
                    errors.append(f"{quantity_prefix}.primary must be boolean")
                if any(
                    not isinstance(quantity[field], str)
                    for field in ("scope", "evidence_url", "review_date", "notes")
                ):
                    errors.append(f"{quantity_prefix} text fields must be strings")
                elif quantity["evidence_url"] and urlparse(
                    quantity["evidence_url"]
                ).scheme not in {
                    "http",
                    "https",
                }:
                    errors.append(
                        f"{quantity_prefix}.evidence_url must use HTTP or HTTPS"
                    )
                if quantity["primary"] is True:
                    primary_quantities.append(quantity)
            if len(primary_quantities) > 1:
                errors.append(
                    f"{prefix} reported_quantities must contain at most one primary"
                )
            elif primary_quantities:
                primary = primary_quantities[0]
                if primary["count"] != info.num_samples:
                    errors.append(
                        f"{prefix} primary quantity count must match num_samples"
                    )
                if primary["unit"] != info.item_count_unit:
                    errors.append(
                        f"{prefix} primary quantity unit must match item_count_unit"
                    )
            elif info.num_samples is not None:
                errors.append(
                    f"{prefix} num_samples requires a primary reported quantity"
                )
            if info.size_gb is not None and info.size_gb <= 0:
                errors.append(f"{prefix} size_gb must be positive or None")
            if info.download_url and urlparse(info.download_url).scheme not in {
                "http",
                "https",
            }:
                errors.append(f"{prefix} download_url must use HTTP or HTTPS")
            if (
                info.classes is not None
                and info.num_classes is not None
                and len(info.classes) != info.num_classes
            ):
                errors.append(f"{prefix} classes and num_classes disagree")
            if info.primary_category != info.modality:
                errors.append(f"{prefix} primary_category must match legacy modality")
            if not info.modalities:
                errors.append(f"{prefix} modalities must name at least one data type")
            if (
                info.primary_category != "multimodal"
                and info.primary_category not in info.modalities
            ):
                errors.append(f"{prefix} modalities must include primary_category")
            if len(info.modalities) != len(set(info.modalities)):
                errors.append(f"{prefix} modalities must not contain duplicates")
            if info.primary_category == "multimodal":
                if "multimodal" in info.modalities:
                    errors.append(
                        f"{prefix} multimodal is a navigation category, not a data modality"
                    )
                if not info.modalities:
                    errors.append(
                        f"{prefix} multimodal records must name their component modalities"
                    )
            if info.access_friction not in ACCESS_FRICTION_VALUES:
                errors.append(
                    f"{prefix} invalid access_friction '{info.access_friction}'"
                )
            if info.acquisition_support not in ACQUISITION_SUPPORT_VALUES:
                errors.append(
                    f"{prefix} invalid acquisition_support '{info.acquisition_support}'"
                )
            if info.availability_status not in AVAILABILITY_STATUS_VALUES:
                errors.append(
                    f"{prefix} invalid availability_status '{info.availability_status}'"
                )
            if info.terms_scope not in TERMS_SCOPE_VALUES:
                errors.append(f"{prefix} invalid terms_scope '{info.terms_scope}'")
            for tri_state in (
                "requires_registration",
                "requires_authentication",
                "requires_api_token",
                "requires_clickthrough",
                "requires_manual_approval",
                "requires_data_use_agreement",
                "requires_author_contact",
                "requires_payment",
                "loader_live_tested",
                "author_source_checked",
            ):
                if getattr(info, tri_state) not in {True, False, None}:
                    errors.append(
                        f"{prefix} {tri_state} must be true, false, or unknown"
                    )
            for url_field in (
                "source_landing_page_url",
                "preferred_route_url",
                "terms_evidence_url",
                "canonical_resolver_url",
            ):
                value = getattr(info, url_field)
                if value and urlparse(value).scheme not in {"http", "https"}:
                    errors.append(f"{prefix} {url_field} must use HTTP or HTTPS")
            alternate_urls: set[str] = set()
            for source_index, source in enumerate(info.alternate_sources, start=1):
                source_prefix = f"{prefix} alternate_sources[{source_index}]"
                if not isinstance(source, dict):
                    errors.append(f"{source_prefix} must be an object")
                    continue
                if set(source) != ALTERNATE_SOURCE_FIELDS:
                    errors.append(
                        f"{source_prefix} does not match the alternate-source schema"
                    )
                    continue
                if any(not isinstance(value, str) for value in source.values()):
                    errors.append(f"{source_prefix} values must be strings")
                    continue
                if not source["platform"]:
                    errors.append(f"{source_prefix}.platform is required")
                if source["role"] not in ALTERNATE_SOURCE_ROLES:
                    errors.append(f"{source_prefix}.role is invalid")
                if urlparse(source["url"]).scheme not in {"http", "https"}:
                    errors.append(f"{source_prefix}.url must use HTTP or HTTPS")
                normalized_url = source["url"].lower().rstrip("/")
                if normalized_url in alternate_urls:
                    errors.append(f"{prefix} alternate source URLs must be unique")
                alternate_urls.add(normalized_url)
        return errors

    def validate(self) -> None:
        """Raise ``ValueError`` when registry metadata fail validation."""
        errors = self.validation_errors()
        if errors:
            raise ValueError("Registry validation failed:\n- " + "\n- ".join(errors))

    # ------------------------------------------------------------------
    # Lookup
    # ------------------------------------------------------------------

    def get_dataset(self, name: str) -> EyeDataHubDataset:
        """
        Return a dataset by name (case-insensitive).

        Raises KeyError if not found.
        """
        key = name.lower()
        if key not in self._datasets:
            available = ", ".join(sorted(self._datasets.keys()))
            raise KeyError(
                f"Dataset '{name}' not found in registry.\n"
                f"Available datasets: {available}"
            )
        return self._datasets[key]

    def list_datasets(
        self,
        modality: Optional[str] = None,
        task: Optional[str] = None,
        tag: Optional[str] = None,
    ) -> List[EyeDataHubDataset]:
        """
        Return a filtered list of datasets.

        Args:
            modality: Filter by modality (e.g. 'fundus', 'oct')
            task: Filter by task type (e.g. 'classification', 'segmentation')
            tag: Filter by tag

        Returns:
            List of EyeDataHubDataset instances
        """
        results = list(self._datasets.values())

        if modality:
            canonical = normalize_modality_label(modality)
            results = [d for d in results if canonical in d.info.modalities]

        if task:
            results = [d for d in results if task.lower() in d.info.tasks]

        if tag:
            results = [d for d in results if tag.lower() in d.info.tags]

        return results

    def names(self) -> List[str]:
        """Return sorted list of all registered dataset names."""
        return sorted(self._datasets.keys())

    def __len__(self) -> int:
        return len(self._datasets)

    def __contains__(self, name: str) -> bool:
        return name.lower() in self._datasets


# ---------------------------------------------------------------------------
# Global registry singleton
# ---------------------------------------------------------------------------

REGISTRY = DatasetRegistry.get()


def _register_all() -> None:
    """Register all built-in datasets. Called once on module import."""
    from eyedatahub.datasets.fundus_vessels import (
        CHASE_DB1Dataset,
        FIVESDataset,
        HRFDataset,
        RAVIRDataset,
        STAREDataset,
    )
    from eyedatahub.datasets.fundus_dr import (
        APTOS2019Dataset,
        DDRDataset,
        IDRiDDataset,
        MESSIDOR2Dataset,
        MAPLESDRDataset,
        EyePACSDataset,
        BiDRDataset,
        DRArrangedDataset,
        MMRDRDataset,
    )
    from eyedatahub.datasets.fundus_glaucoma import (
        REFUGE2018Dataset,
        RIMONEDLDataset,
        DRISHTIGSDataset,
        G1020Dataset,
        AIROGSDataset,
        PAPILADataset,
        HarvardGlaucomaFundusDataset,
        ACRIMADataset,
        BEHDataset,
        HarvardGDPDataset,
    )
    from eyedatahub.datasets.fundus_amd import (
        iChallengeAMDDataset,
    )
    from eyedatahub.datasets.fundus_multi import (
        RFMiDDataset,
        ODIR2019Dataset,
        JSIECDataset,
        CataractDataset,
        NEHUTDataset,
    )
    from eyedatahub.datasets.fundus_misc import (
        AODDataset,
        ToxoFundusDataset,
        FARFUMROPDataset,
    )
    from eyedatahub.datasets.oct_datasets import (
        AROIDataset,
        DRAC22Dataset,
        KermanyOCTDataset,
        OCTDLDataset,
        OCTIDDataset,
        RetinalOCTC8Dataset,
        OCTCirrusDataset,
        OLIVESDataset,
        RastiDataset,
    )
    from eyedatahub.datasets.surgical_datasets import (
        Cataract1KDataset,
        OphNet2024Dataset,
        OphoraDataset,
    )
    from eyedatahub.datasets.oct_segmentation import (
        OCTMSJHUDataset,
        DukeChiuBOEDataset,
        UMNParhiDataset,
        iChallengeOCTDataset,
        DukeRPEDCDataset,
        OIMHSDataset,
        AMDSDDataset,
        OCTAVEDataset,
        CAVRIDataset,
        TianDataset,
    )
    from eyedatahub.datasets.visual_field import (
        GRAPEDataset,
        UWHVFDataset,
    )
    from eyedatahub.datasets.confocal import (
        CORN1500Dataset,
        CORNCollectionDataset,
        CORNProDataset,
        QiluCCMNerveSegmentationDataset,
    )
    from eyedatahub.datasets.stage_challenge import (
        STAGETask1Dataset,
        STAGETask2Dataset,
        STAGETask3Dataset,
    )
    from eyedatahub.datasets.ichallenge_datasets import (
        PALMDataset,
        AGEDataset,
        ADAMDataset,
        REFUGE1MultiRaterDataset,
        REFUGE2Dataset,
        GAMMADataset,
        GOALSDataset,
    )
    from eyedatahub.datasets.zenodo_10035093 import JustRAIGSDataset
    from eyedatahub.datasets.uwf_datasets import (
        TsukazakiUWFDataset,
        UWFTumorDataset,
        OculoScopeDataset,
        DeepDRiDDataset,
        UWFDRDataset,
    )
    from eyedatahub.datasets.community_recent import (
        BRSETDataset,
        MBRSETDataset,
        HarvardFairVisionDataset,
        OCT5kDataset,
        MARIODataset,
        MultiEYEDataset,
        UWFZhejiangDataset,
        UWFDRPengDataset,
        ROPOstravaDataset,
        ROPUWFIntelligentDataset,
        FOVEADataset,
        FundusAVSegDataset,
        HPMIDataset,
        CSDIDataset,
        SLIDDataset,
        Eyecare100KDataset,
    )
    from eyedatahub.datasets.community_2026 import (
        CataractLMMDataset,
        MIGSVideoDataset,
        Cataract101Dataset,
        CaDISDataset,
        InSegCatDataset,
        ERDESDataset,
        RVOMEDataset,
        MCOADataset,
        ASOCTKeratitisDataset,
        TearMeniscusDataset,
        COph100Dataset,
        TOM500Dataset,
        MMRetinalReasonDataset,
        OcularChatVQADataset,
        FairVLMedDataset,
        PairedRetinaDataset,
        RetinalDRLongitudinalDataset,
    )
    from eyedatahub.datasets.platform_2026 import DISCOVERY_DATASETS
    from eyedatahub.datasets.repository_search_other_2026 import (
        OTHER_REPOSITORY_DATASETS,
    )
    from eyedatahub.datasets.repository_search_mendeley_2026 import (
        MENDELEY_REPOSITORY_SEARCH_DATASETS,
    )
    from eyedatahub.datasets.dryad_2026 import DRYAD_DISCOVERY_DATASETS
    from eyedatahub.datasets.repository_refresh_2026 import REFRESH_DATASETS
    from eyedatahub.datasets.gaze_iris_refresh_2026 import GAZE_IRIS_DATASETS
    from eyedatahub.datasets.literature_refresh_2026 import LITERATURE_DATASETS
    from eyedatahub.datasets.community_classics import (
        EOphthaDataset,
        ROCDataset,
        DRIONSDBDataset,
        RITEDataset,
        FIREDataset,
        RIGADataset,
        LAGDataset,
        ChaksuDataset,
        HYGDDataset,
        SMDGDataset,
        MuReDDataset,
        SUSTechSYSUDataset,
        ParaguayDRDataset,
        JichiDRDataset,
        DRTiDDataset,
        MFIDDRDataset,
        RETOUCHDataset,
        ROSEDataset,
        OCTA500Dataset,
        PrimeFP20Dataset,
        CATARACTS2017Dataset,
        DeepEyeNetDataset,
    )

    datasets = [
        # Vessel segmentation (fundus)
        STAREDataset(),
        CHASE_DB1Dataset(),
        HRFDataset(),
        FIVESDataset(),
        RAVIRDataset(),
        # DR grading / lesion segmentation
        APTOS2019Dataset(),
        MESSIDOR2Dataset(),
        IDRiDDataset(),
        DDRDataset(),
        MAPLESDRDataset(),
        EyePACSDataset(),
        BiDRDataset(),
        DRArrangedDataset(),
        MMRDRDataset(),
        # Glaucoma
        REFUGE2018Dataset(),
        RIMONEDLDataset(),
        DRISHTIGSDataset(),
        G1020Dataset(),
        AIROGSDataset(),
        PAPILADataset(),
        HarvardGlaucomaFundusDataset(),
        ACRIMADataset(),
        BEHDataset(),
        HarvardGDPDataset(),
        # AMD
        iChallengeAMDDataset(),
        # Multi-disease fundus
        RFMiDDataset(),
        ODIR2019Dataset(),
        JSIECDataset(),
        CataractDataset(),
        NEHUTDataset(),
        # Misc fundus
        AODDataset(),
        ToxoFundusDataset(),
        FARFUMROPDataset(),
        # OCT / OCTA — classification + biomarkers
        KermanyOCTDataset(),
        OCTIDDataset(),
        AROIDataset(),
        DRAC22Dataset(),
        RetinalOCTC8Dataset(),
        OCTDLDataset(),
        OCTCirrusDataset(),
        OLIVESDataset(),
        RastiDataset(),
        # OCT — layer / fluid segmentation
        OCTMSJHUDataset(),
        DukeChiuBOEDataset(),
        UMNParhiDataset(),
        iChallengeOCTDataset(),
        DukeRPEDCDataset(),
        OIMHSDataset(),
        AMDSDDataset(),
        OCTAVEDataset(),
        CAVRIDataset(),
        TianDataset(),
        # Visual field / perimetry
        UWHVFDataset(),
        GRAPEDataset(),
        # Corneal confocal microscopy (IVCM)
        CORN1500Dataset(),
        CORNProDataset(),
        CORNCollectionDataset(),
        QiluCCMNerveSegmentationDataset(),
        # STAGE Challenge 2023 — OCT → visual field prediction
        STAGETask1Dataset(),
        STAGETask2Dataset(),
        STAGETask3Dataset(),
        # iChallenge / HDMILab ophthalmic challenges
        PALMDataset(),
        AGEDataset(),
        ADAMDataset(),
        REFUGE1MultiRaterDataset(),
        REFUGE2Dataset(),
        GAMMADataset(),
        GOALSDataset(),
        # JustRAIGS glaucoma screening (EyePACS images + Rotterdam labels)
        JustRAIGSDataset(),
        # Ultra-widefield (UWF) fundus datasets
        TsukazakiUWFDataset(),
        UWFTumorDataset(),
        OculoScopeDataset(),
        DeepDRiDDataset(),
        UWFDRDataset(),
        # Surgical video datasets
        Cataract1KDataset(),
        OphNet2024Dataset(),
        OphoraDataset(),
        # Community: recently-released (2024-2026) public ophthalmic datasets
        # See eyedatahub/datasets/community_recent.py — load() stubs welcome PR.
        BRSETDataset(),
        MBRSETDataset(),
        HarvardFairVisionDataset(),
        OCT5kDataset(),
        MARIODataset(),
        MultiEYEDataset(),
        UWFZhejiangDataset(),
        UWFDRPengDataset(),
        ROPOstravaDataset(),
        ROPUWFIntelligentDataset(),
        FOVEADataset(),
        FundusAVSegDataset(),
        HPMIDataset(),
        CSDIDataset(),
        SLIDDataset(),
        Eyecare100KDataset(),
        # Community: classic community-standard datasets cited across 2+
        # public catalogs (FLAIR, MIRAGE, EyecareGPT, openmedlab, Khan 2021,
        # etc.) that were not yet in EyeDataHub. See community_classics.py.
        EOphthaDataset(),
        ROCDataset(),
        DRIONSDBDataset(),
        RITEDataset(),
        FIREDataset(),
        RIGADataset(),
        LAGDataset(),
        ChaksuDataset(),
        HYGDDataset(),
        SMDGDataset(),
        MuReDDataset(),
        SUSTechSYSUDataset(),
        ParaguayDRDataset(),
        JichiDRDataset(),
        DRTiDDataset(),
        MFIDDRDataset(),
        RETOUCHDataset(),
        ROSEDataset(),
        OCTA500Dataset(),
        PrimeFP20Dataset(),
        CATARACTS2017Dataset(),
        DeepEyeNetDataset(),
        # Community: 2026 gap-search additions
        # See eyedatahub/datasets/community_2026.py — 17 datasets
        # spanning surgical video, ocular ultrasound (new), anterior-segment
        # OCT, orbital MRI (new), tear meniscus, pediatric registration,
        # and retinal VQA/dialogue.
        CataractLMMDataset(),
        MIGSVideoDataset(),
        Cataract101Dataset(),
        CaDISDataset(),
        InSegCatDataset(),
        ERDESDataset(),
        RVOMEDataset(),
        MCOADataset(),
        ASOCTKeratitisDataset(),
        TearMeniscusDataset(),
        COph100Dataset(),
        TOM500Dataset(),
        MMRetinalReasonDataset(),
        OcularChatVQADataset(),
        FairVLMedDataset(),
        PairedRetinaDataset(),
        RetinalDRLongitudinalDataset(),
        # Platform sweep: Mendeley, Zenodo, Kaggle, Hugging Face,
        # PhysioNet, and Grand Challenge additions from July 2026.
        *DISCOVERY_DATASETS,
        # Canonical resources retained from the complete August 2026
        # Figshare, Kaggle, and Hugging Face repository searches.
        *OTHER_REPOSITORY_DATASETS,
        # Canonical resources retained from the complete August 2026
        # Mendeley Data repository search.
        *MENDELEY_REPOSITORY_SEARCH_DATASETS,
        # Ocular and ophthalmic records retained after the complete August
        # 2026 Dryad API search and source-level screening.
        *DRYAD_DISCOVERY_DATASETS,
        # Literature and repository refresh through July 14, 2026.
        *REFRESH_DATASETS,
        # Bounded gaze, pupil, and iris-biometrics gap refresh.
        *GAZE_IRIS_DATASETS,
        # Fundus and OCT records recovered from the July 2026 literature review.
        *LITERATURE_DATASETS,
    ]

    for ds in datasets:
        # Curated source records remain in their modules and dated screening
        # ledgers, but records outside the human/model-use boundary are not
        # exposed as headline catalog entries.
        if ds.info.name in CATALOG_SCOPE_EXCLUSIONS:
            continue
        REGISTRY.register(ds)


_register_all()
