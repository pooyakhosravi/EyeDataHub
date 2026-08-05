---
id: hyamd
title: "HYAMD High-Resolution Fundus Image Dataset for AMD Diagnosis"
sidebar_label: hyamd
description: "High-resolution fundus images from Hillel Yaffe Medical Center for age-related macular degeneration diagnosis."
tags: ["fundus", "unknown", "physionet", "classification", "resource-role-current-dataset", "dataset-family-hyamd"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# HYAMD High-Resolution Fundus Image Dataset for AMD Diagnosis

High-resolution fundus images from Hillel Yaffe Medical Center for age-related macular degeneration diagnosis.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `hyamd` |
| **Full name** | HYAMD High-Resolution Fundus Image Dataset for AMD Diagnosis |
| **Primary category** | `fundus` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `hyamd` |
| **Contained modalities** | fundus |
| **Tasks** | classification |
| **Primary reported quantity** | 1,560 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | PhysioNet Restricted Health Data License 1.5.0 |
| **Normalized terms** | `unknown` |
| **Descriptive screening label** | Unknown or unclear; do not assume permission |
| **Terms scope** | `dataset_files` |
| **Access friction** | `controlled_or_manual` |
| **Route backend** | PhysioNet |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `manual_access_blocked` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 1,560 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [physionet.org/content](https://physionet.org/content/hillel-yaffe-fundus-amd/1.0.0/) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> PhysioNet requires registration and the project-specific Restricted Health Data Use Agreement before file access.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# This route requires upstream human action; no transfer starts.
eyehub download hyamd --data-dir ./data --dry-run --json
# Follow the official instructions shown by preflight.
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('hyamd')
print(preflight_dataset(ds, './data'))  # returns manual_access_blocked
```

  </TabItem>
</Tabs>

**Upstream page:** [physionet.org/content](https://physionet.org/content/hillel-yaffe-fundus-amd/1.0.0/)

**Source-term evidence:** [physionet.org/content](https://physionet.org/content/hillel-yaffe-fundus-amd/1.0.0/)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{hyamd,
  title  = { HYAMD High-Resolution Fundus Image Dataset for AMD Diagnosis },
  note   = { Meisel M, Cohen BA, Baskin M, Tiosano B, Behar J, Berkowitz E. HYAMD High-Resolution Fundus Image Dataset for AMD Diagnosis. PhysioNet, version 1.0.0, 2025. doi:10.13026/ydf1-z238 },
  year   = { 2025 },
  url    = { https://physionet.org/content/hillel-yaffe-fundus-amd/1.0.0/ },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Meisel M, Cohen BA, Baskin M, Tiosano B, Behar J, Berkowitz E. HYAMD High-Resolution Fundus Image Dataset for AMD Diagnosis. PhysioNet, version 1.0.0, 2025. doi:10.13026/ydf1-z238
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** PhysioNet Restricted Health Data License 1.5.0
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
