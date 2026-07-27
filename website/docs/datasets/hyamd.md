---
id: hyamd
title: "HYAMD High-Resolution Fundus Image Dataset for AMD Diagnosis"
sidebar_label: hyamd
description: "High-resolution fundus images from Hillel Yaffe Medical Center for age-related macular degeneration diagnosis."
tags: ["fundus", "unknown", "physionet", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# HYAMD High-Resolution Fundus Image Dataset for AMD Diagnosis

High-resolution fundus images from Hillel Yaffe Medical Center for age-related macular degeneration diagnosis.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `hyamd` |
| **Full name** | HYAMD High-Resolution Fundus Image Dataset for AMD Diagnosis |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | classification |
| **Samples** | 1,560 |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | PhysioNet open access terms |
| **Normalized terms** | `unknown` |
| **Descriptive screening label** | Unknown or unclear; do not assume permission |
| **Terms scope** | `unknown` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | PhysioNet |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download hyamd --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download hyamd --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('hyamd')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.13026/f0dn-8q46](https://doi.org/10.13026/f0dn-8q46)

**Source-term evidence:** [https://doi.org/10.13026/f0dn-8q46](https://doi.org/10.13026/f0dn-8q46)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{hyamd,
  title  = { HYAMD High-Resolution Fundus Image Dataset for AMD Diagnosis },
  note   = { Meisel M, Cohen BA, Baskin M, Tiosano B, Behar J, Berkowitz E. HYAMD High-Resolution Fundus Image Dataset for AMD Diagnosis. PhysioNet, 2025. doi:10.13026/f0dn-8q46 },
  year   = { 2025 },
  url    = { https://doi.org/10.13026/f0dn-8q46 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Meisel M, Cohen BA, Baskin M, Tiosano B, Behar J, Berkowitz E. HYAMD High-Resolution Fundus Image Dataset for AMD Diagnosis. PhysioNet, 2025. doi:10.13026/f0dn-8q46
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** PhysioNet open access terms
- **Normalized category:** `unknown`
- **Apparent scope:** `unknown`
- **Descriptive screening label:** Unknown or unclear; do not assume permission

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
