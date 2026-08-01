---
id: oct5k
title: "OCT5k: Multi-Disease Retinal Layer Annotations"
sidebar_label: oct5k
description: "1,672 OCT B-scans from AMD, DME, and healthy controls with 5,016 multi-grader layer annotations + lesion detection labels."
tags: ["oct", "cc0", "figshare", "segmentation", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# OCT5k: Multi-Disease Retinal Layer Annotations

1,672 OCT B-scans from AMD, DME, and healthy controls with 5,016 multi-grader layer annotations + lesion detection labels.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `oct5k` |
| **Full name** | OCT5k: Multi-Disease Retinal Layer Annotations |
| **Primary category** | `oct` |
| **Contained modalities** | oct |
| **Tasks** | segmentation, classification |
| **Samples** | 1,672 |
| **Classes** | 8 (Not reported) |
| **Splits** | all |
| **Size** | 0.05 GB |
| **Source-stated terms** | CC0 1.0 |
| **Normalized terms** | `cc0` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Figshare |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `end_to_end_tested` |
| **Legacy sample-loader status** | Metadata and access only |


## Notes

> UCL Research Data Repository — Figshare-backed, free download.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download oct5k --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download oct5k --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('oct5k')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5522/04/22128671](https://doi.org/10.5522/04/22128671)

**Source-term evidence:** [https://doi.org/10.5522/04/22128671](https://doi.org/10.5522/04/22128671)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{oct5k,
  title  = { OCT5k: Multi-Disease Retinal Layer Annotations },
  note   = { Morano et al., 'OCT5k: a dataset of multi-disease and multi-graded annotations for retinal layers in OCT images', Scientific Data 2024. doi:10.1038/s41597-024-04259-z },
  year   = { 2024 },
  url    = { https://doi.org/10.5522/04/22128671 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Morano et al., 'OCT5k: a dataset of multi-disease and multi-graded annotations for retinal layers in OCT images', Scientific Data 2024. doi:10.1038/s41597-024-04259-z
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC0 1.0
- **Normalized category:** `cc0`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Standard label without an explicit NC clause; not a permission finding

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Related datasets with shared modalities

- [syn_oct](./syn_oct.md): SYN-OCT Synthetic Glaucoma OCT Dataset (200,000 records, `cc-by`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 records, `unknown`)
- [kermany_oct](./kermany_oct.md): Kermany OCT 2018: Retinal OCT Image Classification (84,484 records, `cc-by`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (58,036 records, `mit`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 records, `unknown`)
- [harvard_fairvision](./harvard_fairvision.md): Harvard-FairVision (AMD + DR + Glaucoma, paired SLO + OCT) (30,000 records, `cc-by-nc-nd`)
- [mario](./mario.md): MARIO: AMD-Progression Longitudinal OCT (MICCAI 2024) (30,000 records, `cc-by`)
- [mmrdr](./mmrdr.md): MMRDR: Multi-Modal Retinal Diabetic Retinopathy Dataset (24,460 records, `cc-by`)
