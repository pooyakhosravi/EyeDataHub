"""Recently-released (2024-2026) public ophthalmic datasets.

Each loader carries verified DatasetInfo (catalog metadata + license) and a
real machine-actionable download backend (Zenodo / Figshare / Mendeley /
Kaggle / HuggingFace / PhysioNet / direct file URL) wherever the upstream
permits automation. Where access is gated (PhysioNet credentialed, IEEE
DataPort login, application forms), the loader prints explicit instructions
and raises.

The `load()` method is intentionally a stub on `_StubLoadMixin` for many of
these — the metadata + auto-download alone is valuable for the indexed
catalog and license-aware filtering, and concrete `load()` implementations
are PRs welcome (see CONTRIBUTING.md `.claude/skills/add-dataset/`).

License + download verification: every entry was checked against its
original source page as of June 2026. Update if upstream changes.
"""
from __future__ import annotations

from pathlib import Path
from typing import List, Union

from eyedatahub.core.dataset import DatasetInfo, DatasetSample, EyeDataHubDataset
from eyedatahub.datasets.download_utils import (
    download_figshare,
    download_file,
    download_huggingface,
    download_kaggle,
    download_physionet,
    download_zenodo,
    extract_archive,
    print_manual_download_instructions,
)


# ---------------------------------------------------------------------------
# Helper: stub loader base for datasets we have indexed but not yet parsed.
# Contributors can subclass-replace `load()` with a real implementation.
# ---------------------------------------------------------------------------


class _StubLoadMixin:
    """Mixin: `load()` raises a clear NotImplementedError until a real
    parser is contributed. `is_downloaded()` checks for any image file."""

    _SUBDIR: str = ""
    _EXTENSIONS = (".png", ".jpg", ".jpeg", ".bmp", ".tif", ".tiff", ".dcm", ".npy")

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        if not root.exists():
            return False
        ignored = {".download_complete", "eyedatahub-acquisition-manifest.json"}
        return any(
            path.is_file()
            and path.name not in ignored
            and path.stat().st_size > 0
            for path in root.rglob("*")
        )

    def load(self, data_dir: Union[str, Path], split: str = "test") -> List[DatasetSample]:
        raise NotImplementedError(
            f"{self.info.name}: dataset is indexed in the catalog but no loader "
            f"has been contributed yet. See CONTRIBUTING.md and "
            f".claude/skills/add-dataset/ for the loader template. The download "
            f"backend ({self.info.download_type}) and license "
            f"({self.info.license}) are recorded; a PR adding the load() method "
            f"is the next step."
        )


# ===========================================================================
# Large-scale fundus
# ===========================================================================


class BRSETDataset(_StubLoadMixin, EyeDataHubDataset):
    """BRSET: Brazilian Multilabel Ophthalmological Dataset (Nakayama et al.,
    PLOS Digital Health 2024). 16,266 fundus images / 8,524 patients with
    14 disease labels + rich demographics."""

    _SUBDIR = "brset"
    _PHYSIONET_SLUG = "brazilian-ophthalmological"
    _VERSION = "1.0.1"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="brset",
            full_name="BRSET: Brazilian Multilabel Ophthalmological Dataset",
            description=(
                "16,266 color fundus images from 8,524 Brazilian patients with "
                "14 disease labels (DR, AMD, glaucoma, drusen, others), image "
                "quality flags, and demographic attributes."
            ),
            modality="fundus",
            tasks=["multilabel", "classification", "quality"],
            num_samples=16266,
            splits=["all"],
            num_classes=14,
            download_type="physionet",
            download_url=(
                f"https://physionet.org/content/{self._PHYSIONET_SLUG}/{self._VERSION}/"
            ),
            license="PhysioNet Credentialed Health Data License 1.5.0 (Research only)",
            citation=(
                "Nakayama LF, Restrepo D, Matos J, et al., 'BRSET: A "
                "Brazilian Multilabel Ophthalmological Dataset of Retina "
                "Fundus Photos', PLOS Digital Health 3(7):e0000454, 2024. "
                "doi:10.1371/journal.pdig.0000454 · PhysioNet DOI: "
                "10.13026/1pht-2b69"
            ),
            tags=["fundus", "multilabel", "demographics", "brazil", "large_scale"],
            size_gb=9.0,
            notes=(
                "Requires PhysioNet credentialed-user account + CITI training + "
                "signed Data Use Agreement. Set PHYSIONET_USERNAME and "
                "PHYSIONET_PASSWORD in .env to auto-download."
            ),
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        download_physionet(
            self._PHYSIONET_SLUG,
            self._VERSION,
            Path(data_dir) / self._SUBDIR,
            credentialed=True,
        )


