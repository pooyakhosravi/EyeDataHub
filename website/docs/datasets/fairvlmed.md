---
id: fairvlmed
title: "FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset"
sidebar_label: fairvlmed
description: "10,000 scanning-laser ophthalmoscopy fundus images paired with de-identified clinical notes, visual-field measurements, glaucoma labels, and demographic attributes."
tags: ["multimodal", "fundus", "visual_field", "text", "tabular", "cc-by-nc-nd", "huggingface", "classification", "report_generation", "fairness_analysis"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset

10,000 scanning-laser ophthalmoscopy fundus images paired with de-identified clinical notes, visual-field measurements, glaucoma labels, and demographic attributes.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `fairvlmed` |
| **Full name** | FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset |
| **Primary category** | `multimodal` |
| **Contained modalities** | fundus, visual_field, text, tabular |
| **Tasks** | classification, report_generation, fairness_analysis |
| **Primary reported quantity** | 10,000 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | train, val, test |
| **Size** | 10.0 GB |
| **Source-stated terms** | CC BY-NC-ND 4.0 |
| **Normalized terms** | `cc-by-nc-nd` |
| **Descriptive screening label** | Explicit noncommercial clause recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | HuggingFace Hub |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 10,000 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [huggingface.co/datasets](https://huggingface.co/datasets/harvardairobotics/FairVLMed) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> The official dataset card reports 10,000 patients and 10,000 samples (7,000 train, 1,000 validation, 2,000 test). No source statement supporting cohort identity with the separate Harvard-FairVision record was found, so no catalog relationship is asserted.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download fairvlmed --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download fairvlmed --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('fairvlmed')
print(preflight_dataset(ds, './data'))  # no download
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

- **Raw source string:** CC BY-NC-ND 4.0
- **Normalized category:** `cc-by-nc-nd`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Explicit noncommercial clause recorded; check source

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [grape](./grape.md): GRAPE: Glaucoma Real-world Appraisal Progression Ensemble (1,115 examinations, `cc0`)
- [ocular_chat_vqa](./ocular_chat_vqa.md): OcularChat-VQA: AREDS-Derived Patient-Physician Dialogue Dataset (844,000 records, `cc-by-nc-sa`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [angioreport](./angioreport.md): AngioReport Fundus Angiography Report Dataset (55,361 images, `unknown`)
- [ffa_ir](./ffa_ir.md): FFA-IR Medical Report Dataset (47,247 images, `unknown`)
- [x_pcr](./x_pcr.md): X-PCR Ophthalmology Progressive Clinical Reasoning Benchmark (18,735 rows, `unknown`)
- [deepeyenet](./deepeyenet.md): DeepEyeNet (DEN): Fundus Report Generation Dataset (15,709 images, `research-only`)
