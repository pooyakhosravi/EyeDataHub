---
id: amd_dme_3d_oct
title: "Comprehensive 3D OCT Dataset for AMD and DME"
sidebar_label: amd_dme_3d_oct
description: "Swept-source OCT volumes for AMD and DME with three-dimensional pigment epithelial detachment and intraretinal-fluid masks."
tags: ["oct", "cc-by", "figshare", "segmentation", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Comprehensive 3D OCT Dataset for AMD and DME

Swept-source OCT volumes for AMD and DME with three-dimensional pigment epithelial detachment and intraretinal-fluid masks.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `amd_dme_3d_oct` |
| **Full name** | Comprehensive 3D OCT Dataset for AMD and DME |
| **Primary category** | `oct` |
| **Contained modalities** | oct |
| **Tasks** | segmentation, classification |
| **Primary reported quantity** | 224 volumes |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 19.65 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
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
| Primary | 224 | `volumes` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [https://doi.org/10.6084/m9.figshare.30582035.v1](https://doi.org/10.6084/m9.figshare.30582035.v1) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> The release contains 122 AMD and 102 DME volumes. Of these, 104 volumes are labeled (62 AMD and 42 DME) and 120 are unlabeled.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download amd_dme_3d_oct --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download amd_dme_3d_oct --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('amd_dme_3d_oct')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.6084/m9.figshare.30582035.v1](https://doi.org/10.6084/m9.figshare.30582035.v1)

**Source-term evidence:** [https://doi.org/10.6084/m9.figshare.30582035.v1](https://doi.org/10.6084/m9.figshare.30582035.v1)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{amd_dme_3d_oct,
  title  = { Comprehensive 3D OCT Dataset for AMD and DME },
  note   = { Huang W, Qin L, Xu M, et al. Comprehensive 3D Optical Coherence Tomography Dataset for AMD and DME: Facilitating Deep-Learning-Based 3D Segmentation. Scientific Data. 2026;13:224. doi:10.1038/s41597-025-06497-1 },
  year   = { 2026 },
  url    = { https://doi.org/10.6084/m9.figshare.30582035.v1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Huang W, Qin L, Xu M, et al. Comprehensive 3D Optical Coherence Tomography Dataset for AMD and DME: Facilitating Deep-Learning-Based 3D Segmentation. Scientific Data. 2026;13:224. doi:10.1038/s41597-025-06497-1
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
