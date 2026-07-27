---
id: ophtho_readability
title: "Language and Readability Barriers in Ophthalmology Dataset"
sidebar_label: ophtho_readability
description: "Text/tabular dataset supporting readability and language-access analyses in ophthalmology."
tags: ["text", "tabular", "cc-by", "zenodo", "text_generation", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Language and Readability Barriers in Ophthalmology Dataset

Text/tabular dataset supporting readability and language-access analyses in ophthalmology.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `ophtho_readability` |
| **Full name** | Language and Readability Barriers in Ophthalmology Dataset |
| **Primary category** | `text` |
| **Contained modalities** | text, tabular |
| **Tasks** | text_generation, classification |
| **Samples** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.01 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Zenodo |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download ophtho_readability --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download ophtho_readability --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('ophtho_readability')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [zenodo.org/records](https://zenodo.org/records/16592100)

**Source-term evidence:** [zenodo.org/records](https://zenodo.org/records/16592100)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{ophtho_readability,
  title  = { Language and Readability Barriers in Ophthalmology Dataset },
  note   = { Language and readability barriers in ophthalmology dataset. Zenodo, 2025. doi:10.5281/zenodo.16592100 },
  year   = { 2025 },
  url    = { https://zenodo.org/records/16592100 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Language and readability barriers in ophthalmology dataset. Zenodo, 2025. doi:10.5281/zenodo.16592100
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC BY 4.0
- **Normalized category:** `cc-by`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Standard label without an explicit NC clause; not a permission finding

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Related datasets with shared modalities

- [ocular_chat_vqa](./ocular_chat_vqa.md): OcularChat-VQA: AREDS-Derived Patient-Physician Dialogue Dataset (844,000 records, `cc-by-nc-sa`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 records, `unknown`)
- [soul_octa](./soul_octa.md): SOUL: OCTA Human-Machine Collaborative Annotation Dataset (178 records, `cc-by`)
- [fairvlmed](./fairvlmed.md): FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset (count not reported records, `unknown`)
- [fundus_cc_2_5m](./fundus_cc_2_5m.md): Fundus-CC-2.5M Text Corpus (2,500,000 records, `unknown`)
- [ophora](./ophora.md): Ophora-160K: Ophthalmic Surgical Video Instruction Dataset (160,185 records, `unknown`)
- [fundus_105k](./fundus_105k.md): Fundus-105K Text Dataset (105,000 records, `unknown`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 records, `unknown`)
