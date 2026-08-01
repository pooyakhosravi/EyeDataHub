---
id: irfdrd
title: "Iraqi Retinal Fundus Diabetic Retinopathy Dataset"
sidebar_label: irfdrd
description: "Retinal fundus dataset for five-class diabetic-retinopathy grading."
tags: ["fundus", "cc-by", "zenodo", "classification", "grading"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Iraqi Retinal Fundus Diabetic Retinopathy Dataset

Retinal fundus dataset for five-class diabetic-retinopathy grading.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `irfdrd` |
| **Full name** | Iraqi Retinal Fundus Diabetic Retinopathy Dataset |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | classification, grading |
| **Primary reported quantity** | 700 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Zenodo |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 700 | `images` | JPEG files in the three nested class archives Archive listing resolves a conflicting class table in the source description: 153 healthy, 59 mild, 304 moderate, 99 severe, and 85 PDR files. | `current_deposit_file_listing` | [zenodo.org/records](https://zenodo.org/records/12552326) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download irfdrd --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download irfdrd --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('irfdrd')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [zenodo.org/records](https://zenodo.org/records/12552326)

**Source-term evidence:** [zenodo.org/records](https://zenodo.org/records/12552326)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{irfdrd,
  title  = { Iraqi Retinal Fundus Diabetic Retinopathy Dataset },
  note   = { Iraqi Retinal Fundus Diabetic Retinopathy Dataset. Zenodo, 2024. doi:10.5281/zenodo.12552326 },
  year   = { 2024 },
  url    = { https://zenodo.org/records/12552326 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Iraqi Retinal Fundus Diabetic Retinopathy Dataset. Zenodo, 2024. doi:10.5281/zenodo.12552326
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
- [bidr](./bidr.md): BiDR: Diabetic Retinopathy Diagnosis Dataset (35,126 images, `unknown`)
