---
id: dryad_cone_synapse_computation
title: "Cone Photoreceptor Synapse Dataset"
sidebar_label: dryad_cone_synapse_computation
description: "Ground-squirrel cone-synapse recordings are a well-defined retinal physiology resource relevant to photoreceptor mechanism studies."
tags: ["cell_microscopy", "electrophysiology", "cc0", "dryad", "measurement"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Cone Photoreceptor Synapse Dataset

Ground-squirrel cone-synapse recordings are a well-defined retinal physiology resource relevant to photoreceptor mechanism studies.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_cone_synapse_computation` |
| **Full name** | Cone Photoreceptor Synapse Dataset |
| **Primary category** | `cell_microscopy` |
| **Contained modalities** | cell_microscopy, electrophysiology |
| **Tasks** | measurement |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 19.122706764 GB |
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

> Scope screen: adjacent_add. Current Dryad v8 file listing: 4 files, 11191747623 bytes.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_cone_synapse_computation --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dryad_cone_synapse_computation --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_cone_synapse_computation')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.0p2ngf25g](https://doi.org/10.5061/dryad.0p2ngf25g)

**Source-term evidence:** [https://doi.org/10.5061/dryad.0p2ngf25g](https://doi.org/10.5061/dryad.0p2ngf25g)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_cone_synapse_computation,
  title  = { Cone Photoreceptor Synapse Dataset },
  note   = { DeVries, Steven, Grabner, Chad, Futagi, Daiki, Shi, Jun, Bindokas, Vytas, Kitano, Katsunori, and Schwartz, Eric. Mechanisms of simultaneous linear and nonlinear computations at the mammalian cone photoreceptor synapse. Dryad. 2023. doi:10.5061/dryad.0p2ngf25g },
  year   = { 2023 },
  url    = { https://doi.org/10.5061/dryad.0p2ngf25g },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
DeVries, Steven, Grabner, Chad, Futagi, Daiki, Shi, Jun, Bindokas, Vytas, Kitano, Katsunori, and Schwartz, Eric. Mechanisms of simultaneous linear and nonlinear computations at the mammalian cone photoreceptor synapse. Dryad. 2023. doi:10.5061/dryad.0p2ngf25g
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

- [dryad_5xfad_retina_dlgn](./dryad_5xfad_retina_dlgn.md): 5xFAD Retina and dLGN Disease-Model Dataset (Not reported, `cc0`)
- [dryad_d12d9f](./dryad_d12d9f.md): Excitatory neurotransmission activates compartmentalized calcium transients in Müller glia without affecting lateral process motility (Not reported, `cc0`)
- [dryad_pzgmsbcmk](./dryad_pzgmsbcmk.md): Two-photon calcium recordings of cones (Not reported, `cc0`)
- [dryad_q6rv0kz3](./dryad_q6rv0kz3.md): Asymmetric retinal direction tuning predicts optokinetic eye movements across stimulus conditions (Not reported, `cc0`)
- [dryad_r4xgxd2nt](./dryad_r4xgxd2nt.md): Restoration of cone circuit functionality in the regenerating adult zebrafish retina (Not reported, `cc0`)
- [dryad_rv15dv4bv](./dryad_rv15dv4bv.md): Late gene therapy limits the restoration of retinal function in a mouse model of retinitis pigmentosa (Not reported, `cc0`)
- [dryad_zkh1893nt](./dryad_zkh1893nt.md): Glaucoma-associated optineurin mutations increase transcellular degradation of mitochondria in a vertebrate optic nerve (Not reported, `cc0`)
- [leops_erg](./leops_erg.md): LEOPs Light-Adapted Electroretinogram and Oscillatory Potentials Dataset (9,743 signals, `cc-by`)
