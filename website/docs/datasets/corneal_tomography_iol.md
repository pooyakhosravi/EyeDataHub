---
id: corneal_tomography_iol
title: "Multi-Parameter Corneal Tomography Dataset for IOL Selection"
sidebar_label: corneal_tomography_iol
description: "Pentacam-derived corneal tomography variables for intraocular-lens and corneal subtype modeling."
tags: ["tabular", "cc-by", "mendeley", "classification", "regression"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Multi-Parameter Corneal Tomography Dataset for IOL Selection

Pentacam-derived corneal tomography variables for intraocular-lens and corneal subtype modeling.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `corneal_tomography_iol` |
| **Full name** | Multi-Parameter Corneal Tomography Dataset for IOL Selection |
| **Primary category** | `tabular` |
| **Contained modalities** | tabular |
| **Tasks** | classification, regression |
| **Samples** | 61 |
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
eyehub download corneal_tomography_iol --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download corneal_tomography_iol --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('corneal_tomography_iol')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/wddj7bh9p9/1)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/wddj7bh9p9/1)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{corneal_tomography_iol,
  title  = { Multi-Parameter Corneal Tomography Dataset for IOL Selection },
  note   = { Multi-parameter corneal tomography dataset for IOL selection. Mendeley Data, V1, 2025. doi:10.17632/wddj7bh9p9.1 },
  year   = { 2025 },
  url    = { https://data.mendeley.com/datasets/wddj7bh9p9/1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Multi-parameter corneal tomography dataset for IOL selection. Mendeley Data, V1, 2025. doi:10.17632/wddj7bh9p9.1
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
- [leops_erg](./leops_erg.md): LEOPs Light-Adapted Electroretinogram and Oscillatory Potentials Dataset (9,743 records, `cc-by`)
- [olives](./olives.md): OLIVES: Ophthalmic Labels for Investigating Visual Eye Semantics (9,408 records, `cc-by`)
- [fprm_retina](./fprm_retina.md): FPRM Multimodal Eye Imaging and Psychological Assessment Dataset (3,361 records, `research-only`)
- [uveitis_smote](./uveitis_smote.md): Image Dataset on Eye Diseases Classification with Symptoms and SMOTE Validation (3,245 records, `cc-by`)
- [eed_astig](./eed_astig.md): EED-Astig Pediatric External-Eye Dataset (3,088 records, `research-only`)
