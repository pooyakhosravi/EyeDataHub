---
id: popeye_nir
title: "PopEYE Infrared Ocular Image Dataset"
sidebar_label: popeye_nir
description: "Fourteen thousand nine hundred seventy-six near-infrared ocular images for eye-state detection and coarse gaze-direction classification during ophthalmic measurement workflows."
tags: ["external_eye", "cc-by", "zenodo", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# PopEYE Infrared Ocular Image Dataset

Fourteen thousand nine hundred seventy-six near-infrared ocular images for eye-state detection and coarse gaze-direction classification during ophthalmic measurement workflows.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `popeye_nir` |
| **Full name** | PopEYE Infrared Ocular Image Dataset |
| **Primary category** | `external_eye` |
| **Contained modalities** | external_eye |
| **Tasks** | classification |
| **Primary reported quantity** | 14,976 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 3.0 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Zenodo |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 14,976 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [zenodo.org/records](https://zenodo.org/records/18430187) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download popeye_nir --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download popeye_nir --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('popeye_nir')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [zenodo.org/records](https://zenodo.org/records/18430187)

**Source-term evidence:** [zenodo.org/records](https://zenodo.org/records/18430187)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{popeye_nir,
  title  = { PopEYE Infrared Ocular Image Dataset },
  note   = { Gibertoni G, Borghi G, Rovati L. PopEYE - Infrared Ocular Image Dataset for Eye State and Gaze-Direction Classification. Zenodo, 2026. doi:10.5281/zenodo.18430187 },
  year   = { 2026 },
  url    = { https://zenodo.org/records/18430187 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Gibertoni G, Borghi G, Rovati L. PopEYE - Infrared Ocular Image Dataset for Eye State and Gaze-Direction Classification. Zenodo, 2026. doi:10.5281/zenodo.18430187
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
- [dryad_fungal_keratitis_cci](./dryad_fungal_keratitis_cci.md): CCI.net fungal keratitis cases dataset (8,697 images, `cc0`)
- [mcoa](./mcoa.md): MCOA: Multimodal Corneal Opacity Assessment Dataset (6,664 images, `cc-by`)
- [tear_meniscus](./tear_meniscus.md): Multicentre Tear Meniscus Segmentation Dataset (3,432 images, `cc-by`)
- [uveitis_smote](./uveitis_smote.md): Image Dataset on Eye Diseases Classification with Symptoms and SMOTE Validation (3,245 images, `cc-by`)
- [eed_astig](./eed_astig.md): EED-Astig Pediatric External-Eye Dataset (3,088 images, `research-only`)
