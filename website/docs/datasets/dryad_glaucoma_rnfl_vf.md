---
id: dryad_glaucoma_rnfl_vf
title: "RNFL and Visual-Field Glaucoma Diagnosis Dataset"
sidebar_label: dryad_glaucoma_rnfl_vf
description: "Clinical records combining retinal nerve fiber layer, visual-field, corneal-thickness, and intraocular-pressure features."
tags: ["tabular", "visual_field", "cc0", "dryad", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# RNFL and Visual-Field Glaucoma Diagnosis Dataset

Clinical records combining retinal nerve fiber layer, visual-field, corneal-thickness, and intraocular-pressure features.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_glaucoma_rnfl_vf` |
| **Full name** | RNFL and Visual-Field Glaucoma Diagnosis Dataset |
| **Primary category** | `tabular` |
| **Contained modalities** | tabular, visual_field |
| **Tasks** | classification |
| **Primary reported quantity** | 499 records |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 3.2e-05 GB |
| **Source-stated terms** | CC0 1.0 |
| **Normalized terms** | `cc0` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Dryad |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `end_to_end_tested` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 499 | `records` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [https://doi.org/10.5061/dryad.q6ft5](https://doi.org/10.5061/dryad.q6ft5) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> The source reports 399 training/validation cases and 100 held-out test cases. The archive contains examination-record features rather than raw OCT or visual-field images.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_glaucoma_rnfl_vf --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dryad_glaucoma_rnfl_vf --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_glaucoma_rnfl_vf')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.q6ft5](https://doi.org/10.5061/dryad.q6ft5)

**Source-term evidence:** [https://doi.org/10.5061/dryad.q6ft5](https://doi.org/10.5061/dryad.q6ft5)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_glaucoma_rnfl_vf,
  title  = { RNFL and Visual-Field Glaucoma Diagnosis Dataset },
  note   = { Development of machine learning models for diagnosis of glaucoma. Dryad. 2018. doi:10.5061/dryad.q6ft5 },
  year   = { 2018 },
  url    = { https://doi.org/10.5061/dryad.q6ft5 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Development of machine learning models for diagnosis of glaucoma. Dryad. 2018. doi:10.5061/dryad.q6ft5
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC0 1.0
- **Normalized category:** `cc0`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Standard label without an explicit NC clause; not a permission finding

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [fairvlmed](./fairvlmed.md): FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset (10,000 images, `cc-by-nc-nd`)
- [grape](./grape.md): GRAPE: Glaucoma Real-world Appraisal Progression Ensemble (1,115 examinations, `cc0`)
- [harvard_gdp](./harvard_gdp.md): Harvard GDP: Glaucoma Detection and Progression Dataset (1,000 participants, `cc-by-nc-nd`)
- [dryad_myopia_glaucoma_visual_field](./dryad_myopia_glaucoma_visual_field.md): Myopia and Glaucoma Visual Field Prognosis Dataset (270 eyes, `cc0`)
- [dryad_xgxd254pk](./dryad_xgxd254pk.md): Supporting information for: Discrimination ability of central visual field testing using stimulus size I, II, and III and relationship with macular ganglion cell thickness in chiasmal compression (60 eyes, `cc0`)
- [ocular_chat_vqa](./ocular_chat_vqa.md): OcularChat-VQA: AREDS-Derived Patient-Physician Dialogue Dataset (844,000 records, `cc-by-nc-sa`)
- [brset_mbrset_embeddings](./brset_mbrset_embeddings.md): Embedding-Based Representations for BRSET and mBRSET (53,188 embedding vectors, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
