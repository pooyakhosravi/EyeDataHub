---
id: amdnet23
title: "AMDNet23 Fundus Image Dataset for AMD Detection"
sidebar_label: amdnet23
description: "Two thousand preprocessed fundus images compiled from six public sources for normal, diabetes, cataract, and age-related macular degeneration classification."
tags: ["fundus", "cc-by", "mendeley", "classification", "resource-role-derivative-dataset", "dataset-family-amdnet23", "documented-relationship", "relationship-derived_from"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# AMDNet23 Fundus Image Dataset for AMD Detection

Two thousand preprocessed fundus images compiled from six public sources for normal, diabetes, cataract, and age-related macular degeneration classification.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `amdnet23` |
| **Full name** | AMDNet23 Fundus Image Dataset for AMD Detection |
| **Publication date** | 2025-04-23 |
| **Date basis** | Initial dataset release |
| **Publication date precision** | day |
| **Publication date evidence** | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/yj35kjgrv3/1) |
| **Publication date source field** | citation_publication_date (version 1) |
| **Publication date reviewed** | 2026-09-11 |
| **Date notes** | - |
| **Primary category** | `fundus` |
| **Resource role** | `derivative_dataset` |
| **Dataset family** | `amdnet23` |
| **Contained modalities** | fundus |
| **Tasks** | classification |
| **Primary reported quantity** | 2,000 images |
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

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 2,000 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/yj35kjgrv3/1) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Composite/preprocessed dataset compiled from ODIR, DR_200, Fundus Dataset, RFMiD, HRF, and ARIA; avoid treating it as an independent primary cohort.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- This record is `derived from` [hrf](./hrf.md): AMDNet23 compiles preprocessed images from ODIR, RFMiD, HRF, ARIA, DR_200, and Fundus Dataset. ([evidence](https://doi.org/10.17632/yj35kjgrv3.1))
- This record is `derived from` [odir2019](./odir2019.md): AMDNet23 compiles preprocessed images from ODIR, RFMiD, HRF, ARIA, DR_200, and Fundus Dataset. ([evidence](https://doi.org/10.17632/yj35kjgrv3.1))
- This record is `derived from` [rfmid](./rfmid.md): AMDNet23 compiles preprocessed images from ODIR, RFMiD, HRF, ARIA, DR_200, and Fundus Dataset. ([evidence](https://doi.org/10.17632/yj35kjgrv3.1))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download amdnet23 --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download amdnet23 --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('amdnet23')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/yj35kjgrv3/1)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/yj35kjgrv3/1)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{amdnet23,
  title  = { AMDNet23 Fundus Image Dataset for AMD Detection },
  note   = { Ali MA. AMDNet23: Fundus Image Dataset for Age-Related Macular Degeneration Disease Detection. Mendeley Data, V1, 2025. doi:10.17632/yj35kjgrv3.1 },
  year   = { 2025 },
  url    = { https://data.mendeley.com/datasets/yj35kjgrv3/1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Ali MA. AMDNet23: Fundus Image Dataset for Age-Related Macular Degeneration Disease Detection. Mendeley Data, V1, 2025. doi:10.17632/yj35kjgrv3.1
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
