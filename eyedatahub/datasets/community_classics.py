"""Classic community-standard ophthalmic datasets.

These are widely-used pre-2024 datasets that appear in two or more of the
community catalogs (openmedlab/Awesome-Medical-Dataset, FLAIR, MIRAGE,
EyecareGPT, IRFundusSet, Khan et al. 2021 Lancet review,
m-aryayi/Medical-Imaging-Datasets, TheBeastCoding/glaucoma-dataset-metadata,
FDU-VTS/Awesome-Diabetic-Retinopathy-Detection) but were not yet in
EyeDataHub.

Each entry carries verified DatasetInfo + a machine-actionable download
backend wherever the upstream permits. Where the upstream is form-gated,
NDA-protected, or paywalled (IEEE DataPort login, Iowa Qualtrics, Grand
Challenge DUA), the loader prints explicit instructions and raises —
EyeDataHub cannot bypass institutional access controls.

`load()` is a stub on `_StubLoadMixin` from `community_recent.py` —
concrete parsers welcome PR.
"""
from __future__ import annotations

from pathlib import Path
from typing import Union

from eyedatahub.core.dataset import DatasetInfo, EyeDataHubDataset
from eyedatahub.datasets.community_recent import _StubLoadMixin
from eyedatahub.datasets.download_utils import (
    download_figshare,
    download_file,
    download_kaggle,
    download_mendeley,
    download_physionet,
    download_zenodo,
    extract_archive,
    print_manual_download_instructions,
)


# ===========================================================================
# Classic DR benchmarks
# ===========================================================================


class Messidor1Dataset(_StubLoadMixin, EyeDataHubDataset):
    """MESSIDOR (original release, 2014). 1,200 fundus images with DR
    grading + risk-of-macular-edema labels. ADCIS withdrew M1 in 2018;
    EyeDataHub's `messidor2` is the maintained successor."""

    _SUBDIR = "messidor1"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="messidor1",
            full_name="MESSIDOR (Original)",
            description=(
                "1,200 color fundus images with diabetic retinopathy grade "
                "(0-3) and risk-of-macular-edema labels (0-2). Original "
                "MESSIDOR — successor MESSIDOR-2 already in EyeDataHub as "
                "`messidor2`."
            ),
            modality="fundus",
            tasks=["grading", "classification"],
            num_samples=1200,
            splits=["all"],
            num_classes=4,
            classes=["0_no_dr", "1_mild", "2_moderate", "3_severe"],
            download_type="manual",
            download_url="https://www.adcis.net/en/third-party/messidor/",
            license="Research only (free with registration; withdrawn 2018)",
            citation=(
                "Decencière et al., 'Feedback on a Publicly Distributed Image "
                "Database: The Messidor Database', Image Anal Stereol 2014."
            ),
            tags=["fundus", "dr", "grading", "macular_edema", "classical", "deprecated"],
            size_gb=3.0,
            notes=(
                "DEPRECATED: ADCIS withdrew MESSIDOR-1 in 2018. Use "
                "`messidor2` (already in EyeDataHub) instead. Kept for "
                "reproducing pre-2018 benchmark papers."
            ),
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        print_manual_download_instructions(
            "MESSIDOR-1", self.info.download_url,
            Path(data_dir) / self._SUBDIR,
            extra_notes=(
                "ADCIS no longer distributes MESSIDOR-1 (withdrawn 2018).\n"
                "EyeDataHub already indexes MESSIDOR-2 — prefer that.\n"
                "Pre-2018 mirrors may exist on academic archives."
            ),
        )
        raise RuntimeError("MESSIDOR-1 has been withdrawn from official distribution.")


class EOphthaDataset(_StubLoadMixin, EyeDataHubDataset):
    """E-ophtha: exudate + microaneurysm segmentation (Decencière 2013).
    Official ADCIS site is form-gated; we use the Kaggle community mirror."""

    _SUBDIR = "e_ophtha"
    _KAGGLE_SLUG = "samriddhibagchi/e-ophtha-diabetic-retinopathy-datasets-ex-ma"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="e_ophtha",
            full_name="E-ophtha (EX + MA): Exudate and Microaneurysm Segmentation",
            description=(
                "463 color fundus images with pixel-level segmentation: "
                "82 with exudate (EX) + 381 with microaneurysm (MA) annotations. "
                "Standard DR lesion-segmentation benchmark."
            ),
            modality="fundus",
            tasks=["segmentation"],
            num_samples=463,
            splits=["all"],
            num_classes=2,
            download_type="kaggle",
            download_url="https://www.kaggle.com/datasets/samriddhibagchi/e-ophtha-diabetic-retinopathy-datasets-ex-ma",
            license="Research only (TeleOphta project; Kaggle mirror)",
            citation=(
                "Decencière et al., 'TeleOphta: Machine Learning and Image "
                "Processing Methods for Teleophthalmology', IRBM 2013."
            ),
            tags=["fundus", "dr", "exudate", "microaneurysm", "segmentation"],
            size_gb=1.0,
            notes=(
                "Official source (ADCIS) requires a request form. EyeDataHub "
                "uses the Kaggle community mirror. Verify license terms "
                "with the original ADCIS distribution before commercial use."
            ),
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        download_kaggle(self._KAGGLE_SLUG, Path(data_dir) / self._SUBDIR)


