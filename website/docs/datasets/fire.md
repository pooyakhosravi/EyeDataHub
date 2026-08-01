---
id: fire
title: "FIRE: Fundus Image Registration Dataset"
sidebar_label: fire
description: "129 fundus images from 39 patients forming 134 registration pairs with anatomical ground-truth control points. Only public registration benchmark for ophthalmology."
tags: ["fundus", "research-only", "direct", "regression"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# FIRE: Fundus Image Registration Dataset

129 fundus images from 39 patients forming 134 registration pairs with anatomical ground-truth control points. Only public registration benchmark for ophthalmology.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `fire` |
| **Full name** | FIRE: Fundus Image Registration Dataset |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | regression |
| **Samples** | 129 |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 1.0 GB |
| **Source-stated terms** | Research only (FORTH CVRL) |
| **Normalized terms** | `research-only` |
| **Descriptive screening label** | Research or challenge restriction recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Direct HTTP |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `end_to_end_tested` |
| **Legacy sample-loader status** | Metadata and access only |


## Notes

> Distributed as a 7z archive. EyeDataHub validates archive member paths before extracting it.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download fire --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download fire --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('fire')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [projects.ics.forth.gr/cvrl](https://projects.ics.forth.gr/cvrl/fire/)

**Source-term evidence:** [projects.ics.forth.gr/cvrl](https://projects.ics.forth.gr/cvrl/fire/)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{fire,
  title  = { FIRE: Fundus Image Registration Dataset },
  note   = { Hernandez-Matas et al., 'FIRE: Fundus Image Registration Dataset', Journal of Modeling in Ophthalmology 2017 },
  year   = { 2017 },
  url    = { https://projects.ics.forth.gr/cvrl/fire/ },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Hernandez-Matas et al., 'FIRE: Fundus Image Registration Dataset', Journal of Modeling in Ophthalmology 2017.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Research only (FORTH CVRL)
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
