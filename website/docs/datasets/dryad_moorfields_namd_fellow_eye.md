---
id: dryad_moorfields_namd_fellow_eye
title: "Moorfields nAMD Fellow-Eye Dataset"
sidebar_label: dryad_moorfields_namd_fellow_eye
description: "The Moorfields nAMD fellow-eye dataset is direct human retinal-disease longitudinal outcome data."
tags: ["tabular", "cc0", "dryad", "prognosis", "regression", "documented-relationship", "relationship-same_or_overlapping_cohort_as"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Moorfields nAMD Fellow-Eye Dataset

The Moorfields nAMD fellow-eye dataset is direct human retinal-disease longitudinal outcome data.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_moorfields_namd_fellow_eye` |
| **Full name** | Moorfields nAMD Fellow-Eye Dataset |
| **Primary category** | `tabular` |
| **Contained modalities** | tabular |
| **Tasks** | prognosis, regression |
| **Primary reported quantity** | 6,265 participants |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.031128168 GB |
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
| Primary | 6,265 | `participants` | Source-described Moorfields nAMD database patients Source-stated quantity; Dryad file count is separate metadata and is not a scientific sample count. | `official_source_description` | [https://doi.org/10.5061/dryad.4mw6m906b](https://doi.org/10.5061/dryad.4mw6m906b) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Scope screen: core_add. Current Dryad v7 file listing: 2 files, 15505168 bytes. Related catalog records dryad_namd_oct_quant and dryad_namd_visual_prediction have a documented shared source cohort but distinct outcome tasks.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- This record has a documented `same or overlapping cohort as` relationship with [dryad_moorfields_amd_1_2_year](./dryad_moorfields_amd_1_2_year.md): Both official deposits name the Moorfields AMD database and report overlapping 2008-2018 extraction windows. ([evidence](https://doi.org/10.5061/dryad.4mw6m906b))
- This record has a documented `same or overlapping cohort as` relationship with [dryad_namd_oct_quant](./dryad_namd_oct_quant.md): The official records identify the Moorfields AMD database and overlapping treatment or extraction periods. ([evidence](https://doi.org/10.5061/dryad.2rbnzs7m4))
- This record has a documented `same or overlapping cohort as` relationship with [dryad_namd_visual_prediction](./dryad_namd_visual_prediction.md): The official records identify the Moorfields AMD database and overlapping treatment or extraction periods. ([evidence](https://doi.org/10.5061/dryad.573n5tb5d))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_moorfields_namd_fellow_eye --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dryad_moorfields_namd_fellow_eye --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_moorfields_namd_fellow_eye')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.4mw6m906b](https://doi.org/10.5061/dryad.4mw6m906b)

**Source-term evidence:** [https://doi.org/10.5061/dryad.4mw6m906b](https://doi.org/10.5061/dryad.4mw6m906b)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_moorfields_namd_fellow_eye,
  title  = { Moorfields nAMD Fellow-Eye Dataset },
  note   = { Fasler, Katrin, Fu, Dun Jack, Moraes, Gabriella, Wagner, Siegfried K, Gokhale, Eesha, Kortuem, Karsten U, Chopra, Reena, Faes, Livia, Preston, Gabriella, Pontikos, Nikolas, Patel, Praveen J, Tufail, Adnan, Lee, Aaron Y, Balaskas, Konstantinos, and Keane, Pearse A. Data from: The Moorfields AMD database report 2 - fellow eye involvement with neovascular age-related macular degeneration. Dryad. 2020. doi:10.5061/dryad.4mw6m906b },
  year   = { 2020 },
  url    = { https://doi.org/10.5061/dryad.4mw6m906b },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Fasler, Katrin, Fu, Dun Jack, Moraes, Gabriella, Wagner, Siegfried K, Gokhale, Eesha, Kortuem, Karsten U, Chopra, Reena, Faes, Livia, Preston, Gabriella, Pontikos, Nikolas, Patel, Praveen J, Tufail, Adnan, Lee, Aaron Y, Balaskas, Konstantinos, and Keane, Pearse A. Data from: The Moorfields AMD database report 2 - fellow eye involvement with neovascular age-related macular degeneration. Dryad. 2020. doi:10.5061/dryad.4mw6m906b
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
- [dryad_canine_pra_cea_genotypes](./dryad_canine_pra_cea_genotypes.md): Canine PRA and CEA Genotype Dataset (86,667 records, `cc0`)
- [brset_mbrset_embeddings](./brset_mbrset_embeddings.md): Embedding-Based Representations for BRSET and mBRSET (53,188 embedding vectors, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [oculoscope](./oculoscope.md): OculoScope: Fairer AI in Ophthalmology Dataset (16,530 images, `cc-by`)
- [dryad_r7s04](./dryad_r7s04.md): Data from: Prevalence of depression, anxiety, adjustment disorders, and somatoform disorders in patients with age-related macular degeneration in Germany (15,160 participants, `cc0`)
- [fairvlmed](./fairvlmed.md): FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset (10,000 images, `cc-by-nc-nd`)
- [leops_erg](./leops_erg.md): LEOPs Light-Adapted Electroretinogram and Oscillatory Potentials Dataset (9,743 signals, `cc-by`)
