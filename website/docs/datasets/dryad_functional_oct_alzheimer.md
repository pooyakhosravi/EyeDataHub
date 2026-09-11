---
id: dryad_functional_oct_alzheimer
title: "Functional OCT Retinal Response Dataset"
sidebar_label: dryad_functional_oct_alzheimer
description: "Repeated light/dark SD-OCT acquisitions and retinal reflectivity profiles from healthy, neuromyelitis-optica, and Alzheimer groups."
tags: ["oct", "cc0", "dryad", "classification", "registration", "regression", "resource-role-current-dataset", "dataset-family-dryad-functional-oct-alzheimer"]
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
| **Publication date** | 2019-11-18 |
| **Date basis** | Initial dataset release |
| **Publication date precision** | day |
| **Publication date evidence** | [datadryad.org/api](https://datadryad.org/api/v2/datasets/doi%3A10.5061%2Fdryad.msbcc2ftc/versions) |
| **Publication date source field** | versions[versionNumber=4].publicationDate (earliest public version) |
| **Publication date reviewed** | 2026-09-11 |
| **Date notes** | - |
| **Primary category** | `oct` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `dryad_functional_oct_alzheimer` |
| **Contained modalities** | oct |
| **Tasks** | classification, registration, regression |
| **Primary reported quantity** | 40 participants |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.843520297 GB |
| **Source-stated terms** | CC0 1.0 |
| **Normalized terms** | `cc0` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Dryad |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `end_to_end_tested` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 40 | `participants` | Unique participant identifiers across the two deposited profile tables in Dryad version 6 The Experiment 2 table has four participants, three of whom also occur in the Experiments 1, 3, and 4 table. | `current_deposit_table` | [https://doi.org/10.5061/dryad.msbcc2ftc](https://doi.org/10.5061/dryad.msbcc2ftc) |
| Additional | 1,370 | `rows` | Processed retinal-reflectivity profile rows across the two deposited tables | `current_deposit_table` | [https://doi.org/10.5061/dryad.msbcc2ftc](https://doi.org/10.5061/dryad.msbcc2ftc) |
| Additional | 432 | `images` | ANALYZE-format .img objects in the Dryad version 6 archive This file count includes raw, manually marked, flattened, and spatially normalized representations and is not an independent acquisition count. | `current_deposit_file_listing` | [https://doi.org/10.5061/dryad.msbcc2ftc](https://doi.org/10.5061/dryad.msbcc2ftc) |
| Additional | 1 | `deposited_files` | RAR archive in Dryad version 6 | `current_deposit_file_listing` | [https://doi.org/10.5061/dryad.msbcc2ftc](https://doi.org/10.5061/dryad.msbcc2ftc) |
| Additional | 8 | `group_enrollments` | Healthy young-adult experiment | `official_source_description` | [https://doi.org/10.5061/dryad.msbcc2ftc](https://doi.org/10.5061/dryad.msbcc2ftc) |
| Additional | 3 | `group_enrollments` | Aquaporin-4 antibody experiment | `official_source_description` | [https://doi.org/10.5061/dryad.msbcc2ftc](https://doi.org/10.5061/dryad.msbcc2ftc) |
| Additional | 14 | `group_enrollments` | Early-onset Alzheimer group | `official_source_description` | [https://doi.org/10.5061/dryad.msbcc2ftc](https://doi.org/10.5061/dryad.msbcc2ftc) |
| Additional | 14 | `group_enrollments` | Age-matched control group Group counts are not summed because cross-experiment overlap was not resolved. | `official_source_description` | [https://doi.org/10.5061/dryad.msbcc2ftc](https://doi.org/10.5061/dryad.msbcc2ftc) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> The current version contains 40 unique participant identifiers across four experiments, including overlapping experiment groups. Dryad file downloads require a user-supplied API token; EyeDataHub can also obtain a fresh token from locally configured Dryad client credentials.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_functional_oct_alzheimer --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dryad_functional_oct_alzheimer --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_functional_oct_alzheimer')
print(preflight_dataset(ds, './data'))  # no download
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
