"""
OCT layer-segmentation and fluid-segmentation datasets.

Included:
  - OCT-MS-JHU    : 9-layer boundary delineation, 35 volumes (14 HC + 21 MS)
  - Duke-Chiu-BOE : 8-layer + fluid segmentation, 10 DME subjects
  - UMN-Parhi     : Fluid segmentation (IRF/SRF/PED), 24 AMD subjects, 600 B-scans
  - iChallenge-OCT: HDMILab ophthalmic challenges (registration-gated)
  - Duke-A2A-RPEDC: RPE-DC layer segmentation, 35 subjects (Duke / SF-59 lab)
  - OIMHSDataset  : Macular hole segmentation, 3,859 B-scans, 4 classes (Figshare 23508453)
  - AMDSDDataset  : Wet AMD lesion segmentation, 3,049 B-scans, 5 classes (Figshare / Kaggle)
  - OCTAVEDataset : 3D retinal segmentation, 198 volumes / 3,762 B-scans, 13 classes (Zenodo 14580071)
  - CAVRIDataset  : VitreoRetinal interface, 50 volumes / 7,050 B-scans (email-request)
  - TianDataset   : OCTRIMA 3D layer segmentation, 10 volumes, 8 boundaries (PLOS ONE)
"""
from __future__ import annotations

from pathlib import Path
from typing import Any, List, Union

import numpy as np
from PIL import Image

from eyedatahub.core.dataset import DatasetInfo, DatasetSample, EyeDataHubDataset
from eyedatahub.datasets.download_utils import (
    download_file,
    download_figshare,
    download_kaggle,
    download_zenodo,
    extract_archive,
    print_manual_download_instructions,
)


# ---------------------------------------------------------------------------
# Shared .mat helper
# ---------------------------------------------------------------------------

def _load_mat(path: Union[str, Path]) -> Any:
    """Load a MATLAB .mat file; supports both v5 and v7.3 (HDF5) formats."""
    import scipy.io
    try:
        return scipy.io.loadmat(str(path))
    except Exception:
        try:
            import h5py
            return h5py.File(str(path), "r")
        except ImportError:
            raise ImportError(
                "h5py is required for MATLAB v7.3 files: pip install h5py"
            )


# ---------------------------------------------------------------------------
# OCT MS + Healthy Controls (JHU / IACL)
# ---------------------------------------------------------------------------

