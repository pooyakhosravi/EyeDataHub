---
id: fundus_105k
title: "Fundus-105K Text Dataset"
sidebar_label: fundus_105k
description: "Fundus-focused text dataset for LLM/RAG workflows."
tags: ["text", "unknown", "huggingface", "text_generation", "retrieval"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Fundus-105K Text Dataset

Fundus-focused text dataset for LLM/RAG workflows.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `fundus_105k` |
| **Full name** | Fundus-105K Text Dataset |
| **Primary category** | `text` |
| **Contained modalities** | text |
| **Tasks** | text_generation, retrieval |
| **Samples** | 105,000 |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.5 GB |
| **Source-stated terms** | Unknown |
| **Normalized terms** | `unknown` |
| **Descriptive screening label** | Unknown or unclear; do not assume permission |
| **Terms scope** | `unknown` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | HuggingFace Hub |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download fundus_105k --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download fundus_105k --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('fundus_105k')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [huggingface.co/datasets](https://huggingface.co/datasets/PJMixers-Dev/Fundus-105K)

**Source-term evidence:** [huggingface.co/datasets](https://huggingface.co/datasets/PJMixers-Dev/Fundus-105K)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{fundus_105k,
  title  = { Fundus-105K Text Dataset },
  note   = { PJMixers-Dev/Fundus-105K. Hugging Face dataset, accessed 2026-07 },
  year   = { 2026 },
  url    = { https://huggingface.co/datasets/PJMixers-Dev/Fundus-105K },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
PJMixers-Dev/Fundus-105K. Hugging Face dataset, accessed 2026-07.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Unknown
- **Normalized category:** `unknown`
- **Apparent scope:** `unknown`
- **Descriptive screening label:** Unknown or unclear; do not assume permission

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Related datasets with shared modalities

- [fundus_cc_2_5m](./fundus_cc_2_5m.md): Fundus-CC-2.5M Text Corpus (2,500,000 records, `unknown`)
- [ocular_chat_vqa](./ocular_chat_vqa.md): OcularChat-VQA: AREDS-Derived Patient-Physician Dialogue Dataset (844,000 records, `cc-by-nc-sa`)
- [ophora](./ophora.md): Ophora-160K: Ophthalmic Surgical Video Instruction Dataset (160,185 records, `unknown`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 records, `unknown`)
- [angioreport](./angioreport.md): AngioReport Fundus Angiography Report Dataset (55,361 records, `unknown`)
- [ophthalmology_mcqa_v3](./ophthalmology_mcqa_v3.md): Ophthalmology-MCQA-v3 (51,745 records, `unknown`)
- [ophthalmology_eqa_v3](./ophthalmology_eqa_v3.md): Ophthalmology-EQA-v3 (49,300 records, `unknown`)
- [ffa_ir](./ffa_ir.md): FFA-IR Medical Report Dataset (47,247 records, `unknown`)
