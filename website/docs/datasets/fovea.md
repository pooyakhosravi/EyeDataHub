---
id: fovea
title: "FOVEA: Pre/Intra-Operative Fundus + Biomicroscopy"
sidebar_label: fovea
description: "40 patients with paired pre-operative fundus images and intra-operative biomicroscopy video clips. Annotated for optic disc and vessel segmentation across domains."
tags: ["multimodal", "fundus", "surgical_video", "cc-by", "figshare", "segmentation", "resource-role-current-dataset", "dataset-family-fovea"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# FOVEA: Pre/Intra-Operative Fundus + Biomicroscopy

40 patients with paired pre-operative fundus images and intra-operative biomicroscopy video clips. Annotated for optic disc and vessel segmentation across domains.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `fovea` |
| **Full name** | FOVEA: Pre/Intra-Operative Fundus + Biomicroscopy |
| **First published** | 2025-04-27 |
| **Publication date precision** | day |
| **Publication date evidence** | [api.figshare.com/v2](https://api.figshare.com/v2/articles/28329338/versions/1) |
| **Publication date source field** | published_date (Figshare version 1) |
| **Publication date reviewed** | 2026-09-11 |
| **Primary category** | `multimodal` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `fovea` |
| **Contained modalities** | fundus, surgical_video |
| **Tasks** | segmentation |
| **Primary reported quantity** | 40 participants |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 4.0 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Figshare |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 40 | `participants` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [https://doi.org/10.6084/m9.figshare.28329338](https://doi.org/10.6084/m9.figshare.28329338) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Unique pre-op/intra-op paired modality — only public example.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download fovea --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download fovea --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('fovea')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.6084/m9.figshare.28329338](https://doi.org/10.6084/m9.figshare.28329338)

**Source-term evidence:** [https://doi.org/10.6084/m9.figshare.28329338](https://doi.org/10.6084/m9.figshare.28329338)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{fovea,
  title  = { FOVEA: Pre/Intra-Operative Fundus + Biomicroscopy },
  note   = { Ravasio et al., 'FOVEA: paired pre- and intra-operative fundus + biomicroscopy', Scientific Data 2025. doi:10.1038/s41597-025-04965-2 },
  year   = { 2025 },
  url    = { https://doi.org/10.6084/m9.figshare.28329338 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Ravasio et al., 'FOVEA: paired pre- and intra-operative fundus + biomicroscopy', Scientific Data 2025. doi:10.1038/s41597-025-04965-2
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC BY 4.0
- **Normalized category:** `cc-by`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Standard label without an explicit NC clause; not a permission finding

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [ophora](./ophora.md): Ophora-160K: Ophthalmic Surgical Video Instruction Dataset (162,185 video clip instruction pairs, `unknown`)
- [airogs](./airogs.md): AIROGS: AI for Robust Glaucoma Screening (113,893 images, `cc-by-nc-nd`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (103,959 images, `mit`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [justraigs](./justraigs.md): JustRAIGS: Just Referral AI Glaucoma Screening Dataset (101,442 images, `cc-by-nc-nd`)
- [eyepacs](./eyepacs.md): EyePACS — Diabetic Retinopathy Detection (Kaggle 2015) (88,702 images, `research-only`)
- [angioreport](./angioreport.md): AngioReport Fundus Angiography Report Dataset (55,361 images, `unknown`)