class ROCDataset(_StubLoadMixin, EyeDataHubDataset):
    """ROC: Retinopathy Online Challenge — microaneurysm detection."""

    _SUBDIR = "roc"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="roc",
            full_name="ROC: Retinopathy Online Challenge",
            description=(
                "100 fundus images with microaneurysm annotations from the "
                "Retinopathy Online Challenge."
            ),
            modality="fundus",
            tasks=["segmentation", "classification"],
            num_samples=100,
            splits=["train", "test"],
            num_classes=2,
            download_type="manual",
            download_url="http://webeye.ophth.uiowa.edu/ROC/",
            license="Research only (free for research, University of Iowa)",
            citation=(
                "Niemeijer et al., 'Retinopathy Online Challenge: Automatic "
                "Detection of Microaneurysms in Digital Color Fundus "
                "Photographs', IEEE TMI 2010."
            ),
            tags=["fundus", "dr", "microaneurysm", "detection", "classical"],
            size_gb=0.3,
            notes="University of Iowa registration form required — no auto path.",
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        print_manual_download_instructions(
            "ROC", self.info.download_url,
            Path(data_dir) / self._SUBDIR,
            extra_notes="University of Iowa request form.",
        )
        raise RuntimeError("ROC requires University of Iowa registration.")


# ===========================================================================
# Optic disc / vessel
# ===========================================================================


class DRIONSDBDataset(_StubLoadMixin, EyeDataHubDataset):
    """DRIONS-DB: optic nerve head / optic disc segmentation."""

    _SUBDIR = "drions_db"
    _RAR_URL = "http://www.ia.uned.es/~ejcarmona/DRIONS-DB/BD/DRIONS-DB.rar"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="drions_db",
            full_name="DRIONS-DB: Digital Retinal Images for Optic Nerve Segmentation",
            description=(
                "110 color fundus images with optic-disc contour annotations "
                "by two experts. Foundational OD-segmentation dataset."
            ),
            modality="fundus",
            tasks=["segmentation"],
            num_samples=110,
            splits=["all"],
            num_classes=2,
            classes=["background", "optic_disc"],
            download_type="direct",
            download_url="https://www.ia.uned.es/~ejcarmona/DRIONS-DB.html",
            license="Research only (UNED public release)",
            citation=(
                "Carmona et al., 'Identification of the Optic Nerve Head with "
                "Genetic Algorithms', Artificial Intelligence in Medicine 2008."
            ),
            tags=["fundus", "optic_disc", "segmentation", "classical"],
            size_gb=0.2,
            notes=(
                "UNED host serves an expired SSL certificate as of 2026-07. "
                "EyeDataHub falls back to an unverified HTTPS request; set "
                "PYTHONHTTPSVERIFY=0 in your environment if requests still "
                "fails cert validation. Distributed as .rar — needs `unrar` "
                "(Linux: `apt install unrar`; macOS: `brew install rar`; "
                "Windows: 7-Zip)."
            ),
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        dest = Path(data_dir) / self._SUBDIR
        dest.mkdir(parents=True, exist_ok=True)
        archive = dest / "DRIONS-DB.rar"
        try:
            download_file(self._RAR_URL, archive, desc="DRIONS-DB")
        except Exception as e:
            print(
                f"\nDRIONS-DB failed ({e}). UNED host has an expired SSL cert. "
                f"Retry with PYTHONHTTPSVERIFY=0 or download manually from "
                f"{self.info.download_url}.\n"
            )
            raise
        # .rar extraction is intentionally NOT attempted here — the standard
        # library cannot decode it. Tell the user instead.
        print(
            f"DRIONS-DB downloaded to {archive}. Extract manually with `unrar "
            f"x DRIONS-DB.rar` or 7-Zip."
        )


