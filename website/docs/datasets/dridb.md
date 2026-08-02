---
id: dridb
title: "DRiDB: Diabetic Retinopathy Image Database"
sidebar_label: dridb
description: "Fifty color fundus images with expert markings of diabetic retinopathy lesions, blood vessels, optic disc, and macula."
tags: ["fundus", "research-only", "manual", "segmentation", "lesion_detection", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# DRiDB: Diabetic Retinopathy Image Database

Fifty color fundus images with expert markings of diabetic retinopathy lesions, blood vessels, optic disc, and macula.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dridb` |
| **Full name** | DRiDB: Diabetic Retinopathy Image Database |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | segmentation, lesion_detection, classification |
| **Primary reported quantity** | 50 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | Research only: free for research and educational purposes; copying, redistribution, and unauthorized commercial use prohibited |
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
| Primary | 50 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [ipg.fer.hr/ipg](https://ipg.fer.hr/ipg/resources/image_database) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Access is requested by email from the official University of Zagreb page. The page requires citation of the listed paper when results use the dataset.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# This route requires upstream human action; no transfer starts.
eyehub download dridb --data-dir ./data --dry-run --json
# Follow the official instructions shown by preflight.
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dridb')
print(preflight_dataset(ds, './data'))  # returns manual_access_blocked
```

  </TabItem>
</Tabs>

**Upstream page:** [ipg.fer.hr/ipg](https://ipg.fer.hr/ipg/resources/image_database)

**Source-term evidence:** [ipg.fer.hr/ipg](https://ipg.fer.hr/ipg/resources/image_database)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dridb,
  title  = { DRiDB: Diabetic Retinopathy Image Database },
  note   = { Prentasic P, Loncaric S, Vatavuk Z, et al. Diabetic retinopathy image database (DRiDB): A new database for diabetic retinopathy screening programs research. ISPA. 2013:704-709. doi:10.1109/ISPA.2013.6703830 },
  year   = { 2013 },
  url    = { https://ipg.fer.hr/ipg/resources/image_database },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Prentasic P, Loncaric S, Vatavuk Z, et al. Diabetic retinopathy image database (DRiDB): A new database for diabetic retinopathy screening programs research. ISPA. 2013:704-709. doi:10.1109/ISPA.2013.6703830
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Research only: free for research and educational purposes; copying, redistribution, and unauthorized commercial use prohibited
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
