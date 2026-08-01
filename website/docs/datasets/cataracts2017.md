---
id: cataracts2017
title: "CATARACTS 2017: Surgical Tool Detection Challenge"
sidebar_label: cataracts2017
description: "50 cataract surgery videos (>9 hours total) with frame-level annotations of 21 surgical tools. Earlier and larger sibling to Cataract-1K."
tags: ["surgical_video", "cc-by", "manual", "classification", "multilabel"]
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
| **Samples** | 50 |
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


## Notes

> IEEE DataPort free account login required.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download cataracts2017 --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download cataracts2017 --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('cataracts2017')
print(preflight_dataset(ds, './data'))  # no transfer
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

## Related datasets with shared modalities

- [ophora](./ophora.md): Ophora-160K: Ophthalmic Surgical Video Instruction Dataset (162,185 records, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 records, `unknown`)
- [cadis](./cadis.md): CaDIS: Cataract Dataset for Image Segmentation (4,670 records, `research-only`)
- [cataract_lmm](./cataract_lmm.md): Cataract-LMM: Large-Scale Multi-Source Multi-Task Cataract Surgery Benchmark (3,000 records, `cc-by-nc-nd`)
- [ophnet2024](./ophnet2024.md): OphNet2024: Ophthalmic Surgical Video Dataset (2,278 records, `cc-by-nc-sa`)
- [cataract1k](./cataract1k.md): Cataract-1K: Large-Scale Cataract Surgery Video Dataset (1,000 records, `research-only`)
- [migs_video](./migs_video.md): Multicenter Fine-Annotated MIGS Surgical Video Dataset (186 records, `cc-by`)
- [sics155](./sics155.md): SICS-155 Small Incision Cataract Surgery Videos (155 records, `cc-by-nc`)
