---
id: eyecatcher_visual_field
title: "Eyecatcher Tablet-Based Visual Field Home-Monitoring Data"
sidebar_label: eyecatcher_visual_field
description: "Visual-field data from glaucoma home monitoring: mean deviation, duration, and pointwise differential light sensitivity values across HFA and Eyecatcher tests."
tags: ["visual_field", "cc-by", "mendeley", "regression", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Eyecatcher Tablet-Based Visual Field Home-Monitoring Data

Visual-field data from glaucoma home monitoring: mean deviation, duration, and pointwise differential light sensitivity values across HFA and Eyecatcher tests.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `eyecatcher_visual_field` |
| **Full name** | Eyecatcher Tablet-Based Visual Field Home-Monitoring Data |
| **Primary category** | `visual_field` |
| **Contained modalities** | visual_field |
| **Tasks** | regression, classification |
| **Samples** | 440 |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.01 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Mendeley Data |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download eyecatcher_visual_field --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download eyecatcher_visual_field --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('eyecatcher_visual_field')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/swsfj47cxw/2)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/swsfj47cxw/2)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{eyecatcher_visual_field,
  title  = { Eyecatcher Tablet-Based Visual Field Home-Monitoring Data },
  note   = { Jones P. Data for glaucoma home-monitoring using a tablet-based visual field test (Eyecatcher). Mendeley Data, V2, 2021. doi:10.17632/swsfj47cxw.2 },
  year   = { 2021 },
  url    = { https://data.mendeley.com/datasets/swsfj47cxw/2 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Jones P. Data for glaucoma home-monitoring using a tablet-based visual field test (Eyecatcher). Mendeley Data, V2, 2021. doi:10.17632/swsfj47cxw.2
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC BY 4.0
- **Normalized category:** `cc-by`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Standard label without an explicit NC clause; not a permission finding

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Related datasets with shared modalities

- [uwhvf](./uwhvf.md): UWHVF: University of Washington Humphrey Visual Field (28,943 records, `cc-by`)
- [grape](./grape.md): GRAPE: Glaucoma Real-world Appraisal Progression Ensemble (1,115 records, `cc0`)
- [harvard_gdp](./harvard_gdp.md): Harvard GDP: Glaucoma Detection and Progression Dataset (1,000 records, `cc-by-nc-nd`)
- [dryad_glaucoma_rnfl_vf](./dryad_glaucoma_rnfl_vf.md): RNFL and Visual-Field Glaucoma Diagnosis Dataset (499 records, `cc0`)
- [stage_task1](./stage_task1.md): STAGE 2023 Task 1 — Mean Deviation Prediction from OCT (400 records, `research-only`)
- [stage_task2](./stage_task2.md): STAGE 2023 Task 2 — Visual Field Sensitivity Map Prediction (400 records, `research-only`)
- [stage_task3](./stage_task3.md): STAGE 2023 Task 3 — Pattern Deviation Probability Map (400 records, `research-only`)
- [fairvlmed](./fairvlmed.md): FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset (count not reported records, `unknown`)
