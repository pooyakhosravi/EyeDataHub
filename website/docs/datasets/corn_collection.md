---
id: corn_collection
title: "CORN: Corneal Confocal Microscope Dataset Collection"
sidebar_label: corn_collection
description: "Combined corneal confocal microscopy collection comprising CORN-1, CORN-2, CORN-3, CORN-1500, CORN-Pro, and CORN-Complex. The subsets support corneal-nerve and cell segmentation, image enhancement, to"
tags: ["confocal", "cc-by", "manual", "segmentation", "grading", "classification", "quality", "resource-role-collection", "dataset-family-corn-collection", "documented-relationship", "relationship-component_of", "relationship-has_component"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# CORN: Corneal Confocal Microscope Dataset Collection

Combined corneal confocal microscopy collection comprising CORN-1, CORN-2, CORN-3, CORN-1500, CORN-Pro, and CORN-Complex. The subsets support corneal-nerve and cell segmentation, image enhancement, tortuosity grading, and multi-disease analysis.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `corn_collection` |
| **Full name** | CORN: Corneal Confocal Microscope Dataset Collection |
| **First published** | 2024-07-19 |
| **Publication date precision** | day |
| **Publication date evidence** | [zenodo.org/api](https://zenodo.org/api/records/12776091) |
| **Publication date source field** | metadata.publication_date (earliest CORN collection record/version) |
| **Publication date reviewed** | 2026-09-11 |
| **Primary category** | `confocal` |
| **Resource role** | `collection` |
| **Dataset family** | `corn_collection` |
| **Contained modalities** | confocal |
| **Tasks** | segmentation, grading, classification, quality |
| **Primary reported quantity** | 12,931 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | Creative Commons Attribution 4.0 International |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `controlled_or_manual` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-25) |
| **Acquisition support** | `manual_access_blocked` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 12,931 | `images` | Sum of six source-described CORN subsets Includes the separately cataloged CORN1500 and CORN-Pro components and must not be added as an independent cohort total. | `derived_from_reported_components` | [zenodo.org/records](https://zenodo.org/records/19689814) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> The Zenodo record is publicly visible, but its files require a logged-in access request containing the user's name, organization, work, and intended use. EyeDataHub displays those instructions and does not submit the request. This collection includes and overlaps the separately indexed CORN-1500 and CORN-Pro records; its six subsets must not be counted as independent cohorts.

## Dataset family

This record belongs to `corn_collection`. Family links group documented collection/component records or exact task views; they do not imply independent cohorts.

- [corn1500](./corn1500.md): CORN-1500: Corneal Nerve Tortuosity Grading (`component_dataset`)
- [corn_pro](./corn_pro.md): CORN Pro: Corneal Nerve Confocal Microscopy Dataset (`component_dataset`)

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- [corn1500](./corn1500.md) is `component of` this record: CORN-1500 is a named component of the combined CORN collection. ([evidence](https://zenodo.org/records/19689814))
- [corn_pro](./corn_pro.md) is `component of` this record: CORN-Pro is a named component of the combined CORN collection. ([evidence](https://zenodo.org/records/19689814))
- This record is `has component` [corn1500](./corn1500.md): The CORN collection lists CORN-1500 as one of its six component deposits. ([evidence](https://zenodo.org/records/19689814))
- This record is `has component` [corn_pro](./corn_pro.md): The CORN collection lists CORN-Pro as one of its six component deposits. ([evidence](https://zenodo.org/records/19689814))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# This route requires upstream human action; no transfer starts.
eyehub download corn_collection --data-dir ./data --dry-run --json
# Follow the official instructions shown by preflight.
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('corn_collection')
print(preflight_dataset(ds, './data'))  # returns manual_access_blocked
```

  </TabItem>
</Tabs>

**Upstream page:** [zenodo.org/records](https://zenodo.org/records/19689814)

**Source-term evidence:** [zenodo.org/records](https://zenodo.org/records/19689814)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{corn_collection,
  title  = { CORN: Corneal Confocal Microscope Dataset Collection },
  note   = { iMED. CORN: corneal confocal microscope dataset. Zenodo, Version v2, 2026. doi:10.5281/zenodo.19689814 },
  year   = { 2026 },
  url    = { https://zenodo.org/records/19689814 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
iMED. CORN: corneal confocal microscope dataset. Zenodo, Version v2, 2026. doi:10.5281/zenodo.19689814
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Creative Commons Attribution 4.0 International
- **Normalized category:** `cc-by`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Standard label without an explicit NC clause; not a permission finding

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [corn1500](./corn1500.md): CORN-1500: Corneal Nerve Tortuosity Grading (1,500 images, `unknown`)
- [corn_pro](./corn_pro.md): CORN Pro: Corneal Nerve Confocal Microscopy Dataset (1,120 images, `cc-by`)
- [qilu_ccm_nerve_segmentation](./qilu_ccm_nerve_segmentation.md): Qilu Annotated Corneal Confocal Microscopy Nerve Segmentation Dataset (410 images, `cc-by`)
- [superccm_fineset](./superccm_fineset.md): SuperCCM-FineSet (210 images, `unknown`)
- [corneal_epithelium_confocal](./corneal_epithelium_confocal.md): Keratoconus Corneal Epithelium Confocal Fluorescence Dataset (7 participants, `cc-by`)
- [corneal_nerve_parkinsons](./corneal_nerve_parkinsons.md): Corneal Nerve Parkinson Disease Dataset (Not reported, `cc-by`)
