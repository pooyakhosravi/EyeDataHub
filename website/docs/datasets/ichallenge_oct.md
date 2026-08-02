---
id: ichallenge_oct
title: "iChallenge OCT Datasets (HDMILab / OMIA Workshops)"
sidebar_label: ichallenge_oct
description: "OCT challenge datasets from HDMILab covering retinal layer segmentation and fluid detection tasks from MICCAI/OMIA workshops. Includes sub-challenges such as AMD/CSC/DR classification and retinal laye"
tags: ["oct", "research-only", "manual", "segmentation", "classification", "documented-relationship", "relationship-component_of", "relationship-has_component"]
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
| **Primary reported quantity** | 300 volumes |
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


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 300 | `volumes` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [hdmilab.cn/ichallenge](http://hdmilab.cn/ichallenge) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> num_samples refers to patient volumes (GAMMA has 300 patients, each with 3D OCT + fundus). Slice counts depend on sub-challenge. Visit http://hdmilab.cn/ichallenge, register/log in, and download the relevant challenge dataset(s). Place extracted files under ~/.eyedatahub/data/ichallenge_oct/.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- [gamma](./gamma.md) is `component of` this record: GAMMA is one of the named resources exposed through the cataloged iChallenge OCT portal record. ([evidence](http://hdmilab.cn/ichallenge))
- This record is `has component` [gamma](./gamma.md): The cataloged iChallenge OCT portal record explicitly includes the GAMMA multimodal challenge resource. ([evidence](http://hdmilab.cn/ichallenge))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download ichallenge_oct --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download ichallenge_oct --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('ichallenge_oct')
print(preflight_dataset(ds, './data'))  # no download
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

## Similar resources by shared modality

- [syn_oct](./syn_oct.md): SYN-OCT Synthetic Glaucoma OCT Dataset (200,000 images, `cc-by`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (103,959 images, `mit`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [kermany_oct](./kermany_oct.md): Kermany OCT 2018: Retinal OCT Image Classification (84,484 images, `cc-by`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [harvard_fairvision](./harvard_fairvision.md): Harvard-FairVision (AMD + DR + Glaucoma, paired SLO + OCT) (30,000 participants, `cc-by-nc-nd`)
- [mario](./mario.md): MARIO: AMD-Progression Longitudinal OCT (MICCAI 2024) (30,000 images, `cc-by`)
- [mmrdr](./mmrdr.md): MMRDR: Multi-Modal Retinal Diabetic Retinopathy Dataset (24,460 images, `cc-by`)
