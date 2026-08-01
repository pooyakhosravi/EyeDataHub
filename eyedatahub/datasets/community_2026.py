"""Community datasets identified in the 2026 gap search.

These 17 datasets were flagged by the EyeDataHub Gap Search Memo as
either missing from the registry or providing new modality coverage
(ocular ultrasound video, orbital MRI, anterior-segment OCT, tear
meniscus, pediatric fundus registration, retinal VQA/dialogue).

Every entry carries verified DatasetInfo + real download backends
wherever the upstream permits. `load()` is a stub via
`_StubLoadMixin` for now — full parser implementations welcome PR.
"""
from __future__ import annotations

from pathlib import Path
from typing import Union

from eyedatahub.core.dataset import DatasetInfo, EyeDataHubDataset
from eyedatahub.datasets.community_recent import _StubLoadMixin
from eyedatahub.datasets.download_utils import (
    download_figshare,
    download_figshare_collection,
    download_huggingface,
    download_zenodo,
    print_manual_download_instructions,
)


# ===========================================================================
# Surgical video
# ===========================================================================


class CataractLMMDataset(_StubLoadMixin, EyeDataHubDataset):
    """Cataract-LMM: large-scale multi-source cataract surgery benchmark
    (Ahmadi et al., Sci Data 2026). 3,000 procedures, 1,134 hours."""

    _SUBDIR = "cataract_lmm"
    _HF_REPO = "mjahmadi/Cataract-LMM"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="cataract_lmm",
            full_name="Cataract-LMM: Large-Scale Multi-Source Multi-Task Cataract Surgery Benchmark",
            description=(
                "3,000 cataract surgery procedures, 1,134.2 hours of video with "
                "phase annotations, instance segmentation, tracking, and skill "
                "scoring. Largest public cataract-surgery-video resource."
            ),
            modality="surgical_video",
            tasks=["classification", "segmentation", "multilabel"],
            num_samples=3000,
            splits=["train", "val", "test"],
            download_type="huggingface",
            download_url="https://huggingface.co/datasets/mjahmadi/Cataract-LMM",
            license="CC BY-NC-ND 4.0",
            citation=(
                "Ahmadi MJ, Gandomi I, Abdi P, et al., 'Cataract-LMM: "
                "Large-scale multi-source multi-task benchmark for deep "
                "learning in surgical video analysis', Scientific Data 2026. "
                "doi:10.1038/s41597-026-07464-0"
            ),
            tags=["surgical_video", "cataract", "phase_recognition",
                  "instance_segmentation", "skill_scoring", "large_scale"],
            size_gb=200.0,
            notes=(
                "Largest public cataract-surgery-video resource by hours. "
                "CC BY-NC-ND 4.0 — non-commercial + no derivatives on HF."
            ),
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        download_huggingface(
            self._HF_REPO, Path(data_dir) / self._SUBDIR, repo_type="dataset",
        )


