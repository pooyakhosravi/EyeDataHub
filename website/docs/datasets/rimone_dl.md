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
| **Samples** | 485 |
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


## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download rimone_dl --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download rimone_dl --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('rimone_dl')
print(preflight_dataset(ds, './data'))  # no transfer
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

## Related datasets with shared modalities

- [airogs](./airogs.md): AIROGS: AI for Robust Glaucoma Screening (113,893 records, `cc-by-nc-nd`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 records, `unknown`)
- [justraigs](./justraigs.md): JustRAIGS: Just Referral AI Glaucoma Screening Dataset (101,442 records, `cc-by-nc-nd`)
- [eyepacs](./eyepacs.md): EyePACS — Diabetic Retinopathy Detection (Kaggle 2015) (88,702 records, `research-only`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (58,036 records, `mit`)
- [angioreport](./angioreport.md): AngioReport Fundus Angiography Report Dataset (55,361 records, `unknown`)
- [ffa_ir](./ffa_ir.md): FFA-IR Medical Report Dataset (47,247 records, `unknown`)
- [bidr](./bidr.md): BiDR: Diabetic Retinopathy Diagnosis Dataset (35,126 records, `unknown`)
