---
id: toxofundus
title: "ToxoFundus: Ocular Toxoplasmosis Fundus Dataset"
sidebar_label: toxofundus
description: "Fundus photographs for ocular toxoplasmosis detection: active toxoplasmosis, inactive (scarred) lesions, and normal. ~412 images total (adult + pediatric cases)."
tags: ["fundus", "cc-by", "kaggle", "classification", "resource-role-current-dataset", "dataset-family-toxofundus"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# ToxoFundus: Ocular Toxoplasmosis Fundus Dataset

Fundus photographs for ocular toxoplasmosis detection: active toxoplasmosis, inactive (scarred) lesions, and normal. ~412 images total (adult + pediatric cases).

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `toxofundus` |
| **Full name** | ToxoFundus: Ocular Toxoplasmosis Fundus Dataset |
| **First published** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Primary category** | `fundus` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `toxofundus` |
| **Contained modalities** | fundus |
| **Tasks** | classification |
| **Primary reported quantity** | 412 images |
| **Classes** | 3 (Normal, Active Toxoplasmosis, Inactive Toxoplasmosis) |
| **Splits** | train, test |
| **Size** | 0.2 GB |
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
| Primary | 412 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [kaggle.com/datasets](https://www.kaggle.com/datasets/nafin59/ocular-toxoplasmosis-fundus-images-dataset) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download toxofundus --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download toxofundus --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('toxofundus')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [kaggle.com/datasets](https://www.kaggle.com/datasets/nafin59/ocular-toxoplasmosis-fundus-images-dataset)

**Source-term evidence:** [kaggle.com/datasets](https://www.kaggle.com/datasets/nafin59/ocular-toxoplasmosis-fundus-images-dataset)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('toxofundus')
samples = ds.load(data_dir, split='test')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{toxofundus,
  title  = { ToxoFundus: Ocular Toxoplasmosis Fundus Dataset },
  note   = { Nafisi & Sadri, 'ToxoFundus: Ocular Toxoplasmosis Fundus Image Dataset', Data in Brief 2023. Zenodo: https://zenodo.org/records/5156953 — Kaggle: https://www.kaggle.com/datasets/nafin59/ocular-toxoplasmosis-fundus-images-dataset },
  year   = { 2023 },
  url    = { https://www.kaggle.com/datasets/nafin59/ocular-toxoplasmosis-fundus-images-dataset },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Nafisi & Sadri, 'ToxoFundus: Ocular Toxoplasmosis Fundus Image Dataset', Data in Brief 2023. Zenodo: https://zenodo.org/records/5156953 — Kaggle: https://www.kaggle.com/datasets/nafin59/ocular-toxoplasmosis-fundus-images-dataset
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
- [mfiddr](./mfiddr.md): MFIDDR: Multi-Field Imaging Dataset for Diabetic Retinopathy (34,452 images, `mit`)
