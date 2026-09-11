---
id: eyecare_100k
title: "Eyecare-100K: Multimodal Ophthalmology VQA Corpus"
sidebar_label: eyecare_100k
description: "~102K VQA pairs derived from 58,485 images across 8 ophthalmic modalities (fluorescein angiography, ICGA, OCT, CFP, ultrasound biomicroscopy, slit-lamp, fundus auto-fluorescence, CT) covering 100+ dis"
tags: ["multimodal", "fundus", "fundus_angiography", "fundus_autofluorescence", "oct", "ocular_ultrasound", "external_eye", "ct", "text", "unknown", "huggingface", "classification", "resource-role-current-dataset", "dataset-family-eyecare-100k"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Eyecare-100K: Multimodal Ophthalmology VQA Corpus

~102K VQA pairs derived from 58,485 images across 8 ophthalmic modalities (fluorescein angiography, ICGA, OCT, CFP, ultrasound biomicroscopy, slit-lamp, fundus auto-fluorescence, CT) covering 100+ diseases.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `eyecare_100k` |
| **Full name** | Eyecare-100K: Multimodal Ophthalmology VQA Corpus |
| **First published** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Primary category** | `multimodal` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `eyecare_100k` |
| **Contained modalities** | fundus, fundus_angiography, fundus_autofluorescence, oct, ocular_ultrasound, external_eye, ct, text |
| **Tasks** | classification |
| **Primary reported quantity** | 102,000 question answer pairs |
| **Classes** | Not reported (Not reported) |
| **Splits** | train, val, test |
| **Size** | 30.0 GB |
| **Source-stated terms** | Mixed (inherits source-dataset licenses) — needs per-row check |
| **Normalized terms** | `unknown` |
| **Descriptive screening label** | Unknown or unclear; do not assume permission |
| **Terms scope** | `mixed_components` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | HuggingFace Hub |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 102,000 | `question_answer_pairs` | Source-described VQA corpus The dataset was described as pending release at the catalog cutoff. | `official_source_description` | [github.com/DCDmllm](https://github.com/DCDmllm/EyecareGPT) |
| Additional | 58,485 | `images` | Source images represented by the VQA corpus | `official_source_description` | [github.com/DCDmllm](https://github.com/DCDmllm/EyecareGPT) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Status: PENDING RELEASE. Largest open ophthalmology VQA corpus when published. EyecareGPT models are out (LLSuzy/* on HF) but the VQA dataset itself is not yet public as of 2026-06.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download eyecare_100k --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download eyecare_100k --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('eyecare_100k')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [github.com/DCDmllm](https://github.com/DCDmllm/EyecareGPT)

**Source-term evidence:** [github.com/DCDmllm](https://github.com/DCDmllm/EyecareGPT)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{eyecare_100k,
  title  = { Eyecare-100K: Multimodal Ophthalmology VQA Corpus },
  note   = { EyecareGPT: arXiv 2504.13650; ACM MM 2025. github.com/DCDmllm/EyecareGPT },
  year   = { 2025 },
  url    = { https://github.com/DCDmllm/EyecareGPT },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
EyecareGPT: arXiv 2504.13650; ACM MM 2025. github.com/DCDmllm/EyecareGPT
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Mixed (inherits source-dataset licenses) — needs per-row check
- **Normalized category:** `unknown`
- **Apparent scope:** `mixed_components`
- **Descriptive screening label:** Unknown or unclear; do not assume permission

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [ophthalvqa](./ophthalvqa.md): OphthalVQA Dataset (600 question answer pairs, `cc-by`)
- [x_pcr](./x_pcr.md): X-PCR Ophthalmology Progressive Clinical Reasoning Benchmark (18,735 rows, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [mm_retinal_reason](./mm_retinal_reason.md): MM-Retinal-Reason: Ophthalmology Multimodal Reasoning Dataset (130 question answer pairs, `unknown`)
- [angioreport](./angioreport.md): AngioReport Fundus Angiography Report Dataset (55,361 images, `unknown`)
- [ffa_ir](./ffa_ir.md): FFA-IR Medical Report Dataset (47,247 images, `unknown`)
- [jrc_multimodal_vessels](./jrc_multimodal_vessels.md): JRC Multi-Modal Retinal Vessel Segmentation (120 images, `unknown`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (103,959 images, `mit`)
