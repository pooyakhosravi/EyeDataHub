---
id: fundus_report_dataset
title: "Fundus Report Dataset"
sidebar_label: fundus_report_dataset
description: "Fundus/UWF image-report dataset derived from DeepDRiD and OUWFD-style resources for report-generation research."
tags: ["multimodal", "fundus", "uwf_fundus", "text", "cc-by", "huggingface", "report_generation", "text_generation"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Fundus Report Dataset

Fundus/UWF image-report dataset derived from DeepDRiD and OUWFD-style resources for report-generation research.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `fundus_report_dataset` |
| **Full name** | Fundus Report Dataset |
| **Primary category** | `multimodal` |
| **Contained modalities** | fundus, uwf_fundus, text |
| **Tasks** | report_generation, text_generation |
| **Samples** | 422 |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.5 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | HuggingFace Hub |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Notes

> Derivative report-generation view; verify source image terms row by row.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download fundus_report_dataset --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download fundus_report_dataset --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('fundus_report_dataset')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [huggingface.co/datasets](https://huggingface.co/datasets/zzzzineun/fundus-report-dataset)

**Source-term evidence:** [huggingface.co/datasets](https://huggingface.co/datasets/zzzzineun/fundus-report-dataset)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{fundus_report_dataset,
  title  = { Fundus Report Dataset },
  note   = { zzzzineun/fundus-report-dataset. Hugging Face dataset, accessed 2026-07 },
  year   = { 2026 },
  url    = { https://huggingface.co/datasets/zzzzineun/fundus-report-dataset },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
zzzzineun/fundus-report-dataset. Hugging Face dataset, accessed 2026-07.
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
- [mmrdr](./mmrdr.md): MMRDR: Multi-Modal Retinal Diabetic Retinopathy Dataset (24,460 records, `cc-by`)
- [x_pcr](./x_pcr.md): X-PCR Ophthalmology Progressive Clinical Reasoning Benchmark (18,700 records, `unknown`)
- [deepeyenet](./deepeyenet.md): DeepEyeNet (DEN): Fundus Report Generation Dataset (15,709 records, `research-only`)
- [deepdrid](./deepdrid.md): DeepDRiD: Diabetic Retinopathy Grading and Image Quality Dataset (2,256 records, `cc-by-sa`)
