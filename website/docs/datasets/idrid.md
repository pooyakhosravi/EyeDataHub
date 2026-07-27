---
id: idrid
title: "IDRiD: Indian Diabetic Retinopathy Image Dataset"
sidebar_label: idrid
description: "516 fundus images with DR grade (0-4), macular edema grade (0-2), and pixel-level lesion segmentation for 81 images."
tags: ["fundus", "cc-by", "manual", "grading", "classification", "segmentation"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# IDRiD: Indian Diabetic Retinopathy Image Dataset

516 fundus images with DR grade (0-4), macular edema grade (0-2), and pixel-level lesion segmentation for 81 images.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `idrid` |
| **Full name** | IDRiD: Indian Diabetic Retinopathy Image Dataset |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | grading, classification, segmentation |
| **Samples** | 516 |
| **Classes** | 5 (Grade 0, Grade 1, Grade 2, Grade 3, Grade 4) |
| **Splits** | train, test |
| **Size** | 2.5 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `guided_instructions_only` |
| **Legacy sample-loader status** | Standard loader included |


## Notes

> Requires IEEE DataPort account (free).

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download idrid --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download idrid --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('idrid')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [ieee-dataport.org/open-access](https://ieee-dataport.org/open-access/indian-diabetic-retinopathy-image-dataset-idrid)

**Source-term evidence:** [ieee-dataport.org/open-access](https://ieee-dataport.org/open-access/indian-diabetic-retinopathy-image-dataset-idrid)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('idrid')
samples = ds.load(data_dir, split='test')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{idrid,
  title  = { IDRiD: Indian Diabetic Retinopathy Image Dataset },
  note   = { Porwal et al., 'Indian diabetic retinopathy image dataset (IDRiD): A database for diabetic retinopathy screening research', Data 2018 },
  year   = { 2018 },
  url    = { https://ieee-dataport.org/open-access/indian-diabetic-retinopathy-image-dataset-idrid },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Porwal et al., 'Indian diabetic retinopathy image dataset (IDRiD): A database for diabetic retinopathy screening research', Data 2018.
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
