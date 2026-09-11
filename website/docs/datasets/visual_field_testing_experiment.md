---
id: visual_field_testing_experiment
title: "Visual Field Testing Experiment"
sidebar_label: visual_field_testing_experiment
description: "Visual-field and psychophysics experiment data for scotoma-detection comparisons."
tags: ["visual_field", "cc-by", "kaggle", "classification", "regression", "resource-role-current-dataset", "dataset-family-visual-field-testing-experiment"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Visual Field Testing Experiment

Visual-field and psychophysics experiment data for scotoma-detection comparisons.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `visual_field_testing_experiment` |
| **Full name** | Visual Field Testing Experiment |
| **Publication date** | 2021-10-04 |
| **Date basis** | Initial dataset release |
| **Publication date precision** | day |
| **Publication date evidence** | [kaggle.com/api](https://www.kaggle.com/api/v1/datasets/view/shozosaeki/visual-field-testing-experiment) |
| **Publication date source field** | versions[0].creationDate (version 1, Initial release) |
| **Publication date reviewed** | 2026-09-11 |
| **Date notes** | Public Kaggle v1 is the cataloged experiment-data release; the linked preprint date is not used. |
| **Primary category** | `visual_field` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `visual_field_testing_experiment` |
| **Contained modalities** | visual_field |
| **Tasks** | classification, regression |
| **Primary reported quantity** | 78 visual fields |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.01 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Kaggle |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 78 | `visual_fields` | Rows and distinct IDs in fields.csv | `current_deposit_table` | [kaggle.com/datasets](https://www.kaggle.com/datasets/shozosaeki/visual-field-testing-experiment) |
| Additional | 15,678 | `measurement_rows` | Eye-guided measurement rows in display_results.csv | `current_deposit_table` | [kaggle.com/datasets](https://www.kaggle.com/datasets/shozosaeki/visual-field-testing-experiment) |
| Additional | 4,212 | `measurement_rows` | Humphrey field-analyzer rows in hfa_results.csv | `current_deposit_table` | [kaggle.com/datasets](https://www.kaggle.com/datasets/shozosaeki/visual-field-testing-experiment) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download visual_field_testing_experiment --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download visual_field_testing_experiment --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('visual_field_testing_experiment')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [kaggle.com/datasets](https://www.kaggle.com/datasets/shozosaeki/visual-field-testing-experiment)

**Source-term evidence:** [kaggle.com/datasets](https://www.kaggle.com/datasets/shozosaeki/visual-field-testing-experiment)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{visual_field_testing_experiment,
  title  = { Visual Field Testing Experiment },
  note   = { Visual Field Testing Experiment. Kaggle, accessed 2026-07 },
  year   = { 2026 },
  url    = { https://www.kaggle.com/datasets/shozosaeki/visual-field-testing-experiment },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Visual Field Testing Experiment. Kaggle, accessed 2026-07.
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
