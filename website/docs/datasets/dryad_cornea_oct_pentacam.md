---
id: dryad_cornea_oct_pentacam
title: "Corneal OCT and Pentacam Tomography Dataset"
sidebar_label: dryad_cornea_oct_pentacam
description: "Right-eye corneal OCT and rotating Scheimpflug tomography data with MATLAB code for automatic corneal-layer segmentation."
tags: ["multimodal", "oct", "corneal_topography", "cc0", "dryad", "segmentation", "measurement", "registration"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Corneal OCT and Pentacam Tomography Dataset

Right-eye corneal OCT and rotating Scheimpflug tomography data with MATLAB code for automatic corneal-layer segmentation.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_cornea_oct_pentacam` |
| **Full name** | Corneal OCT and Pentacam Tomography Dataset |
| **Primary category** | `multimodal` |
| **Contained modalities** | oct, corneal_topography |
| **Tasks** | segmentation, measurement, registration |
| **Primary reported quantity** | 52 participants |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.383898834 GB |
| **Source-stated terms** | CC0 1.0 |
| **Normalized terms** | `cc0` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Dryad |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `end_to_end_tested` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 52 | `participants` | Participant directories represented in the corneal OCT component of Dryad version 5 | `current_deposit_file_listing` | [https://doi.org/10.5061/dryad.tht76hf0c](https://doi.org/10.5061/dryad.tht76hf0c) |
| Additional | 208 | `images` | Corneal OCT TIFF files in Dryad version 5 Four TIFF files occur in each of 52 participant directories. | `current_deposit_file_listing` | [https://doi.org/10.5061/dryad.tht76hf0c](https://doi.org/10.5061/dryad.tht76hf0c) |
| Additional | 102 | `records` | Pentacam CSV tomography matrices in Dryad version 5 | `current_deposit_file_listing` | [https://doi.org/10.5061/dryad.tht76hf0c](https://doi.org/10.5061/dryad.tht76hf0c) |
| Additional | 1 | `deposited_files` | OCT_.zip in Dryad version 5 | `current_deposit_file_listing` | [https://doi.org/10.5061/dryad.tht76hf0c](https://doi.org/10.5061/dryad.tht76hf0c) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> The current version contains right-eye data from 52 participant directories, with 208 corneal OCT TIFF files and 102 Pentacam CSV files. Dryad file downloads require a user-supplied API token; EyeDataHub can also obtain a fresh token from locally configured Dryad client credentials.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_cornea_oct_pentacam --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dryad_cornea_oct_pentacam --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_cornea_oct_pentacam')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.tht76hf0c](https://doi.org/10.5061/dryad.tht76hf0c)

**Source-term evidence:** [https://doi.org/10.5061/dryad.tht76hf0c](https://doi.org/10.5061/dryad.tht76hf0c)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_cornea_oct_pentacam,
  title  = { Corneal OCT and Pentacam Tomography Dataset },
  note   = { Ran Z. Dataset for RSOS-211108. Dryad. 2021. doi:10.5061/dryad.tht76hf0c },
  year   = { 2021 },
  url    = { https://doi.org/10.5061/dryad.tht76hf0c },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Ran Z. Dataset for RSOS-211108. Dryad. 2021. doi:10.5061/dryad.tht76hf0c
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
