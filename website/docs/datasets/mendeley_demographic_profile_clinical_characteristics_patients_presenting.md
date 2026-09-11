---
id: mendeley_demographic_profile_clinical_characteristics_patients_presenting
title: "Demographic profile and clinical characteristics of patients presenting with acute ocular burns"
sidebar_label: mendeley_demographic_profile_clinical_characteristics_patients_presenting
description: "Patient-level demographic and clinical tabular observations from Patients with acute ocular burns presenting at two South Indian tertiary eye-care centres during 2016-2020."
tags: ["tabular", "cc-by", "mendeley", "measurement", "resource-role-current-dataset", "dataset-family-mendeley-demographic-profile-clinical-characteristics-patients-presenting"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Demographic profile and clinical characteristics of patients presenting with acute ocular burns

Patient-level demographic and clinical tabular observations from Patients with acute ocular burns presenting at two South Indian tertiary eye-care centres during 2016-2020.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mendeley_demographic_profile_clinical_characteristics_patients_presenting` |
| **Full name** | Demographic profile and clinical characteristics of patients presenting with acute ocular burns |
| **Publication date** | 2023-04-24 |
| **Date basis** | Initial dataset release |
| **Publication date precision** | day |
| **Publication date evidence** | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/hwnm88jyzg/1) |
| **Publication date source field** | citation_publication_date |
| **Publication date reviewed** | 2026-09-11 |
| **Date notes** | Official Mendeley Data version-1 page Published metadata; JSON-LD datePublished agrees. Version 1 is the initial public deposit. |
| **Primary category** | `tabular` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `mendeley_demographic_profile_clinical_characteristics_patients_presenting` |
| **Contained modalities** | tabular |
| **Tasks** | measurement |
| **Primary reported quantity** | 2 documents |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | Creative Commons Attribution 4.0 International |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `unknown` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Mendeley Data |
| **Availability** | `available` (checked 2026-08-02) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 2 | `documents` | Source-stated quantity Preserved from the source-confirmation record. | `official_source_description` | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/hwnm88jyzg) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Human provenance: Patients with acute ocular burns presenting at two South Indian tertiary eye-care centres during 2016-2020. Source-review finding: Source description states two Excel sheets, one adult and one paediatric, containing descriptive data of all presenting patients.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mendeley_demographic_profile_clinical_characteristics_patients_presenting --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download mendeley_demographic_profile_clinical_characteristics_patients_presenting --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mendeley_demographic_profile_clinical_characteristics_patients_presenting')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/hwnm88jyzg/1)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/hwnm88jyzg)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mendeley_demographic_profile_clinical_characteristics_patients_presenting,
  title  = { Demographic profile and clinical characteristics of patients presenting with acute ocular burns },
  note   = { Demographic profile and clinical characteristics of patients presenting with acute ocular burns. Mendeley Data, V1. doi:10.17632/hwnm88jyzg.1 },
  url    = { https://data.mendeley.com/datasets/hwnm88jyzg/1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Demographic profile and clinical characteristics of patients presenting with acute ocular burns. Mendeley Data, V1. doi:10.17632/hwnm88jyzg.1.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Creative Commons Attribution 4.0 International
- **Normalized category:** `cc-by`
- **Apparent scope:** `unknown`
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
