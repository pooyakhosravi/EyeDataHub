---
id: riga_plus
title: "RIGA+ Domain Adaptation Dataset"
sidebar_label: riga_plus
description: "RIGA/MESSIDOR-derived benchmark for optic disc and cup segmentation domain adaptation."
tags: ["fundus", "cc-by", "zenodo", "segmentation", "resource-role-derivative-dataset", "dataset-family-riga-plus", "documented-relationship", "relationship-derived_from"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# RIGA+ Domain Adaptation Dataset

RIGA/MESSIDOR-derived benchmark for optic disc and cup segmentation domain adaptation.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `riga_plus` |
| **Full name** | RIGA+ Domain Adaptation Dataset |
| **First published** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Primary category** | `fundus` |
| **Resource role** | `derivative_dataset` |
| **Dataset family** | `riga_plus` |
| **Contained modalities** | fundus |
| **Tasks** | segmentation |
| **Primary reported quantity** | 1,461 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Zenodo |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 1,461 | `images` | TIF images in the RIGA directory of the current deposit The source reports removal of six RIGA duplicates and cross-dataset duplicates with MESSIDOR. | `current_deposit_file_listing` | [zenodo.org/records](https://zenodo.org/records/6325549) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Derivative benchmark based on existing RIGA/MESSIDOR resources.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- This record is `derived from` [riga](./riga.md): RIGA+ is built from RIGA components plus the original MESSIDOR resource after duplicate removal. ([evidence](https://zenodo.org/records/6325549))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download riga_plus --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download riga_plus --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('riga_plus')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [zenodo.org/records](https://zenodo.org/records/6325549)

**Source-term evidence:** [zenodo.org/records](https://zenodo.org/records/6325549)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{riga_plus,
  title  = { RIGA+ Domain Adaptation Dataset },
  note   = { RIGA+ for domain adaptation. Zenodo, 2022. doi:10.5281/zenodo.6325549 },
  year   = { 2022 },
  url    = { https://zenodo.org/records/6325549 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
RIGA+ for domain adaptation. Zenodo, 2022. doi:10.5281/zenodo.6325549
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
