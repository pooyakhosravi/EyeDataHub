---
id: intraretinal_cystoid_fluid
title: "Intraretinal Cystoid Fluid OCT Segmentation Dataset"
sidebar_label: intraretinal_cystoid_fluid
description: "OCT images for intraretinal cystoid-fluid segmentation, partly derived from public OCT DME sources with expert-selected masks."
tags: ["oct", "cc-by-nc-sa", "kaggle", "segmentation", "resource-role-derivative-dataset", "dataset-family-intraretinal-cystoid-fluid", "documented-relationship", "relationship-derived_from"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Intraretinal Cystoid Fluid OCT Segmentation Dataset

OCT images for intraretinal cystoid-fluid segmentation, partly derived from public OCT DME sources with expert-selected masks.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `intraretinal_cystoid_fluid` |
| **Full name** | Intraretinal Cystoid Fluid OCT Segmentation Dataset |
| **First published** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Primary category** | `oct` |
| **Resource role** | `derivative_dataset` |
| **Dataset family** | `intraretinal_cystoid_fluid` |
| **Contained modalities** | oct |
| **Tasks** | segmentation |
| **Primary reported quantity** | 1,460 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 1.0 GB |
| **Source-stated terms** | CC BY-NC-SA 4.0 |
| **Normalized terms** | `cc-by-nc-sa` |
| **Descriptive screening label** | Explicit noncommercial clause recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Kaggle |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 1,460 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [kaggle.com/datasets](https://www.kaggle.com/datasets/zeeshanahmed13/intraretinal-cystoid-fluid) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Partly derived from existing OCT datasets; retain as segmentation-mask resource.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- This record is `derived from` [kermany_oct](./kermany_oct.md): The source states that 1,000 training images were selected from the Kermany Retinal OCT Images DME class; 200 test images were collected separately. ([evidence](https://www.kaggle.com/datasets/zeeshanahmed13/intraretinal-cystoid-fluid))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download intraretinal_cystoid_fluid --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download intraretinal_cystoid_fluid --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('intraretinal_cystoid_fluid')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [kaggle.com/datasets](https://www.kaggle.com/datasets/zeeshanahmed13/intraretinal-cystoid-fluid)

**Source-term evidence:** [kaggle.com/datasets](https://www.kaggle.com/datasets/zeeshanahmed13/intraretinal-cystoid-fluid)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{intraretinal_cystoid_fluid,
  title  = { Intraretinal Cystoid Fluid OCT Segmentation Dataset },
  note   = { Intraretinal Cystoid Fluid dataset. Kaggle, accessed 2026-07 },
  year   = { 2026 },
  url    = { https://www.kaggle.com/datasets/zeeshanahmed13/intraretinal-cystoid-fluid },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Intraretinal Cystoid Fluid dataset. Kaggle, accessed 2026-07.
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

- [syn_oct](./syn_oct.md): SYN-OCT Synthetic Glaucoma OCT Dataset (200,000 images, `cc-by`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (103,959 images, `mit`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [kermany_oct](./kermany_oct.md): Kermany OCT 2018: Retinal OCT Image Classification (84,484 images, `cc-by`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [harvard_fairvision](./harvard_fairvision.md): Harvard-FairVision (AMD + DR + Glaucoma, paired SLO + OCT) (30,000 participants, `cc-by-nc-nd`)
- [mario](./mario.md): MARIO: AMD-Progression Longitudinal OCT (MICCAI 2024) (30,000 images, `cc-by`)
- [mmrdr](./mmrdr.md): MMRDR: Multi-Modal Retinal Diabetic Retinopathy Dataset (24,460 images, `cc-by`)