class MBRSETDataset(_StubLoadMixin, EyeDataHubDataset):
    """mBRSET: Mobile Brazilian Retinal Dataset (Nakayama et al., Sci. Data
    2025). 5,164 handheld smartphone fundus images / 1,291 patients."""

    _SUBDIR = "mbrset"
    _PHYSIONET_SLUG = "mbrset"
    _VERSION = "1.0"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="mbrset",
            full_name="mBRSET: Mobile Brazilian Retinal Dataset",
            description=(
                "5,164 fundus images from 1,291 patients captured with the "
                "Phelcom Eyer handheld smartphone-based fundus camera. Labels "
                "for DR grading + clinical/demographic prediction."
            ),
            modality="fundus",
            tasks=["grading", "classification"],
            num_samples=5164,
            splits=["all"],
            num_classes=5,
            classes=["0_no_dr", "1_mild", "2_moderate", "3_severe", "4_proliferative"],
            download_type="physionet",
            download_url="https://physionet.org/content/mbrset/1.0/",
            license="PhysioNet Credentialed Health Data License 1.5.0 (Research only)",
            citation=(
                "Wu C, Restrepo D, Nakayama LF, et al., 'A portable retina "
                "fundus photos dataset for clinical, demographic, and "
                "diabetic retinopathy prediction', Scientific Data 12:323, "
                "2025. doi:10.1038/s41597-025-04627-3"
            ),
            tags=["fundus", "mobile", "smartphone", "brazil", "screening"],
            size_gb=3.0,
            notes=(
                "Same PhysioNet credentialed flow as BRSET. Modality EyeDataHub "
                "otherwise lacks (portable smartphone-based fundus)."
            ),
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        download_physionet(
            self._PHYSIONET_SLUG,
            self._VERSION,
            Path(data_dir) / self._SUBDIR,
            credentialed=True,
        )


class HarvardFairVisionDataset(_StubLoadMixin, EyeDataHubDataset):
    """Harvard-FairVision (Luo et al., 2024). 30,000 subjects (10K each AMD/
    DR/glaucoma) with paired SLO + OCT, plus demographic attributes for
    fairness analysis. Application-gated — no automated mirror."""

    _SUBDIR = "harvard_fairvision"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="harvard_fairvision",
            full_name="Harvard-FairVision (AMD + DR + Glaucoma, paired SLO + OCT)",
            description=(
                "30,000 subjects (10K each AMD, DR, glaucoma) with paired SLO "
                "fundus and OCT B-scans, demographic attributes (race, ethnicity, "
                "gender, language), for fairness analysis."
            ),
            modality="multimodal",
            tasks=["classification"],
            num_samples=30000,
            splits=["train", "val", "test"],
            num_classes=3,
            classes=["amd", "dr", "glaucoma"],
            download_type="manual",
            download_url="https://ophai.hms.harvard.edu/datasets/harvard-fairvision30k",
            license="CC BY-NC-ND 4.0",
            citation=(
                "Luo et al., 'FairVision: Equitable Deep Learning for Eye "
                "Disease Screening via Fair Identity Scaling', arXiv "
                "2310.02492; Harvard Ophthalmology AI Lab 2024. Three "
                "disease sub-repos: Harvard-AMD, Harvard-DR, "
                "Harvard-Glaucoma. 30,000 subjects total (10K each)."
            ),
            tags=["multimodal", "fairness", "amd", "dr", "glaucoma", "slo", "oct"],
            size_gb=600.0,
            notes=(
                "Application-gated (Harvard form). No automated mirror. "
                "Sub-repos: github.com/Harvard-Ophthalmology-AI-Lab/Harvard-{AMD,DR,Glaucoma}."
            ),
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        print_manual_download_instructions(
            "Harvard-FairVision",
            self.info.download_url,
            Path(data_dir) / self._SUBDIR,
            extra_notes=(
                "1. Apply via Harvard Ophthalmology AI Lab dataset page.\n"
                "2. Accept the data-use agreement for each sub-dataset:\n"
                "   github.com/Harvard-Ophthalmology-AI-Lab/Harvard-AMD\n"
                "   github.com/Harvard-Ophthalmology-AI-Lab/Harvard-DR\n"
                "   github.com/Harvard-Ophthalmology-AI-Lab/Harvard-Glaucoma\n"
                "3. The 10k glaucoma generative subset alone is on HF as "
                "harvardairobotics/FairGenMed (no application required)."
            ),
        )
        raise RuntimeError("Harvard-FairVision requires application-based access.")


