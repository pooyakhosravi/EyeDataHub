---
id: coph100
title: "COph100: Comprehensive Infant Fundus Image Registration Dataset (RIDIRP)"
sidebar_label: coph100
description: "100 infant eyes with 491 image pairs annotated with ground-truth control points and vessel masks. Enables pediatric / ROP-relevant fundus registration research."
tags: ["fundus", "cc-by", "figshare", "regression", "segmentation"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# COph100: Comprehensive Infant Fundus Image Registration Dataset (RIDIRP)

100 infant eyes with 491 image pairs annotated with ground-truth control points and vessel masks. Enables pediatric / ROP-relevant fundus registration research.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `coph100` |
| **Full name** | COph100: Comprehensive Infant Fundus Image Registration Dataset (RIDIRP) |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | regression, segmentation |
| **Samples** | 982 |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 1.0 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Figshare |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `end_to_end_tested` |
| **Legacy sample-loader status** | Metadata and access only |


## Notes

> Adds infant fundus registration; complements ROP classification datasets.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download coph100 --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download coph100 --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('coph100')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.6084/m9.figshare.27061084.v1](https://doi.org/10.6084/m9.figshare.27061084.v1)

**Source-term evidence:** [https://doi.org/10.6084/m9.figshare.27061084.v1](https://doi.org/10.6084/m9.figshare.27061084.v1)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{coph100,
  title  = { COph100: Comprehensive Infant Fundus Image Registration Dataset (RIDIRP) },
  note   = { Hu Y, et al., 'COph100: A comprehensive fundus image registration dataset from infants constituting the RIDIRP database', Scientific Data 2025;12:99 },
  year   = { 2025 },
  url    = { https://doi.org/10.6084/m9.figshare.27061084.v1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Hu Y, et al., 'COph100: A comprehensive fundus image registration dataset from infants constituting the RIDIRP database', Scientific Data 2025;12:99.
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