class RITEDataset(_StubLoadMixin, EyeDataHubDataset):
    """RITE: Retinal Images vessel Tree Extraction — A/V classification."""

    _SUBDIR = "rite"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="rite",
            full_name="RITE: Retinal Images Vessel Tree Extraction (Artery/Vein)",
            description=(
                "40 fundus images (derived from DRIVE) with artery/vein "
                "annotations and vessel-tree structural labels."
            ),
            modality="fundus",
            tasks=["segmentation"],
            num_samples=40,
            splits=["train", "test"],
            num_classes=4,
            classes=["background", "artery", "vein", "unknown_vessel"],
            download_type="manual",
            download_url="https://eye.medicine.uiowa.edu/rite-dataset",
            license="Research only (Iowa Qualtrics request form)",
            citation=(
                "Hu et al., 'Automated Separation of Binary Overlapping Trees "
                "in Low-Contrast Color Retinal Images', MICCAI 2013."
            ),
            tags=["fundus", "vessel", "artery", "vein", "av_classification"],
            size_gb=0.1,
            notes="Iowa Qualtrics form gates download — no auto path.",
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        print_manual_download_instructions(
            "RITE", self.info.download_url,
            Path(data_dir) / self._SUBDIR,
            extra_notes=(
                "Iowa Qualtrics form: "
                "https://uiowa.qualtrics.com/SE/?SID=SV_a3mc5H4SG2B3e2p"
            ),
        )
        raise RuntimeError("RITE requires the Iowa Qualtrics request form.")


class FIREDataset(_StubLoadMixin, EyeDataHubDataset):
    """FIRE: Fundus Image Registration benchmark."""

    _SUBDIR = "fire"
    _SEVENZ_URL = "https://projects.ics.forth.gr/cvrl/fire/FIRE.7z"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="fire",
            full_name="FIRE: Fundus Image Registration Dataset",
            description=(
                "129 fundus images from 39 patients forming 134 registration "
                "pairs with anatomical ground-truth control points. Only "
                "public registration benchmark for ophthalmology."
            ),
            modality="fundus",
            tasks=["regression"],
            num_samples=129,
            splits=["all"],
            download_type="direct",
            download_url="https://projects.ics.forth.gr/cvrl/fire/",
            license="Research only (FORTH CVRL)",
            citation=(
                "Hernandez-Matas et al., 'FIRE: Fundus Image Registration "
                "Dataset', Journal of Modeling in Ophthalmology 2017."
            ),
            tags=["fundus", "registration", "image_pairs", "classical"],
            size_gb=1.0,
            notes=(
                "Distributed as a 7z archive. EyeDataHub validates archive "
                "member paths before extracting it."
            ),
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        dest = Path(data_dir) / self._SUBDIR
        dest.mkdir(parents=True, exist_ok=True)
        archive = dest / "FIRE.7z"
        download_file(self._SEVENZ_URL, archive, desc="FIRE")
        extract_archive(archive, dest)
        archive.unlink(missing_ok=True)


# ===========================================================================
# Glaucoma — additional benchmarks
# ===========================================================================


class RIGADataset(_StubLoadMixin, EyeDataHubDataset):
    """RIGA: multi-annotator OD/OC segmentation."""

    _SUBDIR = "riga"
    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="riga",
            full_name="RIGA: Retinal Fundus Images for Glaucoma Analysis",
            description=(
                "750 fundus images with optic disc and optic cup segmentations "
                "from 6 ophthalmologists per image. Multi-rater benchmark."
            ),
            modality="fundus",
            tasks=["segmentation"],
            num_samples=750,
            splits=["all"],
            num_classes=3,
            classes=["background", "optic_disc", "optic_cup"],
            download_type="direct",
            download_url="https://deepblue.lib.umich.edu/data/concern/data_sets/3b591905z",
            license="CC BY-NC 4.0",
            citation=(
                "Almazroa et al., 'Retinal Fundus Images for Glaucoma "
                "Analysis: The RIGA Dataset', J. Medical Imaging 2018."
            ),
            tags=["fundus", "glaucoma", "optic_disc", "optic_cup", "multi_rater"],
            size_gb=2.0,
            notes=(
                "Deep Blue provides BinRushed, Magrabi, and MESSIDOR "
                "components. Its current documentation directs users to "
                "Globus for the large MESSIDOR component."
            ),
            acquisition_support="guided_instructions_only",
            loader_live_tested=False,
            loader_test_scope="official_instructions_checked",
            loader_test_result="automation_not_supported",
            failure_reason=(
                "The current official Deep Blue workflow is not supported "
                "end to end by the EyeDataHub downloader."
            ),
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        dest = Path(data_dir) / self._SUBDIR
        print_manual_download_instructions(
            "RIGA",
            self.info.download_url,
            dest,
            extra_notes=(
                "Download the BinRushed and Magrabi components from Deep Blue. "
                "Use the official Globus route for MESSIDOR, as directed by "
                "the source documentation."
            ),
        )
        raise RuntimeError(
            "RIGA currently uses the official Deep Blue/Globus instructions; "
            "automatic transfer is not implemented."
        )


