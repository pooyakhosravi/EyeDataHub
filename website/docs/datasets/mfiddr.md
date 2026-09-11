---
id: mfiddr
title: "MFIDDR: Multi-Field Imaging Dataset for Diabetic Retinopathy"
sidebar_label: mfiddr
description: "34,452 fundus images from 4,344 patients across multiple fields per eye, with DR screening labels. Largest public four-field DR dataset."
tags: ["fundus", "mit", "manual", "grading", "classification", "multilabel", "resource-role-current-dataset", "dataset-family-mfiddr"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# MFIDDR: Multi-Field Imaging Dataset for Diabetic Retinopathy

34,452 fundus images from 4,344 patients across multiple fields per eye, with DR screening labels. Largest public four-field DR dataset.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mfiddr` |
| **Full name** | MFIDDR: Multi-Field Imaging Dataset for Diabetic Retinopathy |
| **Publication date** | Unknown |
| **Date basis** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Date notes** | - |
| **Primary category** | `fundus` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `mfiddr` |
| **Contained modalities** | fundus |
| **Tasks** | grading, classification, multilabel |
| **Primary reported quantity** | 34,452 images |
| **Classes** | 5 (Not reported) |
| **Splits** | train, test |
| **Size** | 30.0 GB |
| **Source-stated terms** | MIT (form-gated download) |
| **Normalized terms** | `mit` |
| **Descriptive screening label** | Standard label without an explicit NC clause; verify that it applies to data |
| **Terms scope** | `unknown` |
| **Access friction** | `controlled_or_manual` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `manual_access_blocked` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 34,452 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [github.com/mfiddr](https://github.com/mfiddr/MFIDDR) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Google Form gates the Drive link — no static download ID.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# This route requires upstream human action; no transfer starts.
eyehub download mfiddr --data-dir ./data --dry-run --json
# Follow the official instructions shown by preflight.
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mfiddr')
print(preflight_dataset(ds, './data'))  # returns manual_access_blocked
```

  </TabItem>
</Tabs>

**Upstream page:** [github.com/mfiddr](https://github.com/mfiddr/MFIDDR)

**Source-term evidence:** [github.com/mfiddr](https://github.com/mfiddr/MFIDDR)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mfiddr,
  title  = { MFIDDR: Multi-Field Imaging Dataset for Diabetic Retinopathy },
  note   = { MFIDDR Multi-Field Imaging Dataset for DR. github.com/mfiddr/MFIDDR },
  url    = { https://github.com/mfiddr/MFIDDR },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
MFIDDR Multi-Field Imaging Dataset for DR. github.com/mfiddr/MFIDDR
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** MIT (form-gated download)
- **Normalized category:** `mit`
- **Apparent scope:** `unknown`
- **Descriptive screening label:** Standard label without an explicit NC clause; verify that it applies to data

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [airogs](./airogs.md): AIROGS: AI for Robust Glaucoma Screening (113,893 images, `cc-by-nc-nd`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (103,959 images, `mit`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [justraigs](./justraigs.md): JustRAIGS: Just Referral AI Glaucoma Screening Dataset (101,442 images, `cc-by-nc-nd`)
- [eyepacs](./eyepacs.md): EyePACS — Diabetic Retinopathy Detection (Kaggle 2015) (88,702 images, `research-only`)
- [angioreport](./angioreport.md): AngioReport Fundus Angiography Report Dataset (55,361 images, `unknown`)
- [ffa_ir](./ffa_ir.md): FFA-IR Medical Report Dataset (47,247 images, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
