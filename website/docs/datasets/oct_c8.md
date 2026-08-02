---
id: oct_c8
title: "Retinal OCT-C8: 8-Class OCT Classification"
sidebar_label: oct_c8
description: "~24,000 retinal OCT images across 8 disease classes: AMD, BRAO, BRVO, CSC, CRAO, CRVO, DME, MH."
tags: ["oct", "unknown", "kaggle", "classification", "resource-role-current-dataset", "dataset-family-oct-c8", "documented-relationship", "relationship-derived_from"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Retinal OCT-C8: 8-Class OCT Classification

~24,000 retinal OCT images across 8 disease classes: AMD, BRAO, BRVO, CSC, CRAO, CRVO, DME, MH.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `oct_c8` |
| **Full name** | Retinal OCT-C8: 8-Class OCT Classification |
| **Primary category** | `oct` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `oct_c8` |
| **Contained modalities** | oct |
| **Tasks** | classification |
| **Primary reported quantity** | 24,000 images |
| **Classes** | 8 (AMD, Branch Retinal Artery Occlusion, Branch Retinal Vein Occlusion, Central Serous Chorioretinopathy, Central Retinal Artery Occlusion, Central Retinal Vein Occlusion, Diabetic Macular Edema, Macular Hole) |
| **Splits** | train, val, test |
| **Size** | 2.5 GB |
| **Source-stated terms** | See Kaggle dataset page |
| **Normalized terms** | `unknown` |
| **Descriptive screening label** | Unknown or unclear; do not assume permission |
| **Terms scope** | `unknown` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Kaggle |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Standard loader included |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 24,000 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [kaggle.com/datasets](https://www.kaggle.com/datasets/obulisainaren/retinal-oct-c8) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- [mm_retinal_reason](./mm_retinal_reason.md) is `derived from` this record: The version-pinned official dataset card lists this record among the CFP or OCT sources used to construct MM-Retinal-Reason. ([evidence](https://huggingface.co/datasets/lxirich/MM-Retinal-Reason/tree/d6243baa82c0914dba3c6f43ca79fdbf856982ef))
- [x_pcr](./x_pcr.md) is `derived from` this record: Source labels in the version-pinned public X-PCR deposit identify this catalog record as upstream material. ([evidence](https://huggingface.co/datasets/Fantasy666/X-PCR/tree/06a318fd852230326386e3c6514d8a11b7a6b4af))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download oct_c8 --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download oct_c8 --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('oct_c8')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [kaggle.com/datasets](https://www.kaggle.com/datasets/obulisainaren/retinal-oct-c8)

**Source-term evidence:** [kaggle.com/datasets](https://www.kaggle.com/datasets/obulisainaren/retinal-oct-c8)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('oct_c8')
samples = ds.load(data_dir, split='test')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{oct_c8,
  title  = { Retinal OCT-C8: 8-Class OCT Classification },
  note   = { Srinivasan et al., 'Fully automated detection of diabetic macular edema and dry age-related macular degeneration from optical coherence tomography images', Biomed. Opt. Express 2014 },
  year   = { 2014 },
  url    = { https://www.kaggle.com/datasets/obulisainaren/retinal-oct-c8 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Srinivasan et al., 'Fully automated detection of diabetic macular edema and dry age-related macular degeneration from optical coherence tomography images', Biomed. Opt. Express 2014.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** See Kaggle dataset page
- **Normalized category:** `unknown`
- **Apparent scope:** `unknown`
- **Descriptive screening label:** Unknown or unclear; do not assume permission

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
