---
id: cataract101_extended_labels
title: "Cataract-101 Extended Labels"
sidebar_label: cataract101_extended_labels
description: "Extended phase/time labels for the Cataract-101 surgical-video dataset."
tags: ["surgical_video", "cc-by", "zenodo", "classification", "resource-role-annotation-layer", "dataset-family-cataract101-extended-labels", "documented-relationship", "relationship-derived_from"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Cataract-101 Extended Labels

Extended phase/time labels for the Cataract-101 surgical-video dataset.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `cataract101_extended_labels` |
| **Full name** | Cataract-101 Extended Labels |
| **Primary category** | `surgical_video` |
| **Resource role** | `annotation_layer` |
| **Dataset family** | `cataract101_extended_labels` |
| **Contained modalities** | surgical_video |
| **Tasks** | classification |
| **Primary reported quantity** | 101 videos |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.01 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Zenodo |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 101 | `videos` | Cataract-101 videos receiving extended labels | `official_source_description` | [zenodo.org/records](https://zenodo.org/records/4984167) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Derivative label layer for existing `cataract_101` images/videos.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- This record is `derived from` [cataract_101](./cataract_101.md): The deposit provides extended labels for the Cataract-101 videos. ([evidence](https://zenodo.org/records/4984167))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download cataract101_extended_labels --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download cataract101_extended_labels --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('cataract101_extended_labels')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [zenodo.org/records](https://zenodo.org/records/4984167)

**Source-term evidence:** [zenodo.org/records](https://zenodo.org/records/4984167)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{cataract101_extended_labels,
  title  = { Cataract-101 Extended Labels },
  note   = { Cataract101 extended labels. Zenodo, 2021. doi:10.5281/zenodo.4984167 },
  year   = { 2021 },
  url    = { https://zenodo.org/records/4984167 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Cataract101 extended labels. Zenodo, 2021. doi:10.5281/zenodo.4984167
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
- [lmod_cataract_1k](./lmod_cataract_1k.md): LMOD-Cataract-1K (2,256 images, `cc-by`)
- [lmod_cataract_1k_cot](./lmod_cataract_1k_cot.md): Cataract-1K Surgical Analysis Chain-of-Thought Dataset (2,256 images, `mit`)
