---
id: intraretinal_cystoid_fluid
title: "Intraretinal Cystoid Fluid OCT Segmentation Dataset"
sidebar_label: intraretinal_cystoid_fluid
description: "OCT images for intraretinal cystoid-fluid segmentation, partly derived from public OCT DME sources with expert-selected masks."
tags: ["oct", "cc-by-nc-sa", "kaggle", "segmentation"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Intraretinal Cystoid Fluid OCT Segmentation Dataset

OCT images for intraretinal cystoid-fluid segmentation, partly derived from public OCT DME sources with expert-selected masks.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `intraretinal_cystoid_fluid` |
| **Full name** | Intraretinal Cystoid Fluid OCT Segmentation Dataset |
| **Primary category** | `oct` |
| **Contained modalities** | oct |
| **Tasks** | segmentation |
| **Samples** | 1,460 |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 1.0 GB |
| **Source-stated terms** | CC BY-NC-SA 4.0 |
| **Normalized terms** | `cc-by-nc-sa` |
| **Descriptive screening label** | Explicit noncommercial clause recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Kaggle |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Notes

> Partly derived from existing OCT datasets; retain as segmentation-mask resource.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download intraretinal_cystoid_fluid --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download intraretinal_cystoid_fluid --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('intraretinal_cystoid_fluid')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [kaggle.com/datasets](https://www.kaggle.com/datasets/zeeshanahmed13/intraretinal-cystoid-fluid)

**Source-term evidence:** [kaggle.com/datasets](https://www.kaggle.com/datasets/zeeshanahmed13/intraretinal-cystoid-fluid)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{intraretinal_cystoid_fluid,
  title  = { Intraretinal Cystoid Fluid OCT Segmentation Dataset },
  note   = { Intraretinal Cystoid Fluid dataset. Kaggle, accessed 2026-07 },
  year   = { 2026 },
  url    = { https://www.kaggle.com/datasets/zeeshanahmed13/intraretinal-cystoid-fluid },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Intraretinal Cystoid Fluid dataset. Kaggle, accessed 2026-07.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC BY-NC-SA 4.0
- **Normalized category:** `cc-by-nc-sa`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Explicit noncommercial clause recorded; check source

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
