---
id: as_oct_keratitis
title: "AS-OCT Keratitis Segmentation Dataset"
sidebar_label: as_oct_keratitis
description: "1,168 anterior-segment OCT images of keratitis with per-pixel lesion, cornea, and iris segmentation labels. Enables 3D reconstruction from B-scan stacks."
tags: ["oct", "cc0", "figshare", "segmentation", "resource-role-current-dataset", "dataset-family-as-oct-keratitis"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# AS-OCT Keratitis Segmentation Dataset

1,168 anterior-segment OCT images of keratitis with per-pixel lesion, cornea, and iris segmentation labels. Enables 3D reconstruction from B-scan stacks.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `as_oct_keratitis` |
| **Full name** | AS-OCT Keratitis Segmentation Dataset |
| **Publication date** | 2024-06-11 |
| **Date basis** | Initial dataset release |
| **Publication date precision** | day |
| **Publication date evidence** | [api.figshare.com/v2](https://api.figshare.com/v2/collections/7036994/versions/1) |
| **Publication date source field** | collection.timeline.firstOnline (Figshare collection version 1) |
| **Publication date reviewed** | 2026-09-11 |
| **Date notes** | Official collection v1 identifies the initial public collection release. |
| **Primary category** | `oct` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `as_oct_keratitis` |
| **Contained modalities** | oct |
| **Tasks** | segmentation |
| **Primary reported quantity** | 1,168 images |
| **Classes** | 4 (background, lesion, cornea, iris) |
| **Splits** | all |
| **Size** | 1.5 GB |
| **Source-stated terms** | CC0 1.0 |
| **Normalized terms** | `cc0` |
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
| Primary | 1,168 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [https://doi.org/10.6084/m9.figshare.c.7036994.v1](https://doi.org/10.6084/m9.figshare.c.7036994.v1) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Adds corneal infectious disease + 3D AS-OCT use case.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download as_oct_keratitis --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download as_oct_keratitis --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('as_oct_keratitis')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.6084/m9.figshare.c.7036994.v1](https://doi.org/10.6084/m9.figshare.c.7036994.v1)

**Source-term evidence:** [https://doi.org/10.6084/m9.figshare.c.7036994.v1](https://doi.org/10.6084/m9.figshare.c.7036994.v1)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{as_oct_keratitis,
  title  = { AS-OCT Keratitis Segmentation Dataset },
  note   = { Sun Y, et al., 'An AS-OCT image dataset for deep learning-enabled segmentation and 3D reconstruction for keratitis', Scientific Data 2024 },
  year   = { 2024 },
  url    = { https://doi.org/10.6084/m9.figshare.c.7036994.v1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Sun Y, et al., 'An AS-OCT image dataset for deep learning-enabled segmentation and 3D reconstruction for keratitis', Scientific Data 2024.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC0 1.0
- **Normalized category:** `cc0`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Standard label without an explicit NC clause; not a permission finding

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
