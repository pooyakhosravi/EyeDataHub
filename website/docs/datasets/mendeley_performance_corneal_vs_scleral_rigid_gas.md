---
id: mendeley_performance_corneal_vs_scleral_rigid_gas
title: "Data for: Performance of corneal vs. scleral rigid gas permeable contact lenses for ectatic corneal disorders"
sidebar_label: mendeley_performance_corneal_vs_scleral_rigid_gas
description: "Participant/eye-level clinical and lens-performance outcomes from People with keratoconus or related corneal ectatic disorders in the randomized contact-lens study."
tags: ["corneal_topography", "unknown", "mendeley", "measurement", "resource-role-current-dataset", "dataset-family-mendeley-performance-corneal-vs-scleral-rigid-gas"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Data for: Performance of corneal vs. scleral rigid gas permeable contact lenses for ectatic corneal disorders

Participant/eye-level clinical and lens-performance outcomes from People with keratoconus or related corneal ectatic disorders in the randomized contact-lens study.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mendeley_performance_corneal_vs_scleral_rigid_gas` |
| **Full name** | Data for: Performance of corneal vs. scleral rigid gas permeable contact lenses for ectatic corneal disorders |
| **Primary category** | `corneal_topography` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `mendeley_performance_corneal_vs_scleral_rigid_gas` |
| **Contained modalities** | corneal_topography |
| **Tasks** | measurement |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | Attribution-NonCommercial 3.0 Unported |
| **Normalized terms** | `unknown` |
| **Descriptive screening label** | Unknown or unclear; do not assume permission |
| **Terms scope** | `unknown` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Mendeley Data |
| **Availability** | `available` (checked 2026-08-02) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

No reproducible primary item count was exposed for the cataloged source version.

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Human provenance: People with keratoconus or related corneal ectatic disorders in the randomized contact-lens study. Source-review finding: Current listing not independently retrievable; source description identifies the corneal-versus-scleral RGP clinical comparison.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mendeley_performance_corneal_vs_scleral_rigid_gas --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download mendeley_performance_corneal_vs_scleral_rigid_gas --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mendeley_performance_corneal_vs_scleral_rigid_gas')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/gmrbh4fvt2/1)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/gmrbh4fvt2)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mendeley_performance_corneal_vs_scleral_rigid_gas,
  title  = { Data for: Performance of corneal vs. scleral rigid gas permeable contact lenses for ectatic corneal disorders },
  note   = { Data for: Performance of corneal vs. scleral rigid gas permeable contact lenses for ectatic corneal disorders. Mendeley Data, V1. doi:10.17632/gmrbh4fvt2.1 },
  url    = { https://data.mendeley.com/datasets/gmrbh4fvt2/1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Data for: Performance of corneal vs. scleral rigid gas permeable contact lenses for ectatic corneal disorders. Mendeley Data, V1. doi:10.17632/gmrbh4fvt2.1.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Attribution-NonCommercial 3.0 Unported
- **Normalized category:** `unknown`
- **Apparent scope:** `unknown`
- **Descriptive screening label:** Unknown or unclear; do not assume permission

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
