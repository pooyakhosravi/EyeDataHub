---
id: cataract
title: "Cataract Fundus Classification Dataset"
sidebar_label: cataract
description: "601 fundus images in 4 classes: Normal, Cataract, Glaucoma, and Retina Disease. Intended for ocular disease classification."
tags: ["fundus", "unknown", "kaggle", "classification", "resource-role-current-dataset", "dataset-family-cataract"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Cataract Fundus Classification Dataset

601 fundus images in 4 classes: Normal, Cataract, Glaucoma, and Retina Disease. Intended for ocular disease classification.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `cataract` |
| **Full name** | Cataract Fundus Classification Dataset |
| **Primary category** | `fundus` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `cataract` |
| **Contained modalities** | fundus |
| **Tasks** | classification |
| **Primary reported quantity** | 601 images |
| **Classes** | 4 (Normal, Cataract, Glaucoma, Retina Disease) |
| **Splits** | train |
| **Size** | 0.1 GB |
| **Source-stated terms** | See Kaggle dataset page |
| **Normalized terms** | `unknown` |
| **Descriptive screening label** | Unknown or unclear; do not assume permission |
| **Terms scope** | `unknown` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Kaggle |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Standard loader included |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 601 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [kaggle.com/datasets](https://www.kaggle.com/datasets/jr2ngb/cataractdataset) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download cataract --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download cataract --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('cataract')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [kaggle.com/datasets](https://www.kaggle.com/datasets/jr2ngb/cataractdataset)

**Source-term evidence:** [kaggle.com/datasets](https://www.kaggle.com/datasets/jr2ngb/cataractdataset)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('cataract')
samples = ds.load(data_dir, split='train')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{cataract,
  title  = { Cataract Fundus Classification Dataset },
  note   = { Kaggle dataset by jr2ngb (2019). https://www.kaggle.com/datasets/jr2ngb/cataractdataset },
  year   = { 2019 },
  url    = { https://www.kaggle.com/datasets/jr2ngb/cataractdataset },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Kaggle dataset by jr2ngb (2019). https://www.kaggle.com/datasets/jr2ngb/cataractdataset
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** See Kaggle dataset page
- **Normalized category:** `unknown`
- **Apparent scope:** `unknown`
- **Descriptive screening label:** Unknown or unclear; do not assume permission

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
