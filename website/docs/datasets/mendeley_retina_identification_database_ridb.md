---
id: mendeley_retina_identification_database_ridb
title: "Retina Identification Database (RIDB)"
sidebar_label: mendeley_retina_identification_database_ridb
description: "Human/derived image or image-annotation observations. from 20 individuals without retinal disease."
tags: ["multimodal", "fundus", "tabular", "cc-by", "mendeley", "measurement", "resource-role-current-dataset", "dataset-family-mendeley-retina-identification-database-ridb"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Retina Identification Database (RIDB)

Human/derived image or image-annotation observations. from 20 individuals without retinal disease.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mendeley_retina_identification_database_ridb` |
| **Full name** | Retina Identification Database (RIDB) |
| **Primary category** | `multimodal` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `mendeley_retina_identification_database_ridb` |
| **Contained modalities** | fundus, tabular |
| **Tasks** | measurement |
| **Primary reported quantity** | 100 images |
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
| Primary | 100 | `images` | Source-stated quantity Preserved from the source-confirmation record. | `official_source_description` | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/tjw3zwntv6) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Human provenance: 20 individuals without retinal disease. Source-review finding: Fundus JPEG image collection captured with TOPCON-TRC.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mendeley_retina_identification_database_ridb --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download mendeley_retina_identification_database_ridb --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mendeley_retina_identification_database_ridb')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/tjw3zwntv6/2)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/tjw3zwntv6)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mendeley_retina_identification_database_ridb,
  title  = { Retina Identification Database (RIDB) },
  note   = { Retina Identification Database (RIDB). Mendeley Data, V2. doi:10.17632/tjw3zwntv6.2 },
  url    = { https://data.mendeley.com/datasets/tjw3zwntv6/2 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Retina Identification Database (RIDB). Mendeley Data, V2. doi:10.17632/tjw3zwntv6.2.
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

- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [fairvlmed](./fairvlmed.md): FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset (10,000 images, `cc-by-nc-nd`)
- [olives](./olives.md): OLIVES: Ophthalmic Labels for Investigating Visual Eye Semantics (9,408 b scans, `cc-by`)
- [fprm_retina](./fprm_retina.md): FPRM Multimodal Eye Imaging and Psychological Assessment Dataset (3,361 images, `research-only`)
- [grape](./grape.md): GRAPE: Glaucoma Real-world Appraisal Progression Ensemble (1,115 examinations, `cc0`)
- [papila](./papila.md): PAPILA: Glaucoma Fundus Dataset with Clinical Data (488 images, `cc-by`)
- [dryad_diabetes_retinal_capillary](./dryad_diabetes_retinal_capillary.md): Diabetes Retinal Capillary Rarefaction Dataset (73 participants, `cc0`)
- [ocular_chat_vqa](./ocular_chat_vqa.md): OcularChat-VQA: AREDS-Derived Patient-Physician Dialogue Dataset (844,000 records, `cc-by-nc-sa`)
