---
id: ubiris_v2
title: "UBIRIS.v2 Noisy Visible-Wavelength Iris Database"
sidebar_label: ubiris_v2
description: "Visible-light iris images captured at a distance and on the move with realistic blur, reflection, occlusion, pose, and illumination noise."
tags: ["iris_biometrics", "unknown", "manual", "biometric_recognition", "classification", "resource-role-current-dataset", "dataset-family-ubiris-v2"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# UBIRIS.v2 Noisy Visible-Wavelength Iris Database

Visible-light iris images captured at a distance and on the move with realistic blur, reflection, occlusion, pose, and illumination noise.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `ubiris_v2` |
| **Full name** | UBIRIS.v2 Noisy Visible-Wavelength Iris Database |
| **Publication date** | Unknown |
| **Date basis** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Date notes** | - |
| **Primary category** | `iris_biometrics` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `ubiris_v2` |
| **Contained modalities** | iris_biometrics |
| **Tasks** | biometric_recognition, classification |
| **Primary reported quantity** | 11,102 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | Unknown; request access and verify UBIRIS.v2-specific terms |
| **Normalized terms** | `unknown` |
| **Descriptive screening label** | Unknown or unclear; do not assume permission |
| **Terms scope** | `unknown` |
| **Access friction** | `controlled_or_manual` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `manual_access_blocked` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 11,102 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [iris.di.ubi.pt/index.html](https://iris.di.ubi.pt/index.html) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> The official readme reports 11,102 images from 261 participants and 522 irises. The site states that UBIRIS.v1 is public and that newer UBIPr derivatives use CC BY-NC-SA 4.0, but it does not make the same license statement for UBIRIS.v2; terms are therefore unknown.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# This route requires upstream human action; no transfer starts.
eyehub download ubiris_v2 --data-dir ./data --dry-run --json
# Follow the official instructions shown by preflight.
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('ubiris_v2')
print(preflight_dataset(ds, './data'))  # returns manual_access_blocked
```

  </TabItem>
</Tabs>

**Upstream page:** [iris.di.ubi.pt/index.html](https://iris.di.ubi.pt/index.html)

**Source-term evidence:** [iris.di.ubi.pt/index.html](https://iris.di.ubi.pt/index.html)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{ubiris_v2,
  title  = { UBIRIS.v2 Noisy Visible-Wavelength Iris Database },
  note   = { Proenca H, Filipe S, Santos R, Oliveira J, Alexandre LA. The UBIRIS.v2: A Database of Visible Wavelength Iris Images Captured On-the-Move and At-a-Distance. IEEE TPAMI. 2010;32:1529-1535 },
  year   = { 2010 },
  url    = { https://iris.di.ubi.pt/index.html },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Proenca H, Filipe S, Santos R, Oliveira J, Alexandre LA. The UBIRIS.v2: A Database of Visible Wavelength Iris Images Captured On-the-Move and At-a-Distance. IEEE TPAMI. 2010;32:1529-1535.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Unknown; request access and verify UBIRIS.v2-specific terms
- **Normalized category:** `unknown`
- **Apparent scope:** `unknown`
- **Descriptive screening label:** Unknown or unclear; do not assume permission

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [nd_iris_0405](./nd_iris_0405.md): ND-IRIS-0405 Iris Image Dataset (64,980 images, `research-only`)
- [casia_iris_v4](./casia_iris_v4.md): CASIA-IrisV4 Iris Image Database (54,601 images, `cc0`)
- [doomgan_ocular_morphs](./doomgan_ocular_morphs.md): DOOMGAN Ocular Morph-Attack Dataset (10,000 images, `mit`)
- [mendeley_cust_iris](./mendeley_cust_iris.md): CUST-Iris (2,880 images, `cc-by`)
- [dryad_sbcc2fr6n](./dryad_sbcc2fr6n.md): Exploring phenotypic diversity of pigmented traits and iris features in Pakistani population (514 participants, `cc0`)
- [dryad_iris_surface_features](./dryad_iris_surface_features.md): Iris Surface Features Dataset (Not reported, `cc0`)
