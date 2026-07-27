---
id: rop_ostrava
title: "Retinal Image Dataset of Infants and ROP (Ostrava)"
sidebar_label: rop_ostrava
description: "6,004 pediatric RetCam fundus images from 188 newborns in Ostrava (Czech Republic), annotated for retinopathy of prematurity (ROP) screening + classification."
tags: ["fundus", "cc-by", "kaggle", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Retinal Image Dataset of Infants and ROP (Ostrava)

6,004 pediatric RetCam fundus images from 188 newborns in Ostrava (Czech Republic), annotated for retinopathy of prematurity (ROP) screening + classification.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `rop_ostrava` |
| **Full name** | Retinal Image Dataset of Infants and ROP (Ostrava) |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | classification |
| **Samples** | 6,004 |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 5.0 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Kaggle |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download rop_ostrava --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download rop_ostrava --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('rop_ostrava')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [kaggle.com/datasets](https://www.kaggle.com/datasets/jananowakova/retinal-image-dataset-of-infants-and-rop)

**Source-term evidence:** [kaggle.com/datasets](https://www.kaggle.com/datasets/jananowakova/retinal-image-dataset-of-infants-and-rop)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{rop_ostrava,
  title  = { Retinal Image Dataset of Infants and ROP (Ostrava) },
  note   = { Timkovic et al., 'Retinal Image Dataset of Infants and ROP', Scientific Data 2024. doi:10.1038/s41597-024-03409-7 },
  year   = { 2024 },
  url    = { https://www.kaggle.com/datasets/jananowakova/retinal-image-dataset-of-infants-and-rop },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Timkovic et al., 'Retinal Image Dataset of Infants and ROP', Scientific Data 2024. doi:10.1038/s41597-024-03409-7
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
