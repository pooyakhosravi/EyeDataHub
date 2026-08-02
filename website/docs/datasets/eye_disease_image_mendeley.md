---
id: eye_disease_image_mendeley
title: "Eye Disease Image Dataset"
sidebar_label: eye_disease_image_mendeley
description: "Original and augmented eye-disease image dataset covering retinitis pigmentosa, retinal detachment, pterygium, myopia, macular scar, glaucoma, disc edema, diabetic retinopathy, central serous choriore"
tags: ["fundus", "cc-by", "mendeley", "classification", "documented-relationship", "relationship-derived_from"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Eye Disease Image Dataset

Original and augmented eye-disease image dataset covering retinitis pigmentosa, retinal detachment, pterygium, myopia, macular scar, glaucoma, disc edema, diabetic retinopathy, central serous chorioretinopathy, and healthy classes.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `eye_disease_image_mendeley` |
| **Full name** | Eye Disease Image Dataset |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | classification |
| **Primary reported quantity** | 5,335 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 1.5 GB |
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
| Primary | 5,335 | `images` | Original and augmented image collection | `official_source_description` | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/s9bfhswzjb/1) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Includes augmented images; use original subset for clinical validation.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- [x_pcr](./x_pcr.md) is `derived from` this record: Source labels in the version-pinned public X-PCR deposit identify this catalog record as upstream material. ([evidence](https://huggingface.co/datasets/Fantasy666/X-PCR/tree/06a318fd852230326386e3c6514d8a11b7a6b4af))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download eye_disease_image_mendeley --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download eye_disease_image_mendeley --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('eye_disease_image_mendeley')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/s9bfhswzjb/1)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/s9bfhswzjb/1)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{eye_disease_image_mendeley,
  title  = { Eye Disease Image Dataset },
  note   = { Eye Disease Image Dataset. Mendeley Data, V1, 2024. doi:10.17632/s9bfhswzjb.1 },
  year   = { 2024 },
  url    = { https://data.mendeley.com/datasets/s9bfhswzjb/1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Eye Disease Image Dataset. Mendeley Data, V1, 2024. doi:10.17632/s9bfhswzjb.1
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
- [bidr](./bidr.md): BiDR: Diabetic Retinopathy Diagnosis Dataset (35,126 images, `unknown`)