# ===========================================================================
# OCT
# ===========================================================================


class OCT5kDataset(_StubLoadMixin, EyeDataHubDataset):
    """OCT5k: multi-disease retinal layer + lesion annotations (Morano et al.,
    Sci. Data 2024). 1,672 B-scans, 5,016 multi-grader labels."""

    _SUBDIR = "oct5k"
    _FIGSHARE_ID = "22128671"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="oct5k",
            full_name="OCT5k: Multi-Disease Retinal Layer Annotations",
            description=(
                "1,672 OCT B-scans from AMD, DME, and healthy controls with "
                "5,016 multi-grader layer annotations + lesion detection labels."
            ),
            modality="oct",
            tasks=["segmentation", "classification"],
            num_samples=1672,
            splits=["all"],
            num_classes=8,
            download_type="figshare",
            download_url="https://doi.org/10.5522/04/22128671",
            license="CC0 1.0",
            citation=(
                "Morano et al., 'OCT5k: a dataset of multi-disease and "
                "multi-graded annotations for retinal layers in OCT images', "
                "Scientific Data 2024. doi:10.1038/s41597-024-04259-z"
            ),
            tags=["oct", "layer_segmentation", "amd", "dme", "multi_grader"],
            size_gb=0.05,
            notes="UCL Research Data Repository — Figshare-backed, free download.",
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        dest = Path(data_dir) / self._SUBDIR
        download_figshare(self._FIGSHARE_ID, dest, extract=True)


class MARIODataset(_StubLoadMixin, EyeDataHubDataset):
    """MARIO Challenge: longitudinal AMD-progression OCT (MICCAI 2024)."""

    _SUBDIR = "mario"
    _ZENODO_RECORD = "15270469"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="mario",
            full_name="MARIO: AMD-Progression Longitudinal OCT (MICCAI 2024)",
            description=(
                "~30,000 longitudinal OCT B-scans across multiple patient visits, "
                "annotated for AMD change detection and progression monitoring."
            ),
            modality="oct",
            tasks=["classification", "progression"],
            num_samples=30000,
            splits=["train", "val", "test"],
            num_classes=4,
            download_type="zenodo",
            download_url="https://zenodo.org/records/15270469",
            license="CC BY 4.0",
            citation=(
                "Quellec G, Zeghlache R, et al., 'MARIO: Monitoring AMD "
                "Progression from OCT — MICCAI 2024 Challenge', arXiv "
                "2506.02976. Data: Zenodo doi:10.5281/zenodo.15270469 "
                "(2025). Peer-reviewed proceedings pending."
            ),
            tags=["oct", "amd", "longitudinal", "progression", "miccai_2024"],
            size_gb=25.0,
            notes=(
                "Distributed as 21 multi-part split zips (Task_1.zip.001-014 "
                "+ Task_2.zip.001-007, ~21.8 GB). After download, reassemble "
                "with `cat Task_1.zip.* > Task_1.zip` then extract with 7-Zip. "
                "The Zenodo files are marked CC BY 4.0. Check any separate "
                "challenge rules before entering a competition."
            ),
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        download_zenodo(
            self._ZENODO_RECORD,
            Path(data_dir) / self._SUBDIR,
            extract=False,  # split zips need manual reassembly
        )


# ===========================================================================
# Multimodal
# ===========================================================================


