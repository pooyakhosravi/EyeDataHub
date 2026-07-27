---
id: stage_task2
title: "STAGE 2023 Task 2 — Visual Field Sensitivity Map Prediction"
sidebar_label: stage_task2
description: "400 macular OCT volumes; predict 52-point Humphrey 24-2 visual field sensitivity map (0–100 dB per point). Multi-output regression."
tags: ["oct", "visual_field", "research-only", "manual", "regression"]
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
| **Primary category** | `oct` |
| **Contained modalities** | oct, visual_field |
| **Tasks** | regression |
| **Samples** | 400 |
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


## Notes

> Labels in task2_GT_training.xlsx (52 columns per sample). All 3 tasks share the same OCT volume set.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download stage_task2 --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download stage_task2 --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('stage_task2')
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

## Related datasets with shared modalities

- [grape](./grape.md): GRAPE: Glaucoma Real-world Appraisal Progression Ensemble (1,115 records, `cc0`)
- [harvard_gdp](./harvard_gdp.md): Harvard GDP: Glaucoma Detection and Progression Dataset (1,000 records, `cc-by-nc-nd`)
- [stage_task1](./stage_task1.md): STAGE 2023 Task 1 — Mean Deviation Prediction from OCT (400 records, `research-only`)
- [stage_task3](./stage_task3.md): STAGE 2023 Task 3 — Pattern Deviation Probability Map (400 records, `research-only`)
- [syn_oct](./syn_oct.md): SYN-OCT Synthetic Glaucoma OCT Dataset (200,000 records, `cc-by`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 records, `unknown`)
- [kermany_oct](./kermany_oct.md): Kermany OCT 2018: Retinal OCT Image Classification (84,484 records, `cc-by`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (58,036 records, `mit`)
