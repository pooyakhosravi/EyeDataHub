---
id: dryad_aoslo_rpe
title: "AOSLO RPE Cell Morphometry and Cone Mosaic Dataset"
sidebar_label: dryad_aoslo_rpe
description: "Adaptive-optics scanning-light-ophthalmoscopy montages and regions of interest for RPE morphometry and cone-to-RPE analysis."
tags: ["adaptive_optics", "cc0", "dryad", "segmentation", "measurement"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# AOSLO RPE Cell Morphometry and Cone Mosaic Dataset

Adaptive-optics scanning-light-ophthalmoscopy montages and regions of interest for RPE morphometry and cone-to-RPE analysis.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_aoslo_rpe` |
| **Full name** | AOSLO RPE Cell Morphometry and Cone Mosaic Dataset |
| **Primary category** | `adaptive_optics` |
| **Contained modalities** | adaptive_optics |
| **Tasks** | segmentation, measurement |
| **Samples** | 10 |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.084 GB |
| **Source-stated terms** | CC0 1.0 |
| **Normalized terms** | `cc0` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Dryad |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `end_to_end_tested` |
| **Legacy sample-loader status** | Metadata and access only |


## Notes

> Contains one-eye data from 10 normal participants for short-wave autofluorescence and photoreceptor reflectance; infrared autofluorescence is available for seven participants with overlap.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_aoslo_rpe --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download dryad_aoslo_rpe --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_aoslo_rpe')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.b41j15h](https://doi.org/10.5061/dryad.b41j15h)

**Source-term evidence:** [https://doi.org/10.5061/dryad.b41j15h](https://doi.org/10.5061/dryad.b41j15h)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_aoslo_rpe,
  title  = { AOSLO RPE Cell Morphometry and Cone Mosaic Dataset },
  note   = { Human retinal pigment epithelium: in vivo cell morphometry, multispectral autofluorescence, and relationship to cone mosaic. Dryad. 2019. doi:10.5061/dryad.b41j15h },
  year   = { 2019 },
  url    = { https://doi.org/10.5061/dryad.b41j15h },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Human retinal pigment epithelium: in vivo cell morphometry, multispectral autofluorescence, and relationship to cone mosaic. Dryad. 2019. doi:10.5061/dryad.b41j15h
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC0 1.0
- **Normalized category:** `cc0`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Standard label without an explicit NC clause; not a permission finding

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.
