---
id: jrc_multimodal_vessels
title: "JRC Multi-Modal Retinal Vessel Segmentation"
sidebar_label: jrc_multimodal_vessels
description: "Multi-modal retinal vessel segmentation dataset spanning fluorescence angiography, fundus autofluorescence, and infrared imaging."
tags: ["multimodal", "fundus", "fundus_angiography", "fundus_autofluorescence", "infrared", "unknown", "manual", "segmentation"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# JRC Multi-Modal Retinal Vessel Segmentation

Multi-modal retinal vessel segmentation dataset spanning fluorescence angiography, fundus autofluorescence, and infrared imaging.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `jrc_multimodal_vessels` |
| **Full name** | JRC Multi-Modal Retinal Vessel Segmentation |
| **Primary category** | `multimodal` |
| **Contained modalities** | fundus, fundus_angiography, fundus_autofluorescence, infrared |
| **Tasks** | segmentation |
| **Samples** | 120 |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | Academic request / Unknown |
| **Normalized terms** | `unknown` |
| **Descriptive screening label** | Unknown or unclear; do not assume permission |
| **Terms scope** | `unknown` |
| **Access friction** | `controlled_or_manual` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `manual_access_blocked` |
| **Legacy sample-loader status** | Metadata and access only |


## Notes

> Source page indicates access by academic request; not an open direct download.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# This route requires upstream human action; no transfer starts.
eyehub download jrc_multimodal_vessels --data-dir ./data --dry-run --json
# Follow the official instructions shown by preflight.
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('jrc_multimodal_vessels')
print(preflight_dataset(ds, './data'))  # returns manual_access_blocked
```

  </TabItem>
</Tabs>

**Upstream page:** [zenodo.org/records](https://zenodo.org/records/17874693)

**Source-term evidence:** [zenodo.org/records](https://zenodo.org/records/17874693)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{jrc_multimodal_vessels,
  title  = { JRC Multi-Modal Retinal Vessel Segmentation },
  note   = { JRC-Multi-Modal Retinal Vessel Segmentation. Zenodo, 2026. doi:10.5281/zenodo.17874693 },
  year   = { 2026 },
  url    = { https://zenodo.org/records/17874693 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
JRC-Multi-Modal Retinal Vessel Segmentation. Zenodo, 2026. doi:10.5281/zenodo.17874693
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Academic request / Unknown
- **Normalized category:** `unknown`
- **Apparent scope:** `unknown`
- **Descriptive screening label:** Unknown or unclear; do not assume permission

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Related datasets with shared modalities

- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 records, `unknown`)
- [angioreport](./angioreport.md): AngioReport Fundus Angiography Report Dataset (55,361 records, `unknown`)
- [ffa_ir](./ffa_ir.md): FFA-IR Medical Report Dataset (47,247 records, `unknown`)
- [x_pcr](./x_pcr.md): X-PCR Ophthalmology Progressive Clinical Reasoning Benchmark (18,700 records, `unknown`)
- [mm_retinal_reason](./mm_retinal_reason.md): MM-Retinal-Reason: Ophthalmology Multimodal Reasoning Dataset (count not reported records, `unknown`)
- [ophthalvqa](./ophthalvqa.md): OphthalVQA Dataset (count not reported records, `cc-by`)
- [airogs](./airogs.md): AIROGS: AI for Robust Glaucoma Screening (113,893 records, `cc-by-nc-nd`)
- [justraigs](./justraigs.md): JustRAIGS: Just Referral AI Glaucoma Screening Dataset (101,442 records, `cc-by-nc-nd`)
