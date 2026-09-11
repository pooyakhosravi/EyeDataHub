---
id: mendeley_deep_learning_prediction_uncorrected_refractive_error
title: "Deep Learning for the Prediction of Uncorrected Refractive Error using OCT"
sidebar_label: mendeley_deep_learning_prediction_uncorrected_refractive_error
description: "Observation-level source data, annotations, or signals. from Source describes OCT-based refractive-error prediction, consistent with human clinical imaging; confirm population wording at addition."
tags: ["oct", "cc-by", "mendeley", "prediction", "resource-role-current-dataset", "dataset-family-mendeley-deep-learning-prediction-uncorrected-refractive-error"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Deep Learning for the Prediction of Uncorrected Refractive Error using OCT

Observation-level source data, annotations, or signals. from Source describes OCT-based refractive-error prediction, consistent with human clinical imaging; confirm population wording at addition.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mendeley_deep_learning_prediction_uncorrected_refractive_error` |
| **Full name** | Deep Learning for the Prediction of Uncorrected Refractive Error using OCT |
| **Publication date** | 2023-04-05 |
| **Date basis** | Initial dataset release |
| **Publication date precision** | day |
| **Publication date evidence** | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/89z7h5gnpw/1) |
| **Publication date source field** | citation_publication_date (version 1) |
| **Publication date reviewed** | 2026-09-11 |
| **Date notes** | - |
| **Primary category** | `oct` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `mendeley_deep_learning_prediction_uncorrected_refractive_error` |
| **Contained modalities** | oct |
| **Tasks** | prediction |
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

> Human provenance: Source describes OCT-based refractive-error prediction, consistent with human clinical imaging; confirm population wording at addition. Source-review finding: Nine files: five JPEG examples, three ZIP archives, and one DOCX.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mendeley_deep_learning_prediction_uncorrected_refractive_error --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download mendeley_deep_learning_prediction_uncorrected_refractive_error --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mendeley_deep_learning_prediction_uncorrected_refractive_error')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/89z7h5gnpw/2)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/89z7h5gnpw)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mendeley_deep_learning_prediction_uncorrected_refractive_error,
  title  = { Deep Learning for the Prediction of Uncorrected Refractive Error using OCT },
  note   = { Deep Learning for the Prediction of Uncorrected Refractive Error using OCT. Mendeley Data, V2. doi:10.17632/89z7h5gnpw.2 },
  url    = { https://data.mendeley.com/datasets/89z7h5gnpw/2 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Deep Learning for the Prediction of Uncorrected Refractive Error using OCT. Mendeley Data, V2. doi:10.17632/89z7h5gnpw.2.
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

- [syn_oct](./syn_oct.md): SYN-OCT Synthetic Glaucoma OCT Dataset (200,000 images, `cc-by`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (103,959 images, `mit`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [kermany_oct](./kermany_oct.md): Kermany OCT 2018: Retinal OCT Image Classification (84,484 images, `cc-by`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [harvard_fairvision](./harvard_fairvision.md): Harvard-FairVision (AMD + DR + Glaucoma, paired SLO + OCT) (30,000 participants, `cc-by-nc-nd`)
- [mario](./mario.md): MARIO: AMD-Progression Longitudinal OCT (MICCAI 2024) (30,000 images, `cc-by`)
- [mmrdr](./mmrdr.md): MMRDR: Multi-Modal Retinal Diabetic Retinopathy Dataset (24,460 images, `cc-by`)
