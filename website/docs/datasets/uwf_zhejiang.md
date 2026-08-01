---
id: uwf_zhejiang
title: "Open UWF Fundus Dataset with Disease + Quality Labels"
sidebar_label: uwf_zhejiang
description: "700 Optos ultra-wide-field fundus images with multi-disease classification labels and image-quality flags from real-world clinical practice."
tags: ["uwf_fundus", "cc-by", "figshare", "classification", "quality"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Open UWF Fundus Dataset with Disease + Quality Labels

700 Optos ultra-wide-field fundus images with multi-disease classification labels and image-quality flags from real-world clinical practice.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `uwf_zhejiang` |
| **Full name** | Open UWF Fundus Dataset with Disease + Quality Labels |
| **Primary category** | `uwf_fundus` |
| **Contained modalities** | uwf_fundus |
| **Tasks** | classification, quality |
| **Samples** | 700 |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 2.0 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Figshare |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `end_to_end_tested` |
| **Legacy sample-loader status** | Metadata and access only |


## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download uwf_zhejiang --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download uwf_zhejiang --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('uwf_zhejiang')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.6084/m9.figshare.26936446](https://doi.org/10.6084/m9.figshare.26936446)

**Source-term evidence:** [https://doi.org/10.6084/m9.figshare.26936446](https://doi.org/10.6084/m9.figshare.26936446)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{uwf_zhejiang,
  title  = { Open UWF Fundus Dataset with Disease + Quality Labels },
  note   = { He S, Ye X, Xie W, et al., 'Open ultrawidefield fundus image dataset with disease diagnosis and clinical image quality assessment', Scientific Data 11:1251, 2024. doi:10.1038/s41597-024-04113-2 },
  year   = { 2024 },
  url    = { https://doi.org/10.6084/m9.figshare.26936446 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
He S, Ye X, Xie W, et al., 'Open ultrawidefield fundus image dataset with disease diagnosis and clinical image quality assessment', Scientific Data 11:1251, 2024. doi:10.1038/s41597-024-04113-2
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
- [uwf_tumor](./uwf_tumor.md): UWF Fundus Intraocular Tumor Dataset (2,031 records, `cc-by`)
- [uwf_dr_peng](./uwf_dr_peng.md): UWF Fundus DR Dataset (Peng et al., 2026) (1,630 records, `cc-by`)
- [uwf_dr](./uwf_dr.md): UWF DR Reasoning Dataset (495 records, `research-only`)
