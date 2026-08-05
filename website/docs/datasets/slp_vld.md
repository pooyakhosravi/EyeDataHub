---
id: slp_vld
title: "SLP-VLD Anonymized Slit-Lamp Vision-Language Dataset"
sidebar_label: slp_vld
description: "Anonymized slit-lamp photographs with English clinical annotations and vision-language conversations."
tags: ["external_eye", "slit_lamp", "cc-by", "figshare", "classification", "image_text", "resource-role-current-dataset", "dataset-family-slp-vld", "alternate-source", "source-figshare", "alternate-role-previous-version"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# SLP-VLD Anonymized Slit-Lamp Vision-Language Dataset

Anonymized slit-lamp photographs with English clinical annotations and vision-language conversations.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `slp_vld` |
| **Full name** | SLP-VLD Anonymized Slit-Lamp Vision-Language Dataset |
| **Primary category** | `external_eye` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `slp_vld` |
| **Contained modalities** | external_eye, slit_lamp |
| **Tasks** | classification, image_text |
| **Primary reported quantity** | 2,228 images |
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

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 2,228 | `images` | Source reports 2,228 slit-lamp photographs. Source-stated quantity; repository file count is separate. | `official_source_description` | [https://doi.org/10.6084/m9.figshare.32576697.v3](https://doi.org/10.6084/m9.figshare.32576697.v3) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download slp_vld --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download slp_vld --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('slp_vld')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.6084/m9.figshare.32576697.v3](https://doi.org/10.6084/m9.figshare.32576697.v3)

## Other documented locations

These links identify alternate deposits, components, metadata records, mirrors, versions, or related derived materials. They do not create additional canonical catalog records.

- [figshare: previous version (32592837)](https://figshare.com/articles/dataset/32592837): Alternate deposit.
- [figshare: previous version (32593101)](https://figshare.com/articles/dataset/32593101): Alternate deposit.
- [figshare: previous version (32593173)](https://figshare.com/articles/dataset/32593173): Alternate deposit.

**Source-term evidence:** [https://doi.org/10.6084/m9.figshare.32576697.v3](https://doi.org/10.6084/m9.figshare.32576697.v3)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{slp_vld,
  title  = { SLP-VLD Anonymized Slit-Lamp Vision-Language Dataset },
  note   = { Repository dataset record. 10.6084/m9.figshare.32576697.v3 },
  url    = { https://doi.org/10.6084/m9.figshare.32576697.v3 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Repository dataset record. 10.6084/m9.figshare.32576697.v3.
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

- [slid_e](./slid_e.md): SLID-E Slit-Lamp Image Dataset for Epiphora (2,999 images, `cc-by`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [x_pcr](./x_pcr.md): X-PCR Ophthalmology Progressive Clinical Reasoning Benchmark (18,735 rows, `unknown`)
- [popeye_nir](./popeye_nir.md): PopEYE Infrared Ocular Image Dataset (14,976 images, `cc-by`)
- [dryad_fungal_keratitis_cci](./dryad_fungal_keratitis_cci.md): CCI.net fungal keratitis cases dataset (8,697 images, `cc0`)
- [mcoa](./mcoa.md): MCOA: Multimodal Corneal Opacity Assessment Dataset (6,664 images, `cc-by`)
- [tear_meniscus](./tear_meniscus.md): Multicentre Tear Meniscus Segmentation Dataset (3,432 images, `cc-by`)
