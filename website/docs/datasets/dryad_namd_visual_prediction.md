---
id: dryad_namd_visual_prediction
title: "Moorfields nAMD Visual-Change Prediction Dataset"
sidebar_label: dryad_namd_visual_prediction
description: "Longitudinal quantitative OCT biomarkers and treatment-response variables for predicting visual acuity in neovascular AMD."
tags: ["tabular", "oct", "cc0", "dryad", "regression", "prognosis"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Moorfields nAMD Visual-Change Prediction Dataset

Longitudinal quantitative OCT biomarkers and treatment-response variables for predicting visual acuity in neovascular AMD.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_namd_visual_prediction` |
| **Full name** | Moorfields nAMD Visual-Change Prediction Dataset |
| **Primary category** | `tabular` |
| **Contained modalities** | tabular, oct |
| **Tasks** | regression, prognosis |
| **Samples** | 926 |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.0016 GB |
| **Source-stated terms** | CC0 1.0 |
| **Normalized terms** | `cc0` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Dryad |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Notes

> Primary analyses used 926 treatment-naive first-treated eyes from a larger Moorfields cohort. This resource overlaps the Moorfields AMD source cohort but exposes a distinct longitudinal prediction task.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_namd_visual_prediction --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download dryad_namd_visual_prediction --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_namd_visual_prediction')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.573n5tb5d](https://doi.org/10.5061/dryad.573n5tb5d)

**Source-term evidence:** [https://doi.org/10.5061/dryad.573n5tb5d](https://doi.org/10.5061/dryad.573n5tb5d)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_namd_visual_prediction,
  title  = { Moorfields nAMD Visual-Change Prediction Dataset },
  note   = { Predicting incremental and future visual change in neovascular age-related macular degeneration using deep learning. Dryad. 2021. doi:10.5061/dryad.573n5tb5d },
  year   = { 2021 },
  url    = { https://doi.org/10.5061/dryad.573n5tb5d },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Predicting incremental and future visual change in neovascular age-related macular degeneration using deep learning. Dryad. 2021. doi:10.5061/dryad.573n5tb5d
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC0 1.0
- **Normalized category:** `cc0`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Standard label without an explicit NC clause; not a permission finding

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Related datasets with shared modalities

- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 records, `unknown`)
- [olives](./olives.md): OLIVES: Ophthalmic Labels for Investigating Visual Eye Semantics (9,408 records, `cc-by`)
- [dryad_namd_oct_quant](./dryad_namd_oct_quant.md): Moorfields nAMD Quantitative OCT Biomarker Dataset (2,966 records, `cc0`)
- [grape](./grape.md): GRAPE: Glaucoma Real-world Appraisal Progression Ensemble (1,115 records, `cc0`)
- [harvard_gdp](./harvard_gdp.md): Harvard GDP: Glaucoma Detection and Progression Dataset (1,000 records, `cc-by-nc-nd`)
- [dryad_subretinal_robot](./dryad_subretinal_robot.md): Head-Mounted Robot Subretinal Injection Dataset (count not reported records, `cc0`)
- [ocular_chat_vqa](./ocular_chat_vqa.md): OcularChat-VQA: AREDS-Derived Patient-Physician Dialogue Dataset (844,000 records, `cc-by-nc-sa`)
- [syn_oct](./syn_oct.md): SYN-OCT Synthetic Glaucoma OCT Dataset (200,000 records, `cc-by`)
