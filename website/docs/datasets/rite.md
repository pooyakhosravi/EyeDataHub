---
id: rite
title: "RITE: Retinal Images Vessel Tree Extraction (Artery/Vein)"
sidebar_label: rite
description: "40 fundus images (derived from DRIVE) with artery/vein annotations and vessel-tree structural labels."
tags: ["fundus", "research-only", "manual", "segmentation"]
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
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | segmentation |
| **Samples** | 40 |
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


## Notes

> Iowa Qualtrics form gates download — no auto path.

## Access preflight and acquisition

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

## Related datasets with shared modalities

- [airogs](./airogs.md): AIROGS: AI for Robust Glaucoma Screening (113,893 records, `cc-by-nc-nd`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 records, `unknown`)
- [justraigs](./justraigs.md): JustRAIGS: Just Referral AI Glaucoma Screening Dataset (101,442 records, `cc-by-nc-nd`)
- [eyepacs](./eyepacs.md): EyePACS — Diabetic Retinopathy Detection (Kaggle 2015) (88,702 records, `research-only`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (58,036 records, `mit`)
- [angioreport](./angioreport.md): AngioReport Fundus Angiography Report Dataset (55,361 records, `unknown`)
- [ffa_ir](./ffa_ir.md): FFA-IR Medical Report Dataset (47,247 records, `unknown`)
- [bidr](./bidr.md): BiDR: Diabetic Retinopathy Diagnosis Dataset (35,126 records, `unknown`)
