---
id: retinal_corrugations_oct
title: "Outer Retinal Corrugations Imaging Dataset"
sidebar_label: retinal_corrugations_oct
description: "High-resolution swept-source OCT images and mechanical-model data for outer retinal corrugations in rhegmatogenous retinal detachment."
tags: ["oct", "cc-by", "mendeley", "segmentation", "regression", "resource-role-current-dataset", "dataset-family-retinal-corrugations-oct"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Outer Retinal Corrugations Imaging Dataset

High-resolution swept-source OCT images and mechanical-model data for outer retinal corrugations in rhegmatogenous retinal detachment.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `retinal_corrugations_oct` |
| **Full name** | Outer Retinal Corrugations Imaging Dataset |
| **First published** | 2022-09-05 |
| **Publication date precision** | day |
| **Publication date evidence** | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/bzsc7gd9p3/1) |
| **Publication date source field** | citation_publication_date (version 1) |
| **Publication date reviewed** | 2026-09-11 |
| **Primary category** | `oct` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `retinal_corrugations_oct` |
| **Contained modalities** | oct |
| **Tasks** | segmentation, regression |
| **Primary reported quantity** | 69 b scans |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.5 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Mendeley Data |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 69 | `b_scans` | Baseline swept-source OCT scans described for the current Mendeley v2 deposit The article abstract and specifications table report 69 scans from 66 patients; one methods passage reports 66 assessed scans. | `associated_publication` | [https://doi.org/10.1016/j.dib.2023.108920](https://doi.org/10.1016/j.dib.2023.108920) |
| Additional | 66 | `participants` | Patients represented by the baseline SS-OCT cohort | `associated_publication` | [https://doi.org/10.1016/j.dib.2023.108920](https://doi.org/10.1016/j.dib.2023.108920) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> The associated Data in Brief article reports 69 baseline cross-sectional SS-OCT scans from 66 patients; one methods passage reports 66 assessed scans, so the count is retained with a source-conflict flag.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download retinal_corrugations_oct --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download retinal_corrugations_oct --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('retinal_corrugations_oct')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/bzsc7gd9p3/2)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/bzsc7gd9p3/2)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{retinal_corrugations_oct,
  title  = { Outer Retinal Corrugations Imaging Dataset },
  note   = { Darabad RR et al. Outer Retinal Corrugations: Imaging Dataset and Mechanical Models. Mendeley Data, V2, 2022. doi:10.17632/bzsc7gd9p3.2 },
  year   = { 2022 },
  url    = { https://data.mendeley.com/datasets/bzsc7gd9p3/2 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Darabad RR et al. Outer Retinal Corrugations: Imaging Dataset and Mechanical Models. Mendeley Data, V2, 2022. doi:10.17632/bzsc7gd9p3.2
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
