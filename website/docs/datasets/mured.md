---
id: mured
title: "MuReD: Multi-label Retinal Diseases Dataset"
sidebar_label: mured
description: "2,208 color fundus images with 20-class multi-label disease annotations."
tags: ["fundus", "cc-by", "mendeley", "multilabel", "classification", "resource-role-derivative-dataset", "dataset-family-mured", "documented-relationship", "relationship-derived_from"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# MuReD: Multi-label Retinal Diseases Dataset

2,208 color fundus images with 20-class multi-label disease annotations.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mured` |
| **Full name** | MuReD: Multi-label Retinal Diseases Dataset |
| **Publication date** | 2022-07-25 |
| **Date basis** | Initial dataset release |
| **Publication date precision** | day |
| **Publication date evidence** | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/pc4mb3h8hz/1) |
| **Publication date source field** | citation_publication_date (version 1) |
| **Publication date reviewed** | 2026-09-11 |
| **Date notes** | - |
| **Primary category** | `fundus` |
| **Resource role** | `derivative_dataset` |
| **Dataset family** | `mured` |
| **Contained modalities** | fundus |
| **Tasks** | multilabel, classification |
| **Primary reported quantity** | 2,208 images |
| **Classes** | 20 (Not reported) |
| **Splits** | train, test |
| **Size** | 2.0 GB |
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
| Primary | 2,208 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/pc4mb3h8hz/1) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> The official source states that images from STARE, RFMiD, and ARIA were post-processed for this release. ARIA is not a separate EyeDataHub record.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- [x_pcr](./x_pcr.md) is `derived from` this record: Source labels in the version-pinned public X-PCR deposit identify this catalog record as upstream material. ([evidence](https://huggingface.co/datasets/Fantasy666/X-PCR/tree/06a318fd852230326386e3c6514d8a11b7a6b4af))
- This record is `derived from` [rfmid](./rfmid.md): The MuReD description identifies STARE, RFMiD, and ARIA as image sources and applies post-processing. ([evidence](https://doi.org/10.17632/pc4mb3h8hz.1))
- This record is `derived from` [stare](./stare.md): The MuReD description identifies STARE, RFMiD, and ARIA as image sources and applies post-processing. ([evidence](https://doi.org/10.17632/pc4mb3h8hz.1))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mured --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download mured --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mured')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/pc4mb3h8hz/1)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/pc4mb3h8hz/1)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mured,
  title  = { MuReD: Multi-label Retinal Diseases Dataset },
  note   = { Rodriguez MA, AlMarzouqi H, Liatsis P, 'Multi-label Retinal Disease Classification using Transformers', IEEE Journal of Biomedical and Health Informatics 27(6):2739-2750, 2022. arXiv:2207.02335 },
  year   = { 2022 },
  url    = { https://data.mendeley.com/datasets/pc4mb3h8hz/1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Rodriguez MA, AlMarzouqi H, Liatsis P, 'Multi-label Retinal Disease Classification using Transformers', IEEE Journal of Biomedical and Health Informatics 27(6):2739-2750, 2022. arXiv:2207.02335
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
