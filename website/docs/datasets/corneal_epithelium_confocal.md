---
id: corneal_epithelium_confocal
title: "Keratoconus Corneal Epithelium Confocal Fluorescence Dataset"
sidebar_label: corneal_epithelium_confocal
description: "Small corneal confocal fluorescence imaging dataset for keratoconus epithelium analysis."
tags: ["confocal", "cc-by", "mendeley", "classification", "segmentation"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Keratoconus Corneal Epithelium Confocal Fluorescence Dataset

Small corneal confocal fluorescence imaging dataset for keratoconus epithelium analysis.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `corneal_epithelium_confocal` |
| **Full name** | Keratoconus Corneal Epithelium Confocal Fluorescence Dataset |
| **Primary category** | `confocal` |
| **Contained modalities** | confocal |
| **Tasks** | classification, segmentation |
| **Samples** | 7 |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.1 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Mendeley Data |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download corneal_epithelium_confocal --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download corneal_epithelium_confocal --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('corneal_epithelium_confocal')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/n3gky25brh/2)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/n3gky25brh/2)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{corneal_epithelium_confocal,
  title  = { Keratoconus Corneal Epithelium Confocal Fluorescence Dataset },
  note   = { Keratoconus corneal epithelium confocal fluorescence dataset. Mendeley Data, V2, 2025. doi:10.17632/n3gky25brh.2 },
  year   = { 2025 },
  url    = { https://data.mendeley.com/datasets/n3gky25brh/2 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Keratoconus corneal epithelium confocal fluorescence dataset. Mendeley Data, V2, 2025. doi:10.17632/n3gky25brh.2
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
- [corn_pro](./corn_pro.md): CORN Pro: Corneal Nerve Confocal Microscopy Dataset (688 records, `cc-by`)
- [superccm_fineset](./superccm_fineset.md): SuperCCM-FineSet (210 records, `unknown`)
- [corn_collection](./corn_collection.md): CORN: Corneal Confocal Microscope Dataset Collection (count not reported records, `cc-by`)