class MultiEYEDataset(_StubLoadMixin, EyeDataHubDataset):
    """MultiEYE: paired fundus + OCT multi-disease benchmark (IEEE TMI 2025)."""

    _SUBDIR = "multieye"
    _HF_REPO = "Luxuriant16/MultiEYE"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="multieye",
            full_name="MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark",
            description=(
                "58,036 fundus + 45,923 OCT images assembled for multi-disease "
                "classification (8 classes) with cross-modal distillation. "
                "Sourced from multiple public ophthalmic datasets."
            ),
            modality="multimodal",
            tasks=["classification"],
            num_samples=58036,
            splits=["train", "val", "test"],
            num_classes=8,
            download_type="huggingface",
            download_url="https://huggingface.co/datasets/Luxuriant16/MultiEYE",
            license="MIT",
            citation=(
                "MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark, IEEE TMI "
                "2025; arXiv:2412.09402"
            ),
            tags=["multimodal", "fundus", "oct", "cross_modal", "distillation"],
            size_gb=27.3,
            notes=(
                "Re-aggregates several source datasets — image licenses inherit "
                "from their original sources. Verify per-component before reuse."
            ),
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        download_huggingface(
            self._HF_REPO,
            Path(data_dir) / self._SUBDIR,
            repo_type="dataset",
        )


# (dr_multimodal_tang dropped — duplicate of mmrdr in fundus_dr.py.
#  Both point to Figshare article 29423747.)


# ===========================================================================
# UWF fundus
# ===========================================================================


class UWFZhejiangDataset(_StubLoadMixin, EyeDataHubDataset):
    """Open UWF fundus dataset w/ disease + quality labels (Sci. Data 2024)."""

    _SUBDIR = "uwf_zhejiang"
    _FIGSHARE_ID = "26936446"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="uwf_zhejiang",
            full_name="Open UWF Fundus Dataset with Disease + Quality Labels",
            description=(
                "700 Optos ultra-wide-field fundus images with multi-disease "
                "classification labels and image-quality flags from real-world "
                "clinical practice."
            ),
            modality="uwf_fundus",
            tasks=["classification", "quality"],
            num_samples=700,
            splits=["all"],
            download_type="figshare",
            download_url="https://doi.org/10.6084/m9.figshare.26936446",
            license="CC BY 4.0",
            citation=(
                "He S, Ye X, Xie W, et al., 'Open ultrawidefield fundus "
                "image dataset with disease diagnosis and clinical image "
                "quality assessment', Scientific Data 11:1251, 2024. "
                "doi:10.1038/s41597-024-04113-2"
            ),
            tags=["uwf", "fundus", "quality", "multi_disease"],
            size_gb=2.0,
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        download_figshare(self._FIGSHARE_ID, Path(data_dir) / self._SUBDIR)


class UWFDRPengDataset(_StubLoadMixin, EyeDataHubDataset):
    """UWF Fundus DR Dataset (Peng et al., Sci. Data 2026)."""

    _SUBDIR = "uwf_dr_peng"
    _FIGSHARE_ID = "31259494"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="uwf_dr_peng",
            full_name="UWF Fundus DR Dataset (Peng et al., 2026)",
            description=(
                "1,630 Optos ultra-wide-field fundus images from 809 patients "
                "graded for diabetic retinopathy (5-class ICDR) by senior "
                "ophthalmologists."
            ),
            modality="uwf_fundus",
            tasks=["grading", "classification"],
            num_samples=1630,
            splits=["all"],
            num_classes=5,
            classes=["0_no_dr", "1_mild", "2_moderate", "3_severe", "4_proliferative"],
            download_type="figshare",
            download_url="https://doi.org/10.6084/m9.figshare.31259494",
            license="CC BY 4.0",
            citation=(
                "Peng et al., 'A UWF fundus DR dataset with senior-ophthalmologist "
                "labels', Scientific Data 2026. doi:10.1038/s41597-026-07093-7"
            ),
            tags=["uwf", "fundus", "dr", "grading"],
            size_gb=3.0,
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        download_figshare(self._FIGSHARE_ID, Path(data_dir) / self._SUBDIR)


# ===========================================================================
# Pediatric / ROP
# ===========================================================================


