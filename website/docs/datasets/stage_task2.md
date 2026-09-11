---
id: stage_task2
title: "STAGE 2023 Task 2 — Visual Field Sensitivity Map Prediction"
sidebar_label: stage_task2
description: "400 macular OCT volumes; predict 52-point Humphrey 24-2 visual field sensitivity map (0–100 dB per point). Multi-output regression."
tags: ["oct", "visual_field", "research-only", "manual", "regression", "resource-role-task-view", "dataset-family-stage-2023", "documented-relationship", "relationship-derived_from", "relationship-same_or_overlapping_cohort_as"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# STAGE 2023 Task 2 — Visual Field Sensitivity Map Prediction

400 macular OCT volumes; predict 52-point Humphrey 24-2 visual field sensitivity map (0–100 dB per point). Multi-output regression.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `stage_task2` |
| **Full name** | STAGE 2023 Task 2 — Visual Field Sensitivity Map Prediction |
| **First published** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Primary category** | `oct` |
| **Resource role** | `task_view` |
| **Dataset family** | `stage_2023` |
| **Contained modalities** | oct, visual_field |
| **Tasks** | regression |
| **Primary reported quantity** | 400 volumes |
| **Classes** | 52 (VF_01, VF_02, VF_03, VF_04, VF_05, VF_06, VF_07, VF_08, VF_09, VF_10, VF_11, VF_12, VF_13, VF_14, VF_15, VF_16, VF_17, VF_18, VF_19, VF_20, VF_21, VF_22, VF_23, VF_24, VF_25, VF_26, VF_27, VF_28, VF_29, VF_30, VF_31, VF_32, VF_33, VF_34, VF_35, VF_36, VF_37, VF_38, VF_39, VF_40, VF_41, VF_42, VF_43, VF_44, VF_45, VF_46, VF_47, VF_48, VF_49, VF_50, VF_51, VF_52) |
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

## Notes

> Labels in task2_GT_training.xlsx (52 columns per sample). All 3 tasks share the same OCT volume set.

## Dataset family

This record belongs to `stage_2023`. Family links group documented collection/component records or exact task views; they do not imply independent cohorts.

- [stage_task1](./stage_task1.md): STAGE 2023 Task 1 — Mean Deviation Prediction from OCT (`task_view`)
- [stage_task3](./stage_task3.md): STAGE 2023 Task 3 — Pattern Deviation Probability Map (`task_view`)

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- [mm_retinal_reason](./mm_retinal_reason.md) is `derived from` this record: The version-pinned official dataset card lists this record among the CFP or OCT sources used to construct MM-Retinal-Reason. ([evidence](https://huggingface.co/datasets/lxirich/MM-Retinal-Reason/tree/d6243baa82c0914dba3c6f43ca79fdbf856982ef))
- This record has a documented `same or overlapping cohort as` relationship with [stage_task1](./stage_task1.md): STAGE Tasks 1 and 2 use the same 400 OCT volumes and expose different labels. ([evidence](https://aistudio.baidu.com/aistudio/competition/detail/968/0/datasets))
- This record has a documented `same or overlapping cohort as` relationship with [stage_task3](./stage_task3.md): STAGE Tasks 2 and 3 use the same 400 OCT volumes and expose different labels. ([evidence](https://aistudio.baidu.com/aistudio/competition/detail/968/0/datasets))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download stage_task2 --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download stage_task2 --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('stage_task2')
print(preflight_dataset(ds, './data'))  # no download
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
ds = REGISTRY.get_dataset('stage_task2')
samples = ds.load(data_dir, split='test')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{stage_task2,
  title  = { STAGE 2023 Task 2 — Visual Field Sensitivity Map Prediction },
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
- [stage_task3](./stage_task3.md): STAGE 2023 Task 3 — Pattern Deviation Probability Map (400 volumes, `research-only`)
- [syn_oct](./syn_oct.md): SYN-OCT Synthetic Glaucoma OCT Dataset (200,000 images, `cc-by`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (103,959 images, `mit`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [kermany_oct](./kermany_oct.md): Kermany OCT 2018: Retinal OCT Image Classification (84,484 images, `cc-by`)
