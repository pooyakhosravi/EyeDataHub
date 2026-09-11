---
id: ophora
title: "Ophora-160K: Ophthalmic Surgical Video Instruction Dataset"
sidebar_label: ophora
description: "162,185 video clip-instruction pair samples from 9,819 ophthalmic surgical videos, covering multiple procedure types. Designed for text-guided surgical video generation and understanding. Published at"
tags: ["surgical_video", "text", "unknown", "huggingface", "classification", "phase_recognition", "resource-role-current-dataset", "dataset-family-ophora"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Ophora-160K: Ophthalmic Surgical Video Instruction Dataset

162,185 video clip-instruction pair samples from 9,819 ophthalmic surgical videos, covering multiple procedure types. Designed for text-guided surgical video generation and understanding. Published at MICCAI 2025.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `ophora` |
| **Full name** | Ophora-160K: Ophthalmic Surgical Video Instruction Dataset |
| **Publication date** | Unknown |
| **Date basis** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Date notes** | - |
| **Primary category** | `surgical_video` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `ophora` |
| **Contained modalities** | surgical_video, text |
| **Tasks** | classification, phase_recognition |
| **Primary reported quantity** | 162,185 video clip instruction pairs |
| **Classes** | Not reported (Not reported) |
| **Splits** | train |
| **Size** | 500.0 GB |
| **Source-stated terms** | Unknown — no license stated |
| **Normalized terms** | `unknown` |
| **Descriptive screening label** | Unknown or unclear; do not assume permission |
| **Terms scope** | `unknown` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | HuggingFace Hub |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Standard loader included |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 162,185 | `video_clip_instruction_pairs` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [huggingface.co/datasets](https://huggingface.co/datasets/General-Medical-AI/Ophora-160K) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> 162,185 video clip-instruction pairs from 9,819 source videos (avg clip length ~5.5 s). Estimated ~500 GB total. Video clip-instruction pair dataset for text-guided surgical video generation. May require HF_TOKEN for gated access. Set in .env.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download ophora --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download ophora --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('ophora')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [huggingface.co/datasets](https://huggingface.co/datasets/General-Medical-AI/Ophora-160K)

**Source-term evidence:** [huggingface.co/datasets](https://huggingface.co/datasets/General-Medical-AI/Ophora-160K)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('ophora')
samples = ds.load(data_dir, split='train')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{ophora,
  title  = { Ophora-160K: Ophthalmic Surgical Video Instruction Dataset },
  note   = { Ophora: Text-Guided Ophthalmic Surgical Video Generation. MICCAI 2025. arXiv:2505.07449. HuggingFace: https://huggingface.co/datasets/General-Medical-AI/Ophora-160K — GitHub: https://github.com/uni-medical/Ophora },
  year   = { 2025 },
  url    = { https://huggingface.co/datasets/General-Medical-AI/Ophora-160K },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Ophora: Text-Guided Ophthalmic Surgical Video Generation. MICCAI 2025. arXiv:2505.07449. HuggingFace: https://huggingface.co/datasets/General-Medical-AI/Ophora-160K — GitHub: https://github.com/uni-medical/Ophora
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Unknown — no license stated
- **Normalized category:** `unknown`
- **Apparent scope:** `unknown`
- **Descriptive screening label:** Unknown or unclear; do not assume permission

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [lmod_cataract_1k_cot](./lmod_cataract_1k_cot.md): Cataract-1K Surgical Analysis Chain-of-Thought Dataset (2,256 images, `mit`)
- [fundus_cc_2_5m](./fundus_cc_2_5m.md): Fundus-CC-2.5M Text Corpus (2,500,000 text items, `unknown`)
- [ocular_chat_vqa](./ocular_chat_vqa.md): OcularChat-VQA: AREDS-Derived Patient-Physician Dialogue Dataset (844,000 records, `cc-by-nc-sa`)
- [fundus_105k](./fundus_105k.md): Fundus-105K Text Dataset (105,000 text items, `unknown`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [angioreport](./angioreport.md): AngioReport Fundus Angiography Report Dataset (55,361 images, `unknown`)
- [ophthalmology_mcqa_v3](./ophthalmology_mcqa_v3.md): Ophthalmology-MCQA-v3 (51,745 questions, `unknown`)