class MIGSVideoDataset(_StubLoadMixin, EyeDataHubDataset):
    """Multicenter fine-annotated MIGS video dataset (Wang et al., Sci Data 2026).
    Minimally invasive glaucoma surgery workflow."""

    _SUBDIR = "migs_video"
    _ZENODO_RECORD = "19438128"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="migs_video",
            full_name="Multicenter Fine-Annotated MIGS Surgical Video Dataset",
            description=(
                "A multicenter collection of 186 minimally invasive glaucoma "
                "surgery (MIGS) videos with annotations for surgical-phase "
                "recognition and semantic segmentation of instruments and "
                "anatomical structures."
            ),
            modality="surgical_video",
            tasks=["classification", "segmentation"],
            num_samples=186,
            splits=["train", "val", "test"],
            download_type="zenodo",
            download_url="https://zenodo.org/records/19438128",
            license="CC BY 4.0",
            citation=(
                "Wang D, Zhang Y, Li Y, et al., 'Multicenter fine annotated "
                "surgical video dataset for minimally invasive glaucoma "
                "surgery', Scientific Data 2026. "
                "doi:10.1038/s41597-026-07535-2"
            ),
            tags=["surgical_video", "glaucoma", "migs", "phase_recognition",
                  "multicenter"],
            size_gb=10.23,
            notes=(
                "The current Zenodo version is 10.5281/zenodo.19438128 under "
                "CC BY 4.0; the version-independent concept DOI is "
                "10.5281/zenodo.18231908. The associated article cites the "
                "earlier deposit version 10.5281/zenodo.18231909."
            ),
            item_count_unit="videos",
            source_landing_page_url="https://zenodo.org/records/19438128",
            preferred_route_type="official_repository",
            preferred_route_url="https://zenodo.org/records/19438128",
            access_friction="anonymous_direct",
            requires_registration=False,
            requires_authentication=False,
            requires_api_token=False,
            requires_clickthrough=False,
            requires_manual_approval=False,
            requires_data_use_agreement=False,
            requires_author_contact=False,
            requires_payment=False,
            availability_status="available",
            route_last_checked="2026-07-25",
            route_check_result="acquisition_route_verified",
            route_check_notes=(
                "The public Zenodo record and its 25-file listing were checked; "
                "the complete 10.98 GB (10.23 GiB) deposit was not transferred."
            ),
            source_terms="CC BY 4.0",
            terms_evidence_url="https://zenodo.org/records/19438128",
            terms_scope="dataset_files",
            terms_component_notes=(
                "The Zenodo dataset files are marked CC BY 4.0. The associated "
                "article has separate publication terms."
            ),
            dataset_doi="10.5281/zenodo.19438128",
            repository_record_id="zenodo:19438128",
            associated_publication_doi="10.1038/s41597-026-07535-2",
            canonical_resolver_url="https://doi.org/10.5281/zenodo.19438128",
            item_count_evidence_url="https://doi.org/10.1038/s41597-026-07535-2",
            modality_evidence_url="https://doi.org/10.1038/s41597-026-07535-2",
            task_evidence_url="https://doi.org/10.1038/s41597-026-07535-2",
            citation_evidence_url="https://doi.org/10.1038/s41597-026-07535-2",
            author_source_checked=True,
            source_check_date="2026-07-25",
            source_check_status="checked_against_cited_source",
            access_check_status="acquisition_route_verified",
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        download_zenodo(
            self._ZENODO_RECORD,
            Path(data_dir) / self._SUBDIR,
            extract=False,
        )


class Cataract101Dataset(_StubLoadMixin, EyeDataHubDataset):
    """Cataract-101: 101 cataract surgery videos with phase annotations
    (Schoeffmann et al., ACM MMSys 2018)."""

    _SUBDIR = "cataract_101"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="cataract_101",
            full_name="Cataract-101: 101 Cataract Surgery Videos with Phase Annotations",
            description=(
                "101 cataract surgery videos with 10-phase workflow "
                "annotations. Canonical older cataract benchmark."
            ),
            modality="surgical_video",
            tasks=["classification"],
            num_samples=101,
            splits=["all"],
            num_classes=10,
            download_type="manual",
            download_url="https://ftp.itec.aau.at/datasets/ovid/cat-101/",
            license="Research only (ITEC AAU)",
            citation=(
                "Schoeffmann K, Taschwer M, Sarny S, Munzer B, Primus MJ, "
                "Putzgruber D, 'Cataract-101 — video dataset of 101 cataract "
                "surgeries', ACM MMSys 2018."
            ),
            tags=["surgical_video", "cataract", "phase_recognition", "classical"],
            size_gb=25.0,
            notes="ITEC public FTP; license verify against institutional page.",
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        print_manual_download_instructions(
            "Cataract-101", self.info.download_url,
            Path(data_dir) / self._SUBDIR,
            extra_notes="ITEC AAU FTP — browse and download videos manually.",
        )


class CaDISDataset(_StubLoadMixin, EyeDataHubDataset):
    """CaDIS: Cataract Dataset for Image Segmentation (Grammatikopoulou et al.,
    2019). Semantic segmentation labels on CATARACTS challenge videos."""

    _SUBDIR = "cadis"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="cadis",
            full_name="CaDIS: Cataract Dataset for Image Segmentation",
            description=(
                "Semantic segmentation labels for 4,670 frames from 25 "
                "cataract surgery videos (CATARACTS challenge). 25 anatomy "
                "and instrument classes."
            ),
            modality="surgical_video",
            tasks=["segmentation"],
            num_samples=4670,
            splits=["train", "val", "test"],
            num_classes=25,
            download_type="manual",
            download_url="https://cataracts-semantic-segmentation2020.grand-challenge.org/",
            license="Research only (Grand Challenge terms)",
            citation=(
                "Grammatikopoulou M, Flouty E, Kadkhodamohammadi A, et al., "
                "'CaDIS: Cataract dataset for image segmentation', arXiv "
                "1906.11586, 2019."
            ),
            tags=["surgical_video", "cataract", "semantic_segmentation",
                  "instruments", "anatomy"],
            size_gb=15.0,
            notes="Standard cataract-scene segmentation benchmark. Grand Challenge account required.",
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        print_manual_download_instructions(
            "CaDIS", self.info.download_url,
            Path(data_dir) / self._SUBDIR,
            extra_notes="Grand Challenge account required — accept terms then download.",
        )


