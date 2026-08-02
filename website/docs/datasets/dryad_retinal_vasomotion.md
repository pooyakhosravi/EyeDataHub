---
id: dryad_retinal_vasomotion
title: "Retinal Laser Speckle Vasomotion Dataset"
sidebar_label: dryad_retinal_vasomotion
description: "Rat retinal laser-speckle measurements are a defined ocular vascular-imaging method resource."
tags: ["fundus", "cc0", "dryad", "vessel_analysis", "measurement"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Retinal Laser Speckle Vasomotion Dataset

Rat retinal laser-speckle measurements are a defined ocular vascular-imaging method resource.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_retinal_vasomotion` |
| **Full name** | Retinal Laser Speckle Vasomotion Dataset |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | vessel_analysis, measurement |
| **Primary reported quantity** | 8 experimental eyes |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 1.111212092 GB |
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

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 8 | `experimental_eyes` | Eight experiments, each recording one rat retina, described in official usage notes Source-stated quantity; Dryad file count is separate metadata and is not a scientific sample count. | `official_source_description` | [https://doi.org/10.5061/dryad.163mp](https://doi.org/10.5061/dryad.163mp) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Scope screen: adjacent_add. Current Dryad v1 file listing: 1 files, 1111189442 bytes.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_retinal_vasomotion --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dryad_retinal_vasomotion --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_retinal_vasomotion')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.163mp](https://doi.org/10.5061/dryad.163mp)

**Source-term evidence:** [https://doi.org/10.5061/dryad.163mp](https://doi.org/10.5061/dryad.163mp)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_retinal_vasomotion,
  title  = { Retinal Laser Speckle Vasomotion Dataset },
  note   = { Neganova, Anastasiia Y., Postnov, Dmitry D., Sosnovtseva, Olga, and Jacobsen, Jens Christian Brings. Data from: Rat retinal vasomotion assessed by laser speckle imaging. Dryad. 2018. doi:10.5061/dryad.163mp },
  year   = { 2018 },
  url    = { https://doi.org/10.5061/dryad.163mp },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Neganova, Anastasiia Y., Postnov, Dmitry D., Sosnovtseva, Olga, and Jacobsen, Jens Christian Brings. Data from: Rat retinal vasomotion assessed by laser speckle imaging. Dryad. 2018. doi:10.5061/dryad.163mp
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

- [airogs](./airogs.md): AIROGS: AI for Robust Glaucoma Screening (113,893 images, `cc-by-nc-nd`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (103,959 images, `mit`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [justraigs](./justraigs.md): JustRAIGS: Just Referral AI Glaucoma Screening Dataset (101,442 images, `cc-by-nc-nd`)
- [eyepacs](./eyepacs.md): EyePACS — Diabetic Retinopathy Detection (Kaggle 2015) (88,702 images, `research-only`)
- [angioreport](./angioreport.md): AngioReport Fundus Angiography Report Dataset (55,361 images, `unknown`)
- [ffa_ir](./ffa_ir.md): FFA-IR Medical Report Dataset (47,247 images, `unknown`)
- [bidr](./bidr.md): BiDR: Diabetic Retinopathy Diagnosis Dataset (35,126 images, `unknown`)
