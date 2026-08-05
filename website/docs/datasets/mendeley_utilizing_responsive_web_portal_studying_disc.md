---
id: mendeley_utilizing_responsive_web_portal_studying_disc
title: "Data for: Utilizing A Responsive Web Portal For Studying Disc Tracing Agreement in Retinal Images"
sidebar_label: mendeley_utilizing_responsive_web_portal_studying_disc
description: "Observation-level source data, annotations, or signals. from Uses human retinal-image benchmarks; it contributes clinician disc tracings."
tags: ["oct", "cc-by", "mendeley", "segmentation", "resource-role-annotation-layer", "dataset-family-mendeley-utilizing-responsive-web-portal-studying-disc", "documented-relationship", "relationship-derived_from"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Data for: Utilizing A Responsive Web Portal For Studying Disc Tracing Agreement in Retinal Images

Observation-level source data, annotations, or signals. from Uses human retinal-image benchmarks; it contributes clinician disc tracings.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mendeley_utilizing_responsive_web_portal_studying_disc` |
| **Full name** | Data for: Utilizing A Responsive Web Portal For Studying Disc Tracing Agreement in Retinal Images |
| **Primary category** | `oct` |
| **Resource role** | `annotation_layer` |
| **Dataset family** | `mendeley_utilizing_responsive_web_portal_studying_disc` |
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

> Human provenance: Uses human retinal-image benchmarks; it contributes clinician disc tracings. Source-review finding: Two ZIP archives of original and ellipse-fitted disc tracings.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- This record is `derived from` [drishti_gs](./drishti_gs.md): The Mendeley deposit is a distinct annotation and task layer built from DRISHTI-GS fundus images. ([evidence](https://data.mendeley.com/datasets/7xv5rzxgrh))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mendeley_utilizing_responsive_web_portal_studying_disc --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download mendeley_utilizing_responsive_web_portal_studying_disc --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mendeley_utilizing_responsive_web_portal_studying_disc')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/7xv5rzxgrh/1)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/7xv5rzxgrh)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mendeley_utilizing_responsive_web_portal_studying_disc,
  title  = { Data for: Utilizing A Responsive Web Portal For Studying Disc Tracing Agreement in Retinal Images },
  note   = { Data for: Utilizing A Responsive Web Portal For Studying Disc Tracing Agreement in Retinal Images. Mendeley Data, V1. doi:10.17632/7xv5rzxgrh.1 },
  url    = { https://data.mendeley.com/datasets/7xv5rzxgrh/1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Data for: Utilizing A Responsive Web Portal For Studying Disc Tracing Agreement in Retinal Images. Mendeley Data, V1. doi:10.17632/7xv5rzxgrh.1.
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
