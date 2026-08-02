---
id: fundus_avseg
title: "Fundus-AVSeg: Artery-Vein-Crossing Segmentation"
sidebar_label: fundus_avseg
description: "100 high-resolution color fundus images with pixel-wise artery / vein / crossing labels from a mixed disease cohort."
tags: ["fundus", "cc-by", "figshare", "segmentation", "resource-role-current-dataset", "dataset-family-fundus-avseg"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Fundus-AVSeg: Artery-Vein-Crossing Segmentation

100 high-resolution color fundus images with pixel-wise artery / vein / crossing labels from a mixed disease cohort.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `fundus_avseg` |
| **Full name** | Fundus-AVSeg: Artery-Vein-Crossing Segmentation |
| **Primary category** | `fundus` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `fundus_avseg` |
| **Contained modalities** | fundus |
| **Tasks** | segmentation |
| **Primary reported quantity** | 100 images |
| **Classes** | 4 (background, artery, vein, crossing) |
| **Splits** | all |
| **Size** | 0.5 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Figshare |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `end_to_end_tested` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 100 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [https://doi.org/10.6084/m9.figshare.27938034](https://doi.org/10.6084/m9.figshare.27938034) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download fundus_avseg --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download fundus_avseg --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('fundus_avseg')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.6084/m9.figshare.27938034](https://doi.org/10.6084/m9.figshare.27938034)

**Source-term evidence:** [https://doi.org/10.6084/m9.figshare.27938034](https://doi.org/10.6084/m9.figshare.27938034)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{fundus_avseg,
  title  = { Fundus-AVSeg: Artery-Vein-Crossing Segmentation },
  note   = { Fundus-AVSeg dataset, Figshare project 229986 (2025). Companion paper: Basit & Alam, 'AVSeg-XAI', BioData Mining, doi:10.1186/s13040-026-00573-x (2026). Sci. Data DOI 10.1038/s41597-025-05381-2 was the paper venue at time of indexing — verify at final publication },
  year   = { 2025 },
  url    = { https://doi.org/10.6084/m9.figshare.27938034 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Fundus-AVSeg dataset, Figshare project 229986 (2025). Companion paper: Basit & Alam, 'AVSeg-XAI', BioData Mining, doi:10.1186/s13040-026-00573-x (2026). Sci. Data DOI 10.1038/s41597-025-05381-2 was the paper venue at time of indexing — verify at final publication.
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
