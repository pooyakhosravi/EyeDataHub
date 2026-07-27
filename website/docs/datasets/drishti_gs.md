---
id: drishti_gs
title: "DRISHTI-GS: Optic Disc and Cup Segmentation"
sidebar_label: drishti_gs
description: "101 fundus images annotated for optic disc and cup segmentation by 4 clinicians. Train/test: 50/51."
tags: ["fundus", "research-only", "kaggle", "segmentation"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# DRISHTI-GS: Optic Disc and Cup Segmentation

101 fundus images annotated for optic disc and cup segmentation by 4 clinicians. Train/test: 50/51.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `drishti_gs` |
| **Full name** | DRISHTI-GS: Optic Disc and Cup Segmentation |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | segmentation |
| **Samples** | 101 |
| **Classes** | Not reported (Not reported) |
| **Splits** | train, test |
| **Size** | 0.8 GB |
| **Source-stated terms** | Research only |
| **Normalized terms** | `research-only` |
| **Descriptive screening label** | Research or challenge restriction recorded; check source |
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
eyehub download drishti_gs --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download drishti_gs --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('drishti_gs')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [kaggle.com/datasets](https://www.kaggle.com/datasets/lokeshsaipureddi/drishtigs-retina-dataset-for-onh-segmentation)

**Source-term evidence:** [kaggle.com/datasets](https://www.kaggle.com/datasets/lokeshsaipureddi/drishtigs-retina-dataset-for-onh-segmentation)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('drishti_gs')
samples = ds.load(data_dir, split='test')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{drishti_gs,
  title  = { DRISHTI-GS: Optic Disc and Cup Segmentation },
  note   = { Sivaswamy et al., 'Drishti-GS: Retinal image dataset for optic nerve head (ONH) segmentation', ISBI 2014 },
  year   = { 2014 },
  url    = { https://www.kaggle.com/datasets/lokeshsaipureddi/drishtigs-retina-dataset-for-onh-segmentation },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Sivaswamy et al., 'Drishti-GS: Retinal image dataset for optic nerve head (ONH) segmentation', ISBI 2014.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Research only
- **Normalized category:** `research-only`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Research or challenge restriction recorded; check source

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
