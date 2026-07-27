---
id: aptos2019
title: "APTOS 2019 Blindness Detection"
sidebar_label: aptos2019
description: "3662 fundus images from Aravind Eye Hospital, graded 0-4 for diabetic retinopathy severity."
tags: ["fundus", "unknown", "kaggle", "grading", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# APTOS 2019 Blindness Detection

3662 fundus images from Aravind Eye Hospital, graded 0-4 for diabetic retinopathy severity.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `aptos2019` |
| **Full name** | APTOS 2019 Blindness Detection |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | grading, classification |
| **Samples** | 3,662 |
| **Classes** | 5 (No DR, Mild, Moderate, Severe, Proliferative DR) |
| **Splits** | train |
| **Size** | 9.0 GB |
| **Source-stated terms** | Competition rules apply |
| **Normalized terms** | `unknown` |
| **Descriptive screening label** | Unknown or unclear; do not assume permission |
| **Terms scope** | `challenge_participation` |
| **Access friction** | `self_service_clickthrough` |
| **Route backend** | Kaggle |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Standard loader included |


## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download aptos2019 --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download aptos2019 --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('aptos2019')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [kaggle.com/c](https://www.kaggle.com/c/aptos2019-blindness-detection)

**Source-term evidence:** [kaggle.com/c](https://www.kaggle.com/c/aptos2019-blindness-detection)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('aptos2019')
samples = ds.load(data_dir, split='train')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{aptos2019,
  title  = { APTOS 2019 Blindness Detection },
  note   = { Karthik et al., APTOS 2019 Blindness Detection. Kaggle competition, 2019 },
  year   = { 2019 },
  url    = { https://www.kaggle.com/c/aptos2019-blindness-detection },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Karthik et al., APTOS 2019 Blindness Detection. Kaggle competition, 2019.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Competition rules apply
- **Normalized category:** `unknown`
- **Apparent scope:** `challenge_participation`
- **Descriptive screening label:** Unknown or unclear; do not assume permission

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
