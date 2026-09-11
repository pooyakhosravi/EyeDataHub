---
id: acrima
title: "ACRIMA: Glaucoma Optic Disc Fundus Database"
sidebar_label: acrima
description: "705 optic disc-centred fundus photographs (396 normal + 309 glaucoma) from Hospital Clinico San Carlos. Expert-annotated binary glaucoma classification."
tags: ["fundus", "cc-by", "figshare", "classification", "resource-role-current-dataset", "dataset-family-acrima", "documented-relationship", "relationship-derived_from"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# ACRIMA: Glaucoma Optic Disc Fundus Database

705 optic disc-centred fundus photographs (396 normal + 309 glaucoma) from Hospital Clinico San Carlos. Expert-annotated binary glaucoma classification.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `acrima` |
| **Full name** | ACRIMA: Glaucoma Optic Disc Fundus Database |
| **First published** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Primary category** | `fundus` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `acrima` |
| **Contained modalities** | fundus |
| **Tasks** | classification |
| **Primary reported quantity** | 705 images |
| **Classes** | 2 (Normal, Glaucoma) |
| **Splits** | train |
| **Size** | 0.5 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Figshare |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `guided_instructions_only` |
| **Legacy sample-loader status** | Standard loader included |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 705 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [Figshare private-share page](https://figshare.com/s/c2d31f850af14c5b5232) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- [higancnn_generated_glaucoma](./higancnn_generated_glaucoma.md) is `derived from` this record: The official dataset description names ACRIMA, DRISHTI-GS, and HRF among the human fundus sources used to construct the synthetic glaucoma resource. ([evidence](https://www.kaggle.com/datasets/hindsaud/datasets-higancnn-glaucoma-detection))
- [mm_retinal_reason](./mm_retinal_reason.md) is `derived from` this record: The version-pinned official dataset card lists this record among the CFP or OCT sources used to construct MM-Retinal-Reason. ([evidence](https://huggingface.co/datasets/lxirich/MM-Retinal-Reason/tree/d6243baa82c0914dba3c6f43ca79fdbf856982ef))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download acrima --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download acrima --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('acrima')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [Figshare private-share page](https://figshare.com/s/c2d31f850af14c5b5232)

**Source-term evidence:** [Figshare private-share page](https://figshare.com/s/c2d31f850af14c5b5232)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('acrima')
samples = ds.load(data_dir, split='train')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{acrima,
  title  = { ACRIMA: Glaucoma Optic Disc Fundus Database },
  note   = { Diaz-Pinto et al., 'Retinal Image Synthesis and Semi-Supervised Learning for Glaucoma Assessment', IEEE TMI 2019. Data: https://figshare.com/s/c2d31f850af14c5b5232 },
  year   = { 2019 },
  url    = { https://figshare.com/s/c2d31f850af14c5b5232 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Diaz-Pinto et al., 'Retinal Image Synthesis and Semi-Supervised Learning for Glaucoma Assessment', IEEE TMI 2019. Data: https://figshare.com/s/c2d31f850af14c5b5232
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
- [mfiddr](./mfiddr.md): MFIDDR: Multi-Field Imaging Dataset for Diabetic Retinopathy (34,452 images, `mit`)