class InSegCatDataset(_StubLoadMixin, EyeDataHubDataset):
    """InSegCat: cataract-surgery instance segmentation (ITEC)."""

    _SUBDIR = "insegcat"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="insegcat",
            full_name="InSegCat: Instance Segmentation for Cataract Surgery",
            description=(
                "Two COCO-format instance-segmentation datasets derived from "
                "cataract surgery videos, covering instruments and anatomical "
                "structures."
            ),
            modality="surgical_video",
            tasks=["segmentation"],
            num_samples=None,
            splits=["train", "test"],
            download_type="manual",
            download_url="https://ftp.itec.aau.at/datasets/ovid/InSegCat/",
            license="Research only (ITEC AAU)",
            citation=(
                "InSegCat dataset, ITEC AAU. COCO-format instance segmentation "
                "for cataract surgery."
            ),
            tags=["surgical_video", "cataract", "instance_segmentation", "coco"],
            size_gb=10.0,
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        print_manual_download_instructions(
            "InSegCat", self.info.download_url,
            Path(data_dir) / self._SUBDIR,
        )


# ===========================================================================
# Ocular ultrasound video (NEW MODALITY)
# ===========================================================================


class ERDESDataset(_StubLoadMixin, EyeDataHubDataset):
    """ERDES: ocular ultrasound video benchmark for retinal detachment
    (Ozkut et al., arXiv 2025). 5,381 B-scan clips, 5h 10min total."""

    _SUBDIR = "erdes"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="erdes",
            full_name="ERDES: Ocular Ultrasound Video Benchmark (Retinal Detachment + Macula)",
            description=(
                "5,381 B-scan ocular ultrasound video clips with retinal-"
                "detachment presence and macula-on/off status labels. Total "
                "runtime approximately 5 hours 10 minutes. Only public "
                "ocular ultrasound video benchmark."
            ),
            modality="multimodal",  # ultrasound is a new modality; using multimodal until formalized
            tasks=["classification"],
            num_samples=5381,
            splits=["train", "val", "test"],
            num_classes=3,
            classes=["no_rd", "rd_macula_on", "rd_macula_off"],
            download_type="manual",
            download_url="https://arxiv.org/abs/2503.04525",
            license="Unknown — needs check (open-access project site)",
            citation=(
                "Ozkut Y, Navard P, Adhikari S, et al., 'ERDES: A benchmark "
                "video dataset for retinal detachment and macular status "
                "classification in ocular ultrasound', arXiv 2503.04525, 2025."
            ),
            tags=["ultrasound", "video", "retinal_detachment", "emergency",
                  "new_modality"],
            size_gb=5.0,
            notes=(
                "Adds ocular ultrasound video — modality EyeDataHub otherwise "
                "lacks. Project page at github/arxiv referenced. Access "
                "verified via project site."
            ),
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        print_manual_download_instructions(
            "ERDES", self.info.download_url,
            Path(data_dir) / self._SUBDIR,
            extra_notes="Project site linked from arXiv 2503.04525.",
        )


# ===========================================================================
# OCT
# ===========================================================================


