---
id: octa_macula_coronal
title: "OCTA Macula Coronal Views"
sidebar_label: octa_macula_coronal
description: "A derived OCT angiography resource with 640 coronal PNG views for each of 129 subjects: 90 normal, 29 diabetic retinopathy, 5 AMD, and 5 choroidal neovascularization cases."
tags: ["octa", "cc-by", "mendeley", "classification", "visualization"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# OCTA Macula Coronal Views

A derived OCT angiography resource with 640 coronal PNG views for each of 129 subjects: 90 normal, 29 diabetic retinopathy, 5 AMD, and 5 choroidal neovascularization cases.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `octa_macula_coronal` |
| **Full name** | OCTA Macula Coronal Views |
| **Primary category** | `octa` |
| **Contained modalities** | octa |
| **Tasks** | classification, visualization |
| **Samples** | 82,560 |
| **Classes** | 4 (normal, diabetic_retinopathy, amd, cnv) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Mendeley Data |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Notes

> The sample count is the number of derived PNG views. They come from 129 subject-level OCTA scans, so analysis and splitting should remain grouped by subject.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download octa_macula_coronal --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download octa_macula_coronal --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('octa_macula_coronal')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/p5h7x55zw7/1)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/p5h7x55zw7/1)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{octa_macula_coronal,
  title  = { OCTA Macula Coronal Views },
  note   = { Al-Hinnawi AR. OCTA Macula Coronal Views. Mendeley Data. 2023. doi:10.17632/p5h7x55zw7.1 },
  year   = { 2023 },
  url    = { https://data.mendeley.com/datasets/p5h7x55zw7/1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Al-Hinnawi AR. OCTA Macula Coronal Views. Mendeley Data. 2023. doi:10.17632/p5h7x55zw7.1
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

- [octa_500](./octa_500.md): OCTA-500: Large-scale OCTA Multi-task Benchmark (500 records, `research-only`)
- [aroma_octa](./aroma_octa.md): AROMA Retinal OCTA Artifact Dataset (281 records, `cc-by`)
- [rose](./rose.md): ROSE: Retinal OCT-Angiography Vessel Segmentation (229 records, `cc-by`)
- [soul_octa](./soul_octa.md): SOUL: OCTA Human-Machine Collaborative Annotation Dataset (178 records, `cc-by`)
- [drac22](./drac22.md): DRAC 2022: Diabetic Retinopathy Analysis Challenge (174 records, `cc-by`)
- [ut_fsocta](./ut_fsocta.md): UTHealth Fundus and Synthetic OCTA Dataset (count not reported records, `unknown`)
