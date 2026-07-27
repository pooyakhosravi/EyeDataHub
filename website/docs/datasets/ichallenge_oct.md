---
id: ichallenge_oct
title: "iChallenge OCT Datasets (HDMILab / OMIA Workshops)"
sidebar_label: ichallenge_oct
description: "OCT challenge datasets from HDMILab covering retinal layer segmentation and fluid detection tasks from MICCAI/OMIA workshops. Includes sub-challenges such as AMD/CSC/DR classification and retinal laye"
tags: ["oct", "research-only", "manual", "segmentation", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# iChallenge OCT Datasets (HDMILab / OMIA Workshops)

OCT challenge datasets from HDMILab covering retinal layer segmentation and fluid detection tasks from MICCAI/OMIA workshops. Includes sub-challenges such as AMD/CSC/DR classification and retinal layer segmentation; GAMMA challenge provides OCT volumes from 300 glaucoma patients (fundus + 3D OCT).

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `ichallenge_oct` |
| **Full name** | iChallenge OCT Datasets (HDMILab / OMIA Workshops) |
| **Primary category** | `oct` |
| **Contained modalities** | oct |
| **Tasks** | segmentation, classification |
| **Samples** | 300 |
| **Classes** | Not reported (Not reported) |
| **Splits** | train, test |
| **Size** | 2.0 GB |
| **Source-stated terms** | Non-commercial research (challenge-specific) |
| **Normalized terms** | `research-only` |
| **Descriptive screening label** | Research or challenge restriction recorded; check source |
| **Terms scope** | `challenge_participation` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `guided_instructions_only` |
| **Legacy sample-loader status** | Standard loader included |


## Notes

> num_samples refers to patient volumes (GAMMA has 300 patients, each with 3D OCT + fundus). Slice counts depend on sub-challenge. Visit http://hdmilab.cn/ichallenge, register/log in, and download the relevant challenge dataset(s). Place extracted files under ~/.eyedatahub/data/ichallenge_oct/.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download ichallenge_oct --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download ichallenge_oct --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('ichallenge_oct')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [hdmilab.cn/ichallenge](http://hdmilab.cn/ichallenge)

**Source-term evidence:** [hdmilab.cn/ichallenge](http://hdmilab.cn/ichallenge)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('ichallenge_oct')
samples = ds.load(data_dir, split='test')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{ichallenge_oct,
  title  = { iChallenge OCT Datasets (HDMILab / OMIA Workshops) },
  note   = { HDMILab iChallenge. http://hdmilab.cn/ichallenge },
  url    = { http://hdmilab.cn/ichallenge },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
HDMILab iChallenge. http://hdmilab.cn/ichallenge
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Non-commercial research (challenge-specific)
- **Normalized category:** `research-only`
- **Apparent scope:** `challenge_participation`
- **Descriptive screening label:** Research or challenge restriction recorded; check source

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
