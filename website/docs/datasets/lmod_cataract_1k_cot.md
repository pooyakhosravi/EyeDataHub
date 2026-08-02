---
id: lmod_cataract_1k_cot
title: "Cataract-1K Surgical Analysis Chain-of-Thought Dataset"
sidebar_label: lmod_cataract_1k_cot
description: "Synthetic surgical-analysis instruction/chain-of-thought dataset derived from Cataract-1K frames."
tags: ["multimodal", "surgical_video", "text", "mit", "huggingface", "visual_question_answering", "text_generation", "documented-relationship", "relationship-derived_from"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Cataract-1K Surgical Analysis Chain-of-Thought Dataset

Synthetic surgical-analysis instruction/chain-of-thought dataset derived from Cataract-1K frames.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `lmod_cataract_1k_cot` |
| **Full name** | Cataract-1K Surgical Analysis Chain-of-Thought Dataset |
| **Primary category** | `multimodal` |
| **Contained modalities** | surgical_video, text |
| **Tasks** | visual_question_answering, text_generation |
| **Primary reported quantity** | 2,256 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 1.0 GB |
| **Source-stated terms** | MIT |
| **Normalized terms** | `mit` |
| **Descriptive screening label** | Standard label without an explicit NC clause; verify that it applies to data |
| **Terms scope** | `unknown` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | HuggingFace Hub |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 2,256 | `images` | PNG images in the versioned Hugging Face deposit | `current_deposit_file_listing` | [huggingface.co/datasets](https://huggingface.co/datasets/mehti/LMOD-Cataract-1K-surgical-analysis-cot) |
| Additional | 11,280 | `question_answer_pairs` | Rows across five cross-validation train/validation fold pairs The five folds repeat the 2,256 source images; 11,280 is not a unique-image count. | `current_deposit_table` | [huggingface.co/datasets](https://huggingface.co/datasets/mehti/LMOD-Cataract-1K-surgical-analysis-cot) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Synthetic instruction layer derived from Cataract-1K; not an independent clinical dataset.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- This record is `derived from` [lmod_cataract_1k](./lmod_cataract_1k.md): The dataset card identifies LMOD-Cataract-1K as its image source. ([evidence](https://huggingface.co/datasets/mehti/LMOD-Cataract-1K-surgical-analysis-cot))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download lmod_cataract_1k_cot --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download lmod_cataract_1k_cot --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('lmod_cataract_1k_cot')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [huggingface.co/datasets](https://huggingface.co/datasets/mehti/LMOD-Cataract-1K-surgical-analysis-cot)

**Source-term evidence:** [huggingface.co/datasets](https://huggingface.co/datasets/mehti/LMOD-Cataract-1K-surgical-analysis-cot)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{lmod_cataract_1k_cot,
  title  = { Cataract-1K Surgical Analysis Chain-of-Thought Dataset },
  note   = { mehti/LMOD-Cataract-1K-surgical-analysis-cot. Hugging Face dataset, accessed 2026-07 },
  year   = { 2026 },
  url    = { https://huggingface.co/datasets/mehti/LMOD-Cataract-1K-surgical-analysis-cot },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
mehti/LMOD-Cataract-1K-surgical-analysis-cot. Hugging Face dataset, accessed 2026-07.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** MIT
- **Normalized category:** `mit`
- **Apparent scope:** `unknown`
- **Descriptive screening label:** Standard label without an explicit NC clause; verify that it applies to data

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [ophora](./ophora.md): Ophora-160K: Ophthalmic Surgical Video Instruction Dataset (162,185 video clip instruction pairs, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [fundus_cc_2_5m](./fundus_cc_2_5m.md): Fundus-CC-2.5M Text Corpus (2,500,000 text items, `unknown`)
- [ocular_chat_vqa](./ocular_chat_vqa.md): OcularChat-VQA: AREDS-Derived Patient-Physician Dialogue Dataset (844,000 records, `cc-by-nc-sa`)
- [fundus_105k](./fundus_105k.md): Fundus-105K Text Dataset (105,000 text items, `unknown`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [angioreport](./angioreport.md): AngioReport Fundus Angiography Report Dataset (55,361 images, `unknown`)
- [ophthalmology_mcqa_v3](./ophthalmology_mcqa_v3.md): Ophthalmology-MCQA-v3 (51,745 questions, `unknown`)
