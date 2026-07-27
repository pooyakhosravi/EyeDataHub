---
id: dryad_glaucoma_rnfl_vf
title: "RNFL and Visual-Field Glaucoma Diagnosis Dataset"
sidebar_label: dryad_glaucoma_rnfl_vf
description: "Clinical records combining retinal nerve fiber layer, visual-field, corneal-thickness, and intraocular-pressure features."
tags: ["tabular", "visual_field", "cc0", "dryad", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# RNFL and Visual-Field Glaucoma Diagnosis Dataset

Clinical records combining retinal nerve fiber layer, visual-field, corneal-thickness, and intraocular-pressure features.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_glaucoma_rnfl_vf` |
| **Full name** | RNFL and Visual-Field Glaucoma Diagnosis Dataset |
| **Primary category** | `tabular` |
| **Contained modalities** | tabular, visual_field |
| **Tasks** | classification |
| **Samples** | 499 |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 3.2e-05 GB |
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

> The source reports 399 training/validation cases and 100 held-out test cases. The archive contains examination-record features rather than raw OCT or visual-field images.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_glaucoma_rnfl_vf --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download dryad_glaucoma_rnfl_vf --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_glaucoma_rnfl_vf')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.q6ft5](https://doi.org/10.5061/dryad.q6ft5)

**Source-term evidence:** [https://doi.org/10.5061/dryad.q6ft5](https://doi.org/10.5061/dryad.q6ft5)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_glaucoma_rnfl_vf,
  title  = { RNFL and Visual-Field Glaucoma Diagnosis Dataset },
  note   = { Development of machine learning models for diagnosis of glaucoma. Dryad. 2018. doi:10.5061/dryad.q6ft5 },
  year   = { 2018 },
  url    = { https://doi.org/10.5061/dryad.q6ft5 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Development of machine learning models for diagnosis of glaucoma. Dryad. 2018. doi:10.5061/dryad.q6ft5
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

- [grape](./grape.md): GRAPE: Glaucoma Real-world Appraisal Progression Ensemble (1,115 records, `cc0`)
- [harvard_gdp](./harvard_gdp.md): Harvard GDP: Glaucoma Detection and Progression Dataset (1,000 records, `cc-by-nc-nd`)
- [fairvlmed](./fairvlmed.md): FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset (count not reported records, `unknown`)
- [ocular_chat_vqa](./ocular_chat_vqa.md): OcularChat-VQA: AREDS-Derived Patient-Physician Dialogue Dataset (844,000 records, `cc-by-nc-sa`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 records, `unknown`)
- [uwhvf](./uwhvf.md): UWHVF: University of Washington Humphrey Visual Field (28,943 records, `cc-by`)
- [oculoscope](./oculoscope.md): OculoScope: Fairer AI in Ophthalmology Dataset (16,530 records, `cc-by`)
- [leops_erg](./leops_erg.md): LEOPs Light-Adapted Electroretinogram and Oscillatory Potentials Dataset (9,743 records, `cc-by`)
