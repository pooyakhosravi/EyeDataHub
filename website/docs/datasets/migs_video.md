---
id: migs_video
title: "Multicenter Fine-Annotated MIGS Surgical Video Dataset"
sidebar_label: migs_video
description: "A multicenter collection of 186 minimally invasive glaucoma surgery (MIGS) videos with annotations for surgical-phase recognition and semantic segmentation of instruments and anatomical structures."
tags: ["surgical_video", "cc-by", "zenodo", "classification", "segmentation"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Multicenter Fine-Annotated MIGS Surgical Video Dataset

A multicenter collection of 186 minimally invasive glaucoma surgery (MIGS) videos with annotations for surgical-phase recognition and semantic segmentation of instruments and anatomical structures.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `migs_video` |
| **Full name** | Multicenter Fine-Annotated MIGS Surgical Video Dataset |
| **Primary category** | `surgical_video` |
| **Contained modalities** | surgical_video |
| **Tasks** | classification, segmentation |
| **Samples** | 186 |
| **Classes** | Not reported (Not reported) |
| **Splits** | train, val, test |
| **Size** | 10.23 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Zenodo |
| **Availability** | `available` (checked 2026-07-25) |
| **Acquisition support** | `transfer_tested_partial` |
| **Legacy sample-loader status** | Metadata and access only |


## Notes

> The current Zenodo version is 10.5281/zenodo.19438128 under CC BY 4.0; the version-independent concept DOI is 10.5281/zenodo.18231908. The associated article cites the earlier deposit version 10.5281/zenodo.18231909.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download migs_video --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download migs_video --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('migs_video')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [zenodo.org/records](https://zenodo.org/records/19438128)

**Source-term evidence:** [zenodo.org/records](https://zenodo.org/records/19438128)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{migs_video,
  title  = { Multicenter Fine-Annotated MIGS Surgical Video Dataset },
  note   = { Wang D, Zhang Y, Li Y, et al., 'Multicenter fine annotated surgical video dataset for minimally invasive glaucoma surgery', Scientific Data 2026. doi:10.1038/s41597-026-07535-2 },
  year   = { 2026 },
  url    = { https://zenodo.org/records/19438128 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Wang D, Zhang Y, Li Y, et al., 'Multicenter fine annotated surgical video dataset for minimally invasive glaucoma surgery', Scientific Data 2026. doi:10.1038/s41597-026-07535-2
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
- [sics155](./sics155.md): SICS-155 Small Incision Cataract Surgery Videos (155 records, `cc-by-nc`)
- [cataract101_extended_labels](./cataract101_extended_labels.md): Cataract-101 Extended Labels (101 records, `cc-by`)
