---
id: sics155
title: "SICS-155 Small Incision Cataract Surgery Videos"
sidebar_label: sics155
description: "Small-incision cataract surgery video dataset with train/validation/test video archives for phase-recognition research."
tags: ["surgical_video", "cc-by-nc", "zenodo", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# SICS-155 Small Incision Cataract Surgery Videos

Small-incision cataract surgery video dataset with train/validation/test video archives for phase-recognition research.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `sics155` |
| **Full name** | SICS-155 Small Incision Cataract Surgery Videos |
| **Primary category** | `surgical_video` |
| **Contained modalities** | surgical_video |
| **Tasks** | classification |
| **Primary reported quantity** | 155 videos |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 30.0 GB |
| **Source-stated terms** | CC BY-NC 4.0 |
| **Normalized terms** | `cc-by-nc` |
| **Descriptive screening label** | Explicit noncommercial clause recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Zenodo |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 155 | `videos` | SICS surgical videos | `official_source_description` | [zenodo.org/records](https://zenodo.org/records/19482928) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download sics155 --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download sics155 --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('sics155')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [zenodo.org/records](https://zenodo.org/records/19482928)

**Source-term evidence:** [zenodo.org/records](https://zenodo.org/records/19482928)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{sics155,
  title  = { SICS-155 Small Incision Cataract Surgery Videos },
  note   = { SICS-155 small incision cataract surgery videos. Zenodo, 2026. doi:10.5281/zenodo.19482928 },
  year   = { 2026 },
  url    = { https://zenodo.org/records/19482928 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
SICS-155 small incision cataract surgery videos. Zenodo, 2026. doi:10.5281/zenodo.19482928
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC BY-NC 4.0
- **Normalized category:** `cc-by-nc`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Explicit noncommercial clause recorded; check source

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [ophora](./ophora.md): Ophora-160K: Ophthalmic Surgical Video Instruction Dataset (162,185 video clip instruction pairs, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [insegcat](./insegcat.md): InSegCat: Instance Segmentation for Cataract Surgery (5,581 annotated images, `research-only`)
- [cadis](./cadis.md): CaDIS: Cataract Dataset for Image Segmentation (4,670 images, `research-only`)
- [cataract_lmm](./cataract_lmm.md): Cataract-LMM: Large-Scale Multi-Source Multi-Task Cataract Surgery Benchmark (3,000 videos, `cc-by-nc-nd`)
- [ophnet2024](./ophnet2024.md): OphNet2024: Ophthalmic Surgical Video Dataset (2,278 videos, `cc-by-nc-sa`)
- [lmod_cataract_1k](./lmod_cataract_1k.md): LMOD-Cataract-1K (2,256 images, `cc-by`)
- [lmod_cataract_1k_cot](./lmod_cataract_1k_cot.md): Cataract-1K Surgical Analysis Chain-of-Thought Dataset (2,256 images, `mit`)
