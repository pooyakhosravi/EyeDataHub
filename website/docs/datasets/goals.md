---
id: goals
title: "GOALS — Glaucoma OCT Layer Segmentation (MICCAI 2022)"
sidebar_label: goals
description: "300 circumpapillary OCT images. RNFL/GCIPL/choroid layer segmentation plus binary glaucoma classification."
tags: ["oct", "cc-by", "gdrive", "segmentation", "classification", "documented-relationship", "relationship-derived_from"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# GOALS — Glaucoma OCT Layer Segmentation (MICCAI 2022)

300 circumpapillary OCT images. RNFL/GCIPL/choroid layer segmentation plus binary glaucoma classification.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `goals` |
| **Full name** | GOALS — Glaucoma OCT Layer Segmentation (MICCAI 2022) |
| **Primary category** | `oct` |
| **Contained modalities** | oct |
| **Tasks** | segmentation, classification |
| **Primary reported quantity** | 300 images |
| **Classes** | 3 (RNFL, GCIPL, Choroid) |
| **Splits** | train, test |
| **Size** | 0.5 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Google Drive |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `loader_implemented_not_live_tested` |
| **Legacy sample-loader status** | Standard loader included |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 300 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [aistudio.baidu.com/competition](https://aistudio.baidu.com/competition/detail/783/0/introduction) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Primary challenge page: https://aistudio.baidu.com/competition/detail/783/0/introduction. Automated downloader still tries the known Google Drive mirror (https://drive.google.com/file/d/1P1cLm9_Pwq4fum4lB1-LGUayO-NMvF5I/view) and then Zenodo record 6362363.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- [mm_retinal_reason](./mm_retinal_reason.md) is `derived from` this record: The version-pinned official dataset card lists this record among the CFP or OCT sources used to construct MM-Retinal-Reason. ([evidence](https://huggingface.co/datasets/lxirich/MM-Retinal-Reason/tree/d6243baa82c0914dba3c6f43ca79fdbf856982ef))
- [multieye](./multieye.md) is `derived from` this record: The MultiEYE paper names this record as one of the public fundus or OCT sources assembled for the benchmark. ([evidence](https://arxiv.org/abs/2412.09402))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download goals --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download goals --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('goals')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [aistudio.baidu.com/competition](https://aistudio.baidu.com/competition/detail/783/0/introduction)

**Source-term evidence:** [aistudio.baidu.com/competition](https://aistudio.baidu.com/competition/detail/783/0/introduction)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('goals')
samples = ds.load(data_dir, split='test')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{goals,
  title  = { GOALS — Glaucoma OCT Layer Segmentation (MICCAI 2022) },
  note   = { Fang H. et al., 'GOALS Challenge: A Large-Scale OCT Image Dataset for Glaucoma Analysis', MICCAI 2022 Workshop },
  year   = { 2022 },
  url    = { https://aistudio.baidu.com/competition/detail/783/0/introduction },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Fang H. et al., 'GOALS Challenge: A Large-Scale OCT Image Dataset for Glaucoma Analysis', MICCAI 2022 Workshop.
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
