---
id: lmod_cataract_1k_cot
title: "Cataract-1K Surgical Analysis Chain-of-Thought Dataset"
sidebar_label: lmod_cataract_1k_cot
description: "Synthetic surgical-analysis instruction/chain-of-thought dataset derived from Cataract-1K frames."
tags: ["multimodal", "surgical_video", "text", "mit", "huggingface", "visual_question_answering", "text_generation"]
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
| **Samples** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 1.0 GB |
| **Source-stated terms** | MIT |
| **Normalized terms** | `mit` |
| **Descriptive screening label** | Standard label without an explicit NC clause; verify that it applies to data |
| **Terms scope** | `unknown` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | HuggingFace Hub |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Notes

> Synthetic instruction layer derived from Cataract-1K; not an independent clinical dataset.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download lmod_cataract_1k_cot --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download lmod_cataract_1k_cot --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('lmod_cataract_1k_cot')
print(preflight_dataset(ds, './data'))  # no transfer
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

## Related datasets with shared modalities

- [ophora](./ophora.md): Ophora-160K: Ophthalmic Surgical Video Instruction Dataset (160,185 records, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 records, `unknown`)
- [fundus_cc_2_5m](./fundus_cc_2_5m.md): Fundus-CC-2.5M Text Corpus (2,500,000 records, `unknown`)
- [ocular_chat_vqa](./ocular_chat_vqa.md): OcularChat-VQA: AREDS-Derived Patient-Physician Dialogue Dataset (844,000 records, `cc-by-nc-sa`)
- [fundus_105k](./fundus_105k.md): Fundus-105K Text Dataset (105,000 records, `unknown`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 records, `unknown`)
- [angioreport](./angioreport.md): AngioReport Fundus Angiography Report Dataset (55,361 records, `unknown`)
- [ophthalmology_mcqa_v3](./ophthalmology_mcqa_v3.md): Ophthalmology-MCQA-v3 (51,745 records, `unknown`)
