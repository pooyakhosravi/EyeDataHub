---
id: nehut
title: "NEH-UT Retinal OCT Dataset"
sidebar_label: nehut
description: "Retinal OCT B-scans from Noor Eye Hospital for classification of Normal, Drusen, and CNV (choroidal neovascularisation) cases. 16,822 B-scans from 441 eyes (Normal 120 / Drusen 160 / CNV 161 eyes)."
tags: ["oct", "cc-by", "mendeley", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# NEH-UT Retinal OCT Dataset

Retinal OCT B-scans from Noor Eye Hospital for classification of Normal, Drusen, and CNV (choroidal neovascularisation) cases. 16,822 B-scans from 441 eyes (Normal 120 / Drusen 160 / CNV 161 eyes).

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `nehut` |
| **Full name** | NEH-UT Retinal OCT Dataset |
| **Primary category** | `oct` |
| **Contained modalities** | oct |
| **Tasks** | classification |
| **Primary reported quantity** | 16,822 images |
| **Classes** | 3 (Normal, Drusen, CNV) |
| **Splits** | all |
| **Size** | 3.65 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Mendeley Data |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Standard loader included |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 16,822 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/8kt969dhx6/2) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download nehut --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download nehut --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('nehut')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/8kt969dhx6/2)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/8kt969dhx6/2)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('nehut')
samples = ds.load(data_dir, split='all')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{nehut,
  title  = { NEH-UT Retinal OCT Dataset },
  note   = { Labeled Retinal OCT Dataset for Classification of Normal, Drusen, and CNV Cases. Mendeley Data, V2. doi:10.17632/8kt969dhx6.2 },
  url    = { https://data.mendeley.com/datasets/8kt969dhx6/2 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Labeled Retinal OCT Dataset for Classification of Normal, Drusen, and CNV Cases. Mendeley Data, V2. doi:10.17632/8kt969dhx6.2
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
