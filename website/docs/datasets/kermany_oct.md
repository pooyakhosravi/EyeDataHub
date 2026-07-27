---
id: kermany_oct
title: "Kermany OCT 2018: Retinal OCT Image Classification"
sidebar_label: kermany_oct
description: "~84,000 retinal OCT B-scan images across 4 classes: CNV, DME, DRUSEN, NORMAL. Train: ~83,484 / Test: 1000."
tags: ["oct", "cc-by", "kaggle", "classification"]
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
| **Primary category** | `oct` |
| **Contained modalities** | oct |
| **Tasks** | classification |
| **Samples** | 84,484 |
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


## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download kermany_oct --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download kermany_oct --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('kermany_oct')
print(preflight_dataset(ds, './data'))  # no transfer
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

## Related datasets with shared modalities

- [syn_oct](./syn_oct.md): SYN-OCT Synthetic Glaucoma OCT Dataset (200,000 records, `cc-by`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 records, `unknown`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (58,036 records, `mit`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 records, `unknown`)
- [harvard_fairvision](./harvard_fairvision.md): Harvard-FairVision (AMD + DR + Glaucoma, paired SLO + OCT) (30,000 records, `cc-by-nc-nd`)
- [mario](./mario.md): MARIO: AMD-Progression Longitudinal OCT (MICCAI 2024) (30,000 records, `cc-by`)
- [mmrdr](./mmrdr.md): MMRDR: Multi-Modal Retinal Diabetic Retinopathy Dataset (24,460 records, `cc-by`)
- [oct_c8](./oct_c8.md): Retinal OCT-C8: 8-Class OCT Classification (24,000 records, `unknown`)
