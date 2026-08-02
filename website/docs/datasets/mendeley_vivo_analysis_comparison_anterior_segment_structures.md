---
id: mendeley_vivo_analysis_comparison_anterior_segment_structures
title: "In Vivo Analysis and Comparison of Anterior Segment Structures of Both Eyes in Unilateral Herpetic Anterior Uveitis"
sidebar_label: mendeley_vivo_analysis_comparison_anterior_segment_structures
description: "Eye-level anterior-segment sd-oct structural measurements from People with unilateral herpetic anterior uveitis and fellow-eye comparison."
tags: ["oct", "cc-by", "mendeley", "segmentation", "resource-role-current-dataset", "dataset-family-mendeley-vivo-analysis-comparison-anterior-segment-structures"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# In Vivo Analysis and Comparison of Anterior Segment Structures of Both Eyes in Unilateral Herpetic Anterior Uveitis

Eye-level anterior-segment sd-oct structural measurements from People with unilateral herpetic anterior uveitis and fellow-eye comparison.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mendeley_vivo_analysis_comparison_anterior_segment_structures` |
| **Full name** | In Vivo Analysis and Comparison of Anterior Segment Structures of Both Eyes in Unilateral Herpetic Anterior Uveitis |
| **Primary category** | `oct` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `mendeley_vivo_analysis_comparison_anterior_segment_structures` |
| **Contained modalities** | oct |
| **Tasks** | segmentation |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | Creative Commons Attribution 4.0 International |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `unknown` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Mendeley Data |
| **Availability** | `available` (checked 2026-08-02) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

No reproducible primary item count was exposed for the cataloged source version.

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Human provenance: People with unilateral herpetic anterior uveitis and fellow-eye comparison. Source-review finding: Current listing not independently retrievable; source abstract describes Schlemm-canal and iris features measured with AS SD-OCT.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mendeley_vivo_analysis_comparison_anterior_segment_structures --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download mendeley_vivo_analysis_comparison_anterior_segment_structures --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mendeley_vivo_analysis_comparison_anterior_segment_structures')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/hmz2cz3jcg/1)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/hmz2cz3jcg)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mendeley_vivo_analysis_comparison_anterior_segment_structures,
  title  = { In Vivo Analysis and Comparison of Anterior Segment Structures of Both Eyes in Unilateral Herpetic Anterior Uveitis },
  note   = { In Vivo Analysis and Comparison of Anterior Segment Structures of Both Eyes in Unilateral Herpetic Anterior Uveitis. Mendeley Data, V1. doi:10.17632/hmz2cz3jcg.1 },
  url    = { https://data.mendeley.com/datasets/hmz2cz3jcg/1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
In Vivo Analysis and Comparison of Anterior Segment Structures of Both Eyes in Unilateral Herpetic Anterior Uveitis. Mendeley Data, V1. doi:10.17632/hmz2cz3jcg.1.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Creative Commons Attribution 4.0 International
- **Normalized category:** `cc-by`
- **Apparent scope:** `unknown`
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
