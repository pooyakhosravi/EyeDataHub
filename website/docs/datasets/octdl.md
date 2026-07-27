---
id: octdl
title: "OCTDL: OCT Deep Learning Dataset"
sidebar_label: octdl
description: "2,000+ OCT images labeled for 7 conditions: AMD, DME, ERM, NO (normal), RAO, RVO, VID."
tags: ["oct", "cc-by", "mendeley", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# OCTDL: OCT Deep Learning Dataset

2,000+ OCT images labeled for 7 conditions: AMD, DME, ERM, NO (normal), RAO, RVO, VID.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `octdl` |
| **Full name** | OCTDL: OCT Deep Learning Dataset |
| **Primary category** | `oct` |
| **Contained modalities** | oct |
| **Tasks** | classification |
| **Samples** | 2,000 |
| **Classes** | 7 (AMD, DME, ERM, NO, RAO, RVO, VID) |
| **Splits** | all |
| **Size** | 0.8 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Mendeley Data |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Standard loader included |


## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download octdl --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download octdl --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('octdl')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/sncdhf53xc/4)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/sncdhf53xc/4)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('octdl')
samples = ds.load(data_dir, split='all')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{octdl,
  title  = { OCTDL: OCT Deep Learning Dataset },
  note   = { Kulyabin et al., 'OCTDL: Optical Coherence Tomography Dataset for Image-Based Deep Learning Methods', Scientific Data 2024 },
  year   = { 2024 },
  url    = { https://data.mendeley.com/datasets/sncdhf53xc/4 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Kulyabin et al., 'OCTDL: Optical Coherence Tomography Dataset for Image-Based Deep Learning Methods', Scientific Data 2024.
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
- [kermany_oct](./kermany_oct.md): Kermany OCT 2018: Retinal OCT Image Classification (84,484 records, `cc-by`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (58,036 records, `mit`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 records, `unknown`)
- [harvard_fairvision](./harvard_fairvision.md): Harvard-FairVision (AMD + DR + Glaucoma, paired SLO + OCT) (30,000 records, `cc-by-nc-nd`)
- [mario](./mario.md): MARIO: AMD-Progression Longitudinal OCT (MICCAI 2024) (30,000 records, `cc-by`)
- [mmrdr](./mmrdr.md): MMRDR: Multi-Modal Retinal Diabetic Retinopathy Dataset (24,460 records, `cc-by`)
