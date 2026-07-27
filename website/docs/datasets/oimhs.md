---
id: oimhs
title: "OIMHS: OCT Image Macular Hole Segmentation Dataset"
sidebar_label: oimhs
description: "3,859 OCT B-scan images (125 eyes, 119 patients) for macular hole segmentation. Each PNG is side-by-side: left half raw B-scan, right half colour-coded mask for 4 classes: Retina, Macular Hole, Intrar"
tags: ["oct", "cc0", "figshare", "segmentation"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# OIMHS: OCT Image Macular Hole Segmentation Dataset

3,859 OCT B-scan images (125 eyes, 119 patients) for macular hole segmentation. Each PNG is side-by-side: left half raw B-scan, right half colour-coded mask for 4 classes: Retina, Macular Hole, Intraretinal Cysts, Choroid.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `oimhs` |
| **Full name** | OIMHS: OCT Image Macular Hole Segmentation Dataset |
| **Primary category** | `oct` |
| **Contained modalities** | oct |
| **Tasks** | segmentation |
| **Samples** | 3,859 |
| **Classes** | 4 (Retina, Macular Hole, Intraretinal Cysts, Choroid) |
| **Splits** | train |
| **Size** | 2.0 GB |
| **Source-stated terms** | CC0 1.0 |
| **Normalized terms** | `cc0` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Figshare |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Standard loader included |


## Notes

> Images are side-by-side PNGs (left=raw, right=mask). 125 eye-level subfolders under images/. No official split — apply your own train/val/test division.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download oimhs --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download oimhs --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('oimhs')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.6084/m9.figshare.23508453](https://doi.org/10.6084/m9.figshare.23508453)

**Source-term evidence:** [https://doi.org/10.6084/m9.figshare.23508453](https://doi.org/10.6084/m9.figshare.23508453)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('oimhs')
samples = ds.load(data_dir, split='train')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{oimhs,
  title  = { OIMHS: OCT Image Macular Hole Segmentation Dataset },
  note   = { Ye X et al., 'OIMHS: An Optical Coherence Tomography Image Dataset Based on Macular Hole Manual Segmentation', Scientific Data 10, 769 (2023). doi:10.1038/s41597-023-02675-1 },
  year   = { 2023 },
  url    = { https://doi.org/10.6084/m9.figshare.23508453 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Ye X et al., 'OIMHS: An Optical Coherence Tomography Image Dataset Based on Macular Hole Manual Segmentation', Scientific Data 10, 769 (2023). doi:10.1038/s41597-023-02675-1
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC0 1.0
- **Normalized category:** `cc0`
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
