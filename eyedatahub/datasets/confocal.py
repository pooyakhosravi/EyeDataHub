"""
In-vivo Confocal Microscopy (IVCM) datasets — CORN-1500, CORN Pro,
and the combined CORN collection.

In-vivo confocal microscopy of the corneal subbasal nerve plexus is used to
assess corneal nerve density and morphology as a non-invasive biomarker for
diabetic peripheral neuropathy, dry eye disease, and other systemic conditions.

CORN-1500 (Zenodo 5880419)
--------------------------
  Task:        Corneal nerve tortuosity grading (4-class ordinal)
  Modality:    Corneal confocal microscopy (Heidelberg HRT-III)
  Images:      1,500 (1,200 train / 300 test)
  Classes:     Level 1 (lowest tortuosity) → Level 4 (highest)
  Resolution:  384 × 384 pixels; FOV = 400 × 400 µm²
  Access:      Restricted — requires request to zenodo record owner

  Reference:
    Mou et al., "DeepGrading: Deep Learning Grading of Corneal Nerve Tortuosity",
    IEEE TMI 2022.

CORN Pro (Zenodo 14263883)
--------------------------
  An extended/professional CORN dataset. Based on the CORN database
  (https://imed.nimte.ac.cn/CORN.html) which includes sub-datasets for
  nerve fiber segmentation, enhancement, and tortuosity grading.

  Access:    Restricted — requires request to zenodo record owner

Combined CORN collection (Zenodo 19689814)
------------------------------------------
  Current collection-level record for CORN-1, CORN-2, CORN-3, CORN-1500,
  CORN-Pro, and CORN-Complex. The record overlaps the two component records
  above and must not be interpreted as an independent cohort.
"""
from __future__ import annotations

from pathlib import Path
from typing import List, Union


from eyedatahub.core.dataset import DatasetInfo, DatasetSample, EyeDataHubDataset
from eyedatahub.datasets.download_utils import (
    download_zenodo,
    print_manual_download_instructions,
)


# ---------------------------------------------------------------------------
# CORN-1500
# ---------------------------------------------------------------------------

CORN_TORTUOSITY_LEVELS = ["Level 1", "Level 2", "Level 3", "Level 4"]


