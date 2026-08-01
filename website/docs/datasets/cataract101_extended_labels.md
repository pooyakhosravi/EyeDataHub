---
id: cataract101_extended_labels
title: "Cataract-101 Extended Labels"
sidebar_label: cataract101_extended_labels
description: "Extended phase/time labels for the Cataract-101 surgical-video dataset."
tags: ["surgical_video", "cc-by", "zenodo", "classification"]
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
| **Contained modalities** | surgical_video |
| **Tasks** | classification |
| **Samples** | 101 |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.01 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Zenodo |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Notes

> Derivative label layer for existing `cataract_101` images/videos.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download cataract101_extended_labels --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download cataract101_extended_labels --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('cataract101_extended_labels')
print(preflight_dataset(ds, './data'))  # no transfer
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

## Related datasets with shared modalities

- [ophora](./ophora.md): Ophora-160K: Ophthalmic Surgical Video Instruction Dataset (162,185 records, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 records, `unknown`)
- [cadis](./cadis.md): CaDIS: Cataract Dataset for Image Segmentation (4,670 records, `research-only`)
- [cataract_lmm](./cataract_lmm.md): Cataract-LMM: Large-Scale Multi-Source Multi-Task Cataract Surgery Benchmark (3,000 records, `cc-by-nc-nd`)
- [ophnet2024](./ophnet2024.md): OphNet2024: Ophthalmic Surgical Video Dataset (2,278 records, `cc-by-nc-sa`)
- [cataract1k](./cataract1k.md): Cataract-1K: Large-Scale Cataract Surgery Video Dataset (1,000 records, `research-only`)
- [migs_video](./migs_video.md): Multicenter Fine-Annotated MIGS Surgical Video Dataset (186 records, `cc-by`)
- [sics155](./sics155.md): SICS-155 Small Incision Cataract Surgery Videos (155 records, `cc-by-nc`)
