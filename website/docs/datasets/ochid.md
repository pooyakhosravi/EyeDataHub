---
id: ochid
title: "OCHID: OCT Choroidal Image Dataset"
sidebar_label: ochid
description: "A collection of 640 retinal OCT images with expert choroidal region annotations for choroid segmentation."
tags: ["oct", "research-only", "manual", "segmentation", "resource-role-current-dataset", "dataset-family-ochid"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# OCHID: OCT Choroidal Image Dataset

A collection of 640 retinal OCT images with expert choroidal region annotations for choroid segmentation.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `ochid` |
| **Full name** | OCHID: OCT Choroidal Image Dataset |
| **Primary category** | `oct` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `ochid` |
| **Contained modalities** | oct |
| **Tasks** | segmentation |
| **Primary reported quantity** | 640 images |
| **Classes** | 2 (background, choroid) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | Research only: academic research use by request |
| **Normalized terms** | `research-only` |
| **Descriptive screening label** | Research or challenge restriction recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `author_contact` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `manual_access_blocked` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 640 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [imed.nimte.ac.cn/OCHID.html](https://imed.nimte.ac.cn/OCHID.html) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> The official project page asks academic users to request the dataset by email. It does not provide a standard license.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# This route requires upstream human action; no transfer starts.
eyehub download ochid --data-dir ./data --dry-run --json
# Follow the official instructions shown by preflight.
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('ochid')
print(preflight_dataset(ds, './data'))  # returns manual_access_blocked
```

  </TabItem>
</Tabs>

**Upstream page:** [imed.nimte.ac.cn/OCHID.html](https://imed.nimte.ac.cn/OCHID.html)

**Source-term evidence:** [imed.nimte.ac.cn/OCHID.html](https://imed.nimte.ac.cn/OCHID.html)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{ochid,
  title  = { OCHID: OCT Choroidal Image Dataset },
  note   = { Yan Q, Gu Y, Zhao J, et al. Automatic choroid layer segmentation in OCT images via context efficient adaptive network. Appl Intell. 2023;53:5554-5566. doi:10.1007/s10489-022-03723-w },
  year   = { 2023 },
  url    = { https://imed.nimte.ac.cn/OCHID.html },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Yan Q, Gu Y, Zhao J, et al. Automatic choroid layer segmentation in OCT images via context efficient adaptive network. Appl Intell. 2023;53:5554-5566. doi:10.1007/s10489-022-03723-w
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Research only: academic research use by request
- **Normalized category:** `research-only`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Research or challenge restriction recorded; check source

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
