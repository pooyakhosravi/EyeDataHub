---
id: ffa_ir
title: "FFA-IR Medical Report Dataset"
sidebar_label: ffa_ir
description: "Fundus fluorescein angiography images paired with Chinese and translated English reports for report-generation research."
tags: ["multimodal", "fundus", "fundus_angiography", "text", "unknown", "physionet", "report_generation", "text_generation"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# FFA-IR Medical Report Dataset

Fundus fluorescein angiography images paired with Chinese and translated English reports for report-generation research.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `ffa_ir` |
| **Full name** | FFA-IR Medical Report Dataset |
| **Primary category** | `multimodal` |
| **Contained modalities** | fundus, fundus_angiography, text |
| **Tasks** | report_generation, text_generation |
| **Primary reported quantity** | 47,247 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | PhysioNet credentialed access terms |
| **Normalized terms** | `unknown` |
| **Descriptive screening label** | Unknown or unclear; do not assume permission |
| **Terms scope** | `unknown` |
| **Access friction** | `controlled_or_manual` |
| **Route backend** | PhysioNet |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `manual_access_blocked` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 47,247 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [https://doi.org/10.13026/k5rp-9h43](https://doi.org/10.13026/k5rp-9h43) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# This route requires upstream human action; no transfer starts.
eyehub download ffa_ir --data-dir ./data --dry-run --json
# Follow the official instructions shown by preflight.
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('ffa_ir')
print(preflight_dataset(ds, './data'))  # returns manual_access_blocked
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.13026/k5rp-9h43](https://doi.org/10.13026/k5rp-9h43)

**Source-term evidence:** [https://doi.org/10.13026/k5rp-9h43](https://doi.org/10.13026/k5rp-9h43)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{ffa_ir,
  title  = { FFA-IR Medical Report Dataset },
  note   = { FFA-IR: Towards an Explainable and Reliable Medical Report Generation Benchmark. PhysioNet, 2021 },
  year   = { 2021 },
  url    = { https://doi.org/10.13026/k5rp-9h43 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
FFA-IR: Towards an Explainable and Reliable Medical Report Generation Benchmark. PhysioNet, 2021.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** PhysioNet credentialed access terms
- **Normalized category:** `unknown`
- **Apparent scope:** `unknown`
- **Descriptive screening label:** Unknown or unclear; do not assume permission

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [angioreport](./angioreport.md): AngioReport Fundus Angiography Report Dataset (55,361 images, `unknown`)
- [x_pcr](./x_pcr.md): X-PCR Ophthalmology Progressive Clinical Reasoning Benchmark (18,735 rows, `unknown`)
- [ophthalvqa](./ophthalvqa.md): OphthalVQA Dataset (600 question answer pairs, `cc-by`)
- [mm_retinal_reason](./mm_retinal_reason.md): MM-Retinal-Reason: Ophthalmology Multimodal Reasoning Dataset (130 question answer pairs, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [deepeyenet](./deepeyenet.md): DeepEyeNet (DEN): Fundus Report Generation Dataset (15,709 images, `research-only`)
- [dme_vqa](./dme_vqa.md): Diabetic Macular Edema Visual Question Answering Dataset (13,470 question answer pairs, `cc-by`)
