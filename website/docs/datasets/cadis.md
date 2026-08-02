---
id: cadis
title: "CaDIS: Cataract Dataset for Image Segmentation"
sidebar_label: cadis
description: "Semantic segmentation labels for 4,670 frames from 25 cataract surgery videos (CATARACTS challenge). 25 anatomy and instrument classes."
tags: ["surgical_video", "research-only", "manual", "segmentation", "documented-relationship", "relationship-derived_from"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# CaDIS: Cataract Dataset for Image Segmentation

Semantic segmentation labels for 4,670 frames from 25 cataract surgery videos (CATARACTS challenge). 25 anatomy and instrument classes.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `cadis` |
| **Full name** | CaDIS: Cataract Dataset for Image Segmentation |
| **Primary category** | `surgical_video` |
| **Contained modalities** | surgical_video |
| **Tasks** | segmentation |
| **Primary reported quantity** | 4,670 images |
| **Classes** | 25 (Not reported) |
| **Splits** | train, val, test |
| **Size** | 15.0 GB |
| **Source-stated terms** | Research only (Grand Challenge terms) |
| **Normalized terms** | `research-only` |
| **Descriptive screening label** | Research or challenge restriction recorded; check source |
| **Terms scope** | `challenge_participation` |
| **Access friction** | `self_service_clickthrough` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `guided_instructions_only` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 4,670 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [cataracts-semantic-segmentation2020.grand-challenge.org](https://cataracts-semantic-segmentation2020.grand-challenge.org/) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Standard cataract-scene segmentation benchmark. Grand Challenge account required.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- [insegcat](./insegcat.md) is `derived from` this record: InSegCat Dataset 2 converts CaDIS semantic masks to instance masks and boxes. ([evidence](https://ftp.itec.aau.at/datasets/ovid/InSegCat/))
- This record is `derived from` [cataracts2017](./cataracts2017.md): CaDIS adds semantic segmentation labels to frames selected from CATARACTS videos. ([evidence](https://cataracts-semantic-segmentation2020.grand-challenge.org/))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download cadis --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download cadis --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('cadis')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [cataracts-semantic-segmentation2020.grand-challenge.org](https://cataracts-semantic-segmentation2020.grand-challenge.org/)

**Source-term evidence:** [cataracts-semantic-segmentation2020.grand-challenge.org](https://cataracts-semantic-segmentation2020.grand-challenge.org/)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{cadis,
  title  = { CaDIS: Cataract Dataset for Image Segmentation },
  note   = { Grammatikopoulou M, Flouty E, Kadkhodamohammadi A, et al., 'CaDIS: Cataract dataset for image segmentation', arXiv 1906.11586, 2019 },
  year   = { 1906 },
  url    = { https://cataracts-semantic-segmentation2020.grand-challenge.org/ },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Grammatikopoulou M, Flouty E, Kadkhodamohammadi A, et al., 'CaDIS: Cataract dataset for image segmentation', arXiv 1906.11586, 2019.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Research only (Grand Challenge terms)
- **Normalized category:** `research-only`
- **Apparent scope:** `challenge_participation`
- **Descriptive screening label:** Research or challenge restriction recorded; check source

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [ophora](./ophora.md): Ophora-160K: Ophthalmic Surgical Video Instruction Dataset (162,185 video clip instruction pairs, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [insegcat](./insegcat.md): InSegCat: Instance Segmentation for Cataract Surgery (5,581 annotated images, `research-only`)
- [cataract_lmm](./cataract_lmm.md): Cataract-LMM: Large-Scale Multi-Source Multi-Task Cataract Surgery Benchmark (3,000 videos, `cc-by-nc-nd`)
- [ophnet2024](./ophnet2024.md): OphNet2024: Ophthalmic Surgical Video Dataset (2,278 videos, `cc-by-nc-sa`)
- [lmod_cataract_1k](./lmod_cataract_1k.md): LMOD-Cataract-1K (2,256 images, `cc-by`)
- [lmod_cataract_1k_cot](./lmod_cataract_1k_cot.md): Cataract-1K Surgical Analysis Chain-of-Thought Dataset (2,256 images, `mit`)
- [cataract1k](./cataract1k.md): Cataract-1K: Large-Scale Cataract Surgery Video Dataset (1,000 videos, `research-only`)
