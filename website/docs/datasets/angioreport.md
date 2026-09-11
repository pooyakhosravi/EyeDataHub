---
id: angioreport
title: "AngioReport Fundus Angiography Report Dataset"
sidebar_label: angioreport
description: "De-identified fluorescein and indocyanine-green angiography images paired with structured lesion descriptions and reports."
tags: ["multimodal", "fundus", "fundus_angiography", "text", "unknown", "manual", "report_generation", "multilabel", "classification", "resource-role-current-dataset", "dataset-family-angioreport"]
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
| **First published** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Primary category** | `multimodal` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `angioreport` |
| **Contained modalities** | fundus, fundus_angiography, text |
| **Tasks** | report_generation, multilabel, classification |
| **Primary reported quantity** | 55,361 images |
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


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 55,361 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [tianchi.aliyun.com/dataset](https://tianchi.aliyun.com/dataset/170128) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> The paper reports 55,361 images from 1,691 patients and 3,179 eyes across 24 diagnostic conditions. Access is routed through the 2023 APTOS/Tianchi competition page; no clear dataset license was visible, so users must review current platform terms.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download angioreport --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download angioreport --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('angioreport')
print(preflight_dataset(ds, './data'))  # no download
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

## Similar resources by shared modality

- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [ffa_ir](./ffa_ir.md): FFA-IR Medical Report Dataset (47,247 images, `unknown`)
- [x_pcr](./x_pcr.md): X-PCR Ophthalmology Progressive Clinical Reasoning Benchmark (18,735 rows, `unknown`)
- [ophthalvqa](./ophthalvqa.md): OphthalVQA Dataset (600 question answer pairs, `cc-by`)
- [mm_retinal_reason](./mm_retinal_reason.md): MM-Retinal-Reason: Ophthalmology Multimodal Reasoning Dataset (130 question answer pairs, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [deepeyenet](./deepeyenet.md): DeepEyeNet (DEN): Fundus Report Generation Dataset (15,709 images, `research-only`)
- [dme_vqa](./dme_vqa.md): Diabetic Macular Edema Visual Question Answering Dataset (13,470 question answer pairs, `cc-by`)
