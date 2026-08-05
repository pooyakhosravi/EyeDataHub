---
id: uwhvf
title: "UWHVF: University of Washington Humphrey Visual Field"
sidebar_label: uwhvf
description: "28,943 HFA 24-2 visual field tests with per-point sensitivities, MD/PSD indices, glaucoma labels, and longitudinal follow-up data. Input: 52-element sensitivity array (not an image)."
tags: ["visual_field", "cc-by", "direct", "classification", "regression", "resource-role-current-dataset", "dataset-family-uwhvf"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# UWHVF: University of Washington Humphrey Visual Field

28,943 HFA 24-2 visual field tests with per-point sensitivities, MD/PSD indices, glaucoma labels, and longitudinal follow-up data. Input: 52-element sensitivity array (not an image).

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `uwhvf` |
| **Full name** | UWHVF: University of Washington Humphrey Visual Field |
| **Primary category** | `visual_field` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `uwhvf` |
| **Contained modalities** | visual_field |
| **Tasks** | classification, regression |
| **Primary reported quantity** | 28,943 visual field tests |
| **Classes** | 2 (Non-glaucoma, Glaucoma) |
| **Splits** | all |
| **Size** | 0.05 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Direct HTTP |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `end_to_end_tested` |
| **Legacy sample-loader status** | Standard loader included |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 28,943 | `visual_field_tests` | HFA 24-2 tests | `official_source_description` | [github.com/uw-biomedical-ml](https://github.com/uw-biomedical-ml/uwhvf) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Non-imaging dataset. Samples are 52-element visual field arrays. Models must accept 1D/2D VF arrays, not RGB images.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download uwhvf --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download uwhvf --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('uwhvf')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [github.com/uw-biomedical-ml](https://github.com/uw-biomedical-ml/uwhvf/archive/refs/heads/master.zip)

**Source-term evidence:** [github.com/uw-biomedical-ml](https://github.com/uw-biomedical-ml/uwhvf/archive/refs/heads/master.zip)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('uwhvf')
samples = ds.load(data_dir, split='all')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{uwhvf,
  title  = { UWHVF: University of Washington Humphrey Visual Field },
  note   = { Boland et al., 'The University of Washington Humphrey Visual Field database', Ophthalmic Epidemiology 2022 },
  year   = { 2022 },
  url    = { https://github.com/uw-biomedical-ml/uwhvf/archive/refs/heads/master.zip },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Boland et al., 'The University of Washington Humphrey Visual Field database', Ophthalmic Epidemiology 2022.
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

- [fairvlmed](./fairvlmed.md): FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset (10,000 images, `cc-by-nc-nd`)
- [grape](./grape.md): GRAPE: Glaucoma Real-world Appraisal Progression Ensemble (1,115 examinations, `cc0`)
- [harvard_gdp](./harvard_gdp.md): Harvard GDP: Glaucoma Detection and Progression Dataset (1,000 participants, `cc-by-nc-nd`)
- [dryad_glaucoma_rnfl_vf](./dryad_glaucoma_rnfl_vf.md): RNFL and Visual-Field Glaucoma Diagnosis Dataset (499 records, `cc0`)
- [eyecatcher_visual_field](./eyecatcher_visual_field.md): Eyecatcher Tablet-Based Visual Field Home-Monitoring Data (440 visual field tests, `cc-by`)
- [stage_task1](./stage_task1.md): STAGE 2023 Task 1 — Mean Deviation Prediction from OCT (400 volumes, `research-only`)
- [stage_task2](./stage_task2.md): STAGE 2023 Task 2 — Visual Field Sensitivity Map Prediction (400 volumes, `research-only`)
- [stage_task3](./stage_task3.md): STAGE 2023 Task 3 — Pattern Deviation Probability Map (400 volumes, `research-only`)
