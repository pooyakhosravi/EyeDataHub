---
id: trend_fundus
title: "TREND Portable Fundus Microvascular Network Dataset"
sidebar_label: trend_fundus
description: "Portable fundus images and segmentations for retinal microvascular network analysis."
tags: ["fundus", "cc-by", "zenodo", "segmentation", "regression", "resource-role-current-dataset", "dataset-family-trend-fundus", "documented-relationship", "relationship-extension_of"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# TREND Portable Fundus Microvascular Network Dataset

Portable fundus images and segmentations for retinal microvascular network analysis.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `trend_fundus` |
| **Full name** | TREND Portable Fundus Microvascular Network Dataset |
| **First published** | 2021-06-16 |
| **Publication date precision** | day |
| **Publication date evidence** | [zenodo.org/api](https://zenodo.org/api/records/4521044) |
| **Publication date source field** | metadata.publication_date (earliest public Zenodo version) |
| **Publication date reviewed** | 2026-09-11 |
| **Primary category** | `fundus` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `trend_fundus` |
| **Contained modalities** | fundus |
| **Tasks** | segmentation, regression |
| **Primary reported quantity** | 82 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.1 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Zenodo |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 82 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [zenodo.org/records](https://zenodo.org/records/4521044) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- [trend2_fundus](./trend2_fundus.md) is `extension of` this record: TREND2 is described as an addition to the TREND portable-fundus resource. ([evidence](https://zenodo.org/records/7678656))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download trend_fundus --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download trend_fundus --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('trend_fundus')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [zenodo.org/records](https://zenodo.org/records/4521044)

**Source-term evidence:** [zenodo.org/records](https://zenodo.org/records/4521044)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{trend_fundus,
  title  = { TREND Portable Fundus Microvascular Network Dataset },
  note   = { TREND portable fundus microvascular network dataset. Zenodo, 2021. doi:10.5281/zenodo.4521044 },
  year   = { 2021 },
  url    = { https://zenodo.org/records/4521044 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
TREND portable fundus microvascular network dataset. Zenodo, 2021. doi:10.5281/zenodo.4521044
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