class RVOMEDataset(_StubLoadMixin, EyeDataHubDataset):
    """RVO-ME: dual-task OCT dataset for RVO macular edema (Xiong et al.,
    Sci Data 2026). 3,012 B-scans, 146 eyes."""

    _SUBDIR = "rvo_me"
    _FIGSHARE_ID = "29804435"
    _DATA_DOI = "10.6084/m9.figshare.29804435.v1"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="rvo_me",
            full_name="RVO-ME: Retinal Vein Occlusion Macular Edema OCT Dataset",
            description=(
                "3,012 OCT B-scans from 146 eyes / 130 patients with retinal "
                "vein occlusion. Dual-task labels: fluid segmentation + "
                "retinal-layer segmentation. Detection of macular lesions."
            ),
            modality="oct",
            tasks=["segmentation", "classification"],
            num_samples=3012,
            splits=["all"],
            download_type="figshare",
            download_url=f"https://doi.org/{self._DATA_DOI}",
            license="CC BY 4.0",
            citation=(
                "Xiong F, et al., 'RVO-ME: A dual-task OCT dataset for "
                "segmentation and detection of macular lesions in retinal "
                "vein occlusion', Scientific Data 2026."
            ),
            tags=["oct", "rvo", "macular_edema", "fluid_segmentation",
                  "layer_segmentation"],
            size_gb=2.0,
            notes="Sci Data 2026 release; verify source license before reuse.",
            dataset_doi=self._DATA_DOI,
            associated_publication_doi="10.1038/s41597-026-06695-5",
            terms_scope="dataset_files",
            terms_evidence_url=f"https://doi.org/{self._DATA_DOI}",
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        download_figshare(self._FIGSHARE_ID, Path(data_dir) / self._SUBDIR)


# ===========================================================================
# Anterior segment / AS-OCT
# ===========================================================================


class MCOADataset(_StubLoadMixin, EyeDataHubDataset):
    """MCOA: multimodal corneal opacity assessment (Ma et al., Sci Data 2025).
    6,272 AS-OCT + 392 anterior-segment photos."""

    _SUBDIR = "mcoa"
    _FIGSHARE_ID = "28123088"
    _DATA_DOI = "10.6084/m9.figshare.28123088.v1"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="mcoa",
            full_name="MCOA: Multimodal Corneal Opacity Assessment Dataset",
            description=(
                "6,272 AS-OCT images + 392 anterior-segment photographs for "
                "corneal opacity assessment with expert grading. First large "
                "public multimodal AS-OCT + photo dataset for cornea."
            ),
            modality="multimodal",
            tasks=["classification", "grading"],
            num_samples=6664,
            splits=["all"],
            num_classes=4,
            download_type="figshare",
            download_url=f"https://doi.org/{self._DATA_DOI}",
            license="CC BY 4.0",
            citation=(
                "Ma X, et al., 'MCOA: A comprehensive multimodal dataset for "
                "advancing deep learning in corneal opacity assessment', "
                "Scientific Data 2025."
            ),
            tags=["anterior_segment", "cornea", "as_oct", "opacity",
                  "multimodal", "grading"],
            size_gb=8.0,
            notes="Anterior-segment expansion; modality otherwise sparse.",
            modalities=["multimodal", "oct", "external_eye"],
            dataset_doi=self._DATA_DOI,
            associated_publication_doi="10.1038/s41597-025-05205-3",
            terms_scope="dataset_files",
            terms_evidence_url=f"https://doi.org/{self._DATA_DOI}",
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        download_figshare(self._FIGSHARE_ID, Path(data_dir) / self._SUBDIR)


class ASOCTKeratitisDataset(_StubLoadMixin, EyeDataHubDataset):
    """AS-OCT keratitis dataset for 3D reconstruction (Sun et al., Sci Data 2024).
    1,168 AS-OCT images with lesion/cornea/iris segmentation."""

    _SUBDIR = "as_oct_keratitis"
    _FIGSHARE_COLLECTION_ID = "7036994"
    _DATA_DOI = "10.6084/m9.figshare.c.7036994.v1"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="as_oct_keratitis",
            full_name="AS-OCT Keratitis Segmentation Dataset",
            description=(
                "1,168 anterior-segment OCT images of keratitis with per-pixel "
                "lesion, cornea, and iris segmentation labels. Enables 3D "
                "reconstruction from B-scan stacks."
            ),
            modality="oct",
            tasks=["segmentation"],
            num_samples=1168,
            splits=["all"],
            num_classes=4,
            classes=["background", "lesion", "cornea", "iris"],
            download_type="figshare",
            download_url=f"https://doi.org/{self._DATA_DOI}",
            license="CC0 1.0",
            citation=(
                "Sun Y, et al., 'An AS-OCT image dataset for deep "
                "learning-enabled segmentation and 3D reconstruction for "
                "keratitis', Scientific Data 2024."
            ),
            tags=["anterior_segment", "cornea", "keratitis", "as_oct",
                  "segmentation", "3d"],
            size_gb=1.5,
            notes="Adds corneal infectious disease + 3D AS-OCT use case.",
            dataset_doi=self._DATA_DOI,
            associated_publication_doi="10.1038/s41597-024-03464-0",
            terms_scope="dataset_files",
            terms_evidence_url=f"https://doi.org/{self._DATA_DOI}",
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        download_figshare_collection(
            self._FIGSHARE_COLLECTION_ID, Path(data_dir) / self._SUBDIR
        )


