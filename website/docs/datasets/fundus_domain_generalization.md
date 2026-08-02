---
id: fundus_domain_generalization
title: "Fundus Dataset for Domain Generalization in Optic Disc/Cup Segmentation"
sidebar_label: fundus_domain_generalization
description: "Five-domain optic disc/cup segmentation benchmark composed from REFUGE, Drishti-GS, ORIGA, RIGA, and related sources."
tags: ["fundus", "cc-by", "zenodo", "segmentation", "documented-relationship", "relationship-derived_from"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Fundus Dataset for Domain Generalization in Optic Disc/Cup Segmentation

Five-domain optic disc/cup segmentation benchmark composed from REFUGE, Drishti-GS, ORIGA, RIGA, and related sources.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `fundus_domain_generalization` |
| **Full name** | Fundus Dataset for Domain Generalization in Optic Disc/Cup Segmentation |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | segmentation |
| **Primary reported quantity** | 1,441 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.62 GB |
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
| Primary | 1,441 | `images` | Five source domains after the documented train/test composition The images reuse REFUGE, Drishti-GS, ORIGA, and RIGA sources. | `derived_from_reported_components` | [zenodo.org/records](https://zenodo.org/records/8009107) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Composite of datasets already indexed separately; retained as a benchmark split/annotation resource.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- This record is `derived from` [drishti_gs](./drishti_gs.md): The official description states that the benchmark is based on REFUGE, Drishti-GS, ORIGA, and RIGA. ([evidence](https://zenodo.org/records/8009107))
- This record is `derived from` [refuge2018](./refuge2018.md): The official description states that the benchmark is based on REFUGE, Drishti-GS, ORIGA, and RIGA. ([evidence](https://zenodo.org/records/8009107))
- This record is `derived from` [riga](./riga.md): The official description states that the benchmark is based on REFUGE, Drishti-GS, ORIGA, and RIGA. ([evidence](https://zenodo.org/records/8009107))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download fundus_domain_generalization --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download fundus_domain_generalization --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('fundus_domain_generalization')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [zenodo.org/records](https://zenodo.org/records/8009107)

**Source-term evidence:** [zenodo.org/records](https://zenodo.org/records/8009107)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{fundus_domain_generalization,
  title  = { Fundus Dataset for Domain Generalization in Optic Disc/Cup Segmentation },
  note   = { A Fundus Image Dataset for Domain Generalization in Joint Segmentation of Optic Disc and Optic Cup. Zenodo, 2023. doi:10.5281/zenodo.8009107 },
  year   = { 2023 },
  url    = { https://zenodo.org/records/8009107 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
A Fundus Image Dataset for Domain Generalization in Joint Segmentation of Optic Disc and Optic Cup. Zenodo, 2023. doi:10.5281/zenodo.8009107
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
