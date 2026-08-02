---
id: rop_uwf_intelligent
title: "Fundus Dataset for Intelligent ROP System"
sidebar_label: rop_uwf_intelligent
description: "1,099 pediatric fundus images from 483 premature infants annotated for retinopathy of prematurity (ROP) staging. Standard fundus (RetCam) — not ultra-widefield; `rop_uwf_intelligent` is retained as th"
tags: ["fundus", "cc-by", "figshare", "grading", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Fundus Dataset for Intelligent ROP System

1,099 pediatric fundus images from 483 premature infants annotated for retinopathy of prematurity (ROP) staging. Standard fundus (RetCam) — not ultra-widefield; `rop_uwf_intelligent` is retained as the registry identifier.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `rop_uwf_intelligent` |
| **Full name** | Fundus Dataset for Intelligent ROP System |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | grading, classification |
| **Primary reported quantity** | 1,099 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 4.0 GB |
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
| Primary | 1,099 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [https://doi.org/10.6084/m9.figshare.25514449](https://doi.org/10.6084/m9.figshare.25514449) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Slug says `uwf` but the paper describes standard RetCam fundus imaging, not ultra-widefield. 1,099 images from 483 infants — earlier metadata claimed ~5,000.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download rop_uwf_intelligent --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download rop_uwf_intelligent --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('rop_uwf_intelligent')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.6084/m9.figshare.25514449](https://doi.org/10.6084/m9.figshare.25514449)

**Source-term evidence:** [https://doi.org/10.6084/m9.figshare.25514449](https://doi.org/10.6084/m9.figshare.25514449)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{rop_uwf_intelligent,
  title  = { Fundus Dataset for Intelligent ROP System },
  note   = { Zhao X, Chen S, Zhang S, et al., 'A fundus image dataset for intelligent retinopathy of prematurity system', Scientific Data 11:543, 2024. doi:10.1038/s41597-024-03362-5 },
  year   = { 2024 },
  url    = { https://doi.org/10.6084/m9.figshare.25514449 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Zhao X, Chen S, Zhang S, et al., 'A fundus image dataset for intelligent retinopathy of prematurity system', Scientific Data 11:543, 2024. doi:10.1038/s41597-024-03362-5
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
