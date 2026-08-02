---
id: visual_field_test_perception
title: "Visual Field Test Perception Dataset"
sidebar_label: visual_field_test_perception
description: "Human visual-field perception observations."
tags: ["visual_field", "cc-by", "figshare", "measurement"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Visual Field Test Perception Dataset

Human visual-field perception observations.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `visual_field_test_perception` |
| **Full name** | Visual Field Test Perception Dataset |
| **Primary category** | `visual_field` |
| **Contained modalities** | visual_field |
| **Tasks** | measurement |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Figshare |
| **Availability** | `available` (checked 2026-08-02) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

No reproducible primary item count was exposed for the cataloged source version.

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download visual_field_test_perception --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download visual_field_test_perception --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('visual_field_test_perception')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.6084/m9.figshare.12443594.v2](https://doi.org/10.6084/m9.figshare.12443594.v2)

**Source-term evidence:** [https://doi.org/10.6084/m9.figshare.12443594.v2](https://doi.org/10.6084/m9.figshare.12443594.v2)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{visual_field_test_perception,
  title  = { Visual Field Test Perception Dataset },
  note   = { Repository dataset record. 10.6084/m9.figshare.12443594.v2 },
  url    = { https://doi.org/10.6084/m9.figshare.12443594.v2 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Repository dataset record. 10.6084/m9.figshare.12443594.v2.
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
