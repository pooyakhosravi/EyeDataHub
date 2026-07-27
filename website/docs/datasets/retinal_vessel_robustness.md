---
id: retinal_vessel_robustness
title: "Natural Robustness Benchmark for Retinal Vessel Segmentation"
sidebar_label: retinal_vessel_robustness
description: "Augmented DRIVE, STARE, and CHASE_DB1 vessel-segmentation images for out-of-distribution robustness evaluation."
tags: ["fundus", "mit", "zenodo", "segmentation"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Natural Robustness Benchmark for Retinal Vessel Segmentation

Augmented DRIVE, STARE, and CHASE_DB1 vessel-segmentation images for out-of-distribution robustness evaluation.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `retinal_vessel_robustness` |
| **Full name** | Natural Robustness Benchmark for Retinal Vessel Segmentation |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | segmentation |
| **Samples** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 8.15 GB |
| **Source-stated terms** | MIT |
| **Normalized terms** | `mit` |
| **Descriptive screening label** | Standard label without an explicit NC clause; verify that it applies to data |
| **Terms scope** | `unknown` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Zenodo |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Notes

> Derivative robustness benchmark from existing vessel datasets.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download retinal_vessel_robustness --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download retinal_vessel_robustness --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('retinal_vessel_robustness')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [zenodo.org/records](https://zenodo.org/records/12659652)

**Source-term evidence:** [zenodo.org/records](https://zenodo.org/records/12659652)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{retinal_vessel_robustness,
  title  = { Natural Robustness Benchmark for Retinal Vessel Segmentation },
  note   = { Evaluation benchmark for natural robustness evaluation of retinal vessel segmentation models. Zenodo, 2024. doi:10.5281/zenodo.12659652 },
  year   = { 2024 },
  url    = { https://zenodo.org/records/12659652 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Evaluation benchmark for natural robustness evaluation of retinal vessel segmentation models. Zenodo, 2024. doi:10.5281/zenodo.12659652
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** MIT
- **Normalized category:** `mit`
- **Apparent scope:** `unknown`
- **Descriptive screening label:** Standard label without an explicit NC clause; verify that it applies to data

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
