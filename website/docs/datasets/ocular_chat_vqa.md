---
id: ocular_chat_vqa
title: "OcularChat-VQA: AREDS-Derived Patient-Physician Dialogue Dataset"
sidebar_label: ocular_chat_vqa
description: "844,000 simulated patient-physician dialogue rows generated from AREDS clinical visits. Enables ophthalmic dialogue and counseling VLM training."
tags: ["multimodal", "text", "tabular", "cc-by-nc-sa", "huggingface", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# OcularChat-VQA: AREDS-Derived Patient-Physician Dialogue Dataset

844,000 simulated patient-physician dialogue rows generated from AREDS clinical visits. Enables ophthalmic dialogue and counseling VLM training.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `ocular_chat_vqa` |
| **Full name** | OcularChat-VQA: AREDS-Derived Patient-Physician Dialogue Dataset |
| **Primary category** | `multimodal` |
| **Contained modalities** | text, tabular |
| **Tasks** | classification |
| **Primary reported quantity** | 844,000 records |
| **Classes** | Not reported (Not reported) |
| **Splits** | train, val, test |
| **Size** | 8.0 GB |
| **Source-stated terms** | CC BY-NC-SA 4.0 |
| **Normalized terms** | `cc-by-nc-sa` |
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
| Primary | 844,000 | `records` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [huggingface.co/datasets](https://huggingface.co/datasets/ncbi/OcularChat-VQA) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Images path may reference AREDS — access to underlying images requires separate NCBI/dbGaP approval. Verify before use.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download ocular_chat_vqa --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download ocular_chat_vqa --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('ocular_chat_vqa')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [huggingface.co/datasets](https://huggingface.co/datasets/ncbi/OcularChat-VQA)

**Source-term evidence:** [huggingface.co/datasets](https://huggingface.co/datasets/ncbi/OcularChat-VQA)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{ocular_chat_vqa,
  title  = { OcularChat-VQA: AREDS-Derived Patient-Physician Dialogue Dataset },
  note   = { OcularChat-VQA: AREDS-derived patient-physician dialogues. HuggingFace / NCBI, 2025 },
  year   = { 2025 },
  url    = { https://huggingface.co/datasets/ncbi/OcularChat-VQA },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
OcularChat-VQA: AREDS-derived patient-physician dialogues. HuggingFace / NCBI, 2025.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC BY-NC-SA 4.0
- **Normalized category:** `cc-by-nc-sa`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Explicit noncommercial clause recorded; check source

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [fairvlmed](./fairvlmed.md): FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset (10,000 images, `cc-by-nc-nd`)
- [soul_octa](./soul_octa.md): SOUL: OCTA Human-Machine Collaborative Annotation Dataset (178 longitudinal samples, `cc-by`)
- [ophtho_readability](./ophtho_readability.md): Language and Readability Barriers in Ophthalmology Dataset (139 documents, `cc-by`)
- [fundus_cc_2_5m](./fundus_cc_2_5m.md): Fundus-CC-2.5M Text Corpus (2,500,000 text items, `unknown`)
- [ophora](./ophora.md): Ophora-160K: Ophthalmic Surgical Video Instruction Dataset (162,185 video clip instruction pairs, `unknown`)
- [fundus_105k](./fundus_105k.md): Fundus-105K Text Dataset (105,000 text items, `unknown`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
