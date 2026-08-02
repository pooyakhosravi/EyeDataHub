---
id: mendeley_development_deep_learning_model_epiretinal_membrane
title: "Development of a deep learning model for epiretinal membrane detection in fundus photography"
sidebar_label: mendeley_development_deep_learning_model_epiretinal_membrane
description: "Fundus-image-level erm observations/labels from Retrospectively collected colour-fundus photographs from patients diagnosed with epiretinal membrane at B&VIIT Eye Center, Seoul."
tags: ["fundus", "cc-by", "manual", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Development of a deep learning model for epiretinal membrane detection in fundus photography

Fundus-image-level erm observations/labels from Retrospectively collected colour-fundus photographs from patients diagnosed with epiretinal membrane at B&VIIT Eye Center, Seoul.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mendeley_development_deep_learning_model_epiretinal_membrane` |
| **Full name** | Development of a deep learning model for epiretinal membrane detection in fundus photography |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | classification |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | Creative Commons Attribution 4.0 International |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `unknown` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-08-02) |
| **Acquisition support** | `guided_instructions_only` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

No reproducible primary item count was exposed for the cataloged source version.

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Human provenance: Retrospectively collected colour-fundus photographs from patients diagnosed with epiretinal membrane at B&VIIT Eye Center, Seoul. Source-review finding: Source description states retrospective CFP collection from patients with an ERM diagnosis.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mendeley_development_deep_learning_model_epiretinal_membrane --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download mendeley_development_deep_learning_model_epiretinal_membrane --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mendeley_development_deep_learning_model_epiretinal_membrane')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/jrgntpv8b8)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/jrgntpv8b8)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mendeley_development_deep_learning_model_epiretinal_membrane,
  title  = { Development of a deep learning model for epiretinal membrane detection in fundus photography },
  note   = { Development of a deep learning model for epiretinal membrane detection in fundus photography. Mendeley Data. doi:10.17632/jrgntpv8b8 },
  url    = { https://data.mendeley.com/datasets/jrgntpv8b8 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Development of a deep learning model for epiretinal membrane detection in fundus photography. Mendeley Data. doi:10.17632/jrgntpv8b8.
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
- [bidr](./bidr.md): BiDR: Diabetic Retinopathy Diagnosis Dataset (35,126 images, `unknown`)
