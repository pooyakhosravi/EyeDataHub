---
id: doomgan_ocular_morphs
title: "DOOMGAN Ocular Morph-Attack Dataset"
sidebar_label: doomgan_ocular_morphs
description: "Synthetic visible-spectrum ocular biometric morph images generated from documented human VISOB source imagery."
tags: ["iris_biometrics", "iris", "mit", "huggingface", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# DOOMGAN Ocular Morph-Attack Dataset

Synthetic visible-spectrum ocular biometric morph images generated from documented human VISOB source imagery.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `doomgan_ocular_morphs` |
| **Full name** | DOOMGAN Ocular Morph-Attack Dataset |
| **Primary category** | `iris_biometrics` |
| **Contained modalities** | iris_biometrics, iris |
| **Tasks** | classification |
| **Primary reported quantity** | 10,000 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | MIT |
| **Normalized terms** | `mit` |
| **Descriptive screening label** | Standard label without an explicit NC clause; verify that it applies to data |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | HuggingFace Hub |
| **Availability** | `available` (checked 2026-08-02) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 10,000 | `images` | Source reports 10,000 morphed PNG images. Source-stated quantity; repository file count is separate. | `official_source_description` | [huggingface.co/datasets](https://huggingface.co/datasets/BharathK333/DOOMGAN-Ocular-Morphs) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Synthetic derivative of VISOB; upstream VISOB is not a current catalog record.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download doomgan_ocular_morphs --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download doomgan_ocular_morphs --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('doomgan_ocular_morphs')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [huggingface.co/datasets](https://huggingface.co/datasets/BharathK333/DOOMGAN-Ocular-Morphs)

**Source-term evidence:** [huggingface.co/datasets](https://huggingface.co/datasets/BharathK333/DOOMGAN-Ocular-Morphs)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{doomgan_ocular_morphs,
  title  = { DOOMGAN Ocular Morph-Attack Dataset },
  note   = { Repository dataset record. BharathK333/DOOMGAN-Ocular-Morphs },
  url    = { https://huggingface.co/datasets/BharathK333/DOOMGAN-Ocular-Morphs },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Repository dataset record. BharathK333/DOOMGAN-Ocular-Morphs.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** MIT
- **Normalized category:** `mit`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Standard label without an explicit NC clause; verify that it applies to data

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [nd_iris_0405](./nd_iris_0405.md): ND-IRIS-0405 Iris Image Dataset (64,980 images, `research-only`)
- [casia_iris_v4](./casia_iris_v4.md): CASIA-IrisV4 Iris Image Database (54,601 images, `cc0`)
- [ubiris_v2](./ubiris_v2.md): UBIRIS.v2 Noisy Visible-Wavelength Iris Database (11,102 images, `unknown`)
- [mendeley_cust_iris](./mendeley_cust_iris.md): CUST-Iris (2,880 images, `cc-by`)
- [dryad_sbcc2fr6n](./dryad_sbcc2fr6n.md): Exploring phenotypic diversity of pigmented traits and iris features in Pakistani population (514 participants, `cc0`)
- [dryad_iris_surface_features](./dryad_iris_surface_features.md): Iris Surface Features Dataset (Not reported, `cc0`)
