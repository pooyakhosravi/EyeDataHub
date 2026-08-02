---
id: farfum_rop
title: "FARFUM-ROP: Fundus Annotation Repository for Retinopathy of Prematurity"
sidebar_label: farfum_rop
description: "Wide-field fundus images from premature infants for ROP staging (Stages 1–5 + Plus Disease). Expert-annotated for AI-assisted ROP diagnosis and screening."
tags: ["fundus", "cc-by", "figshare", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# FARFUM-ROP: Fundus Annotation Repository for Retinopathy of Prematurity

Wide-field fundus images from premature infants for ROP staging (Stages 1–5 + Plus Disease). Expert-annotated for AI-assisted ROP diagnosis and screening.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `farfum_rop` |
| **Full name** | FARFUM-ROP: Fundus Annotation Repository for Retinopathy of Prematurity |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | classification |
| **Primary reported quantity** | 1,533 images |
| **Classes** | 3 (Normal, Pre-Plus, Plus) |
| **Splits** | train, test |
| **Size** | 1.0 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Figshare |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `end_to_end_tested` |
| **Legacy sample-loader status** | Standard loader included |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 1,533 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [https://doi.org/10.6084/m9.figshare.c.6721269](https://doi.org/10.6084/m9.figshare.c.6721269) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download farfum_rop --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download farfum_rop --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('farfum_rop')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.6084/m9.figshare.c.6721269](https://doi.org/10.6084/m9.figshare.c.6721269)

**Source-term evidence:** [https://doi.org/10.6084/m9.figshare.c.6721269](https://doi.org/10.6084/m9.figshare.c.6721269)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('farfum_rop')
samples = ds.load(data_dir, split='test')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{farfum_rop,
  title  = { FARFUM-ROP: Fundus Annotation Repository for Retinopathy of Prematurity },
  note   = { Riazi-Esfahani H et al., 'FARFUM-RoP: A dataset for machine learning-based plus disease diagnosis in retinopathy of prematurity', Scientific Data 2024. https://doi.org/10.6084/m9.figshare.c.6721269 },
  year   = { 2024 },
  url    = { https://doi.org/10.6084/m9.figshare.c.6721269 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Riazi-Esfahani H et al., 'FARFUM-RoP: A dataset for machine learning-based plus disease diagnosis in retinopathy of prematurity', Scientific Data 2024. https://doi.org/10.6084/m9.figshare.c.6721269
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
