---
id: dryad_namd_oct_quant
title: "Moorfields nAMD Quantitative OCT Biomarker Dataset"
sidebar_label: dryad_namd_oct_quant
description: "Anonymized clinical metadata and automated 3D OCT segmentation volumes for neovascular age-related macular degeneration."
tags: ["tabular", "oct", "cc0", "dryad", "regression", "prognosis", "fairness_analysis", "resource-role-current-dataset", "dataset-family-dryad-namd-oct-quant", "documented-relationship", "relationship-same_or_overlapping_cohort_as"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Moorfields nAMD Quantitative OCT Biomarker Dataset

Anonymized clinical metadata and automated 3D OCT segmentation volumes for neovascular age-related macular degeneration.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_namd_oct_quant` |
| **Full name** | Moorfields nAMD Quantitative OCT Biomarker Dataset |
| **First published** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Primary category** | `tabular` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `dryad_namd_oct_quant` |
| **Contained modalities** | tabular, oct |
| **Tasks** | regression, prognosis, fairness_analysis |
| **Primary reported quantity** | 2,966 volumes |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.0032 GB |
| **Source-stated terms** | CC0 1.0 |
| **Normalized terms** | `cc0` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Dryad |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `end_to_end_tested` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 2,966 | `volumes` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [https://doi.org/10.5061/dryad.2rbnzs7m4](https://doi.org/10.5061/dryad.2rbnzs7m4) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Contains derived OCT feature volumes and metadata for 2,473 first-treated and 493 second-treated eyes. Raw OCT scans are not part of this Dryad release.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- This record has a documented `same or overlapping cohort as` relationship with [dryad_moorfields_amd_1_2_year](./dryad_moorfields_amd_1_2_year.md): The official records identify the Moorfields AMD database and overlapping treatment or extraction periods. ([evidence](https://doi.org/10.5061/dryad.2rbnzs7m4))
- This record has a documented `same or overlapping cohort as` relationship with [dryad_moorfields_namd_fellow_eye](./dryad_moorfields_namd_fellow_eye.md): The official records identify the Moorfields AMD database and overlapping treatment or extraction periods. ([evidence](https://doi.org/10.5061/dryad.2rbnzs7m4))
- This record has a documented `same or overlapping cohort as` relationship with [dryad_namd_visual_prediction](./dryad_namd_visual_prediction.md): Both records draw from the Moorfields AMD database; public descriptions do not establish exact containment. ([evidence](https://doi.org/10.5061/dryad.2rbnzs7m4))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_namd_oct_quant --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dryad_namd_oct_quant --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_namd_oct_quant')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.2rbnzs7m4](https://doi.org/10.5061/dryad.2rbnzs7m4)

**Source-term evidence:** [https://doi.org/10.5061/dryad.2rbnzs7m4](https://doi.org/10.5061/dryad.2rbnzs7m4)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_namd_oct_quant,
  title  = { Moorfields nAMD Quantitative OCT Biomarker Dataset },
  note   = { Moraes G, Fu DJ, Wilson M, et al. Quantitative analysis of optical coherence tomography for neovascular age-related macular degeneration using deep learning. Dryad. 2020. doi:10.5061/dryad.2rbnzs7m4 },
  year   = { 2020 },
  url    = { https://doi.org/10.5061/dryad.2rbnzs7m4 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Moraes G, Fu DJ, Wilson M, et al. Quantitative analysis of optical coherence tomography for neovascular age-related macular degeneration using deep learning. Dryad. 2020. doi:10.5061/dryad.2rbnzs7m4
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC0 1.0
- **Normalized category:** `cc0`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Standard label without an explicit NC clause; not a permission finding

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [olives](./olives.md): OLIVES: Ophthalmic Labels for Investigating Visual Eye Semantics (9,408 b scans, `cc-by`)
- [dryad_namd_oct_longitudinal](./dryad_namd_oct_longitudinal.md): Quantifying changes on optical coherence tomography in eyes receiving treatment for neovascular age-related macular degeneration (2,115 eyes, `cc0`)
- [grape](./grape.md): GRAPE: Glaucoma Real-world Appraisal Progression Ensemble (1,115 examinations, `cc0`)
- [harvard_gdp](./harvard_gdp.md): Harvard GDP: Glaucoma Detection and Progression Dataset (1,000 participants, `cc-by-nc-nd`)
- [dryad_namd_visual_prediction](./dryad_namd_visual_prediction.md): Moorfields nAMD Visual-Change Prediction Dataset (926 eyes, `cc0`)
- [dryad_pvd_diagnostic_oct](./dryad_pvd_diagnostic_oct.md): Accuracy of biomicroscopy, ultrasonography and spectral-domain OCT in detection of complete posterior vitreous detachment (123 eyes, `cc0`)
- [dryad_bariatric_ophthalmology](./dryad_bariatric_ophthalmology.md): Bariatric Surgery Ophthalmic Evaluation Dataset (57 participants, `cc0`)
