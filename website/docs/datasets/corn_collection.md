---
id: corn_collection
title: "CORN: Corneal Confocal Microscope Dataset Collection"
sidebar_label: corn_collection
description: "Combined corneal confocal microscopy collection comprising CORN-1, CORN-2, CORN-3, CORN-1500, CORN-Pro, and CORN-Complex. The subsets support corneal-nerve and cell segmentation, image enhancement, to"
tags: ["confocal", "cc-by", "manual", "segmentation", "grading", "classification", "quality"]
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
| **Primary category** | `confocal` |
| **Contained modalities** | confocal |
| **Tasks** | segmentation, grading, classification, quality |
| **Samples** | Not reported |
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


## Notes

> The Zenodo record is publicly visible, but its files require a logged-in access request containing the user's name, organization, work, and intended use. EyeDataHub displays those instructions and does not submit the request. This collection includes and overlaps the separately indexed CORN-1500 and CORN-Pro records; its six subsets must not be counted as independent cohorts.

## Access preflight and acquisition

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

## Related datasets with shared modalities

- [corn1500](./corn1500.md): CORN-1500: Corneal Nerve Tortuosity Grading (1,500 records, `unknown`)
- [corn_pro](./corn_pro.md): CORN Pro: Corneal Nerve Confocal Microscopy Dataset (1,120 records, `cc-by`)
- [superccm_fineset](./superccm_fineset.md): SuperCCM-FineSet (210 records, `unknown`)
- [corneal_epithelium_confocal](./corneal_epithelium_confocal.md): Keratoconus Corneal Epithelium Confocal Fluorescence Dataset (7 records, `cc-by`)
