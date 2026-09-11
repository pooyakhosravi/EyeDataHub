---
id: afio_fundus_vessels
title: "AFIO Fundus Images for Vessel Segmentation and Disease Annotation"
sidebar_label: afio_fundus_vessels
description: "One hundred retinal fundus images from Armed Forces Institute of Ophthalmology, Rawalpindi, with expert annotations for vessels and hypertensive retinopathy, diabetic retinopathy, and papilledema task"
tags: ["fundus", "cc-by", "mendeley", "segmentation", "classification", "resource-role-current-dataset", "dataset-family-afio-fundus-vessels"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# AFIO Fundus Images for Vessel Segmentation and Disease Annotation

One hundred retinal fundus images from Armed Forces Institute of Ophthalmology, Rawalpindi, with expert annotations for vessels and hypertensive retinopathy, diabetic retinopathy, and papilledema tasks.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `afio_fundus_vessels` |
| **Full name** | AFIO Fundus Images for Vessel Segmentation and Disease Annotation |
| **Publication date** | 2019-11-05 |
| **Date basis** | Initial dataset release |
| **Publication date precision** | day |
| **Publication date evidence** | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/3csr652p9y/1) |
| **Publication date source field** | citation_publication_date (version 1) |
| **Publication date reviewed** | 2026-09-11 |
| **Date notes** | - |
| **Primary category** | `fundus` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `afio_fundus_vessels` |
| **Contained modalities** | fundus |
| **Tasks** | segmentation, classification |
| **Primary reported quantity** | 100 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.2 GB |
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
| Primary | 100 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/3csr652p9y/2) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Mendeley Data platform credentials or access setup may be required for automated listing or download requests; verify the current route before acquisition.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download afio_fundus_vessels --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download afio_fundus_vessels --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('afio_fundus_vessels')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/3csr652p9y/2)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/3csr652p9y/2)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{afio_fundus_vessels,
  title  = { AFIO Fundus Images for Vessel Segmentation and Disease Annotation },
  note   = { Akram MU et al. Data on Fundus Images for Vessels Segmentation, Detection of Hypertensive Retinopathy, Diabetic Retinopathy and Papilledema. Mendeley Data, V2, 2019. doi:10.17632/3csr652p9y.2 },
  year   = { 2019 },
  url    = { https://data.mendeley.com/datasets/3csr652p9y/2 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Akram MU et al. Data on Fundus Images for Vessels Segmentation, Detection of Hypertensive Retinopathy, Diabetic Retinopathy and Papilledema. Mendeley Data, V2, 2019. doi:10.17632/3csr652p9y.2
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
