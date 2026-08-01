---
id: multieye
title: "MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark"
sidebar_label: multieye
description: "58,036 fundus + 45,923 OCT images assembled for multi-disease classification (8 classes) with cross-modal distillation. Sourced from multiple public ophthalmic datasets."
tags: ["multimodal", "fundus", "oct", "mit", "huggingface", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark

58,036 fundus + 45,923 OCT images assembled for multi-disease classification (8 classes) with cross-modal distillation. Sourced from multiple public ophthalmic datasets.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `multieye` |
| **Full name** | MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark |
| **Primary category** | `multimodal` |
| **Contained modalities** | fundus, oct |
| **Tasks** | classification |
| **Samples** | 58,036 |
| **Classes** | 8 (Not reported) |
| **Splits** | train, val, test |
| **Size** | 27.3 GB |
| **Source-stated terms** | MIT |
| **Normalized terms** | `mit` |
| **Descriptive screening label** | Standard label without an explicit NC clause; verify that it applies to data |
| **Terms scope** | `unknown` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | HuggingFace Hub |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Notes

> Re-aggregates several source datasets — image licenses inherit from their original sources. Verify per-component before reuse.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download multieye --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download multieye --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('multieye')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [huggingface.co/datasets](https://huggingface.co/datasets/Luxuriant16/MultiEYE)

**Source-term evidence:** [huggingface.co/datasets](https://huggingface.co/datasets/Luxuriant16/MultiEYE)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{multieye,
  title  = { MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark },
  note   = { MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark, IEEE TMI 2025; arXiv:2412.09402 },
  year   = { 2025 },
  url    = { https://huggingface.co/datasets/Luxuriant16/MultiEYE },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark, IEEE TMI 2025; arXiv:2412.09402
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** MIT
- **Normalized category:** `mit`
- **Apparent scope:** `unknown`
- **Descriptive screening label:** Standard label without an explicit NC clause; verify that it applies to data

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Related datasets with shared modalities

- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 records, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 records, `unknown`)
- [harvard_fairvision](./harvard_fairvision.md): Harvard-FairVision (AMD + DR + Glaucoma, paired SLO + OCT) (30,000 records, `cc-by-nc-nd`)
- [mmrdr](./mmrdr.md): MMRDR: Multi-Modal Retinal Diabetic Retinopathy Dataset (24,460 records, `cc-by`)
- [x_pcr](./x_pcr.md): X-PCR Ophthalmology Progressive Clinical Reasoning Benchmark (18,735 records, `unknown`)
- [olives](./olives.md): OLIVES: Ophthalmic Labels for Investigating Visual Eye Semantics (9,408 records, `cc-by`)
- [oct_fundus_dme_dr_mexico](./oct_fundus_dme_dr_mexico.md): OCT and Eye Fundus Dataset for DME and DR (2,661 records, `unknown`)
- [grape](./grape.md): GRAPE: Glaucoma Real-world Appraisal Progression Ensemble (1,115 records, `cc0`)
