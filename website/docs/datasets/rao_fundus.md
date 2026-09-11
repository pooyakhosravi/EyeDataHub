---
id: rao_fundus
title: "RAO Retinal Artery Occlusion Fundus Photography Dataset"
sidebar_label: rao_fundus
description: "Fundus-photography dataset for retinal artery occlusion diagnosis, based on web-derived public data and public fundus datasets."
tags: ["fundus", "cc-by", "mendeley", "classification", "resource-role-derivative-dataset", "dataset-family-rao-fundus", "documented-relationship", "relationship-derived_from"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# RAO Retinal Artery Occlusion Fundus Photography Dataset

Fundus-photography dataset for retinal artery occlusion diagnosis, based on web-derived public data and public fundus datasets.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `rao_fundus` |
| **Full name** | RAO Retinal Artery Occlusion Fundus Photography Dataset |
| **First published** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Primary category** | `fundus` |
| **Resource role** | `derivative_dataset` |
| **Dataset family** | `rao_fundus` |
| **Contained modalities** | fundus |
| **Tasks** | classification |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Mendeley Data |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

No reproducible primary item count was exposed for the cataloged source version.

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Source reports use of web-based public data plus RFMiD and JSIEC. Retained as a distinct RAO task resource, but not an independent primary cohort.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- This record is `derived from` [jsiec](./jsiec.md): The RAO source reports use of public web images plus RFMiD and JSIEC images. ([evidence](https://doi.org/10.17632/5428684j44.2))
- This record is `derived from` [rfmid](./rfmid.md): The RAO source reports use of public web images plus RFMiD and JSIEC images. ([evidence](https://doi.org/10.17632/5428684j44.2))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download rao_fundus --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download rao_fundus --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('rao_fundus')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/5428684j44/2)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/5428684j44/2)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{rao_fundus,
  title  = { RAO Retinal Artery Occlusion Fundus Photography Dataset },
  note   = { Yoo T. RAO (retinal artery occlusion) fundus photography dataset. Mendeley Data, V2, 2024. doi:10.17632/5428684j44.2 },
  year   = { 2024 },
  url    = { https://data.mendeley.com/datasets/5428684j44/2 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Yoo T. RAO (retinal artery occlusion) fundus photography dataset. Mendeley Data, V2, 2024. doi:10.17632/5428684j44.2
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
