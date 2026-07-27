---
id: dryad_cornea_oct_pentacam
title: "Corneal OCT and Pentacam Tomography Dataset"
sidebar_label: dryad_cornea_oct_pentacam
description: "Right-eye corneal OCT and rotating Scheimpflug tomography data with MATLAB code for automatic corneal-layer segmentation."
tags: ["multimodal", "oct", "corneal_topography", "cc0", "dryad", "segmentation", "measurement", "registration"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Corneal OCT and Pentacam Tomography Dataset

Right-eye corneal OCT and rotating Scheimpflug tomography data with MATLAB code for automatic corneal-layer segmentation.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_cornea_oct_pentacam` |
| **Full name** | Corneal OCT and Pentacam Tomography Dataset |
| **Primary category** | `multimodal` |
| **Contained modalities** | oct, corneal_topography |
| **Tasks** | segmentation, measurement, registration |
| **Samples** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.392 GB |
| **Source-stated terms** | CC0 1.0 |
| **Normalized terms** | `cc0` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Dryad |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Notes

> The source describes right-eye OCT and OCULUS Pentacam tomography plus custom segmentation code but does not expose a reliable record count in the repository metadata.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_cornea_oct_pentacam --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download dryad_cornea_oct_pentacam --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_cornea_oct_pentacam')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.tht76hf0c](https://doi.org/10.5061/dryad.tht76hf0c)

**Source-term evidence:** [https://doi.org/10.5061/dryad.tht76hf0c](https://doi.org/10.5061/dryad.tht76hf0c)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_cornea_oct_pentacam,
  title  = { Corneal OCT and Pentacam Tomography Dataset },
  note   = { Ran Z. Dataset for RSOS-211108. Dryad. 2021. doi:10.5061/dryad.tht76hf0c },
  year   = { 2021 },
  url    = { https://doi.org/10.5061/dryad.tht76hf0c },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Ran Z. Dataset for RSOS-211108. Dryad. 2021. doi:10.5061/dryad.tht76hf0c
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
