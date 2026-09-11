---
id: ophthalmology_pubmed_corpus
title: "Ophthalmology PubMed Corpus"
sidebar_label: ophthalmology_pubmed_corpus
description: "Ophthalmology-focused PubMed text corpus for retrieval, pretraining, or RAG experiments."
tags: ["text", "unknown", "huggingface", "text_generation", "retrieval", "resource-role-current-dataset", "dataset-family-ophthalmology-pubmed-corpus"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Ophthalmology PubMed Corpus

Ophthalmology-focused PubMed text corpus for retrieval, pretraining, or RAG experiments.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `ophthalmology_pubmed_corpus` |
| **Full name** | Ophthalmology PubMed Corpus |
| **First published** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Primary category** | `text` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `ophthalmology_pubmed_corpus` |
| **Contained modalities** | text |
| **Tasks** | text_generation, retrieval |
| **Primary reported quantity** | 39,794 documents |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.2 GB |
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
| Primary | 39,794 | `documents` | Ophthalmology-focused PubMed corpus records | `official_source_description` | [huggingface.co/datasets](https://huggingface.co/datasets/BaekSeungJu/Ophthalmology-PubMed-Corpus) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Verify PubMed redistribution terms and whether records are abstracts or full text before reuse.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download ophthalmology_pubmed_corpus --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download ophthalmology_pubmed_corpus --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('ophthalmology_pubmed_corpus')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [huggingface.co/datasets](https://huggingface.co/datasets/BaekSeungJu/Ophthalmology-PubMed-Corpus)

**Source-term evidence:** [huggingface.co/datasets](https://huggingface.co/datasets/BaekSeungJu/Ophthalmology-PubMed-Corpus)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{ophthalmology_pubmed_corpus,
  title  = { Ophthalmology PubMed Corpus },
  note   = { BaekSeungJu/Ophthalmology-PubMed-Corpus. Hugging Face dataset, accessed 2026-07 },
  year   = { 2026 },
  url    = { https://huggingface.co/datasets/BaekSeungJu/Ophthalmology-PubMed-Corpus },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
BaekSeungJu/Ophthalmology-PubMed-Corpus. Hugging Face dataset, accessed 2026-07.
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
- [ophthalmology_eqa_v3](./ophthalmology_eqa_v3.md): Ophthalmology-EQA-v3 (49,300 questions, `unknown`)
