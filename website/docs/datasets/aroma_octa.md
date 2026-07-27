---
id: aroma_octa
title: "AROMA Retinal OCTA Artifact Dataset"
sidebar_label: aroma_octa
description: "Retinal OCTA scans labeled for artifact type, artifact severity, signal strength, and image quality."
tags: ["octa", "cc-by", "zenodo", "quality_assessment", "classification", "grading"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# AROMA Retinal OCTA Artifact Dataset

Retinal OCTA scans labeled for artifact type, artifact severity, signal strength, and image quality.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `aroma_octa` |
| **Full name** | AROMA Retinal OCTA Artifact Dataset |
| **Primary category** | `octa` |
| **Contained modalities** | octa |
| **Tasks** | quality_assessment, classification, grading |
| **Samples** | 281 |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 1.011 GB |
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

> The source reports 281 scans from 115 patients. Fourteen en-face images per scan yield 3,934 derived images with seven artifact types graded on a four-level severity scale.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download aroma_octa --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download aroma_octa --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('aroma_octa')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5281/zenodo.18258095](https://doi.org/10.5281/zenodo.18258095)

**Source-term evidence:** [https://doi.org/10.5281/zenodo.18258095](https://doi.org/10.5281/zenodo.18258095)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{aroma_octa,
  title  = { AROMA Retinal OCTA Artifact Dataset },
  note   = { Szwarcberg L, Anwer A, Gozlan A, et al. The AROMA Dataset for Automatic Detection of Artifact Type and Severity in Retinal Optical Coherence Tomography Angiography. Ophthalmic Research. 2026. doi:10.1159/000551126 },
  year   = { 2026 },
  url    = { https://doi.org/10.5281/zenodo.18258095 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Szwarcberg L, Anwer A, Gozlan A, et al. The AROMA Dataset for Automatic Detection of Artifact Type and Severity in Retinal Optical Coherence Tomography Angiography. Ophthalmic Research. 2026. doi:10.1159/000551126
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
- [rose](./rose.md): ROSE: Retinal OCT-Angiography Vessel Segmentation (229 records, `cc-by`)
- [soul_octa](./soul_octa.md): SOUL: OCTA Human-Machine Collaborative Annotation Dataset (178 records, `cc-by`)
- [drac22](./drac22.md): DRAC 2022: Diabetic Retinopathy Analysis Challenge (174 records, `cc-by`)
- [ut_fsocta](./ut_fsocta.md): UTHealth Fundus and Synthetic OCTA Dataset (count not reported records, `unknown`)
