---
id: hesc_retinal_organoid_early_differentiation
title: "hESC-Derived Retinal Organoid Early Differentiation Imaging Dataset"
sidebar_label: hesc_retinal_organoid_early_differentiation
description: "Time-series bright-field imaging of human embryonic-stem-cell-derived retinal organoid aggregates."
tags: ["cell_microscopy", "microscopy", "cc-by", "figshare", "classification", "measurement", "resource-role-current-dataset", "dataset-family-hesc-retinal-organoid-early-differentiation"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# hESC-Derived Retinal Organoid Early Differentiation Imaging Dataset

Time-series bright-field imaging of human embryonic-stem-cell-derived retinal organoid aggregates.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `hesc_retinal_organoid_early_differentiation` |
| **Full name** | hESC-Derived Retinal Organoid Early Differentiation Imaging Dataset |
| **Publication date** | 2026-03-02 |
| **Date basis** | Initial dataset release |
| **Publication date precision** | day |
| **Publication date evidence** | [api.figshare.com/v2](https://api.figshare.com/v2/articles/30102802/versions/1) |
| **Publication date source field** | published_date (Figshare version 1) |
| **Publication date reviewed** | 2026-09-11 |
| **Date notes** | Only listed Figshare version. |
| **Primary category** | `cell_microscopy` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `hesc_retinal_organoid_early_differentiation` |
| **Contained modalities** | cell_microscopy, microscopy |
| **Tasks** | classification, measurement |
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

> Source reports 384 aggregates imaged across days 6–30; no catalog quantity is asserted because the source unit is outside the controlled vocabulary.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download hesc_retinal_organoid_early_differentiation --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download hesc_retinal_organoid_early_differentiation --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('hesc_retinal_organoid_early_differentiation')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.6084/m9.figshare.30102802.v1](https://doi.org/10.6084/m9.figshare.30102802.v1)

**Source-term evidence:** [https://doi.org/10.6084/m9.figshare.30102802.v1](https://doi.org/10.6084/m9.figshare.30102802.v1)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{hesc_retinal_organoid_early_differentiation,
  title  = { hESC-Derived Retinal Organoid Early Differentiation Imaging Dataset },
  note   = { Repository dataset record. 10.6084/m9.figshare.30102802.v1 },
  url    = { https://doi.org/10.6084/m9.figshare.30102802.v1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Repository dataset record. 10.6084/m9.figshare.30102802.v1.
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

- [goblet_cell_segmentation](./goblet_cell_segmentation.md): Human Conjunctival Goblet Cell Segmentation Dataset (24 images, `cc-by`)
- [mendeley_digital_holograms_rbcs_glaucoma_patients_healthy](./mendeley_digital_holograms_rbcs_glaucoma_patients_healthy.md): Digital holograms of RBCs from the glaucoma patients and healthy controls (Not reported, `cc-by`)
- [mendeley_ocular_sebaceous_neoplasms](./mendeley_ocular_sebaceous_neoplasms.md): Ocular sebaceous neoplasms (Not reported, `cc-by`)
