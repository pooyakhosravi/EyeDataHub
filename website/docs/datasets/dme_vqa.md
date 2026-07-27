---
id: dme_vqa
title: "Diabetic Macular Edema Visual Question Answering Dataset"
sidebar_label: dme_vqa
description: "Fundus-image VQA dataset for diabetic macular edema derived from IDRiD and e-ophtha."
tags: ["multimodal", "fundus", "text", "cc-by", "zenodo", "visual_question_answering", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Diabetic Macular Edema Visual Question Answering Dataset

Fundus-image VQA dataset for diabetic macular edema derived from IDRiD and e-ophtha.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dme_vqa` |
| **Full name** | Diabetic Macular Edema Visual Question Answering Dataset |
| **Primary category** | `multimodal` |
| **Contained modalities** | fundus, text |
| **Tasks** | visual_question_answering, classification |
| **Samples** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.1 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Zenodo |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Notes

> Derivative VQA layer built from existing fundus datasets.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dme_vqa --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download dme_vqa --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dme_vqa')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [zenodo.org/records](https://zenodo.org/records/6784358)

**Source-term evidence:** [zenodo.org/records](https://zenodo.org/records/6784358)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dme_vqa,
  title  = { Diabetic Macular Edema Visual Question Answering Dataset },
  note   = { Diabetic Macular Edema Visual Question Answering Dataset. Zenodo, 2022. doi:10.5281/zenodo.6784358 },
  year   = { 2022 },
  url    = { https://zenodo.org/records/6784358 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Diabetic Macular Edema Visual Question Answering Dataset. Zenodo, 2022. doi:10.5281/zenodo.6784358
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

- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 records, `unknown`)
- [angioreport](./angioreport.md): AngioReport Fundus Angiography Report Dataset (55,361 records, `unknown`)
- [ffa_ir](./ffa_ir.md): FFA-IR Medical Report Dataset (47,247 records, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 records, `unknown`)
- [x_pcr](./x_pcr.md): X-PCR Ophthalmology Progressive Clinical Reasoning Benchmark (18,700 records, `unknown`)
- [deepeyenet](./deepeyenet.md): DeepEyeNet (DEN): Fundus Report Generation Dataset (15,709 records, `research-only`)
- [fundus_report_dataset](./fundus_report_dataset.md): Fundus Report Dataset (422 records, `cc-by`)
- [csdi](./csdi.md): CSDI: Cataract Severity Diagnostic Image Dataset (187 records, `cc-by`)
