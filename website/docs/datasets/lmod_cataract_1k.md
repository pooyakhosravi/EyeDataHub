---
id: lmod_cataract_1k
title: "LMOD-Cataract-1K"
sidebar_label: lmod_cataract_1k
description: "Processed Cataract-1K surgical-frame dataset for segmentation/object-detection workflows."
tags: ["surgical_video", "cc-by", "huggingface", "segmentation", "detection"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# LMOD-Cataract-1K

Processed Cataract-1K surgical-frame dataset for segmentation/object-detection workflows.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `lmod_cataract_1k` |
| **Full name** | LMOD-Cataract-1K |
| **Primary category** | `surgical_video` |
| **Contained modalities** | surgical_video |
| **Tasks** | segmentation, detection |
| **Samples** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 2.0 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | HuggingFace Hub |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Notes

> Derivative/processed view of existing Cataract-1K.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download lmod_cataract_1k --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download lmod_cataract_1k --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('lmod_cataract_1k')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [huggingface.co/datasets](https://huggingface.co/datasets/mehti/LMOD-Cataract-1K)

**Source-term evidence:** [huggingface.co/datasets](https://huggingface.co/datasets/mehti/LMOD-Cataract-1K)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{lmod_cataract_1k,
  title  = { LMOD-Cataract-1K },
  note   = { mehti/LMOD-Cataract-1K. Hugging Face dataset, accessed 2026-07 },
  year   = { 2026 },
  url    = { https://huggingface.co/datasets/mehti/LMOD-Cataract-1K },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
mehti/LMOD-Cataract-1K. Hugging Face dataset, accessed 2026-07.
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
