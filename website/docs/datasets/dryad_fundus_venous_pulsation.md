---
id: dryad_fundus_venous_pulsation
title: "Fundus Venous Pulsation Sequence Dataset"
sidebar_label: dryad_fundus_venous_pulsation
description: "Twelve human fundus-image sequences are a direct ocular imaging resource for venous-pulsation measurement."
tags: ["fundus", "infrared", "cc0", "dryad", "vessel_analysis", "measurement", "resource-role-current-dataset", "dataset-family-dryad-fundus-venous-pulsation"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Fundus Venous Pulsation Sequence Dataset

Twelve human fundus-image sequences are a direct ocular imaging resource for venous-pulsation measurement.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_fundus_venous_pulsation` |
| **Full name** | Fundus Venous Pulsation Sequence Dataset |
| **Publication date** | 2016-07-08 |
| **Date basis** | Initial dataset release |
| **Publication date precision** | day |
| **Publication date evidence** | [https://doi.org/10.5061/dryad.56f1h](https://doi.org/10.5061/dryad.56f1h) |
| **Publication date source field** | Published |
| **Publication date reviewed** | 2026-09-11 |
| **Date notes** | - |
| **Primary category** | `fundus` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `dryad_fundus_venous_pulsation` |
| **Contained modalities** | fundus, infrared |
| **Tasks** | vessel_analysis, measurement |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.118605201 GB |
| **Source-stated terms** | https://spdx.org/licenses/CC0-1.0.html |
| **Normalized terms** | `cc0` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Dryad |
| **Availability** | `available` (checked 2026-08-01) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

No reproducible primary item count was exposed for the cataloged source version.

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Scope screen: core_add. Current Dryad v1 file listing: 2 files, 118583295 bytes.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_fundus_venous_pulsation --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dryad_fundus_venous_pulsation --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_fundus_venous_pulsation')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.56f1h](https://doi.org/10.5061/dryad.56f1h)

**Source-term evidence:** [https://doi.org/10.5061/dryad.56f1h](https://doi.org/10.5061/dryad.56f1h)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_fundus_venous_pulsation,
  title  = { Fundus Venous Pulsation Sequence Dataset },
  note   = { Moret, Fabrice, Reiff, Charlotte M., Lagrèze, Wolf A., and Bach, Michael. Data from: Quantitative analysis of fundus-image sequences reveals phase of spontaneous venous pulsations. Dryad. 2016. doi:10.5061/dryad.56f1h },
  year   = { 2016 },
  url    = { https://doi.org/10.5061/dryad.56f1h },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Moret, Fabrice, Reiff, Charlotte M., Lagrèze, Wolf A., and Bach, Michael. Data from: Quantitative analysis of fundus-image sequences reveals phase of spontaneous venous pulsations. Dryad. 2016. doi:10.5061/dryad.56f1h
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** https://spdx.org/licenses/CC0-1.0.html
- **Normalized category:** `cc0`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Standard label without an explicit NC clause; not a permission finding

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [jrc_multimodal_vessels](./jrc_multimodal_vessels.md): JRC Multi-Modal Retinal Vessel Segmentation (120 images, `unknown`)
- [airogs](./airogs.md): AIROGS: AI for Robust Glaucoma Screening (113,893 images, `cc-by-nc-nd`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (103,959 images, `mit`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [justraigs](./justraigs.md): JustRAIGS: Just Referral AI Glaucoma Screening Dataset (101,442 images, `cc-by-nc-nd`)
- [eyepacs](./eyepacs.md): EyePACS — Diabetic Retinopathy Detection (Kaggle 2015) (88,702 images, `research-only`)
- [angioreport](./angioreport.md): AngioReport Fundus Angiography Report Dataset (55,361 images, `unknown`)
- [ffa_ir](./ffa_ir.md): FFA-IR Medical Report Dataset (47,247 images, `unknown`)
