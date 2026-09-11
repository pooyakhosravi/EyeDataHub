---
id: natural_scene_eye_tracking_collection
title: "Natural-Scene Tobii Eye-Tracking Collection"
sidebar_label: natural_scene_eye_tracking_collection
description: "Tobii Pro Glasses 3 natural-scene viewing recordings with gaze, IMU, event, video, and snapshot files."
tags: ["eye_tracking", "cc-by", "figshare", "gaze_estimation", "measurement", "resource-role-current-dataset", "dataset-family-natural-scene-eye-tracking-collection", "alternate-source", "source-figshare", "alternate-role-component-deposit"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Natural-Scene Tobii Eye-Tracking Collection

Tobii Pro Glasses 3 natural-scene viewing recordings with gaze, IMU, event, video, and snapshot files.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `natural_scene_eye_tracking_collection` |
| **Full name** | Natural-Scene Tobii Eye-Tracking Collection |
| **Publication date** | 2025-11-03 |
| **Date basis** | Initial dataset release |
| **Publication date precision** | day |
| **Publication date evidence** | [api.figshare.com/v2](https://api.figshare.com/v2/articles/30520733/versions/1) |
| **Publication date source field** | published_date (Figshare version 1) |
| **Publication date reviewed** | 2026-09-11 |
| **Date notes** | Collection-level catalog anchor; version 1 is earliest. |
| **Primary category** | `eye_tracking` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `natural_scene_eye_tracking_collection` |
| **Contained modalities** | eye_tracking |
| **Tasks** | gaze_estimation, measurement |
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

## Notes

> Collection-level anchor. Official components include 30520775, 30520829, 30520892, 30520925, and 30520979. The public file listings for 30520775 and 30520892 are byte-identical Indoor Scene 3 deposits.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download natural_scene_eye_tracking_collection --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download natural_scene_eye_tracking_collection --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('natural_scene_eye_tracking_collection')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.6084/m9.figshare.30520733.v1](https://doi.org/10.6084/m9.figshare.30520733.v1)

## Other documented locations

These links identify alternate deposits, components, metadata records, mirrors, versions, or related derived materials. They do not create additional canonical catalog records.

- [figshare: component deposit (30520775, version 1)](https://figshare.com/articles/dataset/30520775): Indoor Scene 3 component; official file listing is byte-identical to 30520892.
- [figshare: component deposit (30520829, version 1)](https://figshare.com/articles/dataset/30520829): Outdoor Scene 1 component.
- [figshare: component deposit (30520892, version 1)](https://figshare.com/articles/dataset/30520892): Indoor Scene 3 component; duplicate payload of 30520775.
- [figshare: component deposit (30520925, version 1)](https://figshare.com/articles/dataset/30520925): Outdoor Scene 2 component.
- [figshare: component deposit (30520979, version 1)](https://figshare.com/articles/dataset/30520979): Outdoor Scene 3 component.

**Source-term evidence:** [https://doi.org/10.6084/m9.figshare.30520733.v1](https://doi.org/10.6084/m9.figshare.30520733.v1)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{natural_scene_eye_tracking_collection,
  title  = { Natural-Scene Tobii Eye-Tracking Collection },
  note   = { Repository dataset record. 10.6084/m9.figshare.30520733.v1 },
  url    = { https://doi.org/10.6084/m9.figshare.30520733.v1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Repository dataset record. 10.6084/m9.figshare.30520733.v1.
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
