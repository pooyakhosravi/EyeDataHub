---
id: mendeley_early_detection_glaucomatous_visual_field_progression
title: "Data for: Early Detection of Glaucomatous Visual Field Progression Using Pointwise Linear Regression with Binomial Test in the Central 10 Degrees"
sidebar_label: mendeley_early_detection_glaucomatous_visual_field_progression
description: "Observation-level human or human-derived measurements/signals. from Glaucoma patients with repeated visual-field observations."
tags: ["visual_field", "cc-by", "mendeley", "classification", "resource-role-current-dataset", "dataset-family-mendeley-early-detection-glaucomatous-visual-field-progression"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Data for: Early Detection of Glaucomatous Visual Field Progression Using Pointwise Linear Regression with Binomial Test in the Central 10 Degrees

Observation-level human or human-derived measurements/signals. from Glaucoma patients with repeated visual-field observations.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mendeley_early_detection_glaucomatous_visual_field_progression` |
| **Full name** | Data for: Early Detection of Glaucomatous Visual Field Progression Using Pointwise Linear Regression with Binomial Test in the Central 10 Degrees |
| **First published** | 2020-03-31 |
| **Publication date precision** | day |
| **Publication date evidence** | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/w34s5mhvpm/1) |
| **Publication date source field** | citation_publication_date (version 1) |
| **Publication date reviewed** | 2026-09-11 |
| **Primary category** | `visual_field` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `mendeley_early_detection_glaucomatous_visual_field_progression` |
| **Contained modalities** | visual_field |
| **Tasks** | classification |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
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

> Human provenance: Glaucoma patients with repeated visual-field observations. Source-review finding: Humphrey Visual Field Analyzer 10-2 data at each observation point.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mendeley_early_detection_glaucomatous_visual_field_progression --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download mendeley_early_detection_glaucomatous_visual_field_progression --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mendeley_early_detection_glaucomatous_visual_field_progression')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/w34s5mhvpm/1)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/w34s5mhvpm)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mendeley_early_detection_glaucomatous_visual_field_progression,
  title  = { Data for: Early Detection of Glaucomatous Visual Field Progression Using Pointwise Linear Regression with Binomial Test in the Central 10 Degrees },
  note   = { Data for: Early Detection of Glaucomatous Visual Field Progression Using Pointwise Linear Regression with Binomial Test in the Central 10 Degrees. Mendeley Data, V1. doi:10.17632/w34s5mhvpm.1 },
  url    = { https://data.mendeley.com/datasets/w34s5mhvpm/1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Data for: Early Detection of Glaucomatous Visual Field Progression Using Pointwise Linear Regression with Binomial Test in the Central 10 Degrees. Mendeley Data, V1. doi:10.17632/w34s5mhvpm.1.
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

- [uwhvf](./uwhvf.md): UWHVF: University of Washington Humphrey Visual Field (28,943 visual field tests, `cc-by`)
- [fairvlmed](./fairvlmed.md): FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset (10,000 images, `cc-by-nc-nd`)
- [grape](./grape.md): GRAPE: Glaucoma Real-world Appraisal Progression Ensemble (1,115 examinations, `cc0`)
- [harvard_gdp](./harvard_gdp.md): Harvard GDP: Glaucoma Detection and Progression Dataset (1,000 participants, `cc-by-nc-nd`)
- [dryad_glaucoma_rnfl_vf](./dryad_glaucoma_rnfl_vf.md): RNFL and Visual-Field Glaucoma Diagnosis Dataset (499 records, `cc0`)
- [eyecatcher_visual_field](./eyecatcher_visual_field.md): Eyecatcher Tablet-Based Visual Field Home-Monitoring Data (440 visual field tests, `cc-by`)
- [stage_task1](./stage_task1.md): STAGE 2023 Task 1 — Mean Deviation Prediction from OCT (400 volumes, `research-only`)
- [stage_task2](./stage_task2.md): STAGE 2023 Task 2 — Visual Field Sensitivity Map Prediction (400 volumes, `research-only`)
