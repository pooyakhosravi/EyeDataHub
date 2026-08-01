---
id: chaksu
title: "CHAKSU: Multi-Device Glaucoma Fundus Dataset"
sidebar_label: chaksu
description: "1,345 fundus images captured across multiple camera manufacturers with OD/OC segmentation + glaucoma classification labels."
tags: ["fundus", "cc-by", "figshare", "classification", "segmentation"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# CHAKSU: Multi-Device Glaucoma Fundus Dataset

1,345 fundus images captured across multiple camera manufacturers with OD/OC segmentation + glaucoma classification labels.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `chaksu` |
| **Full name** | CHAKSU: Multi-Device Glaucoma Fundus Dataset |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | classification, segmentation |
| **Samples** | 1,345 |
| **Classes** | 3 (background, optic_disc, optic_cup) |
| **Splits** | all |
| **Size** | 5.0 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Figshare |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `end_to_end_tested` |
| **Legacy sample-loader status** | Metadata and access only |


## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download chaksu --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download chaksu --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('chaksu')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.6084/m9.figshare.20123135](https://doi.org/10.6084/m9.figshare.20123135)

**Source-term evidence:** [https://doi.org/10.6084/m9.figshare.20123135](https://doi.org/10.6084/m9.figshare.20123135)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{chaksu,
  title  = { CHAKSU: Multi-Device Glaucoma Fundus Dataset },
  note   = { Kumar et al., 'CHAKSU: A glaucoma-specific fundus image database', Scientific Data 2023 },
  year   = { 2023 },
  url    = { https://doi.org/10.6084/m9.figshare.20123135 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Kumar et al., 'CHAKSU: A glaucoma-specific fundus image database', Scientific Data 2023.
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
