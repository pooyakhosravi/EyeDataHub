---
id: maples_dr
title: "MAPLES-DR: Montreal Annotation Project for DR"
sidebar_label: maples_dr
description: "198 fundus images (from MESSIDOR) with pixel-wise segmentation for 10 biomarkers (lesions + structures) + DR and ME severity grades."
tags: ["fundus", "cc-by", "figshare", "segmentation", "grading", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# MAPLES-DR: Montreal Annotation Project for DR

198 fundus images (from MESSIDOR) with pixel-wise segmentation for 10 biomarkers (lesions + structures) + DR and ME severity grades.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `maples_dr` |
| **Full name** | MAPLES-DR: Montreal Annotation Project for DR |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | segmentation, grading, classification |
| **Primary reported quantity** | 198 images |
| **Classes** | 5 (No DR, Mild DR, Moderate DR, Severe DR, PDR) |
| **Splits** | train, test |
| **Size** | 0.5 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Figshare |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Standard loader included |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 198 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [https://doi.org/10.6084/m9.figshare.24328660](https://doi.org/10.6084/m9.figshare.24328660) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Segmentation maps for 10 retinal biomarkers.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download maples_dr --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download maples_dr --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('maples_dr')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.6084/m9.figshare.24328660](https://doi.org/10.6084/m9.figshare.24328660)

**Source-term evidence:** [https://doi.org/10.6084/m9.figshare.24328660](https://doi.org/10.6084/m9.figshare.24328660)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('maples_dr')
samples = ds.load(data_dir, split='test')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{maples_dr,
  title  = { MAPLES-DR: Montreal Annotation Project for DR },
  note   = { Morin et al., 'MAPLES-DR: MESSIDOR Annotation Project for Lesion and Structures Evaluation in Diabetic Retinopathy', Scientific Data 2024 },
  year   = { 2024 },
  url    = { https://doi.org/10.6084/m9.figshare.24328660 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Morin et al., 'MAPLES-DR: MESSIDOR Annotation Project for Lesion and Structures Evaluation in Diabetic Retinopathy', Scientific Data 2024.
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
- [bidr](./bidr.md): BiDR: Diabetic Retinopathy Diagnosis Dataset (35,126 images, `unknown`)
