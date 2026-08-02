---
id: cataract_101
title: "Cataract-101: 101 Cataract Surgery Videos with Phase Annotations"
sidebar_label: cataract_101
description: "101 cataract surgery videos with 10-phase workflow annotations. Canonical older cataract benchmark."
tags: ["surgical_video", "research-only", "manual", "classification", "documented-relationship", "relationship-derived_from"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Cataract-101: 101 Cataract Surgery Videos with Phase Annotations

101 cataract surgery videos with 10-phase workflow annotations. Canonical older cataract benchmark.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `cataract_101` |
| **Full name** | Cataract-101: 101 Cataract Surgery Videos with Phase Annotations |
| **Primary category** | `surgical_video` |
| **Contained modalities** | surgical_video |
| **Tasks** | classification |
| **Primary reported quantity** | 101 videos |
| **Classes** | 10 (Not reported) |
| **Splits** | all |
| **Size** | 25.0 GB |
| **Source-stated terms** | Research only (ITEC AAU) |
| **Normalized terms** | `research-only` |
| **Descriptive screening label** | Research or challenge restriction recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `guided_instructions_only` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 101 | `videos` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [ftp.itec.aau.at/datasets](https://ftp.itec.aau.at/datasets/ovid/cat-101/) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> ITEC public FTP; license verify against institutional page.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- [cataract101_extended_labels](./cataract101_extended_labels.md) is `derived from` this record: The deposit provides extended labels for the Cataract-101 videos. ([evidence](https://zenodo.org/records/4984167))
- [insegcat](./insegcat.md) is `derived from` this record: InSegCat Dataset 1 selects and annotates frames from Cataract-101 videos. ([evidence](https://ftp.itec.aau.at/datasets/ovid/InSegCat/))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download cataract_101 --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download cataract_101 --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('cataract_101')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [ftp.itec.aau.at/datasets](https://ftp.itec.aau.at/datasets/ovid/cat-101/)

**Source-term evidence:** [ftp.itec.aau.at/datasets](https://ftp.itec.aau.at/datasets/ovid/cat-101/)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{cataract_101,
  title  = { Cataract-101: 101 Cataract Surgery Videos with Phase Annotations },
  note   = { Schoeffmann K, Taschwer M, Sarny S, Munzer B, Primus MJ, Putzgruber D, 'Cataract-101 — video dataset of 101 cataract surgeries', ACM MMSys 2018 },
  year   = { 2018 },
  url    = { https://ftp.itec.aau.at/datasets/ovid/cat-101/ },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Schoeffmann K, Taschwer M, Sarny S, Munzer B, Primus MJ, Putzgruber D, 'Cataract-101 — video dataset of 101 cataract surgeries', ACM MMSys 2018.
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
- [insegcat](./insegcat.md): InSegCat: Instance Segmentation for Cataract Surgery (5,581 annotated images, `research-only`)
- [cadis](./cadis.md): CaDIS: Cataract Dataset for Image Segmentation (4,670 images, `research-only`)
- [cataract_lmm](./cataract_lmm.md): Cataract-LMM: Large-Scale Multi-Source Multi-Task Cataract Surgery Benchmark (3,000 videos, `cc-by-nc-nd`)
- [ophnet2024](./ophnet2024.md): OphNet2024: Ophthalmic Surgical Video Dataset (2,278 videos, `cc-by-nc-sa`)
- [lmod_cataract_1k](./lmod_cataract_1k.md): LMOD-Cataract-1K (2,256 images, `cc-by`)
- [lmod_cataract_1k_cot](./lmod_cataract_1k_cot.md): Cataract-1K Surgical Analysis Chain-of-Thought Dataset (2,256 images, `mit`)
