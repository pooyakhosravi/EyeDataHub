---
id: syn_oct
title: "SYN-OCT Synthetic Glaucoma OCT Dataset"
sidebar_label: syn_oct
description: "Synthetic circumpapillary OCT images for healthy and glaucomatous eyes with retinal-layer masks and RNFL thickness values."
tags: ["oct", "cc-by", "zenodo", "classification", "segmentation", "regression", "resource-role-current-dataset", "dataset-family-syn-oct"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# SYN-OCT Synthetic Glaucoma OCT Dataset

Synthetic circumpapillary OCT images for healthy and glaucomatous eyes with retinal-layer masks and RNFL thickness values.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `syn_oct` |
| **Full name** | SYN-OCT Synthetic Glaucoma OCT Dataset |
| **First published** | 2025-09-18 |
| **Publication date precision** | day |
| **Publication date evidence** | [zenodo.org/api](https://zenodo.org/api/records/17151869) |
| **Publication date source field** | metadata.publication_date (earliest public Zenodo version) |
| **Publication date reviewed** | 2026-09-11 |
| **Primary category** | `oct` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `syn_oct` |
| **Contained modalities** | oct |
| **Tasks** | classification, segmentation, regression |
| **Primary reported quantity** | 200,000 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 3.255 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Zenodo |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 200,000 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [https://doi.org/10.5281/zenodo.17151869](https://doi.org/10.5281/zenodo.17151869) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Contains 100,000 synthetic glaucoma and 100,000 synthetic normal circumpapillary OCT images. No real patient images are released.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download syn_oct --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download syn_oct --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('syn_oct')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5281/zenodo.17151869](https://doi.org/10.5281/zenodo.17151869)

**Source-term evidence:** [https://doi.org/10.5281/zenodo.17151869](https://doi.org/10.5281/zenodo.17151869)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{syn_oct,
  title  = { SYN-OCT Synthetic Glaucoma OCT Dataset },
  note   = { SYN-OCT: A synthetic dataset of ocular optical coherence tomography images from healthy and glaucoma eyes. Scientific Data. 2026. doi:10.1038/s41597-026-06946-5 },
  year   = { 2026 },
  url    = { https://doi.org/10.5281/zenodo.17151869 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
SYN-OCT: A synthetic dataset of ocular optical coherence tomography images from healthy and glaucoma eyes. Scientific Data. 2026. doi:10.1038/s41597-026-06946-5
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

- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (103,959 images, `mit`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [kermany_oct](./kermany_oct.md): Kermany OCT 2018: Retinal OCT Image Classification (84,484 images, `cc-by`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [harvard_fairvision](./harvard_fairvision.md): Harvard-FairVision (AMD + DR + Glaucoma, paired SLO + OCT) (30,000 participants, `cc-by-nc-nd`)
- [mario](./mario.md): MARIO: AMD-Progression Longitudinal OCT (MICCAI 2024) (30,000 images, `cc-by`)
- [mmrdr](./mmrdr.md): MMRDR: Multi-Modal Retinal Diabetic Retinopathy Dataset (24,460 images, `cc-by`)
- [oct_c8](./oct_c8.md): Retinal OCT-C8: 8-Class OCT Classification (24,000 images, `unknown`)
