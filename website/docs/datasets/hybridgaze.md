---
id: hybridgaze
title: "HybridGaze Dataset"
sidebar_label: hybridgaze
description: "Synchronized human eye-tracking, webcam eye images, facial landmarks, and gaze annotations."
tags: ["eye_tracking", "unknown", "kaggle", "gaze_estimation", "resource-role-current-dataset", "dataset-family-hybridgaze"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# HybridGaze Dataset

Synchronized human eye-tracking, webcam eye images, facial landmarks, and gaze annotations.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `hybridgaze` |
| **Full name** | HybridGaze Dataset |
| **First published** | 2025-10-13 |
| **Publication date precision** | day |
| **Publication date evidence** | [kaggle.com/api](https://www.kaggle.com/api/v1/datasets/view/michachwesiuk/hybridgaze) |
| **Publication date source field** | versions[0].creationDate (version 1, Initial release) |
| **Publication date reviewed** | 2026-09-11 |
| **Primary category** | `eye_tracking` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `hybridgaze` |
| **Contained modalities** | eye_tracking |
| **Tasks** | gaze_estimation |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | GNU Free Documentation License 1.3 |
| **Normalized terms** | `unknown` |
| **Descriptive screening label** | Unknown or unclear; do not assume permission |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Kaggle |
| **Availability** | `available` (checked 2026-08-02) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

No reproducible primary item count was exposed for the cataloged source version.

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Source exposes one HDF5 gaze-estimation dataset; no participant/frame count is stated.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download hybridgaze --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download hybridgaze --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('hybridgaze')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [kaggle.com/datasets](https://www.kaggle.com/datasets/michachwesiuk/hybridgaze)

**Source-term evidence:** [kaggle.com/datasets](https://www.kaggle.com/datasets/michachwesiuk/hybridgaze)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{hybridgaze,
  title  = { HybridGaze Dataset },
  note   = { Repository dataset record. michachwesiuk/hybridgaze },
  url    = { https://www.kaggle.com/datasets/michachwesiuk/hybridgaze },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Repository dataset record. michachwesiuk/hybridgaze.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** GNU Free Documentation License 1.3
- **Normalized category:** `unknown`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Unknown or unclear; do not assume permission

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [teyed](./teyed.md): TEyeD Real-World Eye-Tracking Dataset (20,666,096 images, `unknown`)
- [gaze_capture](./gaze_capture.md): GazeCapture Mobile Eye-Tracking Dataset (2,445,504 frames, `unknown`)
- [eth_xgaze](./eth_xgaze.md): ETH-XGaze Extreme-Pose Gaze Estimation Dataset (1,083,492 images, `cc-by-nc-sa`)
- [mpii_gaze](./mpii_gaze.md): MPIIGaze Appearance-Based Gaze Estimation Dataset (213,659 images, `cc-by-nc-sa`)
- [gaze360](./gaze360.md): Gaze360 Physically Unconstrained Gaze Dataset (172,000 frames, `unknown`)
- [lpw](./lpw.md): LPW Labelled Pupils in the Wild (130,856 frames, `research-only`)
- [glaucoma_eye_movements](./glaucoma_eye_movements.md): Eye Movements of Glaucoma Patients with Asymmetrical Visual Field Loss (270 participants, `cc-by`)
- [mendeley_sub_cone_visual_resolution_by_active](./mendeley_sub_cone_visual_resolution_by_active.md): Data from: Sub-cone visual resolution by active, adaptive sampling in the human foveola (16 participants, `cc-by`)