class TearMeniscusDataset(_StubLoadMixin, EyeDataHubDataset):
    """Multicenter tear meniscus segmentation (Sci Data 2025).
    1,693 color + 1,739 IR images from 5 centers."""

    _SUBDIR = "tear_meniscus"
    _FIGSHARE_ID = "28650536"
    _DATA_DOI = "10.6084/m9.figshare.28650536.v2"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="tear_meniscus",
            full_name="Multicentre Tear Meniscus Segmentation Dataset",
            description=(
                "1,693 color and 1,739 infrared ocular-surface images from "
                "five clinical centers with pixel-level tear-meniscus "
                "segmentation. First multi-center dry-eye imaging benchmark."
            ),
            modality="multimodal",
            tasks=["segmentation"],
            num_samples=3432,
            splits=["all"],
            num_classes=2,
            download_type="figshare",
            download_url=f"https://doi.org/{self._DATA_DOI}",
            license="CC BY 4.0",
            citation=(
                "Multicentre tear meniscus segmentation dataset, Scientific "
                "Data 2025."
            ),
            tags=["ocular_surface", "tear_meniscus", "dry_eye", "segmentation",
                  "multicenter", "new_modality"],
            size_gb=1.5,
            notes=(
                "Figshare marks the deposited files CC BY 4.0. Adds a "
                "dry-eye and tear-film modality that is otherwise absent."
            ),
            dataset_doi=self._DATA_DOI,
            terms_scope="dataset_files",
            terms_evidence_url=f"https://doi.org/{self._DATA_DOI}",
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        download_figshare(self._FIGSHARE_ID, Path(data_dir) / self._SUBDIR)


# ===========================================================================
# Pediatric fundus / registration
# ===========================================================================


class COph100Dataset(_StubLoadMixin, EyeDataHubDataset):
    """COph100 / RIDIRP: pediatric fundus registration (Hu et al., Sci Data 2025).
    100 infant eyes, 491 image pairs."""

    _SUBDIR = "coph100"
    _FIGSHARE_ID = "27061084"
    _DATA_DOI = "10.6084/m9.figshare.27061084.v1"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="coph100",
            full_name="COph100: Comprehensive Infant Fundus Image Registration Dataset (RIDIRP)",
            description=(
                "100 infant eyes with 491 image pairs annotated with "
                "ground-truth control points and vessel masks. Enables "
                "pediatric / ROP-relevant fundus registration research."
            ),
            modality="fundus",
            tasks=["regression", "segmentation"],
            num_samples=982,  # 491 pairs
            splits=["all"],
            download_type="figshare",
            download_url=f"https://doi.org/{self._DATA_DOI}",
            license="CC BY 4.0",
            citation=(
                "Hu Y, et al., 'COph100: A comprehensive fundus image "
                "registration dataset from infants constituting the RIDIRP "
                "database', Scientific Data 2025;12:99."
            ),
            tags=["fundus", "pediatric", "rop", "registration", "infant",
                  "vessel"],
            size_gb=1.0,
            notes="Adds infant fundus registration; complements ROP classification datasets.",
            dataset_doi=self._DATA_DOI,
            associated_publication_doi="10.1038/s41597-025-04426-w",
            terms_scope="dataset_files",
            terms_evidence_url=f"https://doi.org/{self._DATA_DOI}",
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        download_figshare(self._FIGSHARE_ID, Path(data_dir) / self._SUBDIR)


# ===========================================================================
# Orbital MRI (NEW MODALITY)
# ===========================================================================


