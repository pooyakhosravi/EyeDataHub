---
id: ru_medical_texts_ophthalmology
title: "Ophthalmology Russian-English Medical Text Translations"
sidebar_label: ru_medical_texts_ophthalmology
description: "Russian-English ophthalmology sentence-pair and glossary dataset for translation and LLM evaluation."
tags: ["text", "cc-by", "kaggle", "translation", "text_generation"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Ophthalmology Russian-English Medical Text Translations

Russian-English ophthalmology sentence-pair and glossary dataset for translation and LLM evaluation.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `ru_medical_texts_ophthalmology` |
| **Full name** | Ophthalmology Russian-English Medical Text Translations |
| **Primary category** | `text` |
| **Contained modalities** | text |
| **Tasks** | translation, text_generation |
| **Samples** | 3,473 |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.01 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Kaggle |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download ru_medical_texts_ophthalmology --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download ru_medical_texts_ophthalmology --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('ru_medical_texts_ophthalmology')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [kaggle.com/datasets](https://www.kaggle.com/datasets/cheshrcat/ru-medical-texts-ophtalmology)

**Source-term evidence:** [kaggle.com/datasets](https://www.kaggle.com/datasets/cheshrcat/ru-medical-texts-ophtalmology)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{ru_medical_texts_ophthalmology,
  title  = { Ophthalmology Russian-English Medical Text Translations },
  note   = { Ophthalmology Russian/English translations. Kaggle, accessed 2026-07 },
  year   = { 2026 },
  url    = { https://www.kaggle.com/datasets/cheshrcat/ru-medical-texts-ophtalmology },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Ophthalmology Russian/English translations. Kaggle, accessed 2026-07.
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

- [fundus_cc_2_5m](./fundus_cc_2_5m.md): Fundus-CC-2.5M Text Corpus (2,500,000 records, `unknown`)
- [ocular_chat_vqa](./ocular_chat_vqa.md): OcularChat-VQA: AREDS-Derived Patient-Physician Dialogue Dataset (844,000 records, `cc-by-nc-sa`)
- [ophora](./ophora.md): Ophora-160K: Ophthalmic Surgical Video Instruction Dataset (162,185 records, `unknown`)
- [fundus_105k](./fundus_105k.md): Fundus-105K Text Dataset (105,000 records, `unknown`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 records, `unknown`)
- [angioreport](./angioreport.md): AngioReport Fundus Angiography Report Dataset (55,361 records, `unknown`)
- [ophthalmology_mcqa_v3](./ophthalmology_mcqa_v3.md): Ophthalmology-MCQA-v3 (51,745 records, `unknown`)
- [ophthalmology_eqa_v3](./ophthalmology_eqa_v3.md): Ophthalmology-EQA-v3 (49,300 records, `unknown`)
