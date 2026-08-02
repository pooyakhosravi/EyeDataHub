---
id: mpii_gaze
title: "MPIIGaze Appearance-Based Gaze Estimation Dataset"
sidebar_label: mpii_gaze
description: "Longitudinal laptop-camera images captured during natural daily use with gaze targets, face geometry, and normalized views."
tags: ["eye_tracking", "cc-by-nc-sa", "manual", "gaze_estimation", "regression", "resource-role-current-dataset", "dataset-family-mpii-gaze"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# MPIIGaze Appearance-Based Gaze Estimation Dataset

Longitudinal laptop-camera images captured during natural daily use with gaze targets, face geometry, and normalized views.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mpii_gaze` |
| **Full name** | MPIIGaze Appearance-Based Gaze Estimation Dataset |
| **Primary category** | `eye_tracking` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `mpii_gaze` |
| **Contained modalities** | eye_tracking |
| **Tasks** | gaze_estimation, regression |
| **Primary reported quantity** | 213,659 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 2.1 GB |
| **Source-stated terms** | CC BY-NC-SA 4.0; non-commercial scientific use only |
| **Normalized terms** | `cc-by-nc-sa` |
| **Descriptive screening label** | Explicit noncommercial clause recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `guided_instructions_only` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 213,659 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [mpi-inf.mpg.de/de](https://www.mpi-inf.mpg.de/de/departments/computer-vision-and-machine-learning/research/gaze-based-human-computer-interaction/appearance-based-gaze-estimation-in-the-wild) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> The institutional page reports 213,659 images from 15 participants collected over more than three months and provides a 2.1 GB download for non-commercial scientific use.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mpii_gaze --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download mpii_gaze --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mpii_gaze')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [mpi-inf.mpg.de/de](https://www.mpi-inf.mpg.de/de/departments/computer-vision-and-machine-learning/research/gaze-based-human-computer-interaction/appearance-based-gaze-estimation-in-the-wild)

**Source-term evidence:** [mpi-inf.mpg.de/de](https://www.mpi-inf.mpg.de/de/departments/computer-vision-and-machine-learning/research/gaze-based-human-computer-interaction/appearance-based-gaze-estimation-in-the-wild)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mpii_gaze,
  title  = { MPIIGaze Appearance-Based Gaze Estimation Dataset },
  note   = { Zhang X, Sugano Y, Fritz M, Bulling A. Appearance-Based Gaze Estimation in the Wild. CVPR. 2015:4511-4520 },
  year   = { 2015 },
  url    = { https://www.mpi-inf.mpg.de/de/departments/computer-vision-and-machine-learning/research/gaze-based-human-computer-interaction/appearance-based-gaze-estimation-in-the-wild },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Zhang X, Sugano Y, Fritz M, Bulling A. Appearance-Based Gaze Estimation in the Wild. CVPR. 2015:4511-4520.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC BY-NC-SA 4.0; non-commercial scientific use only
- **Normalized category:** `cc-by-nc-sa`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Explicit noncommercial clause recorded; check source

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [teyed](./teyed.md): TEyeD Real-World Eye-Tracking Dataset (20,666,096 images, `unknown`)
- [gaze_capture](./gaze_capture.md): GazeCapture Mobile Eye-Tracking Dataset (2,445,504 frames, `unknown`)
- [eth_xgaze](./eth_xgaze.md): ETH-XGaze Extreme-Pose Gaze Estimation Dataset (1,083,492 images, `cc-by-nc-sa`)
- [gaze360](./gaze360.md): Gaze360 Physically Unconstrained Gaze Dataset (172,000 frames, `unknown`)
- [lpw](./lpw.md): LPW Labelled Pupils in the Wild (130,856 frames, `research-only`)
- [glaucoma_eye_movements](./glaucoma_eye_movements.md): Eye Movements of Glaucoma Patients with Asymmetrical Visual Field Loss (270 participants, `cc-by`)
- [asd_eye_tracking](./asd_eye_tracking.md): Autism Spectrum Disorder Eye-Tracking Dataset (Not reported, `cc-by`)
- [hybridgaze](./hybridgaze.md): HybridGaze Dataset (Not reported, `unknown`)
