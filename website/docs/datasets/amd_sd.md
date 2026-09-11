---
id: amd_sd
title: "AMD-SD: OCT Wet AMD Lesion Segmentation Dataset"
sidebar_label: amd_sd
description: "3,049 OCT B-scan images (1,140×380 px) from 138 wet AMD patients (156 eyes) with pixel-level annotations for 5 lesion classes: Subretinal Fluid (SRF), Intraretinal Fluid (IRF), Ellipsoid Zone Continui"
tags: ["oct", "cc-by-nc-nd", "kaggle", "segmentation", "resource-role-current-dataset", "dataset-family-amd-sd"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# AMD-SD: OCT Wet AMD Lesion Segmentation Dataset

3,049 OCT B-scan images (1,140×380 px) from 138 wet AMD patients (156 eyes) with pixel-level annotations for 5 lesion classes: Subretinal Fluid (SRF), Intraretinal Fluid (IRF), Ellipsoid Zone Continuity (EZC), Subretinal Hyperreflective Material (SHRM), and Pigment Epithelial Detachment (PED).

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `amd_sd` |
| **Full name** | AMD-SD: OCT Wet AMD Lesion Segmentation Dataset |
| **First published** | 2024-09-17 |
| **Publication date precision** | day |
| **Publication date evidence** | [api.figshare.com/v2](https://api.figshare.com/v2/collections/7157554/articles) |
| **Publication date source field** | articles[0].published_date / timeline.firstOnline |
| **Publication date reviewed** | 2026-09-11 |
| **Primary category** | `oct` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `amd_sd` |
| **Contained modalities** | oct |
| **Tasks** | segmentation |
| **Primary reported quantity** | 3,049 images |
| **Classes** | 5 (SRF, IRF, EZC, SHRM, PED) |
| **Splits** | train, val |
| **Size** | 2.0 GB |
| **Source-stated terms** | CC BY-NC-ND 4.0 |
| **Normalized terms** | `cc-by-nc-nd` |
| **Descriptive screening label** | Explicit noncommercial clause recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Kaggle |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Standard loader included |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 3,049 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [kaggle.com/datasets](https://www.kaggle.com/datasets/gaoweihao/amd-sd) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Official split: training.txt / validation.txt at dataset root. Images in AMD-SD/images/&lt;patient_id&gt;/&lt;scan&gt;.png. Primary source: Figshare collection 7157554; mirror on Kaggle: gaoweihao/amd-sd.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download amd_sd --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download amd_sd --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('amd_sd')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [kaggle.com/datasets](https://www.kaggle.com/datasets/gaoweihao/amd-sd)

**Source-term evidence:** [kaggle.com/datasets](https://www.kaggle.com/datasets/gaoweihao/amd-sd)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('amd_sd')
samples = ds.load(data_dir, split='train')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{amd_sd,
  title  = { AMD-SD: OCT Wet AMD Lesion Segmentation Dataset },
  note   = { Hu Y et al., 'AMD-SD: An Optical Coherence Tomography Image Dataset for wet AMD Lesions Segmentation', Scientific Data 11, 1014 (2024). doi:10.1038/s41597-024-03844-6 },
  year   = { 2024 },
  url    = { https://www.kaggle.com/datasets/gaoweihao/amd-sd },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Hu Y et al., 'AMD-SD: An Optical Coherence Tomography Image Dataset for wet AMD Lesions Segmentation', Scientific Data 11, 1014 (2024). doi:10.1038/s41597-024-03844-6
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC BY-NC-ND 4.0
- **Normalized category:** `cc-by-nc-nd`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Explicit noncommercial clause recorded; check source

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
