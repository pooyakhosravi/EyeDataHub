# Contributing to EyeDataHub

EyeDataHub grows through reviewed corrections, new ophthalmic catalog records,
loader improvements, documentation, and validation evidence. A resource may be
anonymous, self-service, controlled, author-contact, unavailable, or
unverified; do not call every included resource public or downloadable.

Use `eyedatahub` for Python imports and `eyehub` for CLI examples.

## Table Of Contents

- [Add a new dataset](#add-a-new-dataset)
- [Verify a dataset's license](#verify-a-datasets-license)
- [Test before opening a PR](#test-before-opening-a-pr)
- [Open a PR](#open-a-pr)
- [AI-agent workflow](#ai-agent-workflow)
- [Code style](#code-style)
- [Other contributions](#other-contributions)

## Add A New Dataset

### 1. Open an issue first

Open a New Dataset issue from the GitHub issue templates. This catches
duplicates and lets maintainers flag licensing concerns before implementation.

Before editing code, check whether the dataset or a derivative is already in
the catalog:

```bash
eyehub search --json
eyehub show <possible_slug> --json
```

If `eyehub` is not installed in your environment, use the module form:

```bash
python -m eyedatahub.cli list datasets --json
python -m eyedatahub.cli show <possible_slug> --json
```

### 2. Gather source metadata

Record metadata from the official source page, paper, DOI record, challenge
page, repository, or institutional landing page. Do not use a mirror when the
original source is available.

Required fields for review:

| Field | Notes |
|---|---|
| `name` | Stable snake_case slug. |
| `full_name` | Human-readable dataset name. |
| `description` | One or two precise sentences. |
| `primary_category` / `modalities` | Use one navigation category and every contained modality. Multimodal records must remain retrievable through their components. |
| `tasks` | Examples: `classification`, `grading`, `segmentation`, `multilabel`, `regression`, `progression`, `quality`, `registration`, `vqa`, `report_generation`. |
| `num_samples` | Source-reported count and unit. Use `None` only when unavailable. |
| `splits` | Official splits, or `["all"]` if no official split is documented. |
| `classes` / `num_classes` | Use `None` when not applicable. |
| `download_type` | Existing backend or access type such as `direct`, `kaggle`, `huggingface`, `zenodo`, `mendeley`, `figshare`, `dryad`, `manual`, or `gdrive`. |
| `download_url` | Official source URL or DOI URL. |
| `license` | Exact source text, not a guess. |
| `terms_scope` / `terms_evidence_url` | State whether terms apply to dataset files, metadata, code, publication, challenge participation, mixed components, or remain unknown. |
| `access_friction` | One granular current-route category; keep it independent from loader support. |
| Access flags | Record registration, authentication, token, click-through, manual approval, DUA, author contact, and payment as true, false, or unknown. |
| `availability_status` / route check | Record verification date, level, result, and limitations. |
| `acquisition_support` | Complete, partial, implemented-not-live-tested, platform-supported, guided, blocked, unsupported, or unavailable. |
| Typed identifiers | Keep dataset DOI/accession, repository identifier, article DOI, software DOI, and challenge identifier separate. |
| `citation` | Dataset citation and associated publication citation, identified separately. |
| `tags` | Lowercase tags useful for filtering. |
| `relationships` / `notes` | Typed mirror, derivation, version, supplement, and overlap relationships plus remaining caveats. |

### 3. Add a dataset class

Add the class to the closest existing module in `eyedatahub/datasets/`.

| Dataset type | Typical module |
|---|---|
| Fundus DR / lesions | `fundus_dr.py` |
| Fundus glaucoma | `fundus_glaucoma.py` |
| Fundus AMD | `fundus_amd.py` |
| Fundus vessels | `fundus_vessels.py` |
| Fundus misc / multi-disease | `fundus_misc.py` or `fundus_multi.py` |
| OCT / OCTA classification | `oct_datasets.py` |
| OCT segmentation | `oct_segmentation.py` |
| Ultra-widefield fundus | `uwf_datasets.py` |
| Surgical video | `surgical_datasets.py` |
| Visual field | `visual_field.py` |
| Confocal microscopy | `confocal.py` |
| Challenge collections | `ichallenge_datasets.py` or `stage_challenge.py` |
| Recent/community metadata-only additions | `community_recent.py`, `community_2026.py`, or `platform_2026.py` |

Use the current class-based catalog pattern. Do not add new datasets to a
YAML catalog.

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
            notes="Access caveat, duplicate relationship, or parser limitation.",
        )

    def download(self, data_dir: Union[str, Path]) -> None:
        print_manual_download_instructions(
            self.info.full_name,
            self.info.download_url,
            Path(data_dir) / self._SUBDIR,
        )
```

If the dataset has a real parser or downloader, copy the closest implemented
loader. If it is gated, manual, or parser support is not ready, use a manual or
metadata-only pattern and make the limitation explicit in `notes`.

### 4. Register it

Edit `eyedatahub/datasets/registry.py` (the internal class retains its
historical technical name):

- Import the new class inside `_register_all()`.
- Instantiate it in the `datasets = [...]` list under the appropriate section.
- Keep related datasets grouped and readable.

If the dataset changes the catalog size, update
`tests/test_smoke.py::EXPECTED_DATASET_COUNT`.

### 5. Update generated surfaces

Run these when the PR includes generated docs or catalog snapshots:

```bash
python -m hub.docs.generate_dataset_pages --out website/docs
python -m hub.docs.generate_llms_full
```

If the dataset should be included in a redistribution mirror, update
`hub/label_schema.json` only when the labels/classes are understood and the
source documentation explicitly authorizes redistribution for that component.
Do not add restricted datasets to mirrors.

## Verify A Dataset's License

Source-term verification and scope recording are mandatory.

- Find the official source license: dataset page, DOI record, challenge rules,
  repository `LICENSE`, paper data-availability statement, or bundle terms.
- Preserve the exact source string and evidence URL; record its apparent scope.
- Confirm `info.license_family` maps to one of `cc0`, `cc-by`, `cc-by-sa`,
  `mit`, `apache`, `cc-by-nc`, `cc-by-nc-sa`, `cc-by-nc-nd`,
  `research-only`, or `unknown`.
- Never inherit a code, publication, website, or challenge licence as the
  dataset-file licence. Represent component differences explicitly.
- If a mirror has different terms from the official source, preserve both
  pieces of evidence and keep the official route preferred.
- If no explicit license is found, use `license="Unknown"` and add a `notes`
  explanation. Do not guess.

EyeDataHub reports source documentation; it does not make a legal
determination. If a source term or scope appears wrong, open an evidence-backed
issue or pull request.

## Test Before Opening A PR

Install in editable mode if needed:

```bash
pip install -e ".[full]"
```

Run at least:

```bash
python -m pytest -q
python -m eyedatahub.cli list datasets --json
python -m eyedatahub.cli show <slug> --json
python -m eyedatahub.cli search --source-terms <license_family> --json
python -m eyedatahub.cli download <slug> --dry-run --json
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

If the dataset is large, gated, or manual-access, do not download it for the PR
unless a maintainer asks. The PR should still verify that the class imports,
appears in the catalog, and exposes correct metadata.

## Open A PR

1. Fork, branch, commit, and push.
2. Open a PR against `main`.
3. For dataset PRs, complete `.github/PULL_REQUEST_TEMPLATE.md`. Agent-assisted
   PRs should also fill `.claude/skills/add-dataset/NEW_DATASET_PR_TEMPLATE.md`
   or paste that information into the PR body.
4. CI runs import, schema, command, metadata, citation, and loader tests. Heavy
   downloads are not expected in CI.
5. Reviewers will check field-level provenance, terms scope, access flags,
   identifiers, relationships, catalog integration, and loader behavior.

## AI-Agent Workflow

EyeDataHub is designed to be usable by coding agents such as Codex, Claude
Code, Cursor, Aider, Cline, and Continue.

1. Read `CLAUDE.md` first. It is the canonical repository guide.
2. For dataset additions, use `.claude/skills/add-dataset/SKILL.md`.
3. Fill `.claude/skills/add-dataset/NEW_DATASET_PR_TEMPLATE.md` before opening
   a dataset PR.
4. For license-sensitive dataset selection, use `.claude/skills/license-filter/`.
5. Run the smoke-test commands above before asking a maintainer to review.

## Code Style

- Keep edits scoped to the requested change.
- Use current package names: `eyedatahub` and `eyehub`.
- Use type hints for public APIs.
- Add comments only when they clarify non-obvious behavior.
- Avoid new top-level dependencies without discussion. Optional features belong
  in `[project.optional-dependencies]` in `pyproject.toml`.
- Run `ruff check` and `ruff format` when touching Python code.

## Other Contributions

| Change type | Where to start |
|---|---|
| Bug fix | Open an issue with reproduction, then a PR. |
| Dataset metadata correction | Edit the relevant `eyedatahub/datasets/*.py` class and add source evidence. |
| New downloader backend | `eyedatahub/datasets/download_utils.py` |
| Website/docs update | `website/`, `docs/`, or generated docs under `hub/docs/` workflows. |
| URL audit update | `hub/audit/` and `.github/workflows/url-audit.yml` |
| Release a new version | Maintainers only: bump `pyproject.toml`, update `CHANGELOG.md`, and tag. |

Thanks for contributing.