class OCTMSJHUDataset(EyeDataHubDataset):
    """
    Retinal Layer Parcellation for Multiple Sclerosis and Healthy Controls.

    35 Spectralis OCT volumes (49 B-scans each):
      - 14 healthy controls (HC)
      - 21 multiple sclerosis (MS) subjects
    Nine retinal layer boundaries manually delineated per B-scan.

    Download:  https://iacl.ece.jhu.edu/~aaron/data/OCT_Manual_Delineations-2018_June_29_b.zip
    License:   CC BY-NC-ND
    Citation:  He et al., Data in Brief 22:601-604, 2019.
               https://doi.org/10.1016/j.dib.2018.12.073

    Preprocessing (MATLAB → PNG + JSON labels):
        https://github.com/heyufan1995/oct_preprocess

    Notes:
        Raw files are in Spectralis .vol format. After download the dataset
        class reads the binary .vol files directly to extract B-scans; the
        manual boundary annotations are stored in a separate directory.
        Install eyepy for .vol support: pip install eyepy
    """

    _SUBDIR = "oct_ms_jhu"
    _DATA_URL = (
        "https://iacl.ece.jhu.edu/~aaron/data/"
        "OCT_Manual_Delineations-2018_June_29_b.zip"
    )

    # 9 boundary names (ILM through RPE)
    LAYER_NAMES = [
        "ILM", "RNFL-OPL", "OPL-ONL", "ELM", "MZ", "EZ", "OSP", "IZ-RPE", "RPE"
    ]

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="oct_ms_jhu",
            full_name="OCT Retinal Layer Segmentation — MS & Healthy Controls (JHU/IACL)",
            description=(
                "35 Spectralis OCT volumes (1,715 B-scans) with 9 manually "
                "delineated retinal layer boundaries. 14 healthy controls, "
                "21 MS subjects."
            ),
            modality="oct",
            tasks=["segmentation"],
            num_samples=1715,
            splits=["all"],
            classes=self.LAYER_NAMES,
            num_classes=9,
            image_size=(496, 1024),
            download_type="direct",
            download_url=self._DATA_URL,
            license="CC BY-NC-ND",
            citation=(
                "Y. He et al., 'Retinal layer parcellation of optical coherence "
                "tomography images: Data resource for Multiple Sclerosis and "
                "Healthy Controls', Data in Brief 22:601-604, 2019."
            ),
            tags=["oct", "segmentation", "multiple_sclerosis", "layers", "jhu"],
            size_gb=1.8,
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        # After extraction a "Manual_Delineations" or "Volumes" directory exists
        return (
            any(root.glob("**/*.vol")) or
            any(root.glob("**/Manual_Delineations*")) or
            any(root.glob("**/*.png"))  # if already preprocessed
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        dest = Path(data_dir) / self._SUBDIR
        dest.mkdir(parents=True, exist_ok=True)
        zip_path = dest / "OCT_Manual_Delineations.zip"
        try:
            download_file(self._DATA_URL, zip_path)
            extract_archive(zip_path, dest)
            zip_path.unlink(missing_ok=True)
        except Exception as e:
            print_manual_download_instructions(
                "OCT MS & Healthy Controls (JHU/IACL)",
                self._DATA_URL,
                dest,
                extra_notes=(
                    f"Error: {e}\n\n"
                    "If the direct link fails, download the ZIP from:\n"
                    "  https://iacl.ece.jhu.edu/index.php/OCT_Data\n\n"
                    "For preprocessing .vol files to PNG:\n"
                    "  pip install eyepy\n"
                    "  https://github.com/heyufan1995/oct_preprocess"
                ),
            )

    def load(
        self, data_dir: Union[str, Path], split: str = "all"
    ) -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR
        samples: List[DatasetSample] = []

        # Strategy 1: already converted to PNG by oct_preprocess
        png_files = sorted(root.rglob("*.png"))
        if png_files:
            for png in png_files:
                label_path = png.with_suffix(".json")
                label: Any = str(label_path) if label_path.exists() else None
                samples.append(DatasetSample(
                    image_path=str(png),
                    label=label,
                    sample_id=png.stem,
                    metadata={"source": "preprocessed"},
                ))
            return samples

        # Strategy 2: raw .vol files via eyepy
        vol_files = sorted(root.rglob("*.vol"))
        if vol_files:
            for vol in vol_files:
                samples.append(DatasetSample(
                    image_path=str(vol),
                    label=None,   # boundaries stored in sidecar
                    sample_id=vol.stem,
                    metadata={"format": "spectralis_vol"},
                ))
            return samples

        raise FileNotFoundError(
            f"No images found in {root}. "
            "Run: eyehub download --datasets oct_ms_jhu"
        )

    def load_image(self, path: str) -> Image.Image:
        p = Path(path)
        if p.suffix == ".vol":
            return self._load_vol_bscan(p, idx=0)
        return Image.open(path).convert("RGB")

    @staticmethod
    def _load_vol_bscan(vol_path: Path, idx: int = 0) -> Image.Image:
        """Extract B-scan `idx` from a Spectralis .vol file via eyepy."""
        try:
            import eyepy
            vol = eyepy.import_retouch(str(vol_path))  # generic VOL reader
            bscan = vol[idx].data
        except (ImportError, Exception):
            try:
                import eyepy
                vol = eyepy.EyeVolumeVoxelData.from_heyex_vol(str(vol_path))
                bscan = np.array(vol)[idx]
            except Exception:
                # Minimal fallback: return a blank image
                return Image.new("L", (1024, 496), 0)
        arr = (bscan / bscan.max() * 255).astype(np.uint8) if bscan.max() > 0 else bscan.astype(np.uint8)
        return Image.fromarray(arr).convert("RGB")


# ---------------------------------------------------------------------------
# Duke Chiu BOE 2014 — DME OCT Layer + Fluid Segmentation
# ---------------------------------------------------------------------------

class DukeChiuBOEDataset(EyeDataHubDataset):
    """
    Duke OCT DME Dataset (Chiu et al., Biomedical Optics Express 2014).

    10 subjects with severe diabetic macular edema (DME).
    11 B-scans per subject (110 total).
    8 retinal layer boundaries + intra-retinal fluid regions,
    manually annotated by 2 independent clinicians.

    Download:  http://people.duke.edu/~sf59/Chiu_BOE_2014_dataset.htm
    Kaggle mirror: https://www.kaggle.com/datasets/paultimothymooney/chiu-2015
    License:   Research use (Duke University)
    Citation:  Chiu et al., BOE 2014. DOI: 10.1364/BOE.6.001172
    """

    _SUBDIR = "duke_chiu_boe"
    _PAGE_URL = "http://people.duke.edu/~sf59/Chiu_BOE_2014_dataset.htm"
    _KAGGLE_SLUG = "paultimothymooney/chiu-2015"

    # Subject .mat file URLs on Duke's server
    _MAT_BASE = "http://people.duke.edu/~sf59/"
    _MAT_FILES = [f"Subject_{i:02d}.mat" for i in range(1, 11)]

    LAYER_NAMES = [
        "ILM", "NFL-GCL", "IPL-INL", "INL-OPL", "OPL-ONL",
        "IS-OS", "OS-RPE", "BM"
    ]

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="duke_chiu_boe",
            full_name="Duke OCT DME Dataset (Chiu BOE 2014)",
            description=(
                "110 OCT B-scans from 10 DME subjects with 8 layer boundaries "
                "and fluid region annotations by 2 clinicians."
            ),
            modality="oct",
            tasks=["segmentation"],
            num_samples=110,
            splits=["all"],
            classes=self.LAYER_NAMES,
            num_classes=8,
            image_size=(496, 768),
            download_type="direct",
            download_url=self._PAGE_URL,
            license="Research use (Duke University)",
            citation=(
                "Chiu et al., 'Kernel regression based segmentation of optical "
                "coherence tomography images with diabetic macular edema', "
                "Biomedical Optics Express 2014. DOI: 10.1364/BOE.6.001172"
            ),
            tags=["oct", "segmentation", "dme", "layers", "fluid", "duke"],
            size_gb=0.1,
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        mats = list(root.glob("*.mat")) + list(root.glob("**/*.mat"))
        return len(mats) >= 10

    def download(self, data_dir: Union[str, Path]) -> None:
        dest = Path(data_dir) / self._SUBDIR
        dest.mkdir(parents=True, exist_ok=True)

        # Try Kaggle mirror first (more reliable)
        try:
            download_kaggle(self._KAGGLE_SLUG, dest, is_competition=False)
            return
        except Exception:
            pass

        # Try individual .mat files from Duke
        success = 0
        for fname in self._MAT_FILES:
            try:
                url = self._MAT_BASE + fname
                download_file(url, dest / fname)
                success += 1
            except Exception:
                pass

        if success == 0:
            print_manual_download_instructions(
                "Duke Chiu BOE 2014 OCT Dataset",
                self._PAGE_URL,
                dest,
                extra_notes=(
                    "Download all Subject_XX.mat files from the dataset page\n"
                    "and place them in the destination directory.\n\n"
                    "Kaggle mirror: "
                    "https://www.kaggle.com/datasets/paultimothymooney/chiu-2015"
                ),
            )

    def load(
        self, data_dir: Union[str, Path], split: str = "all"
    ) -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR
        mat_files = sorted(
            list(root.glob("*.mat")) + list(root.glob("**/*.mat"))
        )
        if not mat_files:
            raise FileNotFoundError(
                f"No .mat files in {root}. "
                "Run: eyehub download --datasets duke_chiu_boe"
            )

        samples: List[DatasetSample] = []
        for mat_path in mat_files:
            try:
                mat = _load_mat(mat_path)
                images = mat["images"] if "images" in mat else None
                if images is None:
                    continue
                # images shape: (rows, cols, n_bscans) = (496, 768, 11)
                n_bscans = images.shape[2] if images.ndim == 3 else 1
                for b in range(n_bscans):
                    samples.append(DatasetSample(
                        image_path=str(mat_path),
                        label=None,   # boundaries in manualFluid1/2 keys
                        sample_id=f"{mat_path.stem}_bscan{b:02d}",
                        metadata={
                            "mat_file": str(mat_path),
                            "bscan_idx": b,
                            "has_fluid1": "manualFluid1" in mat,
                            "has_fluid2": "manualFluid2" in mat,
                        },
                    ))
            except Exception:
                continue

        return samples

    def load_image(self, path: str) -> Image.Image:
        p = Path(path)
        if p.suffix == ".mat":
            mat = _load_mat(p)
            arr = mat.get("images", np.zeros((496, 768, 1)))
            bscan = arr[:, :, 0].astype(np.float32)
            bscan = (bscan / bscan.max() * 255).astype(np.uint8) if bscan.max() > 0 else bscan.astype(np.uint8)
            return Image.fromarray(bscan).convert("RGB")
        return Image.open(path).convert("RGB")


# ---------------------------------------------------------------------------
# UMN Parhi — AMD Fluid Segmentation
# ---------------------------------------------------------------------------

class UMNParhiDataset(EyeDataHubDataset):
    """
    University of Minnesota (UMN / Parhi Lab) AMD OCT Fluid Dataset.

    600 B-scans from 24 exudative AMD subjects (~25 B-scans/subject).
    Three fluid regions manually annotated by two ophthalmologists:
      - IRF (Intra-Retinal Fluid)
      - SRF (Sub-Retinal Fluid)
      - PED (Pigment Epithelial Detachment)

    Download:  http://people.ece.umn.edu/users/parhi/.DATA/OCT/DME/UMNDataset.mat
    License:   Academic research use (University of Minnesota)
    Citation:  Parhi Lab — http://people.ece.umn.edu/users/parhi/data-and-code/
    """

    _SUBDIR = "umn_parhi_oct"
    _MAT_URL = (
        "http://people.ece.umn.edu/users/parhi/.DATA/OCT/DME/UMNDataset.mat"
    )
    _README_URL = (
        "http://www.ece.umn.edu/users/parhi/.DATA/OCT/DME/ReadMe.pdf"
    )

    FLUID_CLASSES = ["IRF", "SRF", "PED"]

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="umn_parhi_oct",
            full_name="UMN Parhi Lab AMD OCT Fluid Segmentation Dataset",
            description=(
                "600 Spectralis OCT B-scans from 24 exudative AMD subjects. "
                "Three fluid region classes: IRF, SRF, PED. Dual expert annotation."
            ),
            modality="oct",
            tasks=["segmentation"],
            num_samples=600,
            splits=["all"],
            classes=self.FLUID_CLASSES,
            num_classes=3,
            image_size=(512, 512),
            download_type="direct",
            download_url=self._MAT_URL,
            license="Academic research use (University of Minnesota)",
            citation=(
                "Parhi Lab OCT AMD Fluid Dataset. "
                "http://people.ece.umn.edu/users/parhi/data-and-code/"
            ),
            tags=["oct", "segmentation", "amd", "fluid", "irf", "srf", "ped", "umn"],
            size_gb=0.5,
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return (root / "UMNDataset.mat").exists() or len(list(root.glob("*.mat"))) > 0

    def download(self, data_dir: Union[str, Path]) -> None:
        dest = Path(data_dir) / self._SUBDIR
        dest.mkdir(parents=True, exist_ok=True)
        mat_path = dest / "UMNDataset.mat"
        try:
            download_file(self._MAT_URL, mat_path)
            # Also grab the readme
            try:
                download_file(self._README_URL, dest / "ReadMe.pdf")
            except Exception:
                pass
        except Exception as e:
            print_manual_download_instructions(
                "UMN Parhi AMD OCT Dataset",
                self._MAT_URL,
                dest,
                extra_notes=(
                    f"Error: {e}\n\n"
                    "Data & Code page: "
                    "http://people.ece.umn.edu/users/parhi/data-and-code/\n"
                    "Direct MAT URL: " + self._MAT_URL
                ),
            )

    def load(
        self, data_dir: Union[str, Path], split: str = "all"
    ) -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR
        mat_candidates = list(root.glob("*.mat"))
        if not mat_candidates:
            raise FileNotFoundError(
                f"UMNDataset.mat not found in {root}. "
                "Run: eyehub download --datasets umn_parhi_oct"
            )

        mat_path = mat_candidates[0]
        mat = _load_mat(mat_path)

        # The mat file contains a struct/cell array with B-scans and masks
        # Key names vary; common layout: mat['data'] or mat['images']
        samples: List[DatasetSample] = []
        for key in ("data", "images", "oct", "bscan"):
            if key in mat:
                arr = mat[key]
                # arr expected shape: (n_bscans, H, W) or (H, W, n_bscans)
                n = arr.shape[0] if arr.ndim == 3 else 1
                for i in range(n):
                    samples.append(DatasetSample(
                        image_path=str(mat_path),
                        label=None,
                        sample_id=f"umn_bscan_{i:04d}",
                        metadata={"mat_file": str(mat_path), "bscan_idx": i, "data_key": key},
                    ))
                break
        else:
            # Unknown layout — expose raw keys in metadata
            n = 600  # known total
            for i in range(n):
                samples.append(DatasetSample(
                    image_path=str(mat_path),
                    label=None,
                    sample_id=f"umn_bscan_{i:04d}",
                    metadata={"mat_file": str(mat_path), "bscan_idx": i},
                ))

        return samples

    def load_image(self, path: str) -> Image.Image:
        p = Path(path)
        if p.suffix != ".mat":
            return Image.open(path).convert("RGB")
        mat = _load_mat(p)
        for key in ("data", "images", "oct", "bscan"):
            if key in mat:
                arr = np.array(mat[key])
                if arr.ndim == 3:
                    bscan = arr[0]
                elif arr.ndim == 2:
                    bscan = arr
                else:
                    continue
                bscan = bscan.astype(np.float32)
                if bscan.max() > 0:
                    bscan = bscan / bscan.max() * 255
                return Image.fromarray(bscan.astype(np.uint8)).convert("RGB")
        return Image.new("RGB", (512, 512), 0)


# ---------------------------------------------------------------------------
# iChallenge OCT (HDMILab / OMIA)
# ---------------------------------------------------------------------------

class iChallengeOCTDataset(EyeDataHubDataset):
    """
    iChallenge OCT Datasets from HDMILab / OMIA Workshops.

    A collection of ophthalmic OCT challenge datasets hosted at
    http://hdmilab.cn/ichallenge, including both training and test sets
    for various MICCAI / OMIA workshop challenges.

    Tasks vary by sub-challenge: layer segmentation, fluid detection,
    pathology classification.

    Download:  http://hdmilab.cn/ichallenge  (registration may be required)
    License:   Challenge-specific (non-commercial research)
    Notes:     Some datasets are distributed via Google Drive links on the
               challenge page. Accept the data usage agreement before downloading.
    """

    _SUBDIR = "ichallenge_oct"
    _INFO_URL = "http://hdmilab.cn/ichallenge"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="ichallenge_oct",
            full_name="iChallenge OCT Datasets (HDMILab / OMIA Workshops)",
            description=(
                "OCT challenge datasets from HDMILab covering retinal layer "
                "segmentation and fluid detection tasks from MICCAI/OMIA workshops. "
                "Includes sub-challenges such as AMD/CSC/DR classification and "
                "retinal layer segmentation; GAMMA challenge provides OCT volumes "
                "from 300 glaucoma patients (fundus + 3D OCT)."
            ),
            modality="oct",
            tasks=["segmentation", "classification"],
            num_samples=300,
            splits=["train", "test"],
            download_type="manual",
            download_url=self._INFO_URL,
            license="Non-commercial research (challenge-specific)",
            citation=(
                "HDMILab iChallenge. http://hdmilab.cn/ichallenge"
            ),
            tags=["oct", "segmentation", "challenge", "ichallenge", "omia"],
            size_gb=2.0,
            notes=(
                "num_samples refers to patient volumes (GAMMA has 300 patients, "
                "each with 3D OCT + fundus). Slice counts depend on sub-challenge. "
                "Visit http://hdmilab.cn/ichallenge, register/log in, and "
                "download the relevant challenge dataset(s). Place extracted "
                "files under ~/.eyedatahub/data/ichallenge_oct/."
            ),
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return (
            root.exists() and
            (
                any(root.rglob("*.jpg")) or
                any(root.rglob("*.png")) or
                any(root.rglob("*.tif")) or
                any(root.rglob("*.mat"))
            )
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        dest = Path(data_dir) / self._SUBDIR
        print_manual_download_instructions(
            "iChallenge OCT (HDMILab)",
            self._INFO_URL,
            dest,
            extra_notes=(
                "1. Visit http://hdmilab.cn/ichallenge\n"
                "2. Register / log in (free academic account)\n"
                "3. Choose the challenge dataset (some require Google Drive links)\n"
                "4. Download and extract into the destination directory above\n\n"
                "Google Drive links (when available) can be downloaded with:\n"
                "  pip install gdown\n"
                "  gdown 'https://drive.google.com/uc?id=<FILE_ID>'"
            ),
        )

    def load(
        self, data_dir: Union[str, Path], split: str = "train"
    ) -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR
        images = sorted(
            list(root.rglob("*.jpg")) +
            list(root.rglob("*.png")) +
            list(root.rglob("*.tif")) +
            list(root.rglob("*.jpeg"))
        )
        if not images:
            raise FileNotFoundError(
                f"No images found in {root}. "
                "Run: eyehub download --datasets ichallenge_oct"
            )

        # Filter by split dir name if subdirectory structure uses it
        split_lower = split.lower()
        filtered = [
            p for p in images if split_lower in str(p).lower()
        ] or images

        return [
            DatasetSample(
                image_path=str(p),
                label=None,
                sample_id=p.stem,
            )
            for p in filtered
        ]


# ---------------------------------------------------------------------------
# Duke A2A RPEDC OCT Segmentation Dataset
# ---------------------------------------------------------------------------

class DukeRPEDCDataset(EyeDataHubDataset):
    """
    Duke RPE-DC (Retinal Pigment Epithelium - Drusen Complex) OCT Dataset.

    OCT scans and derived RPE and drusen-complex measurements from 384 subjects.
    Published by the SF-59 lab at Duke University.

    Manual download required from:
      https://people.duke.edu/~sf59/RPEDC_Ophth_2013_dataset.htm
    """

    _SUBDIR = "duke_rpedc"
    _URL = "https://people.duke.edu/~sf59/RPEDC_Ophth_2013_dataset.htm"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="duke_rpedc",
            full_name="Duke RPE-Drusen Complex OCT Dataset",
            description=(
                "OCT data from 384 subjects, including 269 with AMD and 115 "
                "normal subjects, with 38,400 B-scans and derived total "
                "retina and RPE-drusen complex thickness measurements."
            ),
            modality="oct",
            tasks=["segmentation", "classification", "measurement"],
            num_samples=384,
            splits=["all"],
            classes=["normal", "amd"],
            num_classes=2,
            download_type="manual",
            download_url="https://people.duke.edu/~sf59/RPEDC_Ophth_2013_dataset.htm",
            license=(
                "Research only: research and educational use; commercialization "
                "and redistribution prohibited"
            ),
            citation=(
                "Farsiu S, Chiu SJ, O'Connell RV, et al. Quantitative "
                "classification of eyes with and without intermediate "
                "age-related macular degeneration using optical coherence "
                "tomography. Ophthalmology. 2014;121:162-172. "
                "doi:10.1016/j.ophtha.2013.07.013"
            ),
            tags=["oct", "segmentation", "classification", "amd", "drusen", "duke"],
            size_gb=20.0,
            notes=(
                "The source describes more than 20 GB of subject data, "
                "segmentation boundaries, and thickness maps."
            ),
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return (
            len(list(root.glob("**/*.mat"))) > 0
            or len(list(root.glob("**/*.img"))) > 0
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        dest = Path(data_dir) / self._SUBDIR
        from eyedatahub.datasets.download_utils import print_manual_download_instructions
        print_manual_download_instructions(
            "Duke A2A RPEDC",
            self._URL,
            dest,
            extra_notes=(
                "This dataset requires manual download from the Duke SF-59 lab website.\n"
                "1. Visit: https://people.duke.edu/~sf59/RPEDC_Ophth_2013_dataset.htm\n"
                "2. Read the source terms and download the provided archives.\n"
                "3. Extract the archives into:\n"
                f"   {dest}\n"
                "Expected layout:\n"
                "  duke_rpedc/AMD/Farsiu_Ophthalmology_2013_AMD_Subject_*.mat\n"
                "  duke_rpedc/Normal/Farsiu_Ophthalmology_2013_Normal_Subject_*.mat"
            ),
        )
        raise RuntimeError(
            "Duke A2A RPEDC dataset requires manual download. "
            "See instructions above."
        )

    def load(
        self, data_dir: Union[str, Path], split: str = "all"
    ) -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR

        samples = []
        for mat_path in sorted(root.rglob("*.mat")):
            path_text = str(mat_path).lower()
            if "normal" in path_text:
                label = 0
                diagnosis = "normal"
            elif "amd" in path_text:
                label = 1
                diagnosis = "amd"
            else:
                label = None
                diagnosis = "unknown"
            samples.append(
                DatasetSample(
                    image_path=str(mat_path),
                    label=label,
                    sample_id=mat_path.stem,
                    metadata={
                        "subject": mat_path.stem,
                        "diagnosis": diagnosis,
                        "split": split,
                        "format": "matlab_subject_volume",
                    },
                )
            )
        return samples



# ---------------------------------------------------------------------------
# OIMHS: OCT Image Macular Hole Segmentation Dataset (Figshare 23508453)
# ---------------------------------------------------------------------------

OIMHS_CLASSES = ["Retina", "Macular Hole", "Intraretinal Cysts", "Choroid"]


class OIMHSDataset(EyeDataHubDataset):
    """
    OIMHS: Optical Coherence Tomography Image Macular Hole Segmentation Dataset.

    3,859 B-scan images from 125 eyes of 119 macular hole patients.
    Images are side-by-side PNGs: left half = raw OCT B-scan,
    right half = colour-coded ground truth mask (4 classes).
    Annotated by 3 junior + 1 expert ophthalmologist.

    Figshare: https://doi.org/10.6084/m9.figshare.23508453
    Paper:    Scientific Data 10, 769 (2023) — doi:10.1038/s41597-023-02675-1
    """

    _SUBDIR = "oimhs"
    _FIGSHARE_ID = "23508453"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="oimhs",
            full_name="OIMHS: OCT Image Macular Hole Segmentation Dataset",
            description=(
                "3,859 OCT B-scan images (125 eyes, 119 patients) for macular "
                "hole segmentation. Each PNG is side-by-side: left half raw "
                "B-scan, right half colour-coded mask for 4 classes: Retina, "
                "Macular Hole, Intraretinal Cysts, Choroid."
            ),
            modality="oct",
            tasks=["segmentation"],
            num_samples=3859,
            splits=["train"],
            classes=OIMHS_CLASSES,
            num_classes=4,
            download_type="figshare",
            download_url="https://doi.org/10.6084/m9.figshare.23508453",
            license="CC0 1.0",
            citation=(
                "Ye X et al., 'OIMHS: An Optical Coherence Tomography Image "
                "Dataset Based on Macular Hole Manual Segmentation', "
                "Scientific Data 10, 769 (2023). "
                "doi:10.1038/s41597-023-02675-1"
            ),
            tags=["oct", "segmentation", "macular_hole", "figshare"],
            size_gb=2.0,
            notes=(
                "Images are side-by-side PNGs (left=raw, right=mask). "
                "125 eye-level subfolders under images/. No official split — "
                "apply your own train/val/test division."
            ),
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return len(list(root.rglob("*.png"))) > 100

    def download(self, data_dir: Union[str, Path]) -> None:
        dest = Path(data_dir) / self._SUBDIR
        try:
            download_figshare(self._FIGSHARE_ID, dest)
            for archive in list(dest.glob("*.zip")) + list(dest.glob("*.tar*")):
                extract_archive(archive, dest)
        except Exception:
            print_manual_download_instructions(
                "OIMHS",
                f"https://doi.org/10.6084/m9.figshare.{self._FIGSHARE_ID}",
                dest,
                extra_notes=(
                    "Download from Figshare article 23508453 and extract into:\n"
                    f"  {dest}\n"
                    "Expected layout: oimhs/images/<eye_id>/<scan>.png"
                ),
            )
            raise

    def load(
        self, data_dir: Union[str, Path], split: str = "train"
    ) -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR
        images = sorted(root.rglob("*.png"))
        if not images:
            raise FileNotFoundError(
                f"No images found in {root}. "
                "Run: eyehub download --datasets oimhs"
            )

        samples = []
        for img_path in images:
            # Each PNG is side-by-side (raw|mask); load left half as image path
            samples.append(
                DatasetSample(
                    image_path=str(img_path),
                    label=None,   # mask is right half of same PNG
                    sample_id=img_path.stem,
                    metadata={
                        "eye_id": img_path.parent.name,
                        "side_by_side": True,  # left=raw, right=mask
                    },
                )
            )
        return samples


# ---------------------------------------------------------------------------
# AMD-SD: Wet AMD OCT Lesion Segmentation Dataset (Figshare collection 7157554)
# ---------------------------------------------------------------------------

AMDSD_CLASSES = [
    "SRF",   # Subretinal Fluid
    "IRF",   # Intraretinal Fluid
    "EZC",   # Ellipsoid Zone Continuity
    "SHRM",  # Subretinal Hyperreflective Material
    "PED",   # Pigment Epithelial Detachment
]


class AMDSDDataset(EyeDataHubDataset):
    """
    AMD-SD: OCT Image Dataset for Wet AMD Lesion Segmentation.

    3,049 B-scan images (1,140 × 380 px) from 138 patients (156 eyes).
    Five lesion classes: SRF, IRF, EZC, SHRM, PED.
    Official train/val split provided as text files.
    Annotated by 3 junior + 1 expert ophthalmologist.

    Figshare: https://springernature.figshare.com/collections/.../7157554
    Paper:    Scientific Data 11, 1014 (2024) — doi:10.1038/s41597-024-03844-6
    Also on Kaggle: gaoweihao/amd-sd
    """

    _SUBDIR = "amd_sd"
    _KAGGLE_SLUG = "gaoweihao/amd-sd"
    _FIGSHARE_COLLECTION_URL = (
        "https://springernature.figshare.com/collections/"
        "AMD-SD_An_Optical_Coherence_Tomography_Image_Dataset_Based_on_"
        "Macular_Hole_Manual_Segmentation/7157554"
    )

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="amd_sd",
            full_name="AMD-SD: OCT Wet AMD Lesion Segmentation Dataset",
            description=(
                "3,049 OCT B-scan images (1,140×380 px) from 138 wet AMD "
                "patients (156 eyes) with pixel-level annotations for 5 lesion "
                "classes: Subretinal Fluid (SRF), Intraretinal Fluid (IRF), "
                "Ellipsoid Zone Continuity (EZC), Subretinal Hyperreflective "
                "Material (SHRM), and Pigment Epithelial Detachment (PED)."
            ),
            modality="oct",
            tasks=["segmentation"],
            num_samples=3049,
            splits=["train", "val"],
            classes=AMDSD_CLASSES,
            num_classes=5,
            download_type="kaggle",
            download_url="https://www.kaggle.com/datasets/gaoweihao/amd-sd",
            license="CC BY-NC-ND 4.0",
            citation=(
                "Hu Y et al., 'AMD-SD: An Optical Coherence Tomography Image "
                "Dataset for wet AMD Lesions Segmentation', "
                "Scientific Data 11, 1014 (2024). "
                "doi:10.1038/s41597-024-03844-6"
            ),
            tags=["oct", "segmentation", "amd", "fluid", "kaggle", "figshare"],
            size_gb=2.0,
            notes=(
                "Official split: training.txt / validation.txt at dataset root. "
                "Images in AMD-SD/images/<patient_id>/<scan>.png. "
                "Primary source: Figshare collection 7157554; "
                "mirror on Kaggle: gaoweihao/amd-sd."
            ),
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return len(list(root.rglob("*.png"))) > 100

    def download(self, data_dir: Union[str, Path]) -> None:
        dest = Path(data_dir) / self._SUBDIR
        try:
            download_kaggle(self._KAGGLE_SLUG, dest, is_competition=False)
        except Exception:
            print_manual_download_instructions(
                "AMD-SD",
                self._FIGSHARE_COLLECTION_URL,
                dest,
                extra_notes=(
                    "Option 1 — Kaggle (mirror):\n"
                    "  kaggle datasets download gaoweihao/amd-sd\n\n"
                    "Option 2 — Figshare collection:\n"
                    f"  Visit {self._FIGSHARE_COLLECTION_URL}\n"
                    "  Download individual article archives and extract.\n\n"
                    "Expected layout:\n"
                    "  amd_sd/images/<patient_id>/*.png\n"
                    "  amd_sd/training.txt\n"
                    "  amd_sd/validation.txt"
                ),
            )
            raise

    def load(
        self, data_dir: Union[str, Path], split: str = "train"
    ) -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR

        # Use official split files if available
        split_file = root / f"{'training' if split == 'train' else 'validation'}.txt"
        if split_file.exists():
            with open(split_file) as f:
                allowed = {line.strip() for line in f if line.strip()}
            images = [
                p for p in sorted(root.rglob("*.png"))
                if p.stem in allowed or p.name in allowed
                or str(p.relative_to(root)) in allowed
            ]
        else:
            images = sorted(root.rglob("*.png"))

        if not images:
            raise FileNotFoundError(
                f"No images found in {root}. "
                "Run: eyehub download --datasets amd_sd"
            )

        return [
            DatasetSample(
                image_path=str(p),
                label=None,  # segmentation masks paired by filename convention
                sample_id=p.stem,
                metadata={"patient_id": p.parent.name, "split": split},
            )
            for p in images
        ]


# ---------------------------------------------------------------------------
# OCTAVE: 3D SD-OCT Retinal Segmentation Dataset (Zenodo 14580071)
# ---------------------------------------------------------------------------

OCTAVE_CLASSES = [
    "RET",   # Retina
    "CHO",   # Choroid & Sclera
    "VIT",   # Vitreous
    "RPE",   # Retinal Pigment Epithelium
    "HYA",   # Hyaloid Membrane
    "RHS",   # Retrohyaloid Space
    "ERM",   # Epiretinal Membrane
    "SES",   # Sub-ERM Space
    "ART",   # Artifact
    "HRM",   # Hyper-Reflective Material
    "FLU",   # Intra-/Sub-Retinal Fluid
    "SRM",   # Subretinal Material
    "HTD",   # Hypertransmission Defect
]


class OCTAVEDataset(EyeDataHubDataset):
    """
    OCTAVE: Largest public annotated 3D SD-OCT segmentation dataset.

    198 annotated 3D OCT volumes (3,762 B-scans) for 13-class pixel-level
    segmentation of anatomic and pathological retinal features.
    4 external validation sets (221 volumes) included: Rasti, Tian,
    Kafieh, and CAVRI-A (Stankiewicz).

    nnU-Net-compatible format.

    Zenodo: https://zenodo.org/records/14580071
    GitHub: https://github.com/Translational-Biophotonics-Laboratory/octvision3d
    Paper:  IOVS 66(6):55 (2025) — doi:10.1167/iovs.66.6.55
    """

    _SUBDIR = "octave"
    _ZENODO_ID = "14580071"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="octave",
            full_name="OCTAVE: 3D SD-OCT Retinal Segmentation Dataset",
            description=(
                "198 annotated 3D SD-OCT volumes (3,762 B-scans) with pixel-level "
                "labels for 13 anatomic and pathological retinal features: "
                "retina, choroid, vitreous, RPE, hyaloid, ERM, fluid, "
                "subretinal material, hypertransmission defects, and more. "
                "4 additional external validation sets (221 volumes). "
                "nnU-Net-compatible format. IOVS 2025."
            ),
            modality="oct",
            tasks=["segmentation"],
            num_samples=198,
            splits=["train"],
            classes=OCTAVE_CLASSES,
            num_classes=13,
            download_type="zenodo",
            download_url="https://zenodo.org/records/14580071",
            license="CC BY-SA 4.0",
            citation=(
                "Kermany DS et al., 'Identifying Retinal Features Using a "
                "Self-Configuring CNN for Clinical Intervention', "
                "Investigative Ophthalmology & Visual Science 66(6):55 (2025). "
                "doi:10.1167/iovs.66.6.55 — "
                "Zenodo: https://zenodo.org/records/14580071"
            ),
            tags=["oct", "segmentation", "3d", "zenodo", "nnunet", "multi_class"],
            size_gb=15.0,
            notes=(
                "nnU-Net layout: nnUNet_raw/Dataset001_OCTAVE/imagesTr+labelsTr/. "
                "External test sets under nnUNet_raw/external_tests/. "
                "19 standardised B-scans per volume after preprocessing. "
                "GitHub: https://github.com/Translational-Biophotonics-Laboratory/"
                "octvision3d"
            ),
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return (
            (root / "nnUNet_raw").exists()
            or len(list(root.rglob("*.nii*"))) > 10
            or len(list(root.rglob("*.png"))) > 50
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        dest = Path(data_dir) / self._SUBDIR
        try:
            download_zenodo(self._ZENODO_ID, dest)
            for archive in list(dest.glob("*.zip")) + list(dest.glob("*.tar*")):
                extract_archive(archive, dest)
        except Exception:
            print_manual_download_instructions(
                "OCTAVE",
                "https://zenodo.org/records/14580071",
                dest,
                extra_notes=(
                    "Download from Zenodo record 14580071 and extract into:\n"
                    f"  {dest}\n\n"
                    "GitHub (code + preprocessing):\n"
                    "  https://github.com/Translational-Biophotonics-Laboratory/"
                    "octvision3d"
                ),
            )
            raise

    def load(
        self, data_dir: Union[str, Path], split: str = "train"
    ) -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR

        # nnU-Net layout: imagesTr / imagesTs / labelsTr
        split_dirs = {
            "train": ["imagesTr", "nnUNet_raw/Dataset001_OCTAVE/imagesTr"],
            "test":  ["imagesTs", "nnUNet_raw/Dataset001_OCTAVE/imagesTs",
                      "nnUNet_raw/external_tests"],
        }
        search_dirs = split_dirs.get(split, [split])

        images: List[Path] = []
        for sd in search_dirs:
            candidate = root / sd
            if candidate.exists():
                images.extend(candidate.rglob("*.nii*"))
                images.extend(candidate.rglob("*.png"))
                images.extend(candidate.rglob("*.tif*"))

        if not images:
            # Fallback: collect all NIfTI / image files
            images = (
                list(root.rglob("*.nii.gz"))
                + list(root.rglob("*.nii"))
                + list(root.rglob("*.png"))
            )

        if not images:
            raise FileNotFoundError(
                f"No volumes/images found in {root}. "
                "Run: eyehub download --datasets octave"
            )

        return [
            DatasetSample(
                image_path=str(p),
                label=None,
                sample_id=p.name.replace(".nii.gz", "").replace(".nii", ""),
                metadata={"split": split},
            )
            for p in sorted(set(images))
        ]


# ---------------------------------------------------------------------------
# CAVRI: Computer Analysis of VitreoRetinal Interface (PUT Poznan, email-request)
# ---------------------------------------------------------------------------

CAVRI_CLASSES = ["PCV", "ILM", "RPE"]   # 3 annotated boundary lines


class CAVRIDataset(EyeDataHubDataset):
    """
    CAVRI: Computer Analysis of VitreoRetinal Interface Dataset.

    50 annotated 3D SD-OCT volumes (7,050 B-scans) from subjects with
    vitreomacular adhesion (VMA, 25 eyes) and vitreomacular traction (VMT,
    25 eyes). Each volume: 141 B-scans at 640×385 px (2×7×7 mm tissue).
    Device: Avanti RTvue (Optovue). 3 annotated boundary layers: PCV, ILM, RPE.

    Access: email request to the PUT Poznan DSP lab.
    Dataset page: https://dsp.put.poznan.pl/cavri_database-191/
    Paper: Sensors 21(22):7521 (2021) — doi:10.3390/s21227521
    """

    _SUBDIR = "cavri"
    _INFO_URL = "https://dsp.put.poznan.pl/cavri_database-191/"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="cavri",
            full_name="CAVRI: Computer Analysis of VitreoRetinal Interface Dataset",
            description=(
                "50 annotated 3D SD-OCT volumes (7,050 B-scans, 640×385 px) "
                "from subjects with vitreomacular adhesion (VMA, 25 eyes) and "
                "vitreomacular traction (VMT, 25 eyes). Each volume: 141 B-scans "
                "over 2×7×7 mm. Annotated boundaries: PCV, ILM, RPE. "
                "Device: Optovue Avanti RTvue."
            ),
            modality="oct",
            tasks=["segmentation"],
            num_samples=50,
            splits=["train", "val", "test"],
            classes=CAVRI_CLASSES,
            num_classes=3,
            image_size=(640, 385),
            download_type="manual",
            download_url=self._INFO_URL,
            license="Research/educational use only (no commercial redistribution)",
            citation=(
                "Stankiewicz A et al., 'Segmentation of Preretinal Space in "
                "Optical Coherence Tomography Images Using Deep Neural Networks', "
                "Sensors 21(22):7521 (2021). doi:10.3390/s21227521"
            ),
            tags=["oct", "segmentation", "vitreoretinal", "boundary", "manual"],
            size_gb=3.0,
            notes=(
                "Access by email request: "
                "agnieszka.stankiewicz@put.poznan.pl or "
                "tomasz.marciniak@put.poznan.pl. "
                "Dataset page: https://dsp.put.poznan.pl/cavri_database-191/ "
                "GitHub (segmentation code): "
                "https://github.com/krzyk87/pcv_segmentation"
            ),
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return (
            root.exists()
            and (
                len(list(root.rglob("*.png"))) > 50
                or len(list(root.rglob("*.tif*"))) > 50
                or len(list(root.rglob("*.mat"))) > 5
            )
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        dest = Path(data_dir) / self._SUBDIR
        print_manual_download_instructions(
            "CAVRI",
            self._INFO_URL,
            dest,
            extra_notes=(
                "CAVRI requires an email access request.\n\n"
                "Contact the PUT Poznan DSP lab:\n"
                "  agnieszka.stankiewicz@put.poznan.pl\n"
                "  tomasz.marciniak@put.poznan.pl\n\n"
                "Dataset info: https://dsp.put.poznan.pl/cavri_database-191/\n"
                "Segmentation code: https://github.com/krzyk87/pcv_segmentation\n\n"
                f"After download, extract into:\n  {dest}"
            ),
        )
        raise RuntimeError(
            "CAVRI requires email access request. See instructions above."
        )

    def load(
        self, data_dir: Union[str, Path], split: str = "train"
    ) -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR
        # Typical layout: volumes in subdirectories per eye
        images = sorted(
            list(root.rglob("*.png"))
            + list(root.rglob("*.tif"))
            + list(root.rglob("*.bmp"))
        )
        # Filter by condition (VMA/VMT) as proxy for split if no split dirs
        if split != "all":
            filtered = [p for p in images if split.lower() in str(p).lower()]
            if filtered:
                images = filtered

        if not images:
            raise FileNotFoundError(
                f"No images found in {root}. "
                "Run: eyehub download --datasets cavri (email request required)"
            )
        return [
            DatasetSample(
                image_path=str(p),
                label=None,
                sample_id=p.stem,
                metadata={"split": split},
            )
            for p in images
        ]


# ---------------------------------------------------------------------------
# Tian OCTRIMA 3D Dataset (PLOS ONE 2015 supplementary data)
# ---------------------------------------------------------------------------

TIAN_BOUNDARIES = [
    "ILM",           # Inner Limiting Membrane
    "RNFL_GCL_IPL",  # RNFL / GCL+IPL boundary
    "IPL_INL",       # IPL / INL boundary
    "INL_OPL",       # INL / OPL boundary
    "OPL_ONL",       # OPL / ONL boundary
    "ELM",           # External Limiting Membrane
    "IS_OS",         # Inner/Outer Segment junction (Ellipsoid Zone)
    "OS_RPE",        # Outer Segment / RPE boundary
]


class TianDataset(EyeDataHubDataset):
    """
    Tian OCTRIMA 3D Layer Segmentation Dataset.

    10 SD-OCT volumes (510 B-scans) from 10 healthy subjects with 8 manually
    annotated retinal layer boundary surfaces (2 independent observers).
    Each volume: 496 × 644 × 51 voxels. Device: Heidelberg Spectralis SD-OCT.
    Data in MATLAB .mat format (raw volume + auto + manual segmentations).

    Supplement (S2 Dataset):
      https://doi.org/10.1371/journal.pone.0133908.s002
    Paper: PLOS ONE 10(8):e0133908 (2015) — doi:10.1371/journal.pone.0133908
    """

    _SUBDIR = "tian_oct"
    _PLOS_S2_DOI = "https://doi.org/10.1371/journal.pone.0133908.s002"
    # Direct download URL for the S2 supplement zip
    _DOWNLOAD_URL = (
        "https://journals.plos.org/plosone/article/file"
        "?id=10.1371/journal.pone.0133908.s002&type=supplementary"
    )

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="tian_oct",
            full_name="Tian OCTRIMA 3D OCT Layer Segmentation Dataset",
            description=(
                "10 Heidelberg Spectralis SD-OCT volumes (510 B-scans, "
                "496×644×51 voxels) from healthy subjects with 8 retinal "
                "layer boundary annotations by 2 independent observers. "
                "MATLAB .mat format; used as the OCTRIMA 3D validation set."
            ),
            modality="oct",
            tasks=["segmentation"],
            num_samples=10,
            splits=["test"],
            classes=TIAN_BOUNDARIES,
            num_classes=8,
            image_size=(496, 644),
            download_type="direct",
            download_url=self._PLOS_S2_DOI,
            license="CC BY 4.0",
            citation=(
                "Tian J et al., 'Real-Time Automatic Segmentation of Optical "
                "Coherence Tomography Volume Data of the Macular Region', "
                "PLOS ONE 10(8):e0133908 (2015). "
                "doi:10.1371/journal.pone.0133908"
            ),
            tags=["oct", "segmentation", "layer", "boundary", "matlab", "healthy"],
            size_gb=0.2,
            notes=(
                "Primarily a benchmark/test set (10 volumes, 2 observers). "
                "Each .mat file contains: raw OCT volume, OCTRIMA 3D automatic "
                "segmentation, Observer 1 manual, Observer 2 manual. "
                "Supplement URL: https://doi.org/10.1371/journal.pone.0133908.s002"
            ),
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return len(list(root.rglob("*.mat"))) >= 5

    def download(self, data_dir: Union[str, Path]) -> None:
        dest = Path(data_dir) / self._SUBDIR
        dest.mkdir(parents=True, exist_ok=True)
        archive = dest / "tian_s2_dataset.zip"
        try:
            download_file(self._DOWNLOAD_URL, archive, desc="Tian PLOS ONE S2")
            extract_archive(archive, dest)
        except Exception:
            print_manual_download_instructions(
                "Tian OCTRIMA 3D",
                self._PLOS_S2_DOI,
                dest,
                extra_notes=(
                    "Download the S2 Dataset supplement from PLOS ONE:\n"
                    "  https://doi.org/10.1371/journal.pone.0133908.s002\n\n"
                    "Or from the article page (Supporting Information → S2 Dataset):\n"
                    "  https://doi.org/10.1371/journal.pone.0133908\n\n"
                    f"Extract .mat files into:\n  {dest}"
                ),
            )
            raise

    def load(
        self, data_dir: Union[str, Path], split: str = "test"
    ) -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR
        mat_files = sorted(root.rglob("*.mat"))
        if not mat_files:
            raise FileNotFoundError(
                f"No .mat files found in {root}. "
                "Run: eyehub download --datasets tian_oct"
            )
        return [
            DatasetSample(
                image_path=str(m),
                label=None,  # boundaries stored inside .mat
                sample_id=m.stem,
                metadata={
                    "format": "matlab",
                    "n_boundaries": 8,
                    "n_observers": 2,
                },
            )
            for m in mat_files
        ]
