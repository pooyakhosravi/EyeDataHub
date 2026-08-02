---
id: aod
title: "AOD: Augmented Ocular Diseases Dataset"
sidebar_label: aod
description: "Augmented ODIR-5K fundus photographs for 8-class ocular disease classification: Normal, Diabetes, Glaucoma, Cataract, AMD, Hypertension, Myopia, Other. Preprocessing includes CLAHE and standard augmen"
tags: ["fundus", "unknown", "kaggle", "classification", "documented-relationship", "relationship-derived_from"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# AOD: Augmented Ocular Diseases Dataset

Augmented ODIR-5K fundus photographs for 8-class ocular disease classification: Normal, Diabetes, Glaucoma, Cataract, AMD, Hypertension, Myopia, Other. Preprocessing includes CLAHE and standard augmentation.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `aod` |
| **Full name** | AOD: Augmented Ocular Diseases Dataset |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | classification |
| **Primary reported quantity** | 14,813 images |
| **Classes** | 8 (Normal, Diabetes, Glaucoma, Cataract, AMD, Hypertension, Myopia, Other) |
| **Splits** | train, test |
| **Size** | 2.0 GB |
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
| Primary | 14,813 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [kaggle.com/datasets](https://www.kaggle.com/datasets/nurmukhammed7/augemnted-ocular-diseases) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> OVERLAP: AOD is an augmented variant of ODIR-2019 (already in EyeDataHub as `odir2019`). Preprocessing (CLAHE) and augmentation explain the 14,813 vs 16,000 image count delta. Kept because the augmented split appears in downstream benchmarks separately.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- This record is `derived from` [odir2019](./odir2019.md): The AOD deposit describes an augmented and preprocessed ODIR-5K resource. ([evidence](https://doi.org/10.17632/d73g6m8d5m.1))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download aod --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download aod --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('aod')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [kaggle.com/datasets](https://www.kaggle.com/datasets/nurmukhammed7/augemnted-ocular-diseases)

**Source-term evidence:** [kaggle.com/datasets](https://www.kaggle.com/datasets/nurmukhammed7/augemnted-ocular-diseases)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('aod')
samples = ds.load(data_dir, split='test')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{aod,
  title  = { AOD: Augmented Ocular Diseases Dataset },
  note   = { AOD Dataset. Kaggle. https://www.kaggle.com/datasets/nurmukhammed7/augemnted-ocular-diseases },
  url    = { https://www.kaggle.com/datasets/nurmukhammed7/augemnted-ocular-diseases },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
AOD Dataset. Kaggle. https://www.kaggle.com/datasets/nurmukhammed7/augemnted-ocular-diseases
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
- [bidr](./bidr.md): BiDR: Diabetic Retinopathy Diagnosis Dataset (35,126 images, `unknown`)
