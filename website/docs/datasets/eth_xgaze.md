---
id: eth_xgaze
title: "ETH-XGaze Extreme-Pose Gaze Estimation Dataset"
sidebar_label: eth_xgaze
description: "High-resolution multi-camera face images with calibrated gaze targets, extreme head poses, and varied illumination."
tags: ["eye_tracking", "cc-by-nc-sa", "manual", "gaze_estimation", "regression", "resource-role-current-dataset", "dataset-family-eth-xgaze"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# ETH-XGaze Extreme-Pose Gaze Estimation Dataset

High-resolution multi-camera face images with calibrated gaze targets, extreme head poses, and varied illumination.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `eth_xgaze` |
| **Full name** | ETH-XGaze Extreme-Pose Gaze Estimation Dataset |
| **Primary category** | `eye_tracking` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `eth_xgaze` |
| **Contained modalities** | eye_tracking |
| **Tasks** | gaze_estimation, regression |
| **Primary reported quantity** | 1,083,492 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 130.0 GB |
| **Source-stated terms** | CC BY-NC-SA 4.0 with additional dataset conditions |
| **Normalized terms** | `cc-by-nc-sa` |
| **Descriptive screening label** | Explicit noncommercial clause recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `controlled_or_manual` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `manual_access_blocked` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 1,083,492 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [ait.ethz.ch/xgaze](https://ait.ethz.ch/xgaze) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Contains 1,083,492 images from 110 participants. The official page offers approximately 130 GB 224-pixel face patches, 497 GB 448-pixel patches, or about 7 TB of raw images on request. The linked completed license adds conditions to CC BY-NC-SA 4.0.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# This route requires upstream human action; no transfer starts.
eyehub download eth_xgaze --data-dir ./data --dry-run --json
# Follow the official instructions shown by preflight.
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('eth_xgaze')
print(preflight_dataset(ds, './data'))  # returns manual_access_blocked
```

  </TabItem>
</Tabs>

**Upstream page:** [ait.ethz.ch/xgaze](https://ait.ethz.ch/xgaze)

**Source-term evidence:** [ait.ethz.ch/xgaze](https://ait.ethz.ch/xgaze)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{eth_xgaze,
  title  = { ETH-XGaze Extreme-Pose Gaze Estimation Dataset },
  note   = { Zhang X, Park S, Beeler T, Bradley D, Tang S, Hilliges O. ETH-XGaze: A Large Scale Dataset for Gaze Estimation under Extreme Head Pose and Gaze Variation. ECCV. 2020 },
  year   = { 2020 },
  url    = { https://ait.ethz.ch/xgaze },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Zhang X, Park S, Beeler T, Bradley D, Tang S, Hilliges O. ETH-XGaze: A Large Scale Dataset for Gaze Estimation under Extreme Head Pose and Gaze Variation. ECCV. 2020.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC BY-NC-SA 4.0 with additional dataset conditions
- **Normalized category:** `cc-by-nc-sa`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Explicit noncommercial clause recorded; check source

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [teyed](./teyed.md): TEyeD Real-World Eye-Tracking Dataset (20,666,096 images, `unknown`)
- [gaze_capture](./gaze_capture.md): GazeCapture Mobile Eye-Tracking Dataset (2,445,504 frames, `unknown`)
- [mpii_gaze](./mpii_gaze.md): MPIIGaze Appearance-Based Gaze Estimation Dataset (213,659 images, `cc-by-nc-sa`)
- [gaze360](./gaze360.md): Gaze360 Physically Unconstrained Gaze Dataset (172,000 frames, `unknown`)
- [lpw](./lpw.md): LPW Labelled Pupils in the Wild (130,856 frames, `research-only`)
- [glaucoma_eye_movements](./glaucoma_eye_movements.md): Eye Movements of Glaucoma Patients with Asymmetrical Visual Field Loss (270 participants, `cc-by`)
- [mendeley_sub_cone_visual_resolution_by_active](./mendeley_sub_cone_visual_resolution_by_active.md): Data from: Sub-cone visual resolution by active, adaptive sampling in the human foveola (16 participants, `cc-by`)
- [asd_eye_tracking](./asd_eye_tracking.md): Autism Spectrum Disorder Eye-Tracking Dataset (Not reported, `cc-by`)
