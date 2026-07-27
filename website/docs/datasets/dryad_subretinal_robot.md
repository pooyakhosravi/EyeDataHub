---
id: dryad_subretinal_robot
title: "Head-Mounted Robot Subretinal Injection Dataset"
sidebar_label: dryad_subretinal_robot
description: "OCT screen recordings, annotated frames, and pressure data from robot-assisted subretinal injections in ex vivo porcine eyes."
tags: ["multimodal", "surgical_video", "oct", "tabular", "cc0", "dryad", "segmentation", "surgical_workflow", "regression"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Head-Mounted Robot Subretinal Injection Dataset

OCT screen recordings, annotated frames, and pressure data from robot-assisted subretinal injections in ex vivo porcine eyes.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_subretinal_robot` |
| **Full name** | Head-Mounted Robot Subretinal Injection Dataset |
| **Primary category** | `multimodal` |
| **Contained modalities** | surgical_video, oct, tabular |
| **Tasks** | segmentation, surgical_workflow, regression |
| **Samples** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 2.481 GB |
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

> All images and videos are from ex vivo porcine eyes. The repository also includes MATLAB bleb masks and pressure-sensor measurements.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_subretinal_robot --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download dryad_subretinal_robot --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_subretinal_robot')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.w0vt4b91w](https://doi.org/10.5061/dryad.w0vt4b91w)

**Source-term evidence:** [https://doi.org/10.5061/dryad.w0vt4b91w](https://doi.org/10.5061/dryad.w0vt4b91w)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_subretinal_robot,
  title  = { Head-Mounted Robot Subretinal Injection Dataset },
  note   = { Data and code from: Head-mounted surgical robots are an enabling technology for subretinal injections. Dryad. 2025. doi:10.5061/dryad.w0vt4b91w },
  year   = { 2025 },
  url    = { https://doi.org/10.5061/dryad.w0vt4b91w },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Data and code from: Head-mounted surgical robots are an enabling technology for subretinal injections. Dryad. 2025. doi:10.5061/dryad.w0vt4b91w
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
- [dryad_namd_visual_prediction](./dryad_namd_visual_prediction.md): Moorfields nAMD Visual-Change Prediction Dataset (926 records, `cc0`)
- [dryad_retinal_vein_cannulation](./dryad_retinal_vein_cannulation.md): Autonomous Retinal Vein Cannulation Data and Code (26 records, `cc0`)
- [ocular_chat_vqa](./ocular_chat_vqa.md): OcularChat-VQA: AREDS-Derived Patient-Physician Dialogue Dataset (844,000 records, `cc-by-nc-sa`)
