---
id: ghana_eye_screening
title: "Eye Screening Data for First-Year University Students in Ghana"
sidebar_label: ghana_eye_screening
description: "Questionnaire and clinical eye-screening data from first-year university students in Ghana."
tags: ["tabular", "cc-by-nc-nd", "mendeley", "classification", "regression"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Eye Screening Data for First-Year University Students in Ghana

Questionnaire and clinical eye-screening data from first-year university students in Ghana.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `ghana_eye_screening` |
| **Full name** | Eye Screening Data for First-Year University Students in Ghana |
| **Primary category** | `tabular` |
| **Contained modalities** | tabular |
| **Tasks** | classification, regression |
| **Samples** | 2,494 |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.01 GB |
| **Source-stated terms** | CC BY-NC-ND 4.0 |
| **Normalized terms** | `cc-by-nc-nd` |
| **Descriptive screening label** | Explicit noncommercial clause recorded; check source |
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
eyehub download ghana_eye_screening --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download ghana_eye_screening --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('ghana_eye_screening')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/mfv6sb5wyc/4)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/mfv6sb5wyc/4)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{ghana_eye_screening,
  title  = { Eye Screening Data for First-Year University Students in Ghana },
  note   = { Eye screening data for first year university students in Ghana. Mendeley Data, V4, 2025. doi:10.17632/mfv6sb5wyc.4 },
  year   = { 2025 },
  url    = { https://data.mendeley.com/datasets/mfv6sb5wyc/4 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Eye screening data for first year university students in Ghana. Mendeley Data, V4, 2025. doi:10.17632/mfv6sb5wyc.4
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC BY-NC-ND 4.0
- **Normalized category:** `cc-by-nc-nd`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Explicit noncommercial clause recorded; check source

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
