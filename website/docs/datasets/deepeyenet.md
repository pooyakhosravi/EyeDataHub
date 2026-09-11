---
id: deepeyenet
title: "DeepEyeNet (DEN): Fundus Report Generation Dataset"
sidebar_label: deepeyenet
description: "15,709 fundus images with paired medical reports and extracted keywords. Only public fundus report-generation dataset — useful for VLM / captioning evaluation."
tags: ["fundus", "text", "research-only", "manual", "classification", "multilabel", "resource-role-current-dataset", "dataset-family-deepeyenet"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# DeepEyeNet (DEN): Fundus Report Generation Dataset

15,709 fundus images with paired medical reports and extracted keywords. Only public fundus report-generation dataset — useful for VLM / captioning evaluation.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `deepeyenet` |
| **Full name** | DeepEyeNet (DEN): Fundus Report Generation Dataset |
| **Publication date** | Unknown |
| **Date basis** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Date notes** | - |
| **Primary category** | `fundus` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `deepeyenet` |
| **Contained modalities** | fundus, text |
| **Tasks** | classification, multilabel |
| **Primary reported quantity** | 15,709 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | train, val, test |
| **Size** | 5.0 GB |
| **Source-stated terms** | Research only (NDA via email request) |
| **Normalized terms** | `research-only` |
| **Descriptive screening label** | Research or challenge restriction recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `author_contact` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `manual_access_blocked` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 15,709 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [github.com/Jhhuangkay](https://github.com/Jhhuangkay/DeepOpht-Medical-Report-Generation-for-Retinal-Images-via-Deep-Models-and-Visual-Explanation) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> NDA gated — email deepeyenet.den@gmail.com to request. No automated mirror exists.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# This route requires upstream human action; no transfer starts.
eyehub download deepeyenet --data-dir ./data --dry-run --json
# Follow the official instructions shown by preflight.
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('deepeyenet')
print(preflight_dataset(ds, './data'))  # returns manual_access_blocked
```

  </TabItem>
</Tabs>

**Upstream page:** [github.com/Jhhuangkay](https://github.com/Jhhuangkay/DeepOpht-Medical-Report-Generation-for-Retinal-Images-via-Deep-Models-and-Visual-Explanation)

**Source-term evidence:** [github.com/Jhhuangkay](https://github.com/Jhhuangkay/DeepOpht-Medical-Report-Generation-for-Retinal-Images-via-Deep-Models-and-Visual-Explanation)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{deepeyenet,
  title  = { DeepEyeNet (DEN): Fundus Report Generation Dataset },
  note   = { Huang et al., 'DeepOpht: Medical Report Generation for Retinal Images via Deep Models and Visual Explanation', WACV 2021 },
  year   = { 2021 },
  url    = { https://github.com/Jhhuangkay/DeepOpht-Medical-Report-Generation-for-Retinal-Images-via-Deep-Models-and-Visual-Explanation },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Huang et al., 'DeepOpht: Medical Report Generation for Retinal Images via Deep Models and Visual Explanation', WACV 2021.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Research only (NDA via email request)
- **Normalized category:** `research-only`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Research or challenge restriction recorded; check source

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [angioreport](./angioreport.md): AngioReport Fundus Angiography Report Dataset (55,361 images, `unknown`)
- [ffa_ir](./ffa_ir.md): FFA-IR Medical Report Dataset (47,247 images, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [x_pcr](./x_pcr.md): X-PCR Ophthalmology Progressive Clinical Reasoning Benchmark (18,735 rows, `unknown`)
- [dme_vqa](./dme_vqa.md): Diabetic Macular Edema Visual Question Answering Dataset (13,470 question answer pairs, `cc-by`)
- [dme_vqa_logical](./dme_vqa_logical.md): DME VQA Dataset with Logical Relations (13,470 question answer pairs, `cc-by`)
- [fairvlmed](./fairvlmed.md): FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset (10,000 images, `cc-by-nc-nd`)
