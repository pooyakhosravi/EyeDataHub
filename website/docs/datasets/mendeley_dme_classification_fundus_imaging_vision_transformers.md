---
id: mendeley_dme_classification_fundus_imaging_vision_transformers
title: "DME Classification in Fundus Imaging with Vision Transformers and ETDRS-Guided Annotation"
sidebar_label: mendeley_dme_classification_fundus_imaging_vision_transformers
description: "Fundus-image-level dme class labels and etdrs-guided annotations from Fundus imaging for diabetic macular edema; human clinical image provenance is inherent to the stated DME dataset."
tags: ["fundus", "cc-by", "mendeley", "segmentation", "resource-role-current-dataset", "dataset-family-mendeley-dme-classification-fundus-imaging-vision-transformers"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# DME Classification in Fundus Imaging with Vision Transformers and ETDRS-Guided Annotation

Fundus-image-level dme class labels and etdrs-guided annotations from Fundus imaging for diabetic macular edema; human clinical image provenance is inherent to the stated DME dataset.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mendeley_dme_classification_fundus_imaging_vision_transformers` |
| **Full name** | DME Classification in Fundus Imaging with Vision Transformers and ETDRS-Guided Annotation |
| **Publication date** | 2026-06-15 |
| **Date basis** | Initial dataset release |
| **Publication date precision** | day |
| **Publication date evidence** | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/sdcfn87pvs/1) |
| **Publication date source field** | citation_publication_date |
| **Publication date reviewed** | 2026-09-11 |
| **Date notes** | Official Mendeley Data version-1 page Published metadata; JSON-LD datePublished agrees. Version 1 is the initial public deposit. |
| **Primary category** | `fundus` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `mendeley_dme_classification_fundus_imaging_vision_transformers` |
| **Contained modalities** | fundus |
| **Tasks** | segmentation |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | Creative Commons Attribution 4.0 International |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `unknown` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Mendeley Data |
| **Availability** | `available` (checked 2026-08-02) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

No reproducible primary item count was exposed for the cataloged source version.

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Human provenance: Fundus imaging for diabetic macular edema; human clinical image provenance is inherent to the stated DME dataset. Source-review finding: Source description identifies ETDRS-based annotations with YOLO-defined macular landmarks supporting ViT/BEiT DME analysis.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mendeley_dme_classification_fundus_imaging_vision_transformers --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download mendeley_dme_classification_fundus_imaging_vision_transformers --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mendeley_dme_classification_fundus_imaging_vision_transformers')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/sdcfn87pvs/1)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/sdcfn87pvs)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mendeley_dme_classification_fundus_imaging_vision_transformers,
  title  = { DME Classification in Fundus Imaging with Vision Transformers and ETDRS-Guided Annotation },
  note   = { DME Classification in Fundus Imaging with Vision Transformers and ETDRS-Guided Annotation. Mendeley Data, V1. doi:10.17632/sdcfn87pvs.1 },
  url    = { https://data.mendeley.com/datasets/sdcfn87pvs/1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
DME Classification in Fundus Imaging with Vision Transformers and ETDRS-Guided Annotation. Mendeley Data, V1. doi:10.17632/sdcfn87pvs.1.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Creative Commons Attribution 4.0 International
- **Normalized category:** `cc-by`
- **Apparent scope:** `unknown`
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
