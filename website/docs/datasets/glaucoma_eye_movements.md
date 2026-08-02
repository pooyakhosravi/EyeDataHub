---
id: glaucoma_eye_movements
title: "Eye Movements of Glaucoma Patients with Asymmetrical Visual Field Loss"
sidebar_label: glaucoma_eye_movements
description: "Raw and processed eye-tracking data from glaucoma patients with asymmetrical visual-field loss during free viewing."
tags: ["eye_tracking", "cc-by", "zenodo", "regression", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Eye Movements of Glaucoma Patients with Asymmetrical Visual Field Loss

Raw and processed eye-tracking data from glaucoma patients with asymmetrical visual-field loss during free viewing.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `glaucoma_eye_movements` |
| **Full name** | Eye Movements of Glaucoma Patients with Asymmetrical Visual Field Loss |
| **Primary category** | `eye_tracking` |
| **Contained modalities** | eye_tracking |
| **Tasks** | regression, classification |
| **Primary reported quantity** | 270 participants |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.1 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Zenodo |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 270 | `participants` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [zenodo.org/records](https://zenodo.org/records/7761477) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download glaucoma_eye_movements --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download glaucoma_eye_movements --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('glaucoma_eye_movements')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [zenodo.org/records](https://zenodo.org/records/7761477)

**Source-term evidence:** [zenodo.org/records](https://zenodo.org/records/7761477)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{glaucoma_eye_movements,
  title  = { Eye Movements of Glaucoma Patients with Asymmetrical Visual Field Loss },
  note   = { Data on eye movements of glaucoma patients with asymmetrical visual field loss during free viewing. Zenodo, 2023. doi:10.5281/zenodo.7761477 },
  year   = { 2023 },
  url    = { https://zenodo.org/records/7761477 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Data on eye movements of glaucoma patients with asymmetrical visual field loss during free viewing. Zenodo, 2023. doi:10.5281/zenodo.7761477
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

- [teyed](./teyed.md): TEyeD Real-World Eye-Tracking Dataset (20,666,096 images, `unknown`)
- [gaze_capture](./gaze_capture.md): GazeCapture Mobile Eye-Tracking Dataset (2,445,504 frames, `unknown`)
- [eth_xgaze](./eth_xgaze.md): ETH-XGaze Extreme-Pose Gaze Estimation Dataset (1,083,492 images, `cc-by-nc-sa`)
- [mpii_gaze](./mpii_gaze.md): MPIIGaze Appearance-Based Gaze Estimation Dataset (213,659 images, `cc-by-nc-sa`)
- [gaze360](./gaze360.md): Gaze360 Physically Unconstrained Gaze Dataset (172,000 frames, `unknown`)
- [lpw](./lpw.md): LPW Labelled Pupils in the Wild (130,856 frames, `research-only`)
- [dryad_biocular_eye_tracking](./dryad_biocular_eye_tracking.md): Bi-Ocular Vertebrate Eye-Tracking Dataset (Not reported, `cc0`)
- [dryad_eye_head_visual_selection](./dryad_eye_head_visual_selection.md): Eye and Head Visual Selection Dataset (Not reported, `cc0`)
