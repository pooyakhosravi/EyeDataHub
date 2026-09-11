---
id: mendeley_human_foveal_cone_topography_preferred_retinal
title: "Human foveal cone topography and preferred retinal locus of fixation"
sidebar_label: mendeley_human_foveal_cone_topography_preferred_retinal
description: "Observation-level source data, annotations, or signals. from Human foveal cone topography and fixation locations are explicitly stated."
tags: ["eye_tracking", "cc-by", "mendeley", "measurement", "resource-role-current-dataset", "dataset-family-mendeley-human-foveal-cone-topography-preferred-retinal"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Human foveal cone topography and preferred retinal locus of fixation

Observation-level source data, annotations, or signals. from Human foveal cone topography and fixation locations are explicitly stated.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mendeley_human_foveal_cone_topography_preferred_retinal` |
| **Full name** | Human foveal cone topography and preferred retinal locus of fixation |
| **First published** | 2021-08-03 |
| **Publication date precision** | day |
| **Publication date evidence** | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/9gkpxsmz23/1) |
| **Publication date source field** | citation_publication_date (version 1) |
| **Publication date reviewed** | 2026-09-11 |
| **Primary category** | `eye_tracking` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `mendeley_human_foveal_cone_topography_preferred_retinal` |
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
| **Route backend** | Mendeley Data |
| **Availability** | `available` (checked 2026-08-02) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

No reproducible primary item count was exposed for the cataloged source version.

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Human provenance: Human foveal cone topography and fixation locations are explicitly stated. Source-review finding: 124 files: 41 TIF images, 82 TXT coordinate files, and one MATLAB script. Potential overlap with related foveola studies was not resolved; no record-to-record edge is encoded.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mendeley_human_foveal_cone_topography_preferred_retinal --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download mendeley_human_foveal_cone_topography_preferred_retinal --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mendeley_human_foveal_cone_topography_preferred_retinal')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/9gkpxsmz23/1)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/9gkpxsmz23)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mendeley_human_foveal_cone_topography_preferred_retinal,
  title  = { Human foveal cone topography and preferred retinal locus of fixation },
  note   = { Human foveal cone topography and preferred retinal locus of fixation. Mendeley Data, V1. doi:10.17632/9gkpxsmz23.1 },
  url    = { https://data.mendeley.com/datasets/9gkpxsmz23/1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Human foveal cone topography and preferred retinal locus of fixation. Mendeley Data, V1. doi:10.17632/9gkpxsmz23.1.
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