class LAGDataset(_StubLoadMixin, EyeDataHubDataset):
    """LAG: Large-scale Attention-based Glaucoma dataset (Li 2019 CVPR).
    Dropbox link password-gated via email."""

    _SUBDIR = "lag"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="lag",
            full_name="LAG: Large-scale Attention-based Glaucoma Database",
            description=(
                "11,760 fundus images with glaucoma classification labels and "
                "ophthalmologist-derived attention maps. Largest public "
                "glaucoma dataset with attention ground truth."
            ),
            modality="fundus",
            tasks=["classification", "segmentation"],
            num_samples=11760,
            splits=["train", "test"],
            num_classes=2,
            classes=["normal", "glaucoma"],
            download_type="manual",
            download_url="https://github.com/smilell/AG-CNN",
            license="Research only (no redistribution; password by email)",
            citation=(
                "Li et al., 'Attention Based Glaucoma Detection: A Large-scale "
                "Database and CNN Model', CVPR 2019."
            ),
            tags=["fundus", "glaucoma", "attention", "large_scale"],
            size_gb=3.0,
            notes=(
                "Dropbox link gated by password — email liliu1995@buaa.edu.cn "
                "to request access. Cannot be auto-downloaded."
            ),
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        print_manual_download_instructions(
            "LAG", self.info.download_url,
            Path(data_dir) / self._SUBDIR,
            extra_notes=(
                "Email liliu1995@buaa.edu.cn for Dropbox password.\n"
                "Repository README lists current instructions."
            ),
        )
        raise RuntimeError("LAG requires email-based password request.")


class ChaksuDataset(_StubLoadMixin, EyeDataHubDataset):
    """CHAKSU: multi-device glaucoma dataset (Kumar 2023 Sci Data)."""

    _SUBDIR = "chaksu"
    _FIGSHARE_ID = "20123135"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="chaksu",
            full_name="CHAKSU: Multi-Device Glaucoma Fundus Dataset",
            description=(
                "1,345 fundus images captured across multiple camera "
                "manufacturers with OD/OC segmentation + glaucoma "
                "classification labels."
            ),
            modality="fundus",
            tasks=["classification", "segmentation"],
            num_samples=1345,
            splits=["all"],
            num_classes=3,
            classes=["background", "optic_disc", "optic_cup"],
            download_type="figshare",
            download_url="https://doi.org/10.6084/m9.figshare.20123135",
            license="CC BY 4.0",
            citation=(
                "Kumar et al., 'CHAKSU: A glaucoma-specific fundus image "
                "database', Scientific Data 2023."
            ),
            tags=["fundus", "glaucoma", "multi_device", "optic_disc"],
            size_gb=5.0,
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        download_figshare(self._FIGSHARE_ID, Path(data_dir) / self._SUBDIR)


class HYGDDataset(_StubLoadMixin, EyeDataHubDataset):
    """HYGD: Hillel Yaffe Glaucoma Dataset (PhysioNet 2024, open-access)."""

    _SUBDIR = "hygd"
    _PHYSIONET_SLUG = "hillel-yaffe-glaucoma-dataset"
    _VERSION = "1.1.0"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="hygd",
            full_name="HYGD: Hillel Yaffe Glaucoma Dataset",
            description=(
                "747 fundus images from 288 patients with glaucoma labels "
                "confirmed by paired OCT + visual field. First public dataset "
                "with gold-standard multimodal glaucoma confirmation."
            ),
            modality="fundus",
            tasks=["classification"],
            num_samples=747,
            splits=["all"],
            num_classes=2,
            classes=["non_glaucoma", "glaucoma"],
            download_type="physionet",
            download_url="https://doi.org/10.13026/pdxv-m215",
            license="ODC-BY 1.0 (Open Data Commons Attribution)",
            citation=(
                "Hillel Yaffe Glaucoma Dataset, PhysioNet 2024 (v1.1.0). "
                "Labels gold-standardized via OCT + visual field. "
                "doi:10.13026/pdxv-m215"
            ),
            tags=["fundus", "glaucoma", "multimodal_confirmed", "physionet"],
            size_gb=1.0,
            notes=(
                "Open-access (ODC-BY) — no PhysioNet credentialing required."
            ),
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        download_physionet(
            self._PHYSIONET_SLUG,
            self._VERSION,
            Path(data_dir) / self._SUBDIR,
            credentialed=False,  # open-access
        )


