---
id: drive
title: "DRIVE: Digital Retinal Images for Vessel Extraction"
sidebar_label: drive
description: "Forty color fundus photographs from a diabetic retinopathy screening program, divided into 20 training and 20 test images, with vessel reference annotations and field of view masks."
tags: ["fundus", "unknown", "manual", "segmentation", "documented-relationship", "relationship-derived_from"]
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
| **Primary reported quantity** | 40 images |
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


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 40 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [drive.grand-challenge.org/DRIVE](https://drive.grand-challenge.org/DRIVE/) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> The official page reports 768 by 584 pixel images, one manual vessel segmentation for each training image, and hidden test references used by the evaluation server. Verify reuse terms with the source before redistribution.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- [dryad_sf7m0cggh](./dryad_sf7m0cggh.md) is `derived from` this record: The official current file listing names DRIVE trace annotations and result files. ([evidence](https://datadryad.org/api/v2/versions/353579/files))
- [retinal_vessel_robustness](./retinal_vessel_robustness.md) is `derived from` this record: The robustness benchmark contains augmented versions of DRIVE, STARE, and CHASE_DB1 images. ([evidence](https://zenodo.org/records/12659652))
- [rite](./rite.md) is `derived from` this record: RITE adds artery, vein, and vessel-tree labels to the same 40 DRIVE images. ([evidence](https://medicine.uiowa.edu/eye/rite-dataset))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download drive --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download drive --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('drive')
print(preflight_dataset(ds, './data'))  # no download
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

## Similar resources by shared modality

- [airogs](./airogs.md): AIROGS: AI for Robust Glaucoma Screening (113,893 images, `cc-by-nc-nd`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (103,959 images, `mit`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [justraigs](./justraigs.md): JustRAIGS: Just Referral AI Glaucoma Screening Dataset (101,442 images, `cc-by-nc-nd`)
- [eyepacs](./eyepacs.md): EyePACS — Diabetic Retinopathy Detection (Kaggle 2015) (88,702 images, `research-only`)
- [angioreport](./angioreport.md): AngioReport Fundus Angiography Report Dataset (55,361 images, `unknown`)
- [ffa_ir](./ffa_ir.md): FFA-IR Medical Report Dataset (47,247 images, `unknown`)
- [bidr](./bidr.md): BiDR: Diabetic Retinopathy Diagnosis Dataset (35,126 images, `unknown`)
