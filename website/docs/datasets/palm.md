---
id: palm
title: "PALM — iChallenge Pathologic Myopia"
sidebar_label: palm
description: "1200 fundus images for pathologic myopia classification and optic disc / lesion segmentation. 50 % PM / 50 % non-PM."
tags: ["fundus", "research-only", "gdrive", "classification", "segmentation"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# PALM — iChallenge Pathologic Myopia

1200 fundus images for pathologic myopia classification and optic disc / lesion segmentation. 50 % PM / 50 % non-PM.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `palm` |
| **Full name** | PALM — iChallenge Pathologic Myopia |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | classification, segmentation |
| **Samples** | 1,200 |
| **Classes** | 2 (non-PM, PM) |
| **Splits** | train, val, test |
| **Size** | 1.5 GB |
| **Source-stated terms** | Challenge data-use agreement (IEEE DataPort) |
| **Normalized terms** | `research-only` |
| **Descriptive screening label** | Research or challenge restriction recorded; check source |
| **Terms scope** | `challenge_participation` |
| **Access friction** | `controlled_or_manual` |
| **Route backend** | Google Drive |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `manual_access_blocked` |
| **Legacy sample-loader status** | Standard loader included |


## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# This route requires upstream human action; no transfer starts.
eyehub download palm --data-dir ./data --dry-run --json
# Follow the official instructions shown by preflight.
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('palm')
print(preflight_dataset(ds, './data'))  # returns manual_access_blocked
```

  </TabItem>
</Tabs>

**Upstream page:** [drive.google.com/file](https://drive.google.com/file/d/14XWD6kX0dVRfAyEc7FkZGKZibWEkvnyv/view)

**Source-term evidence:** [drive.google.com/file](https://drive.google.com/file/d/14XWD6kX0dVRfAyEc7FkZGKZibWEkvnyv/view)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('palm')
samples = ds.load(data_dir, split='test')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{palm,
  title  = { PALM — iChallenge Pathologic Myopia },
  note   = { Fu H. et al., 'PALM: Pathologic Myopia Challenge', MICCAI 2019 Workshop },
  year   = { 2019 },
  url    = { https://drive.google.com/file/d/14XWD6kX0dVRfAyEc7FkZGKZibWEkvnyv/view },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Fu H. et al., 'PALM: Pathologic Myopia Challenge', MICCAI 2019 Workshop.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Challenge data-use agreement (IEEE DataPort)
- **Normalized category:** `research-only`
- **Apparent scope:** `challenge_participation`
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
