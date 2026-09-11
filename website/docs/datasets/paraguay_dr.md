---
id: paraguay_dr
title: "Paraguay Color Fundus DR Dataset"
sidebar_label: paraguay_dr
description: "757 color fundus images from a Paraguayan cohort with 7-class DR grading labels. Adds Latin-American representation."
tags: ["fundus", "cc-by", "zenodo", "grading", "classification", "resource-role-current-dataset", "dataset-family-paraguay-dr", "documented-relationship", "relationship-derived_from"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Paraguay Color Fundus DR Dataset

757 color fundus images from a Paraguayan cohort with 7-class DR grading labels. Adds Latin-American representation.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `paraguay_dr` |
| **Full name** | Paraguay Color Fundus DR Dataset |
| **Publication date** | 2021-02-10 |
| **Date basis** | Initial dataset release |
| **Publication date precision** | day |
| **Publication date evidence** | [zenodo.org/api](https://zenodo.org/api/records/4532361) |
| **Publication date source field** | metadata.publication_date (earliest repository version) |
| **Publication date reviewed** | 2026-09-11 |
| **Date notes** | Zenodo versions history for current record 4647952 identifies record 4532361 as the earliest version; date is the earliest version publication field. |
| **Primary category** | `fundus` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `paraguay_dr` |
| **Contained modalities** | fundus |
| **Tasks** | grading, classification |
| **Primary reported quantity** | 757 images |
| **Classes** | 7 (Not reported) |
| **Splits** | all |
| **Size** | 0.5 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Zenodo |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 757 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [zenodo.org/record](https://zenodo.org/record/4647952) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- [mm_retinal_reason](./mm_retinal_reason.md) is `derived from` this record: The version-pinned official dataset card lists this record among the CFP or OCT sources used to construct MM-Retinal-Reason. ([evidence](https://huggingface.co/datasets/lxirich/MM-Retinal-Reason/tree/d6243baa82c0914dba3c6f43ca79fdbf856982ef))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download paraguay_dr --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download paraguay_dr --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('paraguay_dr')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [zenodo.org/record](https://zenodo.org/record/4647952)

**Source-term evidence:** [zenodo.org/record](https://zenodo.org/record/4647952)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{paraguay_dr,
  title  = { Paraguay Color Fundus DR Dataset },
  note   = { Castillo Benítez et al., Paraguay DR Dataset, Zenodo 2021. doi:10.5281/zenodo.4647952 },
  year   = { 2021 },
  url    = { https://zenodo.org/record/4647952 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Castillo Benítez et al., Paraguay DR Dataset, Zenodo 2021. doi:10.5281/zenodo.4647952
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
