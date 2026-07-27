---
id: retinal_corrugations_oct
title: "Outer Retinal Corrugations Imaging Dataset"
sidebar_label: retinal_corrugations_oct
description: "High-resolution swept-source OCT images and mechanical-model data for outer retinal corrugations in rhegmatogenous retinal detachment."
tags: ["oct", "cc-by", "mendeley", "segmentation", "regression"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Outer Retinal Corrugations Imaging Dataset

High-resolution swept-source OCT images and mechanical-model data for outer retinal corrugations in rhegmatogenous retinal detachment.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `retinal_corrugations_oct` |
| **Full name** | Outer Retinal Corrugations Imaging Dataset |
| **Primary category** | `oct` |
| **Contained modalities** | oct |
| **Tasks** | segmentation, regression |
| **Samples** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.5 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Mendeley Data |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download retinal_corrugations_oct --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download retinal_corrugations_oct --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('retinal_corrugations_oct')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/bzsc7gd9p3/1)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/bzsc7gd9p3/1)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{retinal_corrugations_oct,
  title  = { Outer Retinal Corrugations Imaging Dataset },
  note   = { Darabad RR et al. Outer Retinal Corrugations: Mechanical Models and Imaging Dataset. Mendeley Data, V1, 2022. doi:10.17632/bzsc7gd9p3.1 },
  year   = { 2022 },
  url    = { https://data.mendeley.com/datasets/bzsc7gd9p3/1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Darabad RR et al. Outer Retinal Corrugations: Mechanical Models and Imaging Dataset. Mendeley Data, V1, 2022. doi:10.17632/bzsc7gd9p3.1
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

- [syn_oct](./syn_oct.md): SYN-OCT Synthetic Glaucoma OCT Dataset (200,000 records, `cc-by`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 records, `unknown`)
- [kermany_oct](./kermany_oct.md): Kermany OCT 2018: Retinal OCT Image Classification (84,484 records, `cc-by`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (58,036 records, `mit`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 records, `unknown`)
- [harvard_fairvision](./harvard_fairvision.md): Harvard-FairVision (AMD + DR + Glaucoma, paired SLO + OCT) (30,000 records, `cc-by-nc-nd`)
- [mario](./mario.md): MARIO: AMD-Progression Longitudinal OCT (MICCAI 2024) (30,000 records, `cc-by`)
- [mmrdr](./mmrdr.md): MMRDR: Multi-Modal Retinal Diabetic Retinopathy Dataset (24,460 records, `cc-by`)
