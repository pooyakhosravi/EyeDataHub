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
| **Samples** | 155 |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 30.0 GB |
| **Source-stated terms** | CC BY-NC 4.0 |
| **Normalized terms** | `cc-by-nc` |
| **Descriptive screening label** | Explicit noncommercial clause recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Zenodo |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download sics155 --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download sics155 --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('sics155')
print(preflight_dataset(ds, './data'))  # no transfer
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

## Related datasets with shared modalities

- [ophora](./ophora.md): Ophora-160K: Ophthalmic Surgical Video Instruction Dataset (162,185 records, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 records, `unknown`)
- [cadis](./cadis.md): CaDIS: Cataract Dataset for Image Segmentation (4,670 records, `research-only`)
- [cataract_lmm](./cataract_lmm.md): Cataract-LMM: Large-Scale Multi-Source Multi-Task Cataract Surgery Benchmark (3,000 records, `cc-by-nc-nd`)
- [ophnet2024](./ophnet2024.md): OphNet2024: Ophthalmic Surgical Video Dataset (2,278 records, `cc-by-nc-sa`)
- [cataract1k](./cataract1k.md): Cataract-1K: Large-Scale Cataract Surgery Video Dataset (1,000 records, `research-only`)
- [migs_video](./migs_video.md): Multicenter Fine-Annotated MIGS Surgical Video Dataset (186 records, `cc-by`)
- [cataract101_extended_labels](./cataract101_extended_labels.md): Cataract-101 Extended Labels (101 records, `cc-by`)
