---
id: mendeley_human_mesenchymal_stem_cells_derived_adipose
title: "Human mesenchymal stem cells derived from adipose tissue showed greater effect than from umbilical cord in promoting corneal graft survival through suppressing lymphangiogenesis"
sidebar_label: mendeley_human_mesenchymal_stem_cells_derived_adipose
description: "Observation-level source data, annotations, or signals. from Human adipose- and umbilical-cord-derived mesenchymal stem cells are stated."
tags: ["corneal_topography", "cc-by", "mendeley", "measurement", "resource-role-current-dataset", "dataset-family-mendeley-human-mesenchymal-stem-cells-derived-adipose"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Human mesenchymal stem cells derived from adipose tissue showed greater effect than from umbilical cord in promoting corneal graft survival through suppressing lymphangiogenesis

Observation-level source data, annotations, or signals. from Human adipose- and umbilical-cord-derived mesenchymal stem cells are stated.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mendeley_human_mesenchymal_stem_cells_derived_adipose` |
| **Full name** | Human mesenchymal stem cells derived from adipose tissue showed greater effect than from umbilical cord in promoting corneal graft survival through suppressing lymphangiogenesis |
| **Primary category** | `corneal_topography` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `mendeley_human_mesenchymal_stem_cells_derived_adipose` |
| **Contained modalities** | corneal_topography |
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
| **Route backend** | Mendeley Data |
| **Availability** | `available` (checked 2026-08-02) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

No reproducible primary item count was exposed for the cataloged source version.

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Human provenance: Human adipose- and umbilical-cord-derived mesenchymal stem cells are stated. Source-review finding: One XLSX RNA-sequencing data workbook.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mendeley_human_mesenchymal_stem_cells_derived_adipose --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download mendeley_human_mesenchymal_stem_cells_derived_adipose --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mendeley_human_mesenchymal_stem_cells_derived_adipose')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/bm45p4tcbz/1)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/bm45p4tcbz)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mendeley_human_mesenchymal_stem_cells_derived_adipose,
  title  = { Human mesenchymal stem cells derived from adipose tissue showed greater effect than from umbilical cord in promoting corneal graft survival through suppressing lymphangiogenesis },
  note   = { Human mesenchymal stem cells derived from adipose tissue showed greater effect than from umbilical cord in promoting corneal graft survival through suppressing lymphangiogenesis. Mendeley Data, V1. doi:10.17632/bm45p4tcbz.1 },
  url    = { https://data.mendeley.com/datasets/bm45p4tcbz/1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Human mesenchymal stem cells derived from adipose tissue showed greater effect than from umbilical cord in promoting corneal graft survival through suppressing lymphangiogenesis. Mendeley Data, V1. doi:10.17632/bm45p4tcbz.1.
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
- [mendeley_biomechanical_properties_adult_patients_high_myopia](./mendeley_biomechanical_properties_adult_patients_high_myopia.md): Biomechanical properties of adult patients with high myopia after implantable collamer lens (ICL, V4) implantation (110 eyes, `cc-by`)
- [dryad_cornea_oct_pentacam](./dryad_cornea_oct_pentacam.md): Corneal OCT and Pentacam Tomography Dataset (52 participants, `cc0`)
- [casia2_as_oct_repeatability](./casia2_as_oct_repeatability.md): CASIA2 Anterior-Segment OCT Repeatability Dataset (Not reported, `cc-by`)
- [casia2_keratometric_astigmatism](./casia2_keratometric_astigmatism.md): CASIA2 Keratometric Astigmatism Dataset (Not reported, `cc-by`)
