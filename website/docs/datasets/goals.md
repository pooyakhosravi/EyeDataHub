---
id: goals
title: "GOALS — Glaucoma OCT Layer Segmentation (MICCAI 2022)"
sidebar_label: goals
description: "300 circumpapillary OCT images. RNFL/GCIPL/choroid layer segmentation plus binary glaucoma classification."
tags: ["oct", "cc-by", "gdrive", "segmentation", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# GOALS — Glaucoma OCT Layer Segmentation (MICCAI 2022)

300 circumpapillary OCT images. RNFL/GCIPL/choroid layer segmentation plus binary glaucoma classification.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `goals` |
| **Full name** | GOALS — Glaucoma OCT Layer Segmentation (MICCAI 2022) |
| **Primary category** | `oct` |
| **Contained modalities** | oct |
| **Tasks** | segmentation, classification |
| **Samples** | 300 |
| **Classes** | 3 (RNFL, GCIPL, Choroid) |
| **Splits** | train, test |
| **Size** | 0.5 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Google Drive |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `loader_implemented_not_live_tested` |
| **Legacy sample-loader status** | Standard loader included |


## Notes

> Primary challenge page: https://aistudio.baidu.com/competition/detail/783/0/introduction. Automated downloader still tries the known Google Drive mirror (https://drive.google.com/file/d/1P1cLm9_Pwq4fum4lB1-LGUayO-NMvF5I/view) and then Zenodo record 6362363.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download goals --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download goals --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('goals')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [aistudio.baidu.com/competition](https://aistudio.baidu.com/competition/detail/783/0/introduction)

**Source-term evidence:** [aistudio.baidu.com/competition](https://aistudio.baidu.com/competition/detail/783/0/introduction)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('goals')
samples = ds.load(data_dir, split='test')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{goals,
  title  = { GOALS — Glaucoma OCT Layer Segmentation (MICCAI 2022) },
  note   = { Fang H. et al., 'GOALS Challenge: A Large-Scale OCT Image Dataset for Glaucoma Analysis', MICCAI 2022 Workshop },
  year   = { 2022 },
  url    = { https://aistudio.baidu.com/competition/detail/783/0/introduction },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Fang H. et al., 'GOALS Challenge: A Large-Scale OCT Image Dataset for Glaucoma Analysis', MICCAI 2022 Workshop.
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
