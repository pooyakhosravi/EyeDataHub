---
id: mendeley_et_pd_vis_eye_tracking_visualization
title: "ET_PD_VIS: Eye Tracking Visualization Dataset on Trail Making Test for Parkinson’s Disease Analysis"
sidebar_label: mendeley_et_pd_vis_eye_tracking_visualization
description: "Observation-level source data, annotations, or signals. from The Parkinson disease and healthy-control gaze study is a human visual/gaze resource."
tags: ["eye_tracking", "cc-by", "mendeley", "measurement", "resource-role-current-dataset", "dataset-family-mendeley-et-pd-vis-eye-tracking-visualization"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# ET_PD_VIS: Eye Tracking Visualization Dataset on Trail Making Test for Parkinson’s Disease Analysis 

Observation-level source data, annotations, or signals. from The Parkinson disease and healthy-control gaze study is a human visual/gaze resource.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mendeley_et_pd_vis_eye_tracking_visualization` |
| **Full name** | ET_PD_VIS: Eye Tracking Visualization Dataset on Trail Making Test for Parkinson’s Disease Analysis  |
| **Primary category** | `eye_tracking` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `mendeley_et_pd_vis_eye_tracking_visualization` |
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

> Human provenance: The Parkinson disease and healthy-control gaze study is a human visual/gaze resource. Source-review finding: 360 JPG/PNG eye-tracking visualization images.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mendeley_et_pd_vis_eye_tracking_visualization --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download mendeley_et_pd_vis_eye_tracking_visualization --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mendeley_et_pd_vis_eye_tracking_visualization')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/83htprx9y6/1)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/83htprx9y6)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mendeley_et_pd_vis_eye_tracking_visualization,
  title  = { ET_PD_VIS: Eye Tracking Visualization Dataset on Trail Making Test for Parkinson’s Disease Analysis  },
  note   = { ET_PD_VIS: Eye Tracking Visualization Dataset on Trail Making Test for Parkinson’s Disease Analysis . Mendeley Data, V1. doi:10.17632/83htprx9y6.1 },
  url    = { https://data.mendeley.com/datasets/83htprx9y6/1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
ET_PD_VIS: Eye Tracking Visualization Dataset on Trail Making Test for Parkinson’s Disease Analysis . Mendeley Data, V1. doi:10.17632/83htprx9y6.1.
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
- [asd_eye_tracking](./asd_eye_tracking.md): Autism Spectrum Disorder Eye-Tracking Dataset (Not reported, `cc-by`)
