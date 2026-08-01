---
id: stare
title: "STARE: Structured Analysis of the Retina"
sidebar_label: stare
description: "20 fundus images with manual vessel segmentation (two annotators)."
tags: ["fundus", "research-only", "direct", "segmentation"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# STARE: Structured Analysis of the Retina

20 fundus images with manual vessel segmentation (two annotators).

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `stare` |
| **Full name** | STARE: Structured Analysis of the Retina |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | segmentation |
| **Samples** | 20 |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.02 GB |
| **Source-stated terms** | Research only |
| **Normalized terms** | `research-only` |
| **Descriptive screening label** | Research or challenge restriction recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Direct HTTP |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `end_to_end_tested` |
| **Legacy sample-loader status** | Standard loader included |


## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download stare --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download stare --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('stare')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [cecas.clemson.edu/~ahoover](https://cecas.clemson.edu/~ahoover/stare/)

**Source-term evidence:** [cecas.clemson.edu/~ahoover](https://cecas.clemson.edu/~ahoover/stare/)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('stare')
samples = ds.load(data_dir, split='all')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{stare,
  title  = { STARE: Structured Analysis of the Retina },
  note   = { Hoover et al., 'Locating blood vessels in retinal images by piece-wise threshold probing of a matched filter response', IEEE TMI 2000 },
  year   = { 2000 },
  url    = { https://cecas.clemson.edu/~ahoover/stare/ },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Hoover et al., 'Locating blood vessels in retinal images by piece-wise threshold probing of a matched filter response', IEEE TMI 2000.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Research only
- **Normalized category:** `research-only`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Research or challenge restriction recorded; check source

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