class ROPOstravaDataset(_StubLoadMixin, EyeDataHubDataset):
    """Retinal Image Dataset of Infants and ROP (Ostrava, Sci. Data 2024)."""

    _SUBDIR = "rop_ostrava"
    _KAGGLE_SLUG = "jananowakova/retinal-image-dataset-of-infants-and-rop"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="rop_ostrava",
            full_name="Retinal Image Dataset of Infants and ROP (Ostrava)",
            description=(
                "6,004 pediatric RetCam fundus images from 188 newborns in "
                "Ostrava (Czech Republic), annotated for retinopathy of "
                "prematurity (ROP) screening + classification."
            ),
            modality="fundus",
            tasks=["classification"],
            num_samples=6004,
            splits=["all"],
            download_type="kaggle",
            download_url=f"https://www.kaggle.com/datasets/{self._KAGGLE_SLUG}",
            license="CC BY 4.0",
            citation=(
                "Timkovic et al., 'Retinal Image Dataset of Infants and ROP', "
                "Scientific Data 2024. doi:10.1038/s41597-024-03409-7"
            ),
            tags=["fundus", "pediatric", "rop", "retcam", "european_cohort"],
            size_gb=5.0,
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        download_kaggle(self._KAGGLE_SLUG, Path(data_dir) / self._SUBDIR)


class ROPUWFIntelligentDataset(_StubLoadMixin, EyeDataHubDataset):
    """Fundus dataset for intelligent ROP system (Zhao 2024, Sci. Data)."""

    _SUBDIR = "rop_uwf_intelligent"
    _FIGSHARE_ID = "25514449"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="rop_uwf_intelligent",
            full_name="Fundus Dataset for Intelligent ROP System",
            description=(
                "1,099 pediatric fundus images from 483 premature infants "
                "annotated for retinopathy of prematurity (ROP) staging. "
                "Standard fundus (RetCam) — not ultra-widefield; "
                "`rop_uwf_intelligent` is retained as the registry identifier."
            ),
            modality="fundus",
            tasks=["grading", "classification"],
            num_samples=1099,
            splits=["all"],
            download_type="figshare",
            download_url="https://doi.org/10.6084/m9.figshare.25514449",
            license="CC BY 4.0",
            citation=(
                "Zhao X, Chen S, Zhang S, et al., 'A fundus image dataset for "
                "intelligent retinopathy of prematurity system', Scientific "
                "Data 11:543, 2024. doi:10.1038/s41597-024-03362-5"
            ),
            tags=["fundus", "pediatric", "rop", "stage"],
            size_gb=4.0,
            notes=(
                "Slug says `uwf` but the paper describes standard RetCam "
                "fundus imaging, not ultra-widefield. 1,099 images from 483 "
                "infants — earlier metadata claimed ~5,000."
            ),
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        download_figshare(self._FIGSHARE_ID, Path(data_dir) / self._SUBDIR)


# ===========================================================================
# Surgical / pre-op
# ===========================================================================


class FOVEADataset(_StubLoadMixin, EyeDataHubDataset):
    """FOVEA: pre/intra-operative fundus + biomicroscopy (Sci. Data 2025)."""

    _SUBDIR = "fovea"
    _FIGSHARE_ID = "28329338"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="fovea",
            full_name="FOVEA: Pre/Intra-Operative Fundus + Biomicroscopy",
            description=(
                "40 patients with paired pre-operative fundus images and "
                "intra-operative biomicroscopy video clips. Annotated for "
                "optic disc and vessel segmentation across domains."
            ),
            modality="multimodal",
            tasks=["segmentation"],
            num_samples=40,
            splits=["all"],
            download_type="figshare",
            download_url="https://doi.org/10.6084/m9.figshare.28329338",
            license="CC BY 4.0",
            citation=(
                "Ravasio et al., 'FOVEA: paired pre- and intra-operative "
                "fundus + biomicroscopy', Scientific Data 2025. "
                "doi:10.1038/s41597-025-04965-2"
            ),
            tags=["multimodal", "surgery", "fundus", "biomicroscopy", "vessel", "optic_disc"],
            size_gb=4.0,
            notes="Unique pre-op/intra-op paired modality — only public example.",
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        download_figshare(self._FIGSHARE_ID, Path(data_dir) / self._SUBDIR)


# ===========================================================================
# Vessel / artery-vein
# ===========================================================================


