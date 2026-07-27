---
id: csc_fundus_segmentation
title: "Central Serous Chorioretinopathy Fundus Segmentation Dataset"
sidebar_label: csc_fundus_segmentation
description: "Fundus photographs and segmentation masks for subretinal fluid in central serous chorioretinopathy, with healthy-eye classification controls."
tags: ["fundus", "cc-by", "mendeley", "segmentation", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Central Serous Chorioretinopathy Fundus Segmentation Dataset

Fundus photographs and segmentation masks for subretinal fluid in central serous chorioretinopathy, with healthy-eye classification controls.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `csc_fundus_segmentation` |
| **Full name** | Central Serous Chorioretinopathy Fundus Segmentation Dataset |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | segmentation, classification |
| **Samples** | 287 |
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
eyehub download csc_fundus_segmentation --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download csc_fundus_segmentation --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('csc_fundus_segmentation')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/4k64fwnp4k/5)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/4k64fwnp4k/5)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{csc_fundus_segmentation,
  title  = { Central Serous Chorioretinopathy Fundus Segmentation Dataset },
  note   = { Yang HK et al. Data for deep-learning-based segmentation of central serous chorioretinopathy in fundus photographs. Mendeley Data, V5, 2022. doi:10.17632/4k64fwnp4k.5 },
  year   = { 2022 },
  url    = { https://data.mendeley.com/datasets/4k64fwnp4k/5 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Yang HK et al. Data for deep-learning-based segmentation of central serous chorioretinopathy in fundus photographs. Mendeley Data, V5, 2022. doi:10.17632/4k64fwnp4k.5
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

- [airogs](./airogs.md): AIROGS: AI for Robust Glaucoma Screening (113,893 records, `cc-by-nc-nd`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 records, `unknown`)
- [justraigs](./justraigs.md): JustRAIGS: Just Referral AI Glaucoma Screening Dataset (101,442 records, `cc-by-nc-nd`)
- [eyepacs](./eyepacs.md): EyePACS — Diabetic Retinopathy Detection (Kaggle 2015) (88,702 records, `research-only`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (58,036 records, `mit`)
- [angioreport](./angioreport.md): AngioReport Fundus Angiography Report Dataset (55,361 records, `unknown`)
- [ffa_ir](./ffa_ir.md): FFA-IR Medical Report Dataset (47,247 records, `unknown`)
- [bidr](./bidr.md): BiDR: Diabetic Retinopathy Diagnosis Dataset (35,126 records, `unknown`)
