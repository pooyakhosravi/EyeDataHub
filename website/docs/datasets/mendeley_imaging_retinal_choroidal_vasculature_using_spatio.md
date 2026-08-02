---
id: mendeley_imaging_retinal_choroidal_vasculature_using_spatio
title: "Imaging the retinal and choroidal vasculature using Spatio-Temporal Optical Coherence Tomography (STOC-T)"
sidebar_label: mendeley_imaging_retinal_choroidal_vasculature_using_spatio
description: "Three-dimensional retinal/choroidal oct image observations from Retinal/choroidal images from eyes imaged with a STOC-T system; source description identifies a study sample but does not provide a veri"
tags: ["octa", "cc-by", "mendeley", "measurement", "resource-role-current-dataset", "dataset-family-mendeley-imaging-retinal-choroidal-vasculature-using-spatio"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Imaging the retinal and choroidal vasculature using Spatio-Temporal Optical Coherence Tomography (STOC-T)

Three-dimensional retinal/choroidal oct image observations from Retinal/choroidal images from eyes imaged with a STOC-T system; source description identifies a study sample but does not provide a verified count.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mendeley_imaging_retinal_choroidal_vasculature_using_spatio` |
| **Full name** | Imaging the retinal and choroidal vasculature using Spatio-Temporal Optical Coherence Tomography (STOC-T) |
| **Primary category** | `octa` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `mendeley_imaging_retinal_choroidal_vasculature_using_spatio` |
| **Contained modalities** | octa |
| **Tasks** | measurement |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | Creative Commons Attribution 4.0 International |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
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

> Human provenance: Retinal/choroidal images from eyes imaged with a STOC-T system; source description identifies a study sample but does not provide a verified count. Source-review finding: Current listing not independently retrievable; source description states high-resolution three-dimensional STOC-T retinal images.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mendeley_imaging_retinal_choroidal_vasculature_using_spatio --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download mendeley_imaging_retinal_choroidal_vasculature_using_spatio --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mendeley_imaging_retinal_choroidal_vasculature_using_spatio')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/j39vyvp8ny/1)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/j39vyvp8ny)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mendeley_imaging_retinal_choroidal_vasculature_using_spatio,
  title  = { Imaging the retinal and choroidal vasculature using Spatio-Temporal Optical Coherence Tomography (STOC-T) },
  note   = { Imaging the retinal and choroidal vasculature using Spatio-Temporal Optical Coherence Tomography (STOC-T). Mendeley Data, V1. doi:10.17632/j39vyvp8ny.1 },
  url    = { https://data.mendeley.com/datasets/j39vyvp8ny/1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Imaging the retinal and choroidal vasculature using Spatio-Temporal Optical Coherence Tomography (STOC-T). Mendeley Data, V1. doi:10.17632/j39vyvp8ny.1.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Creative Commons Attribution 4.0 International
- **Normalized category:** `cc-by`
- **Apparent scope:** `unknown`
- **Descriptive screening label:** Standard label without an explicit NC clause; not a permission finding

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [octa_macula_coronal](./octa_macula_coronal.md): OCTA Macula Coronal Views (82,560 images, `cc-by`)
- [octa_500](./octa_500.md): OCTA-500: Large-scale OCTA Multi-task Benchmark (500 participants, `research-only`)
- [aroma_octa](./aroma_octa.md): AROMA Retinal OCTA Artifact Dataset (281 images, `cc-by`)
- [rose](./rose.md): ROSE: Retinal OCT-Angiography Vessel Segmentation (229 images, `cc-by`)
- [soul_octa](./soul_octa.md): SOUL: OCTA Human-Machine Collaborative Annotation Dataset (178 longitudinal samples, `cc-by`)
- [drac22](./drac22.md): DRAC 2022: Diabetic Retinopathy Analysis Challenge (174 images, `cc-by`)
- [ut_fsocta](./ut_fsocta.md): UTHealth Fundus and Synthetic OCTA Dataset (112 participants, `unknown`)
- [dryad_preeclampsia_ocular_octa](./dryad_preeclampsia_ocular_octa.md): Plane wave ultrasound and OCT angiography of the eye in preeclampsia (Not reported, `cc0`)
