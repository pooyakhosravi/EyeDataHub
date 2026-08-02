---
id: dryad_tb2rbp0cq
title: "Serial block face scanning electron micrographs of mouse outer retina"
sidebar_label: dryad_tb2rbp0cq
description: "Official Dryad deposit of source-described ocular microscopy data for the associated study."
tags: ["cell_microscopy", "cc0", "dryad", "reconstruction"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Serial block face scanning electron micrographs of mouse outer retina

Official Dryad deposit of source-described ocular microscopy data for the associated study.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_tb2rbp0cq` |
| **Full name** | Serial block face scanning electron micrographs of mouse outer retina |
| **Primary category** | `cell_microscopy` |
| **Contained modalities** | cell_microscopy |
| **Tasks** | reconstruction |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 5.051903547 GB |
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

> Scope screen: adjacent_add. Current Dryad v4 file listing: 358 files, 5051903547 bytes.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_tb2rbp0cq --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dryad_tb2rbp0cq --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_tb2rbp0cq')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.tb2rbp0cq](https://doi.org/10.5061/dryad.tb2rbp0cq)

**Source-term evidence:** [https://doi.org/10.5061/dryad.tb2rbp0cq](https://doi.org/10.5061/dryad.tb2rbp0cq)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_tb2rbp0cq,
  title  = { Serial block face scanning electron micrographs of mouse outer retina },
  note   = { Thoreson Wallace, Bartol Thomas, Conoan Nicholas, Diamond Jeffrey. Serial block face scanning electron micrographs of mouse outer retina. Dryad. 2025. doi:10.5061/dryad.tb2rbp0cq },
  year   = { 2025 },
  url    = { https://doi.org/10.5061/dryad.tb2rbp0cq },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Thoreson Wallace, Bartol Thomas, Conoan Nicholas, Diamond Jeffrey. Serial block face scanning electron micrographs of mouse outer retina. Dryad. 2025. doi:10.5061/dryad.tb2rbp0cq
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
