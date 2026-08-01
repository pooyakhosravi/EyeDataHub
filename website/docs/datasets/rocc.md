---
id: rocc
title: "ROCC: Retinal OCT Classification Challenge"
sidebar_label: rocc
description: "Grand Challenge OCT classification dataset for diabetic-retinopathy related OCT classification."
tags: ["oct", "research-only", "manual", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# ROCC: Retinal OCT Classification Challenge

Grand Challenge OCT classification dataset for diabetic-retinopathy related OCT classification.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `rocc` |
| **Full name** | ROCC: Retinal OCT Classification Challenge |
| **Primary category** | `oct` |
| **Contained modalities** | oct |
| **Tasks** | classification |
| **Primary reported quantity** | 165 volumes |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | Research only (Grand Challenge terms) |
| **Normalized terms** | `research-only` |
| **Descriptive screening label** | Research or challenge restriction recorded; check source |
| **Terms scope** | `challenge_participation` |
| **Access friction** | `self_service_clickthrough` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `guided_instructions_only` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 165 | `volumes` | OCT volumes in the challenge cohort | `official_source_description` | [rocc.grand-challenge.org](https://rocc.grand-challenge.org/) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Grand Challenge account and challenge terms apply.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download rocc --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download rocc --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('rocc')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [rocc.grand-challenge.org](https://rocc.grand-challenge.org/)

**Source-term evidence:** [rocc.grand-challenge.org](https://rocc.grand-challenge.org/)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{rocc,
  title  = { ROCC: Retinal OCT Classification Challenge },
  note   = { Retinal OCT Classification Challenge (ROCC). Grand Challenge, 2017 },
  year   = { 2017 },
  url    = { https://rocc.grand-challenge.org/ },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Retinal OCT Classification Challenge (ROCC). Grand Challenge, 2017.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Research only (Grand Challenge terms)
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
