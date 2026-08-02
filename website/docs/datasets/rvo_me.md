---
id: rvo_me
title: "RVO-ME: Retinal Vein Occlusion Macular Edema OCT Dataset"
sidebar_label: rvo_me
description: "3,012 OCT B-scans from 146 eyes / 130 patients with retinal vein occlusion. Dual-task labels: fluid segmentation + retinal-layer segmentation. Detection of macular lesions."
tags: ["oct", "cc-by", "figshare", "segmentation", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# RVO-ME: Retinal Vein Occlusion Macular Edema OCT Dataset

3,012 OCT B-scans from 146 eyes / 130 patients with retinal vein occlusion. Dual-task labels: fluid segmentation + retinal-layer segmentation. Detection of macular lesions.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `rvo_me` |
| **Full name** | RVO-ME: Retinal Vein Occlusion Macular Edema OCT Dataset |
| **Primary category** | `oct` |
| **Contained modalities** | oct |
| **Tasks** | segmentation, classification |
| **Primary reported quantity** | 3,012 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 2.0 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Figshare |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `end_to_end_tested` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 3,012 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [https://doi.org/10.6084/m9.figshare.29804435.v1](https://doi.org/10.6084/m9.figshare.29804435.v1) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Sci Data 2026 release; verify source license before reuse.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download rvo_me --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download rvo_me --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('rvo_me')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.6084/m9.figshare.29804435.v1](https://doi.org/10.6084/m9.figshare.29804435.v1)

**Source-term evidence:** [https://doi.org/10.6084/m9.figshare.29804435.v1](https://doi.org/10.6084/m9.figshare.29804435.v1)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{rvo_me,
  title  = { RVO-ME: Retinal Vein Occlusion Macular Edema OCT Dataset },
  note   = { Xiong F, et al., 'RVO-ME: A dual-task OCT dataset for segmentation and detection of macular lesions in retinal vein occlusion', Scientific Data 2026 },
  year   = { 2026 },
  url    = { https://doi.org/10.6084/m9.figshare.29804435.v1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Xiong F, et al., 'RVO-ME: A dual-task OCT dataset for segmentation and detection of macular lesions in retinal vein occlusion', Scientific Data 2026.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC BY 4.0
- **Normalized category:** `cc-by`
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
