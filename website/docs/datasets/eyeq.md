---
id: eyeq
title: "EyeQ Retinal Image Quality Assessment Dataset"
sidebar_label: eyeq
description: "Quality labels for 28,792 EyePACS fundus images, graded as good, usable, or reject and divided into the original EyePACS train and test partitions."
tags: ["fundus", "unknown", "github", "quality", "grading", "resource-role-annotation-layer", "dataset-family-eyeq", "documented-relationship", "relationship-derived_from"]
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
| **Resource role** | `annotation_layer` |
| **Dataset family** | `eyeq` |
| **Contained modalities** | fundus |
| **Tasks** | quality, grading |
| **Primary reported quantity** | 28,792 images |
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
| **Acquisition support** | `end_to_end_tested` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 28,792 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [github.com/HzFu](https://github.com/HzFu/EyeQ) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> EyeQ is a distinct annotation layer over EyePACS. The repository license covers the code but does not clearly license the quality labels. It does not provide the source images. Users must obtain EyePACS separately and comply with its terms.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- This record is `derived from` [eyepacs](./eyepacs.md): EyeQ provides quality labels for 28,792 images from the EyePACS train and test partitions. ([evidence](https://github.com/HzFu/EyeQ))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download eyeq --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download eyeq --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('eyeq')
print(preflight_dataset(ds, './data'))  # no download
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

## Similar resources by shared modality

- [airogs](./airogs.md): AIROGS: AI for Robust Glaucoma Screening (113,893 images, `cc-by-nc-nd`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (103,959 images, `mit`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [justraigs](./justraigs.md): JustRAIGS: Just Referral AI Glaucoma Screening Dataset (101,442 images, `cc-by-nc-nd`)
- [eyepacs](./eyepacs.md): EyePACS — Diabetic Retinopathy Detection (Kaggle 2015) (88,702 images, `research-only`)
- [angioreport](./angioreport.md): AngioReport Fundus Angiography Report Dataset (55,361 images, `unknown`)
- [ffa_ir](./ffa_ir.md): FFA-IR Medical Report Dataset (47,247 images, `unknown`)
- [mfiddr](./mfiddr.md): MFIDDR: Multi-Field Imaging Dataset for Diabetic Retinopathy (34,452 images, `mit`)
