---
id: fiqs
title: "FIQS: Fundus Image Quality Scores Dataset"
sidebar_label: fiqs
description: "A set of 2,246 fundus images with continuous mean opinion scores from 0 to 100, three quality grades, and the individual scores of six ophthalmologists."
tags: ["fundus", "cc-by", "figshare", "quality", "grading", "regression", "resource-role-current-dataset", "dataset-family-fiqs"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# FIQS: Fundus Image Quality Scores Dataset

A set of 2,246 fundus images with continuous mean opinion scores from 0 to 100, three quality grades, and the individual scores of six ophthalmologists.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `fiqs` |
| **Full name** | FIQS: Fundus Image Quality Scores Dataset |
| **Primary category** | `fundus` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `fiqs` |
| **Contained modalities** | fundus |
| **Tasks** | quality, grading, regression |
| **Primary reported quantity** | 2,246 images |
| **Classes** | 3 (good, usable, reject) |
| **Splits** | all |
| **Size** | 9.07 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Figshare |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `end_to_end_tested` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 2,246 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [https://doi.org/10.6084/m9.figshare.28129847.v1](https://doi.org/10.6084/m9.figshare.28129847.v1) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> The deposit provides original resolution images, standardized 1024 by 1024 versions, aggregate scores, and individual grader scores.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download fiqs --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download fiqs --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('fiqs')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.6084/m9.figshare.28129847.v1](https://doi.org/10.6084/m9.figshare.28129847.v1)

**Source-term evidence:** [https://doi.org/10.6084/m9.figshare.28129847.v1](https://doi.org/10.6084/m9.figshare.28129847.v1)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{fiqs,
  title  = { FIQS: Fundus Image Quality Scores Dataset },
  note   = { Gong Z. FIQS Dataset (Fundus Image Quality Scores). Figshare. 2025. doi:10.6084/m9.figshare.28129847.v1 },
  year   = { 2025 },
  url    = { https://doi.org/10.6084/m9.figshare.28129847.v1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Gong Z. FIQS Dataset (Fundus Image Quality Scores). Figshare. 2025. doi:10.6084/m9.figshare.28129847.v1
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

- [airogs](./airogs.md): AIROGS: AI for Robust Glaucoma Screening (113,893 images, `cc-by-nc-nd`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (103,959 images, `mit`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [justraigs](./justraigs.md): JustRAIGS: Just Referral AI Glaucoma Screening Dataset (101,442 images, `cc-by-nc-nd`)
- [eyepacs](./eyepacs.md): EyePACS — Diabetic Retinopathy Detection (Kaggle 2015) (88,702 images, `research-only`)
- [angioreport](./angioreport.md): AngioReport Fundus Angiography Report Dataset (55,361 images, `unknown`)
- [ffa_ir](./ffa_ir.md): FFA-IR Medical Report Dataset (47,247 images, `unknown`)
- [mfiddr](./mfiddr.md): MFIDDR: Multi-Field Imaging Dataset for Diabetic Retinopathy (34,452 images, `mit`)
