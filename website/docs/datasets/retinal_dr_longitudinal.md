---
id: retinal_dr_longitudinal
title: "Retinal DR Longitudinal Fundus Pairs"
sidebar_label: retinal_dr_longitudinal
description: "Baseline and two-year follow-up color fundus image pairs from Tianjin Medical University for diabetic-retinopathy progression research."
tags: ["fundus", "unknown", "huggingface", "progression", "classification", "resource-role-current-dataset", "dataset-family-retinal-dr-longitudinal"]
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
| **Resource role** | `current_dataset` |
| **Dataset family** | `retinal_dr_longitudinal` |
| **Contained modalities** | fundus |
| **Tasks** | progression, classification |
| **Primary reported quantity** | 1,115 image pairs |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 4.0 GB |
| **Source-stated terms** | Unknown — needs check (HF; ethics statement in card) |
| **Normalized terms** | `unknown` |
| **Descriptive screening label** | Unknown or unclear; do not assume permission |
| **Terms scope** | `unknown` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | HuggingFace Hub |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 1,115 | `image_pairs` | Rows in corrected_manifest.csv | `current_deposit_table` | [huggingface.co/datasets](https://huggingface.co/datasets/usama10/retinal-dr-longitudinal/tree/d6e13e91dae69f3080259afd478db92412c7f32d) |
| Additional | 2,428 | `images` | JPG files in the current deposit The deposit contains 1,250 baseline and 1,178 follow-up images; 2,230 participate in the corrected 1,115-pair manifest. | `current_deposit_file_listing` | [huggingface.co/datasets](https://huggingface.co/datasets/usama10/retinal-dr-longitudinal/tree/d6e13e91dae69f3080259afd478db92412c7f32d) |
| Additional | 572 | `participants` | Unique patient IDs in corrected_manifest.csv | `current_deposit_table` | [huggingface.co/datasets](https://huggingface.co/datasets/usama10/retinal-dr-longitudinal/tree/d6e13e91dae69f3080259afd478db92412c7f32d) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Verify source publication before commercial use.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download retinal_dr_longitudinal --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download retinal_dr_longitudinal --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('retinal_dr_longitudinal')
print(preflight_dataset(ds, './data'))  # no download
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

## Similar resources by shared modality

- [airogs](./airogs.md): AIROGS: AI for Robust Glaucoma Screening (113,893 images, `cc-by-nc-nd`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (103,959 images, `mit`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [justraigs](./justraigs.md): JustRAIGS: Just Referral AI Glaucoma Screening Dataset (101,442 images, `cc-by-nc-nd`)
- [eyepacs](./eyepacs.md): EyePACS — Diabetic Retinopathy Detection (Kaggle 2015) (88,702 images, `research-only`)
- [angioreport](./angioreport.md): AngioReport Fundus Angiography Report Dataset (55,361 images, `unknown`)
- [ffa_ir](./ffa_ir.md): FFA-IR Medical Report Dataset (47,247 images, `unknown`)
- [mfiddr](./mfiddr.md): MFIDDR: Multi-Field Imaging Dataset for Diabetic Retinopathy (34,452 images, `mit`)
