---
id: real_fundus
title: "Real Fundus Clinical Image Restoration Benchmark"
sidebar_label: real_fundus
description: "One hundred twenty paired low quality and high quality clinical fundus photographs of the same eyes at 2560 by 2560 pixels for image restoration and enhancement research."
tags: ["fundus", "unknown", "manual", "restoration", "resource-role-current-dataset", "dataset-family-real-fundus"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Real Fundus Clinical Image Restoration Benchmark

One hundred twenty paired low quality and high quality clinical fundus photographs of the same eyes at 2560 by 2560 pixels for image restoration and enhancement research.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `real_fundus` |
| **Full name** | Real Fundus Clinical Image Restoration Benchmark |
| **First published** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Primary category** | `fundus` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `real_fundus` |
| **Contained modalities** | fundus |
| **Tasks** | restoration |
| **Primary reported quantity** | 120 image pairs |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 1.02 GB |
| **Source-stated terms** | Unknown; no dataset license declared in the repository |
| **Normalized terms** | `unknown` |
| **Descriptive screening label** | Unknown or unclear; do not assume permission |
| **Terms scope** | `unknown` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `guided_instructions_only` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 120 | `image_pairs` | Matched low-quality and high-quality fundus pairs | `official_source_description` | [github.com/dengzhuo-AI](https://github.com/dengzhuo-AI/Real-Fundus) |
| Additional | 240 | `images` | Images participating in 120 restoration pairs | `derived_from_reported_components` | [github.com/dengzhuo-AI](https://github.com/dengzhuo-AI/Real-Fundus) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> The public GitHub release contains the image archive. The paper describes a random 81/9/30 experimental split, but the release does not define distributed train, validation, and test partitions. No license file or dataset use terms were found.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download real_fundus --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download real_fundus --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('real_fundus')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [github.com/dengzhuo-AI](https://github.com/dengzhuo-AI/Real-Fundus/releases/tag/v.1.0.0)

**Source-term evidence:** [github.com/dengzhuo-AI](https://github.com/dengzhuo-AI/Real-Fundus/releases/tag/v.1.0.0)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{real_fundus,
  title  = { Real Fundus Clinical Image Restoration Benchmark },
  note   = { Deng Z, Cai Y, Chen L, et al. RFormer: Transformer-based generative adversarial network for real fundus image restoration on a new clinical benchmark. IEEE J Biomed Health Inform. 2022;26:4645-4655. doi:10.1109/JBHI.2022.3187103 },
  year   = { 2022 },
  url    = { https://github.com/dengzhuo-AI/Real-Fundus/releases/tag/v.1.0.0 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Deng Z, Cai Y, Chen L, et al. RFormer: Transformer-based generative adversarial network for real fundus image restoration on a new clinical benchmark. IEEE J Biomed Health Inform. 2022;26:4645-4655. doi:10.1109/JBHI.2022.3187103
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Unknown; no dataset license declared in the repository
- **Normalized category:** `unknown`
- **Apparent scope:** `unknown`
- **Descriptive screening label:** Unknown or unclear; do not assume permission

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [airogs](./airogs.md): AIROGS: AI for Robust Glaucoma Screening (113,893 images, `cc-by-nc-nd`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (103,959 images, `mit`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [justraigs](./justraigs.md): JustRAIGS: Just Referral AI Glaucoma Screening Dataset (101,442 images, `cc-by-nc-nd`)
- [eyepacs](./eyepacs.md): EyePACS — Diabetic Retinopathy Detection (Kaggle 2015) (88,702 images, `research-only`)
- [angioreport](./angioreport.md): AngioReport Fundus Angiography Report Dataset (55,361 images, `unknown`)
- [ffa_ir](./ffa_ir.md): FFA-IR Medical Report Dataset (47,247 images, `unknown`)
- [mfiddr](./mfiddr.md): MFIDDR: Multi-Field Imaging Dataset for Diabetic Retinopathy (34,452 images, `mit`)
