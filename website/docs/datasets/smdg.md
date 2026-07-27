---
id: smdg
title: "SMDG-19: Standardized Multi-channel Glaucoma Benchmark"
sidebar_label: smdg
description: "~12,000 fundus images aggregated from 19 public glaucoma datasets with standardized disc/cup/vessel channels and unified labels. CC0 — fully public domain."
tags: ["fundus", "cc0", "kaggle", "classification", "segmentation"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# SMDG-19: Standardized Multi-channel Glaucoma Benchmark

~12,000 fundus images aggregated from 19 public glaucoma datasets with standardized disc/cup/vessel channels and unified labels. CC0 — fully public domain.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `smdg` |
| **Full name** | SMDG-19: Standardized Multi-channel Glaucoma Benchmark |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | classification, segmentation |
| **Samples** | 12,449 |
| **Classes** | 3 (non_glaucoma, glaucoma, suspect) |
| **Splits** | train, val, test |
| **Size** | 5.0 GB |
| **Source-stated terms** | CC0 1.0 (Public Domain) |
| **Normalized terms** | `cc0` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Kaggle |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Notes

> Aggregator — overlaps with several EyeDataHub-indexed glaucoma datasets. Useful for unified multi-source training.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download smdg --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download smdg --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('smdg')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [kaggle.com/datasets](https://www.kaggle.com/datasets/deathtrooper/multichannel-glaucoma-benchmark-dataset)

**Source-term evidence:** [kaggle.com/datasets](https://www.kaggle.com/datasets/deathtrooper/multichannel-glaucoma-benchmark-dataset)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{smdg,
  title  = { SMDG-19: Standardized Multi-channel Glaucoma Benchmark },
  note   = { Kiefer, 'Standardized Multi-channel Dataset for Glaucoma (SMDG-19)', Kaggle 2022. Breakdown: 7,499 non-glaucoma + 4,817 glaucoma + 133 suspect },
  year   = { 2022 },
  url    = { https://www.kaggle.com/datasets/deathtrooper/multichannel-glaucoma-benchmark-dataset },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Kiefer, 'Standardized Multi-channel Dataset for Glaucoma (SMDG-19)', Kaggle 2022. Breakdown: 7,499 non-glaucoma + 4,817 glaucoma + 133 suspect.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC0 1.0 (Public Domain)
- **Normalized category:** `cc0`
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
