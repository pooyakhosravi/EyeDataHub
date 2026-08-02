---
id: rfmid2
title: "RFMiD 2.0 Auxiliary Multi-Disease Fundus Dataset"
sidebar_label: rfmid2
description: "Auxiliary RFMiD 2.0 retinal fundus dataset spanning 51 disease categories."
tags: ["fundus", "cc-by", "zenodo", "classification", "multilabel", "documented-relationship", "relationship-derived_from", "relationship-extension_of"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# RFMiD 2.0 Auxiliary Multi-Disease Fundus Dataset

Auxiliary RFMiD 2.0 retinal fundus dataset spanning 51 disease categories.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `rfmid2` |
| **Full name** | RFMiD 2.0 Auxiliary Multi-Disease Fundus Dataset |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | classification, multilabel |
| **Primary reported quantity** | 860 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.5 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Zenodo |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 860 | `images` | RFMiD 2.0 auxiliary images | `official_source_description` | [zenodo.org/records](https://zenodo.org/records/7505822) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Versioned extension of existing `rfmid`; retain as separate auxiliary release.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- [multieye](./multieye.md) is `derived from` this record: The MultiEYE paper names this record as one of the public fundus or OCT sources assembled for the benchmark. ([evidence](https://arxiv.org/abs/2412.09402))
- [x_pcr](./x_pcr.md) is `derived from` this record: Source labels in the version-pinned public X-PCR deposit identify this catalog record as upstream material. ([evidence](https://huggingface.co/datasets/Fantasy666/X-PCR/tree/06a318fd852230326386e3c6514d8a11b7a6b4af))
- This record is `extension of` [rfmid](./rfmid.md): RFMiD 2.0 is described as an auxiliary dataset to the earlier RFMiD release, not as the same image cohort. ([evidence](https://zenodo.org/records/7505822))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download rfmid2 --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download rfmid2 --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('rfmid2')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [zenodo.org/records](https://zenodo.org/records/7505822)

**Source-term evidence:** [zenodo.org/records](https://zenodo.org/records/7505822)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{rfmid2,
  title  = { RFMiD 2.0 Auxiliary Multi-Disease Fundus Dataset },
  note   = { RFMiD 2.0. Zenodo, 2022. doi:10.5281/zenodo.7505822 },
  year   = { 2022 },
  url    = { https://zenodo.org/records/7505822 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
RFMiD 2.0. Zenodo, 2022. doi:10.5281/zenodo.7505822
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

- [airogs](./airogs.md): AIROGS: AI for Robust Glaucoma Screening (113,893 images, `cc-by-nc-nd`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (103,959 images, `mit`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [justraigs](./justraigs.md): JustRAIGS: Just Referral AI Glaucoma Screening Dataset (101,442 images, `cc-by-nc-nd`)
- [eyepacs](./eyepacs.md): EyePACS — Diabetic Retinopathy Detection (Kaggle 2015) (88,702 images, `research-only`)
- [angioreport](./angioreport.md): AngioReport Fundus Angiography Report Dataset (55,361 images, `unknown`)
- [ffa_ir](./ffa_ir.md): FFA-IR Medical Report Dataset (47,247 images, `unknown`)
- [bidr](./bidr.md): BiDR: Diabetic Retinopathy Diagnosis Dataset (35,126 images, `unknown`)