class TOM500Dataset(_StubLoadMixin, EyeDataHubDataset):
    """TOM500: multi-organ orbital MRI for thyroid eye disease (Zhang et al.,
    Sci Data 2025). T2-weighted orbital MRI."""

    _SUBDIR = "tom500"
    _FIGSHARE_ID = "27133389"
    _DATA_DOI = "10.6084/m9.figshare.27133389.v1"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="tom500",
            full_name="TOM500: Multi-Organ Annotated Orbital MRI Dataset for Thyroid Eye Disease",
            description=(
                "T2-weighted orbital MRI volumes with multi-organ segmentation "
                "labels (extraocular muscles, optic nerve, lacrimal gland, "
                "orbital fat) and paired clinical data. First public orbital "
                "MRI benchmark for thyroid eye disease."
            ),
            modality="multimodal",  # MRI is a new modality here
            tasks=["segmentation"],
            num_samples=500,
            splits=["all"],
            download_type="figshare",
            download_url=f"https://doi.org/{self._DATA_DOI}",
            license="CC0 1.0",
            citation=(
                "Zhang H, et al., 'TOM500: A multi-organ annotated orbital "
                "MRI dataset for thyroid eye disease', Scientific Data 2025."
            ),
            tags=["orbital_mri", "thyroid_eye_disease", "segmentation",
                  "multi_organ", "new_modality"],
            size_gb=2.31,
            notes="Adds orbital MRI; modality outside typical ophthalmic imaging.",
            modalities=["multimodal", "orbital_mri"],
            dataset_doi=self._DATA_DOI,
            associated_publication_doi="10.1038/s41597-025-04427-9",
            terms_scope="dataset_files",
            terms_evidence_url=f"https://doi.org/{self._DATA_DOI}",
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        download_figshare(self._FIGSHARE_ID, Path(data_dir) / self._SUBDIR)


# ===========================================================================
# VQA / VLM datasets
# ===========================================================================


class MMRetinalReasonDataset(_StubLoadMixin, EyeDataHubDataset):
    """MM-Retinal-Reason: retinal VQA / multimodal reasoning (HF 2025)."""

    _SUBDIR = "mm_retinal_reason"
    _HF_REPO = "lxirich/MM-Retinal-Reason"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="mm_retinal_reason",
            full_name="MM-Retinal-Reason: Ophthalmology Multimodal Reasoning Dataset",
            description=(
                "Ophthalmology-specific multimodal reasoning dataset built "
                "from 45 public datasets. Chain-of-thought reasoning traces "
                "for retinal VQA."
            ),
            modality="multimodal",
            tasks=["classification", "multilabel"],
            num_samples=None,
            splits=["train", "val", "test"],
            download_type="huggingface",
            download_url="https://huggingface.co/datasets/lxirich/MM-Retinal-Reason",
            license="Mixed (inherits from 45 source datasets) — verify per-row",
            citation=(
                "MM-Retinal-Reason: Ophthalmology multimodal reasoning "
                "dataset. HuggingFace, 2025."
            ),
            tags=["vqa", "vlm", "reasoning", "retina", "chain_of_thought"],
            size_gb=15.0,
            notes=(
                "Aggregates 45 source datasets — image licenses inherit; "
                "verify per-row before commercial use."
            ),
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        download_huggingface(
            self._HF_REPO, Path(data_dir) / self._SUBDIR, repo_type="dataset",
        )


class OcularChatVQADataset(_StubLoadMixin, EyeDataHubDataset):
    """OcularChat-VQA: AREDS-derived patient-physician dialogue VQA (HF)."""

    _SUBDIR = "ocular_chat_vqa"
    _HF_REPO = "ncbi/OcularChat-VQA"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="ocular_chat_vqa",
            full_name="OcularChat-VQA: AREDS-Derived Patient-Physician Dialogue Dataset",
            description=(
                "844,000 simulated patient-physician dialogue rows generated "
                "from AREDS clinical visits. Enables ophthalmic dialogue and "
                "counseling VLM training."
            ),
            modality="multimodal",
            tasks=["classification"],
            num_samples=844000,
            splits=["train", "val", "test"],
            download_type="huggingface",
            download_url="https://huggingface.co/datasets/ncbi/OcularChat-VQA",
            license="CC BY-NC-SA 4.0",
            citation=(
                "OcularChat-VQA: AREDS-derived patient-physician dialogues. "
                "HuggingFace / NCBI, 2025."
            ),
            tags=["vqa", "vlm", "dialogue", "amd", "areds", "large_scale"],
            size_gb=8.0,
            notes=(
                "Images path may reference AREDS — access to underlying "
                "images requires separate NCBI/dbGaP approval. Verify "
                "before use."
            ),
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        download_huggingface(
            self._HF_REPO, Path(data_dir) / self._SUBDIR, repo_type="dataset",
        )


