---
id: vietai_retinal_disease
title: "VietAI Retinal Disease Detection 2020"
sidebar_label: vietai_retinal_disease
description: "A multilabel fundus classification challenge with 3,435 labeled training images and 350 test images covering six disease groups and normal findings."
tags: ["fundus", "unknown", "kaggle", "multilabel", "classification", "resource-role-current-dataset", "dataset-family-vietai-retinal-disease", "documented-relationship", "relationship-derived_from"]
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
| **First published** | 2020-09-06 |
| **Publication date precision** | day |
| **Publication date evidence** | [kaggle.com/c](https://www.kaggle.com/c/vietai-advance-retinal-disease-detection-2020) |
| **Publication date source field** | Kaggle competition Overview: Start |
| **Publication date reviewed** | 2026-09-11 |
| **Primary category** | `fundus` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `vietai_retinal_disease` |
| **Contained modalities** | fundus |
| **Tasks** | multilabel, classification |
| **Primary reported quantity** | 3,785 images |
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


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 3,785 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [kaggle.com/competitions](https://www.kaggle.com/competitions/vietai-advance-retinal-disease-detection-2020/data) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Kaggle authentication and acceptance of the competition rules may be required. Derivative archives that mix these images with unverified sources were excluded from the registry.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- [multieye](./multieye.md) is `derived from` this record: The MultiEYE paper names this record as one of the public fundus or OCT sources assembled for the benchmark. ([evidence](https://arxiv.org/abs/2412.09402))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download vietai_retinal_disease --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download vietai_retinal_disease --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('vietai_retinal_disease')
print(preflight_dataset(ds, './data'))  # no download
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

## Similar resources by shared modality

- [airogs](./airogs.md): AIROGS: AI for Robust Glaucoma Screening (113,893 images, `cc-by-nc-nd`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (103,959 images, `mit`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [justraigs](./justraigs.md): JustRAIGS: Just Referral AI Glaucoma Screening Dataset (101,442 images, `cc-by-nc-nd`)
- [eyepacs](./eyepacs.md): EyePACS — Diabetic Retinopathy Detection (Kaggle 2015) (88,702 images, `research-only`)
- [angioreport](./angioreport.md): AngioReport Fundus Angiography Report Dataset (55,361 images, `unknown`)
- [ffa_ir](./ffa_ir.md): FFA-IR Medical Report Dataset (47,247 images, `unknown`)
- [mfiddr](./mfiddr.md): MFIDDR: Multi-Field Imaging Dataset for Diabetic Retinopathy (34,452 images, `mit`)
