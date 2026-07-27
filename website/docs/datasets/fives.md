---
id: fives
title: "FIVES: Fundus Image Vessel Segmentation"
sidebar_label: fives
description: "800 high-resolution (2048x2048) fundus images with pixel-wise vessel segmentation. Covers normal, DR, AMD, glaucoma."
tags: ["fundus", "cc-by", "figshare", "segmentation"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# FIVES: Fundus Image Vessel Segmentation

800 high-resolution (2048x2048) fundus images with pixel-wise vessel segmentation. Covers normal, DR, AMD, glaucoma.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `fives` |
| **Full name** | FIVES: Fundus Image Vessel Segmentation |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | segmentation |
| **Samples** | 800 |
| **Classes** | Not reported (Not reported) |
| **Splits** | train, test |
| **Size** | 1.1 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Figshare |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `transfer_tested_partial` |
| **Legacy sample-loader status** | Standard loader included |


## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download fives --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download fives --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('fives')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.6084/m9.figshare.19688169](https://doi.org/10.6084/m9.figshare.19688169)

**Source-term evidence:** [https://doi.org/10.6084/m9.figshare.19688169](https://doi.org/10.6084/m9.figshare.19688169)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('fives')
samples = ds.load(data_dir, split='test')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{fives,
  title  = { FIVES: Fundus Image Vessel Segmentation },
  note   = { Jin et al., 'FIVES: A Fundus Image Dataset for Artificial Intelligence based Vessel Segmentation', Scientific Data 2022 },
  year   = { 2022 },
  url    = { https://doi.org/10.6084/m9.figshare.19688169 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Jin et al., 'FIVES: A Fundus Image Dataset for Artificial Intelligence based Vessel Segmentation', Scientific Data 2022.
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

- [airogs](./airogs.md): AIROGS: AI for Robust Glaucoma Screening (113,893 records, `cc-by-nc-nd`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 records, `unknown`)
- [justraigs](./justraigs.md): JustRAIGS: Just Referral AI Glaucoma Screening Dataset (101,442 records, `cc-by-nc-nd`)
- [eyepacs](./eyepacs.md): EyePACS — Diabetic Retinopathy Detection (Kaggle 2015) (88,702 records, `research-only`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (58,036 records, `mit`)
- [angioreport](./angioreport.md): AngioReport Fundus Angiography Report Dataset (55,361 records, `unknown`)
- [ffa_ir](./ffa_ir.md): FFA-IR Medical Report Dataset (47,247 records, `unknown`)
- [bidr](./bidr.md): BiDR: Diabetic Retinopathy Diagnosis Dataset (35,126 records, `unknown`)
