---
id: prime_fp20
title: "PRIME-FP20: Ultra-Widefield Vessel Segmentation"
sidebar_label: prime_fp20
description: "15 ultra-widefield (Optos) fundus images with pixel-level vessel segmentation ground truth."
tags: ["uwf_fundus", "cc-by", "manual", "segmentation"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# PRIME-FP20: Ultra-Widefield Vessel Segmentation

15 ultra-widefield (Optos) fundus images with pixel-level vessel segmentation ground truth.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `prime_fp20` |
| **Full name** | PRIME-FP20: Ultra-Widefield Vessel Segmentation |
| **Primary category** | `uwf_fundus` |
| **Contained modalities** | uwf_fundus |
| **Tasks** | segmentation |
| **Primary reported quantity** | 15 images |
| **Classes** | 2 (background, vessel) |
| **Splits** | all |
| **Size** | 0.5 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `guided_instructions_only` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 15 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [ieee-dataport.org/open-access](https://ieee-dataport.org/open-access/prime-fp20-ultra-widefield-fundus-photography-vessel-segmentation-dataset) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> IEEE DataPort free account login required.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download prime_fp20 --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download prime_fp20 --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('prime_fp20')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [ieee-dataport.org/open-access](https://ieee-dataport.org/open-access/prime-fp20-ultra-widefield-fundus-photography-vessel-segmentation-dataset)

**Source-term evidence:** [ieee-dataport.org/open-access](https://ieee-dataport.org/open-access/prime-fp20-ultra-widefield-fundus-photography-vessel-segmentation-dataset)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{prime_fp20,
  title  = { PRIME-FP20: Ultra-Widefield Vessel Segmentation },
  note   = { Ding et al., 'A Novel Deep Learning Pipeline for Retinal Vessel Detection in Fluorescein Angiography', IEEE TMI 2021 },
  year   = { 2021 },
  url    = { https://ieee-dataport.org/open-access/prime-fp20-ultra-widefield-fundus-photography-vessel-segmentation-dataset },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Ding et al., 'A Novel Deep Learning Pipeline for Retinal Vessel Detection in Fluorescein Angiography', IEEE TMI 2021.
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
- [uwf_zhejiang](./uwf_zhejiang.md): Open UWF Fundus Dataset with Disease + Quality Labels (700 images, `cc-by`)
