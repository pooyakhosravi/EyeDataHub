---
name: add-dataset
description: Add a new public ophthalmic or eye-related dataset to EyeDataHub end to end. Triggers when a user says "add a dataset", "register dataset X", "/add-dataset", or describes a new ophthalmic dataset they want indexed. Walks through source verification, DatasetInfo metadata, loader/backend implementation, registry registration, generated docs, tests, and PR preparation.
---

# Skill: add-dataset

Use this skill when adding a dataset to EyeDataHub or preparing a PR for a
community contributor. The canonical repository guide is `CLAUDE.md`; the
human contributor workflow is `CONTRIBUTING.md`. Use `eyedatahub` for Python
imports and `eyehub` for CLI examples.

## First checks

1. Confirm the dataset is public, free to access, and eye-related.
2. Check duplicates before editing:

```bash
eyehub list datasets --json
eyehub show <possible_slug> --json
python -c "from eyedatahub.datasets.registry import REGISTRY; print(len(REGISTRY.list_datasets())); print([n for n in REGISTRY.names() if 'candidate' in n])"
```

3. Identify whether the proposed resource is an original dataset, a mirror, a
   derivative annotation layer, a VQA/report corpus, embeddings, or an
   instruction-tuning resource. Retain derivatives only when they add a
   distinct task, annotation, modality pairing, or machine-readable access
   route.

## Required metadata

Gather these fields from the official source page, paper, DOI record, challenge
page, or repository. Do not rely on mirrors when provenance conflicts.

- `name`: stable snake_case slug.
- `full_name`: human-readable name.
- `description`: one or two precise sentences.
- `modality`: use an existing registry value when possible, such as `fundus`,
  `oct`, `octa`, `uwf_fundus`, `visual_field`, `ivcm`, `surgical_video`,
  `multimodal`, `text`, `tabular`, `eye_tracking`, `electrophysiology`, or
  `corneal_topography`.
- `tasks`: e.g. `classification`, `grading`, `segmentation`, `multilabel`,
  `regression`, `progression`, `quality`, `registration`, `vqa`,
  `report_generation`, or `workflow`.
- `num_samples`: source-reported unit count. Use `None` only when unavailable.
- `splits`: official splits, or `["all"]` when no split is documented.
- `classes` and `num_classes`: omit or set `None` when not applicable.
- `image_size`: typical `(height, width)` when fixed; otherwise omit.
- `download_type`: `direct`, `kaggle`, `huggingface`, `zenodo`, `mendeley`,
  `figshare`, `physionet`, `gdrive`, `synapse`, `manual`, or an existing
  backend in `eyedatahub/datasets/download_utils.py`.
- `download_url`: official source URL or DOI URL.
- `license`: exact source text, not a guess.
- `citation`: publication, DOI, arXiv, dataset DOI, or stable source URL.
- `tags`: short lowercase tags useful for search/filtering.
- `size_gb`: source-reported download size, if known.
- `notes`: access restrictions, license caveats, duplicate/mirror details,
  parser limitations, patient-level split caveats, or upstream dependencies.

## License verification

License verification is mandatory and must happen before coding.

- Find the official source license: dataset page, DOI record, challenge rules,
  repository `LICENSE`, paper data-availability section, or bundle terms.
- Preserve the exact license string in `DatasetInfo.license`.
- Confirm the computed `info.license_family` is one of:
  `cc0`, `cc-by`, `cc-by-sa`, `mit`, `apache`, `cc-by-nc`,
  `cc-by-nc-sa`, `cc-by-nc-nd`, `research-only`, or `unknown`.
- If a mirror has different terms from the original source, use the original
  source as authoritative and document the discrepancy in `notes`. When unsure,
  choose the more restrictive interpretation and mark the caveat.
- If no explicit license is found, use `license="Unknown"` and add a `notes`
  explanation. Never invent a license.

## Implementation workflow

### 1. Choose the dataset module

Add the class to the closest existing module:

| Dataset type | Typical module |
|---|---|
| Fundus DR / lesions | `eyedatahub/datasets/fundus_dr.py` |
| Fundus glaucoma | `eyedatahub/datasets/fundus_glaucoma.py` |
| Fundus AMD | `eyedatahub/datasets/fundus_amd.py` |
| Fundus vessels | `eyedatahub/datasets/fundus_vessels.py` |
| Fundus misc / multi-disease | `eyedatahub/datasets/fundus_misc.py` or `fundus_multi.py` |
| OCT / OCTA classification | `eyedatahub/datasets/oct_datasets.py` |
| OCT segmentation | `eyedatahub/datasets/oct_segmentation.py` |
| Ultra-widefield fundus | `eyedatahub/datasets/uwf_datasets.py` |
| Surgical video | `eyedatahub/datasets/surgical_datasets.py` |
| Visual field | `eyedatahub/datasets/visual_field.py` |
| Confocal microscopy | `eyedatahub/datasets/confocal.py` |
| Challenge collections | `eyedatahub/datasets/ichallenge_datasets.py` or `stage_challenge.py` |
| Recent/community metadata-only additions | `community_recent.py`, `community_2026.py`, or `platform_2026.py` |

If the dataset has a real parser/download pattern, copy the closest implemented
loader. If it is gated/manual or parser support is not ready, use the local
stub pattern used by the community modules and make the limitation explicit in
`notes`.

### 2. Add a `DatasetInfo` class

Use the existing class-based registry pattern, not `configs/datasets.yaml`.

```python
from pathlib import Path
from typing import Union

from eyedatahub.core.dataset import DatasetInfo, EyeDataHubDataset
from eyedatahub.datasets.community_recent import _StubLoadMixin
from eyedatahub.datasets.download_utils import print_manual_download_instructions


class ExampleDataset(_StubLoadMixin, EyeDataHubDataset):
    """Short dataset summary with source/year."""

    _SUBDIR = "example_dataset"

    @property
    def info(self) -> DatasetInfo:
        return DatasetInfo(
            name="example_dataset",
            full_name="Example Ophthalmic Dataset",
            description="What the dataset contains and what task it supports.",
            modality="fundus",
            tasks=["classification"],
            num_samples=1234,
            splits=["all"],
            num_classes=2,
            classes=["negative", "positive"],
            download_type="manual",
            download_url="https://doi.org/10.xxxx/example",
            license="CC BY 4.0",
            citation="Author A, Author B. Dataset title. Journal. 2026. doi:10.xxxx/example",
            tags=["fundus", "classification"],
            size_gb=1.2,
            notes="Any access caveat, duplicate relationship, or parser limitation.",
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        print_manual_download_instructions(
            self.info.full_name,
            self.info.download_url,
            Path(data_dir) / self._SUBDIR,
        )
```

### 3. Register the dataset

Edit `eyedatahub/datasets/registry.py`:

- Import the new class in `_register_all()`.
- Instantiate it in the `datasets = [...]` list under the appropriate section.
- Keep related datasets grouped and readable.

If the new dataset changes the total count, update `EXPECTED_DATASET_COUNT` in
`tests/test_smoke.py`.

### 4. Update generated surfaces

Run these when the PR includes generated docs/catalog snapshots:

```bash
python -m hub.docs.generate_dataset_pages --out website/docs
python -m hub.docs.generate_llms_full
```

If the dataset should be included in the Hugging Face mirror, update
`hub/label_schema.json` only when the labels/classes are understood and the
source documentation explicitly authorizes redistribution for that component.
Do not add restricted datasets to the mirror.

### 5. Smoke tests

At minimum:

```bash
python -m pytest -q
python -m eyedatahub.cli list datasets --json
python -m eyedatahub.cli show <slug> --json
python -m eyedatahub.cli list datasets --license-type <family>
```

For a loader with local data available:

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset("<slug>")
data_dir = Path("~/.eyedatahub/data").expanduser()
samples = ds.load(data_dir, split=(ds.info.splits or ["all"])[0])
print(len(samples), samples[0])
```

Do not bulk-download datasets for a PR unless the maintainer explicitly asks.

## PR preparation

Use `.claude/skills/add-dataset/NEW_DATASET_PR_TEMPLATE.md` as the
agent-fillable PR body. Complete every section that can be verified from the
source. Mark unknowns explicitly; do not hide uncertainty.

The PR should include:

- Source URL and citation.
- Exact license text, license family, and verification source.
- Duplicate/mirror/derivative assessment.
- Files changed and registration location.
- Loader status: full parser, download-only, manual/gated, or metadata-only.
- Smoke-test output.
- Any maintainer questions.

## Refuse or pause when

- The source is paid, private, scraped without permission, or not publicly
  discoverable.
- The user asks to guess a license or ignore conflicting source terms.
- The dataset appears to be a duplicate mirror with no new task or annotation.
- The requested implementation would bypass challenge, account, DUA, or
  institutional access controls.
