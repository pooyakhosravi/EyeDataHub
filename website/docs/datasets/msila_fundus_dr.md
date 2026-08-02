---
id: msila_fundus_dr
title: "M'Sila Retinal Fundus Dataset for Diabetic Retinopathy Classification"
sidebar_label: msila_fundus_dr
description: "Anonymized retinal fundus images from an ophthalmology clinic in M'Sila, Algeria for diabetic-retinopathy classification."
tags: ["fundus", "cc-by", "zenodo", "classification", "grading"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# M'Sila Retinal Fundus Dataset for Diabetic Retinopathy Classification

Anonymized retinal fundus images from an ophthalmology clinic in M'Sila, Algeria for diabetic-retinopathy classification.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `msila_fundus_dr` |
| **Full name** | M'Sila Retinal Fundus Dataset for Diabetic Retinopathy Classification |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | classification, grading |
| **Primary reported quantity** | 1,335 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 1.47 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Zenodo |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 1,335 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [zenodo.org/records](https://zenodo.org/records/19169587) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download msila_fundus_dr --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download msila_fundus_dr --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('msila_fundus_dr')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [zenodo.org/records](https://zenodo.org/records/19169587)

**Source-term evidence:** [zenodo.org/records](https://zenodo.org/records/19169587)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{msila_fundus_dr,
  title  = { M'Sila Retinal Fundus Dataset for Diabetic Retinopathy Classification },
  note   = { M'Sila retinal fundus dataset for diabetic retinopathy classification. Zenodo, 2026. doi:10.5281/zenodo.19169587 },
  year   = { 2026 },
  url    = { https://zenodo.org/records/19169587 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
M'Sila retinal fundus dataset for diabetic retinopathy classification. Zenodo, 2026. doi:10.5281/zenodo.19169587
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
- [bidr](./bidr.md): BiDR: Diabetic Retinopathy Diagnosis Dataset (35,126 images, `unknown`)
