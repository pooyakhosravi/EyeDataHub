---
id: hrf
title: "HRF: High-Resolution Fundus Image Database"
sidebar_label: hrf
description: "45 high-resolution fundus images (healthy/DR/glaucoma) with manual vessel segmentation."
tags: ["fundus", "cc-by", "manual", "segmentation"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# HRF: High-Resolution Fundus Image Database

45 high-resolution fundus images (healthy/DR/glaucoma) with manual vessel segmentation.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `hrf` |
| **Full name** | HRF: High-Resolution Fundus Image Database |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | segmentation |
| **Samples** | 45 |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.5 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `guided_instructions_only` |
| **Legacy sample-loader status** | Standard loader included |


## Notes

> Requires manual download from FAU Erlangen-Nuremberg website.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download hrf --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download hrf --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('hrf')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [www5.cs.fau.de/research](https://www5.cs.fau.de/research/data/fundus-images/)

**Source-term evidence:** [www5.cs.fau.de/research](https://www5.cs.fau.de/research/data/fundus-images/)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('hrf')
samples = ds.load(data_dir, split='all')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{hrf,
  title  = { HRF: High-Resolution Fundus Image Database },
  note   = { Budai et al., 'Robust vessel segmentation in fundus images', Intl Journal of Biomedical Imaging 2013 },
  year   = { 2013 },
  url    = { https://www5.cs.fau.de/research/data/fundus-images/ },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Budai et al., 'Robust vessel segmentation in fundus images', Intl Journal of Biomedical Imaging 2013.
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