class SMDGDataset(_StubLoadMixin, EyeDataHubDataset):
    """SMDG-19: Standardized Multi-channel Dataset for Glaucoma (CC0)."""

    _SUBDIR = "smdg"
    _KAGGLE_SLUG = "deathtrooper/multichannel-glaucoma-benchmark-dataset"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="smdg",
            full_name="SMDG-19: Standardized Multi-channel Glaucoma Benchmark",
            description=(
                "~12,000 fundus images aggregated from 19 public glaucoma "
                "datasets with standardized disc/cup/vessel channels and "
                "unified labels. CC0 — fully public domain."
            ),
            modality="fundus",
            tasks=["classification", "segmentation"],
            num_samples=12449,
            splits=["train", "val", "test"],
            num_classes=3,
            classes=["non_glaucoma", "glaucoma", "suspect"],
            download_type="kaggle",
            download_url="https://www.kaggle.com/datasets/deathtrooper/multichannel-glaucoma-benchmark-dataset",
            license="CC0 1.0 (Public Domain)",
            citation=(
                "Kiefer, 'Standardized Multi-channel Dataset for Glaucoma "
                "(SMDG-19)', Kaggle 2022. Breakdown: 7,499 non-glaucoma + "
                "4,817 glaucoma + 133 suspect."
            ),
            tags=["fundus", "glaucoma", "aggregator", "multi_channel"],
            size_gb=5.0,
            notes=(
                "Aggregator — overlaps with several EyeDataHub-indexed glaucoma "
                "datasets. Useful for unified multi-source training."
            ),
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        download_kaggle(self._KAGGLE_SLUG, Path(data_dir) / self._SUBDIR)


# ===========================================================================
# Multi-label / multi-disease (additional)
# ===========================================================================


class MuReDDataset(_StubLoadMixin, EyeDataHubDataset):
    """MuReD: 20-class Multi-label Retinal Diseases (Rodriguez 2022 CIBM)."""

    _SUBDIR = "mured"
    _MENDELEY_ID = "pc4mb3h8hz"
    _VERSION = 1

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="mured",
            full_name="MuReD: Multi-label Retinal Diseases Dataset",
            description=(
                "2,208 color fundus images with 20-class multi-label disease "
                "annotations."
            ),
            modality="fundus",
            tasks=["multilabel", "classification"],
            num_samples=2208,
            splits=["train", "test"],
            num_classes=20,
            download_type="mendeley",
            download_url="https://data.mendeley.com/datasets/pc4mb3h8hz/1",
            license="CC BY 4.0",
            citation=(
                "Rodriguez MA, AlMarzouqi H, Liatsis P, 'Multi-label Retinal "
                "Disease Classification using Transformers', IEEE Journal of "
                "Biomedical and Health Informatics 27(6):2739-2750, 2022. "
                "arXiv:2207.02335"
            ),
            tags=["fundus", "multilabel", "multi_disease"],
            size_gb=2.0,
            notes=(
                "The official source states that images from STARE, RFMiD, "
                "and ARIA were post-processed for this release. ARIA is not "
                "a separate EyeDataHub record."
            ),
            dataset_doi="10.17632/pc4mb3h8hz.1",
            canonical_resolver_url="https://doi.org/10.17632/pc4mb3h8hz.1",
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        download_mendeley(
            self._MENDELEY_ID,
            self._VERSION,
            Path(data_dir) / self._SUBDIR,
        )


class SUSTechSYSUDataset(_StubLoadMixin, EyeDataHubDataset):
    """SUSTech-SYSU: DR grading + pixel-level exudate segmentation."""

    _SUBDIR = "sustech_sysu"
    _FIGSHARE_ID = "12570770"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="sustech_sysu",
            full_name="SUSTech-SYSU Diabetic Retinopathy + Exudate Dataset",
            description=(
                "1,219 color fundus images with DR severity grading + "
                "pixel-level exudate segmentation masks. Multi-center "
                "(SUSTech + Sun Yat-sen University)."
            ),
            modality="fundus",
            tasks=["grading", "segmentation", "classification"],
            num_samples=1219,
            splits=["all"],
            num_classes=5,
            download_type="figshare",
            download_url="https://doi.org/10.6084/m9.figshare.12570770",
            license="CC BY 4.0",
            citation=(
                "Lin et al., 'The SUSTech-SYSU dataset for automated exudate "
                "detection and diabetic retinopathy grading', Scientific Data "
                "2020."
            ),
            tags=["fundus", "dr", "exudate", "segmentation", "grading"],
            size_gb=3.0,
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        download_figshare(self._FIGSHARE_ID, Path(data_dir) / self._SUBDIR)


