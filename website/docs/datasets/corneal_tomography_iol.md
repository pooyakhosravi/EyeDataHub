---
id: corneal_tomography_iol
title: "Multi-Parameter Corneal Tomography Dataset for IOL Selection"
sidebar_label: corneal_tomography_iol
description: "Pentacam-derived corneal tomography variables for intraocular-lens and corneal subtype modeling."
tags: ["tabular", "cc-by", "mendeley", "classification", "regression", "resource-role-current-dataset", "dataset-family-corneal-tomography-iol"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Multi-Parameter Corneal Tomography Dataset for IOL Selection

Pentacam-derived corneal tomography variables for intraocular-lens and corneal subtype modeling.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `corneal_tomography_iol` |
| **Full name** | Multi-Parameter Corneal Tomography Dataset for IOL Selection |
| **First published** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Primary category** | `tabular` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `corneal_tomography_iol` |
| **Contained modalities** | tabular |
| **Tasks** | classification, regression |
| **Primary reported quantity** | 61 eyes |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.01 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Mendeley Data |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 61 | `eyes` | One structured row per eye | `official_source_description` | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/wddj7bh9p9/1) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download corneal_tomography_iol --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download corneal_tomography_iol --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('corneal_tomography_iol')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/wddj7bh9p9/1)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/wddj7bh9p9/1)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{corneal_tomography_iol,
  title  = { Multi-Parameter Corneal Tomography Dataset for IOL Selection },
  note   = { Multi-parameter corneal tomography dataset for IOL selection. Mendeley Data, V1, 2025. doi:10.17632/wddj7bh9p9.1 },
  year   = { 2025 },
  url    = { https://data.mendeley.com/datasets/wddj7bh9p9/1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Multi-parameter corneal tomography dataset for IOL selection. Mendeley Data, V1, 2025. doi:10.17632/wddj7bh9p9.1
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

- [ocular_chat_vqa](./ocular_chat_vqa.md): OcularChat-VQA: AREDS-Derived Patient-Physician Dialogue Dataset (844,000 records, `cc-by-nc-sa`)
- [brset_mbrset_embeddings](./brset_mbrset_embeddings.md): Embedding-Based Representations for BRSET and mBRSET (53,188 embedding vectors, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [oculoscope](./oculoscope.md): OculoScope: Fairer AI in Ophthalmology Dataset (16,530 images, `cc-by`)
- [dryad_r7s04](./dryad_r7s04.md): Data from: Prevalence of depression, anxiety, adjustment disorders, and somatoform disorders in patients with age-related macular degeneration in Germany (15,160 participants, `cc0`)
- [fairvlmed](./fairvlmed.md): FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset (10,000 images, `cc-by-nc-nd`)
- [leops_erg](./leops_erg.md): LEOPs Light-Adapted Electroretinogram and Oscillatory Potentials Dataset (9,743 signals, `cc-by`)
- [dryad_icmr_eye_see_cataract](./dryad_icmr_eye_see_cataract.md): ICMR EYE SEE Cataract and Sun Exposure Dataset (9,735 participants, `cc0`)
