---
id: ophthalwechat
title: "OphthalWeChat Dataset"
sidebar_label: ophthalwechat
description: "Ophthalmology-oriented WeChat article metadata and image-link dataset for visual question answering and multimodal language-model evaluation."
tags: ["text", "cc-by", "figshare", "visual_question_answering", "retrieval"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# OphthalWeChat Dataset

Ophthalmology-oriented WeChat article metadata and image-link dataset for visual question answering and multimodal language-model evaluation.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `ophthalwechat` |
| **Full name** | OphthalWeChat Dataset |
| **Primary category** | `text` |
| **Contained modalities** | text |
| **Tasks** | visual_question_answering, retrieval |
| **Samples** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.002 GB |
| **Source-stated terms** | CC BY 4.0 for the deposited Figshare files |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `mixed_components` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Figshare |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `end_to_end_tested` |
| **Legacy sample-loader status** | Metadata and access only |


## Notes

> Figshare marks the deposited index files CC BY 4.0. The record exposes URLs and WeChat article identifiers rather than redistributing image files, so original content permissions still need separate review.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download ophthalwechat --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download ophthalwechat --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('ophthalwechat')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.6084/m9.figshare.29064149](https://doi.org/10.6084/m9.figshare.29064149)

**Source-term evidence:** [https://doi.org/10.6084/m9.figshare.29064149](https://doi.org/10.6084/m9.figshare.29064149)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{ophthalwechat,
  title  = { OphthalWeChat Dataset },
  note   = { Xu P. OphthalWeChat. Figshare, 2025. doi:10.6084/m9.figshare.29064149 },
  year   = { 2025 },
  url    = { https://doi.org/10.6084/m9.figshare.29064149 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Xu P. OphthalWeChat. Figshare, 2025. doi:10.6084/m9.figshare.29064149
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC BY 4.0 for the deposited Figshare files
- **Normalized category:** `cc-by`
- **Apparent scope:** `mixed_components`
- **Descriptive screening label:** Standard label without an explicit NC clause; not a permission finding

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Related datasets with shared modalities

- [fundus_cc_2_5m](./fundus_cc_2_5m.md): Fundus-CC-2.5M Text Corpus (2,500,000 records, `unknown`)
- [ocular_chat_vqa](./ocular_chat_vqa.md): OcularChat-VQA: AREDS-Derived Patient-Physician Dialogue Dataset (844,000 records, `cc-by-nc-sa`)
- [ophora](./ophora.md): Ophora-160K: Ophthalmic Surgical Video Instruction Dataset (160,185 records, `unknown`)
- [fundus_105k](./fundus_105k.md): Fundus-105K Text Dataset (105,000 records, `unknown`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 records, `unknown`)
- [angioreport](./angioreport.md): AngioReport Fundus Angiography Report Dataset (55,361 records, `unknown`)
- [ophthalmology_mcqa_v3](./ophthalmology_mcqa_v3.md): Ophthalmology-MCQA-v3 (51,745 records, `unknown`)
- [ophthalmology_eqa_v3](./ophthalmology_eqa_v3.md): Ophthalmology-EQA-v3 (49,300 records, `unknown`)
