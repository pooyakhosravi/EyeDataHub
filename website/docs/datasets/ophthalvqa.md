---
id: ophthalvqa
title: "OphthalVQA Dataset"
sidebar_label: ophthalvqa
description: "Ophthalmic visual question-answering benchmark dataset released as supplementary data for evaluating multimodal language models in ophthalmology."
tags: ["multimodal", "fundus", "fundus_angiography", "oct", "ocular_ultrasound", "external_eye", "text", "cc-by", "figshare", "visual_question_answering", "classification", "resource-role-current-dataset", "dataset-family-ophthalvqa"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# OphthalVQA Dataset

Ophthalmic visual question-answering benchmark dataset released as supplementary data for evaluating multimodal language models in ophthalmology.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `ophthalvqa` |
| **Full name** | OphthalVQA Dataset |
| **Primary category** | `multimodal` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `ophthalvqa` |
| **Contained modalities** | fundus, fundus_angiography, oct, ocular_ultrasound, external_eye, text |
| **Tasks** | visual_question_answering, classification |
| **Primary reported quantity** | 600 question answer pairs |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.03 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Figshare |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `end_to_end_tested` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 600 | `question_answer_pairs` | Rows in OphthalVQA.csv | `current_deposit_table` | [https://doi.org/10.6084/m9.figshare.25624917](https://doi.org/10.6084/m9.figshare.25624917) |
| Additional | 60 | `images` | JPG image files in the current deposit | `current_deposit_file_listing` | [https://doi.org/10.6084/m9.figshare.25624917](https://doi.org/10.6084/m9.figshare.25624917) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Supplementary benchmark for ophthalmic VQA and multimodal model evaluation; inspect image provenance and splits before leakage-sensitive validation.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download ophthalvqa --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download ophthalvqa --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('ophthalvqa')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.6084/m9.figshare.25624917](https://doi.org/10.6084/m9.figshare.25624917)

**Source-term evidence:** [https://doi.org/10.6084/m9.figshare.25624917](https://doi.org/10.6084/m9.figshare.25624917)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{ophthalvqa,
  title  = { OphthalVQA Dataset },
  note   = { Xu P, Chen X, Zhao Z, Shi D. OphthalVQA Dataset. Figshare, 2025. doi:10.6084/m9.figshare.25624917 },
  year   = { 2025 },
  url    = { https://doi.org/10.6084/m9.figshare.25624917 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Xu P, Chen X, Zhao Z, Shi D. OphthalVQA Dataset. Figshare, 2025. doi:10.6084/m9.figshare.25624917
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
- [x_pcr](./x_pcr.md): X-PCR Ophthalmology Progressive Clinical Reasoning Benchmark (18,735 rows, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [mm_retinal_reason](./mm_retinal_reason.md): MM-Retinal-Reason: Ophthalmology Multimodal Reasoning Dataset (130 question answer pairs, `unknown`)
- [angioreport](./angioreport.md): AngioReport Fundus Angiography Report Dataset (55,361 images, `unknown`)
- [ffa_ir](./ffa_ir.md): FFA-IR Medical Report Dataset (47,247 images, `unknown`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (103,959 images, `mit`)
- [harvard_fairvision](./harvard_fairvision.md): Harvard-FairVision (AMD + DR + Glaucoma, paired SLO + OCT) (30,000 participants, `cc-by-nc-nd`)
