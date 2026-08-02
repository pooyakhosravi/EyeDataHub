---
id: cataract_lmm
title: "Cataract-LMM: Large-Scale Multi-Source Multi-Task Cataract Surgery Benchmark"
sidebar_label: cataract_lmm
description: "3,000 cataract surgery procedures, 1,134.2 hours of video with phase annotations, instance segmentation, tracking, and skill scoring. Largest public cataract-surgery-video resource."
tags: ["surgical_video", "cc-by-nc-nd", "huggingface", "classification", "segmentation", "multilabel"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Cataract-LMM: Large-Scale Multi-Source Multi-Task Cataract Surgery Benchmark

3,000 cataract surgery procedures, 1,134.2 hours of video with phase annotations, instance segmentation, tracking, and skill scoring. Largest public cataract-surgery-video resource.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `cataract_lmm` |
| **Full name** | Cataract-LMM: Large-Scale Multi-Source Multi-Task Cataract Surgery Benchmark |
| **Primary category** | `surgical_video` |
| **Contained modalities** | surgical_video |
| **Tasks** | classification, segmentation, multilabel |
| **Primary reported quantity** | 3,000 videos |
| **Classes** | Not reported (Not reported) |
| **Splits** | train, val, test |
| **Size** | 200.0 GB |
| **Source-stated terms** | CC BY-NC-ND 4.0 |
| **Normalized terms** | `cc-by-nc-nd` |
| **Descriptive screening label** | Explicit noncommercial clause recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | HuggingFace Hub |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 3,000 | `videos` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [huggingface.co/datasets](https://huggingface.co/datasets/mjahmadi/Cataract-LMM) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Largest public cataract-surgery-video resource by hours. CC BY-NC-ND 4.0 — non-commercial + no derivatives on HF.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download cataract_lmm --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download cataract_lmm --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('cataract_lmm')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [huggingface.co/datasets](https://huggingface.co/datasets/mjahmadi/Cataract-LMM)

**Source-term evidence:** [huggingface.co/datasets](https://huggingface.co/datasets/mjahmadi/Cataract-LMM)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{cataract_lmm,
  title  = { Cataract-LMM: Large-Scale Multi-Source Multi-Task Cataract Surgery Benchmark },
  note   = { Ahmadi MJ, Gandomi I, Abdi P, et al., 'Cataract-LMM: Large-scale multi-source multi-task benchmark for deep learning in surgical video analysis', Scientific Data 2026. doi:10.1038/s41597-026-07464-0 },
  year   = { 2026 },
  url    = { https://huggingface.co/datasets/mjahmadi/Cataract-LMM },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Ahmadi MJ, Gandomi I, Abdi P, et al., 'Cataract-LMM: Large-scale multi-source multi-task benchmark for deep learning in surgical video analysis', Scientific Data 2026. doi:10.1038/s41597-026-07464-0
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC BY-NC-ND 4.0
- **Normalized category:** `cc-by-nc-nd`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Explicit noncommercial clause recorded; check source

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [ophora](./ophora.md): Ophora-160K: Ophthalmic Surgical Video Instruction Dataset (162,185 video clip instruction pairs, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [insegcat](./insegcat.md): InSegCat: Instance Segmentation for Cataract Surgery (5,581 annotated images, `research-only`)
- [cadis](./cadis.md): CaDIS: Cataract Dataset for Image Segmentation (4,670 images, `research-only`)
- [ophnet2024](./ophnet2024.md): OphNet2024: Ophthalmic Surgical Video Dataset (2,278 videos, `cc-by-nc-sa`)
- [lmod_cataract_1k](./lmod_cataract_1k.md): LMOD-Cataract-1K (2,256 images, `cc-by`)
- [lmod_cataract_1k_cot](./lmod_cataract_1k_cot.md): Cataract-1K Surgical Analysis Chain-of-Thought Dataset (2,256 images, `mit`)
- [cataract1k](./cataract1k.md): Cataract-1K: Large-Scale Cataract Surgery Video Dataset (1,000 videos, `research-only`)
