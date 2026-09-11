---
id: ravir
title: "RAVIR: Retinal Artery/Vein Segmentation in IR"
sidebar_label: ravir
description: "42 infrared reflectance fundus images with separate artery and vein segmentation masks. 23 train / 19 test."
tags: ["fundus", "research-only", "gdrive", "segmentation", "resource-role-current-dataset", "dataset-family-ravir"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# RAVIR: Retinal Artery/Vein Segmentation in IR

42 infrared reflectance fundus images with separate artery and vein segmentation masks. 23 train / 19 test.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `ravir` |
| **Full name** | RAVIR: Retinal Artery/Vein Segmentation in IR |
| **First published** | 2022-07 |
| **Publication date precision** | month |
| **Publication date evidence** | [ravirdataset.github.io/data](https://ravirdataset.github.io/data/) |
| **Publication date source field** | Official project page: News |
| **Publication date reviewed** | 2026-09-11 |
| **Primary category** | `fundus` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `ravir` |
| **Contained modalities** | fundus |
| **Tasks** | segmentation |
| **Primary reported quantity** | 42 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | train, test |
| **Size** | 0.05 GB |
| **Source-stated terms** | Research only |
| **Normalized terms** | `research-only` |
| **Descriptive screening label** | Research or challenge restriction recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Google Drive |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `loader_implemented_not_live_tested` |
| **Legacy sample-loader status** | Standard loader included |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 42 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [ravir.grand-challenge.org/data](https://ravir.grand-challenge.org/data/) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download ravir --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download ravir --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('ravir')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [ravir.grand-challenge.org/data](https://ravir.grand-challenge.org/data/)

**Source-term evidence:** [ravir.grand-challenge.org/data](https://ravir.grand-challenge.org/data/)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('ravir')
samples = ds.load(data_dir, split='test')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{ravir,
  title  = { RAVIR: Retinal Artery/Vein Segmentation in IR },
  note   = { Hatamizadeh et al., 'RAVIR: A Dataset and Methodology for the Semantic Segmentation and Quantitative Analysis of Retinal Arteries and Veins in Infrared Reflectance Imaging', JBHI 2022 },
  year   = { 2022 },
  url    = { https://ravir.grand-challenge.org/data/ },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Hatamizadeh et al., 'RAVIR: A Dataset and Methodology for the Semantic Segmentation and Quantitative Analysis of Retinal Arteries and Veins in Infrared Reflectance Imaging', JBHI 2022.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Research only
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
