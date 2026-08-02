---
id: insegcat
title: "InSegCat: Instance Segmentation for Cataract Surgery"
sidebar_label: insegcat
description: "Two COCO-format instance-segmentation datasets derived from cataract surgery videos, covering instruments and anatomical structures."
tags: ["surgical_video", "research-only", "manual", "segmentation", "resource-role-annotation-layer", "dataset-family-insegcat", "documented-relationship", "relationship-derived_from"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# InSegCat: Instance Segmentation for Cataract Surgery

Two COCO-format instance-segmentation datasets derived from cataract surgery videos, covering instruments and anatomical structures.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `insegcat` |
| **Full name** | InSegCat: Instance Segmentation for Cataract Surgery |
| **Primary category** | `surgical_video` |
| **Resource role** | `annotation_layer` |
| **Dataset family** | `insegcat` |
| **Contained modalities** | surgical_video |
| **Tasks** | segmentation |
| **Primary reported quantity** | 5,581 annotated images |
| **Classes** | Not reported (Not reported) |
| **Splits** | train, test |
| **Size** | 10.0 GB |
| **Source-stated terms** | Research only (ITEC AAU) |
| **Normalized terms** | `research-only` |
| **Descriptive screening label** | Research or challenge restriction recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_clickthrough` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `guided_instructions_only` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 5,581 | `annotated_images` | Current Dataset 1 v2 plus Dataset 2 | `derived_from_reported_components` | [ftp.itec.aau.at/datasets](https://ftp.itec.aau.at/datasets/ovid/InSegCat/) |
| Additional | 843 | `annotated_images` | Dataset 1 v2, manually annotated Cataract-101 frames | `official_source_description` | [ftp.itec.aau.at/datasets](https://ftp.itec.aau.at/datasets/ovid/InSegCat/) |
| Additional | 4,738 | `annotated_images` | Dataset 2, CaDIS-derived annotations | `official_source_description` | [ftp.itec.aau.at/datasets](https://ftp.itec.aau.at/datasets/ovid/InSegCat/) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- This record is `derived from` [cadis](./cadis.md): InSegCat Dataset 2 converts CaDIS semantic masks to instance masks and boxes. ([evidence](https://ftp.itec.aau.at/datasets/ovid/InSegCat/))
- This record is `derived from` [cataract_101](./cataract_101.md): InSegCat Dataset 1 selects and annotates frames from Cataract-101 videos. ([evidence](https://ftp.itec.aau.at/datasets/ovid/InSegCat/))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download insegcat --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download insegcat --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('insegcat')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [ftp.itec.aau.at/datasets](https://ftp.itec.aau.at/datasets/ovid/InSegCat/)

**Source-term evidence:** [ftp.itec.aau.at/datasets](https://ftp.itec.aau.at/datasets/ovid/InSegCat/)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{insegcat,
  title  = { InSegCat: Instance Segmentation for Cataract Surgery },
  note   = { InSegCat dataset, ITEC AAU. COCO-format instance segmentation for cataract surgery },
  url    = { https://ftp.itec.aau.at/datasets/ovid/InSegCat/ },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
InSegCat dataset, ITEC AAU. COCO-format instance segmentation for cataract surgery.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Research only (ITEC AAU)
- **Normalized category:** `research-only`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Research or challenge restriction recorded; check source

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [ophora](./ophora.md): Ophora-160K: Ophthalmic Surgical Video Instruction Dataset (162,185 video clip instruction pairs, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [cadis](./cadis.md): CaDIS: Cataract Dataset for Image Segmentation (4,670 images, `research-only`)
- [cataract_lmm](./cataract_lmm.md): Cataract-LMM: Large-Scale Multi-Source Multi-Task Cataract Surgery Benchmark (3,000 videos, `cc-by-nc-nd`)
- [ophnet2024](./ophnet2024.md): OphNet2024: Ophthalmic Surgical Video Dataset (2,278 videos, `cc-by-nc-sa`)
- [lmod_cataract_1k](./lmod_cataract_1k.md): LMOD-Cataract-1K (2,256 images, `cc-by`)
- [lmod_cataract_1k_cot](./lmod_cataract_1k_cot.md): Cataract-1K Surgical Analysis Chain-of-Thought Dataset (2,256 images, `mit`)
- [cataract1k](./cataract1k.md): Cataract-1K: Large-Scale Cataract Surgery Video Dataset (1,000 videos, `research-only`)
