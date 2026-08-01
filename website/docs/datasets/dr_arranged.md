---
id: dr_arranged
title: "Diabetic Retinopathy Arranged Dataset (Tianchi 93926)"
sidebar_label: dr_arranged
description: "35,126 fundus images organised for 5-class DR severity grading (ICDR grades 0-4): No DR 25,810 / Mild 2,443 / Moderate 5,292 / Severe 873 / Proliferative 708. Hosted on Alibaba Tianchi."
tags: ["fundus", "cc-by-nc-sa", "manual", "grading", "classification", "documented-relationship", "relationship-mirror_of", "relationship-subset_of"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Diabetic Retinopathy Arranged Dataset (Tianchi 93926)

35,126 fundus images organised for 5-class DR severity grading (ICDR grades 0-4): No DR 25,810 / Mild 2,443 / Moderate 5,292 / Severe 873 / Proliferative 708. Hosted on Alibaba Tianchi.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dr_arranged` |
| **Full name** | Diabetic Retinopathy Arranged Dataset (Tianchi 93926) |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | grading, classification |
| **Primary reported quantity** | 35,126 images |
| **Classes** | 5 (No DR, Mild DR, Moderate DR, Severe DR, Proliferative DR) |
| **Splits** | train, test |
| **Size** | 8.0 GB |
| **Source-stated terms** | CC BY-NC-SA 4.0 |
| **Normalized terms** | `cc-by-nc-sa` |
| **Descriptive screening label** | Explicit noncommercial clause recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `guided_instructions_only` |
| **Legacy sample-loader status** | Standard loader included |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 35,126 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [tianchi.aliyun.com/dataset](https://tianchi.aliyun.com/dataset/93926) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> OVERLAP: This is the EyePACS Kaggle 2015 competition TRAIN split (35,126 images) mirrored on Tianchi. Same content as `bidr` (Kaggle mirror) and a strict subset of `eyepacs` (full 88,702). Kept for users who specifically reference the Tianchi 93926 mirror.
> Requires free registration at https://tianchi.aliyun.com. Log in → Datasets → 93926 → Download.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- [bidr](./bidr.md) is `mirror of` this record: BiDR and the Tianchi arranged record contain the same documented EyePACS training split. ([evidence](https://www.kaggle.com/datasets/pkdarabi/diagnosis-of-diabetic-retinopathy))
- This record is `mirror of` [bidr](./bidr.md): The Tianchi arranged record and BiDR contain the same documented EyePACS training split. ([evidence](https://tianchi.aliyun.com/dataset/93926))
- This record is `subset of` [eyepacs](./eyepacs.md): The Tianchi record republishes the 35,126-image EyePACS competition training split. ([evidence](https://tianchi.aliyun.com/dataset/93926))

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dr_arranged --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download dr_arranged --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dr_arranged')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [tianchi.aliyun.com/dataset](https://tianchi.aliyun.com/dataset/93926)

**Source-term evidence:** [tianchi.aliyun.com/dataset](https://tianchi.aliyun.com/dataset/93926)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('dr_arranged')
samples = ds.load(data_dir, split='test')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dr_arranged,
  title  = { Diabetic Retinopathy Arranged Dataset (Tianchi 93926) },
  note   = { Diabetic Retinopathy Arranged Dataset. Tianchi Open Datasets, dataset ID 93926. https://tianchi.aliyun.com/dataset/93926 },
  url    = { https://tianchi.aliyun.com/dataset/93926 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Diabetic Retinopathy Arranged Dataset. Tianchi Open Datasets, dataset ID 93926. https://tianchi.aliyun.com/dataset/93926
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC BY-NC-SA 4.0
- **Normalized category:** `cc-by-nc-sa`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Explicit noncommercial clause recorded; check source

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [airogs](./airogs.md): AIROGS: AI for Robust Glaucoma Screening (113,893 images, `cc-by-nc-nd`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (103,959 images, `mit`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [justraigs](./justraigs.md): JustRAIGS: Just Referral AI Glaucoma Screening Dataset (101,442 images, `cc-by-nc-nd`)
- [eyepacs](./eyepacs.md): EyePACS — Diabetic Retinopathy Detection (Kaggle 2015) (88,702 images, `research-only`)
- [angioreport](./angioreport.md): AngioReport Fundus Angiography Report Dataset (55,361 images, `unknown`)
- [ffa_ir](./ffa_ir.md): FFA-IR Medical Report Dataset (47,247 images, `unknown`)
- [bidr](./bidr.md): BiDR: Diabetic Retinopathy Diagnosis Dataset (35,126 images, `unknown`)
