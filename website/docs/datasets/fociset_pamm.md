---
id: fociset_pamm
title: "FociSet PAMM OCT Lesion Dataset"
sidebar_label: fociset_pamm
description: "SD-OCT B-scans with bounding-box and polygon annotations for paracentral acute middle maculopathy lesions."
tags: ["oct", "cc-by", "mendeley", "detection", "segmentation", "resource-role-current-dataset", "dataset-family-fociset-pamm"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# FociSet PAMM OCT Lesion Dataset

SD-OCT B-scans with bounding-box and polygon annotations for paracentral acute middle maculopathy lesions.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `fociset_pamm` |
| **Full name** | FociSet PAMM OCT Lesion Dataset |
| **First published** | 2024-06-17 |
| **Publication date precision** | day |
| **Publication date evidence** | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/mkwxn7rjpm/1) |
| **Publication date source field** | citation_publication_date (version 1) |
| **Publication date reviewed** | 2026-09-11 |
| **Primary category** | `oct` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `fociset_pamm` |
| **Contained modalities** | oct |
| **Tasks** | detection, segmentation |
| **Primary reported quantity** | 133 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
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
| Primary | 133 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/mkwxn7rjpm/2) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Contains 133 OCT images with PAMM foci annotated in YOLO bounding-box and JSON polygon formats.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download fociset_pamm --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download fociset_pamm --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('fociset_pamm')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/mkwxn7rjpm/2)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/mkwxn7rjpm/2)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{fociset_pamm,
  title  = { FociSet PAMM OCT Lesion Dataset },
  note   = { FociSet: A dataset for detection and segmentation of paracentral acute middle maculopathy lesions in OCT images. Data in Brief. 2024;57:111121. doi:10.1016/j.dib.2024.111121 },
  year   = { 2024 },
  url    = { https://data.mendeley.com/datasets/mkwxn7rjpm/2 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
FociSet: A dataset for detection and segmentation of paracentral acute middle maculopathy lesions in OCT images. Data in Brief. 2024;57:111121. doi:10.1016/j.dib.2024.111121
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
