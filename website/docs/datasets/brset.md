---
id: brset
title: "BRSET: Brazilian Multilabel Ophthalmological Dataset"
sidebar_label: brset
description: "16,266 color fundus images from 8,524 Brazilian patients with 14 disease labels (DR, AMD, glaucoma, drusen, others), image quality flags, and demographic attributes."
tags: ["fundus", "research-only", "physionet", "multilabel", "classification", "quality"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# BRSET: Brazilian Multilabel Ophthalmological Dataset

16,266 color fundus images from 8,524 Brazilian patients with 14 disease labels (DR, AMD, glaucoma, drusen, others), image quality flags, and demographic attributes.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `brset` |
| **Full name** | BRSET: Brazilian Multilabel Ophthalmological Dataset |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | multilabel, classification, quality |
| **Samples** | 16,266 |
| **Classes** | 14 (Not reported) |
| **Splits** | all |
| **Size** | 9.0 GB |
| **Source-stated terms** | PhysioNet Credentialed Health Data License 1.5.0 (Research only) |
| **Normalized terms** | `research-only` |
| **Descriptive screening label** | Research or challenge restriction recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `controlled_or_manual` |
| **Route backend** | PhysioNet |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `manual_access_blocked` |
| **Legacy sample-loader status** | Metadata and access only |


## Notes

> Requires PhysioNet credentialed-user account + CITI training + signed Data Use Agreement. Set PHYSIONET_USERNAME and PHYSIONET_PASSWORD in .env to auto-download.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# This route requires upstream human action; no transfer starts.
eyehub download brset --data-dir ./data --dry-run --json
# Follow the official instructions shown by preflight.
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('brset')
print(preflight_dataset(ds, './data'))  # returns manual_access_blocked
```

  </TabItem>
</Tabs>

**Upstream page:** [physionet.org/content](https://physionet.org/content/brazilian-ophthalmological/1.0.1/)

**Source-term evidence:** [physionet.org/content](https://physionet.org/content/brazilian-ophthalmological/1.0.1/)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{brset,
  title  = { BRSET: Brazilian Multilabel Ophthalmological Dataset },
  note   = { Nakayama LF, Restrepo D, Matos J, et al., 'BRSET: A Brazilian Multilabel Ophthalmological Dataset of Retina Fundus Photos', PLOS Digital Health 3(7):e0000454, 2024. doi:10.1371/journal.pdig.0000454 · PhysioNet DOI: 10.13026/1pht-2b69 },
  year   = { 2024 },
  url    = { https://physionet.org/content/brazilian-ophthalmological/1.0.1/ },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Nakayama LF, Restrepo D, Matos J, et al., 'BRSET: A Brazilian Multilabel Ophthalmological Dataset of Retina Fundus Photos', PLOS Digital Health 3(7):e0000454, 2024. doi:10.1371/journal.pdig.0000454 · PhysioNet DOI: 10.13026/1pht-2b69
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** PhysioNet Credentialed Health Data License 1.5.0 (Research only)
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