class ParaguayDRDataset(_StubLoadMixin, EyeDataHubDataset):
    """Paraguay color fundus DR dataset — Latin American cohort."""

    _SUBDIR = "paraguay_dr"
    _ZENODO_RECORD = "4647952"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="paraguay_dr",
            full_name="Paraguay Color Fundus DR Dataset",
            description=(
                "757 color fundus images from a Paraguayan cohort with "
                "7-class DR grading labels. Adds Latin-American representation."
            ),
            modality="fundus",
            tasks=["grading", "classification"],
            num_samples=757,
            splits=["all"],
            num_classes=7,
            download_type="zenodo",
            download_url="https://zenodo.org/record/4647952",
            license="CC BY 4.0",
            citation=(
                "Castillo Benítez et al., Paraguay DR Dataset, Zenodo 2021. "
                "doi:10.5281/zenodo.4647952"
            ),
            tags=["fundus", "dr", "grading", "latin_america", "paraguay"],
            size_gb=0.5,
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        download_zenodo(self._ZENODO_RECORD, Path(data_dir) / self._SUBDIR)


class JichiDRDataset(_StubLoadMixin, EyeDataHubDataset):
    """Jichi Medical University DR dataset — Japanese cohort (Takahashi 2017)."""

    _SUBDIR = "jichi"
    _FIGSHARE_ID = "4879853"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="jichi",
            full_name="Jichi Medical University Diabetic Retinopathy Dataset",
            description=(
                "9,939 color fundus images from Japanese patients with DR "
                "grading labels (Davis grading scale)."
            ),
            modality="fundus",
            tasks=["grading", "classification"],
            num_samples=9939,
            splits=["all"],
            num_classes=4,
            download_type="figshare",
            download_url="https://doi.org/10.6084/m9.figshare.4879853",
            license="CC BY 4.0",
            citation=(
                "Takahashi et al., 'Applying artificial intelligence to "
                "disease staging: Deep learning for improved staging of "
                "diabetic retinopathy', PLOS ONE 2017. "
                "Article: https://pmc.ncbi.nlm.nih.gov/articles/PMC5480986/"
            ),
            tags=["fundus", "dr", "grading", "japan"],
            size_gb=10.0,
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        download_figshare(self._FIGSHARE_ID, Path(data_dir) / self._SUBDIR)


class DRTiDDataset(_StubLoadMixin, EyeDataHubDataset):
    """DRTiD: Diabetic Retinopathy Two-field image Dataset.
    Wenjuanxing/Google form gated."""

    _SUBDIR = "drtid"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="drtid",
            full_name="DRTiD: Diabetic Retinopathy Two-field Image Dataset",
            description=(
                "3,100 paired two-field fundus images with DR grading labels. "
                "Only public two-field paired DR benchmark."
            ),
            modality="fundus",
            tasks=["grading", "classification"],
            num_samples=3100,
            splits=["train", "test"],
            num_classes=5,
            download_type="manual",
            download_url="https://github.com/FDU-VTS/DRTiD",
            license="Research only (application form)",
            citation=(
                "Hou et al., 'Cross-Field Transformer for Diabetic "
                "Retinopathy Grading on Two-field Fundus Images', IEEE BIBM "
                "2022. arXiv:2211.14552"
            ),
            tags=["fundus", "dr", "two_field", "paired", "grading"],
            size_gb=3.0,
            notes="Wenjuanxing application form — no auto path.",
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        print_manual_download_instructions(
            "DRTiD", self.info.download_url,
            Path(data_dir) / self._SUBDIR,
            extra_notes="Fill the Wenjuanxing form linked in the GitHub README.",
        )
        raise RuntimeError("DRTiD requires Wenjuanxing application form.")


class MFIDDRDataset(_StubLoadMixin, EyeDataHubDataset):
    """MFIDDR: Multi-Field Imaging Dataset for DR — Google Form gated."""

    _SUBDIR = "mfiddr"
    _FORM_URL = (
        "https://docs.google.com/forms/d/e/1FAIpQLSdQLra-4lEtG6zrASbtPf_"
        "Dd5zyEEmQv0HMDgJPBdo97O1qPg/viewform"
    )

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="mfiddr",
            full_name="MFIDDR: Multi-Field Imaging Dataset for Diabetic Retinopathy",
            description=(
                "34,452 fundus images from 4,344 patients across multiple "
                "fields per eye, with DR screening labels. Largest public "
                "four-field DR dataset."
            ),
            modality="fundus",
            tasks=["grading", "classification", "multilabel"],
            num_samples=34452,
            splits=["train", "test"],
            num_classes=5,
            download_type="manual",
            download_url="https://github.com/mfiddr/MFIDDR",
            license="MIT (form-gated download)",
            citation="MFIDDR Multi-Field Imaging Dataset for DR. github.com/mfiddr/MFIDDR",
            tags=["fundus", "dr", "multi_field", "screening", "large_scale"],
            size_gb=30.0,
            notes="Google Form gates the Drive link — no static download ID.",
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        print_manual_download_instructions(
            "MFIDDR", self.info.download_url,
            Path(data_dir) / self._SUBDIR,
            extra_notes=f"Google Form: {self._FORM_URL}",
        )
        raise RuntimeError("MFIDDR Drive link gated by Google Form.")


