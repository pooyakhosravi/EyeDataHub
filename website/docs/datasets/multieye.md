---
id: multieye
title: "MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark"
sidebar_label: multieye
description: "58,036 fundus + 45,923 OCT images assembled for multi-disease classification (8 classes) with cross-modal distillation. Sourced from multiple public ophthalmic datasets."
tags: ["multimodal", "fundus", "oct", "mit", "huggingface", "classification", "resource-role-derivative-dataset", "dataset-family-multieye", "documented-relationship", "relationship-derived_from"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark

58,036 fundus + 45,923 OCT images assembled for multi-disease classification (8 classes) with cross-modal distillation. Sourced from multiple public ophthalmic datasets.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `multieye` |
| **Full name** | MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark |
| **First published** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Primary category** | `multimodal` |
| **Resource role** | `derivative_dataset` |
| **Dataset family** | `multieye` |
| **Contained modalities** | fundus, oct |
| **Tasks** | classification |
| **Primary reported quantity** | 103,959 images |
| **Classes** | 8 (Not reported) |
| **Splits** | train, val, test |
| **Size** | 27.3 GB |
| **Source-stated terms** | MIT |
| **Normalized terms** | `mit` |
| **Descriptive screening label** | Standard label without an explicit NC clause; verify that it applies to data |
| **Terms scope** | `unknown` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | HuggingFace Hub |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 103,959 | `images` | Fundus and OCT images across the composite benchmark Component source datasets overlap other catalog records. | `derived_from_reported_components` | [arxiv.org/abs](https://arxiv.org/abs/2412.09402) |
| Additional | 58,036 | `images` | Fundus component | `official_source_description` | [arxiv.org/abs](https://arxiv.org/abs/2412.09402) |
| Additional | 45,923 | `images` | OCT component | `official_source_description` | [arxiv.org/abs](https://arxiv.org/abs/2412.09402) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Re-aggregates several source datasets — image licenses inherit from their original sources. Verify per-component before reuse.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- This record is `derived from` [ddr](./ddr.md): The MultiEYE paper names this record as one of the public fundus or OCT sources assembled for the benchmark. ([evidence](https://arxiv.org/abs/2412.09402))
- This record is `derived from` [eyepacs](./eyepacs.md): The MultiEYE paper names this record as one of the public fundus or OCT sources assembled for the benchmark. ([evidence](https://arxiv.org/abs/2412.09402))
- This record is `derived from` [fives](./fives.md): The MultiEYE paper names this record as one of the public fundus or OCT sources assembled for the benchmark. ([evidence](https://arxiv.org/abs/2412.09402))
- This record is `derived from` [goals](./goals.md): The MultiEYE paper names this record as one of the public fundus or OCT sources assembled for the benchmark. ([evidence](https://arxiv.org/abs/2412.09402))
- This record is `derived from` [hassan_composite_retina](./hassan_composite_retina.md): The MultiEYE paper names this record as one of the public fundus or OCT sources assembled for the benchmark. ([evidence](https://arxiv.org/abs/2412.09402))
- This record is `derived from` [kermany_oct](./kermany_oct.md): The MultiEYE paper names this record as one of the public fundus or OCT sources assembled for the benchmark. ([evidence](https://arxiv.org/abs/2412.09402))
- This record is `derived from` [messidor2](./messidor2.md): The MultiEYE paper names this record as one of the public fundus or OCT sources assembled for the benchmark. ([evidence](https://arxiv.org/abs/2412.09402))
- This record is `derived from` [octid](./octid.md): The MultiEYE paper names this record as one of the public fundus or OCT sources assembled for the benchmark. ([evidence](https://arxiv.org/abs/2412.09402))
- This record is `derived from` [odir2019](./odir2019.md): The MultiEYE paper names this record as one of the public fundus or OCT sources assembled for the benchmark. ([evidence](https://arxiv.org/abs/2412.09402))
- This record is `derived from` [rfmid](./rfmid.md): The MultiEYE paper names this record as one of the public fundus or OCT sources assembled for the benchmark. ([evidence](https://arxiv.org/abs/2412.09402))
- This record is `derived from` [rfmid2](./rfmid2.md): The MultiEYE paper names this record as one of the public fundus or OCT sources assembled for the benchmark. ([evidence](https://arxiv.org/abs/2412.09402))
- This record is `derived from` [stare](./stare.md): The MultiEYE paper names this record as one of the public fundus or OCT sources assembled for the benchmark. ([evidence](https://arxiv.org/abs/2412.09402))
- This record is `derived from` [vietai_retinal_disease](./vietai_retinal_disease.md): The MultiEYE paper names this record as one of the public fundus or OCT sources assembled for the benchmark. ([evidence](https://arxiv.org/abs/2412.09402))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download multieye --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download multieye --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('multieye')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [huggingface.co/datasets](https://huggingface.co/datasets/Luxuriant16/MultiEYE)

**Source-term evidence:** [huggingface.co/datasets](https://huggingface.co/datasets/Luxuriant16/MultiEYE)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{multieye,
  title  = { MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark },
  note   = { MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark, IEEE TMI 2025; arXiv:2412.09402 },
  year   = { 2025 },
  url    = { https://huggingface.co/datasets/Luxuriant16/MultiEYE },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark, IEEE TMI 2025; arXiv:2412.09402
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** MIT
- **Normalized category:** `mit`
- **Apparent scope:** `unknown`
- **Descriptive screening label:** Standard label without an explicit NC clause; verify that it applies to data

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [harvard_fairvision](./harvard_fairvision.md): Harvard-FairVision (AMD + DR + Glaucoma, paired SLO + OCT) (30,000 participants, `cc-by-nc-nd`)
- [mmrdr](./mmrdr.md): MMRDR: Multi-Modal Retinal Diabetic Retinopathy Dataset (24,460 images, `cc-by`)
- [x_pcr](./x_pcr.md): X-PCR Ophthalmology Progressive Clinical Reasoning Benchmark (18,735 rows, `unknown`)
- [olives](./olives.md): OLIVES: Ophthalmic Labels for Investigating Visual Eye Semantics (9,408 b scans, `cc-by`)
- [oct_fundus_dme_dr_mexico](./oct_fundus_dme_dr_mexico.md): OCT and Eye Fundus Dataset for DME and DR (2,661 images, `unknown`)
- [grape](./grape.md): GRAPE: Glaucoma Real-world Appraisal Progression Ensemble (1,115 examinations, `cc0`)
