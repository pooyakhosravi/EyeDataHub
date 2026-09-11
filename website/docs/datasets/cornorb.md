---
id: cornorb
title: "CornOrb: Orbscan Corneal Topography and Clinical Annotations"
sidebar_label: cornorb
description: "Orbscan corneal topography maps and structured clinical annotations for keratoconus detection."
tags: ["corneal_topography", "cc-by", "zenodo", "classification", "resource-role-current-dataset", "dataset-family-cornorb"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# CornOrb: Orbscan Corneal Topography and Clinical Annotations

Orbscan corneal topography maps and structured clinical annotations for keratoconus detection.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `cornorb` |
| **Full name** | CornOrb: Orbscan Corneal Topography and Clinical Annotations |
| **First published** | 2025-09-15 |
| **Publication date precision** | day |
| **Publication date evidence** | [zenodo.org/api](https://zenodo.org/api/records/17121302) |
| **Publication date source field** | metadata.publication_date (earliest public Zenodo version) |
| **Publication date reviewed** | 2026-09-11 |
| **Primary category** | `corneal_topography` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `cornorb` |
| **Contained modalities** | corneal_topography |
| **Tasks** | classification |
| **Primary reported quantity** | 1,454 eyes |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.68 GB |
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
| Primary | 1,454 | `eyes` | Rows in the current clinical-data table | `current_deposit_table` | [zenodo.org/records](https://zenodo.org/records/20542091) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download cornorb --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download cornorb --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('cornorb')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [zenodo.org/records](https://zenodo.org/records/20542091)

**Source-term evidence:** [zenodo.org/records](https://zenodo.org/records/20542091)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{cornorb,
  title  = { CornOrb: Orbscan Corneal Topography and Clinical Annotations },
  note   = { CornOrb: A Multimodal Dataset of Orbscan Corneal Topography and Clinical Annotations for Keratoconus Detection. Zenodo, 2026. doi:10.5281/zenodo.20542091 },
  year   = { 2026 },
  url    = { https://zenodo.org/records/20542091 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
CornOrb: A Multimodal Dataset of Orbscan Corneal Topography and Clinical Annotations for Keratoconus Detection. Zenodo, 2026. doi:10.5281/zenodo.20542091
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
- [keratoconus_detection_kaggle](./keratoconus_detection_kaggle.md): Keratoconus Detection Corneal Maps (573 images, `unknown`)
- [dryad_pediatric_corneal_endothelium](./dryad_pediatric_corneal_endothelium.md): Corneal endothelial morphology of healthy myopic Malaysian children of Chinese ethnicity aged 8-9 years and its association with axial length (111 participants, `cc0`)
- [mendeley_biomechanical_properties_adult_patients_high_myopia](./mendeley_biomechanical_properties_adult_patients_high_myopia.md): Biomechanical properties of adult patients with high myopia after implantable collamer lens (ICL, V4) implantation (110 eyes, `cc-by`)
- [dryad_cornea_oct_pentacam](./dryad_cornea_oct_pentacam.md): Corneal OCT and Pentacam Tomography Dataset (52 participants, `cc0`)
- [casia2_as_oct_repeatability](./casia2_as_oct_repeatability.md): CASIA2 Anterior-Segment OCT Repeatability Dataset (Not reported, `cc-by`)
- [casia2_keratometric_astigmatism](./casia2_keratometric_astigmatism.md): CASIA2 Keratometric Astigmatism Dataset (Not reported, `cc-by`)
- [dryad_corneal_biomechanics_prostaglandin](./dryad_corneal_biomechanics_prostaglandin.md): Changes in corneal biomechanical properties after long-term topical prostaglandin therapy (Not reported, `cc0`)
