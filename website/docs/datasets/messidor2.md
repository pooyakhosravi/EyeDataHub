---
id: messidor2
title: "MESSIDOR-2"
sidebar_label: messidor2
description: "1748 fundus images with DR grading (0-3 Retinopathy Grade) and macular edema risk (0-2)."
tags: ["fundus", "research-only", "manual", "grading", "classification", "resource-role-current-dataset", "dataset-family-messidor2", "documented-relationship", "relationship-derived_from"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# MESSIDOR-2

1748 fundus images with DR grading (0-3 Retinopathy Grade) and macular edema risk (0-2).

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `messidor2` |
| **Full name** | MESSIDOR-2 |
| **Publication date** | Unknown |
| **Date basis** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Date notes** | - |
| **Primary category** | `fundus` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `messidor2` |
| **Contained modalities** | fundus |
| **Tasks** | grading, classification |
| **Primary reported quantity** | 1,748 images |
| **Classes** | 4 (Grade 0, Grade 1, Grade 2, Grade 3) |
| **Splits** | all |
| **Size** | 3.0 GB |
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
| Primary | 1,748 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [adcis.net/en](https://www.adcis.net/en/third-party/messidor2/) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Free registration required at adcis.net before downloading.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- [multieye](./multieye.md) is `derived from` this record: The MultiEYE paper names this record as one of the public fundus or OCT sources assembled for the benchmark. ([evidence](https://arxiv.org/abs/2412.09402))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download messidor2 --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download messidor2 --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('messidor2')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [adcis.net/en](https://www.adcis.net/en/third-party/messidor2/)

**Source-term evidence:** [adcis.net/en](https://www.adcis.net/en/third-party/messidor2/)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('messidor2')
samples = ds.load(data_dir, split='all')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{messidor2,
  title  = { MESSIDOR-2 },
  note   = { Decencière et al., 'Feedback on a publicly distributed image database: the Messidor database', Image Analysis & Stereology 2014 },
  year   = { 2014 },
  url    = { https://www.adcis.net/en/third-party/messidor2/ },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Decencière et al., 'Feedback on a publicly distributed image database: the Messidor database', Image Analysis & Stereology 2014.
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