class CORN1500Dataset(EyeDataHubDataset):
    """
    CORN-1500: Corneal nerve tortuosity grading dataset.

    1,500 in-vivo confocal microscopy (IVCM) images of the corneal subbasal
    nerve plexus with expert-assigned tortuosity grades (1 = least tortuous,
    4 = most tortuous). Acquired with Heidelberg HRT-III confocal microscope.

    Tortuosity grade distribution (approximate):
      Level 1: 374 images  (normal/straight nerves)
      Level 2: 378 images  (mildly tortuous)
      Level 3: 375 images  (moderately tortuous)
      Level 4: 373 images  (highly tortuous, associated with neuropathy)

    This is an ordinal grading task — models should output grades 0–3
    (0-indexed Level 1–4).

    Access is restricted on Zenodo — you must request access from the record
    owner. See: https://zenodo.org/records/5880419

    Reference:
        Mou et al., "DeepGrading: Deep Learning Grading of Corneal Nerve
        Tortuosity", IEEE Transactions on Medical Imaging 2022.
        DOI: 10.1109/TMI.2022.3156906
    """

    _SUBDIR = "corn1500"
    _ZENODO_URL = "https://zenodo.org/records/5880419"
    _ZENODO_RECORD = "5880419"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="corn1500",
            full_name="CORN-1500: Corneal Nerve Tortuosity Grading",
            description=(
                "1,500 in-vivo confocal microscopy images of corneal subbasal "
                "nerve plexus, graded for tortuosity (4 levels). "
                "Train: 1,200 / Test: 300. 384×384 px, 400×400 µm FOV."
            ),
            modality="confocal",
            tasks=["grading", "classification"],
            num_samples=1500,
            splits=["train", "test"],
            classes=CORN_TORTUOSITY_LEVELS,
            num_classes=4,
            image_size=(384, 384),
            download_type="manual",
            download_url=self._ZENODO_URL,
            license="Restricted — request access from record owner",
            citation=(
                "Mou et al., 'DeepGrading: Deep Learning Grading of Corneal "
                "Nerve Tortuosity', IEEE TMI 2022. "
                "DOI: 10.1109/TMI.2022.3156906"
            ),
            tags=["confocal", "cornea", "nerve", "tortuosity", "grading", "ivcm"],
            size_gb=0.2,
            notes=(
                "Access is restricted. Request access at:\n"
                "  https://zenodo.org/records/5880419\n"
                "After approval, download and extract to the corn1500/ directory.\n"
                "The CORN database website: https://imed.nimte.ac.cn/CORN.html"
            ),
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        # Accept either flat or split-based structure
        return (
            len(list(root.glob("**/*.png"))) > 100
            or len(list(root.glob("**/*.bmp"))) > 100
            or len(list(root.glob("**/*.jpg"))) > 100
            or len(list(root.glob("**/*.tif"))) > 100
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        root = Path(data_dir) / self._SUBDIR
        print_manual_download_instructions(
            "CORN-1500",
            self._ZENODO_URL,
            root,
            extra_notes=(
                "CORN-1500 has restricted access on Zenodo.\n\n"
                "Steps to obtain access:\n"
                "  1. Create a free Zenodo account at https://zenodo.org\n"
                "  2. Navigate to https://zenodo.org/records/5880419\n"
                "  3. Click 'Request access' and provide your affiliation & purpose\n"
                "  4. Once approved, download the ZIP file\n\n"
                "Also check the full CORN database:\n"
                "  https://imed.nimte.ac.cn/CORN.html\n\n"
                "Expected directory structure after extraction:\n"
                "  corn1500/train/Level1/*.png (or *.bmp / *.jpg)\n"
                "  corn1500/train/Level2/*.png\n"
                "  corn1500/train/Level3/*.png\n"
                "  corn1500/train/Level4/*.png\n"
                "  corn1500/test/Level1/*.png\n"
                "  corn1500/test/Level2/*.png\n"
                "  corn1500/test/Level3/*.png\n"
                "  corn1500/test/Level4/*.png\n\n"
                "Alternative flat layout (also supported):\n"
                "  corn1500/images/*.png\n"
                "  corn1500/labels.csv  (columns: filename, grade)"
            ),
        )
        raise RuntimeError(
            "CORN-1500 requires manual download from Zenodo (restricted access)."
        )

    def load(
        self, data_dir: Union[str, Path], split: str = "test"
    ) -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR

        samples: List[DatasetSample] = []

        # ── Option 1: class subdirectory structure ────────────────────────────
        split_dir = root / split
        if not split_dir.exists():
            # Some releases use 'Train' / 'Test' (capitalised)
            split_dir = root / split.capitalize()
        if not split_dir.exists():
            # No split subdirectory — check flat structure
            split_dir = root

        # Try to find class-labelled subdirectories
        class_dirs_found = False
        for level_idx, level_name in enumerate(CORN_TORTUOSITY_LEVELS):
            for folder_name in [
                f"Level{level_idx + 1}",
                f"level{level_idx + 1}",
                f"Grade{level_idx + 1}",
                f"grade{level_idx + 1}",
                str(level_idx + 1),
                str(level_idx),
            ]:
                cls_dir = split_dir / folder_name
                if cls_dir.exists() and cls_dir.is_dir():
                    class_dirs_found = True
                    for img_path in sorted(
                        list(cls_dir.glob("*.png"))
                        + list(cls_dir.glob("*.bmp"))
                        + list(cls_dir.glob("*.jpg"))
                        + list(cls_dir.glob("*.tif"))
                    ):
                        samples.append(DatasetSample(
                            image_path=str(img_path),
                            label=level_idx,
                            sample_id=img_path.stem,
                            metadata={
                                "split": split,
                                "tortuosity_level": level_idx + 1,
                                "class_name": level_name,
                            },
                        ))
                    break

        if class_dirs_found:
            return samples

        # ── Option 2: flat layout with CSV labels ─────────────────────────────
        csv_candidates = (
            list(root.glob("*.csv"))
            + list(root.glob("labels*.csv"))
            + list(split_dir.glob("*.csv"))
        )
        if csv_candidates:
            import pandas as pd

            df = pd.read_csv(csv_candidates[0])
            id_col = df.columns[0]
            lbl_col = next(
                (c for c in df.columns if "grade" in c.lower()
                 or "level" in c.lower() or "label" in c.lower()),
                df.columns[1],
            )

            # Filter to split if a 'split' column is present
            if "split" in df.columns:
                df = df[df["split"] == split]

            img_dir = root / "images" if (root / "images").exists() else root
            for _, row in df.iterrows():
                img_id = str(row[id_col])
                # Grade may be 1-indexed or 0-indexed
                raw_grade = int(row[lbl_col])
                label = raw_grade - 1 if raw_grade >= 1 else raw_grade  # normalise to 0-3

                for ext in [".png", ".bmp", ".jpg", ".tif"]:
                    img_path = img_dir / f"{img_id}{ext}"
                    if img_path.exists():
                        samples.append(DatasetSample(
                            image_path=str(img_path),
                            label=label,
                            sample_id=img_id,
                            metadata={
                                "split": split,
                                "tortuosity_level": raw_grade,
                            },
                        ))
                        break
            return samples

        if not samples:
            raise FileNotFoundError(
                f"CORN-1500 data not found in {root}. "
                "Run `eyehub download --datasets corn1500` for instructions."
            )

        return samples


# ---------------------------------------------------------------------------
# CORN Pro (Zenodo 14263883)
# ---------------------------------------------------------------------------

class CORNProDataset(EyeDataHubDataset):
    """
    CORN Pro: Professional corneal confocal microscopy dataset (Zenodo 14263883).

    A 1,120-image corneal confocal microscopy resource for pixel-level
    segmentation of nerve fibers, Langerhans cells, and stromal cells.

    Part of the CORN database series: https://imed.nimte.ac.cn/CORN.html
    Access is restricted — request access at https://zenodo.org/records/14263883
    """

    _SUBDIR = "corn_pro"
    _ZENODO_URL = "https://zenodo.org/records/14263883"
    _ZENODO_RECORD = "14263883"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="corn_pro",
            full_name="CORN Pro: Corneal Nerve Confocal Microscopy Dataset",
            description=(
                "1,120 in-vivo confocal microscopy images with pixel-level "
                "annotations for corneal subbasal nerves and corneal cells. "
                "The source describes 560 images with nerves and Langerhans "
                "cells and 560 images with nerves and/or stromal cells."
            ),
            modality="confocal",
            tasks=["segmentation"],
            num_samples=1120,
            splits=["all"],
            image_size=(384, 384),
            download_type="manual",
            download_url=self._ZENODO_URL,
            license="CC BY 4.0",
            citation=(
                "CORN database (https://imed.nimte.ac.cn/CORN.html). "
                "Zenodo record 14263883: https://zenodo.org/records/14263883"
            ),
            tags=[
                "confocal",
                "cornea",
                "nerve",
                "langerhans_cells",
                "stromal_cells",
                "segmentation",
                "ivcm",
            ],
            size_gb=0.5,
            notes=(
                "Restricted access. Steps to obtain:\n"
                "  1. Create a free account at https://zenodo.org\n"
                "  2. Visit https://zenodo.org/records/14263883\n"
                "  3. Click 'Request access' with affiliation & purpose\n"
                "Full CORN database: https://imed.nimte.ac.cn/CORN.html"
            ),
        )

    # Keep a class alias so existing code using CORN2Dataset still works
    pass

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        return (
            len(list(root.glob("**/*.png"))) > 50
            or len(list(root.glob("**/*.bmp"))) > 50
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        root = Path(data_dir) / self._SUBDIR
        print_manual_download_instructions(
            "CORN Pro",
            self._ZENODO_URL,
            root,
            extra_notes=(
                "CORN Pro has restricted access on Zenodo.\n\n"
                "Steps to obtain access:\n"
                "  1. Create a free Zenodo account at https://zenodo.org\n"
                "  2. Navigate to https://zenodo.org/records/14263883\n"
                "  3. Click 'Request access' and provide your affiliation & purpose\n\n"
                "Also check the full CORN database website for all variants:\n"
                "  https://imed.nimte.ac.cn/CORN.html\n\n"
                "After download, extract to: corn_pro/\n"
                "The exact structure depends on the dataset variant. "
                "Common layouts:\n"
                "  Segmentation: corn_pro/images/*.png + corn_pro/masks/*.png\n"
                "  Grading:      corn_pro/Level{1-4}/*.png or corn_pro/labels.csv"
            ),
        )
        raise RuntimeError(
            "CORN Pro requires manual download from Zenodo (restricted access)."
        )

    def load(
        self, data_dir: Union[str, Path], split: str = "test"
    ) -> List[DatasetSample]:
        root = Path(data_dir) / self._SUBDIR

        samples: List[DatasetSample] = []

        # ── Segmentation layout: images/ + masks/ ─────────────────────────────
        img_dir = root / "images"
        mask_dir = root / "masks"
        if img_dir.exists():
            for img_path in sorted(
                list(img_dir.glob("*.png"))
                + list(img_dir.glob("*.bmp"))
                + list(img_dir.glob("*.jpg"))
            ):
                stem = img_path.stem
                mask_path = ""
                if mask_dir.exists():
                    candidates = list(mask_dir.glob(f"{stem}*.png")) + list(mask_dir.glob(f"{stem}*.bmp"))
                    mask_path = str(candidates[0]) if candidates else ""
                samples.append(DatasetSample(
                    image_path=str(img_path),
                    label=mask_path if mask_path else 0,
                    sample_id=stem,
                    metadata={"split": split},
                ))
            return samples

        # ── Grading layout: Level{N}/ subdirectories ──────────────────────────
        split_dir = root / split
        if not split_dir.exists():
            split_dir = root

        for level_idx in range(4):
            for folder_name in [
                f"Level{level_idx + 1}", f"level{level_idx + 1}",
                str(level_idx + 1), str(level_idx),
            ]:
                cls_dir = split_dir / folder_name
                if cls_dir.exists():
                    for img_path in sorted(
                        list(cls_dir.glob("*.png")) + list(cls_dir.glob("*.bmp"))
                    ):
                        samples.append(DatasetSample(
                            image_path=str(img_path),
                            label=level_idx,
                            sample_id=img_path.stem,
                            metadata={"split": split},
                        ))
                    break

        if not samples:
            # Fallback: all images without labels
            for img_path in sorted(root.glob("**/*.png")) + sorted(root.glob("**/*.bmp")):
                if "mask" not in img_path.parent.name.lower():
                    samples.append(DatasetSample(
                        image_path=str(img_path),
                        label=0,
                        sample_id=img_path.stem,
                        metadata={"split": split},
                    ))

        if not samples:
            raise FileNotFoundError(
                f"CORN Pro data not found in {root}. "
                "Run `eyehub download --datasets corn_pro` for instructions."
            )

        return samples


# ---------------------------------------------------------------------------
# Combined CORN collection (Zenodo 19689814)
# ---------------------------------------------------------------------------

class CORNCollectionDataset(EyeDataHubDataset):
    """Current combined record for the six CORN confocal-image subsets."""

    _SUBDIR = "corn_collection"
    _ZENODO_URL = "https://zenodo.org/records/19689814"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="corn_collection",
            full_name="CORN: Corneal Confocal Microscope Dataset Collection",
            description=(
                "Combined corneal confocal microscopy collection comprising "
                "CORN-1, CORN-2, CORN-3, CORN-1500, CORN-Pro, and "
                "CORN-Complex. The subsets support corneal-nerve and cell "
                "segmentation, image enhancement, tortuosity grading, and "
                "multi-disease analysis."
            ),
            modality="confocal",
            modalities=["confocal"],
            tasks=["segmentation", "grading", "classification", "quality"],
            # The source reports counts for each component, but the components
            # overlap and no non-overlapping collection total is stated.
            num_samples=None,
            item_count_unit="images",
            splits=["all"],
            image_size=(384, 384),
            download_type="manual",
            download_url=self._ZENODO_URL,
            license="Creative Commons Attribution 4.0 International",
            citation=(
                "iMED. CORN: corneal confocal microscope dataset. "
                "Zenodo, Version v2, 2026. doi:10.5281/zenodo.19689814"
            ),
            tags=[
                "confocal",
                "cornea",
                "corneal_nerve",
                "langerhans_cells",
                "stromal_cells",
                "segmentation",
                "tortuosity",
                "grading",
                "restricted",
            ],
            size_gb=None,
            notes=(
                "The Zenodo record is publicly visible, but its files require "
                "a logged-in access request containing the user's name, "
                "organization, work, and intended use. EyeDataHub displays "
                "those instructions and does not submit the request. This "
                "collection includes and overlaps the separately indexed "
                "CORN-1500 and CORN-Pro records; its six subsets must not be "
                "counted as independent cohorts."
            ),
            source_landing_page_url=self._ZENODO_URL,
            preferred_route_type="documented_manual_route",
            preferred_route_url=self._ZENODO_URL,
            access_friction="controlled_or_manual",
            requires_registration=True,
            requires_authentication=True,
            requires_api_token=False,
            requires_clickthrough=False,
            requires_manual_approval=True,
            requires_data_use_agreement=False,
            requires_author_contact=False,
            requires_payment=False,
            geographic_or_institutional_restriction="none_stated",
            availability_status="available",
            route_last_checked="2026-07-25",
            route_check_result="acquisition_route_verified",
            route_check_notes=(
                "The dataset-specific Zenodo page and restricted request-access "
                "workflow were checked without requesting or transferring files."
            ),
            acquisition_support="manual_access_blocked",
            loader_backend="manual",
            loader_name="manual_access_instructions",
            loader_version="0.4.0",
            loader_live_tested=False,
            loader_test_date="2026-07-25",
            loader_test_scope="preflight_and_manual_blocking",
            loader_test_result="manual_route_blocked_as_intended",
            tested_command=(
                "eyehub download corn_collection --data-dir <directory> "
                "--dry-run --json"
            ),
            source_terms="Creative Commons Attribution 4.0 International",
            terms_evidence_url=self._ZENODO_URL,
            terms_scope="dataset_files",
            terms_component_notes=(
                "Zenodo labels the restricted dataset record CC BY 4.0; access "
                "approval remains a separate requirement."
            ),
            dataset_doi="10.5281/zenodo.19689814",
            repository_record_id="zenodo:19689814",
            resource_version="Version v2",
            canonical_resolver_url="https://doi.org/10.5281/zenodo.19689814",
            item_count_evidence_url=self._ZENODO_URL,
            modality_evidence_url=self._ZENODO_URL,
            task_evidence_url=self._ZENODO_URL,
            citation_evidence_url=self._ZENODO_URL,
            author_source_checked=True,
            source_check_date="2026-07-25",
            source_check_status="checked_against_cited_source",
            access_check_status="acquisition_route_verified",
            transfer_check_status="manual_route_not_transferred",
        )

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = Path(data_dir) / self._SUBDIR
        ignored = {".download_complete", "eyedatahub-acquisition-manifest.json"}
        return root.exists() and any(
            path.is_file() and path.name not in ignored for path in root.rglob("*")
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        root = Path(data_dir) / self._SUBDIR
        print_manual_download_instructions(
            self.info.full_name,
            self._ZENODO_URL,
            root,
            extra_notes=(
                "Sign in to Zenodo and submit the source's request-access form. "
                "EyeDataHub does not submit the request or accept terms for you."
            ),
        )
        raise RuntimeError(
            "The combined CORN collection requires manual approval on Zenodo."
        )

    def load(
        self, data_dir: Union[str, Path], split: str = "all"
    ) -> List[DatasetSample]:
        raise NotImplementedError(
            "corn_collection contains six overlapping subsets with different "
            "tasks and layouts; no unified parser is implemented."
        )


# ---------------------------------------------------------------------------
# Qilu corneal confocal microscopy nerve segmentation dataset
# ---------------------------------------------------------------------------

class QiluCCMNerveSegmentationDataset(EyeDataHubDataset):
    """Human CCM images, nerve masks, and linked clinical data from Qilu."""

    _SUBDIR = "qilu_ccm_nerve_segmentation"
    _ZENODO_URL = "https://zenodo.org/records/18779434"
    _ZENODO_RECORD = "18779434"
    _ARTICLE_URL = "https://doi.org/10.1038/s41597-026-07418-6"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="qilu_ccm_nerve_segmentation",
            full_name=(
                "Qilu Annotated Corneal Confocal Microscopy Nerve "
                "Segmentation Dataset"
            ),
            description=(
                "A human corneal confocal microscopy dataset containing 410 "
                "source images from 88 participants, 410 filename-matched "
                "pixel-level nerve segmentation masks, 20 repeat annotations, "
                "and image-linked clinical and demographic data."
            ),
            modality="confocal",
            modalities=["confocal", "tabular"],
            primary_category="confocal",
            tasks=["segmentation", "classification", "measurement"],
            num_samples=410,
            item_count_unit="images",
            reported_quantities=[
                {
                    "count": 410,
                    "unit": "images",
                    "scope": "Original CCM images in Set1 and Set2",
                    "evidence_url": self._ARTICLE_URL,
                    "evidence_basis": "associated_publication",
                    "primary": True,
                    "exactness": "exact",
                    "review_date": "2026-08-02",
                    "notes": "Set1 contains 210 images and Set2 contains 200 images.",
                },
                {
                    "count": 410,
                    "unit": "annotated_images",
                    "scope": "Filename-matched binary nerve segmentation masks",
                    "evidence_url": self._ARTICLE_URL,
                    "evidence_basis": "associated_publication",
                    "primary": False,
                    "exactness": "exact",
                    "review_date": "2026-08-02",
                    "notes": "One expert-reviewed pixel-level mask per source image.",
                },
                {
                    "count": 88,
                    "unit": "participants",
                    "scope": "Participants represented across Set1 and Set2",
                    "evidence_url": self._ARTICLE_URL,
                    "evidence_basis": "associated_publication",
                    "primary": False,
                    "exactness": "exact",
                    "review_date": "2026-08-02",
                    "notes": "Set1 has 34 participants and Set2 has 54 participants.",
                },
                {
                    "count": 20,
                    "unit": "annotated_images",
                    "scope": "Subset with repeat annotations",
                    "evidence_url": self._ARTICLE_URL,
                    "evidence_basis": "associated_publication",
                    "primary": False,
                    "exactness": "exact",
                    "review_date": "2026-08-02",
                    "notes": "These are repeat labels for existing images, not 20 additional images.",
                },
            ],
            splits=["set1", "set2"],
            download_type="zenodo",
            download_url=self._ZENODO_URL,
            license="Creative Commons Attribution 4.0 International",
            citation=(
                "Qiao Q, Cao J, Hou X. An Annotated Corneal Confocal "
                "Microscopy Dataset for Nerve Segmentation and Clinical "
                "Characterization. Scientific Data. 2026;13:1051. "
                "doi:10.1038/s41597-026-07418-6. Dataset: "
                "doi:10.5281/zenodo.18779434."
            ),
            tags=[
                "confocal",
                "cornea",
                "corneal_nerve",
                "segmentation",
                "clinical_data",
                "diabetes",
                "human",
            ],
            size_gb=0.06370422896,
            notes=(
                "The current Zenodo deposit contains one 68,401,895-byte "
                "archive with 410 source PNG images, 410 corresponding masks, "
                "20 repeat annotations, and one linked workbook. The version-"
                "specific dataset DOI is 10.5281/zenodo.18779434 and the "
                "concept DOI is 10.5281/zenodo.17570502. Reference 35 in the "
                "published article lists 10.5281/zenodo.17570504, which resolves "
                "to an unrelated record; the article's Data Records section "
                "and the official deposit identify 10.5281/zenodo.18779434."
            ),
            source_landing_page_url=self._ZENODO_URL,
            preferred_route_type="official_repository",
            preferred_route_url=self._ZENODO_URL,
            access_friction="anonymous_direct",
            requires_registration=False,
            requires_authentication=False,
            requires_api_token=False,
            requires_clickthrough=False,
            requires_manual_approval=False,
            requires_data_use_agreement=False,
            requires_author_contact=False,
            requires_payment=False,
            geographic_or_institutional_restriction="none_stated",
            availability_status="available",
            route_last_checked="2026-08-02",
            route_check_result="anonymous_official_route_verified",
            route_check_notes=(
                "The public record metadata and complete Dataset.zip file were "
                "retrieved without authentication on 2026-08-02."
            ),
            acquisition_support="standard_platform_supported",
            loader_backend="zenodo",
            loader_name="download_zenodo",
            loader_version="0.6.0",
            loader_live_tested=False,
            loader_test_date="2026-08-02",
            loader_test_scope="implementation_reviewed_against_verified_layout",
            loader_test_result="new_loader_not_yet_live_tested",
            tested_command=(
                "eyehub download qilu_ccm_nerve_segmentation "
                "--data-dir <directory> --json"
            ),
            source_terms="Creative Commons Attribution 4.0 International",
            terms_evidence_url=self._ZENODO_URL,
            terms_scope="dataset_files",
            terms_component_notes=(
                "Zenodo applies CC BY 4.0 to the deposited dataset files."
            ),
            dataset_doi="10.5281/zenodo.18779434",
            repository_record_id="zenodo:18779434",
            associated_publication_doi="10.1038/s41597-026-07418-6",
            resource_version="Zenodo record 18779434",
            canonical_resolver_url="https://doi.org/10.5281/zenodo.18779434",
            item_count_evidence_url=self._ARTICLE_URL,
            modality_evidence_url=self._ARTICLE_URL,
            task_evidence_url=self._ARTICLE_URL,
            citation_evidence_url=self._ARTICLE_URL,
            author_source_checked=True,
            source_check_date="2026-08-02",
            source_check_status="checked_against_official_deposit_and_article",
            access_check_status="anonymous_official_route_verified",
            transfer_check_status=(
                "complete_current_deposit_downloaded_via_official_route"
            ),
        )

    @staticmethod
    def _dataset_root(root: Path) -> Path:
        nested = root / "Dataset"
        return nested if nested.exists() else root

    def is_downloaded(self, data_dir: Union[str, Path]) -> bool:
        root = self._dataset_root(Path(data_dir) / self._SUBDIR)
        image_dir = root / "images"
        annotation_dir = root / "annotations"
        if not image_dir.is_dir() or not annotation_dir.is_dir():
            return False
        image_names = {path.name for path in image_dir.glob("*.png")}
        annotation_names = {path.name for path in annotation_dir.glob("*.png")}
        return len(image_names) == 410 and image_names == annotation_names

    def download(self, data_dir: Union[str, Path]) -> None:
        root = Path(data_dir) / self._SUBDIR
        download_zenodo(self._ZENODO_RECORD, root, extract=True)

    def load(
        self, data_dir: Union[str, Path], split: str = "all"
    ) -> List[DatasetSample]:
        if split not in {"all", "set1", "set2"}:
            raise ValueError("split must be one of: all, set1, set2")

        root = self._dataset_root(Path(data_dir) / self._SUBDIR)
        image_dir = root / "images"
        annotation_dir = root / "annotations"
        if not image_dir.is_dir() or not annotation_dir.is_dir():
            raise FileNotFoundError(
                f"Qilu CCM images and annotations were not found in {root}."
            )

        samples: List[DatasetSample] = []
        for image_path in sorted(image_dir.glob("*.png")):
            set_name = f"set{image_path.stem[0]}"
            if split != "all" and set_name != split:
                continue
            mask_path = annotation_dir / image_path.name
            if not mask_path.is_file():
                raise FileNotFoundError(
                    f"Missing segmentation mask for {image_path.name}"
                )
            samples.append(
                DatasetSample(
                    image_path=str(image_path),
                    label=str(mask_path),
                    sample_id=image_path.stem,
                    metadata={
                        "split": set_name,
                        "mask_path": str(mask_path),
                    },
                )
            )
        return samples


# Backwards-compatible alias
CORN2Dataset = CORNProDataset
