---
id: duke_amd_chiu
title: "Duke AMD Pathology OCT Segmentation Dataset"
sidebar_label: duke_amd_chiu
description: "Twenty OCT volumes with 220 selected B-scans from eyes with non-neovascular AMD, drusen, and geographic atrophy, including manual and automated pathology markings."
tags: ["oct", "unknown", "manual", "segmentation", "measurement"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Duke AMD Pathology OCT Segmentation Dataset

Twenty OCT volumes with 220 selected B-scans from eyes with non-neovascular AMD, drusen, and geographic atrophy, including manual and automated pathology markings.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `duke_amd_chiu` |
| **Full name** | Duke AMD Pathology OCT Segmentation Dataset |
| **Primary category** | `oct` |
| **Contained modalities** | oct |
| **Tasks** | segmentation, measurement |
| **Primary reported quantity** | 20 volumes |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.54 GB |
| **Source-stated terms** | Unknown; no named dataset license on the official page |
| **Normalized terms** | `unknown` |
| **Descriptive screening label** | Unknown or unclear; do not assume permission |
| **Terms scope** | `unknown` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `guided_instructions_only` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 20 | `volumes` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [people.duke.edu/~sf59](https://people.duke.edu/~sf59/Chiu_IOVS_2011_dataset.htm) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> The sample count is the 20-eye main validation cohort. The archive also contains ten reproducibility volumes acquired at 0 and 90 degrees and MATLAB display scripts. The source page does not state a named reuse license.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download duke_amd_chiu --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download duke_amd_chiu --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('duke_amd_chiu')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [people.duke.edu/~sf59](https://people.duke.edu/~sf59/Chiu_IOVS_2011_dataset.htm)

**Source-term evidence:** [people.duke.edu/~sf59](https://people.duke.edu/~sf59/Chiu_IOVS_2011_dataset.htm)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{duke_amd_chiu,
  title  = { Duke AMD Pathology OCT Segmentation Dataset },
  note   = { Chiu SJ, Izatt JA, O'Connell RV, Winter KP, Toth CA, Farsiu S. Validated automatic segmentation of AMD pathology including drusen and geographic atrophy in SD-OCT images. Invest Ophthalmol Vis Sci. 2012;53:53-61. doi:10.1167/iovs.11-7640 },
  year   = { 2012 },
  url    = { https://people.duke.edu/~sf59/Chiu_IOVS_2011_dataset.htm },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Chiu SJ, Izatt JA, O'Connell RV, Winter KP, Toth CA, Farsiu S. Validated automatic segmentation of AMD pathology including drusen and geographic atrophy in SD-OCT images. Invest Ophthalmol Vis Sci. 2012;53:53-61. doi:10.1167/iovs.11-7640
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Unknown; no named dataset license on the official page
- **Normalized category:** `unknown`
- **Apparent scope:** `unknown`
- **Descriptive screening label:** Unknown or unclear; do not assume permission

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
