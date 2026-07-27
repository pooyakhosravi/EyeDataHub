---
id: myopic_regression_fundus
title: "Myopic Regression after Corneal Refractive Surgery Fundus Sample"
sidebar_label: myopic_regression_fundus
description: "Public sample fundus photographs and measurements for modeling myopic regression after corneal refractive surgery."
tags: ["fundus", "cc-by", "mendeley", "regression", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Myopic Regression after Corneal Refractive Surgery Fundus Sample

Public sample fundus photographs and measurements for modeling myopic regression after corneal refractive surgery.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `myopic_regression_fundus` |
| **Full name** | Myopic Regression after Corneal Refractive Surgery Fundus Sample |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | regression, classification |
| **Samples** | 330 |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.2 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Mendeley Data |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Notes

> Public sample release; not the full original clinical study dataset.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download myopic_regression_fundus --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download myopic_regression_fundus --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('myopic_regression_fundus')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/k34rvfw3dg/2)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/k34rvfw3dg/2)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{myopic_regression_fundus,
  title  = { Myopic Regression after Corneal Refractive Surgery Fundus Sample },
  note   = { Machine learning predicting myopic regression after corneal refractive surgery. Mendeley Data, V2, 2021. doi:10.17632/k34rvfw3dg.2 },
  year   = { 2021 },
  url    = { https://data.mendeley.com/datasets/k34rvfw3dg/2 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Machine learning predicting myopic regression after corneal refractive surgery. Mendeley Data, V2, 2021. doi:10.17632/k34rvfw3dg.2
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
