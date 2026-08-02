---
id: thyroid_ophthalmopathy_external
title: "Thyroid Ophthalmopathy External Ocular Images"
sidebar_label: thyroid_ophthalmopathy_external
description: "External ocular photographs of thyroid eye disease collected from web sources, with surgery-related images removed by the source curator."
tags: ["external_eye", "cc-by", "mendeley", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Thyroid Ophthalmopathy External Ocular Images

External ocular photographs of thyroid eye disease collected from web sources, with surgery-related images removed by the source curator.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `thyroid_ophthalmopathy_external` |
| **Full name** | Thyroid Ophthalmopathy External Ocular Images |
| **Primary category** | `external_eye` |
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
| **Route backend** | Mendeley Data |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Additional | 2 | `deposited_files` | Artifacts listed by the current Mendeley v2 deposit The source does not report the number of photographs inside dataset.zip. | `current_deposit_file_listing` | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/z7ys7r4bdn/2) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Source title spells thyroid as 'Thyriod'. Web-sourced photographs; verify image provenance before clinical validation or redistribution.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download thyroid_ophthalmopathy_external --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download thyroid_ophthalmopathy_external --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('thyroid_ophthalmopathy_external')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/z7ys7r4bdn/2)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/z7ys7r4bdn/2)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{thyroid_ophthalmopathy_external,
  title  = { Thyroid Ophthalmopathy External Ocular Images },
  note   = { Yoo T. Thyriod ophthalmopathy - external ocular images. Mendeley Data, V2, 2024. doi:10.17632/z7ys7r4bdn.2 },
  year   = { 2024 },
  url    = { https://data.mendeley.com/datasets/z7ys7r4bdn/2 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Yoo T. Thyriod ophthalmopathy - external ocular images. Mendeley Data, V2, 2024. doi:10.17632/z7ys7r4bdn.2
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
