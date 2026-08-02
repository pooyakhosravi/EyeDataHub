---
id: ophthalmology_eqa_v3
title: "Ophthalmology-EQA-v3"
sidebar_label: ophthalmology_eqa_v3
description: "Text-only ophthalmology explanatory/free-form question-answering dataset for LLM training/evaluation."
tags: ["text", "unknown", "huggingface", "question_answering", "text_generation"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Ophthalmology-EQA-v3

Text-only ophthalmology explanatory/free-form question-answering dataset for LLM training/evaluation.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `ophthalmology_eqa_v3` |
| **Full name** | Ophthalmology-EQA-v3 |
| **Primary category** | `text` |
| **Contained modalities** | text |
| **Tasks** | question_answering, text_generation |
| **Primary reported quantity** | 49,300 questions |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.1 GB |
| **Source-stated terms** | Unknown |
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
| Primary | 49,300 | `questions` | Explanatory or free-form ophthalmology questions | `official_source_description` | [huggingface.co/datasets](https://huggingface.co/datasets/BaekSeungJu/Ophthalmology-EQA-v3) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download ophthalmology_eqa_v3 --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download ophthalmology_eqa_v3 --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('ophthalmology_eqa_v3')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [huggingface.co/datasets](https://huggingface.co/datasets/BaekSeungJu/Ophthalmology-EQA-v3)

**Source-term evidence:** [huggingface.co/datasets](https://huggingface.co/datasets/BaekSeungJu/Ophthalmology-EQA-v3)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{ophthalmology_eqa_v3,
  title  = { Ophthalmology-EQA-v3 },
  note   = { BaekSeungJu/Ophthalmology-EQA-v3. Hugging Face dataset, accessed 2026-07 },
  year   = { 2026 },
  url    = { https://huggingface.co/datasets/BaekSeungJu/Ophthalmology-EQA-v3 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
BaekSeungJu/Ophthalmology-EQA-v3. Hugging Face dataset, accessed 2026-07.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Unknown
- **Normalized category:** `unknown`
- **Apparent scope:** `unknown`
- **Descriptive screening label:** Unknown or unclear; do not assume permission

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [fundus_cc_2_5m](./fundus_cc_2_5m.md): Fundus-CC-2.5M Text Corpus (2,500,000 text items, `unknown`)
- [ocular_chat_vqa](./ocular_chat_vqa.md): OcularChat-VQA: AREDS-Derived Patient-Physician Dialogue Dataset (844,000 records, `cc-by-nc-sa`)
- [ophora](./ophora.md): Ophora-160K: Ophthalmic Surgical Video Instruction Dataset (162,185 video clip instruction pairs, `unknown`)
- [fundus_105k](./fundus_105k.md): Fundus-105K Text Dataset (105,000 text items, `unknown`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [angioreport](./angioreport.md): AngioReport Fundus Angiography Report Dataset (55,361 images, `unknown`)
- [ophthalmology_mcqa_v3](./ophthalmology_mcqa_v3.md): Ophthalmology-MCQA-v3 (51,745 questions, `unknown`)
- [ffa_ir](./ffa_ir.md): FFA-IR Medical Report Dataset (47,247 images, `unknown`)
