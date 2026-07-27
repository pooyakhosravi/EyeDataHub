---
id: lag
title: "LAG: Large-scale Attention-based Glaucoma Database"
sidebar_label: lag
description: "11,760 fundus images with glaucoma classification labels and ophthalmologist-derived attention maps. Largest public glaucoma dataset with attention ground truth."
tags: ["fundus", "research-only", "manual", "classification", "segmentation"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# LAG: Large-scale Attention-based Glaucoma Database

11,760 fundus images with glaucoma classification labels and ophthalmologist-derived attention maps. Largest public glaucoma dataset with attention ground truth.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `lag` |
| **Full name** | LAG: Large-scale Attention-based Glaucoma Database |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | classification, segmentation |
| **Samples** | 11,760 |
| **Classes** | 2 (normal, glaucoma) |
| **Splits** | train, test |
| **Size** | 3.0 GB |
| **Source-stated terms** | Research only (no redistribution; password by email) |
| **Normalized terms** | `research-only` |
| **Descriptive screening label** | Research or challenge restriction recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `author_contact` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `manual_access_blocked` |
| **Legacy sample-loader status** | Metadata and access only |


## Notes

> Dropbox link gated by password — email liliu1995@buaa.edu.cn to request access. Cannot be auto-downloaded.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# This route requires upstream human action; no transfer starts.
eyehub download lag --data-dir ./data --dry-run --json
# Follow the official instructions shown by preflight.
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('lag')
print(preflight_dataset(ds, './data'))  # returns manual_access_blocked
```

  </TabItem>
</Tabs>

**Upstream page:** [github.com/smilell](https://github.com/smilell/AG-CNN)

**Source-term evidence:** [github.com/smilell](https://github.com/smilell/AG-CNN)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{lag,
  title  = { LAG: Large-scale Attention-based Glaucoma Database },
  note   = { Li et al., 'Attention Based Glaucoma Detection: A Large-scale Database and CNN Model', CVPR 2019 },
  year   = { 2019 },
  url    = { https://github.com/smilell/AG-CNN },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Li et al., 'Attention Based Glaucoma Detection: A Large-scale Database and CNN Model', CVPR 2019.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Research only (no redistribution; password by email)
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
