---
id: mendeley_annotated_infant_fundus_images_object_detection
title: "Annotated Infant Fundus Images for Object Detection of Key Structures (Optic Disk and Macula)"
sidebar_label: mendeley_annotated_infant_fundus_images_object_detection
description: "Observation-level source data, annotations, or signals. from Source describes de-identified infant fundus images."
tags: ["fundus", "cc-by", "mendeley", "segmentation", "resource-role-current-dataset", "dataset-family-mendeley-annotated-infant-fundus-images-object-detection"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Annotated Infant Fundus Images for Object Detection of Key Structures (Optic Disk and Macula)

Observation-level source data, annotations, or signals. from Source describes de-identified infant fundus images.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mendeley_annotated_infant_fundus_images_object_detection` |
| **Full name** | Annotated Infant Fundus Images for Object Detection of Key Structures (Optic Disk and Macula) |
| **Publication date** | 2021-03-16 |
| **Date basis** | Initial dataset release |
| **Publication date precision** | day |
| **Publication date evidence** | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/9kvk7nkhx6/1) |
| **Publication date source field** | citation_publication_date (version 1) |
| **Publication date reviewed** | 2026-09-11 |
| **Date notes** | - |
| **Primary category** | `fundus` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `mendeley_annotated_infant_fundus_images_object_detection` |
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

> Human provenance: Source describes de-identified infant fundus images. Source-review finding: 3,010 files including 3,002 JPG images, HDF5 annotations, XLSX, ZIP, and documentation.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mendeley_annotated_infant_fundus_images_object_detection --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download mendeley_annotated_infant_fundus_images_object_detection --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mendeley_annotated_infant_fundus_images_object_detection')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/9kvk7nkhx6/4)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/9kvk7nkhx6)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mendeley_annotated_infant_fundus_images_object_detection,
  title  = { Annotated Infant Fundus Images for Object Detection of Key Structures (Optic Disk and Macula) },
  note   = { Annotated Infant Fundus Images for Object Detection of Key Structures (Optic Disk and Macula). Mendeley Data, V4. doi:10.17632/9kvk7nkhx6.4 },
  url    = { https://data.mendeley.com/datasets/9kvk7nkhx6/4 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Annotated Infant Fundus Images for Object Detection of Key Structures (Optic Disk and Macula). Mendeley Data, V4. doi:10.17632/9kvk7nkhx6.4.
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
