---
id: oct_fundus_dme_dr_mexico
title: "OCT and Eye Fundus Dataset for DME and DR"
sidebar_label: oct_fundus_dme_dr_mexico
description: "Linked color fundus and macular OCT images for diabetic macular edema and diabetic retinopathy classification, with CSV labels and shared patient/eye/image nomenclature."
tags: ["multimodal", "fundus", "oct", "unknown", "github", "classification", "grading", "resource-role-current-dataset", "dataset-family-oct-fundus-dme-dr-mexico"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# OCT and Eye Fundus Dataset for DME and DR

Linked color fundus and macular OCT images for diabetic macular edema and diabetic retinopathy classification, with CSV labels and shared patient/eye/image nomenclature.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `oct_fundus_dme_dr_mexico` |
| **Full name** | OCT and Eye Fundus Dataset for DME and DR |
| **Publication date** | Unknown |
| **Date basis** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Date notes** | - |
| **Primary category** | `multimodal` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `oct_fundus_dme_dr_mexico` |
| **Contained modalities** | fundus, oct |
| **Tasks** | classification, grading |
| **Primary reported quantity** | 2,661 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.49 GB |
| **Source-stated terms** | Unknown; no repository license declared |
| **Normalized terms** | `unknown` |
| **Descriptive screening label** | Unknown or unclear; do not assume permission |
| **Terms scope** | `unknown` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | GitHub |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `end_to_end_tested` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 2,661 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [github.com/Traslational-Visual-Health-Laboratory](https://github.com/Traslational-Visual-Health-Laboratory/OCT-AND-EYE-FUNDUS-DATASET) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Repository README reports 1,548 fundus images and 1,113 OCT images collected between 2015 and 2022, with DME and DR labels in CSV files and shared patient/eye/modality/sample identifiers. No license file is declared; verify source terms before reuse.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download oct_fundus_dme_dr_mexico --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download oct_fundus_dme_dr_mexico --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('oct_fundus_dme_dr_mexico')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [github.com/Traslational-Visual-Health-Laboratory](https://github.com/Traslational-Visual-Health-Laboratory/OCT-AND-EYE-FUNDUS-DATASET)

**Source-term evidence:** [github.com/Traslational-Visual-Health-Laboratory](https://github.com/Traslational-Visual-Health-Laboratory/OCT-AND-EYE-FUNDUS-DATASET)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{oct_fundus_dme_dr_mexico,
  title  = { OCT and Eye Fundus Dataset for DME and DR },
  note   = { Hughes Cano JA, Olivares Pinto U, Thebault SC. Dataset of Eye Fundus and OCT Images for the study of Diabetic Macular Edema and Diabetic Retinopathy. GitHub repository, accessed 2026 },
  year   = { 2026 },
  url    = { https://github.com/Traslational-Visual-Health-Laboratory/OCT-AND-EYE-FUNDUS-DATASET },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Hughes Cano JA, Olivares Pinto U, Thebault SC. Dataset of Eye Fundus and OCT Images for the study of Diabetic Macular Edema and Diabetic Retinopathy. GitHub repository, accessed 2026.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Unknown; no repository license declared
- **Normalized category:** `unknown`
- **Apparent scope:** `unknown`
- **Descriptive screening label:** Unknown or unclear; do not assume permission

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (103,959 images, `mit`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [harvard_fairvision](./harvard_fairvision.md): Harvard-FairVision (AMD + DR + Glaucoma, paired SLO + OCT) (30,000 participants, `cc-by-nc-nd`)
- [mmrdr](./mmrdr.md): MMRDR: Multi-Modal Retinal Diabetic Retinopathy Dataset (24,460 images, `cc-by`)
- [x_pcr](./x_pcr.md): X-PCR Ophthalmology Progressive Clinical Reasoning Benchmark (18,735 rows, `unknown`)
- [olives](./olives.md): OLIVES: Ophthalmic Labels for Investigating Visual Eye Semantics (9,408 b scans, `cc-by`)
- [grape](./grape.md): GRAPE: Glaucoma Real-world Appraisal Progression Ensemble (1,115 examinations, `cc0`)
