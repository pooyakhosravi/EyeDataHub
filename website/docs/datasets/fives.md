---
id: fives
title: "FIVES: Fundus Image Vessel Segmentation"
sidebar_label: fives
description: "800 high-resolution (2048x2048) fundus images with pixel-wise vessel segmentation. Covers normal, DR, AMD, glaucoma."
tags: ["fundus", "cc-by", "figshare", "segmentation", "documented-relationship", "relationship-derived_from"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# FIVES: Fundus Image Vessel Segmentation

800 high-resolution (2048x2048) fundus images with pixel-wise vessel segmentation. Covers normal, DR, AMD, glaucoma.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `fives` |
| **Full name** | FIVES: Fundus Image Vessel Segmentation |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | segmentation |
| **Primary reported quantity** | 800 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | train, test |
| **Size** | 1.1 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Figshare |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `transfer_tested_partial` |
| **Legacy sample-loader status** | Standard loader included |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 800 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [https://doi.org/10.6084/m9.figshare.19688169](https://doi.org/10.6084/m9.figshare.19688169) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- [mm_retinal_reason](./mm_retinal_reason.md) is `derived from` this record: The version-pinned official dataset card lists this record among the CFP or OCT sources used to construct MM-Retinal-Reason. ([evidence](https://huggingface.co/datasets/lxirich/MM-Retinal-Reason/tree/d6243baa82c0914dba3c6f43ca79fdbf856982ef))
- [multieye](./multieye.md) is `derived from` this record: The MultiEYE paper names this record as one of the public fundus or OCT sources assembled for the benchmark. ([evidence](https://arxiv.org/abs/2412.09402))
- [smdg](./smdg.md) is `derived from` this record: The official SMDG source table lists this catalog record among the 19 standardized source domains. ([evidence](https://www.kaggle.com/datasets/deathtrooper/multichannel-glaucoma-benchmark-dataset))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download fives --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download fives --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('fives')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.6084/m9.figshare.19688169](https://doi.org/10.6084/m9.figshare.19688169)

**Source-term evidence:** [https://doi.org/10.6084/m9.figshare.19688169](https://doi.org/10.6084/m9.figshare.19688169)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('fives')
samples = ds.load(data_dir, split='test')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{fives,
  title  = { FIVES: Fundus Image Vessel Segmentation },
  note   = { Jin et al., 'FIVES: A Fundus Image Dataset for Artificial Intelligence based Vessel Segmentation', Scientific Data 2022 },
  year   = { 2022 },
  url    = { https://doi.org/10.6084/m9.figshare.19688169 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Jin et al., 'FIVES: A Fundus Image Dataset for Artificial Intelligence based Vessel Segmentation', Scientific Data 2022.
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
