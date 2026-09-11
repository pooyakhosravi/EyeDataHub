---
id: mendeley_orbscan_iiz_anterior_maps
title: "Multimodal Orbscan IIz Dataset: 3,000 Axial Power Anterior Maps with OCR-Extracted Clinical Parameters from 3,000 Unique Patients"
sidebar_label: mendeley_orbscan_iiz_anterior_maps
description: "Observation-level source data, annotations, or signals. from Source explicitly identifies 3,000 unique patients."
tags: ["corneal_topography", "cc-by-nc", "mendeley", "measurement", "resource-role-current-dataset", "dataset-family-mendeley-orbscan-iiz-anterior-maps"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Multimodal Orbscan IIz Dataset: 3,000 Axial Power Anterior Maps with OCR-Extracted Clinical Parameters from 3,000 Unique Patients

Observation-level source data, annotations, or signals. from Source explicitly identifies 3,000 unique patients.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mendeley_orbscan_iiz_anterior_maps` |
| **Full name** | Multimodal Orbscan IIz Dataset: 3,000 Axial Power Anterior Maps with OCR-Extracted Clinical Parameters from 3,000 Unique Patients |
| **First published** | 2026-06-16 |
| **Publication date precision** | day |
| **Publication date evidence** | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/78wt2nc387/1) |
| **Publication date source field** | citation_publication_date (version 1) |
| **Publication date reviewed** | 2026-09-11 |
| **Primary category** | `corneal_topography` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `mendeley_orbscan_iiz_anterior_maps` |
| **Contained modalities** | corneal_topography |
| **Tasks** | measurement |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | CC BY-NC 4.0 |
| **Normalized terms** | `cc-by-nc` |
| **Descriptive screening label** | Explicit noncommercial clause recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Mendeley Data |
| **Availability** | `available` (checked 2026-08-02) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

No reproducible primary item count was exposed for the cataloged source version.

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Human provenance: Source explicitly identifies 3,000 unique patients. Source-review finding: Nine files including Images.zip, four CSV files, analysis script, and documentation. Source-stated quantity retained without normalization: 3000 axial-power anterior maps (3,000 unique patients).

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mendeley_orbscan_iiz_anterior_maps --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download mendeley_orbscan_iiz_anterior_maps --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mendeley_orbscan_iiz_anterior_maps')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/78wt2nc387/3)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/78wt2nc387)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mendeley_orbscan_iiz_anterior_maps,
  title  = { Multimodal Orbscan IIz Dataset: 3,000 Axial Power Anterior Maps with OCR-Extracted Clinical Parameters from 3,000 Unique Patients },
  note   = { Multimodal Orbscan IIz Dataset: 3,000 Axial Power Anterior Maps with OCR-Extracted Clinical Parameters from 3,000 Unique Patients. Mendeley Data, V3. doi:10.17632/78wt2nc387.3 },
  url    = { https://data.mendeley.com/datasets/78wt2nc387/3 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Multimodal Orbscan IIz Dataset: 3,000 Axial Power Anterior Maps with OCR-Extracted Clinical Parameters from 3,000 Unique Patients. Mendeley Data, V3. doi:10.17632/78wt2nc387.3.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC BY-NC 4.0
- **Normalized category:** `cc-by-nc`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Explicit noncommercial clause recorded; check source

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [mendeley_corneal_refractive_parameters_age_patients_without](./mendeley_corneal_refractive_parameters_age_patients_without.md): corneal refractive parameters with age in patients without corneal diseases based on Fourier analysis  (2,545 participants, `cc-by`)
- [cornorb](./cornorb.md): CornOrb: Orbscan Corneal Topography and Clinical Annotations (1,454 eyes, `cc-by`)
- [keratoconus_detection_kaggle](./keratoconus_detection_kaggle.md): Keratoconus Detection Corneal Maps (573 images, `unknown`)
- [dryad_pediatric_corneal_endothelium](./dryad_pediatric_corneal_endothelium.md): Corneal endothelial morphology of healthy myopic Malaysian children of Chinese ethnicity aged 8-9 years and its association with axial length (111 participants, `cc0`)
- [mendeley_biomechanical_properties_adult_patients_high_myopia](./mendeley_biomechanical_properties_adult_patients_high_myopia.md): Biomechanical properties of adult patients with high myopia after implantable collamer lens (ICL, V4) implantation (110 eyes, `cc-by`)
- [dryad_cornea_oct_pentacam](./dryad_cornea_oct_pentacam.md): Corneal OCT and Pentacam Tomography Dataset (52 participants, `cc0`)
- [casia2_as_oct_repeatability](./casia2_as_oct_repeatability.md): CASIA2 Anterior-Segment OCT Repeatability Dataset (Not reported, `cc-by`)
- [casia2_keratometric_astigmatism](./casia2_keratometric_astigmatism.md): CASIA2 Keratometric Astigmatism Dataset (Not reported, `cc-by`)
