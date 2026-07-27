---
id: rop_synthetic_mendeley
title: "Synthetic Medical Images for ROP Diagnosis"
sidebar_label: rop_synthetic_mendeley
description: "Retinopathy-of-prematurity fundus-image dataset and synthetic-image resources for privacy-preserving AI training."
tags: ["fundus", "cc-by", "mendeley", "classification", "segmentation"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Synthetic Medical Images for ROP Diagnosis

Retinopathy-of-prematurity fundus-image dataset and synthetic-image resources for privacy-preserving AI training.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `rop_synthetic_mendeley` |
| **Full name** | Synthetic Medical Images for ROP Diagnosis |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | classification, segmentation |
| **Samples** | 5,842 |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 2.0 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Mendeley Data |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Notes

> Includes synthetic images; keep separate from primary clinical cohorts in validation.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download rop_synthetic_mendeley --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download rop_synthetic_mendeley --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('rop_synthetic_mendeley')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/fscyyhg6vt/1)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/fscyyhg6vt/1)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{rop_synthetic_mendeley,
  title  = { Synthetic Medical Images for ROP Diagnosis },
  note   = { Coyner AS et al. Synthetic Medical Images for Robust, Privacy-Preserving Training of AI: Application to ROP Diagnosis. Mendeley Data, V1, 2022. doi:10.17632/fscyyhg6vt.1 },
  year   = { 2022 },
  url    = { https://data.mendeley.com/datasets/fscyyhg6vt/1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Coyner AS et al. Synthetic Medical Images for Robust, Privacy-Preserving Training of AI: Application to ROP Diagnosis. Mendeley Data, V1, 2022. doi:10.17632/fscyyhg6vt.1
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
