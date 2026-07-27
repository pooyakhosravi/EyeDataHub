---
id: harvard_glaucoma
title: "Harvard Glaucoma Fundus Image Dataset"
sidebar_label: harvard_glaucoma
description: "Fundus images for glaucoma detection from Harvard Medical School / Mass Eye and Ear. Binary glaucoma classification."
tags: ["fundus", "cc0", "direct", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Harvard Glaucoma Fundus Image Dataset

Fundus images for glaucoma detection from Harvard Medical School / Mass Eye and Ear. Binary glaucoma classification.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `harvard_glaucoma` |
| **Full name** | Harvard Glaucoma Fundus Image Dataset |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | classification |
| **Samples** | 1,000 |
| **Classes** | 2 (Non-glaucoma, Glaucoma) |
| **Splits** | all |
| **Size** | 1.5 GB |
| **Source-stated terms** | CC0 1.0 (Public Domain) |
| **Normalized terms** | `cc0` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Direct HTTP |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `loader_implemented_not_live_tested` |
| **Legacy sample-loader status** | Standard loader included |


## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download harvard_glaucoma --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download harvard_glaucoma --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('harvard_glaucoma')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.7910/DVN/1YRRAC](https://doi.org/10.7910/DVN/1YRRAC)

**Source-term evidence:** [https://doi.org/10.7910/DVN/1YRRAC](https://doi.org/10.7910/DVN/1YRRAC)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('harvard_glaucoma')
samples = ds.load(data_dir, split='all')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{harvard_glaucoma,
  title  = { Harvard Glaucoma Fundus Image Dataset },
  note   = { Luo X. et al., 'Harvard Glaucoma Detection and Progression Dataset', Harvard Dataverse, doi:10.7910/DVN/1YRRAC, 2023 },
  year   = { 2023 },
  url    = { https://doi.org/10.7910/DVN/1YRRAC },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Luo X. et al., 'Harvard Glaucoma Detection and Progression Dataset', Harvard Dataverse, doi:10.7910/DVN/1YRRAC, 2023.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC0 1.0 (Public Domain)
- **Normalized category:** `cc0`
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
