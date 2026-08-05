---
id: superccm_fineset
title: "SuperCCM-FineSet"
sidebar_label: superccm_fineset
description: "Restricted corneal confocal microscopy image set with pixel-level corneal-nerve masks annotated for high-precision segmentation."
tags: ["confocal", "unknown", "manual", "segmentation", "resource-role-current-dataset", "dataset-family-superccm-fineset"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# SuperCCM-FineSet

Restricted corneal confocal microscopy image set with pixel-level corneal-nerve masks annotated for high-precision segmentation.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `superccm_fineset` |
| **Full name** | SuperCCM-FineSet |
| **Primary category** | `confocal` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `superccm_fineset` |
| **Contained modalities** | confocal |
| **Tasks** | segmentation |
| **Primary reported quantity** | 210 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.05 GB |
| **Source-stated terms** | GPL-3.0-or-later |
| **Normalized terms** | `unknown` |
| **Descriptive screening label** | Unknown or unclear; do not assume permission |
| **Terms scope** | `unknown` |
| **Access friction** | `controlled_or_manual` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `manual_access_blocked` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 210 | `images` | Restricted fine-segmentation image set | `official_source_description` | [zenodo.org/records](https://zenodo.org/records/17051148) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Zenodo record is publicly visible, but files are restricted; source instructions request an email application with name, organization, and intended use.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# This route requires upstream human action; no transfer starts.
eyehub download superccm_fineset --data-dir ./data --dry-run --json
# Follow the official instructions shown by preflight.
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('superccm_fineset')
print(preflight_dataset(ds, './data'))  # returns manual_access_blocked
```

  </TabItem>
</Tabs>

**Upstream page:** [zenodo.org/records](https://zenodo.org/records/17051148)

**Source-term evidence:** [zenodo.org/records](https://zenodo.org/records/17051148)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{superccm_fineset,
  title  = { SuperCCM-FineSet },
  note   = { Qiao Q. SuperCCM-FineSet. Zenodo, 2025. doi:10.5281/zenodo.17051148 },
  year   = { 2025 },
  url    = { https://zenodo.org/records/17051148 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Qiao Q. SuperCCM-FineSet. Zenodo, 2025. doi:10.5281/zenodo.17051148
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** GPL-3.0-or-later
- **Normalized category:** `unknown`
- **Apparent scope:** `unknown`
- **Descriptive screening label:** Unknown or unclear; do not assume permission

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [corn_collection](./corn_collection.md): CORN: Corneal Confocal Microscope Dataset Collection (12,931 images, `cc-by`)
- [corn1500](./corn1500.md): CORN-1500: Corneal Nerve Tortuosity Grading (1,500 images, `unknown`)
- [corn_pro](./corn_pro.md): CORN Pro: Corneal Nerve Confocal Microscopy Dataset (1,120 images, `cc-by`)
- [qilu_ccm_nerve_segmentation](./qilu_ccm_nerve_segmentation.md): Qilu Annotated Corneal Confocal Microscopy Nerve Segmentation Dataset (410 images, `cc-by`)
- [corneal_epithelium_confocal](./corneal_epithelium_confocal.md): Keratoconus Corneal Epithelium Confocal Fluorescence Dataset (7 participants, `cc-by`)
- [corneal_nerve_parkinsons](./corneal_nerve_parkinsons.md): Corneal Nerve Parkinson Disease Dataset (Not reported, `cc-by`)