# ===========================================================================
# OCT / OCTA
# ===========================================================================


class RETOUCHDataset(_StubLoadMixin, EyeDataHubDataset):
    """RETOUCH: Retinal OCT fluid challenge — Grand Challenge DUA gated."""

    _SUBDIR = "retouch"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="retouch",
            full_name="RETOUCH: RETinal OCT Fluid Challenge",
            description=(
                "112 OCT volumes from three vendors (Cirrus / Spectralis / "
                "Topcon) with pixel-level segmentation of intraretinal fluid "
                "(IRF), subretinal fluid (SRF), and pigment epithelium "
                "detachment (PED)."
            ),
            modality="oct",
            tasks=["segmentation"],
            num_samples=112,
            splits=["train", "test"],
            num_classes=4,
            classes=["background", "irf", "srf", "ped"],
            download_type="manual",
            download_url="https://retouch.grand-challenge.org/",
            license="Research only (signed DUA via Grand Challenge)",
            citation=(
                "Bogunovic et al., 'RETOUCH — The Retinal OCT Fluid Detection "
                "and Segmentation Benchmark and Challenge', IEEE TMI 2019."
            ),
            tags=["oct", "fluid_segmentation", "amd", "dme", "multi_vendor"],
            size_gb=5.0,
            notes="Grand Challenge account + signed DUA required.",
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        print_manual_download_instructions(
            "RETOUCH", self.info.download_url,
            Path(data_dir) / self._SUBDIR,
        )
        raise RuntimeError("RETOUCH requires signed DUA via Grand Challenge.")


class ROSEDataset(_StubLoadMixin, EyeDataHubDataset):
    """ROSE: Retinal OCT-Angiography vessel SEgmentation. Now on Zenodo
    (was previously form-gated on imed.nimte.ac.cn)."""

    _SUBDIR = "rose"
    _ZENODO_RECORD = "12775880"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="rose",
            full_name="ROSE: Retinal OCT-Angiography Vessel Segmentation",
            description=(
                "229 OCTA images (ROSE-1 + ROSE-2) with pixel-level retinal "
                "vessel segmentation ground truth."
            ),
            modality="octa",
            tasks=["segmentation"],
            num_samples=229,
            splits=["train", "test"],
            num_classes=2,
            classes=["background", "vessel"],
            download_type="zenodo",
            download_url="https://zenodo.org/doi/10.5281/zenodo.12775880",
            license="CC BY 4.0",
            citation=(
                "Ma et al., 'ROSE: A Retinal OCT-Angiography Vessel "
                "Segmentation Dataset and New Model', IEEE TMI 2021. "
                "Zenodo mirror: doi:10.5281/zenodo.12775880 (CC BY 4.0)."
            ),
            tags=["octa", "vessel", "segmentation"],
            size_gb=0.8,
            notes=(
                "Zenodo mirror (2024) publishes ROSE-1 + ROSE-2 under CC BY "
                "4.0 — upgraded from the previous form-gated academic-only "
                "distribution on imed.nimte.ac.cn. EyeDataHub auto-downloads "
                "from Zenodo record 12775880."
            ),
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        download_zenodo(self._ZENODO_RECORD, Path(data_dir) / self._SUBDIR)


class OCTA500Dataset(_StubLoadMixin, EyeDataHubDataset):
    """OCTA-500: largest public OCTA dataset (Li 2024 MedIA).
    IEEE DataPort password-gated."""

    _SUBDIR = "octa_500"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="octa_500",
            full_name="OCTA-500: Large-scale OCTA Multi-task Benchmark",
            description=(
                "500 subjects with OCTA volumes, vessel segmentation, FAZ "
                "(foveal avascular zone) annotations, and layer segmentation. "
                "Largest public OCTA dataset."
            ),
            modality="octa",
            tasks=["segmentation", "classification"],
            num_samples=500,
            splits=["train", "val", "test"],
            num_classes=4,
            download_type="manual",
            download_url="https://ieee-dataport.org/open-access/octa-500",
            license="IEEE DataPort Open Access (research only)",
            citation=(
                "Li et al., 'OCTA-500: A retinal dataset for optical coherence "
                "tomography angiography study', Medical Image Analysis 2024."
            ),
            tags=["octa", "vessel", "faz", "layer_segmentation", "large_scale"],
            size_gb=70.0,
            notes=(
                "IEEE login + password-protected zip — email "
                "chen2qiang@njust.edu.cn for the unlock password."
            ),
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        print_manual_download_instructions(
            "OCTA-500", self.info.download_url,
            Path(data_dir) / self._SUBDIR,
            extra_notes="Email chen2qiang@njust.edu.cn for the zip password.",
        )
        raise RuntimeError("OCTA-500 zip is password-protected.")


