---
id: tian_oct
title: "Tian OCTRIMA 3D OCT Layer Segmentation Dataset"
sidebar_label: tian_oct
description: "10 Heidelberg Spectralis SD-OCT volumes (510 B-scans, 496×644×51 voxels) from healthy subjects with 8 retinal layer boundary annotations by 2 independent observers. MATLAB .mat format; used as the OCT"
tags: ["oct", "cc-by", "direct", "segmentation"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Tian OCTRIMA 3D OCT Layer Segmentation Dataset

10 Heidelberg Spectralis SD-OCT volumes (510 B-scans, 496×644×51 voxels) from healthy subjects with 8 retinal layer boundary annotations by 2 independent observers. MATLAB .mat format; used as the OCTRIMA 3D validation set.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `tian_oct` |
| **Full name** | Tian OCTRIMA 3D OCT Layer Segmentation Dataset |
| **Primary category** | `oct` |
| **Contained modalities** | oct |
| **Tasks** | segmentation |
| **Samples** | 10 |
| **Classes** | 8 (ILM, RNFL_GCL_IPL, IPL_INL, INL_OPL, OPL_ONL, ELM, IS_OS, OS_RPE) |
| **Splits** | test |
| **Size** | 0.2 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Direct HTTP |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `loader_implemented_not_live_tested` |
| **Legacy sample-loader status** | Standard loader included |


## Notes

> Primarily a benchmark/test set (10 volumes, 2 observers). Each .mat file contains: raw OCT volume, OCTRIMA 3D automatic segmentation, Observer 1 manual, Observer 2 manual. Supplement URL: https://doi.org/10.1371/journal.pone.0133908.s002

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download tian_oct --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download tian_oct --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('tian_oct')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.1371/journal.pone.0133908.s002](https://doi.org/10.1371/journal.pone.0133908.s002)

**Source-term evidence:** [https://doi.org/10.1371/journal.pone.0133908.s002](https://doi.org/10.1371/journal.pone.0133908.s002)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('tian_oct')
samples = ds.load(data_dir, split='test')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{tian_oct,
  title  = { Tian OCTRIMA 3D OCT Layer Segmentation Dataset },
  note   = { Tian J et al., 'Real-Time Automatic Segmentation of Optical Coherence Tomography Volume Data of the Macular Region', PLOS ONE 10(8):e0133908 (2015). doi:10.1371/journal.pone.0133908 },
  year   = { 2015 },
  url    = { https://doi.org/10.1371/journal.pone.0133908.s002 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Tian J et al., 'Real-Time Automatic Segmentation of Optical Coherence Tomography Volume Data of the Macular Region', PLOS ONE 10(8):e0133908 (2015). doi:10.1371/journal.pone.0133908
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
