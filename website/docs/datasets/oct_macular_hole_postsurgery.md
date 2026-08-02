---
id: oct_macular_hole_postsurgery
title: "HD-OCT of Macular Hole Before and After Surgery"
sidebar_label: oct_macular_hole_postsurgery
description: "HD-OCT scans and clinical outcome variables for macular-hole visual-improvement prediction after surgery."
tags: ["oct", "unknown", "kaggle", "regression", "classification", "resource-role-current-dataset", "dataset-family-oct-macular-hole-postsurgery"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# HD-OCT of Macular Hole Before and After Surgery

HD-OCT scans and clinical outcome variables for macular-hole visual-improvement prediction after surgery.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `oct_macular_hole_postsurgery` |
| **Full name** | HD-OCT of Macular Hole Before and After Surgery |
| **Primary category** | `oct` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `oct_macular_hole_postsurgery` |
| **Contained modalities** | oct |
| **Tasks** | regression, classification |
| **Primary reported quantity** | 2,658 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 1.0 GB |
| **Source-stated terms** | LGPL-3.0 |
| **Normalized terms** | `unknown` |
| **Descriptive screening label** | Unknown or unclear; do not assume permission |
| **Terms scope** | `unknown` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Kaggle |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 2,658 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [kaggle.com/datasets](https://www.kaggle.com/datasets/mathieugodbout/oct-postsurgery-visual-improvement) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download oct_macular_hole_postsurgery --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download oct_macular_hole_postsurgery --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('oct_macular_hole_postsurgery')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [kaggle.com/datasets](https://www.kaggle.com/datasets/mathieugodbout/oct-postsurgery-visual-improvement)

**Source-term evidence:** [kaggle.com/datasets](https://www.kaggle.com/datasets/mathieugodbout/oct-postsurgery-visual-improvement)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{oct_macular_hole_postsurgery,
  title  = { HD-OCT of Macular Hole Before and After Surgery },
  note   = { HD-OCT of macular hole, pre/postoperative. Kaggle, accessed 2026-07 },
  year   = { 2026 },
  url    = { https://www.kaggle.com/datasets/mathieugodbout/oct-postsurgery-visual-improvement },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
HD-OCT of macular hole, pre/postoperative. Kaggle, accessed 2026-07.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** LGPL-3.0
- **Normalized category:** `unknown`
- **Apparent scope:** `unknown`
- **Descriptive screening label:** Unknown or unclear; do not assume permission

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [syn_oct](./syn_oct.md): SYN-OCT Synthetic Glaucoma OCT Dataset (200,000 images, `cc-by`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (103,959 images, `mit`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [kermany_oct](./kermany_oct.md): Kermany OCT 2018: Retinal OCT Image Classification (84,484 images, `cc-by`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [harvard_fairvision](./harvard_fairvision.md): Harvard-FairVision (AMD + DR + Glaucoma, paired SLO + OCT) (30,000 participants, `cc-by-nc-nd`)
- [mario](./mario.md): MARIO: AMD-Progression Longitudinal OCT (MICCAI 2024) (30,000 images, `cc-by`)
- [mmrdr](./mmrdr.md): MMRDR: Multi-Modal Retinal Diabetic Retinopathy Dataset (24,460 images, `cc-by`)
