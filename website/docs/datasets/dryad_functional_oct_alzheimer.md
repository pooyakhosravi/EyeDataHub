---
id: dryad_functional_oct_alzheimer
title: "Functional OCT Retinal Response Dataset"
sidebar_label: dryad_functional_oct_alzheimer
description: "Repeated light/dark SD-OCT acquisitions and retinal reflectivity profiles from healthy, neuromyelitis-optica, and Alzheimer groups."
tags: ["oct", "cc0", "dryad", "classification", "registration", "regression"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Functional OCT Retinal Response Dataset

Repeated light/dark SD-OCT acquisitions and retinal reflectivity profiles from healthy, neuromyelitis-optica, and Alzheimer groups.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_functional_oct_alzheimer` |
| **Full name** | Functional OCT Retinal Response Dataset |
| **Primary category** | `oct` |
| **Contained modalities** | oct |
| **Tasks** | classification, registration, regression |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 2.058 GB |
| **Source-stated terms** | CC0 1.0 |
| **Normalized terms** | `cc0` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Dryad |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `guided_instructions_only` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Additional | 1 | `deposited_files` | RAR archive in the current Dryad version The source describes four experiments but does not expose a single non-overlapping participant or image total. | `current_deposit_file_listing` | [https://doi.org/10.5061/dryad.msbcc2ftc](https://doi.org/10.5061/dryad.msbcc2ftc) |
| Additional | 8 | `group_enrollments` | Healthy young-adult experiment | `official_source_description` | [https://doi.org/10.5061/dryad.msbcc2ftc](https://doi.org/10.5061/dryad.msbcc2ftc) |
| Additional | 3 | `group_enrollments` | Aquaporin-4 antibody experiment | `official_source_description` | [https://doi.org/10.5061/dryad.msbcc2ftc](https://doi.org/10.5061/dryad.msbcc2ftc) |
| Additional | 14 | `group_enrollments` | Early-onset Alzheimer group | `official_source_description` | [https://doi.org/10.5061/dryad.msbcc2ftc](https://doi.org/10.5061/dryad.msbcc2ftc) |
| Additional | 14 | `group_enrollments` | Age-matched control group Group counts are not summed because cross-experiment overlap was not resolved. | `official_source_description` | [https://doi.org/10.5061/dryad.msbcc2ftc](https://doi.org/10.5061/dryad.msbcc2ftc) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> The release contains repeated acquisitions across four experiments; source groups include eight young adults, three participants with aquaporin-4 antibodies, 14 early-onset Alzheimer patients, and 14 age-matched controls. Group overlap is not assumed in num_samples. Dryad declines whole-version archive assembly for this record; EyeDataHub therefore directs users to the official landing page. Authenticated per-file API transfer is available when a user configures DRYAD_TOKEN.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_functional_oct_alzheimer --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download dryad_functional_oct_alzheimer --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_functional_oct_alzheimer')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.msbcc2ftc](https://doi.org/10.5061/dryad.msbcc2ftc)

**Source-term evidence:** [https://doi.org/10.5061/dryad.msbcc2ftc](https://doi.org/10.5061/dryad.msbcc2ftc)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_functional_oct_alzheimer,
  title  = { Functional OCT Retinal Response Dataset },
  note   = { Bissig D, Zhou C, Le V, Bernard J. A practical approach to functional optical coherence tomography shows abnormal retinal responses in Alzheimer's disease. Dryad. 2020. doi:10.5061/dryad.msbcc2ftc },
  year   = { 2020 },
  url    = { https://doi.org/10.5061/dryad.msbcc2ftc },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Bissig D, Zhou C, Le V, Bernard J. A practical approach to functional optical coherence tomography shows abnormal retinal responses in Alzheimer's disease. Dryad. 2020. doi:10.5061/dryad.msbcc2ftc
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC0 1.0
- **Normalized category:** `cc0`
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
