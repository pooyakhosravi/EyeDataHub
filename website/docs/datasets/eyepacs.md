---
id: eyepacs
title: "EyePACS — Diabetic Retinopathy Detection (Kaggle 2015)"
sidebar_label: eyepacs
description: "~88,000 fundus images graded 0–4 for DR severity. Largest public DR dataset; competition images from EyePACS clinics."
tags: ["fundus", "research-only", "kaggle", "grading", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# EyePACS — Diabetic Retinopathy Detection (Kaggle 2015)

~88,000 fundus images graded 0–4 for DR severity. Largest public DR dataset; competition images from EyePACS clinics.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `eyepacs` |
| **Full name** | EyePACS — Diabetic Retinopathy Detection (Kaggle 2015) |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | grading, classification |
| **Samples** | 88,702 |
| **Classes** | 5 (No DR, Mild, Moderate, Severe, Proliferative DR) |
| **Splits** | train, test |
| **Size** | 89.0 GB |
| **Source-stated terms** | Kaggle competition rules (non-commercial research) |
| **Normalized terms** | `research-only` |
| **Descriptive screening label** | Research or challenge restriction recorded; check source |
| **Terms scope** | `challenge_participation` |
| **Access friction** | `self_service_clickthrough` |
| **Route backend** | Kaggle |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Standard loader included |


## Notes

> Very large (~89 GB). Kaggle competition account and acceptance of rules required.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download eyepacs --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download eyepacs --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('eyepacs')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [kaggle.com/c](https://www.kaggle.com/c/diabetic-retinopathy-detection)

**Source-term evidence:** [kaggle.com/c](https://www.kaggle.com/c/diabetic-retinopathy-detection)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('eyepacs')
samples = ds.load(data_dir, split='test')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{eyepacs,
  title  = { EyePACS — Diabetic Retinopathy Detection (Kaggle 2015) },
  note   = { EyePACS / California Healthcare Foundation. 'Diabetic Retinopathy Detection', Kaggle Competition, 2015 },
  year   = { 2015 },
  url    = { https://www.kaggle.com/c/diabetic-retinopathy-detection },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
EyePACS / California Healthcare Foundation. 'Diabetic Retinopathy Detection', Kaggle Competition, 2015.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Kaggle competition rules (non-commercial research)
- **Normalized category:** `research-only`
- **Apparent scope:** `challenge_participation`
- **Descriptive screening label:** Research or challenge restriction recorded; check source

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Related datasets with shared modalities

- [airogs](./airogs.md): AIROGS: AI for Robust Glaucoma Screening (113,893 records, `cc-by-nc-nd`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 records, `unknown`)
- [justraigs](./justraigs.md): JustRAIGS: Just Referral AI Glaucoma Screening Dataset (101,442 records, `cc-by-nc-nd`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (58,036 records, `mit`)
- [angioreport](./angioreport.md): AngioReport Fundus Angiography Report Dataset (55,361 records, `unknown`)
- [ffa_ir](./ffa_ir.md): FFA-IR Medical Report Dataset (47,247 records, `unknown`)
- [bidr](./bidr.md): BiDR: Diabetic Retinopathy Diagnosis Dataset (35,126 records, `unknown`)
- [dr_arranged](./dr_arranged.md): Diabetic Retinopathy Arranged Dataset (Tianchi 93926) (35,126 records, `cc-by-nc-sa`)
