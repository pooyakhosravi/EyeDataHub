---
id: lmod_cataract_1k
title: "LMOD-Cataract-1K"
sidebar_label: lmod_cataract_1k
description: "Processed Cataract-1K surgical-frame dataset for segmentation/object-detection workflows."
tags: ["surgical_video", "cc-by", "huggingface", "segmentation", "detection", "documented-relationship", "relationship-derived_from"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# LMOD-Cataract-1K

Processed Cataract-1K surgical-frame dataset for segmentation/object-detection workflows.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `lmod_cataract_1k` |
| **Full name** | LMOD-Cataract-1K |
| **Primary category** | `surgical_video` |
| **Contained modalities** | surgical_video |
| **Tasks** | segmentation, detection |
| **Primary reported quantity** | 2,256 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 2.0 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | HuggingFace Hub |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 2,256 | `images` | Rows in the versioned Hugging Face deposit | `current_deposit_table` | [huggingface.co/datasets](https://huggingface.co/datasets/mehti/LMOD-Cataract-1K) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Derivative/processed view of existing Cataract-1K.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- [lmod_cataract_1k_cot](./lmod_cataract_1k_cot.md) is `derived from` this record: The dataset card identifies LMOD-Cataract-1K as its image source. ([evidence](https://huggingface.co/datasets/mehti/LMOD-Cataract-1K-surgical-analysis-cot))
- This record is `derived from` [cataract1k](./cataract1k.md): The dataset card identifies Cataract-1K as the source of the processed surgical frames. ([evidence](https://huggingface.co/datasets/mehti/LMOD-Cataract-1K))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download lmod_cataract_1k --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download lmod_cataract_1k --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('lmod_cataract_1k')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [huggingface.co/datasets](https://huggingface.co/datasets/mehti/LMOD-Cataract-1K)

**Source-term evidence:** [huggingface.co/datasets](https://huggingface.co/datasets/mehti/LMOD-Cataract-1K)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{lmod_cataract_1k,
  title  = { LMOD-Cataract-1K },
  note   = { mehti/LMOD-Cataract-1K. Hugging Face dataset, accessed 2026-07 },
  year   = { 2026 },
  url    = { https://huggingface.co/datasets/mehti/LMOD-Cataract-1K },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
mehti/LMOD-Cataract-1K. Hugging Face dataset, accessed 2026-07.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC BY 4.0
- **Normalized category:** `cc-by`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Standard label without an explicit NC clause; not a permission finding

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [ophora](./ophora.md): Ophora-160K: Ophthalmic Surgical Video Instruction Dataset (162,185 video clip instruction pairs, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [insegcat](./insegcat.md): InSegCat: Instance Segmentation for Cataract Surgery (5,581 annotated images, `research-only`)
- [cadis](./cadis.md): CaDIS: Cataract Dataset for Image Segmentation (4,670 images, `research-only`)
- [cataract_lmm](./cataract_lmm.md): Cataract-LMM: Large-Scale Multi-Source Multi-Task Cataract Surgery Benchmark (3,000 videos, `cc-by-nc-nd`)
- [ophnet2024](./ophnet2024.md): OphNet2024: Ophthalmic Surgical Video Dataset (2,278 videos, `cc-by-nc-sa`)
- [lmod_cataract_1k_cot](./lmod_cataract_1k_cot.md): Cataract-1K Surgical Analysis Chain-of-Thought Dataset (2,256 images, `mit`)
- [cataract1k](./cataract1k.md): Cataract-1K: Large-Scale Cataract Surgery Video Dataset (1,000 videos, `research-only`)
