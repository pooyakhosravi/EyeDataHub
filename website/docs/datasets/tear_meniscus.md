---
id: tear_meniscus
title: "Multicentre Tear Meniscus Segmentation Dataset"
sidebar_label: tear_meniscus
description: "1,693 color and 1,739 infrared ocular-surface images from five clinical centers with pixel-level tear-meniscus segmentation. First multi-center dry-eye imaging benchmark."
tags: ["multimodal", "external_eye", "infrared", "cc-by", "figshare", "segmentation"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Multicentre Tear Meniscus Segmentation Dataset

1,693 color and 1,739 infrared ocular-surface images from five clinical centers with pixel-level tear-meniscus segmentation. First multi-center dry-eye imaging benchmark.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `tear_meniscus` |
| **Full name** | Multicentre Tear Meniscus Segmentation Dataset |
| **Primary category** | `multimodal` |
| **Contained modalities** | external_eye, infrared |
| **Tasks** | segmentation |
| **Samples** | 3,432 |
| **Classes** | 2 (Not reported) |
| **Splits** | all |
| **Size** | 1.5 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Figshare |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `end_to_end_tested` |
| **Legacy sample-loader status** | Metadata and access only |


## Notes

> Figshare marks the deposited files CC BY 4.0. Adds a dry-eye and tear-film modality that is otherwise absent.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download tear_meniscus --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download tear_meniscus --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('tear_meniscus')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.6084/m9.figshare.28650536.v2](https://doi.org/10.6084/m9.figshare.28650536.v2)

**Source-term evidence:** [https://doi.org/10.6084/m9.figshare.28650536.v2](https://doi.org/10.6084/m9.figshare.28650536.v2)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{tear_meniscus,
  title  = { Multicentre Tear Meniscus Segmentation Dataset },
  note   = { Multicentre tear meniscus segmentation dataset, Scientific Data 2025 },
  year   = { 2025 },
  url    = { https://doi.org/10.6084/m9.figshare.28650536.v2 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Multicentre tear meniscus segmentation dataset, Scientific Data 2025.
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
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 records, `unknown`)
- [x_pcr](./x_pcr.md): X-PCR Ophthalmology Progressive Clinical Reasoning Benchmark (18,735 records, `unknown`)
- [popeye_nir](./popeye_nir.md): PopEYE Infrared Ocular Image Dataset (14,976 records, `cc-by`)
- [mcoa](./mcoa.md): MCOA: Multimodal Corneal Opacity Assessment Dataset (6,664 records, `cc-by`)
- [uveitis_smote](./uveitis_smote.md): Image Dataset on Eye Diseases Classification with Symptoms and SMOTE Validation (3,245 records, `cc-by`)
- [eed_astig](./eed_astig.md): EED-Astig Pediatric External-Eye Dataset (3,088 records, `research-only`)
- [periorbital_segmentation](./periorbital_segmentation.md): Open-Source Periorbital Segmentation Dataset (2,842 records, `cc-by`)
