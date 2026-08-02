---
id: teyed
title: "TEyeD Real-World Eye-Tracking Dataset"
sidebar_label: teyed
description: "Head-mounted eye images with pupil, iris, eyelid, eyeball, gaze, landmark, segmentation, and eye-movement annotations."
tags: ["eye_tracking", "unknown", "manual", "gaze_estimation", "segmentation", "landmark_detection", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# TEyeD Real-World Eye-Tracking Dataset

Head-mounted eye images with pupil, iris, eyelid, eyeball, gaze, landmark, segmentation, and eye-movement annotations.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `teyed` |
| **Full name** | TEyeD Real-World Eye-Tracking Dataset |
| **Primary category** | `eye_tracking` |
| **Contained modalities** | eye_tracking |
| **Tasks** | gaze_estimation, segmentation, landmark_detection, classification |
| **Primary reported quantity** | 20,666,096 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | Unknown; public FTP is described in the paper but no license is stated |
| **Normalized terms** | `unknown` |
| **Descriptive screening label** | Unknown or unclear; do not assume permission |
| **Terms scope** | `unknown` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `guided_instructions_only` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 20,666,096 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [arxiv.org/abs](https://arxiv.org/abs/2102.02115) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> The paper reports 20,666,096 open- or closed-eye frames and also 200,977 no-eye frames, collected with seven trackers. It documents anonymous FTP access at nephrit.cs.uni-tuebingen.de using user TEyeDUser, but does not state a standard dataset license; confirm availability and terms before use.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download teyed --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download teyed --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('teyed')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [arxiv.org/abs](https://arxiv.org/abs/2102.02115)

**Source-term evidence:** [arxiv.org/abs](https://arxiv.org/abs/2102.02115)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{teyed,
  title  = { TEyeD Real-World Eye-Tracking Dataset },
  note   = { Fuhl W, Kasneci G, Kasneci E. TEyeD: Over 20 Million Real-World Eye Images with Rich 2D and 3D Annotations. arXiv:2102.02115. 2021 },
  year   = { 2102 },
  url    = { https://arxiv.org/abs/2102.02115 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Fuhl W, Kasneci G, Kasneci E. TEyeD: Over 20 Million Real-World Eye Images with Rich 2D and 3D Annotations. arXiv:2102.02115. 2021.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Unknown; public FTP is described in the paper but no license is stated
- **Normalized category:** `unknown`
- **Apparent scope:** `unknown`
- **Descriptive screening label:** Unknown or unclear; do not assume permission

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [gaze_capture](./gaze_capture.md): GazeCapture Mobile Eye-Tracking Dataset (2,445,504 frames, `unknown`)
- [eth_xgaze](./eth_xgaze.md): ETH-XGaze Extreme-Pose Gaze Estimation Dataset (1,083,492 images, `cc-by-nc-sa`)
- [mpii_gaze](./mpii_gaze.md): MPIIGaze Appearance-Based Gaze Estimation Dataset (213,659 images, `cc-by-nc-sa`)
- [gaze360](./gaze360.md): Gaze360 Physically Unconstrained Gaze Dataset (172,000 frames, `unknown`)
- [lpw](./lpw.md): LPW Labelled Pupils in the Wild (130,856 frames, `research-only`)
- [glaucoma_eye_movements](./glaucoma_eye_movements.md): Eye Movements of Glaucoma Patients with Asymmetrical Visual Field Loss (270 participants, `cc-by`)
- [dryad_biocular_eye_tracking](./dryad_biocular_eye_tracking.md): Bi-Ocular Vertebrate Eye-Tracking Dataset (Not reported, `cc0`)
- [dryad_eye_head_visual_selection](./dryad_eye_head_visual_selection.md): Eye and Head Visual Selection Dataset (Not reported, `cc0`)
