---
id: cadis
title: "CaDIS: Cataract Dataset for Image Segmentation"
sidebar_label: cadis
description: "Semantic segmentation labels for 4,670 frames from 25 cataract surgery videos (CATARACTS challenge). 25 anatomy and instrument classes."
tags: ["surgical_video", "research-only", "manual", "segmentation"]
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
| **Samples** | 4,670 |
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


## Notes

> Standard cataract-scene segmentation benchmark. Grand Challenge account required.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download cadis --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download cadis --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('cadis')
print(preflight_dataset(ds, './data'))  # no transfer
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

## Related datasets with shared modalities

- [ophora](./ophora.md): Ophora-160K: Ophthalmic Surgical Video Instruction Dataset (160,185 records, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 records, `unknown`)
- [cataract_lmm](./cataract_lmm.md): Cataract-LMM: Large-Scale Multi-Source Multi-Task Cataract Surgery Benchmark (3,000 records, `cc-by-nc-nd`)
- [ophnet2024](./ophnet2024.md): OphNet2024: Ophthalmic Surgical Video Dataset (2,278 records, `cc-by-nc-sa`)
- [cataract1k](./cataract1k.md): Cataract-1K: Large-Scale Cataract Surgery Video Dataset (1,000 records, `research-only`)
- [migs_video](./migs_video.md): Multicenter Fine-Annotated MIGS Surgical Video Dataset (186 records, `cc-by`)
- [sics155](./sics155.md): SICS-155 Small Incision Cataract Surgery Videos (155 records, `cc-by-nc`)
- [cataract101_extended_labels](./cataract101_extended_labels.md): Cataract-101 Extended Labels (101 records, `cc-by`)
