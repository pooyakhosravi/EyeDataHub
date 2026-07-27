---
id: refuge2
title: "REFUGE2 — Retinal Fundus Glaucoma Challenge 2"
sidebar_label: refuge2
description: "2000 fundus images for glaucoma classification, optic disc/cup segmentation, and fovea localisation. Extends REFUGE1."
tags: ["fundus", "research-only", "gdrive", "classification", "segmentation"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# REFUGE2 — Retinal Fundus Glaucoma Challenge 2

2000 fundus images for glaucoma classification, optic disc/cup segmentation, and fovea localisation. Extends REFUGE1.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `refuge2` |
| **Full name** | REFUGE2 — Retinal Fundus Glaucoma Challenge 2 |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | classification, segmentation |
| **Samples** | 2,000 |
| **Classes** | 2 (non-glaucoma, glaucoma) |
| **Splits** | train, val, test |
| **Size** | 1.2 GB |
| **Source-stated terms** | Research use (Grand Challenge) |
| **Normalized terms** | `research-only` |
| **Descriptive screening label** | Research or challenge restriction recorded; check source |
| **Terms scope** | `challenge_participation` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Google Drive |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `loader_implemented_not_live_tested` |
| **Legacy sample-loader status** | Standard loader included |


## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download refuge2 --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download refuge2 --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('refuge2')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [drive.google.com/file](https://drive.google.com/file/d/1DspRzDqypeBOxZnWPQxmXprNVmJwkBRJ/view)

**Source-term evidence:** [drive.google.com/file](https://drive.google.com/file/d/1DspRzDqypeBOxZnWPQxmXprNVmJwkBRJ/view)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('refuge2')
samples = ds.load(data_dir, split='test')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{refuge2,
  title  = { REFUGE2 — Retinal Fundus Glaucoma Challenge 2 },
  note   = { Fang H. et al., 'REFUGE2 Challenge: Treasure for Multi-Domain Learning in Glaucoma Assessment', MIA 2022 },
  year   = { 2022 },
  url    = { https://drive.google.com/file/d/1DspRzDqypeBOxZnWPQxmXprNVmJwkBRJ/view },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Fang H. et al., 'REFUGE2 Challenge: Treasure for Multi-Domain Learning in Glaucoma Assessment', MIA 2022.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Research use (Grand Challenge)
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
