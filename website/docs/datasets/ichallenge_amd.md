---
id: ichallenge_amd
title: "iChallenge-AMD: Age-related Macular Degeneration"
sidebar_label: ichallenge_amd
description: "400 training fundus images with AMD classification (non-AMD vs AMD) and lesion annotations. Challenge dataset from ISBI 2020."
tags: ["fundus", "research-only", "manual", "classification", "resource-role-current-dataset", "dataset-family-ichallenge-amd"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# iChallenge-AMD: Age-related Macular Degeneration

400 training fundus images with AMD classification (non-AMD vs AMD) and lesion annotations. Challenge dataset from ISBI 2020.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `ichallenge_amd` |
| **Full name** | iChallenge-AMD: Age-related Macular Degeneration |
| **Primary category** | `fundus` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `ichallenge_amd` |
| **Contained modalities** | fundus |
| **Tasks** | classification |
| **Primary reported quantity** | 400 images |
| **Classes** | 2 (Non-AMD, AMD) |
| **Splits** | train, test |
| **Size** | 1.5 GB |
| **Source-stated terms** | Research only — requires registration |
| **Normalized terms** | `research-only` |
| **Descriptive screening label** | Research or challenge restriction recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `guided_instructions_only` |
| **Legacy sample-loader status** | Standard loader included |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 400 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [amd.grand-challenge.org/download](https://amd.grand-challenge.org/download/) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Grand Challenge login is required:
>   https://amd.grand-challenge.org/download/
> The original Baidu BROAD portal has returned intermittent 5xx errors since 2024. Alternative partial resource:
> - PaddleSeg optic-disc subset (~19 MB, direct HTTPS, no login): https://paddleseg.bj.bcebos.com/dataset/optic_disc_seg.zip
> The full 1.5 GB dataset is only via Grand Challenge or the Baidu portal.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download ichallenge_amd --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download ichallenge_amd --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('ichallenge_amd')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [amd.grand-challenge.org/download](https://amd.grand-challenge.org/download/)

**Source-term evidence:** [amd.grand-challenge.org/download](https://amd.grand-challenge.org/download/)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('ichallenge_amd')
samples = ds.load(data_dir, split='test')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{ichallenge_amd,
  title  = { iChallenge-AMD: Age-related Macular Degeneration },
  note   = { Fu et al., 'Age-Related Macular Degeneration and Pathologic Myopia Fundus Image Analysis Challenge', ISBI 2020 },
  year   = { 2020 },
  url    = { https://amd.grand-challenge.org/download/ },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Fu et al., 'Age-Related Macular Degeneration and Pathologic Myopia Fundus Image Analysis Challenge', ISBI 2020.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Research only — requires registration
- **Normalized category:** `research-only`
- **Apparent scope:** `dataset_files`
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
