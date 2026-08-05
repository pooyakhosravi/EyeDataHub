---
id: adam_challenge
title: "ADAM — Automatic Detection of AMD Challenge"
sidebar_label: adam_challenge
description: "1200 fundus images for AMD classification, five-class lesion segmentation, fovea/optic disc localisation."
tags: ["fundus", "research-only", "gdrive", "classification", "segmentation", "resource-role-current-dataset", "dataset-family-adam-challenge"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# ADAM — Automatic Detection of AMD Challenge

1200 fundus images for AMD classification, five-class lesion segmentation, fovea/optic disc localisation.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `adam_challenge` |
| **Full name** | ADAM — Automatic Detection of AMD Challenge |
| **Primary category** | `fundus` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `adam_challenge` |
| **Contained modalities** | fundus |
| **Tasks** | classification, segmentation |
| **Primary reported quantity** | 1,200 images |
| **Classes** | 2 (non-AMD, AMD) |
| **Splits** | train, val, test |
| **Size** | 1.5 GB |
| **Source-stated terms** | Challenge data-use agreement (IEEE DataPort) |
| **Normalized terms** | `research-only` |
| **Descriptive screening label** | Research or challenge restriction recorded; check source |
| **Terms scope** | `challenge_participation` |
| **Access friction** | `controlled_or_manual` |
| **Route backend** | Google Drive |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `manual_access_blocked` |
| **Legacy sample-loader status** | Standard loader included |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 1,200 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [drive.google.com/file](https://drive.google.com/file/d/1Uz5x0aqXb0aecjzNWQ4522oCxaRDZxBt/view) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# This route requires upstream human action; no transfer starts.
eyehub download adam_challenge --data-dir ./data --dry-run --json
# Follow the official instructions shown by preflight.
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('adam_challenge')
print(preflight_dataset(ds, './data'))  # returns manual_access_blocked
```

  </TabItem>
</Tabs>

**Upstream page:** [drive.google.com/file](https://drive.google.com/file/d/1Uz5x0aqXb0aecjzNWQ4522oCxaRDZxBt/view)

**Source-term evidence:** [drive.google.com/file](https://drive.google.com/file/d/1Uz5x0aqXb0aecjzNWQ4522oCxaRDZxBt/view)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('adam_challenge')
samples = ds.load(data_dir, split='test')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{adam_challenge,
  title  = { ADAM — Automatic Detection of AMD Challenge },
  note   = { Fang H. et al., 'ADAM Challenge: Detecting AMD from Fundus Images', IEEE TMI 2022 },
  year   = { 2022 },
  url    = { https://drive.google.com/file/d/1Uz5x0aqXb0aecjzNWQ4522oCxaRDZxBt/view },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Fang H. et al., 'ADAM Challenge: Detecting AMD from Fundus Images', IEEE TMI 2022.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Challenge data-use agreement (IEEE DataPort)
- **Normalized category:** `research-only`
- **Apparent scope:** `challenge_participation`
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
