---
id: fimd
title: "Fundus Image Myopia Development Dataset"
sidebar_label: fimd
description: "Seventy retinal image pairs with visible myopia development and manually annotated corresponding control points."
tags: ["fundus", "cc-by", "mendeley", "registration", "regression", "resource-role-current-dataset", "dataset-family-fimd"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Fundus Image Myopia Development Dataset

Seventy retinal image pairs with visible myopia development and manually annotated corresponding control points.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `fimd` |
| **Full name** | Fundus Image Myopia Development Dataset |
| **First published** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Primary category** | `fundus` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `fimd` |
| **Contained modalities** | fundus |
| **Tasks** | registration, regression |
| **Primary reported quantity** | 70 image pairs |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.2 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Mendeley Data |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 70 | `image_pairs` | Longitudinal retinal registration pairs | `official_source_description` | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/jkzsh6pcv4/1) |
| Additional | 140 | `images` | Images participating in 70 pairs | `derived_from_reported_components` | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/jkzsh6pcv4/1) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download fimd --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download fimd --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('fimd')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/jkzsh6pcv4/1)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/jkzsh6pcv4/1)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{fimd,
  title  = { Fundus Image Myopia Development Dataset },
  note   = { Wang Z, Zou H, Guo Y, Guo S, Zhao X, Wang Y, Sun M. Fundus Image Myopia Development (FIMD) dataset. Mendeley Data, V1, 2023. doi:10.17632/jkzsh6pcv4.1 },
  year   = { 2023 },
  url    = { https://data.mendeley.com/datasets/jkzsh6pcv4/1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Wang Z, Zou H, Guo Y, Guo S, Zhao X, Wang Y, Sun M. Fundus Image Myopia Development (FIMD) dataset. Mendeley Data, V1, 2023. doi:10.17632/jkzsh6pcv4.1
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC BY 4.0
- **Normalized category:** `cc-by`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Standard label without an explicit NC clause; not a permission finding

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
