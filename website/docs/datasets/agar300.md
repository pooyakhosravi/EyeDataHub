---
id: agar300
title: "AGAR300 Microaneurysm Fundus Image Dataset"
sidebar_label: agar300
description: "The first public AGAR300 release contains 28 color fundus images with microaneurysms, captured at a 45 degree field of view and 2448 by 3264 pixel resolution."
tags: ["fundus", "cc-by", "manual", "lesion_detection"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# AGAR300 Microaneurysm Fundus Image Dataset

The first public AGAR300 release contains 28 color fundus images with microaneurysms, captured at a 45 degree field of view and 2448 by 3264 pixel resolution.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `agar300` |
| **Full name** | AGAR300 Microaneurysm Fundus Image Dataset |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | lesion_detection |
| **Samples** | 28 |
| **Classes** | 1 (microaneurysm) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `guided_instructions_only` |
| **Legacy sample-loader status** | Metadata and access only |


## Notes

> The source paper describes a larger 300 image clinical collection. The DOI record states that the public first release contains 28 images. All released images contain microaneurysms, and the release does not include spatial annotations. An IEEE DataPort account may be required to download it.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download agar300 --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download agar300 --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('agar300')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [ieee-dataport.org/open-access](https://ieee-dataport.org/open-access/diabetic-retinopathy-fundus-image-datasetagar300)

**Source-term evidence:** [ieee-dataport.org/open-access](https://ieee-dataport.org/open-access/diabetic-retinopathy-fundus-image-datasetagar300)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{agar300,
  title  = { AGAR300 Microaneurysm Fundus Image Dataset },
  note   = { Derwin J, Shan P. Diabetic Retinopathy - Fundus Image Dataset (AGAR300). IEEE DataPort. 2020. doi:10.21227/fsnq-tn19 },
  year   = { 2020 },
  url    = { https://ieee-dataport.org/open-access/diabetic-retinopathy-fundus-image-datasetagar300 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Derwin J, Shan P. Diabetic Retinopathy - Fundus Image Dataset (AGAR300). IEEE DataPort. 2020. doi:10.21227/fsnq-tn19
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
