---
id: gaze_capture
title: "GazeCapture Mobile Eye-Tracking Dataset"
sidebar_label: gaze_capture
description: "Crowdsourced iPhone and iPad face videos with screen-fixation coordinates for appearance-based mobile gaze estimation."
tags: ["eye_tracking", "unknown", "manual", "gaze_estimation", "regression", "resource-role-current-dataset", "dataset-family-gaze-capture"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# GazeCapture Mobile Eye-Tracking Dataset

Crowdsourced iPhone and iPad face videos with screen-fixation coordinates for appearance-based mobile gaze estimation.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `gaze_capture` |
| **Full name** | GazeCapture Mobile Eye-Tracking Dataset |
| **Publication date** | 2017-03 |
| **Date basis** | Initial dataset release |
| **Publication date precision** | month |
| **Publication date evidence** | [github.com/CSAILVision](https://github.com/CSAILVision/GazeCapture) |
| **Publication date source field** | Official GitHub README: History |
| **Publication date reviewed** | 2026-09-11 |
| **Date notes** | The official project README says the original code, dataset, and models were released in March 2017; no day is given. |
| **Primary category** | `eye_tracking` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `gaze_capture` |
| **Contained modalities** | eye_tracking |
| **Tasks** | gaze_estimation, regression |
| **Primary reported quantity** | 2,445,504 frames |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | Unknown; registration required and source terms must be checked |
| **Normalized terms** | `unknown` |
| **Descriptive screening label** | Unknown or unclear; do not assume permission |
| **Terms scope** | `unknown` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `guided_instructions_only` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 2,445,504 | `frames` | Labeled mobile-camera frames | `official_source_description` | [gazecapture.csail.mit.edu](https://gazecapture.csail.mit.edu/) |
| Additional | 1,474 | `participants` | Crowdsourced participants | `official_source_description` | [gazecapture.csail.mit.edu](https://gazecapture.csail.mit.edu/) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> The primary paper reports 2,445,504 frames with fixation locations from 1,474 participants. The official site requires account registration; verify the current agreement before reuse.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download gaze_capture --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download gaze_capture --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('gaze_capture')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [gazecapture.csail.mit.edu/dataset.php](https://gazecapture.csail.mit.edu/dataset.php)

**Source-term evidence:** [gazecapture.csail.mit.edu/dataset.php](https://gazecapture.csail.mit.edu/dataset.php)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{gaze_capture,
  title  = { GazeCapture Mobile Eye-Tracking Dataset },
  note   = { Krafka K, Khosla A, Kellnhofer P, et al. Eye Tracking for Everyone. CVPR. 2016:2176-2184. arXiv:1606.05814 },
  year   = { 2016 },
  url    = { https://gazecapture.csail.mit.edu/dataset.php },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Krafka K, Khosla A, Kellnhofer P, et al. Eye Tracking for Everyone. CVPR. 2016:2176-2184. arXiv:1606.05814
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Unknown; registration required and source terms must be checked
- **Normalized category:** `unknown`
- **Apparent scope:** `unknown`
- **Descriptive screening label:** Unknown or unclear; do not assume permission

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [teyed](./teyed.md): TEyeD Real-World Eye-Tracking Dataset (20,666,096 images, `unknown`)
- [eth_xgaze](./eth_xgaze.md): ETH-XGaze Extreme-Pose Gaze Estimation Dataset (1,083,492 images, `cc-by-nc-sa`)
- [mpii_gaze](./mpii_gaze.md): MPIIGaze Appearance-Based Gaze Estimation Dataset (213,659 images, `cc-by-nc-sa`)
- [gaze360](./gaze360.md): Gaze360 Physically Unconstrained Gaze Dataset (172,000 frames, `unknown`)
- [lpw](./lpw.md): LPW Labelled Pupils in the Wild (130,856 frames, `research-only`)
- [glaucoma_eye_movements](./glaucoma_eye_movements.md): Eye Movements of Glaucoma Patients with Asymmetrical Visual Field Loss (270 participants, `cc-by`)
- [mendeley_sub_cone_visual_resolution_by_active](./mendeley_sub_cone_visual_resolution_by_active.md): Data from: Sub-cone visual resolution by active, adaptive sampling in the human foveola (16 participants, `cc-by`)
- [asd_eye_tracking](./asd_eye_tracking.md): Autism Spectrum Disorder Eye-Tracking Dataset (Not reported, `cc-by`)
