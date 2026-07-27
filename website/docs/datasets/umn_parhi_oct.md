---
id: umn_parhi_oct
title: "UMN Parhi Lab AMD OCT Fluid Segmentation Dataset"
sidebar_label: umn_parhi_oct
description: "600 Spectralis OCT B-scans from 24 exudative AMD subjects. Three fluid region classes: IRF, SRF, PED. Dual expert annotation."
tags: ["oct", "research-only", "direct", "segmentation"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# UMN Parhi Lab AMD OCT Fluid Segmentation Dataset

600 Spectralis OCT B-scans from 24 exudative AMD subjects. Three fluid region classes: IRF, SRF, PED. Dual expert annotation.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `umn_parhi_oct` |
| **Full name** | UMN Parhi Lab AMD OCT Fluid Segmentation Dataset |
| **Primary category** | `oct` |
| **Contained modalities** | oct |
| **Tasks** | segmentation |
| **Samples** | 600 |
| **Classes** | 3 (IRF, SRF, PED) |
| **Splits** | all |
| **Size** | 0.5 GB |
| **Source-stated terms** | Academic research use (University of Minnesota) |
| **Normalized terms** | `research-only` |
| **Descriptive screening label** | Research or challenge restriction recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Direct HTTP |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `loader_implemented_not_live_tested` |
| **Legacy sample-loader status** | Standard loader included |


## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download umn_parhi_oct --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download umn_parhi_oct --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('umn_parhi_oct')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [people.ece.umn.edu/users](http://people.ece.umn.edu/users/parhi/.DATA/OCT/DME/UMNDataset.mat)

**Source-term evidence:** [people.ece.umn.edu/users](http://people.ece.umn.edu/users/parhi/.DATA/OCT/DME/UMNDataset.mat)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('umn_parhi_oct')
samples = ds.load(data_dir, split='all')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{umn_parhi_oct,
  title  = { UMN Parhi Lab AMD OCT Fluid Segmentation Dataset },
  note   = { Parhi Lab OCT AMD Fluid Dataset. http://people.ece.umn.edu/users/parhi/data-and-code/ },
  url    = { http://people.ece.umn.edu/users/parhi/.DATA/OCT/DME/UMNDataset.mat },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Parhi Lab OCT AMD Fluid Dataset. http://people.ece.umn.edu/users/parhi/data-and-code/
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Academic research use (University of Minnesota)
- **Normalized category:** `research-only`
- **Apparent scope:** `dataset_files`
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
