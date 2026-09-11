---
id: fire
title: "FIRE: Fundus Image Registration Dataset"
sidebar_label: fire
description: "129 fundus images from 39 patients forming 134 registration pairs with anatomical ground-truth control points. Only public registration benchmark for ophthalmology."
tags: ["fundus", "research-only", "direct", "regression", "resource-role-current-dataset", "dataset-family-fire"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# FIRE: Fundus Image Registration Dataset

129 fundus images from 39 patients forming 134 registration pairs with anatomical ground-truth control points. Only public registration benchmark for ophthalmology.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `fire` |
| **Full name** | FIRE: Fundus Image Registration Dataset |
| **First published** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Primary category** | `fundus` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `fire` |
| **Contained modalities** | fundus |
| **Tasks** | regression |
| **Primary reported quantity** | 129 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 1.0 GB |
| **Source-stated terms** | Research only (FORTH CVRL) |
| **Normalized terms** | `research-only` |
| **Descriptive screening label** | Research or challenge restriction recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Direct HTTP |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `end_to_end_tested` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 129 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [projects.ics.forth.gr/cvrl](https://projects.ics.forth.gr/cvrl/fire/) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Distributed as a 7z archive. EyeDataHub validates archive member paths before extracting it.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download fire --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download fire --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('fire')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [projects.ics.forth.gr/cvrl](https://projects.ics.forth.gr/cvrl/fire/)

**Source-term evidence:** [projects.ics.forth.gr/cvrl](https://projects.ics.forth.gr/cvrl/fire/)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{fire,
  title  = { FIRE: Fundus Image Registration Dataset },
  note   = { Hernandez-Matas et al., 'FIRE: Fundus Image Registration Dataset', Journal of Modeling in Ophthalmology 2017 },
  year   = { 2017 },
  url    = { https://projects.ics.forth.gr/cvrl/fire/ },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Hernandez-Matas et al., 'FIRE: Fundus Image Registration Dataset', Journal of Modeling in Ophthalmology 2017.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Research only (FORTH CVRL)
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
