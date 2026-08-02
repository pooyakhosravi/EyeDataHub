---
id: dryad_bariatric_ophthalmology
title: "Bariatric Surgery Ophthalmic Evaluation Dataset"
sidebar_label: dryad_bariatric_ophthalmology
description: "Longitudinal human ophthalmic and OCT measurements in the bariatric cohort are directly reusable clinical data."
tags: ["oct", "tabular", "cc0", "dryad", "regression", "resource-role-current-dataset", "dataset-family-dryad-bariatric-ophthalmology"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Bariatric Surgery Ophthalmic Evaluation Dataset

Longitudinal human ophthalmic and OCT measurements in the bariatric cohort are directly reusable clinical data.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_bariatric_ophthalmology` |
| **Full name** | Bariatric Surgery Ophthalmic Evaluation Dataset |
| **Primary category** | `oct` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `dryad_bariatric_ophthalmology` |
| **Contained modalities** | oct, tabular |
| **Tasks** | regression |
| **Primary reported quantity** | 57 participants |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 5.4325e-05 GB |
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
| Primary | 57 | `participants` | Source-described severely obese ophthalmology cohort Source-stated quantity; Dryad file count is separate metadata and is not a scientific sample count. | `official_source_description` | [https://doi.org/10.5061/dryad.1g6vm34](https://doi.org/10.5061/dryad.1g6vm34) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Scope screen: core_add. Current Dryad v1 file listing: 1 files, 32456 bytes.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_bariatric_ophthalmology --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dryad_bariatric_ophthalmology --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_bariatric_ophthalmology')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.1g6vm34](https://doi.org/10.5061/dryad.1g6vm34)

**Source-term evidence:** [https://doi.org/10.5061/dryad.1g6vm34](https://doi.org/10.5061/dryad.1g6vm34)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_bariatric_ophthalmology,
  title  = { Bariatric Surgery Ophthalmic Evaluation Dataset },
  note   = { Posarelli, Chiara, Salvetti, Guido, Paolo, Piaggi, Guido, Francesca, Ceccarini, Giovanni, Santini, Ferruccio, and Figus, Michele. Data from: Ophthalmologic evaluation of severely obese patients undergoing bariatric surgery: a pilot, monocentric, prospective, open-label study. Dryad. 2019. doi:10.5061/dryad.1g6vm34 },
  year   = { 2019 },
  url    = { https://doi.org/10.5061/dryad.1g6vm34 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Posarelli, Chiara, Salvetti, Guido, Paolo, Piaggi, Guido, Francesca, Ceccarini, Giovanni, Santini, Ferruccio, and Figus, Michele. Data from: Ophthalmologic evaluation of severely obese patients undergoing bariatric surgery: a pilot, monocentric, prospective, open-label study. Dryad. 2019. doi:10.5061/dryad.1g6vm34
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
