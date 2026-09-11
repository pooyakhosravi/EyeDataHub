---
id: tunisian_retinal_oct_multidisease
title: "Tunisian Retinal OCT Multi-Disease Dataset"
sidebar_label: tunisian_retinal_oct_multidisease
description: "Clinically acquired retinal OCT images for AMD, DME, rhegmatogenous retinal detachment, and normal classification."
tags: ["oct", "cc-by", "manual", "classification", "resource-role-current-dataset", "dataset-family-tunisian-retinal-oct-multidisease"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Tunisian Retinal OCT Multi-Disease Dataset

Clinically acquired retinal OCT images for AMD, DME, rhegmatogenous retinal detachment, and normal classification.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `tunisian_retinal_oct_multidisease` |
| **Full name** | Tunisian Retinal OCT Multi-Disease Dataset |
| **First published** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Primary category** | `oct` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `tunisian_retinal_oct_multidisease` |
| **Contained modalities** | oct |
| **Tasks** | classification |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `controlled_or_manual` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-08-02) |
| **Acquisition support** | `manual_access_blocked` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

No reproducible primary item count was exposed for the cataloged source version.

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Official record has no public files; access is by approved signed data-use agreement.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# This route requires upstream human action; no transfer starts.
eyehub download tunisian_retinal_oct_multidisease --data-dir ./data --dry-run --json
# Follow the official instructions shown by preflight.
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('tunisian_retinal_oct_multidisease')
print(preflight_dataset(ds, './data'))  # returns manual_access_blocked
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.6084/m9.figshare.31385596.v3](https://doi.org/10.6084/m9.figshare.31385596.v3)

**Source-term evidence:** [https://doi.org/10.6084/m9.figshare.31385596.v3](https://doi.org/10.6084/m9.figshare.31385596.v3)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{tunisian_retinal_oct_multidisease,
  title  = { Tunisian Retinal OCT Multi-Disease Dataset },
  note   = { Repository dataset record. 10.6084/m9.figshare.31385596.v3 },
  url    = { https://doi.org/10.6084/m9.figshare.31385596.v3 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Repository dataset record. 10.6084/m9.figshare.31385596.v3.
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

- [syn_oct](./syn_oct.md): SYN-OCT Synthetic Glaucoma OCT Dataset (200,000 images, `cc-by`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (103,959 images, `mit`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [kermany_oct](./kermany_oct.md): Kermany OCT 2018: Retinal OCT Image Classification (84,484 images, `cc-by`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [harvard_fairvision](./harvard_fairvision.md): Harvard-FairVision (AMD + DR + Glaucoma, paired SLO + OCT) (30,000 participants, `cc-by-nc-nd`)
- [mario](./mario.md): MARIO: AMD-Progression Longitudinal OCT (MICCAI 2024) (30,000 images, `cc-by`)
- [mmrdr](./mmrdr.md): MMRDR: Multi-Modal Retinal Diabetic Retinopathy Dataset (24,460 images, `cc-by`)
