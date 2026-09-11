---
id: itec_iris_pupil
title: "ITEC Iris and Pupil Segmentation Dataset"
sidebar_label: itec_iris_pupil
description: "Human cataract-surgery video frames with iris and pupil pixel masks."
tags: ["surgical_video", "unknown", "manual", "segmentation", "resource-role-annotation-layer", "dataset-family-itec-iris-pupil", "documented-relationship", "relationship-derived_from", "alternate-source", "source-kaggle", "alternate-role-mirror"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# ITEC Iris and Pupil Segmentation Dataset

Human cataract-surgery video frames with iris and pupil pixel masks.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `itec_iris_pupil` |
| **Full name** | ITEC Iris and Pupil Segmentation Dataset |
| **Publication date** | Unknown |
| **Date basis** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Date notes** | - |
| **Primary category** | `surgical_video` |
| **Resource role** | `annotation_layer` |
| **Dataset family** | `itec_iris_pupil` |
| **Contained modalities** | surgical_video |
| **Tasks** | segmentation |
| **Primary reported quantity** | 82 frames |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | Scientific-research-only; noncommercial use |
| **Normalized terms** | `unknown` |
| **Descriptive screening label** | Unknown or unclear; do not assume permission |
| **Terms scope** | `dataset_files` |
| **Access friction** | `controlled_or_manual` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-08-02) |
| **Acquisition support** | `manual_access_blocked` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 82 | `frames` | Official ITEC source reports 82 annotated frames from 35 cataract-surgery videos. Source-stated quantity; repository file count is separate. | `official_source_description` | [ftp.itec.aau.at/datasets](https://ftp.itec.aau.at/datasets/ovid/iris_pupil_seg/index.html) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> The official ITEC agreement route is canonical. Kaggle is an alternate mirror, not the controlling source.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- This record is `derived from` [cataract_101](./cataract_101.md): The official ITEC page states that the annotated iris and pupil frames were selected from Cataract-101 surgery videos. ([evidence](https://ftp.itec.aau.at/datasets/ovid/iris_pupil_seg/index.html))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# This route requires upstream human action; no transfer starts.
eyehub download itec_iris_pupil --data-dir ./data --dry-run --json
# Follow the official instructions shown by preflight.
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('itec_iris_pupil')
print(preflight_dataset(ds, './data'))  # returns manual_access_blocked
```

  </TabItem>
</Tabs>

**Upstream page:** [ftp.itec.aau.at/datasets](https://ftp.itec.aau.at/datasets/ovid/iris_pupil_seg/index.html)

## Other documented locations

These links identify alternate deposits, components, metadata records, mirrors, versions, or related derived materials. They do not create additional canonical catalog records.

- [kaggle: mirror (arwabasal/itec-iris-and-pupil-segmentation)](https://www.kaggle.com/datasets/arwabasal/itec-iris-and-pupil-segmentation): Non-authoritative alternate route.

**Source-term evidence:** [ftp.itec.aau.at/datasets](https://ftp.itec.aau.at/datasets/ovid/iris_pupil_seg/index.html)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{itec_iris_pupil,
  title  = { ITEC Iris and Pupil Segmentation Dataset },
  note   = { Repository dataset record. arwabasal/itec-iris-and-pupil-segmentation },
  url    = { https://ftp.itec.aau.at/datasets/ovid/iris_pupil_seg/index.html },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Repository dataset record. arwabasal/itec-iris-and-pupil-segmentation.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Scientific-research-only; noncommercial use
- **Normalized category:** `unknown`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Unknown or unclear; do not assume permission

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [ophora](./ophora.md): Ophora-160K: Ophthalmic Surgical Video Instruction Dataset (162,185 video clip instruction pairs, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [insegcat](./insegcat.md): InSegCat: Instance Segmentation for Cataract Surgery (5,581 annotated images, `research-only`)
- [cadis](./cadis.md): CaDIS: Cataract Dataset for Image Segmentation (4,670 images, `research-only`)
- [cataract_lmm](./cataract_lmm.md): Cataract-LMM: Large-Scale Multi-Source Multi-Task Cataract Surgery Benchmark (3,000 videos, `cc-by-nc-nd`)
- [ophnet2024](./ophnet2024.md): OphNet2024: Ophthalmic Surgical Video Dataset (2,278 videos, `cc-by-nc-sa`)
- [lmod_cataract_1k](./lmod_cataract_1k.md): LMOD-Cataract-1K (2,256 images, `cc-by`)
- [lmod_cataract_1k_cot](./lmod_cataract_1k_cot.md): Cataract-1K Surgical Analysis Chain-of-Thought Dataset (2,256 images, `mit`)
