---
id: oct_c8
title: "Retinal OCT-C8: 8-Class OCT Classification"
sidebar_label: oct_c8
description: "~24,000 retinal OCT images across 8 disease classes: AMD, BRAO, BRVO, CSC, CRAO, CRVO, DME, MH."
tags: ["oct", "unknown", "kaggle", "classification"]
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
| **Contained modalities** | oct |
| **Tasks** | classification |
| **Samples** | 24,000 |
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


## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download oct_c8 --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download oct_c8 --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('oct_c8')
print(preflight_dataset(ds, './data'))  # no transfer
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

## Related datasets with shared modalities

- [syn_oct](./syn_oct.md): SYN-OCT Synthetic Glaucoma OCT Dataset (200,000 records, `cc-by`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 records, `unknown`)
- [kermany_oct](./kermany_oct.md): Kermany OCT 2018: Retinal OCT Image Classification (84,484 records, `cc-by`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (58,036 records, `mit`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 records, `unknown`)
- [harvard_fairvision](./harvard_fairvision.md): Harvard-FairVision (AMD + DR + Glaucoma, paired SLO + OCT) (30,000 records, `cc-by-nc-nd`)
- [mario](./mario.md): MARIO: AMD-Progression Longitudinal OCT (MICCAI 2024) (30,000 records, `cc-by`)
- [mmrdr](./mmrdr.md): MMRDR: Multi-Modal Retinal Diabetic Retinopathy Dataset (24,460 records, `cc-by`)
