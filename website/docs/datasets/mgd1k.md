---
id: mgd1k
title: "MGD-1k Meibomian Gland Dataset"
sidebar_label: mgd1k
description: "One thousand infrared meibography images with meibomian-gland masks, eyelid masks, and six rounds of expert meiboscore grading."
tags: ["external_eye", "unknown", "github", "segmentation", "grading", "resource-role-current-dataset", "dataset-family-mgd1k"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# MGD-1k Meibomian Gland Dataset

One thousand infrared meibography images with meibomian-gland masks, eyelid masks, and six rounds of expert meiboscore grading.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mgd1k` |
| **Full name** | MGD-1k Meibomian Gland Dataset |
| **Publication date** | Unknown |
| **Date basis** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Date notes** | - |
| **Primary category** | `external_eye` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `mgd1k` |
| **Contained modalities** | external_eye |
| **Tasks** | segmentation, grading |
| **Primary reported quantity** | 1,000 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | Unknown; project page states All Rights Reserved |
| **Normalized terms** | `unknown` |
| **Descriptive screening label** | Unknown or unclear; do not assume permission |
| **Terms scope** | `unknown` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | GitHub |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `loader_implemented_not_live_tested` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 1,000 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [mgd1k.github.io/index.html](https://mgd1k.github.io/index.html) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Official project page reports 1,000 infrared meibomian-gland images from 320 patients, 1,000 gland masks, 1,000 eyelid masks, and six meiboscore rounds. License is not explicit; verify source terms before reuse.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mgd1k --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download mgd1k --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mgd1k')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [mgd1k.github.io/index.html](https://mgd1k.github.io/index.html)

**Source-term evidence:** [mgd1k.github.io/index.html](https://mgd1k.github.io/index.html)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mgd1k,
  title  = { MGD-1k Meibomian Gland Dataset },
  note   = { Saha RK, Chowdhury AM, Na KS, Hwang GD, Eom Y, Kim J, Jeon HG, Hwang HS, Chung E. Automated quantification of meibomian gland dropout in infrared meibography using deep learning. The Ocular Surface. 2022;26:283-294 },
  year   = { 2022 },
  url    = { https://mgd1k.github.io/index.html },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Saha RK, Chowdhury AM, Na KS, Hwang GD, Eom Y, Kim J, Jeon HG, Hwang HS, Chung E. Automated quantification of meibomian gland dropout in infrared meibography using deep learning. The Ocular Surface. 2022;26:283-294.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Unknown; project page states All Rights Reserved
- **Normalized category:** `unknown`
- **Apparent scope:** `unknown`
- **Descriptive screening label:** Unknown or unclear; do not assume permission

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