class FairVLMedDataset(_StubLoadMixin, EyeDataHubDataset):
    """FairVLMed: glaucoma SLO images, clinical notes, and tabular fields."""

    _SUBDIR = "fairvlmed"
    _HF_REPO = "harvardairobotics/FairVLMed"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="fairvlmed",
            full_name="FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset",
            description=(
                "10,000 scanning-laser ophthalmoscopy fundus images paired "
                "with de-identified clinical notes, visual-field measurements, "
                "glaucoma labels, and demographic attributes."
            ),
            modality="multimodal",
            tasks=["classification", "report_generation", "fairness_analysis"],
            num_samples=10000,
            splits=["train", "val", "test"],
            download_type="huggingface",
            download_url="https://huggingface.co/datasets/harvardairobotics/FairVLMed",
            license="CC BY-NC-ND 4.0",
            citation=(
                "Harvard AI Robotics, FairVLMed: Fair vision-language medical "
                "ophthalmic dataset. HuggingFace, 2024."
            ),
            tags=[
                "multimodal",
                "fundus",
                "slo",
                "visual_field",
                "tabular",
                "vlm",
                "fairness",
                "harvard",
                "clinical_text",
                "glaucoma",
            ],
            size_gb=10.0,
            notes=(
                "The official dataset card reports 10,000 patients and "
                "10,000 samples (7,000 train, 1,000 validation, 2,000 test). "
                "No source statement supporting cohort identity with the "
                "separate Harvard-FairVision record was found, so no catalog "
                "relationship is asserted."
            ),
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        download_huggingface(
            self._HF_REPO, Path(data_dir) / self._SUBDIR, repo_type="dataset",
        )


class PairedRetinaDataset(_StubLoadMixin, EyeDataHubDataset):
    """Paired Retina Dataset: cross-device fundus pairs (HF 2025)."""

    _SUBDIR = "paired_retina"
    _HF_REPO = "smartretina2025/paired_retina"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="paired_retina",
            full_name="Paired Retina Dataset: Cross-Device Fundus Pairs",
            description=(
                "Paired tabletop and portable retinal images from the same "
                "patients, enabling cross-device domain-adaptation research."
            ),
            modality="fundus",
            tasks=["classification", "regression"],
            num_samples=None,
            splits=["train", "val", "test"],
            download_type="huggingface",
            download_url="https://huggingface.co/datasets/smartretina2025/paired_retina",
            license="Unknown — needs check (HF)",
            citation=(
                "Paired Retina Dataset: Cross-device fundus pairs. "
                "HuggingFace, 2025."
            ),
            tags=["fundus", "domain_adaptation", "paired", "portable_camera",
                  "cross_device"],
            size_gb=3.0,
            notes=(
                "Provenance and license require verification against the "
                "underlying publication before commercial use."
            ),
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        download_huggingface(
            self._HF_REPO, Path(data_dir) / self._SUBDIR, repo_type="dataset",
        )


class RetinalDRLongitudinalDataset(_StubLoadMixin, EyeDataHubDataset):
    """Retinal DR longitudinal: baseline + 2-year follow-up fundus pairs (HF)."""

    _SUBDIR = "retinal_dr_longitudinal"
    _HF_REPO = "usama10/retinal-dr-longitudinal"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="retinal_dr_longitudinal",
            full_name="Retinal DR Longitudinal Fundus Pairs",
            description=(
                "Baseline and two-year follow-up color fundus image pairs "
                "from Tianjin Medical University for diabetic-retinopathy "
                "progression research."
            ),
            modality="fundus",
            tasks=["progression", "classification"],
            num_samples=None,
            splits=["all"],
            download_type="huggingface",
            download_url="https://huggingface.co/datasets/usama10/retinal-dr-longitudinal",
            license="Unknown — needs check (HF; ethics statement in card)",
            citation=(
                "Retinal DR longitudinal fundus pairs, Tianjin Medical "
                "University. HuggingFace, 2025."
            ),
            tags=["fundus", "dr", "longitudinal", "progression", "two_year"],
            size_gb=4.0,
            notes="Verify source publication before commercial use.",
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        download_huggingface(
            self._HF_REPO, Path(data_dir) / self._SUBDIR, repo_type="dataset",
        )
