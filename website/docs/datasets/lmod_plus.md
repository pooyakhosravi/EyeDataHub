---
id: lmod_plus
title: "LMOD+ Multimodal Ophthalmology Benchmark"
sidebar_label: lmod_plus
description: "Composite multimodal ophthalmology benchmark with multi-granular anatomical, diagnostic, staging, demographic, and text annotations."
tags: ["multimodal", "fundus", "oct", "external_eye", "surgical_video", "text", "tabular", "unknown", "manual", "visual_question_answering", "classification", "grading", "detection", "resource-role-derivative-dataset", "dataset-family-lmod-plus", "documented-relationship", "relationship-derived_from"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# LMOD+ Multimodal Ophthalmology Benchmark

Composite multimodal ophthalmology benchmark with multi-granular anatomical, diagnostic, staging, demographic, and text annotations.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `lmod_plus` |
| **Full name** | LMOD+ Multimodal Ophthalmology Benchmark |
| **First published** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Primary category** | `multimodal` |
| **Resource role** | `derivative_dataset` |
| **Dataset family** | `lmod_plus` |
| **Contained modalities** | fundus, oct, external_eye, surgical_video, text, tabular |
| **Tasks** | visual_question_answering, classification, grading, detection |
| **Primary reported quantity** | 32,633 annotated instances |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | Mixed upstream licenses; verify each component |
| **Normalized terms** | `unknown` |
| **Descriptive screening label** | Unknown or unclear; do not assume permission |
| **Terms scope** | `mixed_components` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `guided_instructions_only` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 32,633 | `annotated_instances` | Composite benchmark instances | `official_source_description` | [kfzyqin.github.io/lmod_plus](https://kfzyqin.github.io/lmod_plus/) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Integrates 32,633 instances from nine public datasets across five modalities and 12 conditions. It adds a distinct benchmark and annotation surface but does not replace the source datasets; license and redistribution terms remain component-specific.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- This record is `derived from` [cataract1k](./cataract1k.md): The LMOD+ project page lists nine component datasets, including the five cataloged targets represented by these edges. ([evidence](https://kfzyqin.github.io/lmod_plus/))
- This record is `derived from` [g1020](./g1020.md): The LMOD+ project page lists nine component datasets, including the five cataloged targets represented by these edges. ([evidence](https://kfzyqin.github.io/lmod_plus/))
- This record is `derived from` [idrid](./idrid.md): The LMOD+ project page lists nine component datasets, including the five cataloged targets represented by these edges. ([evidence](https://kfzyqin.github.io/lmod_plus/))
- This record is `derived from` [oimhs](./oimhs.md): The LMOD+ project page lists nine component datasets, including the five cataloged targets represented by these edges. ([evidence](https://kfzyqin.github.io/lmod_plus/))
- This record is `derived from` [refuge2](./refuge2.md): The LMOD+ project page lists nine component datasets, including the five cataloged targets represented by these edges. ([evidence](https://kfzyqin.github.io/lmod_plus/))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download lmod_plus --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download lmod_plus --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('lmod_plus')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [kfzyqin.github.io/lmod_plus](https://kfzyqin.github.io/lmod_plus/)

**Source-term evidence:** [kfzyqin.github.io/lmod_plus](https://kfzyqin.github.io/lmod_plus/)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{lmod_plus,
  title  = { LMOD+ Multimodal Ophthalmology Benchmark },
  note   = { Qin Z, Liu Y, Yin Y, et al. LMOD+: A Comprehensive Multimodal Dataset and Benchmark for Developing and Evaluating Multimodal Large Language Models in Ophthalmology. ACM Transactions on Computing for Healthcare. 2026. doi:10.1145/3801746 },
  year   = { 2026 },
  url    = { https://kfzyqin.github.io/lmod_plus/ },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Qin Z, Liu Y, Yin Y, et al. LMOD+: A Comprehensive Multimodal Dataset and Benchmark for Developing and Evaluating Multimodal Large Language Models in Ophthalmology. ACM Transactions on Computing for Healthcare. 2026. doi:10.1145/3801746
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Mixed upstream licenses; verify each component
- **Normalized category:** `unknown`
- **Apparent scope:** `mixed_components`
- **Descriptive screening label:** Unknown or unclear; do not assume permission

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [x_pcr](./x_pcr.md): X-PCR Ophthalmology Progressive Clinical Reasoning Benchmark (18,735 rows, `unknown`)
- [ophthalvqa](./ophthalvqa.md): OphthalVQA Dataset (600 question answer pairs, `cc-by`)
- [fairvlmed](./fairvlmed.md): FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset (10,000 images, `cc-by-nc-nd`)
- [olives](./olives.md): OLIVES: Ophthalmic Labels for Investigating Visual Eye Semantics (9,408 b scans, `cc-by`)
- [grape](./grape.md): GRAPE: Glaucoma Real-world Appraisal Progression Ensemble (1,115 examinations, `cc0`)
- [mm_retinal_reason](./mm_retinal_reason.md): MM-Retinal-Reason: Ophthalmology Multimodal Reasoning Dataset (130 question answer pairs, `unknown`)
- [ocular_chat_vqa](./ocular_chat_vqa.md): OcularChat-VQA: AREDS-Derived Patient-Physician Dialogue Dataset (844,000 records, `cc-by-nc-sa`)
