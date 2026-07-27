---
id: vietai_retinal_disease
title: "VietAI Retinal Disease Detection 2020"
sidebar_label: vietai_retinal_disease
description: "A multilabel fundus classification challenge with 3,435 labeled training images and 350 test images covering six disease groups and normal findings."
tags: ["fundus", "unknown", "kaggle", "multilabel", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# VietAI Retinal Disease Detection 2020

A multilabel fundus classification challenge with 3,435 labeled training images and 350 test images covering six disease groups and normal findings.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `vietai_retinal_disease` |
| **Full name** | VietAI Retinal Disease Detection 2020 |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | multilabel, classification |
| **Samples** | 3,785 |
| **Classes** | 7 (opacity, diabetic_retinopathy, glaucoma, macular_edema, macular_degeneration, retinal_vein_occlusion, normal) |
| **Splits** | train, test |
| **Size** | Not reported |
| **Source-stated terms** | Kaggle competition rules |
| **Normalized terms** | `unknown` |
| **Descriptive screening label** | Unknown or unclear; do not assume permission |
| **Terms scope** | `challenge_participation` |
| **Access friction** | `self_service_clickthrough` |
| **Route backend** | Kaggle |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Notes

> Kaggle authentication and acceptance of the competition rules may be required. Derivative archives that mix these images with unverified sources were excluded from the registry.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download vietai_retinal_disease --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download vietai_retinal_disease --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('vietai_retinal_disease')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [kaggle.com/competitions](https://www.kaggle.com/competitions/vietai-advance-retinal-disease-detection-2020/data)

**Source-term evidence:** [kaggle.com/competitions](https://www.kaggle.com/competitions/vietai-advance-retinal-disease-detection-2020/data)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{vietai_retinal_disease,
  title  = { VietAI Retinal Disease Detection 2020 },
  note   = { VietAI Advance Course Retinal Disease Detection. Kaggle. 2020 },
  year   = { 2020 },
  url    = { https://www.kaggle.com/competitions/vietai-advance-retinal-disease-detection-2020/data },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
VietAI Advance Course Retinal Disease Detection. Kaggle. 2020.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Kaggle competition rules
- **Normalized category:** `unknown`
- **Apparent scope:** `challenge_participation`
- **Descriptive screening label:** Unknown or unclear; do not assume permission

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
