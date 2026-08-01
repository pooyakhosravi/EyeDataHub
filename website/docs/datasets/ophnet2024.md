---
id: ophnet2024
title: "OphNet2024: Ophthalmic Surgical Video Dataset"
sidebar_label: ophnet2024
description: "Large-scale multi-procedure ophthalmic surgical video dataset covering 66 surgery types, 102 phases, 150 operations (~285 h). 1,969 untrimmed videos; 17,508 trimmed operation-level clips; 14,674 trimm"
tags: ["surgical_video", "cc-by-nc-sa", "huggingface", "classification", "phase_recognition", "detection"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# OphNet2024: Ophthalmic Surgical Video Dataset

Large-scale multi-procedure ophthalmic surgical video dataset covering 66 surgery types, 102 phases, 150 operations (~285 h). 1,969 untrimmed videos; 17,508 trimmed operation-level clips; 14,674 trimmed phase-level clips across cataract, vitreoretinal, glaucoma, corneal, refractive, oculoplastic, and strabismus. 743 videos have time-boundary annotations. ECCV 2024.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `ophnet2024` |
| **Full name** | OphNet2024: Ophthalmic Surgical Video Dataset |
| **Primary category** | `surgical_video` |
| **Contained modalities** | surgical_video |
| **Tasks** | classification, phase_recognition, detection |
| **Primary reported quantity** | 2,278 videos |
| **Classes** | 8 (Cataract Surgery, Vitreoretinal Surgery, Glaucoma Surgery, Corneal Surgery, Refractive Surgery, Oculoplastic Surgery, Strabismus Surgery, Other) |
| **Splits** | train, val, test |
| **Size** | 583.0 GB |
| **Source-stated terms** | CC BY-NC-SA 4.0 |
| **Normalized terms** | `cc-by-nc-sa` |
| **Descriptive screening label** | Explicit noncommercial clause recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | HuggingFace Hub |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Standard loader included |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 2,278 | `videos` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [huggingface.co/datasets](https://huggingface.co/datasets/xioamiyh/OphNet2024) |
| Additional | 1,969 | `videos` | Untrimmed videos | `official_source_description` | [huggingface.co/datasets](https://huggingface.co/datasets/xioamiyh/OphNet2024) |
| Additional | 17,508 | `video_clips` | Trimmed operation-level clips | `official_source_description` | [huggingface.co/datasets](https://huggingface.co/datasets/xioamiyh/OphNet2024) |
| Additional | 14,674 | `video_clips` | Trimmed phase-level clips | `official_source_description` | [huggingface.co/datasets](https://huggingface.co/datasets/xioamiyh/OphNet2024) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> ~583 GB total: untrimmed ~305 GB, trimmed operations ~139 GB, trimmed phases ~139 GB, features ~26 GB. num_samples = 2,278 source videos. May require HF_TOKEN for gated access. Set HF_TOKEN in .env. GitHub: https://github.com/minghu0830/OphNet-benchmark

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download ophnet2024 --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download ophnet2024 --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('ophnet2024')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [huggingface.co/datasets](https://huggingface.co/datasets/xioamiyh/OphNet2024)

**Source-term evidence:** [huggingface.co/datasets](https://huggingface.co/datasets/xioamiyh/OphNet2024)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('ophnet2024')
samples = ds.load(data_dir, split='test')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{ophnet2024,
  title  = { OphNet2024: Ophthalmic Surgical Video Dataset },
  note   = { Hu M et al., 'OphNet: A Large-Scale Video Benchmark for Ophthalmic Surgical Workflow Understanding', ECCV 2024. arXiv:2406.07471. HuggingFace: https://huggingface.co/datasets/xioamiyh/OphNet2024 — GitHub: https://github.com/minghu0830/OphNet-benchmark },
  year   = { 2024 },
  url    = { https://huggingface.co/datasets/xioamiyh/OphNet2024 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Hu M et al., 'OphNet: A Large-Scale Video Benchmark for Ophthalmic Surgical Workflow Understanding', ECCV 2024. arXiv:2406.07471. HuggingFace: https://huggingface.co/datasets/xioamiyh/OphNet2024 — GitHub: https://github.com/minghu0830/OphNet-benchmark
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC BY-NC-SA 4.0
- **Normalized category:** `cc-by-nc-sa`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Explicit noncommercial clause recorded; check source

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [ophora](./ophora.md): Ophora-160K: Ophthalmic Surgical Video Instruction Dataset (162,185 video clip instruction pairs, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [insegcat](./insegcat.md): InSegCat: Instance Segmentation for Cataract Surgery (5,581 annotated images, `research-only`)
- [cadis](./cadis.md): CaDIS: Cataract Dataset for Image Segmentation (4,670 images, `research-only`)
- [cataract_lmm](./cataract_lmm.md): Cataract-LMM: Large-Scale Multi-Source Multi-Task Cataract Surgery Benchmark (3,000 videos, `cc-by-nc-nd`)
- [lmod_cataract_1k](./lmod_cataract_1k.md): LMOD-Cataract-1K (2,256 images, `cc-by`)
- [lmod_cataract_1k_cot](./lmod_cataract_1k_cot.md): Cataract-1K Surgical Analysis Chain-of-Thought Dataset (2,256 images, `mit`)
- [cataract1k](./cataract1k.md): Cataract-1K: Large-Scale Cataract Surgery Video Dataset (1,000 videos, `research-only`)
