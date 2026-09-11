---
id: retouch
title: "RETOUCH: RETinal OCT Fluid Challenge"
sidebar_label: retouch
description: "112 OCT volumes from three vendors (Cirrus / Spectralis / Topcon) with pixel-level segmentation of intraretinal fluid (IRF), subretinal fluid (SRF), and pigment epithelium detachment (PED)."
tags: ["oct", "research-only", "manual", "segmentation", "resource-role-current-dataset", "dataset-family-retouch"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# RETOUCH: RETinal OCT Fluid Challenge

112 OCT volumes from three vendors (Cirrus / Spectralis / Topcon) with pixel-level segmentation of intraretinal fluid (IRF), subretinal fluid (SRF), and pigment epithelium detachment (PED).

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `retouch` |
| **Full name** | RETOUCH: RETinal OCT Fluid Challenge |
| **Publication date** | 2017-04-10 |
| **Date basis** | Initial dataset release |
| **Publication date precision** | day |
| **Publication date evidence** | [retouch.grand-challenge.org](https://retouch.grand-challenge.org/) |
| **Publication date source field** | Official RETOUCH Important Dates: First part of the Training set was released (Cirrus and Spectralis) |
| **Publication date reviewed** | 2026-09-11 |
| **Date notes** | The official RETOUCH challenge page states that the first training set was released April 10, 2017; this is the initial public training-data release, before the later Topcon training part. |
| **Primary category** | `oct` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `retouch` |
| **Contained modalities** | oct |
| **Tasks** | segmentation |
| **Primary reported quantity** | 112 volumes |
| **Classes** | 4 (background, irf, srf, ped) |
| **Splits** | train, test |
| **Size** | 5.0 GB |
| **Source-stated terms** | Research only (signed DUA via Grand Challenge) |
| **Normalized terms** | `research-only` |
| **Descriptive screening label** | Research or challenge restriction recorded; check source |
| **Terms scope** | `challenge_participation` |
| **Access friction** | `controlled_or_manual` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `manual_access_blocked` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 112 | `volumes` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [retouch.grand-challenge.org](https://retouch.grand-challenge.org/) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Grand Challenge account + signed DUA required.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# This route requires upstream human action; no transfer starts.
eyehub download retouch --data-dir ./data --dry-run --json
# Follow the official instructions shown by preflight.
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('retouch')
print(preflight_dataset(ds, './data'))  # returns manual_access_blocked
```

  </TabItem>
</Tabs>

**Upstream page:** [retouch.grand-challenge.org](https://retouch.grand-challenge.org/)

**Source-term evidence:** [retouch.grand-challenge.org](https://retouch.grand-challenge.org/)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{retouch,
  title  = { RETOUCH: RETinal OCT Fluid Challenge },
  note   = { Bogunovic et al., 'RETOUCH — The Retinal OCT Fluid Detection and Segmentation Benchmark and Challenge', IEEE TMI 2019 },
  year   = { 2019 },
  url    = { https://retouch.grand-challenge.org/ },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Bogunovic et al., 'RETOUCH — The Retinal OCT Fluid Detection and Segmentation Benchmark and Challenge', IEEE TMI 2019.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Research only (signed DUA via Grand Challenge)
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
