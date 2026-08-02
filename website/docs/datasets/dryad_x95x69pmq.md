---
id: dryad_x95x69pmq
title: "Robust cone-mediated signaling persists late into rod photoreceptor degeneration"
sidebar_label: dryad_x95x69pmq
description: "Official Dryad deposit of source-described ocular microscopy data for the associated study."
tags: ["cell_microscopy", "cc0", "dryad", "measurement"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Robust cone-mediated signaling persists late into rod photoreceptor degeneration

Official Dryad deposit of source-described ocular microscopy data for the associated study.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_x95x69pmq` |
| **Full name** | Robust cone-mediated signaling persists late into rod photoreceptor degeneration |
| **Primary category** | `cell_microscopy` |
| **Contained modalities** | cell_microscopy |
| **Tasks** | measurement |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 5.659015815 GB |
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

> Scope screen: adjacent_add. Current Dryad v5 file listing: 20 files, 5659015815 bytes.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_x95x69pmq --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dryad_x95x69pmq --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_x95x69pmq')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.x95x69pmq](https://doi.org/10.5061/dryad.x95x69pmq)

**Source-term evidence:** [https://doi.org/10.5061/dryad.x95x69pmq](https://doi.org/10.5061/dryad.x95x69pmq)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_x95x69pmq,
  title  = { Robust cone-mediated signaling persists late into rod photoreceptor degeneration },
  note   = { Scalabrino Miranda. Robust cone-mediated signaling persists late into rod photoreceptor degeneration. Dryad. 2022. doi:10.5061/dryad.x95x69pmq },
  year   = { 2022 },
  url    = { https://doi.org/10.5061/dryad.x95x69pmq },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Scalabrino Miranda. Robust cone-mediated signaling persists late into rod photoreceptor degeneration. Dryad. 2022. doi:10.5061/dryad.x95x69pmq
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
