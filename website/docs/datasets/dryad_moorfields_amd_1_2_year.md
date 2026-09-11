---
id: dryad_moorfields_amd_1_2_year
title: "One and two year visual outcomes from the Moorfields age-related macular degeneration database: a retrospective cohort study and an open science resource"
sidebar_label: dryad_moorfields_amd_1_2_year
description: "The de-identified 8,174-eye Moorfields AMD CSV is an explicitly released human longitudinal outcome resource."
tags: ["tabular", "cc0", "dryad", "progression_analysis", "resource-role-current-dataset", "dataset-family-dryad-moorfields-amd-1-2-year", "documented-relationship", "relationship-same_or_overlapping_cohort_as"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# One and two year visual outcomes from the Moorfields age-related macular degeneration database: a retrospective cohort study and an open science resource

The de-identified 8,174-eye Moorfields AMD CSV is an explicitly released human longitudinal outcome resource.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_moorfields_amd_1_2_year` |
| **Full name** | One and two year visual outcomes from the Moorfields age-related macular degeneration database: a retrospective cohort study and an open science resource |
| **First published** | 2019-05-22 |
| **Publication date precision** | day |
| **Publication date evidence** | [datadryad.org/api](https://datadryad.org/api/v2/datasets/doi%3A10.5061%2Fdryad.97r9289/versions) |
| **Publication date source field** | versions[versionNumber=1].publicationDate (earliest public version) |
| **Publication date reviewed** | 2026-09-11 |
| **Primary category** | `tabular` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `dryad_moorfields_amd_1_2_year` |
| **Contained modalities** | tabular |
| **Tasks** | progression_analysis |
| **Primary reported quantity** | 8,174 eyes |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.010106429 GB |
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
| Primary | 8,174 | `eyes` | Source-stated primary resource quantity. Current official Dryad metadata. | `official_source_description` | [https://doi.org/10.5061/dryad.97r9289](https://doi.org/10.5061/dryad.97r9289) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Scope: core_add. Named file-level object: Moorfields_AMD_Database_1.csv plus README. Official Dryad metadata does not explicitly document cohort overlap with an existing catalog record; no relationship is asserted. Official Dryad API metadata and current file listing reviewed 2026-08-01.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- This record has a documented `same or overlapping cohort as` relationship with [dryad_moorfields_namd_fellow_eye](./dryad_moorfields_namd_fellow_eye.md): Both official deposits name the Moorfields AMD database and report overlapping 2008-2018 extraction windows. ([evidence](https://doi.org/10.5061/dryad.4mw6m906b))
- This record has a documented `same or overlapping cohort as` relationship with [dryad_namd_oct_quant](./dryad_namd_oct_quant.md): The official records identify the Moorfields AMD database and overlapping treatment or extraction periods. ([evidence](https://doi.org/10.5061/dryad.2rbnzs7m4))
- This record has a documented `same or overlapping cohort as` relationship with [dryad_namd_visual_prediction](./dryad_namd_visual_prediction.md): The official records identify the Moorfields AMD database and overlapping treatment or extraction periods. ([evidence](https://doi.org/10.5061/dryad.573n5tb5d))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_moorfields_amd_1_2_year --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dryad_moorfields_amd_1_2_year --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_moorfields_amd_1_2_year')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.97r9289](https://doi.org/10.5061/dryad.97r9289)

**Source-term evidence:** [https://doi.org/10.5061/dryad.97r9289](https://doi.org/10.5061/dryad.97r9289)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_moorfields_amd_1_2_year,
  title  = { One and two year visual outcomes from the Moorfields age-related macular degeneration database: a retrospective cohort study and an open science resource },
  note   = { One and two year visual outcomes from the Moorfields age-related macular degeneration database: a retrospective cohort study and an open science resource. Dryad Dataset. doi:10.5061/dryad.97r9289 },
  url    = { https://doi.org/10.5061/dryad.97r9289 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
One and two year visual outcomes from the Moorfields age-related macular degeneration database: a retrospective cohort study and an open science resource. Dryad Dataset. doi:10.5061/dryad.97r9289.
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
