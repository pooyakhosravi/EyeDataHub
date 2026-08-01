---
id: fprm_retina
title: "FPRM Multimodal Eye Imaging and Psychological Assessment Dataset"
sidebar_label: fprm_retina
description: "Fundus photography, multispectral and functional retinal imaging, retinal blood-flow and pupillary-light videos, retina-characteristic labels, quality labels, demographics, and psychological assessmen"
tags: ["multimodal", "fundus", "retinal_oximetry", "pupillometry", "tabular", "research-only", "manual", "classification", "quality_assessment", "regression"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# FPRM Multimodal Eye Imaging and Psychological Assessment Dataset

Fundus photography, multispectral and functional retinal imaging, retinal blood-flow and pupillary-light videos, retina-characteristic labels, quality labels, demographics, and psychological assessments.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `fprm_retina` |
| **Full name** | FPRM Multimodal Eye Imaging and Psychological Assessment Dataset |
| **Primary category** | `multimodal` |
| **Contained modalities** | fundus, retinal_oximetry, pupillometry, tabular |
| **Tasks** | classification, quality_assessment, regression |
| **Primary reported quantity** | 3,361 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | Synapse Data Use Agreement; research use only |
| **Normalized terms** | `research-only` |
| **Descriptive screening label** | Research or challenge restriction recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `controlled_or_manual` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `manual_access_blocked` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 3,361 | `images` | Fundus photographs | `associated_publication` | [https://doi.org/10.1038/s41597-024-03690-6](https://doi.org/10.1038/s41597-024-03690-6) |
| Additional | 1,683 | `participants` | Participants contributing fundus photographs | `associated_publication` | [https://doi.org/10.1038/s41597-024-03690-6](https://doi.org/10.1038/s41597-024-03690-6) |
| Additional | 384 | `participants` | Participants contributing additional multimodal imaging This group is not added to the fundus cohort because overlap is not resolved here. | `associated_publication` | [https://doi.org/10.1038/s41597-024-03690-6](https://doi.org/10.1038/s41597-024-03690-6) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Scientific Data descriptor reports 3,361 fundus photographs from 1,683 participants plus multimodal imaging from 384 participants; Synapse access requires certified account and completed data-use agreement.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# This route requires upstream human action; no transfer starts.
eyehub download fprm_retina --data-dir ./data --dry-run --json
# Follow the official instructions shown by preflight.
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('fprm_retina')
print(preflight_dataset(ds, './data'))  # returns manual_access_blocked
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.7303/syn61672643](https://doi.org/10.7303/syn61672643)

**Source-term evidence:** [https://doi.org/10.7303/syn61672643](https://doi.org/10.7303/syn61672643)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{fprm_retina,
  title  = { FPRM Multimodal Eye Imaging and Psychological Assessment Dataset },
  note   = { Zhang G, Qu Y, Zhang Y, et al. Multimodal Eye Imaging, Retina Characteristics, and Psychological Assessment Dataset. Scientific Data. 2024;11:836. doi:10.1038/s41597-024-03690-6 },
  year   = { 2024 },
  url    = { https://doi.org/10.7303/syn61672643 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Zhang G, Qu Y, Zhang Y, et al. Multimodal Eye Imaging, Retina Characteristics, and Psychological Assessment Dataset. Scientific Data. 2024;11:836. doi:10.1038/s41597-024-03690-6
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Synapse Data Use Agreement; research use only
- **Normalized category:** `research-only`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Research or challenge restriction recorded; check source

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [fairvlmed](./fairvlmed.md): FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset (10,000 images, `cc-by-nc-nd`)
- [olives](./olives.md): OLIVES: Ophthalmic Labels for Investigating Visual Eye Semantics (9,408 b scans, `cc-by`)
- [grape](./grape.md): GRAPE: Glaucoma Real-world Appraisal Progression Ensemble (1,115 examinations, `cc0`)
- [papila](./papila.md): PAPILA: Glaucoma Fundus Dataset with Clinical Data (488 images, `cc-by`)
- [ocular_chat_vqa](./ocular_chat_vqa.md): OcularChat-VQA: AREDS-Derived Patient-Physician Dialogue Dataset (844,000 records, `cc-by-nc-sa`)
- [airogs](./airogs.md): AIROGS: AI for Robust Glaucoma Screening (113,893 images, `cc-by-nc-nd`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (103,959 images, `mit`)
