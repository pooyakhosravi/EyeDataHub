---
id: sustech_sysu_corneal_ulcers
title: "SUSTech-SYSU Corneal Ulcer Dataset"
sidebar_label: sustech_sysu_corneal_ulcers
description: "Human corneal-ulcer clinical images and labels."
tags: ["external_eye", "cc-by", "figshare", "classification", "resource-role-current-dataset", "dataset-family-sustech-sysu-corneal-ulcers"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# SUSTech-SYSU Corneal Ulcer Dataset

Human corneal-ulcer clinical images and labels.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `sustech_sysu_corneal_ulcers` |
| **Full name** | SUSTech-SYSU Corneal Ulcer Dataset |
| **Publication date** | 2020-01-13 |
| **Date basis** | Initial dataset release |
| **Publication date precision** | day |
| **Publication date evidence** | [api.figshare.com/v2](https://api.figshare.com/v2/articles/10247501/versions/1) |
| **Publication date source field** | published_date (Figshare version 1) |
| **Publication date reviewed** | 2026-09-11 |
| **Date notes** | Only listed Figshare version. |
| **Primary category** | `external_eye` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `sustech_sysu_corneal_ulcers` |
| **Contained modalities** | external_eye |
| **Tasks** | classification |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Figshare |
| **Availability** | `available` (checked 2026-08-02) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

No reproducible primary item count was exposed for the cataloged source version.

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download sustech_sysu_corneal_ulcers --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download sustech_sysu_corneal_ulcers --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('sustech_sysu_corneal_ulcers')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.6084/m9.figshare.10247501.v1](https://doi.org/10.6084/m9.figshare.10247501.v1)

**Source-term evidence:** [https://doi.org/10.6084/m9.figshare.10247501.v1](https://doi.org/10.6084/m9.figshare.10247501.v1)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{sustech_sysu_corneal_ulcers,
  title  = { SUSTech-SYSU Corneal Ulcer Dataset },
  note   = { Repository dataset record. 10.6084/m9.figshare.10247501.v1 },
  url    = { https://doi.org/10.6084/m9.figshare.10247501.v1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Repository dataset record. 10.6084/m9.figshare.10247501.v1.
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
- [popeye_nir](./popeye_nir.md): PopEYE Infrared Ocular Image Dataset (14,976 images, `cc-by`)
- [dryad_fungal_keratitis_cci](./dryad_fungal_keratitis_cci.md): CCI.net fungal keratitis cases dataset (8,697 images, `cc0`)
- [mcoa](./mcoa.md): MCOA: Multimodal Corneal Opacity Assessment Dataset (6,664 images, `cc-by`)
- [tear_meniscus](./tear_meniscus.md): Multicentre Tear Meniscus Segmentation Dataset (3,432 images, `cc-by`)
- [uveitis_smote](./uveitis_smote.md): Image Dataset on Eye Diseases Classification with Symptoms and SMOTE Validation (3,245 images, `cc-by`)
