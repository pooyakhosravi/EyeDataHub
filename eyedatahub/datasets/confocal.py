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

    An extended/professional version of the CORN database for corneal nerve
    analysis. Covers:
      - Nerve fiber segmentation (pixel-level annotations)
      - Image quality assessment / enhancement
      - Tortuosity grading (4 levels)

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
                "Professional/extended CORN database with in-vivo confocal "
                "microscopy images of the corneal subbasal nerve plexus. "
                "Supports nerve fiber segmentation, image quality enhancement, "
                "and tortuosity grading (4 levels). 384×384 px, 400×400 µm FOV. "
                "Based on the CORN-2 dataset (~688 annotated images: train 340 "
                "low-quality + 288 high-quality, test 60)."
            ),
            modality="confocal",
            tasks=["segmentation", "grading", "classification"],
            num_samples=688,
            splits=["train", "test"],
            image_size=(384, 384),
            download_type="manual",
            download_url=self._ZENODO_URL,
            license="CC BY 4.0",
            citation=(
                "CORN database (https://imed.nimte.ac.cn/CORN.html). "
                "Zenodo record 14263883: https://zenodo.org/records/14263883"
            ),
            tags=["confocal", "cornea", "nerve", "segmentation", "grading", "ivcm"],
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
            loader_version="0.3.0",
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
            relationships=[
                {
                    "type": "same_or_overlapping_cohort_as",
                    "target": "corn1500",
                },
                {
                    "type": "same_or_overlapping_cohort_as",
                    "target": "corn_pro",
                },
            ],
            item_count_evidence_url=self._ZENODO_URL,
            modality_evidence_url=self._ZENODO_URL,
            task_evidence_url=self._ZENODO_URL,
            citation_evidence_url=self._ZENODO_URL,
            author_source_checked=True,
            source_check_date="2026-07-25",
            source_check_status="checked_against_cited_source",
            independent_audit_status="not_independently_audited",
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


# Backwards-compatible alias
CORN2Dataset = CORNProDataset
