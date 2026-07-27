---
id: refuge1_multirater
title: "REFUGE Multi-Rater — Glaucoma with Multi-Expert Annotations"
sidebar_label: refuge1_multirater
description: "1200 fundus images from REFUGE1 with optic disc/cup segmentation masks annotated by multiple expert raters."
tags: ["fundus", "cc-by-nc-sa", "gdrive", "classification", "segmentation"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# REFUGE Multi-Rater — Glaucoma with Multi-Expert Annotations

1200 fundus images from REFUGE1 with optic disc/cup segmentation masks annotated by multiple expert raters.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `refuge1_multirater` |
| **Full name** | REFUGE Multi-Rater — Glaucoma with Multi-Expert Annotations |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | classification, segmentation |
| **Samples** | 1,200 |
| **Classes** | 2 (non-glaucoma, glaucoma) |
| **Splits** | train, val, test |
| **Size** | 0.8 GB |
| **Source-stated terms** | CC BY-NC-SA (see HuggingFace page) |
| **Normalized terms** | `cc-by-nc-sa` |
| **Descriptive screening label** | Explicit noncommercial clause recorded; check source |
| **Terms scope** | `dataset_files` |
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
eyehub download refuge1_multirater --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download refuge1_multirater --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('refuge1_multirater')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [drive.google.com/file](https://drive.google.com/file/d/1TXTrZyaZ76faXek46pEzaYQmAejLf30d/view)

**Source-term evidence:** [drive.google.com/file](https://drive.google.com/file/d/1TXTrZyaZ76faXek46pEzaYQmAejLf30d/view)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('refuge1_multirater')
samples = ds.load(data_dir, split='test')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{refuge1_multirater,
  title  = { REFUGE Multi-Rater — Glaucoma with Multi-Expert Annotations },
  note   = { Orlando J.I. et al., 'REFUGE Challenge: A Unified Framework for Evaluating Automated Methods for Glaucoma Assessment from Fundus Photographs', MIA 2020 },
  year   = { 2020 },
  url    = { https://drive.google.com/file/d/1TXTrZyaZ76faXek46pEzaYQmAejLf30d/view },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Orlando J.I. et al., 'REFUGE Challenge: A Unified Framework for Evaluating Automated Methods for Glaucoma Assessment from Fundus Photographs', MIA 2020.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC BY-NC-SA (see HuggingFace page)
- **Normalized category:** `cc-by-nc-sa`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Explicit noncommercial clause recorded; check source

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
