---
id: e_ophtha
title: "E-ophtha (EX + MA): Exudate and Microaneurysm Segmentation"
sidebar_label: e_ophtha
description: "463 color fundus images with pixel-level segmentation: 82 with exudate (EX) + 381 with microaneurysm (MA) annotations. Standard DR lesion-segmentation benchmark."
tags: ["fundus", "research-only", "kaggle", "segmentation", "documented-relationship", "relationship-derived_from"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# E-ophtha (EX + MA): Exudate and Microaneurysm Segmentation

463 color fundus images with pixel-level segmentation: 82 with exudate (EX) + 381 with microaneurysm (MA) annotations. Standard DR lesion-segmentation benchmark.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `e_ophtha` |
| **Full name** | E-ophtha (EX + MA): Exudate and Microaneurysm Segmentation |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | segmentation |
| **Primary reported quantity** | 463 images |
| **Classes** | 2 (Not reported) |
| **Splits** | all |
| **Size** | 1.0 GB |
| **Source-stated terms** | Research only (TeleOphta project; Kaggle mirror) |
| **Normalized terms** | `research-only` |
| **Descriptive screening label** | Research or challenge restriction recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `controlled_or_manual` |
| **Route backend** | Kaggle |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `manual_access_blocked` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 463 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [kaggle.com/datasets](https://www.kaggle.com/datasets/samriddhibagchi/e-ophtha-diabetic-retinopathy-datasets-ex-ma) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Official source (ADCIS) requires a request form. EyeDataHub uses the Kaggle community mirror. Verify license terms with the original ADCIS distribution before commercial use.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- [dme_vqa](./dme_vqa.md) is `derived from` this record: The DME VQA deposit identifies e-ophtha images as source material. ([evidence](https://zenodo.org/records/6784358))
- [mm_retinal_reason](./mm_retinal_reason.md) is `derived from` this record: The version-pinned official dataset card lists this record among the CFP or OCT sources used to construct MM-Retinal-Reason. ([evidence](https://huggingface.co/datasets/lxirich/MM-Retinal-Reason/tree/d6243baa82c0914dba3c6f43ca79fdbf856982ef))

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# This route requires upstream human action; no transfer starts.
eyehub download e_ophtha --data-dir ./data --dry-run --json
# Follow the official instructions shown by preflight.
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('e_ophtha')
print(preflight_dataset(ds, './data'))  # returns manual_access_blocked
```

  </TabItem>
</Tabs>

**Upstream page:** [kaggle.com/datasets](https://www.kaggle.com/datasets/samriddhibagchi/e-ophtha-diabetic-retinopathy-datasets-ex-ma)

**Source-term evidence:** [kaggle.com/datasets](https://www.kaggle.com/datasets/samriddhibagchi/e-ophtha-diabetic-retinopathy-datasets-ex-ma)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{e_ophtha,
  title  = { E-ophtha (EX + MA): Exudate and Microaneurysm Segmentation },
  note   = { Decencière et al., 'TeleOphta: Machine Learning and Image Processing Methods for Teleophthalmology', IRBM 2013 },
  year   = { 2013 },
  url    = { https://www.kaggle.com/datasets/samriddhibagchi/e-ophtha-diabetic-retinopathy-datasets-ex-ma },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Decencière et al., 'TeleOphta: Machine Learning and Image Processing Methods for Teleophthalmology', IRBM 2013.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Research only (TeleOphta project; Kaggle mirror)
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
