---
id: lag
title: "LAG: Large-scale Attention-based Glaucoma Database"
sidebar_label: lag
description: "11,760 fundus images with glaucoma classification labels and ophthalmologist-derived attention maps. Largest public glaucoma dataset with attention ground truth."
tags: ["fundus", "research-only", "manual", "classification", "segmentation", "documented-relationship", "relationship-derived_from"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# LAG: Large-scale Attention-based Glaucoma Database

11,760 fundus images with glaucoma classification labels and ophthalmologist-derived attention maps. Largest public glaucoma dataset with attention ground truth.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `lag` |
| **Full name** | LAG: Large-scale Attention-based Glaucoma Database |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | classification, segmentation |
| **Primary reported quantity** | 11,760 images |
| **Classes** | 2 (normal, glaucoma) |
| **Splits** | train, test |
| **Size** | 3.0 GB |
| **Source-stated terms** | Research only (no redistribution; password by email) |
| **Normalized terms** | `research-only` |
| **Descriptive screening label** | Research or challenge restriction recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `author_contact` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `manual_access_blocked` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 11,760 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [github.com/smilell](https://github.com/smilell/AG-CNN) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Dropbox link gated by password — email liliu1995@buaa.edu.cn to request access. Cannot be auto-downloaded.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- [mm_retinal_reason](./mm_retinal_reason.md) is `derived from` this record: The version-pinned official dataset card lists this record among the CFP or OCT sources used to construct MM-Retinal-Reason. ([evidence](https://huggingface.co/datasets/lxirich/MM-Retinal-Reason/tree/d6243baa82c0914dba3c6f43ca79fdbf856982ef))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# This route requires upstream human action; no transfer starts.
eyehub download lag --data-dir ./data --dry-run --json
# Follow the official instructions shown by preflight.
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('lag')
print(preflight_dataset(ds, './data'))  # returns manual_access_blocked
```

  </TabItem>
</Tabs>

**Upstream page:** [github.com/smilell](https://github.com/smilell/AG-CNN)

**Source-term evidence:** [github.com/smilell](https://github.com/smilell/AG-CNN)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{lag,
  title  = { LAG: Large-scale Attention-based Glaucoma Database },
  note   = { Li et al., 'Attention Based Glaucoma Detection: A Large-scale Database and CNN Model', CVPR 2019 },
  year   = { 2019 },
  url    = { https://github.com/smilell/AG-CNN },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Li et al., 'Attention Based Glaucoma Detection: A Large-scale Database and CNN Model', CVPR 2019.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Research only (no redistribution; password by email)
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
- [bidr](./bidr.md): BiDR: Diabetic Retinopathy Diagnosis Dataset (35,126 images, `unknown`)
