---
id: dryad_pvd_diagnostic_oct
title: "Accuracy of biomicroscopy, ultrasonography and spectral-domain OCT in detection of complete posterior vitreous detachment"
sidebar_label: dryad_pvd_diagnostic_oct
description: "The 123-eye diagnostic workbook directly evaluates clinical OCT ultrasonography and biomicroscopy for vitreous detachment."
tags: ["oct", "tabular", "cc0", "dryad", "evaluation", "resource-role-current-dataset", "dataset-family-dryad-pvd-diagnostic-oct"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Accuracy of biomicroscopy, ultrasonography and spectral-domain OCT in detection of complete posterior vitreous detachment

The 123-eye diagnostic workbook directly evaluates clinical OCT ultrasonography and biomicroscopy for vitreous detachment.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_pvd_diagnostic_oct` |
| **Full name** | Accuracy of biomicroscopy, ultrasonography and spectral-domain OCT in detection of complete posterior vitreous detachment |
| **Publication date** | 2023-06-26 |
| **Date basis** | Initial dataset release |
| **Publication date precision** | day |
| **Publication date evidence** | [https://doi.org/10.5061/dryad.h44j0zpnp](https://doi.org/10.5061/dryad.h44j0zpnp) |
| **Publication date source field** | Published |
| **Publication date reviewed** | 2026-09-11 |
| **Date notes** | - |
| **Primary category** | `oct` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `dryad_pvd_diagnostic_oct` |
| **Contained modalities** | oct, tabular |
| **Tasks** | evaluation |
| **Primary reported quantity** | 123 eyes |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.000410897 GB |
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
| Primary | 123 | `eyes` | Source-stated primary resource quantity. Current official Dryad metadata. | `official_source_description` | [https://doi.org/10.5061/dryad.h44j0zpnp](https://doi.org/10.5061/dryad.h44j0zpnp) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Scope: core_add. Named file-level object: PVD diagnostic workbook plus README. Official Dryad API metadata and current file listing reviewed 2026-08-01.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_pvd_diagnostic_oct --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dryad_pvd_diagnostic_oct --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_pvd_diagnostic_oct')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.h44j0zpnp](https://doi.org/10.5061/dryad.h44j0zpnp)

**Source-term evidence:** [https://doi.org/10.5061/dryad.h44j0zpnp](https://doi.org/10.5061/dryad.h44j0zpnp)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_pvd_diagnostic_oct,
  title  = { Accuracy of biomicroscopy, ultrasonography and spectral-domain OCT in detection of complete posterior vitreous detachment },
  note   = { Accuracy of biomicroscopy, ultrasonography and spectral-domain OCT in detection of complete posterior vitreous detachment. Dryad Dataset. doi:10.5061/dryad.h44j0zpnp },
  url    = { https://doi.org/10.5061/dryad.h44j0zpnp },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Accuracy of biomicroscopy, ultrasonography and spectral-domain OCT in detection of complete posterior vitreous detachment. Dryad Dataset. doi:10.5061/dryad.h44j0zpnp.
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
- [dryad_bariatric_ophthalmology](./dryad_bariatric_ophthalmology.md): Bariatric Surgery Ophthalmic Evaluation Dataset (57 participants, `cc0`)
