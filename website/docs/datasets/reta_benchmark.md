---
id: reta_benchmark
title: "RETA Benchmark for Retinal Vascular Tree Analysis"
sidebar_label: reta_benchmark
description: "Retinal vessel analysis benchmark with vessel masks, artery/vein masks and skeletons, bifurcation points, vascular trees, and abnormality annotations."
tags: ["fundus", "cc-by", "figshare", "segmentation", "vessel_analysis", "resource-role-annotation-layer", "dataset-family-reta-benchmark", "documented-relationship", "relationship-derived_from"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# RETA Benchmark for Retinal Vascular Tree Analysis

Retinal vessel analysis benchmark with vessel masks, artery/vein masks and skeletons, bifurcation points, vascular trees, and abnormality annotations.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `reta_benchmark` |
| **Full name** | RETA Benchmark for Retinal Vascular Tree Analysis |
| **Primary category** | `fundus` |
| **Resource role** | `annotation_layer` |
| **Dataset family** | `reta_benchmark` |
| **Contained modalities** | fundus |
| **Tasks** | segmentation, vessel_analysis |
| **Primary reported quantity** | 81 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.84 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Figshare |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `end_to_end_tested` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 81 | `images` | IDRiD-derived images with vascular-tree annotations | `official_source_description` | [https://doi.org/10.6084/m9.figshare.16960855](https://doi.org/10.6084/m9.figshare.16960855) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> RETA inherits the 81 images from the first subset of IDRiD and adds retinal vascular-tree annotations; keep it separate as an annotation/benchmark layer, not an independent imaging cohort.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- This record is `derived from` [idrid](./idrid.md): RETA reuses 81 images from the first IDRiD subset and adds vascular-tree annotations. ([evidence](https://doi.org/10.6084/m9.figshare.16960855))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download reta_benchmark --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download reta_benchmark --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('reta_benchmark')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.6084/m9.figshare.16960855](https://doi.org/10.6084/m9.figshare.16960855)

**Source-term evidence:** [https://doi.org/10.6084/m9.figshare.16960855](https://doi.org/10.6084/m9.figshare.16960855)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{reta_benchmark,
  title  = { RETA Benchmark for Retinal Vascular Tree Analysis },
  note   = { Lyu X, Cheng L, Zhang S. The RETA Benchmark for Retinal Vascular Tree Analysis. Scientific Data. 2022;9:397. doi:10.1038/s41597-022-01507-y },
  year   = { 2022 },
  url    = { https://doi.org/10.6084/m9.figshare.16960855 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Lyu X, Cheng L, Zhang S. The RETA Benchmark for Retinal Vascular Tree Analysis. Scientific Data. 2022;9:397. doi:10.1038/s41597-022-01507-y
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
