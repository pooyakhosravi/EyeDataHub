---
id: dryad_biocular_eye_tracking
title: "Bi-Ocular Vertebrate Eye-Tracking Dataset"
sidebar_label: dryad_biocular_eye_tracking
description: "The bi-ocular vertebrate eye-tracking spreadsheets are a defined ocular-motor measurement-method resource."
tags: ["eye_tracking", "cc0", "dryad", "gaze_estimation", "measurement"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Bi-Ocular Vertebrate Eye-Tracking Dataset

The bi-ocular vertebrate eye-tracking spreadsheets are a defined ocular-motor measurement-method resource.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_biocular_eye_tracking` |
| **Full name** | Bi-Ocular Vertebrate Eye-Tracking Dataset |
| **Primary category** | `eye_tracking` |
| **Contained modalities** | eye_tracking |
| **Tasks** | gaze_estimation, measurement |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.000132673 GB |
| **Source-stated terms** | https://spdx.org/licenses/CC0-1.0.html |
| **Normalized terms** | `cc0` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Dryad |
| **Availability** | `available` (checked 2026-08-01) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

No reproducible primary item count was exposed for the cataloged source version.

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Scope screen: adjacent_add. Current Dryad v1 file listing: 2 files, 108554 bytes.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_biocular_eye_tracking --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dryad_biocular_eye_tracking --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_biocular_eye_tracking')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.84hc0](https://doi.org/10.5061/dryad.84hc0)

**Source-term evidence:** [https://doi.org/10.5061/dryad.84hc0](https://doi.org/10.5061/dryad.84hc0)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_biocular_eye_tracking,
  title  = { Bi-Ocular Vertebrate Eye-Tracking Dataset },
  note   = { Tyrrell, Luke P., Butler, Shannon R., Yorzinski, Jessica L., and Fernández-Juricic, Esteban. Data from: A novel system for bi-ocular eye-tracking in vertebrates with laterally placed eyes. Dryad. 2015. doi:10.5061/dryad.84hc0 },
  year   = { 2015 },
  url    = { https://doi.org/10.5061/dryad.84hc0 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Tyrrell, Luke P., Butler, Shannon R., Yorzinski, Jessica L., and Fernández-Juricic, Esteban. Data from: A novel system for bi-ocular eye-tracking in vertebrates with laterally placed eyes. Dryad. 2015. doi:10.5061/dryad.84hc0
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** https://spdx.org/licenses/CC0-1.0.html
- **Normalized category:** `cc0`
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
- [dryad_eye_head_visual_selection](./dryad_eye_head_visual_selection.md): Eye and Head Visual Selection Dataset (Not reported, `cc0`)
