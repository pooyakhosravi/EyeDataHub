---
id: synthetic_retinal_oct_biomarkers
title: "Synthetic Retinal OCT Biomarker Dataset"
sidebar_label: synthetic_retinal_oct_biomarkers
description: "Synthetic OCT images for the four Kermany diagnostic classes."
tags: ["oct", "unknown", "huggingface", "classification", "documented-relationship", "relationship-derived_from"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Synthetic Retinal OCT Biomarker Dataset

Synthetic OCT images for the four Kermany diagnostic classes.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `synthetic_retinal_oct_biomarkers` |
| **Full name** | Synthetic Retinal OCT Biomarker Dataset |
| **Primary category** | `oct` |
| **Contained modalities** | oct |
| **Tasks** | classification |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | Unknown; no dataset license stated |
| **Normalized terms** | `unknown` |
| **Descriptive screening label** | Unknown or unclear; do not assume permission |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | HuggingFace Hub |
| **Availability** | `available` (checked 2026-08-02) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

No reproducible primary item count was exposed for the cataloged source version.

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Synthetic derivative of the cataloged Kermany OCT dataset; source reports four class archives but no image count.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- This record is `derived from` [kermany_oct](./kermany_oct.md): The official dataset card documents the Kermany retinal OCT collection as the source for the four synthetic diagnostic classes. ([evidence](https://huggingface.co/datasets/serag-ai/Synthetic-Ophthalmology-Images))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download synthetic_retinal_oct_biomarkers --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download synthetic_retinal_oct_biomarkers --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('synthetic_retinal_oct_biomarkers')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [huggingface.co/datasets](https://huggingface.co/datasets/serag-ai/Synthetic-Ophthalmology-Images)

**Source-term evidence:** [huggingface.co/datasets](https://huggingface.co/datasets/serag-ai/Synthetic-Ophthalmology-Images)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{synthetic_retinal_oct_biomarkers,
  title  = { Synthetic Retinal OCT Biomarker Dataset },
  note   = { Repository dataset record. serag-ai/Synthetic-Ophthalmology-Images },
  url    = { https://huggingface.co/datasets/serag-ai/Synthetic-Ophthalmology-Images },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Repository dataset record. serag-ai/Synthetic-Ophthalmology-Images.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Unknown; no dataset license stated
- **Normalized category:** `unknown`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Unknown or unclear; do not assume permission

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [syn_oct](./syn_oct.md): SYN-OCT Synthetic Glaucoma OCT Dataset (200,000 images, `cc-by`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (103,959 images, `mit`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [kermany_oct](./kermany_oct.md): Kermany OCT 2018: Retinal OCT Image Classification (84,484 images, `cc-by`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [harvard_fairvision](./harvard_fairvision.md): Harvard-FairVision (AMD + DR + Glaucoma, paired SLO + OCT) (30,000 participants, `cc-by-nc-nd`)
- [mario](./mario.md): MARIO: AMD-Progression Longitudinal OCT (MICCAI 2024) (30,000 images, `cc-by`)
- [mmrdr](./mmrdr.md): MMRDR: Multi-Modal Retinal Diabetic Retinopathy Dataset (24,460 images, `cc-by`)
