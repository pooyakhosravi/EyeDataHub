---
id: mendeley_red_lesion_localization_messidor_retinal_images
title: "Red lesion localization for MESSIDOR retinal images dataset using patch-based convolutional neural networks."
sidebar_label: mendeley_red_lesion_localization_messidor_retinal_images
description: "Observation-level source data, annotations, or signals. from MESSIDOR is a human retinal-image benchmark; this deposit adds lesion-localization data."
tags: ["fundus", "tabular", "cc-by", "mendeley", "segmentation", "resource-role-current-dataset", "dataset-family-mendeley-red-lesion-localization-messidor-retinal-images"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Red lesion localization for MESSIDOR retinal images dataset using patch-based convolutional neural networks.

Observation-level source data, annotations, or signals. from MESSIDOR is a human retinal-image benchmark; this deposit adds lesion-localization data.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mendeley_red_lesion_localization_messidor_retinal_images` |
| **Full name** | Red lesion localization for MESSIDOR retinal images dataset using patch-based convolutional neural networks. |
| **First published** | 2019-05-30 |
| **Publication date precision** | day |
| **Publication date evidence** | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/3r5m3nfdkv/1) |
| **Publication date source field** | citation_publication_date (version 1) |
| **Publication date reviewed** | 2026-09-11 |
| **Primary category** | `fundus` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `mendeley_red_lesion_localization_messidor_retinal_images` |
| **Contained modalities** | fundus, tabular |
| **Tasks** | segmentation |
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
| **Availability** | `available` (checked 2026-08-02) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

No reproducible primary item count was exposed for the cataloged source version.

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Human provenance: MESSIDOR is a human retinal-image benchmark; this deposit adds lesion-localization data. Source-review finding: 1,200 PNG files plus one CSV annotation file. The source identifies a MESSIDOR-family annotation layer, but the exact catalog edition was not established; no record-to-record edge is encoded.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mendeley_red_lesion_localization_messidor_retinal_images --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download mendeley_red_lesion_localization_messidor_retinal_images --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mendeley_red_lesion_localization_messidor_retinal_images')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/3r5m3nfdkv/1)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/3r5m3nfdkv)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mendeley_red_lesion_localization_messidor_retinal_images,
  title  = { Red lesion localization for MESSIDOR retinal images dataset using patch-based convolutional neural networks. },
  note   = { Red lesion localization for MESSIDOR retinal images dataset using patch-based convolutional neural networks.. Mendeley Data, V1. doi:10.17632/3r5m3nfdkv.1 },
  url    = { https://data.mendeley.com/datasets/3r5m3nfdkv/1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Red lesion localization for MESSIDOR retinal images dataset using patch-based convolutional neural networks.. Mendeley Data, V1. doi:10.17632/3r5m3nfdkv.1.
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

- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [fairvlmed](./fairvlmed.md): FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset (10,000 images, `cc-by-nc-nd`)
- [olives](./olives.md): OLIVES: Ophthalmic Labels for Investigating Visual Eye Semantics (9,408 b scans, `cc-by`)
- [fprm_retina](./fprm_retina.md): FPRM Multimodal Eye Imaging and Psychological Assessment Dataset (3,361 images, `research-only`)
- [grape](./grape.md): GRAPE: Glaucoma Real-world Appraisal Progression Ensemble (1,115 examinations, `cc0`)
- [papila](./papila.md): PAPILA: Glaucoma Fundus Dataset with Clinical Data (488 images, `cc-by`)
- [mendeley_retina_identification_database_ridb](./mendeley_retina_identification_database_ridb.md): Retina Identification Database (RIDB) (100 images, `cc-by`)
- [dryad_diabetes_retinal_capillary](./dryad_diabetes_retinal_capillary.md): Diabetes Retinal Capillary Rarefaction Dataset (73 participants, `cc0`)
