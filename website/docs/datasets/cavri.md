---
id: cavri
title: "CAVRI: Computer Analysis of VitreoRetinal Interface Dataset"
sidebar_label: cavri
description: "50 annotated 3D SD-OCT volumes (7,050 B-scans, 640×385 px) from subjects with vitreomacular adhesion (VMA, 25 eyes) and vitreomacular traction (VMT, 25 eyes). Each volume: 141 B-scans over 2×7×7 mm. A"
tags: ["oct", "research-only", "manual", "segmentation"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# CAVRI: Computer Analysis of VitreoRetinal Interface Dataset

50 annotated 3D SD-OCT volumes (7,050 B-scans, 640×385 px) from subjects with vitreomacular adhesion (VMA, 25 eyes) and vitreomacular traction (VMT, 25 eyes). Each volume: 141 B-scans over 2×7×7 mm. Annotated boundaries: PCV, ILM, RPE. Device: Optovue Avanti RTvue.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `cavri` |
| **Full name** | CAVRI: Computer Analysis of VitreoRetinal Interface Dataset |
| **Primary category** | `oct` |
| **Contained modalities** | oct |
| **Tasks** | segmentation |
| **Primary reported quantity** | 50 volumes |
| **Classes** | 3 (PCV, ILM, RPE) |
| **Splits** | train, val, test |
| **Size** | 3.0 GB |
| **Source-stated terms** | Research/educational use only (no commercial redistribution) |
| **Normalized terms** | `research-only` |
| **Descriptive screening label** | Research or challenge restriction recorded; check source |
| **Terms scope** | `unknown` |
| **Access friction** | `author_contact` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `manual_access_blocked` |
| **Legacy sample-loader status** | Standard loader included |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 50 | `volumes` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [dsp.put.poznan.pl/cavri_database-191](https://dsp.put.poznan.pl/cavri_database-191/) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Access by email request: agnieszka.stankiewicz@put.poznan.pl or tomasz.marciniak@put.poznan.pl. Dataset page: https://dsp.put.poznan.pl/cavri_database-191/ GitHub (segmentation code): https://github.com/krzyk87/pcv_segmentation

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# This route requires upstream human action; no transfer starts.
eyehub download cavri --data-dir ./data --dry-run --json
# Follow the official instructions shown by preflight.
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('cavri')
print(preflight_dataset(ds, './data'))  # returns manual_access_blocked
```

  </TabItem>
</Tabs>

**Upstream page:** [dsp.put.poznan.pl/cavri_database-191](https://dsp.put.poznan.pl/cavri_database-191/)

**Source-term evidence:** [dsp.put.poznan.pl/cavri_database-191](https://dsp.put.poznan.pl/cavri_database-191/)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('cavri')
samples = ds.load(data_dir, split='test')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{cavri,
  title  = { CAVRI: Computer Analysis of VitreoRetinal Interface Dataset },
  note   = { Stankiewicz A et al., 'Segmentation of Preretinal Space in Optical Coherence Tomography Images Using Deep Neural Networks', Sensors 21(22):7521 (2021). doi:10.3390/s21227521 },
  year   = { 2021 },
  url    = { https://dsp.put.poznan.pl/cavri_database-191/ },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Stankiewicz A et al., 'Segmentation of Preretinal Space in Optical Coherence Tomography Images Using Deep Neural Networks', Sensors 21(22):7521 (2021). doi:10.3390/s21227521
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Research/educational use only (no commercial redistribution)
- **Normalized category:** `research-only`
- **Apparent scope:** `unknown`
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
