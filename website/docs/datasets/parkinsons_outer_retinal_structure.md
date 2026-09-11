---
id: parkinsons_outer_retinal_structure
title: "Parkinson Disease Outer Retinal Structure and Function Dataset"
sidebar_label: parkinsons_outer_retinal_structure
description: "Retinal structure, electrophysiology, and visual-perception measurements from Parkinson disease and comparison participants."
tags: ["oct", "cc-by", "figshare", "measurement", "classification", "resource-role-current-dataset", "dataset-family-parkinsons-outer-retinal-structure"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Parkinson Disease Outer Retinal Structure and Function Dataset

Retinal structure, electrophysiology, and visual-perception measurements from Parkinson disease and comparison participants.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `parkinsons_outer_retinal_structure` |
| **Full name** | Parkinson Disease Outer Retinal Structure and Function Dataset |
| **First published** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Primary category** | `oct` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `parkinsons_outer_retinal_structure` |
| **Contained modalities** | oct |
| **Tasks** | measurement, classification |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Figshare |
| **Availability** | `available` (checked 2026-08-02) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

No reproducible primary item count was exposed for the cataloged source version.

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download parkinsons_outer_retinal_structure --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download parkinsons_outer_retinal_structure --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('parkinsons_outer_retinal_structure')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.26188/24138420.v2](https://doi.org/10.26188/24138420.v2)

**Source-term evidence:** [https://doi.org/10.26188/24138420.v2](https://doi.org/10.26188/24138420.v2)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{parkinsons_outer_retinal_structure,
  title  = { Parkinson Disease Outer Retinal Structure and Function Dataset },
  note   = { Repository dataset record. 10.26188/24138420.v2 },
  url    = { https://doi.org/10.26188/24138420.v2 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Repository dataset record. 10.26188/24138420.v2.
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
