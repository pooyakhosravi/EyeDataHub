---
id: mendeley_two_photon_excited_fluorescence_scanning_laser
title: "Two-photon excited fluorescence scanning laser ophthalmoscopy images and software for data processing"
sidebar_label: mendeley_two_photon_excited_fluorescence_scanning_laser
description: "Ophthalmoscopy image/measurement data plus processing software from Exemplary two-photon fluorescence ophthalmoscope recordings from a healthy subject's eye."
tags: ["fundus", "retinal_imaging", "tabular", "cc-by", "mendeley", "measurement", "resource-role-current-dataset", "dataset-family-mendeley-two-photon-excited-fluorescence-scanning-laser"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Two-photon excited fluorescence scanning laser ophthalmoscopy images and software for data processing

Ophthalmoscopy image/measurement data plus processing software from Exemplary two-photon fluorescence ophthalmoscope recordings from a healthy subject's eye.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mendeley_two_photon_excited_fluorescence_scanning_laser` |
| **Full name** | Two-photon excited fluorescence scanning laser ophthalmoscopy images and software for data processing |
| **First published** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Primary category** | `fundus` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `mendeley_two_photon_excited_fluorescence_scanning_laser` |
| **Contained modalities** | fundus, retinal_imaging, tabular |
| **Tasks** | measurement |
| **Primary reported quantity** | 1 participants |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | Creative Commons Attribution 4.0 International |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `mixed_components` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Mendeley Data |
| **Availability** | `available` (checked 2026-08-02) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 1 | `participants` | Source-stated quantity Preserved from the source-confirmation record. | `official_source_description` | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/nhpnt78ssy) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Human provenance: Exemplary two-photon fluorescence ophthalmoscope recordings from a healthy subject's eye. Source-review finding: Source description says the repository contains an exemplary healthy-subject imaging dataset and data-processing software.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mendeley_two_photon_excited_fluorescence_scanning_laser --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download mendeley_two_photon_excited_fluorescence_scanning_laser --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mendeley_two_photon_excited_fluorescence_scanning_laser')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/nhpnt78ssy/1)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/nhpnt78ssy)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mendeley_two_photon_excited_fluorescence_scanning_laser,
  title  = { Two-photon excited fluorescence scanning laser ophthalmoscopy images and software for data processing },
  note   = { Two-photon excited fluorescence scanning laser ophthalmoscopy images and software for data processing. Mendeley Data, V1. doi:10.17632/nhpnt78ssy.1 },
  url    = { https://data.mendeley.com/datasets/nhpnt78ssy/1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Two-photon excited fluorescence scanning laser ophthalmoscopy images and software for data processing. Mendeley Data, V1. doi:10.17632/nhpnt78ssy.1.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Creative Commons Attribution 4.0 International
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
