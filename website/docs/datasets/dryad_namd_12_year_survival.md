---
id: dryad_namd_12_year_survival
title: "Insights from survival analyses during 12 years of anti-VEGF therapy for neovascular age-related macular degeneration"
sidebar_label: dryad_namd_12_year_survival
description: "The anonymized 7,802-eye human AMD CSV is a clearly defined long-term ophthalmic survival resource."
tags: ["tabular", "cc0", "dryad", "survival_analysis", "resource-role-current-dataset", "dataset-family-dryad-namd-12-year-survival"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Insights from survival analyses during 12 years of anti-VEGF therapy for neovascular age-related macular degeneration

The anonymized 7,802-eye human AMD CSV is a clearly defined long-term ophthalmic survival resource.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_namd_12_year_survival` |
| **Full name** | Insights from survival analyses during 12 years of anti-VEGF therapy for neovascular age-related macular degeneration |
| **Publication date** | 2020-11-05 |
| **Date basis** | Initial dataset release |
| **Publication date precision** | day |
| **Publication date evidence** | [datadryad.org/api](https://datadryad.org/api/v2/datasets/doi%3A10.5061%2Fdryad.nvx0k6dqg/versions) |
| **Publication date source field** | versions[versionNumber=4].publicationDate (earliest public version) |
| **Publication date reviewed** | 2026-09-11 |
| **Date notes** | - |
| **Primary category** | `tabular` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `dryad_namd_12_year_survival` |
| **Contained modalities** | tabular |
| **Tasks** | survival_analysis |
| **Primary reported quantity** | 7,802 eyes |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.020398805 GB |
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
| Primary | 7,802 | `eyes` | Source-stated primary resource quantity. Current official Dryad metadata. | `official_source_description` | [https://doi.org/10.5061/dryad.nvx0k6dqg](https://doi.org/10.5061/dryad.nvx0k6dqg) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Scope: core_add. Named file-level object: MEH_AMD_survivaloutcomes_database.csv plus README. Official Dryad metadata does not explicitly document cohort overlap with an existing catalog record; no relationship is asserted. Official Dryad API metadata and current file listing reviewed 2026-08-01.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_namd_12_year_survival --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dryad_namd_12_year_survival --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_namd_12_year_survival')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.nvx0k6dqg](https://doi.org/10.5061/dryad.nvx0k6dqg)

**Source-term evidence:** [https://doi.org/10.5061/dryad.nvx0k6dqg](https://doi.org/10.5061/dryad.nvx0k6dqg)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_namd_12_year_survival,
  title  = { Insights from survival analyses during 12 years of anti-VEGF therapy for neovascular age-related macular degeneration },
  note   = { Insights from survival analyses during 12 years of anti-VEGF therapy for neovascular age-related macular degeneration. Dryad Dataset. doi:10.5061/dryad.nvx0k6dqg },
  url    = { https://doi.org/10.5061/dryad.nvx0k6dqg },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Insights from survival analyses during 12 years of anti-VEGF therapy for neovascular age-related macular degeneration. Dryad Dataset. doi:10.5061/dryad.nvx0k6dqg.
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
- [dryad_icmr_eye_see_cataract](./dryad_icmr_eye_see_cataract.md): ICMR EYE SEE Cataract and Sun Exposure Dataset (9,735 participants, `cc0`)
