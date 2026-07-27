---
id: octave
title: "OCTAVE: 3D SD-OCT Retinal Segmentation Dataset"
sidebar_label: octave
description: "198 annotated 3D SD-OCT volumes (3,762 B-scans) with pixel-level labels for 13 anatomic and pathological retinal features: retina, choroid, vitreous, RPE, hyaloid, ERM, fluid, subretinal material, hyp"
tags: ["oct", "cc-by-sa", "zenodo", "segmentation"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# OCTAVE: 3D SD-OCT Retinal Segmentation Dataset

198 annotated 3D SD-OCT volumes (3,762 B-scans) with pixel-level labels for 13 anatomic and pathological retinal features: retina, choroid, vitreous, RPE, hyaloid, ERM, fluid, subretinal material, hypertransmission defects, and more. 4 additional external validation sets (221 volumes). nnU-Net-compatible format. IOVS 2025.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `octave` |
| **Full name** | OCTAVE: 3D SD-OCT Retinal Segmentation Dataset |
| **Primary category** | `oct` |
| **Contained modalities** | oct |
| **Tasks** | segmentation |
| **Samples** | 198 |
| **Classes** | 13 (RET, CHO, VIT, RPE, HYA, RHS, ERM, SES, ART, HRM, FLU, SRM, HTD) |
| **Splits** | train |
| **Size** | 15.0 GB |
| **Source-stated terms** | CC BY-SA 4.0 |
| **Normalized terms** | `cc-by-sa` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Zenodo |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Standard loader included |


## Notes

> nnU-Net layout: nnUNet_raw/Dataset001_OCTAVE/imagesTr+labelsTr/. External test sets under nnUNet_raw/external_tests/. 19 standardised B-scans per volume after preprocessing. GitHub: https://github.com/Translational-Biophotonics-Laboratory/octvision3d

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download octave --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download octave --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('octave')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [zenodo.org/records](https://zenodo.org/records/14580071)

**Source-term evidence:** [zenodo.org/records](https://zenodo.org/records/14580071)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('octave')
samples = ds.load(data_dir, split='train')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{octave,
  title  = { OCTAVE: 3D SD-OCT Retinal Segmentation Dataset },
  note   = { Kermany DS et al., 'Identifying Retinal Features Using a Self-Configuring CNN for Clinical Intervention', Investigative Ophthalmology & Visual Science 66(6):55 (2025). doi:10.1167/iovs.66.6.55 — Zenodo: https://zenodo.org/records/14580071 },
  year   = { 2025 },
  url    = { https://zenodo.org/records/14580071 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Kermany DS et al., 'Identifying Retinal Features Using a Self-Configuring CNN for Clinical Intervention', Investigative Ophthalmology & Visual Science 66(6):55 (2025). doi:10.1167/iovs.66.6.55 — Zenodo: https://zenodo.org/records/14580071
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC BY-SA 4.0
- **Normalized category:** `cc-by-sa`
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
