---
id: keratoconus_detection_kaggle
title: "Keratoconus Detection Corneal Maps"
sidebar_label: keratoconus_detection_kaggle
description: "Corneal map images for three-class keratoconus detection."
tags: ["corneal_topography", "unknown", "kaggle", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Keratoconus Detection Corneal Maps

Corneal map images for three-class keratoconus detection.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `keratoconus_detection_kaggle` |
| **Full name** | Keratoconus Detection Corneal Maps |
| **Primary category** | `corneal_topography` |
| **Contained modalities** | corneal_topography |
| **Tasks** | classification |
| **Primary reported quantity** | 573 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.5 GB |
| **Source-stated terms** | Unknown |
| **Normalized terms** | `unknown` |
| **Descriptive screening label** | Unknown or unclear; do not assume permission |
| **Terms scope** | `unknown` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Kaggle |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 573 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [kaggle.com/datasets](https://www.kaggle.com/datasets/elmehdi12/keratoconus-detection) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download keratoconus_detection_kaggle --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download keratoconus_detection_kaggle --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('keratoconus_detection_kaggle')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [kaggle.com/datasets](https://www.kaggle.com/datasets/elmehdi12/keratoconus-detection)

**Source-term evidence:** [kaggle.com/datasets](https://www.kaggle.com/datasets/elmehdi12/keratoconus-detection)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{keratoconus_detection_kaggle,
  title  = { Keratoconus Detection Corneal Maps },
  note   = { Keratoconus detection dataset. Kaggle, accessed 2026-07 },
  year   = { 2026 },
  url    = { https://www.kaggle.com/datasets/elmehdi12/keratoconus-detection },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Keratoconus detection dataset. Kaggle, accessed 2026-07.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Unknown
- **Normalized category:** `unknown`
- **Apparent scope:** `unknown`
- **Descriptive screening label:** Unknown or unclear; do not assume permission

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [cornorb](./cornorb.md): CornOrb: Orbscan Corneal Topography and Clinical Annotations (1,454 eyes, `cc-by`)
- [dryad_pediatric_corneal_endothelium](./dryad_pediatric_corneal_endothelium.md): Corneal endothelial morphology of healthy myopic Malaysian children of Chinese ethnicity aged 8-9 years and its association with axial length (111 participants, `cc0`)
- [dryad_cornea_oct_pentacam](./dryad_cornea_oct_pentacam.md): Corneal OCT and Pentacam Tomography Dataset (52 participants, `cc0`)
- [dryad_corneal_biomechanics_prostaglandin](./dryad_corneal_biomechanics_prostaglandin.md): Changes in corneal biomechanical properties after long-term topical prostaglandin therapy (Not reported, `cc0`)
