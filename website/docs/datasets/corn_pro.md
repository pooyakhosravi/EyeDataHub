---
id: corn_pro
title: "CORN Pro: Corneal Nerve Confocal Microscopy Dataset"
sidebar_label: corn_pro
description: "1,120 in-vivo confocal microscopy images with pixel-level annotations for corneal subbasal nerves and corneal cells. The source describes 560 images with nerves and Langerhans cells and 560 images wit"
tags: ["confocal", "cc-by", "manual", "segmentation"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# CORN Pro: Corneal Nerve Confocal Microscopy Dataset

1,120 in-vivo confocal microscopy images with pixel-level annotations for corneal subbasal nerves and corneal cells. The source describes 560 images with nerves and Langerhans cells and 560 images with nerves and/or stromal cells.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `corn_pro` |
| **Full name** | CORN Pro: Corneal Nerve Confocal Microscopy Dataset |
| **Primary category** | `confocal` |
| **Contained modalities** | confocal |
| **Tasks** | segmentation |
| **Samples** | 1,120 |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.5 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `controlled_or_manual` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `manual_access_blocked` |
| **Legacy sample-loader status** | Standard loader included |


## Notes

> Restricted access. Steps to obtain:
>   1. Create a free account at https://zenodo.org
>   2. Visit https://zenodo.org/records/14263883
>   3. Click 'Request access' with affiliation & purpose
> Full CORN database: https://imed.nimte.ac.cn/CORN.html

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# This route requires upstream human action; no transfer starts.
eyehub download corn_pro --data-dir ./data --dry-run --json
# Follow the official instructions shown by preflight.
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('corn_pro')
print(preflight_dataset(ds, './data'))  # returns manual_access_blocked
```

  </TabItem>
</Tabs>

**Upstream page:** [zenodo.org/records](https://zenodo.org/records/14263883)

**Source-term evidence:** [zenodo.org/records](https://zenodo.org/records/14263883)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('corn_pro')
samples = ds.load(data_dir, split='all')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{corn_pro,
  title  = { CORN Pro: Corneal Nerve Confocal Microscopy Dataset },
  note   = { CORN database (https://imed.nimte.ac.cn/CORN.html). Zenodo record 14263883: https://zenodo.org/records/14263883 },
  url    = { https://zenodo.org/records/14263883 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
CORN database (https://imed.nimte.ac.cn/CORN.html). Zenodo record 14263883: https://zenodo.org/records/14263883
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

- [corn1500](./corn1500.md): CORN-1500: Corneal Nerve Tortuosity Grading (1,500 records, `unknown`)
- [superccm_fineset](./superccm_fineset.md): SuperCCM-FineSet (210 records, `unknown`)
- [corneal_epithelium_confocal](./corneal_epithelium_confocal.md): Keratoconus Corneal Epithelium Confocal Fluorescence Dataset (7 records, `cc-by`)
- [corn_collection](./corn_collection.md): CORN: Corneal Confocal Microscope Dataset Collection (count not reported records, `cc-by`)