class FundusAVSegDataset(_StubLoadMixin, EyeDataHubDataset):
    """Fundus-AVSeg: pixel-wise artery/vein/crossing segmentation (Sci. Data 2025)."""

    _SUBDIR = "fundus_avseg"
    _FIGSHARE_ID = "27938034"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="fundus_avseg",
            full_name="Fundus-AVSeg: Artery-Vein-Crossing Segmentation",
            description=(
                "100 high-resolution color fundus images with pixel-wise "
                "artery / vein / crossing labels from a mixed disease cohort."
            ),
            modality="fundus",
            tasks=["segmentation"],
            num_samples=100,
            splits=["all"],
            num_classes=4,
            classes=["background", "artery", "vein", "crossing"],
            download_type="figshare",
            download_url="https://doi.org/10.6084/m9.figshare.27938034",
            license="CC BY 4.0",
            citation=(
                "Fundus-AVSeg dataset, Figshare project 229986 (2025). "
                "Companion paper: Basit & Alam, 'AVSeg-XAI', BioData Mining, "
                "doi:10.1186/s13040-026-00573-x (2026). Sci. Data DOI "
                "10.1038/s41597-025-05381-2 was the paper venue at time "
                "of indexing — verify at final publication."
            ),
            tags=["fundus", "vessel", "artery", "vein", "crossing", "segmentation"],
            size_gb=0.5,
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        download_figshare(self._FIGSHARE_ID, Path(data_dir) / self._SUBDIR)


# ===========================================================================
# Myopia
# ===========================================================================


class HPMIDataset(_StubLoadMixin, EyeDataHubDataset):
    """HPMI: High & Pathological Myopia identification fundus (Figshare 2024)."""

    _SUBDIR = "hpmi"
    _FIGSHARE_ID = "24800232"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="hpmi",
            full_name="HPMI: High & Pathological Myopia Identification",
            description=(
                "4,011 color fundus images labeled for high-myopia vs "
                "pathological-myopia classification — largest public dataset "
                "for HM/PM separation."
            ),
            modality="fundus",
            tasks=["classification"],
            num_samples=4011,
            splits=["all"],
            num_classes=2,
            classes=["high_myopia", "pathological_myopia"],
            download_type="figshare",
            download_url="https://doi.org/10.6084/m9.figshare.24800232",
            license="CC BY 4.0",
            citation=(
                "Huang et al., 'HPMI: A retinal fundus image dataset for "
                "identification of high and pathological myopia based on deep "
                "learning', Figshare 2024. doi:10.6084/m9.figshare.24800232"
            ),
            tags=["fundus", "myopia", "high_myopia", "pathological_myopia"],
            size_gb=2.0,
            notes="Complements EyeDataHub's PALM (pathological-myopia challenge).",
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        download_figshare(self._FIGSHARE_ID, Path(data_dir) / self._SUBDIR)


# ===========================================================================
# Cataract / reports
# ===========================================================================


class CSDIDataset(_StubLoadMixin, EyeDataHubDataset):
    """CSDI: Cataract Severity Diagnostic Image dataset (Sci. Data 2026)."""

    _SUBDIR = "csdi"
    _HF_REPO = "RainyNight/CSDI"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="csdi",
            full_name="CSDI: Cataract Severity Diagnostic Image Dataset",
            description=(
                "187 cataract cases with color fundus images and paired "
                "professional cataract-grading diagnostic reports. Designed "
                "for medical multimodal-LLM evaluation."
            ),
            modality="fundus",
            tasks=["grading", "classification"],
            num_samples=187,
            splits=["all"],
            download_type="huggingface",
            download_url="https://huggingface.co/datasets/RainyNight/CSDI",
            license="CC BY 4.0",
            citation="Scientific Data 2026. doi:10.1038/s41597-026-06684-8",
            tags=["fundus", "cataract", "severity", "report_generation", "mllm"],
            size_gb=1.0,
            notes=(
                "First public fundus dataset with paired professional cataract "
                "reports. Canonical Hugging Face repository: RainyNight/CSDI."
            ),
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        download_huggingface(
            self._HF_REPO,
            Path(data_dir) / self._SUBDIR,
            repo_type="dataset",
        )


# ===========================================================================
# Anterior segment / slit lamp
# ===========================================================================


