---
id: drtid
title: "DRTiD: Diabetic Retinopathy Two-field Image Dataset"
sidebar_label: drtid
description: "3,100 paired two-field fundus images with DR grading labels. Only public two-field paired DR benchmark."
tags: ["fundus", "research-only", "manual", "grading", "classification", "resource-role-current-dataset", "dataset-family-drtid"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# DRTiD: Diabetic Retinopathy Two-field Image Dataset

3,100 paired two-field fundus images with DR grading labels. Only public two-field paired DR benchmark.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `drtid` |
| **Full name** | DRTiD: Diabetic Retinopathy Two-field Image Dataset |
| **Primary category** | `fundus` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `drtid` |
| **Contained modalities** | fundus |
| **Tasks** | grading, classification |
| **Primary reported quantity** | 3,100 images |
| **Classes** | 5 (Not reported) |
| **Splits** | train, test |
| **Size** | 3.0 GB |
| **Source-stated terms** | Research only (application form) |
| **Normalized terms** | `research-only` |
| **Descriptive screening label** | Research or challenge restriction recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `controlled_or_manual` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `manual_access_blocked` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 3,100 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [github.com/FDU-VTS](https://github.com/FDU-VTS/DRTiD) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Wenjuanxing application form — no auto path.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# This route requires upstream human action; no transfer starts.
eyehub download drtid --data-dir ./data --dry-run --json
# Follow the official instructions shown by preflight.
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('drtid')
print(preflight_dataset(ds, './data'))  # returns manual_access_blocked
```

  </TabItem>
</Tabs>

**Upstream page:** [github.com/FDU-VTS](https://github.com/FDU-VTS/DRTiD)

**Source-term evidence:** [github.com/FDU-VTS](https://github.com/FDU-VTS/DRTiD)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{drtid,
  title  = { DRTiD: Diabetic Retinopathy Two-field Image Dataset },
  note   = { Hou et al., 'Cross-Field Transformer for Diabetic Retinopathy Grading on Two-field Fundus Images', IEEE BIBM 2022. arXiv:2211.14552 },
  year   = { 2022 },
  url    = { https://github.com/FDU-VTS/DRTiD },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Hou et al., 'Cross-Field Transformer for Diabetic Retinopathy Grading on Two-field Fundus Images', IEEE BIBM 2022. arXiv:2211.14552
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Research only (application form)
- **Normalized category:** `research-only`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Research or challenge restriction recorded; check source

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
