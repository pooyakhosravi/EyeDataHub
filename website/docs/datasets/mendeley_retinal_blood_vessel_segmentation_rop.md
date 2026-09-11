---
id: mendeley_retinal_blood_vessel_segmentation_rop
title: "Retinal blood vessel segmentation(ROP)"
sidebar_label: mendeley_retinal_blood_vessel_segmentation_rop
description: "Fundus-image-level vessel-segmentation data from Retinopathy-of-prematurity retinal images; human infant provenance is inherent to the stated ROP source."
tags: ["fundus", "tabular", "cc-by", "mendeley", "segmentation", "resource-role-current-dataset", "dataset-family-mendeley-retinal-blood-vessel-segmentation-rop"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Retinal blood vessel segmentation(ROP)

Fundus-image-level vessel-segmentation data from Retinopathy-of-prematurity retinal images; human infant provenance is inherent to the stated ROP source.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mendeley_retinal_blood_vessel_segmentation_rop` |
| **Full name** | Retinal blood vessel segmentation(ROP) |
| **Publication date** | 2020-07-15 |
| **Date basis** | Initial dataset release |
| **Publication date precision** | day |
| **Publication date evidence** | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/prcy36j53v/1) |
| **Publication date source field** | citation_publication_date (version 1) |
| **Publication date reviewed** | 2026-09-11 |
| **Date notes** | - |
| **Primary category** | `fundus` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `mendeley_retinal_blood_vessel_segmentation_rop` |
| **Contained modalities** | fundus, tabular |
| **Tasks** | segmentation |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | Source description: free only for academic purpose; DOI registration also lists Creative Commons Attribution 4.0 International. |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `mixed_components` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Mendeley Data |
| **Availability** | `available` (checked 2026-08-02) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

No reproducible primary item count was exposed for the cataloged source version.

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Human provenance: Retinopathy-of-prematurity retinal images; human infant provenance is inherent to the stated ROP source. Source-review finding: Source description identifies retinal blood-vessel segmentation for ROP and asks users to cite the associated article.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mendeley_retinal_blood_vessel_segmentation_rop --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download mendeley_retinal_blood_vessel_segmentation_rop --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mendeley_retinal_blood_vessel_segmentation_rop')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/prcy36j53v/1)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/prcy36j53v)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mendeley_retinal_blood_vessel_segmentation_rop,
  title  = { Retinal blood vessel segmentation(ROP) },
  note   = { Retinal blood vessel segmentation(ROP). Mendeley Data, V1. doi:10.17632/prcy36j53v.1 },
  url    = { https://data.mendeley.com/datasets/prcy36j53v/1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Retinal blood vessel segmentation(ROP). Mendeley Data, V1. doi:10.17632/prcy36j53v.1.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Source description: free only for academic purpose; DOI registration also lists Creative Commons Attribution 4.0 International.
- **Normalized category:** `cc-by`
- **Apparent scope:** `mixed_components`
- **Descriptive screening label:** Standard label without an explicit NC clause; not a permission finding

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [fairvlmed](./fairvlmed.md): FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset (10,000 images, `cc-by-nc-nd`)
- [olives](./olives.md): OLIVES: Ophthalmic Labels for Investigating Visual Eye Semantics (9,408 b scans, `cc-by`)
- [fprm_retina](./fprm_retina.md): FPRM Multimodal Eye Imaging and Psychological Assessment Dataset (3,361 images, `research-only`)
- [grape](./grape.md): GRAPE: Glaucoma Real-world Appraisal Progression Ensemble (1,115 examinations, `cc0`)
- [papila](./papila.md): PAPILA: Glaucoma Fundus Dataset with Clinical Data (488 images, `cc-by`)
- [mendeley_retina_identification_database_ridb](./mendeley_retina_identification_database_ridb.md): Retina Identification Database (RIDB) (100 images, `cc-by`)
- [dryad_diabetes_retinal_capillary](./dryad_diabetes_retinal_capillary.md): Diabetes Retinal Capillary Rarefaction Dataset (73 participants, `cc0`)
