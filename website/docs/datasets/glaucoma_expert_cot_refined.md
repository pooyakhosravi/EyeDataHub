---
id: glaucoma_expert_cot_refined
title: "Glaucoma Expert Chain-of-Thought Refined Dataset"
sidebar_label: glaucoma_expert_cot_refined
description: "Revised glaucoma reasoning reports paired with the documented source fundus cases."
tags: ["fundus", "unknown", "huggingface", "classification", "image_text", "resource-role-annotation-layer", "dataset-family-glaucoma-expert-cot-refined", "documented-relationship", "relationship-derived_from", "alternate-source", "source-huggingface", "alternate-role-previous-version"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Glaucoma Expert Chain-of-Thought Refined Dataset

Revised glaucoma reasoning reports paired with the documented source fundus cases.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `glaucoma_expert_cot_refined` |
| **Full name** | Glaucoma Expert Chain-of-Thought Refined Dataset |
| **Primary category** | `fundus` |
| **Resource role** | `annotation_layer` |
| **Dataset family** | `glaucoma_expert_cot_refined` |
| **Contained modalities** | fundus |
| **Tasks** | classification, image_text |
| **Primary reported quantity** | 1,074 image report pairs |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | Other; source-image terms apply |
| **Normalized terms** | `unknown` |
| **Descriptive screening label** | Unknown or unclear; do not assume permission |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | HuggingFace Hub |
| **Availability** | `available` (checked 2026-08-02) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 1,074 | `image_report_pairs` | Source reports 1,074 fundus cases with refined JSONL reasoning records. Source-stated quantity; repository file count is separate. | `official_source_description` | [huggingface.co/datasets](https://huggingface.co/datasets/yuzhench/glaucoma-expert-cot-refined-1077) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Current refined release. The earlier raw reasoning release is retained as version history and is not counted separately.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- This record is `derived from` [lag](./lag.md): The official dataset card identifies LAG and PAPILA as the source fundus resources paired with the refined glaucoma reasoning records. ([evidence](https://huggingface.co/datasets/yuzhench/glaucoma-expert-cot-refined-1077))
- This record is `derived from` [papila](./papila.md): The official dataset card identifies LAG and PAPILA as the source fundus resources paired with the refined glaucoma reasoning records. ([evidence](https://huggingface.co/datasets/yuzhench/glaucoma-expert-cot-refined-1077))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download glaucoma_expert_cot_refined --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download glaucoma_expert_cot_refined --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('glaucoma_expert_cot_refined')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [huggingface.co/datasets](https://huggingface.co/datasets/yuzhench/glaucoma-expert-cot-refined-1077)

## Other documented locations

These links identify alternate deposits, components, metadata records, mirrors, versions, or related derived materials. They do not create additional canonical catalog records.

- [huggingface: previous version (yuzhench/glaucoma-expert-cot-raw-1077, version raw)](https://huggingface.co/datasets/yuzhench/glaucoma-expert-cot-raw-1077): Earlier reasoning release superseded by the refined record.

**Source-term evidence:** [huggingface.co/datasets](https://huggingface.co/datasets/yuzhench/glaucoma-expert-cot-refined-1077)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{glaucoma_expert_cot_refined,
  title  = { Glaucoma Expert Chain-of-Thought Refined Dataset },
  note   = { Repository dataset record. yuzhench/glaucoma-expert-cot-refined-1077 },
  url    = { https://huggingface.co/datasets/yuzhench/glaucoma-expert-cot-refined-1077 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Repository dataset record. yuzhench/glaucoma-expert-cot-refined-1077.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Other; source-image terms apply
- **Normalized category:** `unknown`
- **Apparent scope:** `dataset_files`
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
