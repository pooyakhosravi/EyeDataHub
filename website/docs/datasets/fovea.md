---
id: fovea
title: "FOVEA: Pre/Intra-Operative Fundus + Biomicroscopy"
sidebar_label: fovea
description: "40 patients with paired pre-operative fundus images and intra-operative biomicroscopy video clips. Annotated for optic disc and vessel segmentation across domains."
tags: ["multimodal", "fundus", "surgical_video", "cc-by", "figshare", "segmentation"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# FOVEA: Pre/Intra-Operative Fundus + Biomicroscopy

40 patients with paired pre-operative fundus images and intra-operative biomicroscopy video clips. Annotated for optic disc and vessel segmentation across domains.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `fovea` |
| **Full name** | FOVEA: Pre/Intra-Operative Fundus + Biomicroscopy |
| **Primary category** | `multimodal` |
| **Contained modalities** | fundus, surgical_video |
| **Tasks** | segmentation |
| **Samples** | 40 |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 4.0 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Figshare |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Notes

> Unique pre-op/intra-op paired modality — only public example.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download fovea --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download fovea --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('fovea')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.6084/m9.figshare.28329338](https://doi.org/10.6084/m9.figshare.28329338)

**Source-term evidence:** [https://doi.org/10.6084/m9.figshare.28329338](https://doi.org/10.6084/m9.figshare.28329338)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{fovea,
  title  = { FOVEA: Pre/Intra-Operative Fundus + Biomicroscopy },
  note   = { Ravasio et al., 'FOVEA: paired pre- and intra-operative fundus + biomicroscopy', Scientific Data 2025. doi:10.1038/s41597-025-04965-2 },
  year   = { 2025 },
  url    = { https://doi.org/10.6084/m9.figshare.28329338 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Ravasio et al., 'FOVEA: paired pre- and intra-operative fundus + biomicroscopy', Scientific Data 2025. doi:10.1038/s41597-025-04965-2
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC BY 4.0
- **Normalized category:** `cc-by`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Standard label without an explicit NC clause; not a permission finding

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Related datasets with shared modalities

- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 records, `unknown`)
- [ophora](./ophora.md): Ophora-160K: Ophthalmic Surgical Video Instruction Dataset (160,185 records, `unknown`)
- [airogs](./airogs.md): AIROGS: AI for Robust Glaucoma Screening (113,893 records, `cc-by-nc-nd`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 records, `unknown`)
- [justraigs](./justraigs.md): JustRAIGS: Just Referral AI Glaucoma Screening Dataset (101,442 records, `cc-by-nc-nd`)
- [eyepacs](./eyepacs.md): EyePACS — Diabetic Retinopathy Detection (Kaggle 2015) (88,702 records, `research-only`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (58,036 records, `mit`)
- [angioreport](./angioreport.md): AngioReport Fundus Angiography Report Dataset (55,361 records, `unknown`)
