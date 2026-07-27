---
id: drive
title: "DRIVE: Digital Retinal Images for Vessel Extraction"
sidebar_label: drive
description: "Forty color fundus photographs from a diabetic retinopathy screening program, divided into 20 training and 20 test images, with vessel reference annotations and field of view masks."
tags: ["fundus", "unknown", "manual", "segmentation"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# DRIVE: Digital Retinal Images for Vessel Extraction

Forty color fundus photographs from a diabetic retinopathy screening program, divided into 20 training and 20 test images, with vessel reference annotations and field of view masks.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `drive` |
| **Full name** | DRIVE: Digital Retinal Images for Vessel Extraction |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | segmentation |
| **Samples** | 40 |
| **Classes** | 2 (background, vessel) |
| **Splits** | train, test |
| **Size** | Not reported |
| **Source-stated terms** | Unknown; no named dataset license on the official page |
| **Normalized terms** | `unknown` |
| **Descriptive screening label** | Unknown or unclear; do not assume permission |
| **Terms scope** | `unknown` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `guided_instructions_only` |
| **Legacy sample-loader status** | Metadata and access only |


## Notes

> The official page reports 768 by 584 pixel images, one manual vessel segmentation for each training image, and hidden test references used by the evaluation server. Verify reuse terms with the source before redistribution.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download drive --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download drive --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('drive')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [drive.grand-challenge.org/DRIVE](https://drive.grand-challenge.org/DRIVE/)

**Source-term evidence:** [drive.grand-challenge.org/DRIVE](https://drive.grand-challenge.org/DRIVE/)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{drive,
  title  = { DRIVE: Digital Retinal Images for Vessel Extraction },
  note   = { Staal J, Abramoff MD, Niemeijer M, Viergever MA, van Ginneken B. Ridge-based vessel segmentation in color images of the retina. IEEE Trans Med Imaging. 2004;23:501-509. doi:10.1109/TMI.2004.825627 },
  year   = { 2004 },
  url    = { https://drive.grand-challenge.org/DRIVE/ },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Staal J, Abramoff MD, Niemeijer M, Viergever MA, van Ginneken B. Ridge-based vessel segmentation in color images of the retina. IEEE Trans Med Imaging. 2004;23:501-509. doi:10.1109/TMI.2004.825627
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Unknown; no named dataset license on the official page
- **Normalized category:** `unknown`
- **Apparent scope:** `unknown`
- **Descriptive screening label:** Unknown or unclear; do not assume permission

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
