---
id: eyeq
title: "EyeQ Retinal Image Quality Assessment Dataset"
sidebar_label: eyeq
description: "Quality labels for 28,792 EyePACS fundus images, graded as good, usable, or reject and divided into the original EyePACS train and test partitions."
tags: ["fundus", "unknown", "github", "quality", "grading"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# EyeQ Retinal Image Quality Assessment Dataset

Quality labels for 28,792 EyePACS fundus images, graded as good, usable, or reject and divided into the original EyePACS train and test partitions.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `eyeq` |
| **Full name** | EyeQ Retinal Image Quality Assessment Dataset |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | quality, grading |
| **Samples** | 28,792 |
| **Classes** | 3 (good, usable, reject) |
| **Splits** | train, test |
| **Size** | Not reported |
| **Source-stated terms** | Unknown for released quality labels; code is CC BY-NC-SA 4.0 |
| **Normalized terms** | `unknown` |
| **Descriptive screening label** | Unknown or unclear; do not assume permission |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | GitHub |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `loader_implemented_not_live_tested` |
| **Legacy sample-loader status** | Metadata and access only |


## Notes

> EyeQ is a distinct annotation layer over EyePACS. The repository license covers the code but does not clearly license the quality labels. It does not provide the source images. Users must obtain EyePACS separately and comply with its terms.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download eyeq --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download eyeq --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('eyeq')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [github.com/HzFu](https://github.com/HzFu/EyeQ)

**Source-term evidence:** [github.com/HzFu](https://github.com/HzFu/EyeQ)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{eyeq,
  title  = { EyeQ Retinal Image Quality Assessment Dataset },
  note   = { Fu H, Wang B, Shen J, et al. Evaluation of retinal image quality assessment networks in different color-spaces. MICCAI. 2019. doi:10.1007/978-3-030-32239-7_6 },
  year   = { 2019 },
  url    = { https://github.com/HzFu/EyeQ },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Fu H, Wang B, Shen J, et al. Evaluation of retinal image quality assessment networks in different color-spaces. MICCAI. 2019. doi:10.1007/978-3-030-32239-7_6
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Unknown for released quality labels; code is CC BY-NC-SA 4.0
- **Normalized category:** `unknown`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Unknown or unclear; do not assume permission

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Related datasets with shared modalities

- [airogs](./airogs.md): AIROGS: AI for Robust Glaucoma Screening (113,893 records, `cc-by-nc-nd`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 records, `unknown`)
- [justraigs](./justraigs.md): JustRAIGS: Just Referral AI Glaucoma Screening Dataset (101,442 records, `cc-by-nc-nd`)
- [eyepacs](./eyepacs.md): EyePACS — Diabetic Retinopathy Detection (Kaggle 2015) (88,702 records, `research-only`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (58,036 records, `mit`)
- [angioreport](./angioreport.md): AngioReport Fundus Angiography Report Dataset (55,361 records, `unknown`)
- [ffa_ir](./ffa_ir.md): FFA-IR Medical Report Dataset (47,247 records, `unknown`)
- [bidr](./bidr.md): BiDR: Diabetic Retinopathy Diagnosis Dataset (35,126 records, `unknown`)
