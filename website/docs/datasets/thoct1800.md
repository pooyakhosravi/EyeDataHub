---
id: thoct1800
title: "THOCT1800 Retinal OCT Dataset"
sidebar_label: thoct1800
description: "A collection of 1,800 preprocessed retinal OCT B-scans, with 600 images each for AMD, diabetic macular edema, and normal retina."
tags: ["oct", "research-only", "github", "classification", "resource-role-current-dataset", "dataset-family-thoct1800"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# THOCT1800 Retinal OCT Dataset

A collection of 1,800 preprocessed retinal OCT B-scans, with 600 images each for AMD, diabetic macular edema, and normal retina.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `thoct1800` |
| **Full name** | THOCT1800 Retinal OCT Dataset |
| **First published** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Primary category** | `oct` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `thoct1800` |
| **Contained modalities** | oct |
| **Tasks** | classification |
| **Primary reported quantity** | 1,800 images |
| **Classes** | 3 (amd, dme, normal) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | Research only: research and educational use |
| **Normalized terms** | `research-only` |
| **Descriptive screening label** | Research or challenge restriction recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | GitHub |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `end_to_end_tested` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 1,800 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [github.com/SJD095](https://github.com/SJD095/OCT-Segmentation) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> The official repository permits research and educational use and asks users to cite the project. No standard license file is present.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download thoct1800 --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download thoct1800 --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('thoct1800')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [github.com/SJD095](https://github.com/SJD095/OCT-Segmentation)

**Source-term evidence:** [github.com/SJD095](https://github.com/SJD095/OCT-Segmentation)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{thoct1800,
  title  = { THOCT1800 Retinal OCT Dataset },
  note   = { THOCT1800 retinal OCT image dataset. OCT-Segmentation project. GitHub },
  url    = { https://github.com/SJD095/OCT-Segmentation },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
THOCT1800 retinal OCT image dataset. OCT-Segmentation project. GitHub.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Research only: research and educational use
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
