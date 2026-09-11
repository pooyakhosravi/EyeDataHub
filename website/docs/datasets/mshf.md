---
id: mshf
title: "Multi-Source Heterogeneous Fundus Dataset for Image Quality Assessment"
sidebar_label: mshf
description: "Multi-source heterogeneous retinal fundus image-quality assessment dataset for training and evaluating quality-control models."
tags: ["fundus", "cc-by", "figshare", "quality_assessment", "classification", "resource-role-current-dataset", "dataset-family-mshf"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Multi-Source Heterogeneous Fundus Dataset for Image Quality Assessment

Multi-source heterogeneous retinal fundus image-quality assessment dataset for training and evaluating quality-control models.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mshf` |
| **Full name** | Multi-Source Heterogeneous Fundus Dataset for Image Quality Assessment |
| **First published** | 2022-11-06 |
| **Publication date precision** | day |
| **Publication date evidence** | [api.figshare.com/v2](https://api.figshare.com/v2/articles/21507564/versions/1) |
| **Publication date source field** | published_date (Figshare version 1) |
| **Publication date reviewed** | 2026-09-11 |
| **Primary category** | `fundus` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `mshf` |
| **Contained modalities** | fundus |
| **Tasks** | quality_assessment, classification |
| **Primary reported quantity** | 1,302 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 1.06 GB |
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
| Primary | 1,302 | `images` | Unique source images in the Original directory | `current_deposit_file_listing` | [https://doi.org/10.6084/m9.figshare.21507564](https://doi.org/10.6084/m9.figshare.21507564) |
| Additional | 1,302 | `images` | Train/test analysis copies These are copies of the 1,302 source images and are not an additional cohort. | `current_deposit_file_listing` | [https://doi.org/10.6084/m9.figshare.21507564](https://doi.org/10.6084/m9.figshare.21507564) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Multi-source quality-assessment dataset; review source composition before treating all images as a single independent cohort.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mshf --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download mshf --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mshf')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.6084/m9.figshare.21507564](https://doi.org/10.6084/m9.figshare.21507564)

**Source-term evidence:** [https://doi.org/10.6084/m9.figshare.21507564](https://doi.org/10.6084/m9.figshare.21507564)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mshf,
  title  = { Multi-Source Heterogeneous Fundus Dataset for Image Quality Assessment },
  note   = { Jin K, Gao Z, Jiang X, Wang Y, Ma X, Li Y, Ye J. MSHF: A Multi-Source Heterogeneous Fundus Dataset for Image Quality Assessment. Figshare, 2023. doi:10.6084/m9.figshare.21507564 },
  year   = { 2023 },
  url    = { https://doi.org/10.6084/m9.figshare.21507564 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Jin K, Gao Z, Jiang X, Wang Y, Ma X, Li Y, Ye J. MSHF: A Multi-Source Heterogeneous Fundus Dataset for Image Quality Assessment. Figshare, 2023. doi:10.6084/m9.figshare.21507564
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
