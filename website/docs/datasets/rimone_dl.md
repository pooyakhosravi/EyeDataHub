---
id: rimone_dl
title: "RIM-ONE DL"
sidebar_label: rimone_dl
description: "485 fundus images (313 normal, 172 glaucoma) with optic disc region of interest crops for deep learning."
tags: ["fundus", "cc-by", "kaggle", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# RIM-ONE DL

485 fundus images (313 normal, 172 glaucoma) with optic disc region of interest crops for deep learning.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `rimone_dl` |
| **Full name** | RIM-ONE DL |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | classification |
| **Primary reported quantity** | 485 images |
| **Classes** | 2 (Normal, Glaucoma) |
| **Splits** | train, test |
| **Size** | 0.5 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Kaggle |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Standard loader included |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 485 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [kaggle.com/datasets](https://www.kaggle.com/datasets/orvile/rim-one-retinal-dataset-for-assessing-glaucoma) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download rimone_dl --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download rimone_dl --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('rimone_dl')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [kaggle.com/datasets](https://www.kaggle.com/datasets/orvile/rim-one-retinal-dataset-for-assessing-glaucoma)

**Source-term evidence:** [kaggle.com/datasets](https://www.kaggle.com/datasets/orvile/rim-one-retinal-dataset-for-assessing-glaucoma)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('rimone_dl')
samples = ds.load(data_dir, split='test')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{rimone_dl,
  title  = { RIM-ONE DL },
  note   = { Fumero et al., 'RIM-ONE DL: A Unified Retinal Image Database for Assessing Glaucoma Using Deep Learning', Intl. Image Analysis and Ophthalmology 2020 },
  year   = { 2020 },
  url    = { https://www.kaggle.com/datasets/orvile/rim-one-retinal-dataset-for-assessing-glaucoma },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Fumero et al., 'RIM-ONE DL: A Unified Retinal Image Database for Assessing Glaucoma Using Deep Learning', Intl. Image Analysis and Ophthalmology 2020.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC BY 4.0
- **Normalized category:** `cc-by`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Standard label without an explicit NC clause; not a permission finding

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
