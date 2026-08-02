---
id: cataracts2017
title: "CATARACTS 2017: Surgical Tool Detection Challenge"
sidebar_label: cataracts2017
description: "50 cataract surgery videos (>9 hours total) with frame-level annotations of 21 surgical tools. Earlier and larger sibling to Cataract-1K."
tags: ["surgical_video", "cc-by", "manual", "classification", "multilabel", "documented-relationship", "relationship-derived_from"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# CATARACTS 2017: Surgical Tool Detection Challenge

50 cataract surgery videos (&gt;9 hours total) with frame-level annotations of 21 surgical tools. Earlier and larger sibling to Cataract-1K.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `cataracts2017` |
| **Full name** | CATARACTS 2017: Surgical Tool Detection Challenge |
| **Primary category** | `surgical_video` |
| **Contained modalities** | surgical_video |
| **Tasks** | classification, multilabel |
| **Primary reported quantity** | 50 videos |
| **Classes** | 21 (Not reported) |
| **Splits** | train, test |
| **Size** | 50.0 GB |
| **Source-stated terms** | CC BY 4.0 (IEEE DataPort) |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `guided_instructions_only` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 50 | `videos` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [ieee-dataport.org/open-access](https://ieee-dataport.org/open-access/cataracts) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> IEEE DataPort free account login required.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- [cadis](./cadis.md) is `derived from` this record: CaDIS adds semantic segmentation labels to frames selected from CATARACTS videos. ([evidence](https://cataracts-semantic-segmentation2020.grand-challenge.org/))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download cataracts2017 --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download cataracts2017 --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('cataracts2017')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [ieee-dataport.org/open-access](https://ieee-dataport.org/open-access/cataracts)

**Source-term evidence:** [ieee-dataport.org/open-access](https://ieee-dataport.org/open-access/cataracts)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{cataracts2017,
  title  = { CATARACTS 2017: Surgical Tool Detection Challenge },
  note   = { Al Hajj et al., 'CATARACTS: Challenge on Automatic Tool Annotation for cataRACT Surgery', Medical Image Analysis 2019 },
  year   = { 2019 },
  url    = { https://ieee-dataport.org/open-access/cataracts },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Al Hajj et al., 'CATARACTS: Challenge on Automatic Tool Annotation for cataRACT Surgery', Medical Image Analysis 2019.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC BY 4.0 (IEEE DataPort)
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
