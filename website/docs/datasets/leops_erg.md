---
id: leops_erg
title: "LEOPs Light-Adapted Electroretinogram and Oscillatory Potentials Dataset"
sidebar_label: leops_erg
description: "Light-adapted electroretinogram and oscillatory-potential waveform dataset from 253 pediatric participants, with structured JSON, tabular metadata, and electrode-position eye images."
tags: ["electrophysiology", "tabular", "cc-by", "mendeley", "classification", "regression", "resource-role-current-dataset", "dataset-family-leops-erg"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# LEOPs Light-Adapted Electroretinogram and Oscillatory Potentials Dataset

Light-adapted electroretinogram and oscillatory-potential waveform dataset from 253 pediatric participants, with structured JSON, tabular metadata, and electrode-position eye images.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `leops_erg` |
| **Full name** | LEOPs Light-Adapted Electroretinogram and Oscillatory Potentials Dataset |
| **Primary category** | `electrophysiology` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `leops_erg` |
| **Contained modalities** | electrophysiology, tabular |
| **Tasks** | classification, regression |
| **Primary reported quantity** | 9,743 signals |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
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
| Primary | 9,743 | `signals` | Averaged ERG and oscillatory-potential waveforms | `derived_from_reported_components` | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/w3yx7hdds7/1) |
| Additional | 253 | `participants` | Pediatric participants | `official_source_description` | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/w3yx7hdds7/1) |
| Additional | 558 | `images` | Electrode-position eye images | `official_source_description` | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/w3yx7hdds7/1) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Source reports 5,309 averaged ERG waveforms, 4,434 OP waveforms, 253 participant JSON files, and 558 electrode-position eye images.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download leops_erg --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download leops_erg --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('leops_erg')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/w3yx7hdds7/1)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/w3yx7hdds7/1)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{leops_erg,
  title  = { LEOPs Light-Adapted Electroretinogram and Oscillatory Potentials Dataset },
  note   = { Constable P, Thompson D, Lee I, Loh L, Zhdanov A, Kulyabin M, Maier A. Light-Adapted Electroretinogram and Oscillatory Potentials (LEOPs) Dataset for Autism Spectrum Disorder and Typically Developing Individuals. Mendeley Data, V1, 2026. doi:10.17632/w3yx7hdds7.1 },
  year   = { 2026 },
  url    = { https://data.mendeley.com/datasets/w3yx7hdds7/1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Constable P, Thompson D, Lee I, Loh L, Zhdanov A, Kulyabin M, Maier A. Light-Adapted Electroretinogram and Oscillatory Potentials (LEOPs) Dataset for Autism Spectrum Disorder and Typically Developing Individuals. Mendeley Data, V1, 2026. doi:10.17632/w3yx7hdds7.1
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

- [perg_ioba](./perg_ioba.md): PERG-IOBA Ocular Electrophysiology Dataset (1,354 signals, `odc-by`)
- [ocular_chat_vqa](./ocular_chat_vqa.md): OcularChat-VQA: AREDS-Derived Patient-Physician Dialogue Dataset (844,000 records, `cc-by-nc-sa`)
- [brset_mbrset_embeddings](./brset_mbrset_embeddings.md): Embedding-Based Representations for BRSET and mBRSET (53,188 embedding vectors, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [oculoscope](./oculoscope.md): OculoScope: Fairer AI in Ophthalmology Dataset (16,530 images, `cc-by`)
- [dryad_r7s04](./dryad_r7s04.md): Data from: Prevalence of depression, anxiety, adjustment disorders, and somatoform disorders in patients with age-related macular degeneration in Germany (15,160 participants, `cc0`)
- [fairvlmed](./fairvlmed.md): FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset (10,000 images, `cc-by-nc-nd`)
- [dryad_icmr_eye_see_cataract](./dryad_icmr_eye_see_cataract.md): ICMR EYE SEE Cataract and Sun Exposure Dataset (9,735 participants, `cc0`)
