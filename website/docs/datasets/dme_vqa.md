---
id: dme_vqa
title: "Diabetic Macular Edema Visual Question Answering Dataset"
sidebar_label: dme_vqa
description: "Fundus-image VQA dataset for diabetic macular edema derived from IDRiD and e-ophtha."
tags: ["multimodal", "fundus", "text", "cc-by", "zenodo", "visual_question_answering", "classification", "resource-role-annotation-layer", "dataset-family-dme-vqa", "documented-relationship", "relationship-extension_of", "relationship-derived_from"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Diabetic Macular Edema Visual Question Answering Dataset

Fundus-image VQA dataset for diabetic macular edema derived from IDRiD and e-ophtha.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dme_vqa` |
| **Full name** | Diabetic Macular Edema Visual Question Answering Dataset |
| **Primary category** | `multimodal` |
| **Resource role** | `annotation_layer` |
| **Dataset family** | `dme_vqa` |
| **Contained modalities** | fundus, text |
| **Tasks** | visual_question_answering, classification |
| **Primary reported quantity** | 13,470 question answer pairs |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.1 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Zenodo |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 13,470 | `question_answer_pairs` | Train, validation, and test QA pairs | `derived_from_reported_components` | [zenodo.org/records](https://zenodo.org/records/6784358) |
| Additional | 679 | `images` | Train, validation, and test images | `derived_from_reported_components` | [zenodo.org/records](https://zenodo.org/records/6784358) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Derivative VQA layer built from existing fundus datasets.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- [dme_vqa_logical](./dme_vqa_logical.md) is `extension of` this record: This release adds logical-relation annotations to the earlier DME VQA resource. ([evidence](https://zenodo.org/records/7777849))
- This record is `derived from` [e_ophtha](./e_ophtha.md): The DME VQA deposit identifies e-ophtha images as source material. ([evidence](https://zenodo.org/records/6784358))
- This record is `derived from` [idrid](./idrid.md): The DME VQA deposit identifies IDRiD images as source material. ([evidence](https://zenodo.org/records/6784358))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dme_vqa --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dme_vqa --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dme_vqa')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [zenodo.org/records](https://zenodo.org/records/6784358)

**Source-term evidence:** [zenodo.org/records](https://zenodo.org/records/6784358)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dme_vqa,
  title  = { Diabetic Macular Edema Visual Question Answering Dataset },
  note   = { Diabetic Macular Edema Visual Question Answering Dataset. Zenodo, 2022. doi:10.5281/zenodo.6784358 },
  year   = { 2022 },
  url    = { https://zenodo.org/records/6784358 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Diabetic Macular Edema Visual Question Answering Dataset. Zenodo, 2022. doi:10.5281/zenodo.6784358
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC BY 4.0
- **Normalized category:** `cc-by`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Standard label without an explicit NC clause; not a permission finding

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [angioreport](./angioreport.md): AngioReport Fundus Angiography Report Dataset (55,361 images, `unknown`)
- [ffa_ir](./ffa_ir.md): FFA-IR Medical Report Dataset (47,247 images, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [x_pcr](./x_pcr.md): X-PCR Ophthalmology Progressive Clinical Reasoning Benchmark (18,735 rows, `unknown`)
- [deepeyenet](./deepeyenet.md): DeepEyeNet (DEN): Fundus Report Generation Dataset (15,709 images, `research-only`)
- [dme_vqa_logical](./dme_vqa_logical.md): DME VQA Dataset with Logical Relations (13,470 question answer pairs, `cc-by`)
- [fairvlmed](./fairvlmed.md): FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset (10,000 images, `cc-by-nc-nd`)
