---
id: mendeley_code_manuscript_fixational_eye_movements_as
title: "Data and code for manuscript: Fixational eye movements as active sensation for high visual acuity"
sidebar_label: mendeley_code_manuscript_fixational_eye_movements_as
description: "Eye-movement sequences and supporting code from Human fixation/eye-movement experiment, as stated by the linked study title."
tags: ["eye_tracking", "tabular", "cc-by", "mendeley", "classification", "resource-role-current-dataset", "dataset-family-mendeley-code-manuscript-fixational-eye-movements-as"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Data and code for manuscript: Fixational eye movements as active sensation for high visual acuity

Eye-movement sequences and supporting code from Human fixation/eye-movement experiment, as stated by the linked study title.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mendeley_code_manuscript_fixational_eye_movements_as` |
| **Full name** | Data and code for manuscript: Fixational eye movements as active sensation for high visual acuity |
| **Publication date** | 2025-01-17 |
| **Date basis** | Initial dataset release |
| **Publication date precision** | day |
| **Publication date evidence** | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/p7dyyrfds6/1) |
| **Publication date source field** | citation_publication_date (version 1) |
| **Publication date reviewed** | 2026-09-11 |
| **Date notes** | - |
| **Primary category** | `eye_tracking` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `mendeley_code_manuscript_fixational_eye_movements_as` |
| **Contained modalities** | eye_tracking, tabular |
| **Tasks** | classification |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | Creative Commons Attribution Non Commercial 4.0 International |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `mixed_components` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Mendeley Data |
| **Availability** | `available` (checked 2026-08-02) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

No reproducible primary item count was exposed for the cataloged source version.

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Human provenance: Human fixation/eye-movement experiment, as stated by the linked study title. Source-review finding: Source description explicitly says the deposit contains code and data to reproduce the fixational-eye-movement findings.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mendeley_code_manuscript_fixational_eye_movements_as --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download mendeley_code_manuscript_fixational_eye_movements_as --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mendeley_code_manuscript_fixational_eye_movements_as')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/p7dyyrfds6/2)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/p7dyyrfds6)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mendeley_code_manuscript_fixational_eye_movements_as,
  title  = { Data and code for manuscript: Fixational eye movements as active sensation for high visual acuity },
  note   = { Data and code for manuscript: Fixational eye movements as active sensation for high visual acuity. Mendeley Data, V2. doi:10.17632/p7dyyrfds6.2 },
  url    = { https://data.mendeley.com/datasets/p7dyyrfds6/2 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Data and code for manuscript: Fixational eye movements as active sensation for high visual acuity. Mendeley Data, V2. doi:10.17632/p7dyyrfds6.2.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Creative Commons Attribution Non Commercial 4.0 International
- **Normalized category:** `cc-by`
- **Apparent scope:** `mixed_components`
- **Descriptive screening label:** Standard label without an explicit NC clause; not a permission finding

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [mendeley_sub_cone_visual_resolution_by_active](./mendeley_sub_cone_visual_resolution_by_active.md): Data from: Sub-cone visual resolution by active, adaptive sampling in the human foveola (16 participants, `cc-by`)
- [teyed](./teyed.md): TEyeD Real-World Eye-Tracking Dataset (20,666,096 images, `unknown`)
- [gaze_capture](./gaze_capture.md): GazeCapture Mobile Eye-Tracking Dataset (2,445,504 frames, `unknown`)
- [eth_xgaze](./eth_xgaze.md): ETH-XGaze Extreme-Pose Gaze Estimation Dataset (1,083,492 images, `cc-by-nc-sa`)
- [ocular_chat_vqa](./ocular_chat_vqa.md): OcularChat-VQA: AREDS-Derived Patient-Physician Dialogue Dataset (844,000 records, `cc-by-nc-sa`)
- [mpii_gaze](./mpii_gaze.md): MPIIGaze Appearance-Based Gaze Estimation Dataset (213,659 images, `cc-by-nc-sa`)
- [gaze360](./gaze360.md): Gaze360 Physically Unconstrained Gaze Dataset (172,000 frames, `unknown`)
- [lpw](./lpw.md): LPW Labelled Pupils in the Wild (130,856 frames, `research-only`)
