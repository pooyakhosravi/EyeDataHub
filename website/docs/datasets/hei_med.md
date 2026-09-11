---
id: hei_med
title: "HEI-MED: Hamilton Eye Institute Macular Edema Dataset"
sidebar_label: hei_med
description: "A collection of 169 fundus photographs with expert exudate and bright lesion annotations, clinical metadata, optic nerve locations, vessel estimates, and image quality scores."
tags: ["fundus", "research-only", "github", "segmentation", "classification", "quality", "resource-role-current-dataset", "dataset-family-hei-med"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# HEI-MED: Hamilton Eye Institute Macular Edema Dataset

A collection of 169 fundus photographs with expert exudate and bright lesion annotations, clinical metadata, optic nerve locations, vessel estimates, and image quality scores.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `hei_med` |
| **Full name** | HEI-MED: Hamilton Eye Institute Macular Edema Dataset |
| **Publication date** | Unknown |
| **Date basis** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Date notes** | - |
| **Primary category** | `fundus` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `hei_med` |
| **Contained modalities** | fundus |
| **Tasks** | segmentation, classification, quality |
| **Primary reported quantity** | 169 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.32 GB |
| **Source-stated terms** | Research only: non-commercial research use |
| **Normalized terms** | `research-only` |
| **Descriptive screening label** | Research or challenge restriction recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | GitHub |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `end_to_end_tested` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 169 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [github.com/lgiancaUTH](https://github.com/lgiancaUTH/HEI-MED) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> The source README permits only non-commercial research use and requires citation. No SPDX license file is present.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download hei_med --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download hei_med --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('hei_med')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [github.com/lgiancaUTH](https://github.com/lgiancaUTH/HEI-MED)

**Source-term evidence:** [github.com/lgiancaUTH](https://github.com/lgiancaUTH/HEI-MED)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{hei_med,
  title  = { HEI-MED: Hamilton Eye Institute Macular Edema Dataset },
  note   = { Giancardo L, Meriaudeau F, Karnowski TP, et al. Exudate-based diabetic macular edema detection in fundus images using publicly available datasets. Med Image Anal. 2012;16:216-226. doi:10.1016/j.media.2011.07.004 },
  year   = { 2012 },
  url    = { https://github.com/lgiancaUTH/HEI-MED },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Giancardo L, Meriaudeau F, Karnowski TP, et al. Exudate-based diabetic macular edema detection in fundus images using publicly available datasets. Med Image Anal. 2012;16:216-226. doi:10.1016/j.media.2011.07.004
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Research only: non-commercial research use
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
