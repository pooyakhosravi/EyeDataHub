---
id: dryad_zkh1893nt
title: "Glaucoma-associated optineurin mutations increase transcellular degradation of mitochondria in a vertebrate optic nerve"
sidebar_label: dryad_zkh1893nt
description: "Official Dryad deposit of source-described ocular microscopy data for the associated study."
tags: ["cell_microscopy", "electrophysiology", "tabular", "cc0", "dryad", "measurement"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Glaucoma-associated optineurin mutations increase transcellular degradation of mitochondria in a vertebrate optic nerve

Official Dryad deposit of source-described ocular microscopy data for the associated study.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_zkh1893nt` |
| **Full name** | Glaucoma-associated optineurin mutations increase transcellular degradation of mitochondria in a vertebrate optic nerve |
| **Primary category** | `cell_microscopy` |
| **Contained modalities** | cell_microscopy, electrophysiology, tabular |
| **Tasks** | measurement |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 130.554606106 GB |
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

> Scope screen: adjacent_add. Current Dryad v7 file listing: 32 files, 130554606106 bytes.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_zkh1893nt --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dryad_zkh1893nt --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_zkh1893nt')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.zkh1893nt](https://doi.org/10.5061/dryad.zkh1893nt)

**Source-term evidence:** [https://doi.org/10.5061/dryad.zkh1893nt](https://doi.org/10.5061/dryad.zkh1893nt)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_zkh1893nt,
  title  = { Glaucoma-associated optineurin mutations increase transcellular degradation of mitochondria in a vertebrate optic nerve },
  note   = { Marsh-Armstrong Nicholas, Jeong Yaeram, Davis Chung-ha O., Muscarella Aaron M., Navarro Hector H., Deshpande Viraj, Moore Lucy G., Kim Keun-Young, Ellisman Mark H.. Glaucoma-associated optineurin mutations increase transcellular degradation of mitochondria in a vertebrate optic nerve. Dryad. 2025. doi:10.5061/dryad.zkh1893nt },
  year   = { 2025 },
  url    = { https://doi.org/10.5061/dryad.zkh1893nt },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Marsh-Armstrong Nicholas, Jeong Yaeram, Davis Chung-ha O., Muscarella Aaron M., Navarro Hector H., Deshpande Viraj, Moore Lucy G., Kim Keun-Young, Ellisman Mark H.. Glaucoma-associated optineurin mutations increase transcellular degradation of mitochondria in a vertebrate optic nerve. Dryad. 2025. doi:10.5061/dryad.zkh1893nt
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
- [leops_erg](./leops_erg.md): LEOPs Light-Adapted Electroretinogram and Oscillatory Potentials Dataset (9,743 signals, `cc-by`)
- [perg_ioba](./perg_ioba.md): PERG-IOBA Ocular Electrophysiology Dataset (1,354 signals, `odc-by`)
- [dryad_cone_synapse_computation](./dryad_cone_synapse_computation.md): Cone Photoreceptor Synapse Dataset (Not reported, `cc0`)
- [dryad_htr1b_mouse_retina](./dryad_htr1b_mouse_retina.md): &lt;em&gt;Htr1b&lt;/em&gt; is necessary for normal retinal function in mice (Not reported, `cc0`)
- [dryad_mouse_pupil_masking_retinal_deg](./dryad_mouse_pupil_masking_retinal_deg.md): Pupil and masking responses to light as functional measures of retinal degeneration in mice Mus Musculus (Not reported, `cc0`)
