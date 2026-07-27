---
id: paired_retina
title: "Paired Retina Dataset: Cross-Device Fundus Pairs"
sidebar_label: paired_retina
description: "Paired tabletop and portable retinal images from the same patients, enabling cross-device domain-adaptation research."
tags: ["fundus", "unknown", "huggingface", "classification", "regression"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Paired Retina Dataset: Cross-Device Fundus Pairs

Paired tabletop and portable retinal images from the same patients, enabling cross-device domain-adaptation research.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `paired_retina` |
| **Full name** | Paired Retina Dataset: Cross-Device Fundus Pairs |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | classification, regression |
| **Samples** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | train, val, test |
| **Size** | 3.0 GB |
| **Source-stated terms** | Unknown — needs check (HF) |
| **Normalized terms** | `unknown` |
| **Descriptive screening label** | Unknown or unclear; do not assume permission |
| **Terms scope** | `unknown` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | HuggingFace Hub |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Notes

> Provenance and license require verification against the underlying publication before commercial use.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download paired_retina --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download paired_retina --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('paired_retina')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [huggingface.co/datasets](https://huggingface.co/datasets/smartretina2025/paired_retina)

**Source-term evidence:** [huggingface.co/datasets](https://huggingface.co/datasets/smartretina2025/paired_retina)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{paired_retina,
  title  = { Paired Retina Dataset: Cross-Device Fundus Pairs },
  note   = { Paired Retina Dataset: Cross-device fundus pairs. HuggingFace, 2025 },
  year   = { 2025 },
  url    = { https://huggingface.co/datasets/smartretina2025/paired_retina },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Paired Retina Dataset: Cross-device fundus pairs. HuggingFace, 2025.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Unknown — needs check (HF)
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
