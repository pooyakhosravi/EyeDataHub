---
id: dryad_pzgmsbcmk
title: "Two-photon calcium recordings of cones"
sidebar_label: dryad_pzgmsbcmk
description: "Official Dryad deposit of source-described retinal physiology data for the associated study."
tags: ["electrophysiology", "cell_microscopy", "tabular", "cc0", "dryad", "measurement"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Two-photon calcium recordings of cones

Official Dryad deposit of source-described retinal physiology data for the associated study.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_pzgmsbcmk` |
| **Full name** | Two-photon calcium recordings of cones |
| **Primary category** | `electrophysiology` |
| **Contained modalities** | electrophysiology, cell_microscopy, tabular |
| **Tasks** | measurement |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.878189959 GB |
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

> Scope screen: adjacent_add. Current Dryad v3 file listing: 13 files, 878189959 bytes.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_pzgmsbcmk --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dryad_pzgmsbcmk --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_pzgmsbcmk')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.pzgmsbcmk](https://doi.org/10.5061/dryad.pzgmsbcmk)

**Source-term evidence:** [https://doi.org/10.5061/dryad.pzgmsbcmk](https://doi.org/10.5061/dryad.pzgmsbcmk)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_pzgmsbcmk,
  title  = { Two-photon calcium recordings of cones },
  note   = { Yoshimatsu Takeshi, Bartel Philipp, Schroder Cornelius, Janiak Filip, St-Pierre Francois, Berens Philipp, Baden Tom. Two-photon calcium recordings of cones. Dryad. 2021. doi:10.5061/dryad.pzgmsbcmk },
  year   = { 2021 },
  url    = { https://doi.org/10.5061/dryad.pzgmsbcmk },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Yoshimatsu Takeshi, Bartel Philipp, Schroder Cornelius, Janiak Filip, St-Pierre Francois, Berens Philipp, Baden Tom. Two-photon calcium recordings of cones. Dryad. 2021. doi:10.5061/dryad.pzgmsbcmk
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
- [dryad_zkh1893nt](./dryad_zkh1893nt.md): Glaucoma-associated optineurin mutations increase transcellular degradation of mitochondria in a vertebrate optic nerve (Not reported, `cc0`)
- [leops_erg](./leops_erg.md): LEOPs Light-Adapted Electroretinogram and Oscillatory Potentials Dataset (9,743 signals, `cc-by`)
- [perg_ioba](./perg_ioba.md): PERG-IOBA Ocular Electrophysiology Dataset (1,354 signals, `odc-by`)
- [dryad_cone_synapse_computation](./dryad_cone_synapse_computation.md): Cone Photoreceptor Synapse Dataset (Not reported, `cc0`)
- [dryad_htr1b_mouse_retina](./dryad_htr1b_mouse_retina.md): &lt;em&gt;Htr1b&lt;/em&gt; is necessary for normal retinal function in mice (Not reported, `cc0`)
- [dryad_mouse_pupil_masking_retinal_deg](./dryad_mouse_pupil_masking_retinal_deg.md): Pupil and masking responses to light as functional measures of retinal degeneration in mice Mus Musculus (Not reported, `cc0`)
