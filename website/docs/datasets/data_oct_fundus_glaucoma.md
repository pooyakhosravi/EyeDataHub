---
id: data_oct_fundus_glaucoma
title: "Data on OCT and Fundus Images"
sidebar_label: data_oct_fundus_glaucoma
description: "Fifty OCT and fundus images with healthy/glaucomatous labels and cup-to-disc ratio annotations by ophthalmologists."
tags: ["multimodal", "fundus", "oct", "cc-by", "mendeley", "classification", "grading", "resource-role-current-dataset", "dataset-family-data-oct-fundus-glaucoma"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Data on OCT and Fundus Images

Fifty OCT and fundus images with healthy/glaucomatous labels and cup-to-disc ratio annotations by ophthalmologists.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `data_oct_fundus_glaucoma` |
| **Full name** | Data on OCT and Fundus Images |
| **Primary category** | `multimodal` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `data_oct_fundus_glaucoma` |
| **Contained modalities** | fundus, oct |
| **Tasks** | classification, grading |
| **Primary reported quantity** | 50 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.1 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Mendeley Data |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 50 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/2rnnz5nz74/2) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download data_oct_fundus_glaucoma --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download data_oct_fundus_glaucoma --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('data_oct_fundus_glaucoma')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/2rnnz5nz74/2)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/2rnnz5nz74/2)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{data_oct_fundus_glaucoma,
  title  = { Data on OCT and Fundus Images },
  note   = { Raja H, Akram MU, Ramzan A, Khalil T, Nazid N. Data on OCT and Fundus Images. Mendeley Data, V2, 2020. doi:10.17632/2rnnz5nz74.2 },
  year   = { 2020 },
  url    = { https://data.mendeley.com/datasets/2rnnz5nz74/2 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Raja H, Akram MU, Ramzan A, Khalil T, Nazid N. Data on OCT and Fundus Images. Mendeley Data, V2, 2020. doi:10.17632/2rnnz5nz74.2
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

- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (103,959 images, `mit`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [harvard_fairvision](./harvard_fairvision.md): Harvard-FairVision (AMD + DR + Glaucoma, paired SLO + OCT) (30,000 participants, `cc-by-nc-nd`)
- [mmrdr](./mmrdr.md): MMRDR: Multi-Modal Retinal Diabetic Retinopathy Dataset (24,460 images, `cc-by`)
- [x_pcr](./x_pcr.md): X-PCR Ophthalmology Progressive Clinical Reasoning Benchmark (18,735 rows, `unknown`)
- [olives](./olives.md): OLIVES: Ophthalmic Labels for Investigating Visual Eye Semantics (9,408 b scans, `cc-by`)
- [oct_fundus_dme_dr_mexico](./oct_fundus_dme_dr_mexico.md): OCT and Eye Fundus Dataset for DME and DR (2,661 images, `unknown`)
