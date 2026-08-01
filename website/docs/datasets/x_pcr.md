---
id: x_pcr
title: "X-PCR Ophthalmology Progressive Clinical Reasoning Benchmark"
sidebar_label: x_pcr
description: "The version-pinned public deposit contains 18,735 ophthalmic image-text benchmark rows across CFP, external-eye, FFA, OCT, and RetCam subsets."
tags: ["multimodal", "fundus", "fundus_angiography", "oct", "external_eye", "retcam", "text", "unknown", "huggingface", "visual_question_answering", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# X-PCR Ophthalmology Progressive Clinical Reasoning Benchmark

The version-pinned public deposit contains 18,735 ophthalmic image-text benchmark rows across CFP, external-eye, FFA, OCT, and RetCam subsets.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `x_pcr` |
| **Full name** | X-PCR Ophthalmology Progressive Clinical Reasoning Benchmark |
| **Primary category** | `multimodal` |
| **Contained modalities** | fundus, fundus_angiography, oct, external_eye, retcam, text |
| **Tasks** | visual_question_answering, classification |
| **Samples** | 18,735 |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 5.0 GB |
| **Source-stated terms** | Unknown |
| **Normalized terms** | `unknown` |
| **Descriptive screening label** | Unknown or unclear; do not assume permission |
| **Terms scope** | `unknown` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | HuggingFace Hub |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Notes

> The public deposit at commit 06a318fd852230326386e3c6514d8a11b7a6b4af has 18,735 rows. The dataset card describes a broader benchmark of 26,415 images and 177,868 VQA pairs; these units and scopes are not interchangeable.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download x_pcr --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download x_pcr --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('x_pcr')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [huggingface.co/datasets](https://huggingface.co/datasets/Fantasy666/X-PCR)

**Source-term evidence:** [huggingface.co/datasets](https://huggingface.co/datasets/Fantasy666/X-PCR)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{x_pcr,
  title  = { X-PCR Ophthalmology Progressive Clinical Reasoning Benchmark },
  note   = { Fantasy666/X-PCR. Hugging Face dataset, accessed 2026-07 },
  year   = { 2026 },
  url    = { https://huggingface.co/datasets/Fantasy666/X-PCR },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Fantasy666/X-PCR. Hugging Face dataset, accessed 2026-07.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Unknown
- **Normalized category:** `unknown`
- **Apparent scope:** `unknown`
- **Descriptive screening label:** Unknown or unclear; do not assume permission

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Related datasets with shared modalities

- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 records, `unknown`)
- [ophthalvqa](./ophthalvqa.md): OphthalVQA Dataset (count not reported records, `cc-by`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 records, `unknown`)
- [mm_retinal_reason](./mm_retinal_reason.md): MM-Retinal-Reason: Ophthalmology Multimodal Reasoning Dataset (count not reported records, `unknown`)
- [angioreport](./angioreport.md): AngioReport Fundus Angiography Report Dataset (55,361 records, `unknown`)
- [ffa_ir](./ffa_ir.md): FFA-IR Medical Report Dataset (47,247 records, `unknown`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (58,036 records, `mit`)
- [harvard_fairvision](./harvard_fairvision.md): Harvard-FairVision (AMD + DR + Glaucoma, paired SLO + OCT) (30,000 records, `cc-by-nc-nd`)
