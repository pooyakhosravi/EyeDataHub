---
id: dryad_diabetes_retinal_capillary
title: "Diabetes Retinal Capillary Rarefaction Dataset"
sidebar_label: dryad_diabetes_retinal_capillary
description: "The human diabetic retinal-capillary case-control measurements directly support retinal vascular analysis."
tags: ["fundus", "tabular", "cc0", "dryad", "vessel_analysis", "regression", "resource-role-current-dataset", "dataset-family-dryad-diabetes-retinal-capillary"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Diabetes Retinal Capillary Rarefaction Dataset

The human diabetic retinal-capillary case-control measurements directly support retinal vascular analysis.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_diabetes_retinal_capillary` |
| **Full name** | Diabetes Retinal Capillary Rarefaction Dataset |
| **Primary category** | `fundus` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `dryad_diabetes_retinal_capillary` |
| **Contained modalities** | fundus, tabular |
| **Tasks** | vessel_analysis, regression |
| **Primary reported quantity** | 73 participants |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 7.2745e-05 GB |
| **Source-stated terms** | https://spdx.org/licenses/CC0-1.0.html |
| **Normalized terms** | `cc0` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Dryad |
| **Availability** | `available` (checked 2026-08-01) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 73 | `participants` | Source-described type 2 diabetes participant group Source-stated quantity; Dryad file count is separate metadata and is not a scientific sample count. | `official_source_description` | [https://doi.org/10.5061/dryad.58791](https://doi.org/10.5061/dryad.58791) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Scope screen: core_add. Current Dryad v1 file listing: 1 files, 54983 bytes.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_diabetes_retinal_capillary --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dryad_diabetes_retinal_capillary --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_diabetes_retinal_capillary')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.58791](https://doi.org/10.5061/dryad.58791)

**Source-term evidence:** [https://doi.org/10.5061/dryad.58791](https://doi.org/10.5061/dryad.58791)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_diabetes_retinal_capillary,
  title  = { Diabetes Retinal Capillary Rarefaction Dataset },
  note   = { Jumar, Agnes, Harazny, Joanna M., Ott, Christian, Friedrich, Stefanie, Kistner, Iris, Striepe, Kristina, Schmieder, Roland, and Schmieder, Roland E.. Data from: Retinal capillary rarefaction in patients with type 2 diabetes mellitus. Dryad. 2017. doi:10.5061/dryad.58791 },
  year   = { 2017 },
  url    = { https://doi.org/10.5061/dryad.58791 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Jumar, Agnes, Harazny, Joanna M., Ott, Christian, Friedrich, Stefanie, Kistner, Iris, Striepe, Kristina, Schmieder, Roland, and Schmieder, Roland E.. Data from: Retinal capillary rarefaction in patients with type 2 diabetes mellitus. Dryad. 2017. doi:10.5061/dryad.58791
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** https://spdx.org/licenses/CC0-1.0.html
- **Normalized category:** `cc0`
- **Apparent scope:** `dataset_files`
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
- [mendeley_two_photon_excited_fluorescence_scanning_laser](./mendeley_two_photon_excited_fluorescence_scanning_laser.md): Two-photon excited fluorescence scanning laser ophthalmoscopy images and software for data processing (1 participants, `cc-by`)
