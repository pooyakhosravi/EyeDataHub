---
id: retinal_oct_octa_two_subjects_processed
title: "Processed Retinal OCT and OCTA Two-Subject Dataset"
sidebar_label: retinal_oct_octa_two_subjects_processed
description: "Processed human OCT/OCTA data including segmentations and ETDRS-grid materials."
tags: ["octa", "cc-by", "kaggle", "segmentation", "measurement", "resource-role-current-dataset", "dataset-family-retinal-oct-octa-two-subjects-processed"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Processed Retinal OCT and OCTA Two-Subject Dataset

Processed human OCT/OCTA data including segmentations and ETDRS-grid materials.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `retinal_oct_octa_two_subjects_processed` |
| **Full name** | Processed Retinal OCT and OCTA Two-Subject Dataset |
| **First published** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Primary category** | `octa` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `retinal_oct_octa_two_subjects_processed` |
| **Contained modalities** | octa |
| **Tasks** | segmentation, measurement |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Kaggle |
| **Availability** | `available` (checked 2026-08-02) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

No reproducible primary item count was exposed for the cataloged source version.

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Source describes processed 3 × 3 mm OCTA/OCT data for two subjects; no catalog quantity is asserted because the source unit is not controlled.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download retinal_oct_octa_two_subjects_processed --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download retinal_oct_octa_two_subjects_processed --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('retinal_oct_octa_two_subjects_processed')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [kaggle.com/datasets](https://www.kaggle.com/datasets/cnzakimuena/retinal-oct-and-octa-data-3)

**Source-term evidence:** [kaggle.com/datasets](https://www.kaggle.com/datasets/cnzakimuena/retinal-oct-and-octa-data-3)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{retinal_oct_octa_two_subjects_processed,
  title  = { Processed Retinal OCT and OCTA Two-Subject Dataset },
  note   = { Repository dataset record. cnzakimuena/retinal-oct-and-octa-data-3 },
  url    = { https://www.kaggle.com/datasets/cnzakimuena/retinal-oct-and-octa-data-3 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Repository dataset record. cnzakimuena/retinal-oct-and-octa-data-3.
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

- [octa_macula_coronal](./octa_macula_coronal.md): OCTA Macula Coronal Views (82,560 images, `cc-by`)
- [octa_500](./octa_500.md): OCTA-500: Large-scale OCTA Multi-task Benchmark (500 participants, `research-only`)
- [aroma_octa](./aroma_octa.md): AROMA Retinal OCTA Artifact Dataset (281 images, `cc-by`)
- [rose](./rose.md): ROSE: Retinal OCT-Angiography Vessel Segmentation (229 images, `cc-by`)
- [soul_octa](./soul_octa.md): SOUL: OCTA Human-Machine Collaborative Annotation Dataset (178 longitudinal samples, `cc-by`)
- [drac22](./drac22.md): DRAC 2022: Diabetic Retinopathy Analysis Challenge (174 images, `cc-by`)
- [ut_fsocta](./ut_fsocta.md): UTHealth Fundus and Synthetic OCTA Dataset (112 participants, `unknown`)
- [dryad_preeclampsia_ocular_octa](./dryad_preeclampsia_ocular_octa.md): Plane wave ultrasound and OCT angiography of the eye in preeclampsia (Not reported, `cc0`)
