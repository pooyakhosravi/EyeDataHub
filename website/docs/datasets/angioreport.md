---
id: angioreport
title: "AngioReport Fundus Angiography Report Dataset"
sidebar_label: angioreport
description: "De-identified fluorescein and indocyanine-green angiography images paired with structured lesion descriptions and reports."
tags: ["multimodal", "fundus", "fundus_angiography", "text", "unknown", "manual", "report_generation", "multilabel", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# AngioReport Fundus Angiography Report Dataset

De-identified fluorescein and indocyanine-green angiography images paired with structured lesion descriptions and reports.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `angioreport` |
| **Full name** | AngioReport Fundus Angiography Report Dataset |
| **Primary category** | `multimodal` |
| **Contained modalities** | fundus, fundus_angiography, text |
| **Tasks** | report_generation, multilabel, classification |
| **Samples** | 55,361 |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | Unknown; competition data terms must be reviewed |
| **Normalized terms** | `unknown` |
| **Descriptive screening label** | Unknown or unclear; do not assume permission |
| **Terms scope** | `unknown` |
| **Access friction** | `self_service_clickthrough` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `guided_instructions_only` |
| **Legacy sample-loader status** | Metadata and access only |


## Notes

> The paper reports 55,361 images from 1,691 patients and 3,179 eyes across 24 diagnostic conditions. Access is routed through the 2023 APTOS/Tianchi competition page; no clear dataset license was visible, so users must review current platform terms.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download angioreport --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download angioreport --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('angioreport')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [tianchi.aliyun.com/dataset](https://tianchi.aliyun.com/dataset/170128)

**Source-term evidence:** [tianchi.aliyun.com/dataset](https://tianchi.aliyun.com/dataset/170128)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{angioreport,
  title  = { AngioReport Fundus Angiography Report Dataset },
  note   = { Xu P, Chotcomwongse P, Zhang W, et al. AngioReport: Dataset and baseline methods for fundus angiography report generation. British Journal of Ophthalmology. 2025;109:1283-1288. doi:10.1136/bjo-2024-327006 },
  year   = { 2025 },
  url    = { https://tianchi.aliyun.com/dataset/170128 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Xu P, Chotcomwongse P, Zhang W, et al. AngioReport: Dataset and baseline methods for fundus angiography report generation. British Journal of Ophthalmology. 2025;109:1283-1288. doi:10.1136/bjo-2024-327006
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Unknown; competition data terms must be reviewed
- **Normalized category:** `unknown`
- **Apparent scope:** `unknown`
- **Descriptive screening label:** Unknown or unclear; do not assume permission

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Related datasets with shared modalities

- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 records, `unknown`)
- [ffa_ir](./ffa_ir.md): FFA-IR Medical Report Dataset (47,247 records, `unknown`)
- [x_pcr](./x_pcr.md): X-PCR Ophthalmology Progressive Clinical Reasoning Benchmark (18,735 records, `unknown`)
- [mm_retinal_reason](./mm_retinal_reason.md): MM-Retinal-Reason: Ophthalmology Multimodal Reasoning Dataset (count not reported records, `unknown`)
- [ophthalvqa](./ophthalvqa.md): OphthalVQA Dataset (count not reported records, `cc-by`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 records, `unknown`)
- [deepeyenet](./deepeyenet.md): DeepEyeNet (DEN): Fundus Report Generation Dataset (15,709 records, `research-only`)
- [fairvlmed](./fairvlmed.md): FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset (10,000 records, `cc-by-nc-nd`)
