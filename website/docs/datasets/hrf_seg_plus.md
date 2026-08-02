---
id: hrf_seg_plus
title: "HRF-Seg+: Multi-Structure Fundus Annotations"
sidebar_label: hrf_seg_plus
description: "Extended HRF annotations for optic disc, cup, retinal vessels, and alpha/beta peripapillary zones."
tags: ["fundus", "cc-by", "zenodo", "segmentation", "documented-relationship", "relationship-derived_from"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# HRF-Seg+: Multi-Structure Fundus Annotations

Extended HRF annotations for optic disc, cup, retinal vessels, and alpha/beta peripapillary zones.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `hrf_seg_plus` |
| **Full name** | HRF-Seg+: Multi-Structure Fundus Annotations |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | segmentation |
| **Primary reported quantity** | 45 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.01 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Zenodo |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 45 | `images` | HRF images receiving extended annotations | `official_source_description` | [zenodo.org/records](https://zenodo.org/records/16744782) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Derivative annotation layer for existing HRF images.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- This record is `derived from` [hrf](./hrf.md): HRF-Seg+ adds multi-structure annotations to the 45 HRF images. ([evidence](https://zenodo.org/records/16744782))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download hrf_seg_plus --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download hrf_seg_plus --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('hrf_seg_plus')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [zenodo.org/records](https://zenodo.org/records/16744782)

**Source-term evidence:** [zenodo.org/records](https://zenodo.org/records/16744782)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{hrf_seg_plus,
  title  = { HRF-Seg+: Multi-Structure Fundus Annotations },
  note   = { HRF-Seg+: A multi-structure annotated fundus image dataset. Zenodo, 2026. doi:10.5281/zenodo.16744782 },
  year   = { 2026 },
  url    = { https://zenodo.org/records/16744782 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
HRF-Seg+: A multi-structure annotated fundus image dataset. Zenodo, 2026. doi:10.5281/zenodo.16744782
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
