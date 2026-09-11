---
id: mcoa
title: "MCOA: Multimodal Corneal Opacity Assessment Dataset"
sidebar_label: mcoa
description: "6,272 AS-OCT images + 392 anterior-segment photographs for corneal opacity assessment with expert grading. First large public multimodal AS-OCT + photo dataset for cornea."
tags: ["multimodal", "oct", "external_eye", "cc-by", "figshare", "classification", "grading", "resource-role-current-dataset", "dataset-family-mcoa"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# MCOA: Multimodal Corneal Opacity Assessment Dataset

6,272 AS-OCT images + 392 anterior-segment photographs for corneal opacity assessment with expert grading. First large public multimodal AS-OCT + photo dataset for cornea.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mcoa` |
| **Full name** | MCOA: Multimodal Corneal Opacity Assessment Dataset |
| **First published** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Primary category** | `multimodal` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `mcoa` |
| **Contained modalities** | oct, external_eye |
| **Tasks** | classification, grading |
| **Primary reported quantity** | 6,664 images |
| **Classes** | 4 (Not reported) |
| **Splits** | all |
| **Size** | 8.0 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Figshare |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `end_to_end_tested` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 6,664 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [https://doi.org/10.6084/m9.figshare.28123088.v1](https://doi.org/10.6084/m9.figshare.28123088.v1) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Anterior-segment expansion; modality otherwise sparse.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mcoa --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download mcoa --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mcoa')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.6084/m9.figshare.28123088.v1](https://doi.org/10.6084/m9.figshare.28123088.v1)

**Source-term evidence:** [https://doi.org/10.6084/m9.figshare.28123088.v1](https://doi.org/10.6084/m9.figshare.28123088.v1)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mcoa,
  title  = { MCOA: Multimodal Corneal Opacity Assessment Dataset },
  note   = { Ma X, et al., 'MCOA: A comprehensive multimodal dataset for advancing deep learning in corneal opacity assessment', Scientific Data 2025 },
  year   = { 2025 },
  url    = { https://doi.org/10.6084/m9.figshare.28123088.v1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Ma X, et al., 'MCOA: A comprehensive multimodal dataset for advancing deep learning in corneal opacity assessment', Scientific Data 2025.
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

- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [x_pcr](./x_pcr.md): X-PCR Ophthalmology Progressive Clinical Reasoning Benchmark (18,735 rows, `unknown`)
- [ophthalvqa](./ophthalvqa.md): OphthalVQA Dataset (600 question answer pairs, `cc-by`)
- [syn_oct](./syn_oct.md): SYN-OCT Synthetic Glaucoma OCT Dataset (200,000 images, `cc-by`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (103,959 images, `mit`)
- [kermany_oct](./kermany_oct.md): Kermany OCT 2018: Retinal OCT Image Classification (84,484 images, `cc-by`)
- [harvard_fairvision](./harvard_fairvision.md): Harvard-FairVision (AMD + DR + Glaucoma, paired SLO + OCT) (30,000 participants, `cc-by-nc-nd`)