class SLIDDataset(_StubLoadMixin, EyeDataHubDataset):
    """SLID: Slit-Lamp Image Dataset (Frontiers Digital Health 2025)."""

    _SUBDIR = "slid"
    _ZIP_URL = "https://github.com/xumingyu-hub/SLID/raw/main/Original_Slit-lamp_Images.zip"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="slid",
            full_name="SLID: Slit-Lamp Image Dataset",
            description=(
                "~2,617 annotated slit-lamp frames covering anterior-segment "
                "anatomy + multi-lesion detection (cataract, corneal disease, "
                "conjunctivitis)."
            ),
            modality="multimodal",  # slit-lamp not yet a first-class modality
            tasks=["segmentation", "classification"],
            num_samples=2617,
            splits=["all"],
            download_type="direct",
            download_url="https://github.com/xumingyu-hub/SLID",
            license="See repo (no LICENSE file as of 2026-06; assume research-only)",
            citation=(
                "Xu et al., 'SLID: Slit-Lamp Image Dataset', Frontiers Digital "
                "Health 2025. doi:10.3389/fdgth.2025.1716501"
            ),
            tags=["slit_lamp", "anterior_segment", "cornea", "cataract"],
            size_gb=1.0,
            notes=(
                "Modality EyeDataHub otherwise lacks (slit-lamp anterior-segment). "
                "Annotations CSV is at github.com/xumingyu-hub/SLID/raw/main/Annotations.csv."
            ),
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        dest = Path(data_dir) / self._SUBDIR
        dest.mkdir(parents=True, exist_ok=True)
        archive = dest / "Original_Slit-lamp_Images.zip"
        download_file(self._ZIP_URL, archive, desc="SLID images")
        try:
            extract_archive(archive, dest)
            archive.unlink(missing_ok=True)
        except Exception:
            pass
        # Annotations CSV ships separately in the same repo
        ann_url = "https://github.com/xumingyu-hub/SLID/raw/main/Annotations.csv"
        download_file(ann_url, dest / "Annotations.csv", desc="SLID annotations")


# ===========================================================================
# Vision-Language / VQA
# ===========================================================================


class Eyecare100KDataset(_StubLoadMixin, EyeDataHubDataset):
    """Eyecare-100K VQA: 102K VQA pairs from 58,485 images across 8 ophthalmic
    modalities (FA/ICGA/OCT/CFP/UBM/slit-lamp/FSI/CT). ACM MM 2025.

    NOTE: As of June 2026 the dataset is not yet publicly released; the
    EyecareGPT GitHub README marks it 'Dataset — Coming Soon'. download()
    will fail until upstream publishes."""

    _SUBDIR = "eyecare_100k"
    _HF_REPO = "DCDM/EyecareGPT"  # to-be-published

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="eyecare_100k",
            full_name="Eyecare-100K: Multimodal Ophthalmology VQA Corpus",
            description=(
                "~102K VQA pairs derived from 58,485 images across 8 ophthalmic "
                "modalities (fluorescein angiography, ICGA, OCT, CFP, "
                "ultrasound biomicroscopy, slit-lamp, fundus auto-fluorescence, "
                "CT) covering 100+ diseases."
            ),
            modality="multimodal",
            tasks=["classification"],  # extended to VQA in practice
            num_samples=102000,
            splits=["train", "val", "test"],
            download_type="huggingface",
            download_url="https://github.com/DCDmllm/EyecareGPT",
            license="Mixed (inherits source-dataset licenses) — needs per-row check",
            citation=(
                "EyecareGPT: arXiv 2504.13650; ACM MM 2025. "
                "github.com/DCDmllm/EyecareGPT"
            ),
            tags=["vqa", "vlm", "multimodal", "fa", "icga", "ubm", "slit_lamp", "fundus"],
            size_gb=30.0,
            notes=(
                "Status: PENDING RELEASE. Largest open ophthalmology VQA "
                "corpus when published. EyecareGPT models are out (LLSuzy/* on "
                "HF) but the VQA dataset itself is not yet public as of 2026-06."
            ),
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        try:
            download_huggingface(
                self._HF_REPO,
                Path(data_dir) / self._SUBDIR,
                repo_type="dataset",
            )
        except Exception:
            print_manual_download_instructions(
                "Eyecare-100K", self.info.download_url,
                Path(data_dir) / self._SUBDIR,
                extra_notes=(
                    "Dataset is not yet publicly released as of June 2026. "
                    "Watch github.com/DCDmllm/EyecareGPT for the release "
                    "announcement, then re-run `eyehub download eyecare_100k`."
                ),
            )
            raise
