---
id: bidr
title: "BiDR: Diabetic Retinopathy Diagnosis Dataset"
sidebar_label: bidr
description: "35,126 fundus images for 5-class diabetic retinopathy grading (No DR: 25,810 / Mild: 2,443 / Moderate: 5,292 / Severe: 873 / Proliferative: 708). Available via Kaggle."
tags: ["fundus", "unknown", "kaggle", "grading", "classification", "documented-relationship", "relationship-mirror_of", "relationship-subset_of"]
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
| **Primary reported quantity** | 35,126 images |
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


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 35,126 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [kaggle.com/datasets](https://www.kaggle.com/datasets/pkdarabi/diagnosis-of-diabetic-retinopathy) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> OVERLAP: BiDR is a Kaggle re-upload of the EyePACS Kaggle 2015 competition TRAIN split (35,126 images). Already in EyeDataHub as `eyepacs` (full 88,702 train+test) and also as `dr_arranged` (Tianchi mirror of the same train split). Kept for users who specifically reference the BiDR slug.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- [dr_arranged](./dr_arranged.md) is `mirror of` this record: The Tianchi arranged record and BiDR contain the same documented EyePACS training split. ([evidence](https://tianchi.aliyun.com/dataset/93926))
- This record is `mirror of` [dr_arranged](./dr_arranged.md): BiDR and the Tianchi arranged record contain the same documented EyePACS training split. ([evidence](https://www.kaggle.com/datasets/pkdarabi/diagnosis-of-diabetic-retinopathy))
- This record is `subset of` [eyepacs](./eyepacs.md): BiDR republishes the 35,126-image EyePACS competition training split, not the full EyePACS record. ([evidence](https://www.kaggle.com/datasets/pkdarabi/diagnosis-of-diabetic-retinopathy))

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

## Similar resources by shared modality

- [airogs](./airogs.md): AIROGS: AI for Robust Glaucoma Screening (113,893 images, `cc-by-nc-nd`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (103,959 images, `mit`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [justraigs](./justraigs.md): JustRAIGS: Just Referral AI Glaucoma Screening Dataset (101,442 images, `cc-by-nc-nd`)
- [eyepacs](./eyepacs.md): EyePACS — Diabetic Retinopathy Detection (Kaggle 2015) (88,702 images, `research-only`)
- [angioreport](./angioreport.md): AngioReport Fundus Angiography Report Dataset (55,361 images, `unknown`)
- [ffa_ir](./ffa_ir.md): FFA-IR Medical Report Dataset (47,247 images, `unknown`)
- [dr_arranged](./dr_arranged.md): Diabetic Retinopathy Arranged Dataset (Tianchi 93926) (35,126 images, `cc-by-nc-sa`)
