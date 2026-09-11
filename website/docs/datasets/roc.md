---
id: roc
title: "ROC: Retinopathy Online Challenge"
sidebar_label: roc
description: "100 fundus images with microaneurysm annotations from the Retinopathy Online Challenge."
tags: ["fundus", "research-only", "manual", "segmentation", "classification", "resource-role-current-dataset", "dataset-family-roc", "documented-relationship", "relationship-derived_from"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# ROC: Retinopathy Online Challenge

100 fundus images with microaneurysm annotations from the Retinopathy Online Challenge.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `roc` |
| **Full name** | ROC: Retinopathy Online Challenge |
| **Publication date** | Unknown |
| **Date basis** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Date notes** | - |
| **Primary category** | `fundus` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `roc` |
| **Contained modalities** | fundus |
| **Tasks** | segmentation, classification |
| **Primary reported quantity** | 100 images |
| **Classes** | 2 (Not reported) |
| **Splits** | train, test |
| **Size** | 0.3 GB |
| **Source-stated terms** | Research only (free for research, University of Iowa) |
| **Normalized terms** | `research-only` |
| **Descriptive screening label** | Research or challenge restriction recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `guided_instructions_only` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 100 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [webeye.ophth.uiowa.edu/ROC](http://webeye.ophth.uiowa.edu/ROC/) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> University of Iowa registration form required — no auto path.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- [mm_retinal_reason](./mm_retinal_reason.md) is `derived from` this record: The version-pinned official dataset card lists this record among the CFP or OCT sources used to construct MM-Retinal-Reason. ([evidence](https://huggingface.co/datasets/lxirich/MM-Retinal-Reason/tree/d6243baa82c0914dba3c6f43ca79fdbf856982ef))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download roc --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download roc --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('roc')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [webeye.ophth.uiowa.edu/ROC](http://webeye.ophth.uiowa.edu/ROC/)

**Source-term evidence:** [webeye.ophth.uiowa.edu/ROC](http://webeye.ophth.uiowa.edu/ROC/)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{roc,
  title  = { ROC: Retinopathy Online Challenge },
  note   = { Niemeijer et al., 'Retinopathy Online Challenge: Automatic Detection of Microaneurysms in Digital Color Fundus Photographs', IEEE TMI 2010 },
  year   = { 2010 },
  url    = { http://webeye.ophth.uiowa.edu/ROC/ },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Niemeijer et al., 'Retinopathy Online Challenge: Automatic Detection of Microaneurysms in Digital Color Fundus Photographs', IEEE TMI 2010.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Research only (free for research, University of Iowa)
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
