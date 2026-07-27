---
id: insegcat
title: "InSegCat: Instance Segmentation for Cataract Surgery"
sidebar_label: insegcat
description: "Two COCO-format instance-segmentation datasets derived from cataract surgery videos, covering instruments and anatomical structures."
tags: ["surgical_video", "research-only", "manual", "segmentation"]
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
| **Contained modalities** | surgical_video |
| **Tasks** | segmentation |
| **Samples** | Not reported |
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


## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download insegcat --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download insegcat --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('insegcat')
print(preflight_dataset(ds, './data'))  # no transfer
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

## Related datasets with shared modalities

- [ophora](./ophora.md): Ophora-160K: Ophthalmic Surgical Video Instruction Dataset (160,185 records, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 records, `unknown`)
- [cadis](./cadis.md): CaDIS: Cataract Dataset for Image Segmentation (4,670 records, `research-only`)
- [cataract_lmm](./cataract_lmm.md): Cataract-LMM: Large-Scale Multi-Source Multi-Task Cataract Surgery Benchmark (3,000 records, `cc-by-nc-nd`)
- [ophnet2024](./ophnet2024.md): OphNet2024: Ophthalmic Surgical Video Dataset (2,278 records, `cc-by-nc-sa`)
- [cataract1k](./cataract1k.md): Cataract-1K: Large-Scale Cataract Surgery Video Dataset (1,000 records, `research-only`)
- [migs_video](./migs_video.md): Multicenter Fine-Annotated MIGS Surgical Video Dataset (186 records, `cc-by`)
- [sics155](./sics155.md): SICS-155 Small Incision Cataract Surgery Videos (155 records, `cc-by-nc`)
