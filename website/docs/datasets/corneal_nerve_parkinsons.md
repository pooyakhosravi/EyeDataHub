---
id: corneal_nerve_parkinsons
title: "Corneal Nerve Parkinson Disease Dataset"
sidebar_label: corneal_nerve_parkinsons
description: "Human corneal-nerve measurements in Parkinson disease study participants."
tags: ["confocal", "ivcm", "cc-by", "figshare", "measurement", "resource-role-current-dataset", "dataset-family-corneal-nerve-parkinsons"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Corneal Nerve Parkinson Disease Dataset

Human corneal-nerve measurements in Parkinson disease study participants.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `corneal_nerve_parkinsons` |
| **Full name** | Corneal Nerve Parkinson Disease Dataset |
| **First published** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Primary category** | `confocal` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `corneal_nerve_parkinsons` |
| **Contained modalities** | confocal, ivcm |
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
eyehub download corneal_nerve_parkinsons --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download corneal_nerve_parkinsons --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('corneal_nerve_parkinsons')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.6084/m9.figshare.28189571.v1](https://doi.org/10.6084/m9.figshare.28189571.v1)

**Source-term evidence:** [https://doi.org/10.6084/m9.figshare.28189571.v1](https://doi.org/10.6084/m9.figshare.28189571.v1)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{corneal_nerve_parkinsons,
  title  = { Corneal Nerve Parkinson Disease Dataset },
  note   = { Repository dataset record. 10.6084/m9.figshare.28189571.v1 },
  url    = { https://doi.org/10.6084/m9.figshare.28189571.v1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Repository dataset record. 10.6084/m9.figshare.28189571.v1.
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

- [corn_collection](./corn_collection.md): CORN: Corneal Confocal Microscope Dataset Collection (12,931 images, `cc-by`)
- [corn1500](./corn1500.md): CORN-1500: Corneal Nerve Tortuosity Grading (1,500 images, `unknown`)
- [corn_pro](./corn_pro.md): CORN Pro: Corneal Nerve Confocal Microscopy Dataset (1,120 images, `cc-by`)
- [qilu_ccm_nerve_segmentation](./qilu_ccm_nerve_segmentation.md): Qilu Annotated Corneal Confocal Microscopy Nerve Segmentation Dataset (410 images, `cc-by`)
- [superccm_fineset](./superccm_fineset.md): SuperCCM-FineSet (210 images, `unknown`)
- [corneal_epithelium_confocal](./corneal_epithelium_confocal.md): Keratoconus Corneal Epithelium Confocal Fluorescence Dataset (7 participants, `cc-by`)
