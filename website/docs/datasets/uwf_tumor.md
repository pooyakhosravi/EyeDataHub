---
id: uwf_tumor
title: "UWF Fundus Intraocular Tumor Dataset"
sidebar_label: uwf_tumor
description: "2,031 ultra-widefield fundus images for AI-assisted intraocular tumor detection and classification. Six categories: Normal, Choroidal Hemangioma (CH), Retinal Capillary Hemangioma (RCH), Choroidal Ost"
tags: ["uwf_fundus", "cc-by", "figshare", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# UWF Fundus Intraocular Tumor Dataset

2,031 ultra-widefield fundus images for AI-assisted intraocular tumor detection and classification. Six categories: Normal, Choroidal Hemangioma (CH), Retinal Capillary Hemangioma (RCH), Choroidal Osteoma (CO), Retinoblastoma (RB), Uveal Melanoma (UM). Annotated by 3 experts; split 8:1:1 (stratified).

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `uwf_tumor` |
| **Full name** | UWF Fundus Intraocular Tumor Dataset |
| **Primary category** | `uwf_fundus` |
| **Contained modalities** | uwf_fundus |
| **Tasks** | classification |
| **Samples** | 2,031 |
| **Classes** | 6 (Normal, Choroidal Hemangioma, Retinal Capillary Hemangioma, Choroidal Osteoma, Retinoblastoma, Uveal Melanoma) |
| **Splits** | train, val, test |
| **Size** | 2.0 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Figshare |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `end_to_end_tested` |
| **Legacy sample-loader status** | Standard loader included |


## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download uwf_tumor --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download uwf_tumor --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('uwf_tumor')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.6084/m9.figshare.27986258](https://doi.org/10.6084/m9.figshare.27986258)

**Source-term evidence:** [https://doi.org/10.6084/m9.figshare.27986258](https://doi.org/10.6084/m9.figshare.27986258)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('uwf_tumor')
samples = ds.load(data_dir, split='test')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{uwf_tumor,
  title  = { UWF Fundus Intraocular Tumor Dataset },
  note   = { UWF Intraocular Tumor Dataset. Scientific Data 2025. https://www.nature.com/articles/s41597-025-05864-2 — Figshare: https://doi.org/10.6084/m9.figshare.27986258 },
  year   = { 2025 },
  url    = { https://doi.org/10.6084/m9.figshare.27986258 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
UWF Intraocular Tumor Dataset. Scientific Data 2025. https://www.nature.com/articles/s41597-025-05864-2 — Figshare: https://doi.org/10.6084/m9.figshare.27986258
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

- [mmrdr](./mmrdr.md): MMRDR: Multi-Modal Retinal Diabetic Retinopathy Dataset (24,460 records, `cc-by`)
- [oculoscope](./oculoscope.md): OculoScope: Fairer AI in Ophthalmology Dataset (16,530 records, `cc-by`)
- [tsukazaki_uwf](./tsukazaki_uwf.md): Tsukazaki Hospital UWF Fundus Dataset (13,047 records, `research-only`)
- [birdshot_wide](./birdshot_wide.md): Birdshot-WIDE Widefield Fundus Dataset (6,352 records, `cc-by`)
- [deepdrid](./deepdrid.md): DeepDRiD: Diabetic Retinopathy Grading and Image Quality Dataset (2,256 records, `cc-by-sa`)
- [uwf_dr_peng](./uwf_dr_peng.md): UWF Fundus DR Dataset (Peng et al., 2026) (1,630 records, `cc-by`)
- [uwf_zhejiang](./uwf_zhejiang.md): Open UWF Fundus Dataset with Disease + Quality Labels (700 records, `cc-by`)
- [uwf_dr](./uwf_dr.md): UWF DR Reasoning Dataset (495 records, `research-only`)
