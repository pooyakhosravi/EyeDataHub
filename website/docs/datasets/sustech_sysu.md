---
id: sustech_sysu
title: "SUSTech-SYSU Diabetic Retinopathy + Exudate Dataset"
sidebar_label: sustech_sysu
description: "1,219 color fundus images with DR severity grading + pixel-level exudate segmentation masks. Multi-center (SUSTech + Sun Yat-sen University)."
tags: ["fundus", "cc-by", "figshare", "grading", "segmentation", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# SUSTech-SYSU Diabetic Retinopathy + Exudate Dataset

1,219 color fundus images with DR severity grading + pixel-level exudate segmentation masks. Multi-center (SUSTech + Sun Yat-sen University).

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `sustech_sysu` |
| **Full name** | SUSTech-SYSU Diabetic Retinopathy + Exudate Dataset |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | grading, segmentation, classification |
| **Samples** | 1,219 |
| **Classes** | 5 (Not reported) |
| **Splits** | all |
| **Size** | 3.0 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Figshare |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download sustech_sysu --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download sustech_sysu --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('sustech_sysu')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.6084/m9.figshare.12570770](https://doi.org/10.6084/m9.figshare.12570770)

**Source-term evidence:** [https://doi.org/10.6084/m9.figshare.12570770](https://doi.org/10.6084/m9.figshare.12570770)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{sustech_sysu,
  title  = { SUSTech-SYSU Diabetic Retinopathy + Exudate Dataset },
  note   = { Lin et al., 'The SUSTech-SYSU dataset for automated exudate detection and diabetic retinopathy grading', Scientific Data 2020 },
  year   = { 2020 },
  url    = { https://doi.org/10.6084/m9.figshare.12570770 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Lin et al., 'The SUSTech-SYSU dataset for automated exudate detection and diabetic retinopathy grading', Scientific Data 2020.
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
