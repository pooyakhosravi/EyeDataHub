---
id: mm_retinal_reason
title: "MM-Retinal-Reason: Ophthalmology Multimodal Reasoning Dataset"
sidebar_label: mm_retinal_reason
description: "Ophthalmology-specific multimodal reasoning dataset built from 45 public datasets. Chain-of-thought reasoning traces for retinal VQA."
tags: ["multimodal", "fundus", "fundus_angiography", "oct", "text", "unknown", "huggingface", "classification", "multilabel"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# MM-Retinal-Reason: Ophthalmology Multimodal Reasoning Dataset

Ophthalmology-specific multimodal reasoning dataset built from 45 public datasets. Chain-of-thought reasoning traces for retinal VQA.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mm_retinal_reason` |
| **Full name** | MM-Retinal-Reason: Ophthalmology Multimodal Reasoning Dataset |
| **Primary category** | `multimodal` |
| **Contained modalities** | fundus, fundus_angiography, oct, text |
| **Tasks** | classification, multilabel |
| **Samples** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | train, val, test |
| **Size** | 15.0 GB |
| **Source-stated terms** | Mixed (inherits from 45 source datasets) — verify per-row |
| **Normalized terms** | `unknown` |
| **Descriptive screening label** | Unknown or unclear; do not assume permission |
| **Terms scope** | `mixed_components` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | HuggingFace Hub |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `transfer_tested_partial` |
| **Legacy sample-loader status** | Metadata and access only |


## Notes

> Aggregates 45 source datasets — image licenses inherit; verify per-row before commercial use.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mm_retinal_reason --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download mm_retinal_reason --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mm_retinal_reason')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [huggingface.co/datasets](https://huggingface.co/datasets/lxirich/MM-Retinal-Reason)

**Source-term evidence:** [huggingface.co/datasets](https://huggingface.co/datasets/lxirich/MM-Retinal-Reason)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mm_retinal_reason,
  title  = { MM-Retinal-Reason: Ophthalmology Multimodal Reasoning Dataset },
  note   = { MM-Retinal-Reason: Ophthalmology multimodal reasoning dataset. HuggingFace, 2025 },
  year   = { 2025 },
  url    = { https://huggingface.co/datasets/lxirich/MM-Retinal-Reason },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
MM-Retinal-Reason: Ophthalmology multimodal reasoning dataset. HuggingFace, 2025.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Mixed (inherits from 45 source datasets) — verify per-row
- **Normalized category:** `unknown`
- **Apparent scope:** `mixed_components`
- **Descriptive screening label:** Unknown or unclear; do not assume permission

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Related datasets with shared modalities

- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 records, `unknown`)
- [x_pcr](./x_pcr.md): X-PCR Ophthalmology Progressive Clinical Reasoning Benchmark (18,735 records, `unknown`)
- [ophthalvqa](./ophthalvqa.md): OphthalVQA Dataset (count not reported records, `cc-by`)
- [angioreport](./angioreport.md): AngioReport Fundus Angiography Report Dataset (55,361 records, `unknown`)
- [ffa_ir](./ffa_ir.md): FFA-IR Medical Report Dataset (47,247 records, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 records, `unknown`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (58,036 records, `mit`)
- [harvard_fairvision](./harvard_fairvision.md): Harvard-FairVision (AMD + DR + Glaucoma, paired SLO + OCT) (30,000 records, `cc-by-nc-nd`)
