---
id: belo
title: "BELO Benchmark for Evaluating Language Models in Ophthalmology"
sidebar_label: belo
description: "Expert-curated ophthalmology multiple-choice benchmark with rationales, assembled for held-out language-model evaluation."
tags: ["text", "unknown", "manual", "question_answering", "evaluation", "reasoning"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# BELO Benchmark for Evaluating Language Models in Ophthalmology

Expert-curated ophthalmology multiple-choice benchmark with rationales, assembled for held-out language-model evaluation.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `belo` |
| **Full name** | BELO Benchmark for Evaluating Language Models in Ophthalmology |
| **Primary category** | `text` |
| **Contained modalities** | text |
| **Tasks** | question_answering, evaluation, reasoning |
| **Primary reported quantity** | 900 questions |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | Unknown; mixed upstream question-bank terms |
| **Normalized terms** | `unknown` |
| **Descriptive screening label** | Unknown or unclear; do not assume permission |
| **Terms scope** | `mixed_components` |
| **Access friction** | `author_contact` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `manual_access_blocked` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 900 | `questions` | Held-out multiple-choice benchmark | `official_source_description` | [belo-dataset.vercel.app](https://belo-dataset.vercel.app/) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> The 900 questions aggregate BCSC, BioASQ, MedMCQA, MedQA, and PubMedQA sources. The project page instructs users to request the held-out benchmark by email; verify every applicable source term.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# This route requires upstream human action; no transfer starts.
eyehub download belo --data-dir ./data --dry-run --json
# Follow the official instructions shown by preflight.
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('belo')
print(preflight_dataset(ds, './data'))  # returns manual_access_blocked
```

  </TabItem>
</Tabs>

**Upstream page:** [belo-dataset.vercel.app](https://belo-dataset.vercel.app/)

**Source-term evidence:** [belo-dataset.vercel.app](https://belo-dataset.vercel.app/)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{belo,
  title  = { BELO Benchmark for Evaluating Language Models in Ophthalmology },
  note   = { BELO: A Benchmark for Evaluation of Language Models in Ophthalmology. Ophthalmology Science. 2025:101050. doi:10.1016/j.xops.2025.101050 },
  year   = { 2025 },
  url    = { https://belo-dataset.vercel.app/ },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
BELO: A Benchmark for Evaluation of Language Models in Ophthalmology. Ophthalmology Science. 2025:101050. doi:10.1016/j.xops.2025.101050
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Unknown; mixed upstream question-bank terms
- **Normalized category:** `unknown`
- **Apparent scope:** `mixed_components`
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
- [ophthalmology_eqa_v3](./ophthalmology_eqa_v3.md): Ophthalmology-EQA-v3 (49,300 questions, `unknown`)
