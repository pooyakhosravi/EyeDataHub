---
id: amd_sd
title: "AMD-SD: OCT Wet AMD Lesion Segmentation Dataset"
sidebar_label: amd_sd
description: "3,049 OCT B-scan images (1,140×380 px) from 138 wet AMD patients (156 eyes) with pixel-level annotations for 5 lesion classes: Subretinal Fluid (SRF), Intraretinal Fluid (IRF), Ellipsoid Zone Continui"
tags: ["oct", "cc-by-nc-nd", "kaggle", "segmentation"]
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
| **Primary category** | `oct` |
| **Contained modalities** | oct |
| **Tasks** | segmentation |
| **Samples** | 3,049 |
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


## Notes

> Official split: training.txt / validation.txt at dataset root. Images in AMD-SD/images/&lt;patient_id&gt;/&lt;scan&gt;.png. Primary source: Figshare collection 7157554; mirror on Kaggle: gaoweihao/amd-sd.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download amd_sd --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download amd_sd --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('amd_sd')
print(preflight_dataset(ds, './data'))  # no transfer
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

## Related datasets with shared modalities

- [syn_oct](./syn_oct.md): SYN-OCT Synthetic Glaucoma OCT Dataset (200,000 records, `cc-by`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 records, `unknown`)
- [kermany_oct](./kermany_oct.md): Kermany OCT 2018: Retinal OCT Image Classification (84,484 records, `cc-by`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (58,036 records, `mit`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 records, `unknown`)
- [harvard_fairvision](./harvard_fairvision.md): Harvard-FairVision (AMD + DR + Glaucoma, paired SLO + OCT) (30,000 records, `cc-by-nc-nd`)
- [mario](./mario.md): MARIO: AMD-Progression Longitudinal OCT (MICCAI 2024) (30,000 records, `cc-by`)
- [mmrdr](./mmrdr.md): MMRDR: Multi-Modal Retinal Diabetic Retinopathy Dataset (24,460 records, `cc-by`)
