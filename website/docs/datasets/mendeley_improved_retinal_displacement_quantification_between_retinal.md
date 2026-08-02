---
id: mendeley_improved_retinal_displacement_quantification_between_retinal
title: "Improved Retinal Displacement Quantification Between Retinal Vessels and Corresponding Retinal Vessel Printings Across the 3D Spherical Surface of the Eye: Dataset of Measurements on Fundus Autofluorescence Imaging"
sidebar_label: mendeley_improved_retinal_displacement_quantification_between_retinal
description: "Patient/eye-level fundus-autofluorescence retinal-displacement measurements from Patients who underwent pars plana vitrectomy or pneumatic retinopexy."
tags: ["fundus", "cc-by", "mendeley", "classification", "resource-role-current-dataset", "dataset-family-mendeley-improved-retinal-displacement-quantification-between-retinal"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Improved Retinal Displacement Quantification Between Retinal Vessels and Corresponding Retinal Vessel Printings Across the 3D Spherical Surface of the Eye: Dataset of Measurements on Fundus Autofluorescence Imaging

Patient/eye-level fundus-autofluorescence retinal-displacement measurements from Patients who underwent pars plana vitrectomy or pneumatic retinopexy.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mendeley_improved_retinal_displacement_quantification_between_retinal` |
| **Full name** | Improved Retinal Displacement Quantification Between Retinal Vessels and Corresponding Retinal Vessel Printings Across the 3D Spherical Surface of the Eye: Dataset of Measurements on Fundus Autofluorescence Imaging |
| **Primary category** | `fundus` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `mendeley_improved_retinal_displacement_quantification_between_retinal` |
| **Contained modalities** | fundus |
| **Tasks** | classification |
| **Primary reported quantity** | 53 participants |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | Creative Commons Attribution 4.0 International |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `unknown` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Mendeley Data |
| **Availability** | `available` (checked 2026-08-02) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 53 | `participants` | Source-stated quantity Preserved from the source-confirmation record. | `official_source_description` | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/jxwkym2phr) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Human provenance: Patients who underwent pars plana vitrectomy or pneumatic retinopexy. Source-review finding: Source description states measurements from 53 patients, 35 treated with PPV and the remainder with PnR.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mendeley_improved_retinal_displacement_quantification_between_retinal --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download mendeley_improved_retinal_displacement_quantification_between_retinal --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mendeley_improved_retinal_displacement_quantification_between_retinal')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/jxwkym2phr/1)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/jxwkym2phr)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mendeley_improved_retinal_displacement_quantification_between_retinal,
  title  = { Improved Retinal Displacement Quantification Between Retinal Vessels and Corresponding Retinal Vessel Printings Across the 3D Spherical Surface of the Eye: Dataset of Measurements on Fundus Autofluorescence Imaging },
  note   = { Improved Retinal Displacement Quantification Between Retinal Vessels and Corresponding Retinal Vessel Printings Across the 3D Spherical Surface of the Eye: Dataset of Measurements on Fundus Autofluorescence Imaging. Mendeley Data, V1. doi:10.17632/jxwkym2phr.1 },
  url    = { https://data.mendeley.com/datasets/jxwkym2phr/1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Improved Retinal Displacement Quantification Between Retinal Vessels and Corresponding Retinal Vessel Printings Across the 3D Spherical Surface of the Eye: Dataset of Measurements on Fundus Autofluorescence Imaging. Mendeley Data, V1. doi:10.17632/jxwkym2phr.1.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Creative Commons Attribution 4.0 International
- **Normalized category:** `cc-by`
- **Apparent scope:** `unknown`
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
