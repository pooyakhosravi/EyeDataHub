---
id: anterior_segment_smile
title: "Anterior Segment Parameters After SMILE Surgery"
sidebar_label: anterior_segment_smile
description: "Tabular anterior-segment and ocular-biometry measurements before and after SMILE surgery, including slit-lamp examination, Pentacam, and IOLMaster variables."
tags: ["tabular", "cc-by", "mendeley", "regression"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Anterior Segment Parameters After SMILE Surgery

Tabular anterior-segment and ocular-biometry measurements before and after SMILE surgery, including slit-lamp examination, Pentacam, and IOLMaster variables.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `anterior_segment_smile` |
| **Full name** | Anterior Segment Parameters After SMILE Surgery |
| **Primary category** | `tabular` |
| **Contained modalities** | tabular |
| **Tasks** | regression |
| **Primary reported quantity** | 69 eyes |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.01 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Mendeley Data |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 69 | `eyes` | Source-described cohort: 69 eyes from 35 participants The current Mendeley v1 deposit does not expose an enumerable row count. | `associated_publication` | [https://doi.org/10.21203/rs.3.rs-8639765/v1](https://doi.org/10.21203/rs.3.rs-8639765/v1) |
| Additional | 35 | `participants` | Source-described cohort | `associated_publication` | [https://doi.org/10.21203/rs.3.rs-8639765/v1](https://doi.org/10.21203/rs.3.rs-8639765/v1) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Source page reports clinical examination, Pentacam, and IOLMaster measurements; sample count was not exposed during curation.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download anterior_segment_smile --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download anterior_segment_smile --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('anterior_segment_smile')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/vkdxsnhkrm/1)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/vkdxsnhkrm/1)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{anterior_segment_smile,
  title  = { Anterior Segment Parameters After SMILE Surgery },
  note   = { Sun C. Anterior Segment Parameter Analysis After SMILE Surgery and Its Impact on the Calculation of Effective Intraocular Lens Position. Mendeley Data, V1, 2026. doi:10.17632/vkdxsnhkrm.1 },
  year   = { 2026 },
  url    = { https://data.mendeley.com/datasets/vkdxsnhkrm/1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Sun C. Anterior Segment Parameter Analysis After SMILE Surgery and Its Impact on the Calculation of Effective Intraocular Lens Position. Mendeley Data, V1, 2026. doi:10.17632/vkdxsnhkrm.1
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
- [fairvlmed](./fairvlmed.md): FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset (10,000 images, `cc-by-nc-nd`)
- [leops_erg](./leops_erg.md): LEOPs Light-Adapted Electroretinogram and Oscillatory Potentials Dataset (9,743 signals, `cc-by`)
- [olives](./olives.md): OLIVES: Ophthalmic Labels for Investigating Visual Eye Semantics (9,408 b scans, `cc-by`)
- [fprm_retina](./fprm_retina.md): FPRM Multimodal Eye Imaging and Psychological Assessment Dataset (3,361 images, `research-only`)
