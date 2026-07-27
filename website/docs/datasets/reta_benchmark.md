---
id: reta_benchmark
title: "RETA Benchmark for Retinal Vascular Tree Analysis"
sidebar_label: reta_benchmark
description: "Retinal vessel analysis benchmark with vessel masks, artery/vein masks and skeletons, bifurcation points, vascular trees, and abnormality annotations."
tags: ["fundus", "cc-by", "figshare", "segmentation", "vessel_analysis"]
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
| **Contained modalities** | fundus |
| **Tasks** | segmentation, vessel_analysis |
| **Samples** | 81 |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.84 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Figshare |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Notes

> RETA inherits the 81 images from the first subset of IDRiD and adds retinal vascular-tree annotations; keep it separate as an annotation/benchmark layer, not an independent imaging cohort.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download reta_benchmark --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download reta_benchmark --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('reta_benchmark')
print(preflight_dataset(ds, './data'))  # no transfer
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

## Related datasets with shared modalities

- [airogs](./airogs.md): AIROGS: AI for Robust Glaucoma Screening (113,893 records, `cc-by-nc-nd`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 records, `unknown`)
- [justraigs](./justraigs.md): JustRAIGS: Just Referral AI Glaucoma Screening Dataset (101,442 records, `cc-by-nc-nd`)
- [eyepacs](./eyepacs.md): EyePACS — Diabetic Retinopathy Detection (Kaggle 2015) (88,702 records, `research-only`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (58,036 records, `mit`)
- [angioreport](./angioreport.md): AngioReport Fundus Angiography Report Dataset (55,361 records, `unknown`)
- [ffa_ir](./ffa_ir.md): FFA-IR Medical Report Dataset (47,247 records, `unknown`)
- [bidr](./bidr.md): BiDR: Diabetic Retinopathy Diagnosis Dataset (35,126 records, `unknown`)
