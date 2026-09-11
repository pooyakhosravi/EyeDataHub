---
id: mendeley_cust_iris
title: "CUST-Iris"
sidebar_label: mendeley_cust_iris
description: "Observation-level source data, annotations, or signals. from Source explicitly describes consenting human subjects and 720 unique irises."
tags: ["iris_biometrics", "cc-by", "mendeley", "segmentation", "resource-role-current-dataset", "dataset-family-mendeley-cust-iris"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# CUST-Iris

Observation-level source data, annotations, or signals. from Source explicitly describes consenting human subjects and 720 unique irises.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mendeley_cust_iris` |
| **Full name** | CUST-Iris |
| **First published** | 2026-06-22 |
| **Publication date precision** | day |
| **Publication date evidence** | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/3j6skjpsng/1) |
| **Publication date source field** | citation_publication_date (version 1) |
| **Publication date reviewed** | 2026-09-11 |
| **Primary category** | `iris_biometrics` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `mendeley_cust_iris` |
| **Contained modalities** | iris_biometrics |
| **Tasks** | segmentation |
| **Primary reported quantity** | 2,880 images |
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

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 2,880 | `images` | Source-stated quantity Preserved from the source-confirmation record. | `official_source_description` | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/3j6skjpsng) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Human provenance: Source explicitly describes consenting human subjects and 720 unique irises. Source-review finding: One ZIP containing CUST-Iris images.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mendeley_cust_iris --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download mendeley_cust_iris --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mendeley_cust_iris')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/3j6skjpsng/2)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/3j6skjpsng)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mendeley_cust_iris,
  title  = { CUST-Iris },
  note   = { CUST-Iris. Mendeley Data, V2. doi:10.17632/3j6skjpsng.2 },
  url    = { https://data.mendeley.com/datasets/3j6skjpsng/2 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
CUST-Iris. Mendeley Data, V2. doi:10.17632/3j6skjpsng.2.
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

- [nd_iris_0405](./nd_iris_0405.md): ND-IRIS-0405 Iris Image Dataset (64,980 images, `research-only`)
- [casia_iris_v4](./casia_iris_v4.md): CASIA-IrisV4 Iris Image Database (54,601 images, `cc0`)
- [ubiris_v2](./ubiris_v2.md): UBIRIS.v2 Noisy Visible-Wavelength Iris Database (11,102 images, `unknown`)
- [doomgan_ocular_morphs](./doomgan_ocular_morphs.md): DOOMGAN Ocular Morph-Attack Dataset (10,000 images, `mit`)
- [dryad_sbcc2fr6n](./dryad_sbcc2fr6n.md): Exploring phenotypic diversity of pigmented traits and iris features in Pakistani population (514 participants, `cc0`)
- [dryad_iris_surface_features](./dryad_iris_surface_features.md): Iris Surface Features Dataset (Not reported, `cc0`)
