---
id: ut_fsocta
title: "UTHealth Fundus and Synthetic OCTA Dataset"
sidebar_label: ut_fsocta
description: "Fundus and synthetic OCTA vessel-segmentation resource for domain-transfer research."
tags: ["multimodal", "fundus", "octa", "unknown", "zenodo", "segmentation"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# UTHealth Fundus and Synthetic OCTA Dataset

Fundus and synthetic OCTA vessel-segmentation resource for domain-transfer research.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `ut_fsocta` |
| **Full name** | UTHealth Fundus and Synthetic OCTA Dataset |
| **Primary category** | `multimodal` |
| **Contained modalities** | fundus, octa |
| **Tasks** | segmentation |
| **Samples** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | Unknown |
| **Normalized terms** | `unknown` |
| **Descriptive screening label** | Unknown or unclear; do not assume permission |
| **Terms scope** | `unknown` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Zenodo |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download ut_fsocta --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download ut_fsocta --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('ut_fsocta')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [zenodo.org/records](https://zenodo.org/records/6476639)

**Source-term evidence:** [zenodo.org/records](https://zenodo.org/records/6476639)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{ut_fsocta,
  title  = { UTHealth Fundus and Synthetic OCTA Dataset },
  note   = { UTHealth fundus and synthetic OCTA dataset. Zenodo, 2022. doi:10.5281/zenodo.6476639 },
  year   = { 2022 },
  url    = { https://zenodo.org/records/6476639 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
UTHealth fundus and synthetic OCTA dataset. Zenodo, 2022. doi:10.5281/zenodo.6476639
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Unknown
- **Normalized category:** `unknown`
- **Apparent scope:** `unknown`
- **Descriptive screening label:** Unknown or unclear; do not assume permission

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Related datasets with shared modalities

- [airogs](./airogs.md): AIROGS: AI for Robust Glaucoma Screening (113,893 records, `cc-by-nc-nd`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 records, `unknown`)
- [justraigs](./justraigs.md): JustRAIGS: Just Referral AI Glaucoma Screening Dataset (101,442 records, `cc-by-nc-nd`)
- [eyepacs](./eyepacs.md): EyePACS — Diabetic Retinopathy Detection (Kaggle 2015) (88,702 records, `research-only`)
- [octa_macula_coronal](./octa_macula_coronal.md): OCTA Macula Coronal Views (82,560 records, `cc-by`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (58,036 records, `mit`)
- [angioreport](./angioreport.md): AngioReport Fundus Angiography Report Dataset (55,361 records, `unknown`)
- [ffa_ir](./ffa_ir.md): FFA-IR Medical Report Dataset (47,247 records, `unknown`)
