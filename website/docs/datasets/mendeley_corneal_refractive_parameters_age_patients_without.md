---
id: mendeley_corneal_refractive_parameters_age_patients_without
title: "corneal refractive parameters with age in patients without corneal diseases based on Fourier analysis"
sidebar_label: mendeley_corneal_refractive_parameters_age_patients_without
description: "Observation-level human or human-derived measurements/signals. from 2,545 patients without corneal disease (5,074 eyes)."
tags: ["corneal_topography", "cc-by", "mendeley", "classification", "resource-role-current-dataset", "dataset-family-mendeley-corneal-refractive-parameters-age-patients-without"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# corneal refractive parameters with age in patients without corneal diseases based on Fourier analysis 

Observation-level human or human-derived measurements/signals. from 2,545 patients without corneal disease (5,074 eyes).

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mendeley_corneal_refractive_parameters_age_patients_without` |
| **Full name** | corneal refractive parameters with age in patients without corneal diseases based on Fourier analysis  |
| **First published** | 2025-07-07 |
| **Publication date precision** | day |
| **Publication date evidence** | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/yr8hbwmsvy/1) |
| **Publication date source field** | citation_publication_date (version 1) |
| **Publication date reviewed** | 2026-09-11 |
| **Primary category** | `corneal_topography` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `mendeley_corneal_refractive_parameters_age_patients_without` |
| **Contained modalities** | corneal_topography |
| **Tasks** | classification |
| **Primary reported quantity** | 2,545 participants |
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
| Primary | 2,545 | `participants` | Source-stated quantity Preserved from the source-confirmation record. | `official_source_description` | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/yr8hbwmsvy) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Human provenance: 2,545 patients without corneal disease (5,074 eyes). Source-review finding: Videokeratography/Pentacam Fourier-derived corneal parameter dataset.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mendeley_corneal_refractive_parameters_age_patients_without --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download mendeley_corneal_refractive_parameters_age_patients_without --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mendeley_corneal_refractive_parameters_age_patients_without')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/yr8hbwmsvy/1)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/yr8hbwmsvy)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mendeley_corneal_refractive_parameters_age_patients_without,
  title  = { corneal refractive parameters with age in patients without corneal diseases based on Fourier analysis  },
  note   = { corneal refractive parameters with age in patients without corneal diseases based on Fourier analysis . Mendeley Data, V1. doi:10.17632/yr8hbwmsvy.1 },
  url    = { https://data.mendeley.com/datasets/yr8hbwmsvy/1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
corneal refractive parameters with age in patients without corneal diseases based on Fourier analysis . Mendeley Data, V1. doi:10.17632/yr8hbwmsvy.1.
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

- [cornorb](./cornorb.md): CornOrb: Orbscan Corneal Topography and Clinical Annotations (1,454 eyes, `cc-by`)
- [keratoconus_detection_kaggle](./keratoconus_detection_kaggle.md): Keratoconus Detection Corneal Maps (573 images, `unknown`)
- [dryad_pediatric_corneal_endothelium](./dryad_pediatric_corneal_endothelium.md): Corneal endothelial morphology of healthy myopic Malaysian children of Chinese ethnicity aged 8-9 years and its association with axial length (111 participants, `cc0`)
- [mendeley_biomechanical_properties_adult_patients_high_myopia](./mendeley_biomechanical_properties_adult_patients_high_myopia.md): Biomechanical properties of adult patients with high myopia after implantable collamer lens (ICL, V4) implantation (110 eyes, `cc-by`)
- [dryad_cornea_oct_pentacam](./dryad_cornea_oct_pentacam.md): Corneal OCT and Pentacam Tomography Dataset (52 participants, `cc0`)
- [casia2_as_oct_repeatability](./casia2_as_oct_repeatability.md): CASIA2 Anterior-Segment OCT Repeatability Dataset (Not reported, `cc-by`)
- [casia2_keratometric_astigmatism](./casia2_keratometric_astigmatism.md): CASIA2 Keratometric Astigmatism Dataset (Not reported, `cc-by`)
- [dryad_corneal_biomechanics_prostaglandin](./dryad_corneal_biomechanics_prostaglandin.md): Changes in corneal biomechanical properties after long-term topical prostaglandin therapy (Not reported, `cc0`)
