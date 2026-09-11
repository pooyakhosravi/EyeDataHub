---
id: nd_iris_0405
title: "ND-IRIS-0405 Iris Image Dataset"
sidebar_label: nd_iris_0405
description: "Longitudinal near-infrared iris images with subject, eye, age, sex, and ethnicity metadata used in ICE iris-recognition evaluations."
tags: ["iris_biometrics", "research-only", "manual", "biometric_recognition", "classification", "demographic_analysis", "resource-role-current-dataset", "dataset-family-nd-iris-0405"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# ND-IRIS-0405 Iris Image Dataset

Longitudinal near-infrared iris images with subject, eye, age, sex, and ethnicity metadata used in ICE iris-recognition evaluations.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `nd_iris_0405` |
| **Full name** | ND-IRIS-0405 Iris Image Dataset |
| **Publication date** | 2009 |
| **Date basis** | Associated publication |
| **Publication date precision** | year |
| **Publication date evidence** | [cvrl.nd.edu/publications](https://cvrl.nd.edu/publications/) |
| **Publication date source field** | Notre Dame CVRL publications listing: Published 2009 section and card anchor 2009-05-01 |
| **Publication date reviewed** | 2026-09-11 |
| **Date notes** | CVRL lists the technical report under 2009. The associated preprint was uploaded in June 2016. |
| **Primary category** | `iris_biometrics` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `nd_iris_0405` |
| **Contained modalities** | iris_biometrics |
| **Tasks** | biometric_recognition, classification, demographic_analysis |
| **Primary reported quantity** | 64,980 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | Research use under a signed institutional data license agreement |
| **Normalized terms** | `research-only` |
| **Descriptive screening label** | Research or challenge restriction recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `controlled_or_manual` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `manual_access_blocked` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 64,980 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [tsapps.nist.gov/BDbC](https://tsapps.nist.gov/BDbC/Search/Details/371) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> The current NIST catalog record reports 64,980 images from 356 participants and 712 irises. Access requires an institutional license signed by an authorized representative; approval and download instructions are issued by Notre Dame.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# This route requires upstream human action; no transfer starts.
eyehub download nd_iris_0405 --data-dir ./data --dry-run --json
# Follow the official instructions shown by preflight.
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('nd_iris_0405')
print(preflight_dataset(ds, './data'))  # returns manual_access_blocked
```

  </TabItem>
</Tabs>

**Upstream page:** [tsapps.nist.gov/BDbC](https://tsapps.nist.gov/BDbC/Search/Details/371)

**Source-term evidence:** [tsapps.nist.gov/BDbC](https://tsapps.nist.gov/BDbC/Search/Details/371)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{nd_iris_0405,
  title  = { ND-IRIS-0405 Iris Image Dataset },
  note   = { Bowyer KW, Flynn PJ. The ND-IRIS-0405 Iris Image Dataset. arXiv:1606.04853. 2016 },
  year   = { 2016 },
  url    = { https://tsapps.nist.gov/BDbC/Search/Details/371 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Bowyer KW, Flynn PJ. The ND-IRIS-0405 Iris Image Dataset. arXiv:1606.04853. 2016.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Research use under a signed institutional data license agreement
- **Normalized category:** `research-only`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Research or challenge restriction recorded; check source

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [casia_iris_v4](./casia_iris_v4.md): CASIA-IrisV4 Iris Image Database (54,601 images, `cc0`)
- [ubiris_v2](./ubiris_v2.md): UBIRIS.v2 Noisy Visible-Wavelength Iris Database (11,102 images, `unknown`)
- [doomgan_ocular_morphs](./doomgan_ocular_morphs.md): DOOMGAN Ocular Morph-Attack Dataset (10,000 images, `mit`)
- [mendeley_cust_iris](./mendeley_cust_iris.md): CUST-Iris (2,880 images, `cc-by`)
- [dryad_sbcc2fr6n](./dryad_sbcc2fr6n.md): Exploring phenotypic diversity of pigmented traits and iris features in Pakistani population (514 participants, `cc0`)
- [dryad_iris_surface_features](./dryad_iris_surface_features.md): Iris Surface Features Dataset (Not reported, `cc0`)
