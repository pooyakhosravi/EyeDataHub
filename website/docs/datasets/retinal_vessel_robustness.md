---
id: retinal_vessel_robustness
title: "Natural Robustness Benchmark for Retinal Vessel Segmentation"
sidebar_label: retinal_vessel_robustness
description: "Augmented DRIVE, STARE, and CHASE_DB1 vessel-segmentation images for out-of-distribution robustness evaluation."
tags: ["fundus", "mit", "zenodo", "segmentation", "documented-relationship", "relationship-derived_from"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Natural Robustness Benchmark for Retinal Vessel Segmentation

Augmented DRIVE, STARE, and CHASE_DB1 vessel-segmentation images for out-of-distribution robustness evaluation.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `retinal_vessel_robustness` |
| **Full name** | Natural Robustness Benchmark for Retinal Vessel Segmentation |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | segmentation |
| **Primary reported quantity** | 13,024 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 8.15 GB |
| **Source-stated terms** | MIT |
| **Normalized terms** | `mit` |
| **Descriptive screening label** | Standard label without an explicit NC clause; verify that it applies to data |
| **Terms scope** | `unknown` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Zenodo |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 13,024 | `images` | Files under the images directories in all three current archives Includes 5,920 DRIVE, 4,144 CHASE, and 2,960 STARE original or augmented images; parent datasets overlap catalog records. | `current_deposit_file_listing` | [zenodo.org/records](https://zenodo.org/records/12659652) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Derivative robustness benchmark from existing vessel datasets.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- This record is `derived from` [chase_db1](./chase_db1.md): The robustness benchmark contains augmented versions of DRIVE, STARE, and CHASE_DB1 images. ([evidence](https://zenodo.org/records/12659652))
- This record is `derived from` [drive](./drive.md): The robustness benchmark contains augmented versions of DRIVE, STARE, and CHASE_DB1 images. ([evidence](https://zenodo.org/records/12659652))
- This record is `derived from` [stare](./stare.md): The robustness benchmark contains augmented versions of DRIVE, STARE, and CHASE_DB1 images. ([evidence](https://zenodo.org/records/12659652))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download retinal_vessel_robustness --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download retinal_vessel_robustness --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('retinal_vessel_robustness')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [zenodo.org/records](https://zenodo.org/records/12659652)

**Source-term evidence:** [zenodo.org/records](https://zenodo.org/records/12659652)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{retinal_vessel_robustness,
  title  = { Natural Robustness Benchmark for Retinal Vessel Segmentation },
  note   = { Evaluation benchmark for natural robustness evaluation of retinal vessel segmentation models. Zenodo, 2024. doi:10.5281/zenodo.12659652 },
  year   = { 2024 },
  url    = { https://zenodo.org/records/12659652 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Evaluation benchmark for natural robustness evaluation of retinal vessel segmentation models. Zenodo, 2024. doi:10.5281/zenodo.12659652
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** MIT
- **Normalized category:** `mit`
- **Apparent scope:** `unknown`
- **Descriptive screening label:** Standard label without an explicit NC clause; verify that it applies to data

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
