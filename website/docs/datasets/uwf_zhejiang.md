---
id: uwf_zhejiang
title: "Open UWF Fundus Dataset with Disease + Quality Labels"
sidebar_label: uwf_zhejiang
description: "700 Optos ultra-wide-field fundus images with multi-disease classification labels and image-quality flags from real-world clinical practice."
tags: ["uwf_fundus", "cc-by", "figshare", "classification", "quality", "resource-role-current-dataset", "dataset-family-uwf-zhejiang"]
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
| **Resource role** | `current_dataset` |
| **Dataset family** | `uwf_zhejiang` |
| **Contained modalities** | uwf_fundus |
| **Tasks** | classification, quality |
| **Primary reported quantity** | 700 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 2.0 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Figshare |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `end_to_end_tested` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 700 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [https://doi.org/10.6084/m9.figshare.26936446](https://doi.org/10.6084/m9.figshare.26936446) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download uwf_zhejiang --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download uwf_zhejiang --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('uwf_zhejiang')
print(preflight_dataset(ds, './data'))  # no download
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

## Similar resources by shared modality

- [mmrdr](./mmrdr.md): MMRDR: Multi-Modal Retinal Diabetic Retinopathy Dataset (24,460 images, `cc-by`)
- [oculoscope](./oculoscope.md): OculoScope: Fairer AI in Ophthalmology Dataset (16,530 images, `cc-by`)
- [tsukazaki_uwf](./tsukazaki_uwf.md): Tsukazaki Hospital UWF Fundus Dataset (13,047 images, `research-only`)
- [birdshot_wide](./birdshot_wide.md): Birdshot-WIDE Widefield Fundus Dataset (6,352 images, `cc-by`)
- [deepdrid](./deepdrid.md): DeepDRiD: Diabetic Retinopathy Grading and Image Quality Dataset (2,256 images, `cc-by-sa`)
- [uwf_tumor](./uwf_tumor.md): UWF Fundus Intraocular Tumor Dataset (2,031 images, `cc-by`)
- [uwf_dr_peng](./uwf_dr_peng.md): UWF Fundus DR Dataset (Peng et al., 2026) (1,630 images, `cc-by`)
- [uwf_dr](./uwf_dr.md): UWF DR Reasoning Dataset (495 images, `research-only`)
