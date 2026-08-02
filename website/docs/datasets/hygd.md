---
id: hygd
title: "HYGD: Hillel Yaffe Glaucoma Dataset"
sidebar_label: hygd
description: "747 fundus images from 288 patients with glaucoma labels confirmed by paired OCT + visual field. First public dataset with gold-standard multimodal glaucoma confirmation."
tags: ["fundus", "odc-by", "physionet", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# HYGD: Hillel Yaffe Glaucoma Dataset

747 fundus images from 288 patients with glaucoma labels confirmed by paired OCT + visual field. First public dataset with gold-standard multimodal glaucoma confirmation.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `hygd` |
| **Full name** | HYGD: Hillel Yaffe Glaucoma Dataset |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | classification |
| **Primary reported quantity** | 747 images |
| **Classes** | 2 (non_glaucoma, glaucoma) |
| **Splits** | all |
| **Size** | 1.0 GB |
| **Source-stated terms** | ODC-BY 1.0 (Open Data Commons Attribution) |
| **Normalized terms** | `odc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | PhysioNet |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `end_to_end_tested` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 747 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [https://doi.org/10.13026/pdxv-m215](https://doi.org/10.13026/pdxv-m215) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Open-access (ODC-BY) — no PhysioNet credentialing required.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download hygd --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download hygd --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('hygd')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.13026/pdxv-m215](https://doi.org/10.13026/pdxv-m215)

**Source-term evidence:** [https://doi.org/10.13026/pdxv-m215](https://doi.org/10.13026/pdxv-m215)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{hygd,
  title  = { HYGD: Hillel Yaffe Glaucoma Dataset },
  note   = { Hillel Yaffe Glaucoma Dataset, PhysioNet 2024 (v1.1.0). Labels gold-standardized via OCT + visual field. doi:10.13026/pdxv-m215 },
  year   = { 2024 },
  url    = { https://doi.org/10.13026/pdxv-m215 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Hillel Yaffe Glaucoma Dataset, PhysioNet 2024 (v1.1.0). Labels gold-standardized via OCT + visual field. doi:10.13026/pdxv-m215
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** ODC-BY 1.0 (Open Data Commons Attribution)
- **Normalized category:** `odc-by`
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
