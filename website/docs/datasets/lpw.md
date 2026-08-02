---
id: lpw
title: "LPW Labelled Pupils in the Wild"
sidebar_label: lpw
description: "High-speed head-mounted eye-region videos with pupil-center annotations under varied indoor, outdoor, eyewear, and lighting conditions."
tags: ["eye_tracking", "research-only", "manual", "pupil_detection", "landmark_detection"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# LPW Labelled Pupils in the Wild

High-speed head-mounted eye-region videos with pupil-center annotations under varied indoor, outdoor, eyewear, and lighting conditions.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `lpw` |
| **Full name** | LPW Labelled Pupils in the Wild |
| **Primary category** | `eye_tracking` |
| **Contained modalities** | eye_tracking |
| **Tasks** | pupil_detection, landmark_detection |
| **Primary reported quantity** | 130,856 frames |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 2.4 GB |
| **Source-stated terms** | Non-commercial research use only |
| **Normalized terms** | `research-only` |
| **Descriptive screening label** | Research or challenge restriction recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `guided_instructions_only` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 130,856 | `frames` | Labeled eye-region images | `official_source_description` | [mpi-inf.mpg.de/departments](https://www.mpi-inf.mpg.de/departments/computer-vision-and-machine-learning/research/gaze-based-human-computer-interaction/labelled-pupils-in-the-wild-lpw) |
| Additional | 66 | `videos` | High-speed source videos | `official_source_description` | [mpi-inf.mpg.de/departments](https://www.mpi-inf.mpg.de/departments/computer-vision-and-machine-learning/research/gaze-based-human-computer-interaction/labelled-pupils-in-the-wild-lpw) |
| Additional | 22 | `participants` | Participants recorded in everyday locations | `official_source_description` | [mpi-inf.mpg.de/departments](https://www.mpi-inf.mpg.de/departments/computer-vision-and-machine-learning/research/gaze-based-human-computer-interaction/labelled-pupils-in-the-wild-lpw) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> The institutional page reports 66 videos and 130,856 images from 22 participants. It explicitly limits use to non-commercial scientific purposes.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download lpw --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download lpw --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('lpw')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [mpi-inf.mpg.de/de](https://www.mpi-inf.mpg.de/de/departments/computer-vision-and-machine-learning/research/gaze-based-human-computer-interaction/labelled-pupils-in-the-wild-lpw/)

**Source-term evidence:** [mpi-inf.mpg.de/de](https://www.mpi-inf.mpg.de/de/departments/computer-vision-and-machine-learning/research/gaze-based-human-computer-interaction/labelled-pupils-in-the-wild-lpw/)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{lpw,
  title  = { LPW Labelled Pupils in the Wild },
  note   = { Tonsen M, Zhang X, Sugano Y, Bulling A. Labelled Pupils in the Wild: A Dataset for Studying Pupil Detection in Unconstrained Environments. ETRA. 2016:139-142. doi:10.1145/2857491.2857520 },
  year   = { 2016 },
  url    = { https://www.mpi-inf.mpg.de/de/departments/computer-vision-and-machine-learning/research/gaze-based-human-computer-interaction/labelled-pupils-in-the-wild-lpw/ },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Tonsen M, Zhang X, Sugano Y, Bulling A. Labelled Pupils in the Wild: A Dataset for Studying Pupil Detection in Unconstrained Environments. ETRA. 2016:139-142. doi:10.1145/2857491.2857520
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Non-commercial research use only
- **Normalized category:** `research-only`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Research or challenge restriction recorded; check source

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [teyed](./teyed.md): TEyeD Real-World Eye-Tracking Dataset (20,666,096 images, `unknown`)
- [gaze_capture](./gaze_capture.md): GazeCapture Mobile Eye-Tracking Dataset (2,445,504 frames, `unknown`)
- [eth_xgaze](./eth_xgaze.md): ETH-XGaze Extreme-Pose Gaze Estimation Dataset (1,083,492 images, `cc-by-nc-sa`)
- [mpii_gaze](./mpii_gaze.md): MPIIGaze Appearance-Based Gaze Estimation Dataset (213,659 images, `cc-by-nc-sa`)
- [gaze360](./gaze360.md): Gaze360 Physically Unconstrained Gaze Dataset (172,000 frames, `unknown`)
- [glaucoma_eye_movements](./glaucoma_eye_movements.md): Eye Movements of Glaucoma Patients with Asymmetrical Visual Field Loss (270 participants, `cc-by`)
- [dryad_biocular_eye_tracking](./dryad_biocular_eye_tracking.md): Bi-Ocular Vertebrate Eye-Tracking Dataset (Not reported, `cc0`)
- [dryad_eye_head_visual_selection](./dryad_eye_head_visual_selection.md): Eye and Head Visual Selection Dataset (Not reported, `cc0`)
