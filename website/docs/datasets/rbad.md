---
id: rbad
title: "RBAD Retinal Branching-Angle Detection Benchmark"
sidebar_label: rbad
description: "Fundus-image benchmark with retinal vessel branching-angle annotations for evaluating branching-angle detection and measurement algorithms."
tags: ["fundus", "research-only", "github", "landmark_detection", "measurement", "resource-role-current-dataset", "dataset-family-rbad"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# RBAD Retinal Branching-Angle Detection Benchmark

Fundus-image benchmark with retinal vessel branching-angle annotations for evaluating branching-angle detection and measurement algorithms.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `rbad` |
| **Full name** | RBAD Retinal Branching-Angle Detection Benchmark |
| **First published** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Primary category** | `fundus` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `rbad` |
| **Contained modalities** | fundus |
| **Tasks** | landmark_detection, measurement |
| **Primary reported quantity** | 40 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | ASU non-commercial research license |
| **Normalized terms** | `research-only` |
| **Descriptive screening label** | Research or challenge restriction recorded; check source |
| **Terms scope** | `unknown` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | GitHub |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `end_to_end_tested` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 40 | `images` | Branching-angle benchmark images | `official_source_description` | [github.com/Retinal-Research](https://github.com/Retinal-Research/RBAD) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Repository provides 40 benchmark images and annotations under an academic non-commercial license from Arizona Board of Regents; verify terms before redistribution or commercial use.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download rbad --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download rbad --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('rbad')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [github.com/Retinal-Research](https://github.com/Retinal-Research/RBAD)

**Source-term evidence:** [github.com/Retinal-Research](https://github.com/Retinal-Research/RBAD)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{rbad,
  title  = { RBAD Retinal Branching-Angle Detection Benchmark },
  note   = { Yu F, Yu S, Ma S, Williams MA, Yu H. RBAD: A Dataset and Benchmark for Retinal Vessels Branching Angle Detection. IEEE BHI. 2024. doi:10.1109/BHI62660.2024.10913865 },
  year   = { 2024 },
  url    = { https://github.com/Retinal-Research/RBAD },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Yu F, Yu S, Ma S, Williams MA, Yu H. RBAD: A Dataset and Benchmark for Retinal Vessels Branching Angle Detection. IEEE BHI. 2024. doi:10.1109/BHI62660.2024.10913865
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** ASU non-commercial research license
- **Normalized category:** `research-only`
- **Apparent scope:** `unknown`
- **Descriptive screening label:** Research or challenge restriction recorded; check source

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [airogs](./airogs.md): AIROGS: AI for Robust Glaucoma Screening (113,893 images, `cc-by-nc-nd`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (103,959 images, `mit`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [justraigs](./justraigs.md): JustRAIGS: Just Referral AI Glaucoma Screening Dataset (101,442 images, `cc-by-nc-nd`)
- [eyepacs](./eyepacs.md): EyePACS — Diabetic Retinopathy Detection (Kaggle 2015) (88,702 images, `research-only`)
- [angioreport](./angioreport.md): AngioReport Fundus Angiography Report Dataset (55,361 images, `unknown`)
- [ffa_ir](./ffa_ir.md): FFA-IR Medical Report Dataset (47,247 images, `unknown`)
- [mfiddr](./mfiddr.md): MFIDDR: Multi-Field Imaging Dataset for Diabetic Retinopathy (34,452 images, `mit`)
