---
id: dryad_sf7m0cggh
title: "Robust semi-automatic vessel tracing in the human retinal image by an instance segmentation neural network"
sidebar_label: dryad_sf7m0cggh
description: "Official Dryad deposit of source-described retinal vessel annotation data for the associated study."
tags: ["fundus", "tabular", "cc0", "dryad", "segmentation", "vessel_analysis", "documented-relationship", "relationship-derived_from"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Robust semi-automatic vessel tracing in the human retinal image by an instance segmentation neural network

Official Dryad deposit of source-described retinal vessel annotation data for the associated study.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_sf7m0cggh` |
| **Full name** | Robust semi-automatic vessel tracing in the human retinal image by an instance segmentation neural network |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus, tabular |
| **Tasks** | segmentation, vessel_analysis |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.000117131 GB |
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

No reproducible primary item count was exposed for the cataloged source version.

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Scope screen: core_add. Current Dryad v9 file listing: 5 files, 117131 bytes. Relationship clue: derived_from existing catalog record drive.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- This record is `derived from` [drive](./drive.md): The official current file listing names DRIVE trace annotations and result files. ([evidence](https://datadryad.org/api/v2/versions/353579/files))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_sf7m0cggh --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dryad_sf7m0cggh --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_sf7m0cggh')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.sf7m0cggh](https://doi.org/10.5061/dryad.sf7m0cggh)

**Source-term evidence:** [https://doi.org/10.5061/dryad.sf7m0cggh](https://doi.org/10.5061/dryad.sf7m0cggh)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_sf7m0cggh,
  title  = { Robust semi-automatic vessel tracing in the human retinal image by an instance segmentation neural network },
  note   = { Chen Siyi, Hoang Linh, Yi Ji, Kashani Amir. Robust semi-automatic vessel tracing in the human retinal image by an instance segmentation neural network. Dryad. 2025. doi:10.5061/dryad.sf7m0cggh },
  year   = { 2025 },
  url    = { https://doi.org/10.5061/dryad.sf7m0cggh },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Chen Siyi, Hoang Linh, Yi Ji, Kashani Amir. Robust semi-automatic vessel tracing in the human retinal image by an instance segmentation neural network. Dryad. 2025. doi:10.5061/dryad.sf7m0cggh
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

- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [fairvlmed](./fairvlmed.md): FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset (10,000 images, `cc-by-nc-nd`)
- [olives](./olives.md): OLIVES: Ophthalmic Labels for Investigating Visual Eye Semantics (9,408 b scans, `cc-by`)
- [fprm_retina](./fprm_retina.md): FPRM Multimodal Eye Imaging and Psychological Assessment Dataset (3,361 images, `research-only`)
- [grape](./grape.md): GRAPE: Glaucoma Real-world Appraisal Progression Ensemble (1,115 examinations, `cc0`)
- [papila](./papila.md): PAPILA: Glaucoma Fundus Dataset with Clinical Data (488 images, `cc-by`)
- [dryad_diabetes_retinal_capillary](./dryad_diabetes_retinal_capillary.md): Diabetes Retinal Capillary Rarefaction Dataset (73 participants, `cc0`)
- [ocular_chat_vqa](./ocular_chat_vqa.md): OcularChat-VQA: AREDS-Derived Patient-Physician Dialogue Dataset (844,000 records, `cc-by-nc-sa`)
