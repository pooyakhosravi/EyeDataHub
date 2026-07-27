---
id: retinal_dr_longitudinal
title: "Retinal DR Longitudinal Fundus Pairs"
sidebar_label: retinal_dr_longitudinal
description: "Baseline and two-year follow-up color fundus image pairs from Tianjin Medical University for diabetic-retinopathy progression research."
tags: ["fundus", "unknown", "huggingface", "progression", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Retinal DR Longitudinal Fundus Pairs

Baseline and two-year follow-up color fundus image pairs from Tianjin Medical University for diabetic-retinopathy progression research.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `retinal_dr_longitudinal` |
| **Full name** | Retinal DR Longitudinal Fundus Pairs |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | progression, classification |
| **Samples** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 4.0 GB |
| **Source-stated terms** | Unknown — needs check (HF; ethics statement in card) |
| **Normalized terms** | `unknown` |
| **Descriptive screening label** | Unknown or unclear; do not assume permission |
| **Terms scope** | `unknown` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | HuggingFace Hub |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Notes

> Verify source publication before commercial use.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download retinal_dr_longitudinal --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download retinal_dr_longitudinal --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('retinal_dr_longitudinal')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [huggingface.co/datasets](https://huggingface.co/datasets/usama10/retinal-dr-longitudinal)

**Source-term evidence:** [huggingface.co/datasets](https://huggingface.co/datasets/usama10/retinal-dr-longitudinal)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{retinal_dr_longitudinal,
  title  = { Retinal DR Longitudinal Fundus Pairs },
  note   = { Retinal DR longitudinal fundus pairs, Tianjin Medical University. HuggingFace, 2025 },
  year   = { 2025 },
  url    = { https://huggingface.co/datasets/usama10/retinal-dr-longitudinal },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Retinal DR longitudinal fundus pairs, Tianjin Medical University. HuggingFace, 2025.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Unknown — needs check (HF; ethics statement in card)
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
