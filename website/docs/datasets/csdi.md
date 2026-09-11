---
id: csdi
title: "CSDI: Cataract Severity Diagnostic Image Dataset"
sidebar_label: csdi
description: "187 cataract cases with color fundus images and paired professional cataract-grading diagnostic reports. Designed for medical multimodal-LLM evaluation."
tags: ["fundus", "text", "cc-by", "huggingface", "grading", "classification", "resource-role-current-dataset", "dataset-family-csdi"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# CSDI: Cataract Severity Diagnostic Image Dataset

187 cataract cases with color fundus images and paired professional cataract-grading diagnostic reports. Designed for medical multimodal-LLM evaluation.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `csdi` |
| **Full name** | CSDI: Cataract Severity Diagnostic Image Dataset |
| **First published** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Primary category** | `fundus` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `csdi` |
| **Contained modalities** | fundus, text |
| **Tasks** | grading, classification |
| **Primary reported quantity** | 187 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 1.0 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | HuggingFace Hub |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 187 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [huggingface.co/datasets](https://huggingface.co/datasets/RainyNight/CSDI) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> First public fundus dataset with paired professional cataract reports. Canonical Hugging Face repository: RainyNight/CSDI.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download csdi --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download csdi --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('csdi')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [huggingface.co/datasets](https://huggingface.co/datasets/RainyNight/CSDI)

**Source-term evidence:** [huggingface.co/datasets](https://huggingface.co/datasets/RainyNight/CSDI)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{csdi,
  title  = { CSDI: Cataract Severity Diagnostic Image Dataset },
  note   = { Scientific Data 2026. doi:10.1038/s41597-026-06684-8 },
  year   = { 2026 },
  url    = { https://huggingface.co/datasets/RainyNight/CSDI },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Scientific Data 2026. doi:10.1038/s41597-026-06684-8
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC BY 4.0
- **Normalized category:** `cc-by`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Standard label without an explicit NC clause; not a permission finding

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [angioreport](./angioreport.md): AngioReport Fundus Angiography Report Dataset (55,361 images, `unknown`)
- [ffa_ir](./ffa_ir.md): FFA-IR Medical Report Dataset (47,247 images, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [x_pcr](./x_pcr.md): X-PCR Ophthalmology Progressive Clinical Reasoning Benchmark (18,735 rows, `unknown`)
- [deepeyenet](./deepeyenet.md): DeepEyeNet (DEN): Fundus Report Generation Dataset (15,709 images, `research-only`)
- [dme_vqa](./dme_vqa.md): Diabetic Macular Edema Visual Question Answering Dataset (13,470 question answer pairs, `cc-by`)
- [dme_vqa_logical](./dme_vqa_logical.md): DME VQA Dataset with Logical Relations (13,470 question answer pairs, `cc-by`)
