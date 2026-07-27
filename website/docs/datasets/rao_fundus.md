---
id: rao_fundus
title: "RAO Retinal Artery Occlusion Fundus Photography Dataset"
sidebar_label: rao_fundus
description: "Fundus-photography dataset for retinal artery occlusion diagnosis, based on web-derived public data and public fundus datasets."
tags: ["fundus", "cc-by", "mendeley", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# RAO Retinal Artery Occlusion Fundus Photography Dataset

Fundus-photography dataset for retinal artery occlusion diagnosis, based on web-derived public data and public fundus datasets.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `rao_fundus` |
| **Full name** | RAO Retinal Artery Occlusion Fundus Photography Dataset |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | classification |
| **Samples** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
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

> Source reports use of web-based public data plus RFMiD and JSIEC. Retained as a distinct RAO task resource, but not an independent primary cohort.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download rao_fundus --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download rao_fundus --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('rao_fundus')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/5428684j44/1)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/5428684j44/1)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{rao_fundus,
  title  = { RAO Retinal Artery Occlusion Fundus Photography Dataset },
  note   = { Yoo T. RAO (retinal artery occlusion) fundus photography dataset. Mendeley Data, V1, 2024. doi:10.17632/5428684j44.1 },
  year   = { 2024 },
  url    = { https://data.mendeley.com/datasets/5428684j44/1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Yoo T. RAO (retinal artery occlusion) fundus photography dataset. Mendeley Data, V1, 2024. doi:10.17632/5428684j44.1
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
