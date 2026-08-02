---
id: gleam
title: "GLEAM Multimodal Glaucoma Staging Dataset"
sidebar_label: gleam
description: "SLO, circumpapillary OCT, and visual-field pattern-deviation maps with four-class glaucoma labels."
tags: ["oct", "cc-by-nc-nd", "kaggle", "classification", "staging", "resource-role-current-dataset", "dataset-family-gleam"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# GLEAM Multimodal Glaucoma Staging Dataset

SLO, circumpapillary OCT, and visual-field pattern-deviation maps with four-class glaucoma labels.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `gleam` |
| **Full name** | GLEAM Multimodal Glaucoma Staging Dataset |
| **Primary category** | `oct` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `gleam` |
| **Contained modalities** | oct |
| **Tasks** | classification, staging |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | CC BY-NC-ND 4.0 |
| **Normalized terms** | `cc-by-nc-nd` |
| **Descriptive screening label** | Explicit noncommercial clause recorded; check source |
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

> Source reports 1,200 tri-modal samples from 841 patients; no catalog quantity is asserted because the source unit is not controlled.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download gleam --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download gleam --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('gleam')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [kaggle.com/datasets](https://www.kaggle.com/datasets/zhangyiyinge/gleam-dataset)

**Source-term evidence:** [kaggle.com/datasets](https://www.kaggle.com/datasets/zhangyiyinge/gleam-dataset)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{gleam,
  title  = { GLEAM Multimodal Glaucoma Staging Dataset },
  note   = { Repository dataset record. zhangyiyinge/gleam-dataset },
  url    = { https://www.kaggle.com/datasets/zhangyiyinge/gleam-dataset },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Repository dataset record. zhangyiyinge/gleam-dataset.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC BY-NC-ND 4.0
- **Normalized category:** `cc-by-nc-nd`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Explicit noncommercial clause recorded; check source

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
