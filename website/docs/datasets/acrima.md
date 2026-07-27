---
id: acrima
title: "ACRIMA: Glaucoma Optic Disc Fundus Database"
sidebar_label: acrima
description: "705 optic disc-centred fundus photographs (396 normal + 309 glaucoma) from Hospital Clinico San Carlos. Expert-annotated binary glaucoma classification."
tags: ["fundus", "cc-by", "figshare", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# ACRIMA: Glaucoma Optic Disc Fundus Database

705 optic disc-centred fundus photographs (396 normal + 309 glaucoma) from Hospital Clinico San Carlos. Expert-annotated binary glaucoma classification.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `acrima` |
| **Full name** | ACRIMA: Glaucoma Optic Disc Fundus Database |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | classification |
| **Samples** | 705 |
| **Classes** | 2 (Normal, Glaucoma) |
| **Splits** | train |
| **Size** | 0.5 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Figshare |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `guided_instructions_only` |
| **Legacy sample-loader status** | Standard loader included |


## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download acrima --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download acrima --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('acrima')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [Figshare private-share page](https://figshare.com/s/c2d31f850af14c5b5232)

**Source-term evidence:** [Figshare private-share page](https://figshare.com/s/c2d31f850af14c5b5232)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('acrima')
samples = ds.load(data_dir, split='train')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{acrima,
  title  = { ACRIMA: Glaucoma Optic Disc Fundus Database },
  note   = { Diaz-Pinto et al., 'Retinal Image Synthesis and Semi-Supervised Learning for Glaucoma Assessment', IEEE TMI 2019. Data: https://figshare.com/s/c2d31f850af14c5b5232 },
  year   = { 2019 },
  url    = { https://figshare.com/s/c2d31f850af14c5b5232 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Diaz-Pinto et al., 'Retinal Image Synthesis and Semi-Supervised Learning for Glaucoma Assessment', IEEE TMI 2019. Data: https://figshare.com/s/c2d31f850af14c5b5232
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
