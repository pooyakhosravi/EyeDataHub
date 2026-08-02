---
id: casia2_keratometric_astigmatism
title: "CASIA2 Keratometric Astigmatism Dataset"
sidebar_label: casia2_keratometric_astigmatism
description: "Human anterior-segment OCT keratometric-astigmatism measurements."
tags: ["corneal_topography", "as_oct", "cc-by", "figshare", "measurement"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# CASIA2 Keratometric Astigmatism Dataset

Human anterior-segment OCT keratometric-astigmatism measurements.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `casia2_keratometric_astigmatism` |
| **Full name** | CASIA2 Keratometric Astigmatism Dataset |
| **Primary category** | `corneal_topography` |
| **Contained modalities** | corneal_topography, as_oct |
| **Tasks** | measurement |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Figshare |
| **Availability** | `available` (checked 2026-08-02) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

No reproducible primary item count was exposed for the cataloged source version.

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download casia2_keratometric_astigmatism --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download casia2_keratometric_astigmatism --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('casia2_keratometric_astigmatism')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.6084/m9.figshare.26395018.v1](https://doi.org/10.6084/m9.figshare.26395018.v1)

**Source-term evidence:** [https://doi.org/10.6084/m9.figshare.26395018.v1](https://doi.org/10.6084/m9.figshare.26395018.v1)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{casia2_keratometric_astigmatism,
  title  = { CASIA2 Keratometric Astigmatism Dataset },
  note   = { Repository dataset record. 10.6084/m9.figshare.26395018.v1 },
  url    = { https://doi.org/10.6084/m9.figshare.26395018.v1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Repository dataset record. 10.6084/m9.figshare.26395018.v1.
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

- [casia2_as_oct_repeatability](./casia2_as_oct_repeatability.md): CASIA2 Anterior-Segment OCT Repeatability Dataset (Not reported, `cc-by`)
- [mendeley_corneal_refractive_parameters_age_patients_without](./mendeley_corneal_refractive_parameters_age_patients_without.md): corneal refractive parameters with age in patients without corneal diseases based on Fourier analysis  (2,545 participants, `cc-by`)
- [cornorb](./cornorb.md): CornOrb: Orbscan Corneal Topography and Clinical Annotations (1,454 eyes, `cc-by`)
- [keratoconus_detection_kaggle](./keratoconus_detection_kaggle.md): Keratoconus Detection Corneal Maps (573 images, `unknown`)
- [dryad_pediatric_corneal_endothelium](./dryad_pediatric_corneal_endothelium.md): Corneal endothelial morphology of healthy myopic Malaysian children of Chinese ethnicity aged 8-9 years and its association with axial length (111 participants, `cc0`)
- [mendeley_biomechanical_properties_adult_patients_high_myopia](./mendeley_biomechanical_properties_adult_patients_high_myopia.md): Biomechanical properties of adult patients with high myopia after implantable collamer lens (ICL, V4) implantation (110 eyes, `cc-by`)
- [dryad_cornea_oct_pentacam](./dryad_cornea_oct_pentacam.md): Corneal OCT and Pentacam Tomography Dataset (52 participants, `cc0`)
- [dryad_corneal_biomechanics_prostaglandin](./dryad_corneal_biomechanics_prostaglandin.md): Changes in corneal biomechanical properties after long-term topical prostaglandin therapy (Not reported, `cc0`)
