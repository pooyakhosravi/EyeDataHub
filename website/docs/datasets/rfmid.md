---
id: rfmid
title: "RFMiD: Retinal Fundus Multi-disease Image Dataset"
sidebar_label: rfmid
description: "3200 fundus images annotated for 45 retinal conditions. Used for multi-label disease classification."
tags: ["fundus", "cc-by-sa", "kaggle", "multilabel", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# RFMiD: Retinal Fundus Multi-disease Image Dataset

3200 fundus images annotated for 45 retinal conditions. Used for multi-label disease classification.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `rfmid` |
| **Full name** | RFMiD: Retinal Fundus Multi-disease Image Dataset |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | multilabel, classification |
| **Samples** | 3,200 |
| **Classes** | 29 (Disease_Risk, DR, ARMD, MH, DN, MYA, BRVO, TSLN, ERM, LS, MS, CSR, ODC, CRVO, TV, AH, ODP, ODE, ST, AION, PT, RT, RS, CRS, EDN, RPEC, MHL, RP, other) |
| **Splits** | train, val, test |
| **Size** | 1.5 GB |
| **Source-stated terms** | CC BY-SA 4.0 |
| **Normalized terms** | `cc-by-sa` |
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
eyehub download rfmid --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download rfmid --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('rfmid')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [kaggle.com/datasets](https://www.kaggle.com/datasets/andrewmvd/retinal-disease-classification)

**Source-term evidence:** [kaggle.com/datasets](https://www.kaggle.com/datasets/andrewmvd/retinal-disease-classification)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('rfmid')
samples = ds.load(data_dir, split='test')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{rfmid,
  title  = { RFMiD: Retinal Fundus Multi-disease Image Dataset },
  note   = { Pachade et al., 'Retinal Fundus Multi-disease Image Dataset (RFMiD): A Dataset for Multi-Disease Detection Research', Data 2021 },
  year   = { 2021 },
  url    = { https://www.kaggle.com/datasets/andrewmvd/retinal-disease-classification },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Pachade et al., 'Retinal Fundus Multi-disease Image Dataset (RFMiD): A Dataset for Multi-Disease Detection Research', Data 2021.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC BY-SA 4.0
- **Normalized category:** `cc-by-sa`
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
