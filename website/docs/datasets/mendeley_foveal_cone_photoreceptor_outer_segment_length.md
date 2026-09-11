---
id: mendeley_foveal_cone_photoreceptor_outer_segment_length
title: "Foveal cone photoreceptor outer segment length and cone density"
sidebar_label: mendeley_foveal_cone_photoreceptor_outer_segment_length
description: "Observation-level source data, annotations, or signals. from Source describes human foveolar cone observations."
tags: ["oct", "cc-by", "mendeley", "segmentation", "resource-role-current-dataset", "dataset-family-mendeley-foveal-cone-photoreceptor-outer-segment-length"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Foveal cone photoreceptor outer segment length and cone density

Observation-level source data, annotations, or signals. from Source describes human foveolar cone observations.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mendeley_foveal_cone_photoreceptor_outer_segment_length` |
| **Full name** | Foveal cone photoreceptor outer segment length and cone density |
| **First published** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Primary category** | `oct` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `mendeley_foveal_cone_photoreceptor_outer_segment_length` |
| **Contained modalities** | oct |
| **Tasks** | segmentation |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Mendeley Data |
| **Availability** | `available` (checked 2026-08-02) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

No reproducible primary item count was exposed for the cataloged source version.

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Human provenance: Source describes human foveolar cone observations. Source-review finding: 66 files: 44 MAT, 19 TIF, two TXT, and one PNG. Potential overlap with related foveola studies was not resolved; no record-to-record edge is encoded.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mendeley_foveal_cone_photoreceptor_outer_segment_length --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download mendeley_foveal_cone_photoreceptor_outer_segment_length --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mendeley_foveal_cone_photoreceptor_outer_segment_length')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/89rykrg8j2/1)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/89rykrg8j2)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mendeley_foveal_cone_photoreceptor_outer_segment_length,
  title  = { Foveal cone photoreceptor outer segment length and cone density },
  note   = { Foveal cone photoreceptor outer segment length and cone density. Mendeley Data, V1. doi:10.17632/89rykrg8j2.1 },
  url    = { https://data.mendeley.com/datasets/89rykrg8j2/1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Foveal cone photoreceptor outer segment length and cone density. Mendeley Data, V1. doi:10.17632/89rykrg8j2.1.
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
