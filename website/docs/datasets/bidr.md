---
id: bidr
title: "BiDR: Diabetic Retinopathy Diagnosis Dataset"
sidebar_label: bidr
description: "35,126 fundus images for 5-class diabetic retinopathy grading (No DR: 25,810 / Mild: 2,443 / Moderate: 5,292 / Severe: 873 / Proliferative: 708). Available via Kaggle."
tags: ["fundus", "unknown", "kaggle", "grading", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# BiDR: Diabetic Retinopathy Diagnosis Dataset

35,126 fundus images for 5-class diabetic retinopathy grading (No DR: 25,810 / Mild: 2,443 / Moderate: 5,292 / Severe: 873 / Proliferative: 708). Available via Kaggle.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `bidr` |
| **Full name** | BiDR: Diabetic Retinopathy Diagnosis Dataset |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | grading, classification |
| **Samples** | 35,126 |
| **Classes** | 5 (No DR, Mild DR, Moderate DR, Severe DR, Proliferative DR) |
| **Splits** | train, test |
| **Size** | 1.0 GB |
| **Source-stated terms** | See Kaggle dataset page |
| **Normalized terms** | `unknown` |
| **Descriptive screening label** | Unknown or unclear; do not assume permission |
| **Terms scope** | `unknown` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Kaggle |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Standard loader included |


## Notes

> OVERLAP: BiDR is a Kaggle re-upload of the EyePACS Kaggle 2015 competition TRAIN split (35,126 images). Already in EyeDataHub as `eyepacs` (full 88,702 train+test) and also as `dr_arranged` (Tianchi mirror of the same train split). Kept for users who specifically reference the BiDR slug.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download bidr --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download bidr --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('bidr')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [kaggle.com/datasets](https://www.kaggle.com/datasets/pkdarabi/diagnosis-of-diabetic-retinopathy)

**Source-term evidence:** [kaggle.com/datasets](https://www.kaggle.com/datasets/pkdarabi/diagnosis-of-diabetic-retinopathy)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('bidr')
samples = ds.load(data_dir, split='test')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{bidr,
  title  = { BiDR: Diabetic Retinopathy Diagnosis Dataset },
  note   = { BiDR Dataset. Kaggle. https://www.kaggle.com/datasets/pkdarabi/diagnosis-of-diabetic-retinopathy },
  url    = { https://www.kaggle.com/datasets/pkdarabi/diagnosis-of-diabetic-retinopathy },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
BiDR Dataset. Kaggle. https://www.kaggle.com/datasets/pkdarabi/diagnosis-of-diabetic-retinopathy
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** See Kaggle dataset page
- **Normalized category:** `unknown`
- **Apparent scope:** `unknown`
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
- [dr_arranged](./dr_arranged.md): Diabetic Retinopathy Arranged Dataset (Tianchi 93926) (35,126 records, `cc-by-nc-sa`)
