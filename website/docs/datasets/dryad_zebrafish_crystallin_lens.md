---
id: dryad_zebrafish_crystallin_lens
title: "Zebrafish Crystallin Cataract Lens-Image Dataset"
sidebar_label: dryad_zebrafish_crystallin_lens
description: "Lens-image data from zebrafish crystallin mutants support investigation of age-related cataract mechanisms."
tags: ["cell_microscopy", "cc0", "dryad", "measurement"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Zebrafish Crystallin Cataract Lens-Image Dataset

Lens-image data from zebrafish crystallin mutants support investigation of age-related cataract mechanisms.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_zebrafish_crystallin_lens` |
| **Full name** | Zebrafish Crystallin Cataract Lens-Image Dataset |
| **Primary category** | `cell_microscopy` |
| **Contained modalities** | cell_microscopy |
| **Tasks** | measurement |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 4.451422309 GB |
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

No reproducible primary item count was exposed for the cataloged source version.

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Deferred-resolution scope: adjacent_add. Current Dryad v4 listing contains 2 files totaling 4451422309 bytes. No source-stated primary quantity was identified; file count is not used as num_samples.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_zebrafish_crystallin_lens --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dryad_zebrafish_crystallin_lens --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_zebrafish_crystallin_lens')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.f4qrfj730](https://doi.org/10.5061/dryad.f4qrfj730)

**Source-term evidence:** [https://doi.org/10.5061/dryad.f4qrfj730](https://doi.org/10.5061/dryad.f4qrfj730)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_zebrafish_crystallin_lens,
  title  = { Zebrafish Crystallin Cataract Lens-Image Dataset },
  note   = { Posner, Mason, and Farnsworth, Dylan. Loss of alpha Ba-crystallin, but not alpha A-crystallin, increases age-related cataract in the zebrafish lens. Dryad. 2024. doi:10.5061/dryad.f4qrfj730 },
  year   = { 2024 },
  url    = { https://doi.org/10.5061/dryad.f4qrfj730 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Posner, Mason, and Farnsworth, Dylan. Loss of alpha Ba-crystallin, but not alpha A-crystallin, increases age-related cataract in the zebrafish lens. Dryad. 2024. doi:10.5061/dryad.f4qrfj730
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

- [goblet_cell_segmentation](./goblet_cell_segmentation.md): Human Conjunctival Goblet Cell Segmentation Dataset (24 images, `cc-by`)
- [dryad_5xfad_retina_dlgn](./dryad_5xfad_retina_dlgn.md): 5xFAD Retina and dLGN Disease-Model Dataset (Not reported, `cc0`)
- [dryad_cone_synapse_computation](./dryad_cone_synapse_computation.md): Cone Photoreceptor Synapse Dataset (Not reported, `cc0`)
- [dryad_d12d9f](./dryad_d12d9f.md): Excitatory neurotransmission activates compartmentalized calcium transients in Müller glia without affecting lateral process motility (Not reported, `cc0`)
- [dryad_pk0p2ngzh](./dryad_pk0p2ngzh.md): Morphometric analysis of retinal ganglionic cells (3D confocal images) analyzed using filament tracer from Imaris software (Not reported, `cc0`)
- [dryad_pzgmsbcmk](./dryad_pzgmsbcmk.md): Two-photon calcium recordings of cones (Not reported, `cc0`)
- [dryad_q6rv0kz3](./dryad_q6rv0kz3.md): Asymmetric retinal direction tuning predicts optokinetic eye movements across stimulus conditions (Not reported, `cc0`)
- [dryad_r4xgxd2nt](./dryad_r4xgxd2nt.md): Restoration of cone circuit functionality in the regenerating adult zebrafish retina (Not reported, `cc0`)
