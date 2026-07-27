---
id: roc
title: "ROC: Retinopathy Online Challenge"
sidebar_label: roc
description: "100 fundus images with microaneurysm annotations from the Retinopathy Online Challenge."
tags: ["fundus", "research-only", "manual", "segmentation", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# ROC: Retinopathy Online Challenge

100 fundus images with microaneurysm annotations from the Retinopathy Online Challenge.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `roc` |
| **Full name** | ROC: Retinopathy Online Challenge |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | segmentation, classification |
| **Samples** | 100 |
| **Classes** | 2 (Not reported) |
| **Splits** | train, test |
| **Size** | 0.3 GB |
| **Source-stated terms** | Research only (free for research, University of Iowa) |
| **Normalized terms** | `research-only` |
| **Descriptive screening label** | Research or challenge restriction recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `guided_instructions_only` |
| **Legacy sample-loader status** | Metadata and access only |


## Notes

> University of Iowa registration form required — no auto path.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download roc --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download roc --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('roc')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [webeye.ophth.uiowa.edu/ROC](http://webeye.ophth.uiowa.edu/ROC/)

**Source-term evidence:** [webeye.ophth.uiowa.edu/ROC](http://webeye.ophth.uiowa.edu/ROC/)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{roc,
  title  = { ROC: Retinopathy Online Challenge },
  note   = { Niemeijer et al., 'Retinopathy Online Challenge: Automatic Detection of Microaneurysms in Digital Color Fundus Photographs', IEEE TMI 2010 },
  year   = { 2010 },
  url    = { http://webeye.ophth.uiowa.edu/ROC/ },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Niemeijer et al., 'Retinopathy Online Challenge: Automatic Detection of Microaneurysms in Digital Color Fundus Photographs', IEEE TMI 2010.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Research only (free for research, University of Iowa)
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
