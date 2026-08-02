---
id: dryad_bbs1_retinal_degeneration
title: "BBS1 Retinal Degeneration Mouse Dataset"
sidebar_label: dryad_bbs1_retinal_degeneration
description: "BBS1 mouse data include retinal-degeneration and OCT phenotypes, making it a direct disease-mechanism resource."
tags: ["oct", "tabular", "cc0", "dryad", "regression"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# BBS1 Retinal Degeneration Mouse Dataset

BBS1 mouse data include retinal-degeneration and OCT phenotypes, making it a direct disease-mechanism resource.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_bbs1_retinal_degeneration` |
| **Full name** | BBS1 Retinal Degeneration Mouse Dataset |
| **Primary category** | `oct` |
| **Contained modalities** | oct, tabular |
| **Tasks** | regression |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.000149028 GB |
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

> Scope screen: adjacent_add. Current Dryad v6 file listing: 1 files, 58847 bytes.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_bbs1_retinal_degeneration --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dryad_bbs1_retinal_degeneration --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_bbs1_retinal_degeneration')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.2rbnzs7jm](https://doi.org/10.5061/dryad.2rbnzs7jm)

**Source-term evidence:** [https://doi.org/10.5061/dryad.2rbnzs7jm](https://doi.org/10.5061/dryad.2rbnzs7jm)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_bbs1_retinal_degeneration,
  title  = { BBS1 Retinal Degeneration Mouse Dataset },
  note   = { Cring, Matthew. Ectopic expression of BBS1 rescues male infertility, but not retinal degeneration, in a BBS1 mouse model. Dryad. 2020. doi:10.5061/dryad.2rbnzs7jm },
  year   = { 2020 },
  url    = { https://doi.org/10.5061/dryad.2rbnzs7jm },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Cring, Matthew. Ectopic expression of BBS1 rescues male infertility, but not retinal degeneration, in a BBS1 mouse model. Dryad. 2020. doi:10.5061/dryad.2rbnzs7jm
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

- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [olives](./olives.md): OLIVES: Ophthalmic Labels for Investigating Visual Eye Semantics (9,408 b scans, `cc-by`)
- [dryad_namd_oct_quant](./dryad_namd_oct_quant.md): Moorfields nAMD Quantitative OCT Biomarker Dataset (2,966 volumes, `cc0`)
- [dryad_namd_oct_longitudinal](./dryad_namd_oct_longitudinal.md): Quantifying changes on optical coherence tomography in eyes receiving treatment for neovascular age-related macular degeneration (2,115 eyes, `cc0`)
- [grape](./grape.md): GRAPE: Glaucoma Real-world Appraisal Progression Ensemble (1,115 examinations, `cc0`)
- [harvard_gdp](./harvard_gdp.md): Harvard GDP: Glaucoma Detection and Progression Dataset (1,000 participants, `cc-by-nc-nd`)
- [dryad_namd_visual_prediction](./dryad_namd_visual_prediction.md): Moorfields nAMD Visual-Change Prediction Dataset (926 eyes, `cc0`)
- [dryad_pvd_diagnostic_oct](./dryad_pvd_diagnostic_oct.md): Accuracy of biomicroscopy, ultrasonography and spectral-domain OCT in detection of complete posterior vitreous detachment (123 eyes, `cc0`)
