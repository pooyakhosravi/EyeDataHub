---
id: dme_vqa_logical
title: "DME VQA Dataset with Logical Relations"
sidebar_label: dme_vqa_logical
description: "Extension of the DME VQA dataset with logical-relation consistency annotations."
tags: ["multimodal", "fundus", "text", "cc-by", "zenodo", "visual_question_answering", "resource-role-annotation-layer", "dataset-family-dme-vqa-logical", "documented-relationship", "relationship-extension_of"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# DME VQA Dataset with Logical Relations

Extension of the DME VQA dataset with logical-relation consistency annotations.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dme_vqa_logical` |
| **Full name** | DME VQA Dataset with Logical Relations |
| **First published** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Primary category** | `multimodal` |
| **Resource role** | `annotation_layer` |
| **Dataset family** | `dme_vqa_logical` |
| **Contained modalities** | fundus, text |
| **Tasks** | visual_question_answering |
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
| Primary | 13,470 | `question_answer_pairs` | DME VQA pairs with added logical relations The source states that this is the same DME VQA dataset with logical relations added. | `official_source_description` | [zenodo.org/records](https://zenodo.org/records/7777849) |
| Additional | 679 | `images` | Parent DME VQA images reused by this extension These images overlap completely with dme_vqa. | `official_source_description` | [zenodo.org/records](https://zenodo.org/records/7777849) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Derivative extension of DME VQA; not an independent image cohort.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- This record is `extension of` [dme_vqa](./dme_vqa.md): This release adds logical-relation annotations to the earlier DME VQA resource. ([evidence](https://zenodo.org/records/7777849))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dme_vqa_logical --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dme_vqa_logical --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dme_vqa_logical')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [zenodo.org/records](https://zenodo.org/records/7777849)

**Source-term evidence:** [zenodo.org/records](https://zenodo.org/records/7777849)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dme_vqa_logical,
  title  = { DME VQA Dataset with Logical Relations },
  note   = { DME VQA dataset with logical relations. Zenodo, 2023. doi:10.5281/zenodo.7777849 },
  year   = { 2023 },
  url    = { https://zenodo.org/records/7777849 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
DME VQA dataset with logical relations. Zenodo, 2023. doi:10.5281/zenodo.7777849
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
- [dme_vqa](./dme_vqa.md): Diabetic Macular Edema Visual Question Answering Dataset (13,470 question answer pairs, `cc-by`)
- [fairvlmed](./fairvlmed.md): FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset (10,000 images, `cc-by-nc-nd`)
