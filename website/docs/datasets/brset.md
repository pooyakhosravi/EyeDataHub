---
id: brset
title: "BRSET: Brazilian Multilabel Ophthalmological Dataset"
sidebar_label: brset
description: "16,266 color fundus images from 8,524 Brazilian patients with 14 disease labels (DR, AMD, glaucoma, drusen, others), image quality flags, and demographic attributes."
tags: ["fundus", "research-only", "physionet", "multilabel", "classification", "quality", "resource-role-current-dataset", "dataset-family-brset", "documented-relationship", "relationship-derived_from"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# BRSET: Brazilian Multilabel Ophthalmological Dataset

16,266 color fundus images from 8,524 Brazilian patients with 14 disease labels (DR, AMD, glaucoma, drusen, others), image quality flags, and demographic attributes.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `brset` |
| **Full name** | BRSET: Brazilian Multilabel Ophthalmological Dataset |
| **Publication date** | 2023-03-08 |
| **Date basis** | Initial dataset release |
| **Publication date precision** | day |
| **Publication date evidence** | [physionet.org/content](https://physionet.org/content/brazilian-ophthalmological/1.0.0/) |
| **Publication date source field** | PhysioNet landing page: Published |
| **Publication date reviewed** | 2026-09-11 |
| **Date notes** | The version 1.0.0 PhysioNet page states Published: March 8, 2023; this is the initial version, not the later version 1.0.1. |
| **Primary category** | `fundus` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `brset` |
| **Contained modalities** | fundus |
| **Tasks** | multilabel, classification, quality |
| **Primary reported quantity** | 16,266 images |
| **Classes** | 14 (Not reported) |
| **Splits** | all |
| **Size** | 9.0 GB |
| **Source-stated terms** | PhysioNet Credentialed Health Data License 1.5.0 (Research only) |
| **Normalized terms** | `research-only` |
| **Descriptive screening label** | Research or challenge restriction recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `controlled_or_manual` |
| **Route backend** | PhysioNet |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `manual_access_blocked` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 16,266 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [physionet.org/content](https://physionet.org/content/brazilian-ophthalmological/1.0.1/) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Requires PhysioNet credentialed-user account + CITI training + signed Data Use Agreement. Set PHYSIONET_USERNAME and PHYSIONET_PASSWORD in .env to auto-download.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- [brset_mbrset_embeddings](./brset_mbrset_embeddings.md) is `derived from` this record: The PhysioNet record supplies precomputed representations for BRSET images. ([evidence](https://physionet.org/content/embedding-brset-mbrset/1.0.0/))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# This route requires upstream human action; no transfer starts.
eyehub download brset --data-dir ./data --dry-run --json
# Follow the official instructions shown by preflight.
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('brset')
print(preflight_dataset(ds, './data'))  # returns manual_access_blocked
```

  </TabItem>
</Tabs>

**Upstream page:** [physionet.org/content](https://physionet.org/content/brazilian-ophthalmological/1.0.1/)

**Source-term evidence:** [physionet.org/content](https://physionet.org/content/brazilian-ophthalmological/1.0.1/)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{brset,
  title  = { BRSET: Brazilian Multilabel Ophthalmological Dataset },
  note   = { Nakayama LF, Restrepo D, Matos J, et al., 'BRSET: A Brazilian Multilabel Ophthalmological Dataset of Retina Fundus Photos', PLOS Digital Health 3(7):e0000454, 2024. doi:10.1371/journal.pdig.0000454 · PhysioNet DOI: 10.13026/1pht-2b69 },
  year   = { 2024 },
  url    = { https://physionet.org/content/brazilian-ophthalmological/1.0.1/ },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Nakayama LF, Restrepo D, Matos J, et al., 'BRSET: A Brazilian Multilabel Ophthalmological Dataset of Retina Fundus Photos', PLOS Digital Health 3(7):e0000454, 2024. doi:10.1371/journal.pdig.0000454 · PhysioNet DOI: 10.13026/1pht-2b69
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** PhysioNet Credentialed Health Data License 1.5.0 (Research only)
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
