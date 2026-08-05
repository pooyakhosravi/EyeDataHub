---
id: mendeley_hvdropdb_datasets_classification_segmentation_research_retinopathy
title: "HVDROPDB Datasets for Classification and Segmentation for Research in Retinopathy of Prematurity, Ranjana Agrawal"
sidebar_label: mendeley_hvdropdb_datasets_classification_segmentation_research_retinopathy
description: "Human/derived image or image-annotation observations. from Preterm infants screened at H.V. Desai Eye Hospital."
tags: ["fundus", "cc-by", "mendeley", "segmentation", "resource-role-current-dataset", "dataset-family-mendeley-hvdropdb-datasets-classification-segmentation-research-retinopathy"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# HVDROPDB Datasets for Classification and Segmentation for Research in Retinopathy of Prematurity, Ranjana Agrawal

Human/derived image or image-annotation observations. from Preterm infants screened at H.V. Desai Eye Hospital.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mendeley_hvdropdb_datasets_classification_segmentation_research_retinopathy` |
| **Full name** | HVDROPDB Datasets for Classification and Segmentation for Research in Retinopathy of Prematurity, Ranjana Agrawal |
| **Primary category** | `fundus` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `mendeley_hvdropdb_datasets_classification_segmentation_research_retinopathy` |
| **Contained modalities** | fundus |
| **Tasks** | segmentation |
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
| **Availability** | `available` (checked 2026-08-02) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

No reproducible primary item count was exposed for the cataloged source version.

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Human provenance: Preterm infants screened at H.V. Desai Eye Hospital. Source-review finding: RetCam/Neo fundus images; ROP/normal classification and expert manual segmentation ground truth.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mendeley_hvdropdb_datasets_classification_segmentation_research_retinopathy --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download mendeley_hvdropdb_datasets_classification_segmentation_research_retinopathy --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mendeley_hvdropdb_datasets_classification_segmentation_research_retinopathy')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/xw5xc7xrmp/3)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/xw5xc7xrmp)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mendeley_hvdropdb_datasets_classification_segmentation_research_retinopathy,
  title  = { HVDROPDB Datasets for Classification and Segmentation for Research in Retinopathy of Prematurity, Ranjana Agrawal },
  note   = { HVDROPDB Datasets for Classification and Segmentation for Research in Retinopathy of Prematurity, Ranjana Agrawal. Mendeley Data, V3. doi:10.17632/xw5xc7xrmp.3 },
  url    = { https://data.mendeley.com/datasets/xw5xc7xrmp/3 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
HVDROPDB Datasets for Classification and Segmentation for Research in Retinopathy of Prematurity, Ranjana Agrawal. Mendeley Data, V3. doi:10.17632/xw5xc7xrmp.3.
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
