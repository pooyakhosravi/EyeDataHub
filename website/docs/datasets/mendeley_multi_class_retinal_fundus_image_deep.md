---
id: mendeley_multi_class_retinal_fundus_image_deep
title: "A Multi-Class Retinal Fundus Image Dataset for Deep Learning-Based Ocular Disease Diagnosis"
sidebar_label: mendeley_multi_class_retinal_fundus_image_deep
description: "Human/derived image or image-annotation observations. from Patients imaged at Rajbari Eye Clinic and Specialised Hospital, Bangladesh."
tags: ["fundus", "cc-by", "mendeley", "classification", "resource-role-current-dataset", "dataset-family-mendeley-multi-class-retinal-fundus-image-deep"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# A Multi-Class Retinal Fundus Image Dataset for Deep Learning-Based Ocular Disease Diagnosis

Human/derived image or image-annotation observations. from Patients imaged at Rajbari Eye Clinic and Specialised Hospital, Bangladesh.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mendeley_multi_class_retinal_fundus_image_deep` |
| **Full name** | A Multi-Class Retinal Fundus Image Dataset for Deep Learning-Based Ocular Disease Diagnosis |
| **Publication date** | 2026-07-14 |
| **Date basis** | Initial dataset release |
| **Publication date precision** | day |
| **Publication date evidence** | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/z227d626vm/1) |
| **Publication date source field** | citation_publication_date (version 1) |
| **Publication date reviewed** | 2026-09-11 |
| **Date notes** | - |
| **Primary category** | `fundus` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `mendeley_multi_class_retinal_fundus_image_deep` |
| **Contained modalities** | fundus |
| **Tasks** | classification |
| **Primary reported quantity** | 1,222 images |
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

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 1,222 | `images` | Source-stated quantity Preserved from the source-confirmation record. | `official_source_description` | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/z227d626vm) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Human provenance: Patients imaged at Rajbari Eye Clinic and Specialised Hospital, Bangladesh. Source-review finding: High-resolution fundus images across 11 labelled disease classes; source separately notes augmented derivatives.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mendeley_multi_class_retinal_fundus_image_deep --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download mendeley_multi_class_retinal_fundus_image_deep --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mendeley_multi_class_retinal_fundus_image_deep')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/z227d626vm/1)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/z227d626vm)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mendeley_multi_class_retinal_fundus_image_deep,
  title  = { A Multi-Class Retinal Fundus Image Dataset for Deep Learning-Based Ocular Disease Diagnosis },
  note   = { A Multi-Class Retinal Fundus Image Dataset for Deep Learning-Based Ocular Disease Diagnosis. Mendeley Data, V1. doi:10.17632/z227d626vm.1 },
  url    = { https://data.mendeley.com/datasets/z227d626vm/1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
A Multi-Class Retinal Fundus Image Dataset for Deep Learning-Based Ocular Disease Diagnosis. Mendeley Data, V1. doi:10.17632/z227d626vm.1.
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
