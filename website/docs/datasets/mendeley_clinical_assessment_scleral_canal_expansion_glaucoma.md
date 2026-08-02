---
id: mendeley_clinical_assessment_scleral_canal_expansion_glaucoma
title: "Data for: Clinical Assessment of Scleral Canal Expansion in Glaucoma Using Spectral Domain Optical Coherence Tomography"
sidebar_label: mendeley_clinical_assessment_scleral_canal_expansion_glaucoma
description: "Observation-level source data, annotations, or signals. from Unilateral and bilateral glaucoma patient eyes are described."
tags: ["visual_field", "cc-by-nc", "mendeley", "measurement", "resource-role-current-dataset", "dataset-family-mendeley-clinical-assessment-scleral-canal-expansion-glaucoma"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Data for: Clinical Assessment of Scleral Canal Expansion in Glaucoma Using Spectral Domain Optical Coherence Tomography

Observation-level source data, annotations, or signals. from Unilateral and bilateral glaucoma patient eyes are described.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mendeley_clinical_assessment_scleral_canal_expansion_glaucoma` |
| **Full name** | Data for: Clinical Assessment of Scleral Canal Expansion in Glaucoma Using Spectral Domain Optical Coherence Tomography |
| **Primary category** | `visual_field` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `mendeley_clinical_assessment_scleral_canal_expansion_glaucoma` |
| **Contained modalities** | visual_field |
| **Tasks** | measurement |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | CC BY-NC 3.0 |
| **Normalized terms** | `cc-by-nc` |
| **Descriptive screening label** | Explicit noncommercial clause recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Mendeley Data |
| **Availability** | `available` (checked 2026-08-02) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

No reproducible primary item count was exposed for the cataloged source version.

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Human provenance: Unilateral and bilateral glaucoma patient eyes are described. Source-review finding: Four CSV files of demographic and optic-disc structural observations.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mendeley_clinical_assessment_scleral_canal_expansion_glaucoma --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download mendeley_clinical_assessment_scleral_canal_expansion_glaucoma --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mendeley_clinical_assessment_scleral_canal_expansion_glaucoma')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/7x3tgtskyj/2)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/7x3tgtskyj)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mendeley_clinical_assessment_scleral_canal_expansion_glaucoma,
  title  = { Data for: Clinical Assessment of Scleral Canal Expansion in Glaucoma Using Spectral Domain Optical Coherence Tomography },
  note   = { Data for: Clinical Assessment of Scleral Canal Expansion in Glaucoma Using Spectral Domain Optical Coherence Tomography. Mendeley Data, V2. doi:10.17632/7x3tgtskyj.2 },
  url    = { https://data.mendeley.com/datasets/7x3tgtskyj/2 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Data for: Clinical Assessment of Scleral Canal Expansion in Glaucoma Using Spectral Domain Optical Coherence Tomography. Mendeley Data, V2. doi:10.17632/7x3tgtskyj.2.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC BY-NC 3.0
- **Normalized category:** `cc-by-nc`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Explicit noncommercial clause recorded; check source

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [uwhvf](./uwhvf.md): UWHVF: University of Washington Humphrey Visual Field (28,943 visual field tests, `cc-by`)
- [fairvlmed](./fairvlmed.md): FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset (10,000 images, `cc-by-nc-nd`)
- [grape](./grape.md): GRAPE: Glaucoma Real-world Appraisal Progression Ensemble (1,115 examinations, `cc0`)
- [harvard_gdp](./harvard_gdp.md): Harvard GDP: Glaucoma Detection and Progression Dataset (1,000 participants, `cc-by-nc-nd`)
- [dryad_glaucoma_rnfl_vf](./dryad_glaucoma_rnfl_vf.md): RNFL and Visual-Field Glaucoma Diagnosis Dataset (499 records, `cc0`)
- [eyecatcher_visual_field](./eyecatcher_visual_field.md): Eyecatcher Tablet-Based Visual Field Home-Monitoring Data (440 visual field tests, `cc-by`)
- [stage_task1](./stage_task1.md): STAGE 2023 Task 1 — Mean Deviation Prediction from OCT (400 volumes, `research-only`)
- [stage_task2](./stage_task2.md): STAGE 2023 Task 2 — Visual Field Sensitivity Map Prediction (400 volumes, `research-only`)
