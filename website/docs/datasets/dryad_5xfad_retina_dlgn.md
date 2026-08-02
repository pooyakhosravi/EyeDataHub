---
id: dryad_5xfad_retina_dlgn
title: "5xFAD Retina and dLGN Disease-Model Dataset"
sidebar_label: dryad_5xfad_retina_dlgn
description: "Workbook data characterize retinal and dLGN effects of amyloid pathology in the 5xFAD mouse model using electrophysiology, imaging, and histology."
tags: ["multimodal", "electrophysiology", "cell_microscopy", "tabular", "cc0", "dryad", "measurement"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# 5xFAD Retina and dLGN Disease-Model Dataset

Workbook data characterize retinal and dLGN effects of amyloid pathology in the 5xFAD mouse model using electrophysiology, imaging, and histology.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_5xfad_retina_dlgn` |
| **Full name** | 5xFAD Retina and dLGN Disease-Model Dataset |
| **Primary category** | `multimodal` |
| **Contained modalities** | electrophysiology, cell_microscopy, tabular |
| **Tasks** | measurement |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.000108816 GB |
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

> Deferred-resolution scope: adjacent_add. Current Dryad v2 listing contains 2 files totaling 108816 bytes. No source-stated primary quantity was identified; file count is not used as num_samples.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_5xfad_retina_dlgn --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dryad_5xfad_retina_dlgn --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_5xfad_retina_dlgn')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.dbrv15fbk](https://doi.org/10.5061/dryad.dbrv15fbk)

**Source-term evidence:** [https://doi.org/10.5061/dryad.dbrv15fbk](https://doi.org/10.5061/dryad.dbrv15fbk)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_5xfad_retina_dlgn,
  title  = { 5xFAD Retina and dLGN Disease-Model Dataset },
  note   = { McCool, Shaylah, and Van Hook, Matthew. Influence of amyloid pathology on retina and dLGN in 5xFAD mouse model. Dryad. 2024. doi:10.5061/dryad.dbrv15fbk },
  year   = { 2024 },
  url    = { https://doi.org/10.5061/dryad.dbrv15fbk },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
McCool, Shaylah, and Van Hook, Matthew. Influence of amyloid pathology on retina and dLGN in 5xFAD mouse model. Dryad. 2024. doi:10.5061/dryad.dbrv15fbk
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

- [dryad_d12d9f](./dryad_d12d9f.md): Excitatory neurotransmission activates compartmentalized calcium transients in Müller glia without affecting lateral process motility (Not reported, `cc0`)
- [dryad_pzgmsbcmk](./dryad_pzgmsbcmk.md): Two-photon calcium recordings of cones (Not reported, `cc0`)
- [dryad_zkh1893nt](./dryad_zkh1893nt.md): Glaucoma-associated optineurin mutations increase transcellular degradation of mitochondria in a vertebrate optic nerve (Not reported, `cc0`)
- [leops_erg](./leops_erg.md): LEOPs Light-Adapted Electroretinogram and Oscillatory Potentials Dataset (9,743 signals, `cc-by`)
- [perg_ioba](./perg_ioba.md): PERG-IOBA Ocular Electrophysiology Dataset (1,354 signals, `odc-by`)
- [dryad_cone_synapse_computation](./dryad_cone_synapse_computation.md): Cone Photoreceptor Synapse Dataset (Not reported, `cc0`)
- [dryad_htr1b_mouse_retina](./dryad_htr1b_mouse_retina.md): &lt;em&gt;Htr1b&lt;/em&gt; is necessary for normal retinal function in mice (Not reported, `cc0`)
- [dryad_mouse_pupil_masking_retinal_deg](./dryad_mouse_pupil_masking_retinal_deg.md): Pupil and masking responses to light as functional measures of retinal degeneration in mice Mus Musculus (Not reported, `cc0`)
