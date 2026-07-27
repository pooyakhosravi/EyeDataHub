---
id: drac22
title: "DRAC 2022: Diabetic Retinopathy Analysis Challenge"
sidebar_label: drac22
description: "174 OCTA images for DR lesion segmentation (IRMA, NPA, NV), image quality assessment, and DR grading (3-class)."
tags: ["octa", "cc-by", "zenodo", "segmentation", "classification", "grading"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# DRAC 2022: Diabetic Retinopathy Analysis Challenge

174 OCTA images for DR lesion segmentation (IRMA, NPA, NV), image quality assessment, and DR grading (3-class).

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `drac22` |
| **Full name** | DRAC 2022: Diabetic Retinopathy Analysis Challenge |
| **Primary category** | `octa` |
| **Contained modalities** | octa |
| **Tasks** | segmentation, classification, grading |
| **Samples** | 174 |
| **Classes** | 3 (No DR, Non-proliferative DR, Proliferative DR) |
| **Splits** | train, test |
| **Size** | 0.3 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Zenodo |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Standard loader included |


## Notes

> Available from Grand Challenge after free registration.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download drac22 --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download drac22 --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('drac22')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [zenodo.org/records](https://zenodo.org/records/10280359)

**Source-term evidence:** [zenodo.org/records](https://zenodo.org/records/10280359)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('drac22')
samples = ds.load(data_dir, split='test')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{drac22,
  title  = { DRAC 2022: Diabetic Retinopathy Analysis Challenge },
  note   = { Qin et al., 'DRAC: Diabetic Retinopathy Analysis Challenge with Ultra-Wide Optical Coherence Tomography Angiography Images', Medical Image Analysis 2024 },
  year   = { 2024 },
  url    = { https://zenodo.org/records/10280359 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Qin et al., 'DRAC: Diabetic Retinopathy Analysis Challenge with Ultra-Wide Optical Coherence Tomography Angiography Images', Medical Image Analysis 2024.
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

- [octa_macula_coronal](./octa_macula_coronal.md): OCTA Macula Coronal Views (82,560 records, `cc-by`)
- [octa_500](./octa_500.md): OCTA-500: Large-scale OCTA Multi-task Benchmark (500 records, `research-only`)
- [aroma_octa](./aroma_octa.md): AROMA Retinal OCTA Artifact Dataset (281 records, `cc-by`)
- [rose](./rose.md): ROSE: Retinal OCT-Angiography Vessel Segmentation (229 records, `cc-by`)
- [soul_octa](./soul_octa.md): SOUL: OCTA Human-Machine Collaborative Annotation Dataset (178 records, `cc-by`)
- [ut_fsocta](./ut_fsocta.md): UTHealth Fundus and Synthetic OCTA Dataset (count not reported records, `unknown`)
