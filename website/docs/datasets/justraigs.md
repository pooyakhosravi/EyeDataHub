---
id: justraigs
title: "JustRAIGS: Just Referral AI Glaucoma Screening Dataset"
sidebar_label: justraigs
description: "101,442 gradable fundus images labeled as referable (RG) or non-referable (NRG) for glaucoma. Image data from EyePACS LLC; labels from Rotterdam Eye Hospital expert graders."
tags: ["fundus", "cc-by-nc-nd", "zenodo", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# JustRAIGS: Just Referral AI Glaucoma Screening Dataset

101,442 gradable fundus images labeled as referable (RG) or non-referable (NRG) for glaucoma. Image data from EyePACS LLC; labels from Rotterdam Eye Hospital expert graders.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `justraigs` |
| **Full name** | JustRAIGS: Just Referral AI Glaucoma Screening Dataset |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | classification |
| **Primary reported quantity** | 101,442 images |
| **Classes** | 2 (No Referable Glaucoma, Referable Glaucoma) |
| **Splits** | train |
| **Size** | 100.0 GB |
| **Source-stated terms** | CC BY-NC-ND 4.0 |
| **Normalized terms** | `cc-by-nc-nd` |
| **Descriptive screening label** | Explicit noncommercial clause recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_clickthrough` |
| **Route backend** | Zenodo |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Standard loader included |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 101,442 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [zenodo.org/records](https://zenodo.org/records/10035093) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Large dataset (~100 GB). The record is publicly accessible but downloading requires accepting the CC BY-NC-ND terms on the Zenodo page. Set ZENODO_TOKEN in .env if access is denied.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download justraigs --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download justraigs --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('justraigs')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [zenodo.org/records](https://zenodo.org/records/10035093)

**Source-term evidence:** [zenodo.org/records](https://zenodo.org/records/10035093)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('justraigs')
samples = ds.load(data_dir, split='train')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{justraigs,
  title  = { JustRAIGS: Just Referral AI Glaucoma Screening Dataset },
  note   = { Thakoor et al., 'JustRAIGS: Justify Your Artificial Intelligence Prediction for Referable or Not Referable Glaucoma Screening', MICCAI 2023. Zenodo: https://zenodo.org/records/10035093 },
  year   = { 2023 },
  url    = { https://zenodo.org/records/10035093 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Thakoor et al., 'JustRAIGS: Justify Your Artificial Intelligence Prediction for Referable or Not Referable Glaucoma Screening', MICCAI 2023. Zenodo: https://zenodo.org/records/10035093
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC BY-NC-ND 4.0
- **Normalized category:** `cc-by-nc-nd`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Explicit noncommercial clause recorded; check source

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [airogs](./airogs.md): AIROGS: AI for Robust Glaucoma Screening (113,893 images, `cc-by-nc-nd`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (103,959 images, `mit`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [eyepacs](./eyepacs.md): EyePACS — Diabetic Retinopathy Detection (Kaggle 2015) (88,702 images, `research-only`)
- [angioreport](./angioreport.md): AngioReport Fundus Angiography Report Dataset (55,361 images, `unknown`)
- [ffa_ir](./ffa_ir.md): FFA-IR Medical Report Dataset (47,247 images, `unknown`)
- [bidr](./bidr.md): BiDR: Diabetic Retinopathy Diagnosis Dataset (35,126 images, `unknown`)
- [dr_arranged](./dr_arranged.md): Diabetic Retinopathy Arranged Dataset (Tianchi 93926) (35,126 images, `cc-by-nc-sa`)
