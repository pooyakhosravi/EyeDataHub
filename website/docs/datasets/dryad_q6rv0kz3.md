---
id: dryad_q6rv0kz3
title: "Asymmetric retinal direction tuning predicts optokinetic eye movements across stimulus conditions"
sidebar_label: dryad_q6rv0kz3
description: "Official Dryad deposit of source-described retinal circuit and eye-movement data for the associated study."
tags: ["multimodal", "eye_tracking", "electrophysiology", "cell_microscopy", "cc0", "dryad", "gaze_estimation", "measurement"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Asymmetric retinal direction tuning predicts optokinetic eye movements across stimulus conditions

Official Dryad deposit of source-described retinal circuit and eye-movement data for the associated study.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_q6rv0kz3` |
| **Full name** | Asymmetric retinal direction tuning predicts optokinetic eye movements across stimulus conditions |
| **Primary category** | `multimodal` |
| **Contained modalities** | eye_tracking, electrophysiology, cell_microscopy |
| **Tasks** | gaze_estimation, measurement |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.693075185 GB |
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

> Scope screen: adjacent_add. Current Dryad v6 file listing: 19 files, 693075185 bytes.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_q6rv0kz3 --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dryad_q6rv0kz3 --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_q6rv0kz3')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.7272/q6rv0kz3](https://doi.org/10.7272/q6rv0kz3)

**Source-term evidence:** [https://doi.org/10.7272/q6rv0kz3](https://doi.org/10.7272/q6rv0kz3)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_q6rv0kz3,
  title  = { Asymmetric retinal direction tuning predicts optokinetic eye movements across stimulus conditions },
  note   = { Harris Scott, Dunn Felice. Asymmetric retinal direction tuning predicts optokinetic eye movements across stimulus conditions. Dryad. 2023. doi:10.7272/q6rv0kz3 },
  year   = { 2023 },
  url    = { https://doi.org/10.7272/q6rv0kz3 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Harris Scott, Dunn Felice. Asymmetric retinal direction tuning predicts optokinetic eye movements across stimulus conditions. Dryad. 2023. doi:10.7272/q6rv0kz3
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
- [dryad_cone_synapse_computation](./dryad_cone_synapse_computation.md): Cone Photoreceptor Synapse Dataset (Not reported, `cc0`)
- [dryad_d12d9f](./dryad_d12d9f.md): Excitatory neurotransmission activates compartmentalized calcium transients in Müller glia without affecting lateral process motility (Not reported, `cc0`)
- [dryad_pzgmsbcmk](./dryad_pzgmsbcmk.md): Two-photon calcium recordings of cones (Not reported, `cc0`)
- [dryad_r4xgxd2nt](./dryad_r4xgxd2nt.md): Restoration of cone circuit functionality in the regenerating adult zebrafish retina (Not reported, `cc0`)
- [dryad_rv15dv4bv](./dryad_rv15dv4bv.md): Late gene therapy limits the restoration of retinal function in a mouse model of retinitis pigmentosa (Not reported, `cc0`)
- [dryad_zkh1893nt](./dryad_zkh1893nt.md): Glaucoma-associated optineurin mutations increase transcellular degradation of mitochondria in a vertebrate optic nerve (Not reported, `cc0`)
- [teyed](./teyed.md): TEyeD Real-World Eye-Tracking Dataset (20,666,096 images, `unknown`)
