---
id: kermany_oct
title: "Kermany OCT 2018: Retinal OCT Image Classification"
sidebar_label: kermany_oct
description: "~84,000 retinal OCT B-scan images across 4 classes: CNV, DME, DRUSEN, NORMAL. Train: ~83,484 / Test: 1000."
tags: ["oct", "cc-by", "kaggle", "classification", "resource-role-current-dataset", "dataset-family-kermany-oct", "documented-relationship", "relationship-derived_from"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Kermany OCT 2018: Retinal OCT Image Classification

~84,000 retinal OCT B-scan images across 4 classes: CNV, DME, DRUSEN, NORMAL. Train: ~83,484 / Test: 1000.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `kermany_oct` |
| **Full name** | Kermany OCT 2018: Retinal OCT Image Classification |
| **Publication date** | 2017-12-25 |
| **Date basis** | Initial dataset release |
| **Publication date precision** | day |
| **Publication date evidence** | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/rscbjbr9sj/1) |
| **Publication date source field** | Mendeley Data version 1 page: Published |
| **Publication date reviewed** | 2026-09-11 |
| **Date notes** | Original Mendeley Data release is used; Kaggle mirror version dates are not substituted. |
| **Primary category** | `oct` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `kermany_oct` |
| **Contained modalities** | oct |
| **Tasks** | classification |
| **Primary reported quantity** | 84,484 images |
| **Classes** | 4 (CNV, DME, DRUSEN, NORMAL) |
| **Splits** | train, test, val |
| **Size** | 6.0 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Kaggle |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Standard loader included |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 84,484 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [kaggle.com/datasets](https://www.kaggle.com/datasets/paultimothymooney/kermany2018) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- [intraretinal_cystoid_fluid](./intraretinal_cystoid_fluid.md) is `derived from` this record: The source states that 1,000 training images were selected from the Kermany Retinal OCT Images DME class; 200 test images were collected separately. ([evidence](https://www.kaggle.com/datasets/zeeshanahmed13/intraretinal-cystoid-fluid))
- [mm_retinal_reason](./mm_retinal_reason.md) is `derived from` this record: The version-pinned official dataset card lists this record among the CFP or OCT sources used to construct MM-Retinal-Reason. ([evidence](https://huggingface.co/datasets/lxirich/MM-Retinal-Reason/tree/d6243baa82c0914dba3c6f43ca79fdbf856982ef))
- [multieye](./multieye.md) is `derived from` this record: The MultiEYE paper names this record as one of the public fundus or OCT sources assembled for the benchmark. ([evidence](https://arxiv.org/abs/2412.09402))
- [synthetic_retinal_oct_biomarkers](./synthetic_retinal_oct_biomarkers.md) is `derived from` this record: The official dataset card documents the Kermany retinal OCT collection as the source for the four synthetic diagnostic classes. ([evidence](https://huggingface.co/datasets/serag-ai/Synthetic-Ophthalmology-Images))
- [x_pcr](./x_pcr.md) is `derived from` this record: Source labels in the version-pinned public X-PCR deposit identify this catalog record as upstream material. ([evidence](https://huggingface.co/datasets/Fantasy666/X-PCR/tree/06a318fd852230326386e3c6514d8a11b7a6b4af))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download kermany_oct --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download kermany_oct --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('kermany_oct')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [kaggle.com/datasets](https://www.kaggle.com/datasets/paultimothymooney/kermany2018)

**Source-term evidence:** [kaggle.com/datasets](https://www.kaggle.com/datasets/paultimothymooney/kermany2018)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('kermany_oct')
samples = ds.load(data_dir, split='test')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{kermany_oct,
  title  = { Kermany OCT 2018: Retinal OCT Image Classification },
  note   = { Kermany et al., 'Identifying medical diagnoses and treatable diseases by image-based deep learning', Cell 2018 },
  year   = { 2018 },
  url    = { https://www.kaggle.com/datasets/paultimothymooney/kermany2018 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Kermany et al., 'Identifying medical diagnoses and treatable diseases by image-based deep learning', Cell 2018.
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
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [harvard_fairvision](./harvard_fairvision.md): Harvard-FairVision (AMD + DR + Glaucoma, paired SLO + OCT) (30,000 participants, `cc-by-nc-nd`)
- [mario](./mario.md): MARIO: AMD-Progression Longitudinal OCT (MICCAI 2024) (30,000 images, `cc-by`)
- [mmrdr](./mmrdr.md): MMRDR: Multi-Modal Retinal Diabetic Retinopathy Dataset (24,460 images, `cc-by`)
- [oct_c8](./oct_c8.md): Retinal OCT-C8: 8-Class OCT Classification (24,000 images, `unknown`)
