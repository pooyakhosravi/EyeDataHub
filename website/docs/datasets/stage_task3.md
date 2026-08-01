---
id: stage_task3
title: "STAGE 2023 Task 3 — Pattern Deviation Probability Map"
sidebar_label: stage_task3
description: "400 macular OCT volumes; predict 52-point pattern deviation probability map from 24-2 Humphrey visual field test. Multi-output regression."
tags: ["oct", "visual_field", "research-only", "manual", "regression", "documented-relationship", "relationship-same_or_overlapping_cohort_as"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# STAGE 2023 Task 3 — Pattern Deviation Probability Map

400 macular OCT volumes; predict 52-point pattern deviation probability map from 24-2 Humphrey visual field test. Multi-output regression.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `stage_task3` |
| **Full name** | STAGE 2023 Task 3 — Pattern Deviation Probability Map |
| **Primary category** | `oct` |
| **Contained modalities** | oct, visual_field |
| **Tasks** | regression |
| **Primary reported quantity** | 400 volumes |
| **Classes** | 52 (PD_01, PD_02, PD_03, PD_04, PD_05, PD_06, PD_07, PD_08, PD_09, PD_10, PD_11, PD_12, PD_13, PD_14, PD_15, PD_16, PD_17, PD_18, PD_19, PD_20, PD_21, PD_22, PD_23, PD_24, PD_25, PD_26, PD_27, PD_28, PD_29, PD_30, PD_31, PD_32, PD_33, PD_34, PD_35, PD_36, PD_37, PD_38, PD_39, PD_40, PD_41, PD_42, PD_43, PD_44, PD_45, PD_46, PD_47, PD_48, PD_49, PD_50, PD_51, PD_52) |
| **Splits** | train, test |
| **Size** | 5.0 GB |
| **Source-stated terms** | Non-commercial research (Baidu AI Studio) |
| **Normalized terms** | `research-only` |
| **Descriptive screening label** | Research or challenge restriction recorded; check source |
| **Terms scope** | `unknown` |
| **Access friction** | `self_service_clickthrough` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `guided_instructions_only` |
| **Legacy sample-loader status** | Standard loader included |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 400 | `volumes` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [aistudio.baidu.com/aistudio](https://aistudio.baidu.com/aistudio/competition/detail/968/0/datasets) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- [stage_task1](./stage_task1.md) is `same or overlapping cohort as` this record: STAGE Tasks 1 and 3 use the same 400 OCT volumes and expose different labels. ([evidence](https://aistudio.baidu.com/aistudio/competition/detail/968/0/datasets))
- [stage_task2](./stage_task2.md) is `same or overlapping cohort as` this record: STAGE Tasks 2 and 3 use the same 400 OCT volumes and expose different labels. ([evidence](https://aistudio.baidu.com/aistudio/competition/detail/968/0/datasets))
- This record is `same or overlapping cohort as` [stage_task1](./stage_task1.md): STAGE Tasks 1 and 3 use the same 400 OCT volumes and expose different labels. ([evidence](https://aistudio.baidu.com/aistudio/competition/detail/968/0/datasets))
- This record is `same or overlapping cohort as` [stage_task2](./stage_task2.md): STAGE Tasks 2 and 3 use the same 400 OCT volumes and expose different labels. ([evidence](https://aistudio.baidu.com/aistudio/competition/detail/968/0/datasets))

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download stage_task3 --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download stage_task3 --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('stage_task3')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [aistudio.baidu.com/aistudio](https://aistudio.baidu.com/aistudio/competition/detail/968/0/datasets)

**Source-term evidence:** [aistudio.baidu.com/aistudio](https://aistudio.baidu.com/aistudio/competition/detail/968/0/datasets)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('stage_task3')
samples = ds.load(data_dir, split='test')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{stage_task3,
  title  = { STAGE 2023 Task 3 — Pattern Deviation Probability Map },
  note   = { MICCAI 2023 STAGE Challenge. https://aistudio.baidu.com/aistudio/competition/detail/968 },
  year   = { 2023 },
  url    = { https://aistudio.baidu.com/aistudio/competition/detail/968/0/datasets },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
MICCAI 2023 STAGE Challenge. https://aistudio.baidu.com/aistudio/competition/detail/968
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Non-commercial research (Baidu AI Studio)
- **Normalized category:** `research-only`
- **Apparent scope:** `unknown`
- **Descriptive screening label:** Research or challenge restriction recorded; check source

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [grape](./grape.md): GRAPE: Glaucoma Real-world Appraisal Progression Ensemble (1,115 examinations, `cc0`)
- [harvard_gdp](./harvard_gdp.md): Harvard GDP: Glaucoma Detection and Progression Dataset (1,000 participants, `cc-by-nc-nd`)
- [stage_task1](./stage_task1.md): STAGE 2023 Task 1 — Mean Deviation Prediction from OCT (400 volumes, `research-only`)
- [stage_task2](./stage_task2.md): STAGE 2023 Task 2 — Visual Field Sensitivity Map Prediction (400 volumes, `research-only`)
- [syn_oct](./syn_oct.md): SYN-OCT Synthetic Glaucoma OCT Dataset (200,000 images, `cc-by`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (103,959 images, `mit`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [kermany_oct](./kermany_oct.md): Kermany OCT 2018: Retinal OCT Image Classification (84,484 images, `cc-by`)
