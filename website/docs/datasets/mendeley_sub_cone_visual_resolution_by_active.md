---
id: mendeley_sub_cone_visual_resolution_by_active
title: "Data from: Sub-cone visual resolution by active, adaptive sampling in the human foveola"
sidebar_label: mendeley_sub_cone_visual_resolution_by_active
description: "Human/derived image or image-annotation observations. from 16 human participants, both eyes."
tags: ["tabular", "cc-by", "mendeley", "prediction", "resource-role-current-dataset", "dataset-family-mendeley-sub-cone-visual-resolution-by-active"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Data from: Sub-cone visual resolution by active, adaptive sampling in the human foveola

Human/derived image or image-annotation observations. from 16 human participants, both eyes.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mendeley_sub_cone_visual_resolution_by_active` |
| **Full name** | Data from: Sub-cone visual resolution by active, adaptive sampling in the human foveola |
| **Primary category** | `tabular` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `mendeley_sub_cone_visual_resolution_by_active` |
| **Contained modalities** | tabular |
| **Tasks** | prediction |
| **Primary reported quantity** | 16 participants |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Mendeley Data |
| **Availability** | `available` (checked 2026-08-02) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 16 | `participants` | Source-stated quantity Preserved from the source-confirmation record. | `official_source_description` | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/zp6d5w8kdv) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Human provenance: 16 human participants, both eyes. Source-review finding: Cone-mosaic images/coordinates, retinal locations and eye-motion trajectories; MATLAB plotting code is ancillary. Potential overlap with related foveola studies was not resolved; no record-to-record edge is encoded.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mendeley_sub_cone_visual_resolution_by_active --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download mendeley_sub_cone_visual_resolution_by_active --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mendeley_sub_cone_visual_resolution_by_active')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/zp6d5w8kdv/1)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/zp6d5w8kdv)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mendeley_sub_cone_visual_resolution_by_active,
  title  = { Data from: Sub-cone visual resolution by active, adaptive sampling in the human foveola },
  note   = { Data from: Sub-cone visual resolution by active, adaptive sampling in the human foveola. Mendeley Data, V1. doi:10.17632/zp6d5w8kdv.1 },
  url    = { https://data.mendeley.com/datasets/zp6d5w8kdv/1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Data from: Sub-cone visual resolution by active, adaptive sampling in the human foveola. Mendeley Data, V1. doi:10.17632/zp6d5w8kdv.1.
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
