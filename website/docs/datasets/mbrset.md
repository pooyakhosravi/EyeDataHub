---
id: mbrset
title: "mBRSET: Mobile Brazilian Retinal Dataset"
sidebar_label: mbrset
description: "5,164 fundus images from 1,291 patients captured with the Phelcom Eyer handheld smartphone-based fundus camera. Labels for DR grading + clinical/demographic prediction."
tags: ["fundus", "research-only", "physionet", "grading", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# mBRSET: Mobile Brazilian Retinal Dataset

5,164 fundus images from 1,291 patients captured with the Phelcom Eyer handheld smartphone-based fundus camera. Labels for DR grading + clinical/demographic prediction.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mbrset` |
| **Full name** | mBRSET: Mobile Brazilian Retinal Dataset |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | grading, classification |
| **Samples** | 5,164 |
| **Classes** | 5 (0_no_dr, 1_mild, 2_moderate, 3_severe, 4_proliferative) |
| **Splits** | all |
| **Size** | 3.0 GB |
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

> Same PhysioNet credentialed flow as BRSET. Modality EyeDataHub otherwise lacks (portable smartphone-based fundus).

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# This route requires upstream human action; no transfer starts.
eyehub download mbrset --data-dir ./data --dry-run --json
# Follow the official instructions shown by preflight.
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mbrset')
print(preflight_dataset(ds, './data'))  # returns manual_access_blocked
```

  </TabItem>
</Tabs>

**Upstream page:** [physionet.org/content](https://physionet.org/content/mbrset/1.0/)

**Source-term evidence:** [physionet.org/content](https://physionet.org/content/mbrset/1.0/)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mbrset,
  title  = { mBRSET: Mobile Brazilian Retinal Dataset },
  note   = { Wu C, Restrepo D, Nakayama LF, et al., 'A portable retina fundus photos dataset for clinical, demographic, and diabetic retinopathy prediction', Scientific Data 12:323, 2025. doi:10.1038/s41597-025-04627-3 },
  year   = { 2025 },
  url    = { https://physionet.org/content/mbrset/1.0/ },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Wu C, Restrepo D, Nakayama LF, et al., 'A portable retina fundus photos dataset for clinical, demographic, and diabetic retinopathy prediction', Scientific Data 12:323, 2025. doi:10.1038/s41597-025-04627-3
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
