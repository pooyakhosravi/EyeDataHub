---
id: dryad_icmr_eye_see_cataract
title: "ICMR EYE SEE Cataract and Sun Exposure Dataset"
sidebar_label: dryad_icmr_eye_see_cataract
description: "The large Indian cataract/UV exposure survey is direct human ophthalmic epidemiology data."
tags: ["tabular", "cc0", "dryad", "regression", "resource-role-current-dataset", "dataset-family-dryad-icmr-eye-see-cataract"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# ICMR EYE SEE Cataract and Sun Exposure Dataset

The large Indian cataract/UV exposure survey is direct human ophthalmic epidemiology data.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_icmr_eye_see_cataract` |
| **Full name** | ICMR EYE SEE Cataract and Sun Exposure Dataset |
| **Primary category** | `tabular` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `dryad_icmr_eye_see_cataract` |
| **Contained modalities** | tabular |
| **Tasks** | regression |
| **Primary reported quantity** | 9,735 participants |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.003331471 GB |
| **Source-stated terms** | https://spdx.org/licenses/CC0-1.0.html |
| **Normalized terms** | `cc0` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Dryad |
| **Availability** | `available` (checked 2026-08-01) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 9,735 | `participants` | Source-described participants who underwent ophthalmic evaluation Source-stated quantity; Dryad file count is separate metadata and is not a scientific sample count. | `official_source_description` | [https://doi.org/10.5061/dryad.5qfttdz19](https://doi.org/10.5061/dryad.5qfttdz19) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Scope screen: core_add. Current Dryad v6 file listing: 2 files, 2438708 bytes.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_icmr_eye_see_cataract --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dryad_icmr_eye_see_cataract --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_icmr_eye_see_cataract')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.5qfttdz19](https://doi.org/10.5061/dryad.5qfttdz19)

**Source-term evidence:** [https://doi.org/10.5061/dryad.5qfttdz19](https://doi.org/10.5061/dryad.5qfttdz19)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_icmr_eye_see_cataract,
  title  = { ICMR EYE SEE Cataract and Sun Exposure Dataset },
  note   = { Vashist, Praveen, Tandon, Radhika, Murthy, GVS, Barua, CK, Deka, Dipali, Singh, Sachchidanand, Gupta, Vivek, Gupta, Noopur, Wadhwani, Meenakshi, Singh, Rashmi, and Vishwanath, K. Association of cataract and sun exposure in geographically diverse populations of India: the case study. first report of the ICMR-EYE SEE study group. Dryad. 2020. doi:10.5061/dryad.5qfttdz19 },
  year   = { 2020 },
  url    = { https://doi.org/10.5061/dryad.5qfttdz19 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Vashist, Praveen, Tandon, Radhika, Murthy, GVS, Barua, CK, Deka, Dipali, Singh, Sachchidanand, Gupta, Vivek, Gupta, Noopur, Wadhwani, Meenakshi, Singh, Rashmi, and Vishwanath, K. Association of cataract and sun exposure in geographically diverse populations of India: the case study. first report of the ICMR-EYE SEE study group. Dryad. 2020. doi:10.5061/dryad.5qfttdz19
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** https://spdx.org/licenses/CC0-1.0.html
- **Normalized category:** `cc0`
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
- [olives](./olives.md): OLIVES: Ophthalmic Labels for Investigating Visual Eye Semantics (9,408 b scans, `cc-by`)
