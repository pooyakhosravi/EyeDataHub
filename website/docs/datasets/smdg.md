---
id: smdg
title: "SMDG-19: Standardized Multi-channel Glaucoma Benchmark"
sidebar_label: smdg
description: "~12,000 fundus images aggregated from 19 public glaucoma datasets with standardized disc/cup/vessel channels and unified labels. CC0 — fully public domain."
tags: ["fundus", "cc0", "kaggle", "classification", "segmentation", "resource-role-derivative-dataset", "dataset-family-smdg", "documented-relationship", "relationship-derived_from"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# SMDG-19: Standardized Multi-channel Glaucoma Benchmark

~12,000 fundus images aggregated from 19 public glaucoma datasets with standardized disc/cup/vessel channels and unified labels. CC0 — fully public domain.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `smdg` |
| **Full name** | SMDG-19: Standardized Multi-channel Glaucoma Benchmark |
| **First published** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Primary category** | `fundus` |
| **Resource role** | `derivative_dataset` |
| **Dataset family** | `smdg` |
| **Contained modalities** | fundus |
| **Tasks** | classification, segmentation |
| **Primary reported quantity** | 12,449 images |
| **Classes** | 3 (non_glaucoma, glaucoma, suspect) |
| **Splits** | train, val, test |
| **Size** | 5.0 GB |
| **Source-stated terms** | CC0 1.0 (Public Domain) |
| **Normalized terms** | `cc0` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Kaggle |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 12,449 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [kaggle.com/datasets](https://www.kaggle.com/datasets/deathtrooper/multichannel-glaucoma-benchmark-dataset) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Aggregator — overlaps with several EyeDataHub-indexed glaucoma datasets. Useful for unified multi-source training.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- This record is `derived from` [airogs](./airogs.md): The official SMDG source table lists this catalog record among the 19 standardized source domains. ([evidence](https://www.kaggle.com/datasets/deathtrooper/multichannel-glaucoma-benchmark-dataset))
- This record is `derived from` [beh](./beh.md): The official SMDG source table lists this catalog record among the 19 standardized source domains. ([evidence](https://www.kaggle.com/datasets/deathtrooper/multichannel-glaucoma-benchmark-dataset))
- This record is `derived from` [drishti_gs](./drishti_gs.md): The official SMDG source table lists this catalog record among the 19 standardized source domains. ([evidence](https://www.kaggle.com/datasets/deathtrooper/multichannel-glaucoma-benchmark-dataset))
- This record is `derived from` [fives](./fives.md): The official SMDG source table lists this catalog record among the 19 standardized source domains. ([evidence](https://www.kaggle.com/datasets/deathtrooper/multichannel-glaucoma-benchmark-dataset))
- This record is `derived from` [g1020](./g1020.md): The official SMDG source table lists this catalog record among the 19 standardized source domains. ([evidence](https://www.kaggle.com/datasets/deathtrooper/multichannel-glaucoma-benchmark-dataset))
- This record is `derived from` [hrf](./hrf.md): The official SMDG source table lists this catalog record among the 19 standardized source domains. ([evidence](https://www.kaggle.com/datasets/deathtrooper/multichannel-glaucoma-benchmark-dataset))
- This record is `derived from` [jsiec](./jsiec.md): The official SMDG source table lists this catalog record among the 19 standardized source domains. ([evidence](https://www.kaggle.com/datasets/deathtrooper/multichannel-glaucoma-benchmark-dataset))
- This record is `derived from` [odir2019](./odir2019.md): The official SMDG source table lists this catalog record among the 19 standardized source domains. ([evidence](https://www.kaggle.com/datasets/deathtrooper/multichannel-glaucoma-benchmark-dataset))
- This record is `derived from` [papila](./papila.md): The official SMDG source table lists this catalog record among the 19 standardized source domains. ([evidence](https://www.kaggle.com/datasets/deathtrooper/multichannel-glaucoma-benchmark-dataset))
- This record is `derived from` [refuge2](./refuge2.md): The official SMDG source table lists this catalog record among the 19 standardized source domains. ([evidence](https://www.kaggle.com/datasets/deathtrooper/multichannel-glaucoma-benchmark-dataset))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download smdg --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download smdg --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('smdg')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [kaggle.com/datasets](https://www.kaggle.com/datasets/deathtrooper/multichannel-glaucoma-benchmark-dataset)

**Source-term evidence:** [kaggle.com/datasets](https://www.kaggle.com/datasets/deathtrooper/multichannel-glaucoma-benchmark-dataset)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{smdg,
  title  = { SMDG-19: Standardized Multi-channel Glaucoma Benchmark },
  note   = { Kiefer, 'Standardized Multi-channel Dataset for Glaucoma (SMDG-19)', Kaggle 2022. Breakdown: 7,499 non-glaucoma + 4,817 glaucoma + 133 suspect },
  year   = { 2022 },
  url    = { https://www.kaggle.com/datasets/deathtrooper/multichannel-glaucoma-benchmark-dataset },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Kiefer, 'Standardized Multi-channel Dataset for Glaucoma (SMDG-19)', Kaggle 2022. Breakdown: 7,499 non-glaucoma + 4,817 glaucoma + 133 suspect.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC0 1.0 (Public Domain)
- **Normalized category:** `cc0`
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
