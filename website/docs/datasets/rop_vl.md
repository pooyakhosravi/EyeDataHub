---
id: rop_vl
title: "ROP-VL Retinopathy of Prematurity Vision-Language Dataset"
sidebar_label: rop_vl
description: "Color fundus photographs paired with biological metadata and structured descriptions for retinopathy of prematurity."
tags: ["fundus", "cc-by", "figshare", "classification", "image_text", "resource-role-current-dataset", "dataset-family-rop-vl"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# ROP-VL Retinopathy of Prematurity Vision-Language Dataset

Color fundus photographs paired with biological metadata and structured descriptions for retinopathy of prematurity.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `rop_vl` |
| **Full name** | ROP-VL Retinopathy of Prematurity Vision-Language Dataset |
| **First published** | 2025-09-28 |
| **Publication date precision** | day |
| **Publication date evidence** | [api.figshare.com/v2](https://api.figshare.com/v2/articles/30143461/versions/1) |
| **Publication date source field** | published_date (Figshare version 1) |
| **Publication date reviewed** | 2026-09-11 |
| **Primary category** | `fundus` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `rop_vl` |
| **Contained modalities** | fundus |
| **Tasks** | classification, image_text |
| **Primary reported quantity** | 2,020 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Figshare |
| **Availability** | `available` (checked 2026-08-02) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 2,020 | `images` | Source reports 2,020 color fundus photographs from 1,116 infants. Source-stated quantity; repository file count is separate. | `official_source_description` | [https://doi.org/10.6084/m9.figshare.30143461.v1](https://doi.org/10.6084/m9.figshare.30143461.v1) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Current official metadata has no references or source-image relationship. FARFUM-ROP and ROP Ostrava are cataloged ROP resources, but no internal edge is asserted.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download rop_vl --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download rop_vl --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('rop_vl')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.6084/m9.figshare.30143461.v1](https://doi.org/10.6084/m9.figshare.30143461.v1)

**Source-term evidence:** [https://doi.org/10.6084/m9.figshare.30143461.v1](https://doi.org/10.6084/m9.figshare.30143461.v1)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{rop_vl,
  title  = { ROP-VL Retinopathy of Prematurity Vision-Language Dataset },
  note   = { Repository dataset record. 10.6084/m9.figshare.30143461.v1 },
  url    = { https://doi.org/10.6084/m9.figshare.30143461.v1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Repository dataset record. 10.6084/m9.figshare.30143461.v1.
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
