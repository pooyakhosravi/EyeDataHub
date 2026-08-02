---
id: dryad_mouse_oct_beam_tilt
title: "Quantifying the influence of optical coherence tomography beam tilt in the normal adult mouse retina"
sidebar_label: dryad_mouse_oct_beam_tilt
description: "The large named OCT archive is a directly reusable imaging-method resource despite its normal mouse rather than human cohort."
tags: ["oct", "tabular", "cc0", "dryad", "measurement"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Quantifying the influence of optical coherence tomography beam tilt in the normal adult mouse retina

The large named OCT archive is a directly reusable imaging-method resource despite its normal mouse rather than human cohort.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_mouse_oct_beam_tilt` |
| **Full name** | Quantifying the influence of optical coherence tomography beam tilt in the normal adult mouse retina |
| **Primary category** | `oct` |
| **Contained modalities** | oct, tabular |
| **Tasks** | measurement |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 4.704522143 GB |
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

> Scope: adjacent_add. Named file-level object: beam_tilt_data_for_Dryad.zip plus README. Official Dryad API metadata and current file listing reviewed 2026-08-01.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_mouse_oct_beam_tilt --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dryad_mouse_oct_beam_tilt --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_mouse_oct_beam_tilt')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.95x69p8th](https://doi.org/10.5061/dryad.95x69p8th)

**Source-term evidence:** [https://doi.org/10.5061/dryad.95x69p8th](https://doi.org/10.5061/dryad.95x69p8th)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_mouse_oct_beam_tilt,
  title  = { Quantifying the influence of optical coherence tomography beam tilt in the normal adult mouse retina },
  note   = { Quantifying the influence of optical coherence tomography beam tilt in the normal adult mouse retina. Dryad Dataset. doi:10.5061/dryad.95x69p8th },
  url    = { https://doi.org/10.5061/dryad.95x69p8th },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Quantifying the influence of optical coherence tomography beam tilt in the normal adult mouse retina. Dryad Dataset. doi:10.5061/dryad.95x69p8th.
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
