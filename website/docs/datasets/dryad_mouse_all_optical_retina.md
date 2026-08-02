---
id: dryad_mouse_all_optical_retina
title: "All-Optical Retinal Degeneration Mouse Dataset"
sidebar_label: dryad_mouse_all_optical_retina
description: "Mouse all-optical retinal recording/stimulation archive is a defined retinal-degeneration imaging and therapy-method resource."
tags: ["adaptive_optics", "electrophysiology", "cc0", "dryad", "measurement", "evaluation"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# All-Optical Retinal Degeneration Mouse Dataset

Mouse all-optical retinal recording/stimulation archive is a defined retinal-degeneration imaging and therapy-method resource.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_mouse_all_optical_retina` |
| **Full name** | All-Optical Retinal Degeneration Mouse Dataset |
| **Primary category** | `adaptive_optics` |
| **Contained modalities** | adaptive_optics, electrophysiology |
| **Tasks** | measurement, evaluation |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.22163995 GB |
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

> Scope screen: adjacent_add. Current Dryad v1 file listing: 2 files, 221621774 bytes.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_mouse_all_optical_retina --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dryad_mouse_all_optical_retina --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_mouse_all_optical_retina')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.7q37g6b](https://doi.org/10.5061/dryad.7q37g6b)

**Source-term evidence:** [https://doi.org/10.5061/dryad.7q37g6b](https://doi.org/10.5061/dryad.7q37g6b)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_mouse_all_optical_retina,
  title  = { All-Optical Retinal Degeneration Mouse Dataset },
  note   = { Cheong, Soon Keen, Strazzeri, Jennifer M., Williams, David R., and Merigan, William H.. Data from: All-optical recording and stimulation of retinal neurons in vivo in retinal degeneration mice. Dryad. 2019. doi:10.5061/dryad.7q37g6b },
  year   = { 2019 },
  url    = { https://doi.org/10.5061/dryad.7q37g6b },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Cheong, Soon Keen, Strazzeri, Jennifer M., Williams, David R., and Merigan, William H.. Data from: All-optical recording and stimulation of retinal neurons in vivo in retinal degeneration mice. Dryad. 2019. doi:10.5061/dryad.7q37g6b
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

- [leops_erg](./leops_erg.md): LEOPs Light-Adapted Electroretinogram and Oscillatory Potentials Dataset (9,743 signals, `cc-by`)
- [perg_ioba](./perg_ioba.md): PERG-IOBA Ocular Electrophysiology Dataset (1,354 signals, `odc-by`)
- [dryad_human_foveal_cones](./dryad_human_foveal_cones.md): Human foveal cone photoreceptor topography and its dependence on eye length (28 eyes, `cc0`)
- [dryad_brvo_bevacizumab_multimodal](./dryad_brvo_bevacizumab_multimodal.md): BRVO Bevacizumab Multimodal Dataset (27 eyes, `cc0`)
- [dryad_aoslo_rpe](./dryad_aoslo_rpe.md): AOSLO RPE Cell Morphometry and Cone Mosaic Dataset (10 participants, `cc0`)
- [dryad_5xfad_retina_dlgn](./dryad_5xfad_retina_dlgn.md): 5xFAD Retina and dLGN Disease-Model Dataset (Not reported, `cc0`)
- [dryad_cone_synapse_computation](./dryad_cone_synapse_computation.md): Cone Photoreceptor Synapse Dataset (Not reported, `cc0`)
- [dryad_d12d9f](./dryad_d12d9f.md): Excitatory neurotransmission activates compartmentalized calcium transients in Müller glia without affecting lateral process motility (Not reported, `cc0`)
