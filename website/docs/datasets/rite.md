---
id: rite
title: "RITE: Retinal Images Vessel Tree Extraction (Artery/Vein)"
sidebar_label: rite
description: "40 fundus images (derived from DRIVE) with artery/vein annotations and vessel-tree structural labels."
tags: ["fundus", "research-only", "manual", "segmentation", "resource-role-annotation-layer", "dataset-family-rite", "documented-relationship", "relationship-derived_from"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# RITE: Retinal Images Vessel Tree Extraction (Artery/Vein)

40 fundus images (derived from DRIVE) with artery/vein annotations and vessel-tree structural labels.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `rite` |
| **Full name** | RITE: Retinal Images Vessel Tree Extraction (Artery/Vein) |
| **Publication date** | Unknown |
| **Date basis** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Date notes** | - |
| **Primary category** | `fundus` |
| **Resource role** | `annotation_layer` |
| **Dataset family** | `rite` |
| **Contained modalities** | fundus |
| **Tasks** | segmentation |
| **Primary reported quantity** | 40 images |
| **Classes** | 4 (background, artery, vein, unknown_vessel) |
| **Splits** | train, test |
| **Size** | 0.1 GB |
| **Source-stated terms** | Research only (Iowa Qualtrics request form) |
| **Normalized terms** | `research-only` |
| **Descriptive screening label** | Research or challenge restriction recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `controlled_or_manual` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `manual_access_blocked` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 40 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [eye.medicine.uiowa.edu/rite-dataset](https://eye.medicine.uiowa.edu/rite-dataset) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Iowa Qualtrics form gates download — no auto path.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- This record is `derived from` [drive](./drive.md): RITE adds artery, vein, and vessel-tree labels to the same 40 DRIVE images. ([evidence](https://medicine.uiowa.edu/eye/rite-dataset))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# This route requires upstream human action; no transfer starts.
eyehub download rite --data-dir ./data --dry-run --json
# Follow the official instructions shown by preflight.
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('rite')
print(preflight_dataset(ds, './data'))  # returns manual_access_blocked
```

  </TabItem>
</Tabs>

**Upstream page:** [eye.medicine.uiowa.edu/rite-dataset](https://eye.medicine.uiowa.edu/rite-dataset)

**Source-term evidence:** [eye.medicine.uiowa.edu/rite-dataset](https://eye.medicine.uiowa.edu/rite-dataset)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{rite,
  title  = { RITE: Retinal Images Vessel Tree Extraction (Artery/Vein) },
  note   = { Hu et al., 'Automated Separation of Binary Overlapping Trees in Low-Contrast Color Retinal Images', MICCAI 2013 },
  year   = { 2013 },
  url    = { https://eye.medicine.uiowa.edu/rite-dataset },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Hu et al., 'Automated Separation of Binary Overlapping Trees in Low-Contrast Color Retinal Images', MICCAI 2013.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Research only (Iowa Qualtrics request form)
- **Normalized category:** `research-only`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Research or challenge restriction recorded; check source

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [airogs](./airogs.md): AIROGS: AI for Robust Glaucoma Screening (113,893 images, `cc-by-nc-nd`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (103,959 images, `mit`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [justraigs](./justraigs.md): JustRAIGS: Just Referral AI Glaucoma Screening Dataset (101,442 images, `cc-by-nc-nd`)
- [eyepacs](./eyepacs.md): EyePACS — Diabetic Retinopathy Detection (Kaggle 2015) (88,702 images, `research-only`)
- [angioreport](./angioreport.md): AngioReport Fundus Angiography Report Dataset (55,361 images, `unknown`)
- [ffa_ir](./ffa_ir.md): FFA-IR Medical Report Dataset (47,247 images, `unknown`)
- [mfiddr](./mfiddr.md): MFIDDR: Multi-Field Imaging Dataset for Diabetic Retinopathy (34,452 images, `mit`)
