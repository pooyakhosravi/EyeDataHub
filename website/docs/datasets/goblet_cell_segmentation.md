---
id: goblet_cell_segmentation
title: "Human Conjunctival Goblet Cell Segmentation Dataset"
sidebar_label: goblet_cell_segmentation
description: "Phase-contrast microscopy fields of cultured human conjunctival goblet cells with semantic and instance-compatible masks."
tags: ["cell_microscopy", "cc-by", "zenodo", "segmentation", "counting", "resource-role-current-dataset", "dataset-family-goblet-cell-segmentation"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Human Conjunctival Goblet Cell Segmentation Dataset

Phase-contrast microscopy fields of cultured human conjunctival goblet cells with semantic and instance-compatible masks.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `goblet_cell_segmentation` |
| **Full name** | Human Conjunctival Goblet Cell Segmentation Dataset |
| **Primary category** | `cell_microscopy` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `goblet_cell_segmentation` |
| **Contained modalities** | cell_microscopy |
| **Tasks** | segmentation, counting |
| **Primary reported quantity** | 24 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.514 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Zenodo |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 24 | `images` | Unpatched microscopy fields | `official_source_description` | [https://doi.org/10.5281/zenodo.18642562](https://doi.org/10.5281/zenodo.18642562) |
| Additional | 1,152 | `images` | Derivative 256 by 256 patches Patches derive from the 24 primary fields and must not be added as independent source images. | `official_source_description` | [https://doi.org/10.5281/zenodo.18642562](https://doi.org/10.5281/zenodo.18642562) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> The independent unit is 24 unpatched 2048x1536 fields with 65,108 cell instances. The release also contains 1,152 derivative 256x256 patches (75,597 counted instances because boundary cells can recur).

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download goblet_cell_segmentation --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download goblet_cell_segmentation --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('goblet_cell_segmentation')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5281/zenodo.18642562](https://doi.org/10.5281/zenodo.18642562)

**Source-term evidence:** [https://doi.org/10.5281/zenodo.18642562](https://doi.org/10.5281/zenodo.18642562)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{goblet_cell_segmentation,
  title  = { Human Conjunctival Goblet Cell Segmentation Dataset },
  note   = { Fineide FA, Bair J, Utheim TP, Riegler MA, Dartt DA. Development of Human Conjunctival Goblet Cell Segmentation Datasets to Improve Quantitation. Scientific Data. 2026. doi:10.1038/s41597-026-07309-w },
  year   = { 2026 },
  url    = { https://doi.org/10.5281/zenodo.18642562 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Fineide FA, Bair J, Utheim TP, Riegler MA, Dartt DA. Development of Human Conjunctival Goblet Cell Segmentation Datasets to Improve Quantitation. Scientific Data. 2026. doi:10.1038/s41597-026-07309-w
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

- [hesc_retinal_organoid_early_differentiation](./hesc_retinal_organoid_early_differentiation.md): hESC-Derived Retinal Organoid Early Differentiation Imaging Dataset (Not reported, `cc-by`)
