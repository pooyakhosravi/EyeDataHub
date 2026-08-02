---
id: aptos_arcade_onh_masks
title: "APTOS Vascular Arcade and Optic Nerve Head Masks"
sidebar_label: aptos_arcade_onh_masks
description: "Segmentation masks for the vascular arcade and optic nerve head derived from APTOS 2019 fundus images."
tags: ["fundus", "apache", "zenodo", "segmentation", "documented-relationship", "relationship-derived_from"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# APTOS Vascular Arcade and Optic Nerve Head Masks

Segmentation masks for the vascular arcade and optic nerve head derived from APTOS 2019 fundus images.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `aptos_arcade_onh_masks` |
| **Full name** | APTOS Vascular Arcade and Optic Nerve Head Masks |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | segmentation |
| **Primary reported quantity** | 500 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.1 GB |
| **Source-stated terms** | Apache-2.0 |
| **Normalized terms** | `apache` |
| **Descriptive screening label** | Standard label without an explicit NC clause; verify that it applies to data |
| **Terms scope** | `unknown` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Zenodo |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 500 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [zenodo.org/records](https://zenodo.org/records/20711325) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Derivative annotation layer for APTOS 2019; does not represent a new image cohort.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- This record is `derived from` [aptos2019](./aptos2019.md): The deposit supplies vascular-arcade and optic-nerve-head masks for APTOS 2019 images. ([evidence](https://zenodo.org/records/20711325))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download aptos_arcade_onh_masks --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download aptos_arcade_onh_masks --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('aptos_arcade_onh_masks')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [zenodo.org/records](https://zenodo.org/records/20711325)

**Source-term evidence:** [zenodo.org/records](https://zenodo.org/records/20711325)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{aptos_arcade_onh_masks,
  title  = { APTOS Vascular Arcade and Optic Nerve Head Masks },
  note   = { APTOS vascular arcade and optic nerve head masks. Zenodo, 2026. doi:10.5281/zenodo.20711325 },
  year   = { 2026 },
  url    = { https://zenodo.org/records/20711325 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
APTOS vascular arcade and optic nerve head masks. Zenodo, 2026. doi:10.5281/zenodo.20711325
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Apache-2.0
- **Normalized category:** `apache`
- **Apparent scope:** `unknown`
- **Descriptive screening label:** Standard label without an explicit NC clause; verify that it applies to data

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
