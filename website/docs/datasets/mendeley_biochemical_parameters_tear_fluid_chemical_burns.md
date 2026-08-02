---
id: mendeley_biochemical_parameters_tear_fluid_chemical_burns
title: "Dataset of biochemical parameters of tear fluid in chemical burns"
sidebar_label: mendeley_biochemical_parameters_tear_fluid_chemical_burns
description: "Observation-level human or human-derived measurements/signals. from 110 chemical-burn patients (155 eyes) in Tashkent."
tags: ["tabular", "cc-by", "mendeley", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Dataset of biochemical parameters of tear fluid in chemical burns

Observation-level human or human-derived measurements/signals. from 110 chemical-burn patients (155 eyes) in Tashkent.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mendeley_biochemical_parameters_tear_fluid_chemical_burns` |
| **Full name** | Dataset of biochemical parameters of tear fluid in chemical burns |
| **Primary category** | `tabular` |
| **Contained modalities** | tabular |
| **Tasks** | classification |
| **Primary reported quantity** | 110 participants |
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
| Primary | 110 | `participants` | Source-stated quantity Preserved from the source-confirmation record. | `official_source_description` | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/zhk775h6n4) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Human provenance: 110 chemical-burn patients (155 eyes) in Tashkent. Source-review finding: Tear-fluid biochemical-parameter examination dataset.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mendeley_biochemical_parameters_tear_fluid_chemical_burns --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download mendeley_biochemical_parameters_tear_fluid_chemical_burns --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mendeley_biochemical_parameters_tear_fluid_chemical_burns')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/zhk775h6n4/1)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/zhk775h6n4)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mendeley_biochemical_parameters_tear_fluid_chemical_burns,
  title  = { Dataset of biochemical parameters of tear fluid in chemical burns },
  note   = { Dataset of biochemical parameters of tear fluid in chemical burns. Mendeley Data, V1. doi:10.17632/zhk775h6n4.1 },
  url    = { https://data.mendeley.com/datasets/zhk775h6n4/1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Dataset of biochemical parameters of tear fluid in chemical burns. Mendeley Data, V1. doi:10.17632/zhk775h6n4.1.
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
