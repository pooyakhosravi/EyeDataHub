---
id: corneal_parameters_kc
title: "Corneal Parameters Keratoconus Study"
sidebar_label: corneal_parameters_kc
description: "Tabular keratoconus dataset with 77 eye-level rows and 60 variables describing visual acuity, contrast sensitivity, stage, and corneal elevation/shape parameters."
tags: ["tabular", "cc-by", "mendeley", "classification", "regression"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Corneal Parameters Keratoconus Study

Tabular keratoconus dataset with 77 eye-level rows and 60 variables describing visual acuity, contrast sensitivity, stage, and corneal elevation/shape parameters.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `corneal_parameters_kc` |
| **Full name** | Corneal Parameters Keratoconus Study |
| **Primary category** | `tabular` |
| **Contained modalities** | tabular |
| **Tasks** | classification, regression |
| **Samples** | 77 |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.01 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Mendeley Data |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download corneal_parameters_kc --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download corneal_parameters_kc --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('corneal_parameters_kc')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/3nz4fkwn3y/1)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/3nz4fkwn3y/1)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{corneal_parameters_kc,
  title  = { Corneal Parameters Keratoconus Study },
  note   = { Luguzis A, Liduma S. corneal-parameters-KC-study_2020-07-03. Mendeley Data, V1, 2020. doi:10.17632/3nz4fkwn3y.1 },
  year   = { 2020 },
  url    = { https://data.mendeley.com/datasets/3nz4fkwn3y/1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Luguzis A, Liduma S. corneal-parameters-KC-study_2020-07-03. Mendeley Data, V1, 2020. doi:10.17632/3nz4fkwn3y.1
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC BY 4.0
- **Normalized category:** `cc-by`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Standard label without an explicit NC clause; not a permission finding

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Related datasets with shared modalities

- [ocular_chat_vqa](./ocular_chat_vqa.md): OcularChat-VQA: AREDS-Derived Patient-Physician Dialogue Dataset (844,000 records, `cc-by-nc-sa`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 records, `unknown`)
- [oculoscope](./oculoscope.md): OculoScope: Fairer AI in Ophthalmology Dataset (16,530 records, `cc-by`)
- [fairvlmed](./fairvlmed.md): FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset (10,000 records, `cc-by-nc-nd`)
- [leops_erg](./leops_erg.md): LEOPs Light-Adapted Electroretinogram and Oscillatory Potentials Dataset (9,743 records, `cc-by`)
- [olives](./olives.md): OLIVES: Ophthalmic Labels for Investigating Visual Eye Semantics (9,408 records, `cc-by`)
- [fprm_retina](./fprm_retina.md): FPRM Multimodal Eye Imaging and Psychological Assessment Dataset (3,361 records, `research-only`)
- [uveitis_smote](./uveitis_smote.md): Image Dataset on Eye Diseases Classification with Symptoms and SMOTE Validation (3,245 records, `cc-by`)
