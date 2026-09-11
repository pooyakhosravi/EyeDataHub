---
id: pupillometry_eeg_fmri_salience
title: "Pupillometry, EEG, and fMRI Salience Dataset"
sidebar_label: pupillometry_eeg_fmri_salience
description: "Human synchronized pupillometry, EEG, and fMRI salience measurements."
tags: ["eye_tracking", "pupillometry", "cc-by", "figshare", "measurement", "resource-role-current-dataset", "dataset-family-pupillometry-eeg-fmri-salience"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Pupillometry, EEG, and fMRI Salience Dataset

Human synchronized pupillometry, EEG, and fMRI salience measurements.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `pupillometry_eeg_fmri_salience` |
| **Full name** | Pupillometry, EEG, and fMRI Salience Dataset |
| **Publication date** | 2023-04-03 |
| **Date basis** | Initial dataset release |
| **Publication date precision** | day |
| **Publication date evidence** | [api.figshare.com/v2](https://api.figshare.com/v2/articles/22518010/versions/1) |
| **Publication date source field** | published_date (Figshare version 1) |
| **Publication date reviewed** | 2026-09-11 |
| **Date notes** | Dataset-and-demo record release; only listed version. |
| **Primary category** | `eye_tracking` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `pupillometry_eeg_fmri_salience` |
| **Contained modalities** | eye_tracking, pupillometry |
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
eyehub download pupillometry_eeg_fmri_salience --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download pupillometry_eeg_fmri_salience --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('pupillometry_eeg_fmri_salience')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.6084/m9.figshare.22518010.v1](https://doi.org/10.6084/m9.figshare.22518010.v1)

**Source-term evidence:** [https://doi.org/10.6084/m9.figshare.22518010.v1](https://doi.org/10.6084/m9.figshare.22518010.v1)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{pupillometry_eeg_fmri_salience,
  title  = { Pupillometry, EEG, and fMRI Salience Dataset },
  note   = { Repository dataset record. 10.6084/m9.figshare.22518010.v1 },
  url    = { https://doi.org/10.6084/m9.figshare.22518010.v1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Repository dataset record. 10.6084/m9.figshare.22518010.v1.
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

- [spectrosense_pupil_light_exposure](./spectrosense_pupil_light_exposure.md): SpectroSense Pupil Light Exposure Dataset (Not reported, `cc-by`)
- [teyed](./teyed.md): TEyeD Real-World Eye-Tracking Dataset (20,666,096 images, `unknown`)
- [gaze_capture](./gaze_capture.md): GazeCapture Mobile Eye-Tracking Dataset (2,445,504 frames, `unknown`)
- [eth_xgaze](./eth_xgaze.md): ETH-XGaze Extreme-Pose Gaze Estimation Dataset (1,083,492 images, `cc-by-nc-sa`)
- [mpii_gaze](./mpii_gaze.md): MPIIGaze Appearance-Based Gaze Estimation Dataset (213,659 images, `cc-by-nc-sa`)
- [gaze360](./gaze360.md): Gaze360 Physically Unconstrained Gaze Dataset (172,000 frames, `unknown`)
- [lpw](./lpw.md): LPW Labelled Pupils in the Wild (130,856 frames, `research-only`)
- [fprm_retina](./fprm_retina.md): FPRM Multimodal Eye Imaging and Psychological Assessment Dataset (3,361 images, `research-only`)
