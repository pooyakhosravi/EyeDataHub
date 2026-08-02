---
id: brasil_glaucoma_brg
title: "Brazil Glaucoma (BrG) Dataset"
sidebar_label: brasil_glaucoma_brg
description: "Portable/smartphone fundus photographs of Brazilian glaucoma and non-glaucoma volunteers."
tags: ["fundus", "cc-by-nc", "kaggle", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Brazil Glaucoma (BrG) Dataset

Portable/smartphone fundus photographs of Brazilian glaucoma and non-glaucoma volunteers.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `brasil_glaucoma_brg` |
| **Full name** | Brazil Glaucoma (BrG) Dataset |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | classification |
| **Primary reported quantity** | 2,000 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | CC BY-NC 4.0 |
| **Normalized terms** | `cc-by-nc` |
| **Descriptive screening label** | Explicit noncommercial clause recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Kaggle |
| **Availability** | `available` (checked 2026-08-02) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 2,000 | `images` | Source article reports 2,000 fundus images from 1,000 volunteers. Source-stated quantity; repository file count is separate. | `official_source_description` | [kaggle.com/datasets](https://www.kaggle.com/datasets/clerimar/brasil-glaucoma-brg) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Kaggle description gives a conflicting image count; the source article quantity is retained.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download brasil_glaucoma_brg --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download brasil_glaucoma_brg --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('brasil_glaucoma_brg')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [kaggle.com/datasets](https://www.kaggle.com/datasets/clerimar/brasil-glaucoma-brg)

**Source-term evidence:** [kaggle.com/datasets](https://www.kaggle.com/datasets/clerimar/brasil-glaucoma-brg)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{brasil_glaucoma_brg,
  title  = { Brazil Glaucoma (BrG) Dataset },
  note   = { Repository dataset record. clerimar/brasil-glaucoma-brg },
  url    = { https://www.kaggle.com/datasets/clerimar/brasil-glaucoma-brg },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Repository dataset record. clerimar/brasil-glaucoma-brg.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC BY-NC 4.0
- **Normalized category:** `cc-by-nc`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Explicit noncommercial clause recorded; check source

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
