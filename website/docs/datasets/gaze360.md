---
id: gaze360
title: "Gaze360 Physically Unconstrained Gaze Dataset"
sidebar_label: gaze360
description: "Indoor and outdoor panoramic-camera recordings with continuous three-dimensional gaze labels across wide head poses and distances."
tags: ["eye_tracking", "unknown", "manual", "gaze_estimation", "regression", "resource-role-current-dataset", "dataset-family-gaze360"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Gaze360 Physically Unconstrained Gaze Dataset

Indoor and outdoor panoramic-camera recordings with continuous three-dimensional gaze labels across wide head poses and distances.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `gaze360` |
| **Full name** | Gaze360 Physically Unconstrained Gaze Dataset |
| **First published** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Primary category** | `eye_tracking` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `gaze360` |
| **Contained modalities** | eye_tracking |
| **Tasks** | gaze_estimation, regression |
| **Primary reported quantity** | 172,000 frames |
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
| Primary | 172,000 | `frames` | Labeled panoramic-camera frames | `official_source_description` | [gaze360.csail.mit.edu](http://gaze360.csail.mit.edu/) |
| Additional | 238 | `participants` | Source-described participants | `official_source_description` | [gaze360.csail.mit.edu](http://gaze360.csail.mit.edu/) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> The project reports 238 participants; the benchmark is commonly reported as 172,000 labeled frames. Access uses registration, and the public landing page does not state a standard reuse license.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download gaze360 --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download gaze360 --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('gaze360')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [gaze360.csail.mit.edu](https://gaze360.csail.mit.edu/)

**Source-term evidence:** [gaze360.csail.mit.edu](https://gaze360.csail.mit.edu/)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{gaze360,
  title  = { Gaze360 Physically Unconstrained Gaze Dataset },
  note   = { Kellnhofer P, Recasens A, Stent S, Matusik W, Torralba A. Gaze360: Physically Unconstrained Gaze Estimation in the Wild. ICCV. 2019:6912-6921. arXiv:1910.10088 },
  year   = { 2019 },
  url    = { https://gaze360.csail.mit.edu/ },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Kellnhofer P, Recasens A, Stent S, Matusik W, Torralba A. Gaze360: Physically Unconstrained Gaze Estimation in the Wild. ICCV. 2019:6912-6921. arXiv:1910.10088
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
- [gaze_capture](./gaze_capture.md): GazeCapture Mobile Eye-Tracking Dataset (2,445,504 frames, `unknown`)
- [eth_xgaze](./eth_xgaze.md): ETH-XGaze Extreme-Pose Gaze Estimation Dataset (1,083,492 images, `cc-by-nc-sa`)
- [mpii_gaze](./mpii_gaze.md): MPIIGaze Appearance-Based Gaze Estimation Dataset (213,659 images, `cc-by-nc-sa`)
- [lpw](./lpw.md): LPW Labelled Pupils in the Wild (130,856 frames, `research-only`)
- [glaucoma_eye_movements](./glaucoma_eye_movements.md): Eye Movements of Glaucoma Patients with Asymmetrical Visual Field Loss (270 participants, `cc-by`)
- [mendeley_sub_cone_visual_resolution_by_active](./mendeley_sub_cone_visual_resolution_by_active.md): Data from: Sub-cone visual resolution by active, adaptive sampling in the human foveola (16 participants, `cc-by`)
- [asd_eye_tracking](./asd_eye_tracking.md): Autism Spectrum Disorder Eye-Tracking Dataset (Not reported, `cc-by`)
