---
id: lmod_plus
title: "LMOD+ Multimodal Ophthalmology Benchmark"
sidebar_label: lmod_plus
description: "Composite multimodal ophthalmology benchmark with multi-granular anatomical, diagnostic, staging, demographic, and text annotations."
tags: ["multimodal", "fundus", "oct", "external_eye", "surgical_video", "text", "tabular", "unknown", "manual", "visual_question_answering", "classification", "grading", "detection"]
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
| **Primary category** | `multimodal` |
| **Contained modalities** | fundus, oct, external_eye, surgical_video, text, tabular |
| **Tasks** | visual_question_answering, classification, grading, detection |
| **Samples** | 32,633 |
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


## Notes

> Integrates 32,633 instances from nine public datasets across five modalities and 12 conditions. It adds a distinct benchmark and annotation surface but does not replace the source datasets; license and redistribution terms remain component-specific.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download lmod_plus --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download lmod_plus --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('lmod_plus')
print(preflight_dataset(ds, './data'))  # no transfer
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

## Related datasets with shared modalities

- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 records, `unknown`)
- [x_pcr](./x_pcr.md): X-PCR Ophthalmology Progressive Clinical Reasoning Benchmark (18,700 records, `unknown`)
- [ophthalvqa](./ophthalvqa.md): OphthalVQA Dataset (count not reported records, `cc-by`)
- [olives](./olives.md): OLIVES: Ophthalmic Labels for Investigating Visual Eye Semantics (9,408 records, `cc-by`)
- [grape](./grape.md): GRAPE: Glaucoma Real-world Appraisal Progression Ensemble (1,115 records, `cc0`)
- [dryad_subretinal_robot](./dryad_subretinal_robot.md): Head-Mounted Robot Subretinal Injection Dataset (count not reported records, `cc0`)
- [fairvlmed](./fairvlmed.md): FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset (count not reported records, `unknown`)
- [mm_retinal_reason](./mm_retinal_reason.md): MM-Retinal-Reason: Ophthalmology Multimodal Reasoning Dataset (count not reported records, `unknown`)
