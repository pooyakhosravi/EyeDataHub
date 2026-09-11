---
id: dryad_brvo_bevacizumab_multimodal
title: "BRVO Bevacizumab Multimodal Dataset"
sidebar_label: dryad_brvo_bevacizumab_multimodal
description: "The 27-eye BRVO archive contains named OCT, fluorescein, and mfERG research objects for retinal treatment analysis."
tags: ["multimodal", "oct", "fundus_angiography", "electrophysiology", "cc0", "dryad", "regression", "measurement", "resource-role-current-dataset", "dataset-family-dryad-brvo-bevacizumab-multimodal"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# BRVO Bevacizumab Multimodal Dataset

The 27-eye BRVO archive contains named OCT, fluorescein, and mfERG research objects for retinal treatment analysis.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_brvo_bevacizumab_multimodal` |
| **Full name** | BRVO Bevacizumab Multimodal Dataset |
| **Publication date** | 2017-08-30 |
| **Date basis** | Initial dataset release |
| **Publication date precision** | day |
| **Publication date evidence** | [datadryad.org/api](https://datadryad.org/api/v2/datasets/doi%3A10.5061%2Fdryad.3cp54) |
| **Publication date source field** | publicationDate |
| **Publication date reviewed** | 2026-09-11 |
| **Date notes** | Official Dryad API v2 publicationDate; current record version 1 and later lastModificationDate do not replace the publication date. |
| **Primary category** | `multimodal` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `dryad_brvo_bevacizumab_multimodal` |
| **Contained modalities** | oct, fundus_angiography, electrophysiology |
| **Tasks** | regression, measurement |
| **Primary reported quantity** | 27 eyes |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.061464266 GB |
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
| Primary | 27 | `eyes` | Source-described treatment-naive BRVO eyes Source-stated quantity; Dryad file count is separate metadata and is not a scientific sample count. | `official_source_description` | [https://doi.org/10.5061/dryad.3cp54](https://doi.org/10.5061/dryad.3cp54) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Scope screen: core_add. Current Dryad v1 file listing: 3 files, 61440336 bytes.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_brvo_bevacizumab_multimodal --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dryad_brvo_bevacizumab_multimodal --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_brvo_bevacizumab_multimodal')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.3cp54](https://doi.org/10.5061/dryad.3cp54)

**Source-term evidence:** [https://doi.org/10.5061/dryad.3cp54](https://doi.org/10.5061/dryad.3cp54)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_brvo_bevacizumab_multimodal,
  title  = { BRVO Bevacizumab Multimodal Dataset },
  note   = { Rishi, Pukhraj, Raka, Neha, and Rishi, Ekta. Data from: Analysis of potential ischemic effect of intravitreal bevacizumab on unaffected retina in treatment-naïve macular edema due to branch retinal vein occlusion: a prospective, interventional case-series. Dryad. 2017. doi:10.5061/dryad.3cp54 },
  year   = { 2017 },
  url    = { https://doi.org/10.5061/dryad.3cp54 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Rishi, Pukhraj, Raka, Neha, and Rishi, Ekta. Data from: Analysis of potential ischemic effect of intravitreal bevacizumab on unaffected retina in treatment-naïve macular edema due to branch retinal vein occlusion: a prospective, interventional case-series. Dryad. 2017. doi:10.5061/dryad.3cp54
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

- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [x_pcr](./x_pcr.md): X-PCR Ophthalmology Progressive Clinical Reasoning Benchmark (18,735 rows, `unknown`)
- [ophthalvqa](./ophthalvqa.md): OphthalVQA Dataset (600 question answer pairs, `cc-by`)
- [mm_retinal_reason](./mm_retinal_reason.md): MM-Retinal-Reason: Ophthalmology Multimodal Reasoning Dataset (130 question answer pairs, `unknown`)
- [syn_oct](./syn_oct.md): SYN-OCT Synthetic Glaucoma OCT Dataset (200,000 images, `cc-by`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (103,959 images, `mit`)
- [kermany_oct](./kermany_oct.md): Kermany OCT 2018: Retinal OCT Image Classification (84,484 images, `cc-by`)
- [angioreport](./angioreport.md): AngioReport Fundus Angiography Report Dataset (55,361 images, `unknown`)
