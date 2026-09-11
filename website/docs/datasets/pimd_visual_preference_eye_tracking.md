---
id: pimd_visual_preference_eye_tracking
title: "PIMD Visual Preference Eye-Tracking Dataset"
sidebar_label: pimd_visual_preference_eye_tracking
description: "Human eye-tracking observations from a visual-preference study."
tags: ["eye_tracking", "cc-by", "figshare", "measurement", "resource-role-current-dataset", "dataset-family-pimd-visual-preference-eye-tracking"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# PIMD Visual Preference Eye-Tracking Dataset

Human eye-tracking observations from a visual-preference study.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `pimd_visual_preference_eye_tracking` |
| **Full name** | PIMD Visual Preference Eye-Tracking Dataset |
| **First published** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Primary category** | `eye_tracking` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `pimd_visual_preference_eye_tracking` |
| **Contained modalities** | eye_tracking |
| **Tasks** | measurement |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Figshare |
| **Availability** | `available` (checked 2026-08-02) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

No reproducible primary item count was exposed for the cataloged source version.

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download pimd_visual_preference_eye_tracking --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download pimd_visual_preference_eye_tracking --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('pimd_visual_preference_eye_tracking')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.1371/journal.pone.0266176.s010](https://doi.org/10.1371/journal.pone.0266176.s010)

**Source-term evidence:** [https://doi.org/10.1371/journal.pone.0266176.s010](https://doi.org/10.1371/journal.pone.0266176.s010)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{pimd_visual_preference_eye_tracking,
  title  = { PIMD Visual Preference Eye-Tracking Dataset },
  note   = { Repository dataset record. 10.1371/journal.pone.0266176.s010 },
  url    = { https://doi.org/10.1371/journal.pone.0266176.s010 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Repository dataset record. 10.1371/journal.pone.0266176.s010.
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
- [glaucoma_eye_movements](./glaucoma_eye_movements.md): Eye Movements of Glaucoma Patients with Asymmetrical Visual Field Loss (270 participants, `cc-by`)
- [mendeley_sub_cone_visual_resolution_by_active](./mendeley_sub_cone_visual_resolution_by_active.md): Data from: Sub-cone visual resolution by active, adaptive sampling in the human foveola (16 participants, `cc-by`)
