---
id: fairvlmed
title: "FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset"
sidebar_label: fairvlmed
description: "Ophthalmic clinical text + NPZ records covering glaucoma, cataract, and neuro-ophthalmology with paired age, sex, race/ethnicity, and language attributes. Derived from the same Harvard clinical popula"
tags: ["multimodal", "fundus", "visual_field", "text", "tabular", "unknown", "huggingface", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset

Ophthalmic clinical text + NPZ records covering glaucoma, cataract, and neuro-ophthalmology with paired age, sex, race/ethnicity, and language attributes. Derived from the same Harvard clinical population as Harvard-FairVision.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `fairvlmed` |
| **Full name** | FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset |
| **Primary category** | `multimodal` |
| **Contained modalities** | fundus, visual_field, text, tabular |
| **Tasks** | classification |
| **Samples** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | train, val, test |
| **Size** | 10.0 GB |
| **Source-stated terms** | See Harvard AI Robotics terms |
| **Normalized terms** | `unknown` |
| **Descriptive screening label** | Unknown or unclear; do not assume permission |
| **Terms scope** | `unknown` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | HuggingFace Hub |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Notes

> OVERLAP: Derived from the same Harvard clinical cohort as `harvard_fairvision` (already indexed). Kept for VLM/text researchers who specifically need the text+NPZ view.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download fairvlmed --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download fairvlmed --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('fairvlmed')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [huggingface.co/datasets](https://huggingface.co/datasets/harvardairobotics/FairVLMed)

**Source-term evidence:** [huggingface.co/datasets](https://huggingface.co/datasets/harvardairobotics/FairVLMed)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{fairvlmed,
  title  = { FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset },
  note   = { Harvard AI Robotics, FairVLMed: Fair vision-language medical ophthalmic dataset. HuggingFace, 2024 },
  year   = { 2024 },
  url    = { https://huggingface.co/datasets/harvardairobotics/FairVLMed },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Harvard AI Robotics, FairVLMed: Fair vision-language medical ophthalmic dataset. HuggingFace, 2024.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** See Harvard AI Robotics terms
- **Normalized category:** `unknown`
- **Apparent scope:** `unknown`
- **Descriptive screening label:** Unknown or unclear; do not assume permission

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Related datasets with shared modalities

- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 records, `unknown`)
- [grape](./grape.md): GRAPE: Glaucoma Real-world Appraisal Progression Ensemble (1,115 records, `cc0`)
- [ocular_chat_vqa](./ocular_chat_vqa.md): OcularChat-VQA: AREDS-Derived Patient-Physician Dialogue Dataset (844,000 records, `cc-by-nc-sa`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 records, `unknown`)
- [angioreport](./angioreport.md): AngioReport Fundus Angiography Report Dataset (55,361 records, `unknown`)
- [ffa_ir](./ffa_ir.md): FFA-IR Medical Report Dataset (47,247 records, `unknown`)
- [x_pcr](./x_pcr.md): X-PCR Ophthalmology Progressive Clinical Reasoning Benchmark (18,700 records, `unknown`)
- [deepeyenet](./deepeyenet.md): DeepEyeNet (DEN): Fundus Report Generation Dataset (15,709 records, `research-only`)
