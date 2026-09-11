---
id: mendeley_biomechanical_properties_adult_patients_high_myopia
title: "Biomechanical properties of adult patients with high myopia after implantable collamer lens (ICL, V4) implantation"
sidebar_label: mendeley_biomechanical_properties_adult_patients_high_myopia
description: "Observation-level human or human-derived measurements/signals. from 55 high-myopia patients (110 eyes) after ICL implantation."
tags: ["corneal_topography", "cc-by", "mendeley", "measurement", "resource-role-current-dataset", "dataset-family-mendeley-biomechanical-properties-adult-patients-high-myopia"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Biomechanical properties of adult patients with high myopia after implantable collamer lens (ICL, V4) implantation

Observation-level human or human-derived measurements/signals. from 55 high-myopia patients (110 eyes) after ICL implantation.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mendeley_biomechanical_properties_adult_patients_high_myopia` |
| **Full name** | Biomechanical properties of adult patients with high myopia after implantable collamer lens (ICL, V4) implantation |
| **Publication date** | 2024-11-22 |
| **Date basis** | Initial dataset release |
| **Publication date precision** | day |
| **Publication date evidence** | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/yry4r9y9v5/1) |
| **Publication date source field** | citation_publication_date |
| **Publication date reviewed** | 2026-09-11 |
| **Date notes** | Official Mendeley Data version-1 page Published metadata; JSON-LD datePublished agrees. Version 1 is the initial public deposit. |
| **Primary category** | `corneal_topography` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `mendeley_biomechanical_properties_adult_patients_high_myopia` |
| **Contained modalities** | corneal_topography |
| **Tasks** | measurement |
| **Primary reported quantity** | 110 eyes |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Mendeley Data |
| **Availability** | `available` (checked 2026-08-02) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 110 | `eyes` | Source-stated quantity Preserved from the source-confirmation record. | `official_source_description` | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/yry4r9y9v5) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Human provenance: 55 high-myopia patients (110 eyes) after ICL implantation. Source-review finding: Corvis, Pentacam and eye-examination XLSX measurement tables.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mendeley_biomechanical_properties_adult_patients_high_myopia --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download mendeley_biomechanical_properties_adult_patients_high_myopia --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mendeley_biomechanical_properties_adult_patients_high_myopia')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/yry4r9y9v5/1)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/yry4r9y9v5)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mendeley_biomechanical_properties_adult_patients_high_myopia,
  title  = { Biomechanical properties of adult patients with high myopia after implantable collamer lens (ICL, V4) implantation },
  note   = { Biomechanical properties of adult patients with high myopia after implantable collamer lens (ICL, V4) implantation. Mendeley Data, V1. doi:10.17632/yry4r9y9v5.1 },
  url    = { https://data.mendeley.com/datasets/yry4r9y9v5/1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Biomechanical properties of adult patients with high myopia after implantable collamer lens (ICL, V4) implantation. Mendeley Data, V1. doi:10.17632/yry4r9y9v5.1.
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

- [mendeley_corneal_refractive_parameters_age_patients_without](./mendeley_corneal_refractive_parameters_age_patients_without.md): corneal refractive parameters with age in patients without corneal diseases based on Fourier analysis  (2,545 participants, `cc-by`)
- [cornorb](./cornorb.md): CornOrb: Orbscan Corneal Topography and Clinical Annotations (1,454 eyes, `cc-by`)
- [keratoconus_detection_kaggle](./keratoconus_detection_kaggle.md): Keratoconus Detection Corneal Maps (573 images, `unknown`)
- [dryad_pediatric_corneal_endothelium](./dryad_pediatric_corneal_endothelium.md): Corneal endothelial morphology of healthy myopic Malaysian children of Chinese ethnicity aged 8-9 years and its association with axial length (111 participants, `cc0`)
- [dryad_cornea_oct_pentacam](./dryad_cornea_oct_pentacam.md): Corneal OCT and Pentacam Tomography Dataset (52 participants, `cc0`)
- [casia2_as_oct_repeatability](./casia2_as_oct_repeatability.md): CASIA2 Anterior-Segment OCT Repeatability Dataset (Not reported, `cc-by`)
- [casia2_keratometric_astigmatism](./casia2_keratometric_astigmatism.md): CASIA2 Keratometric Astigmatism Dataset (Not reported, `cc-by`)
- [dryad_corneal_biomechanics_prostaglandin](./dryad_corneal_biomechanics_prostaglandin.md): Changes in corneal biomechanical properties after long-term topical prostaglandin therapy (Not reported, `cc0`)