# ===========================================================================
# UWF / surgical / captioning
# ===========================================================================


class PrimeFP20Dataset(_StubLoadMixin, EyeDataHubDataset):
    """PRIME-FP20: UWF vessel segmentation. IEEE DataPort login-gated."""

    _SUBDIR = "prime_fp20"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="prime_fp20",
            full_name="PRIME-FP20: Ultra-Widefield Vessel Segmentation",
            description=(
                "15 ultra-widefield (Optos) fundus images with pixel-level "
                "vessel segmentation ground truth."
            ),
            modality="uwf_fundus",
            tasks=["segmentation"],
            num_samples=15,
            splits=["all"],
            num_classes=2,
            classes=["background", "vessel"],
            download_type="manual",
            download_url="https://ieee-dataport.org/open-access/prime-fp20-ultra-widefield-fundus-photography-vessel-segmentation-dataset",
            license="CC BY 4.0",
            citation=(
                "Ding et al., 'A Novel Deep Learning Pipeline for Retinal "
                "Vessel Detection in Fluorescein Angiography', IEEE TMI 2021."
            ),
            tags=["uwf", "fundus", "vessel", "segmentation"],
            size_gb=0.5,
            notes="IEEE DataPort free account login required.",
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        print_manual_download_instructions(
            "PRIME-FP20", self.info.download_url,
            Path(data_dir) / self._SUBDIR,
            extra_notes="Free IEEE account required to download.",
        )
        raise RuntimeError("PRIME-FP20 requires IEEE DataPort login.")


class CATARACTS2017Dataset(_StubLoadMixin, EyeDataHubDataset):
    """CATARACTS 2017: surgical tool detection (Al Hajj 2019 MedIA)."""

    _SUBDIR = "cataracts2017"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="cataracts2017",
            full_name="CATARACTS 2017: Surgical Tool Detection Challenge",
            description=(
                "50 cataract surgery videos (>9 hours total) with frame-level "
                "annotations of 21 surgical tools. Earlier and larger sibling "
                "to Cataract-1K."
            ),
            modality="surgical_video",
            tasks=["classification", "multilabel"],
            num_samples=50,
            splits=["train", "test"],
            num_classes=21,
            download_type="manual",
            download_url="https://ieee-dataport.org/open-access/cataracts",
            license="CC BY 4.0 (IEEE DataPort)",
            citation=(
                "Al Hajj et al., 'CATARACTS: Challenge on Automatic Tool "
                "Annotation for cataRACT Surgery', Medical Image Analysis 2019."
            ),
            tags=["surgical_video", "cataract", "tool_detection", "classical"],
            size_gb=50.0,
            notes="IEEE DataPort free account login required.",
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        print_manual_download_instructions(
            "CATARACTS 2017", self.info.download_url,
            Path(data_dir) / self._SUBDIR,
            extra_notes="Free IEEE account required to download.",
        )
        raise RuntimeError("CATARACTS 2017 requires IEEE DataPort login.")


class DeepEyeNetDataset(_StubLoadMixin, EyeDataHubDataset):
    """DeepEyeNet: fundus report-generation dataset (NDA-gated)."""

    _SUBDIR = "deepeyenet"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="deepeyenet",
            full_name="DeepEyeNet (DEN): Fundus Report Generation Dataset",
            description=(
                "15,709 fundus images with paired medical reports and "
                "extracted keywords. Only public fundus report-generation "
                "dataset — useful for VLM / captioning evaluation."
            ),
            modality="fundus",
            tasks=["classification", "multilabel"],  # primary task is report generation
            num_samples=15709,
            splits=["train", "val", "test"],
            download_type="manual",
            download_url="https://github.com/Jhhuangkay/DeepOpht-Medical-Report-Generation-for-Retinal-Images-via-Deep-Models-and-Visual-Explanation",
            license="Research only (NDA via email request)",
            citation=(
                "Huang et al., 'DeepOpht: Medical Report Generation for "
                "Retinal Images via Deep Models and Visual Explanation', "
                "WACV 2021."
            ),
            tags=["fundus", "report_generation", "vlm", "captioning"],
            size_gb=5.0,
            notes=(
                "NDA gated — email deepeyenet.den@gmail.com to request. "
                "No automated mirror exists."
            ),
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        print_manual_download_instructions(
            "DeepEyeNet", self.info.download_url,
            Path(data_dir) / self._SUBDIR,
            extra_notes="Email deepeyenet.den@gmail.com to request NDA.",
        )
        raise RuntimeError("DeepEyeNet requires NDA request via email.")
