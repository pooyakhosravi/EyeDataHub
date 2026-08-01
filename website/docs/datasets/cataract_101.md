---
id: cataract_101
title: "Cataract-101: 101 Cataract Surgery Videos with Phase Annotations"
sidebar_label: cataract_101
description: "101 cataract surgery videos with 10-phase workflow annotations. Canonical older cataract benchmark."
tags: ["surgical_video", "research-only", "manual", "classification"]
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
| **Samples** | 101 |
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


## Notes

> ITEC public FTP; license verify against institutional page.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download cataract_101 --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download cataract_101 --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('cataract_101')
print(preflight_dataset(ds, './data'))  # no transfer
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

## Related datasets with shared modalities

- [ophora](./ophora.md): Ophora-160K: Ophthalmic Surgical Video Instruction Dataset (162,185 records, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 records, `unknown`)
- [cadis](./cadis.md): CaDIS: Cataract Dataset for Image Segmentation (4,670 records, `research-only`)
- [cataract_lmm](./cataract_lmm.md): Cataract-LMM: Large-Scale Multi-Source Multi-Task Cataract Surgery Benchmark (3,000 records, `cc-by-nc-nd`)
- [ophnet2024](./ophnet2024.md): OphNet2024: Ophthalmic Surgical Video Dataset (2,278 records, `cc-by-nc-sa`)
- [cataract1k](./cataract1k.md): Cataract-1K: Large-Scale Cataract Surgery Video Dataset (1,000 records, `research-only`)
- [migs_video](./migs_video.md): Multicenter Fine-Annotated MIGS Surgical Video Dataset (186 records, `cc-by`)
- [sics155](./sics155.md): SICS-155 Small Incision Cataract Surgery Videos (155 records, `cc-by-nc`)
