---
id: dryad_mouse_pupil_masking_retinal_deg
title: "Pupil and masking responses to light as functional measures of retinal degeneration in mice Mus Musculus"
sidebar_label: dryad_mouse_pupil_masking_retinal_deg
description: "The three named ERG pupil and masking response files form a defined retinal-degeneration functional-assay resource in a disease model."
tags: ["electrophysiology", "tabular", "cc0", "dryad", "measurement", "evaluation"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Pupil and masking responses to light as functional measures of retinal degeneration in mice Mus Musculus

The three named ERG pupil and masking response files form a defined retinal-degeneration functional-assay resource in a disease model.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_mouse_pupil_masking_retinal_deg` |
| **Full name** | Pupil and masking responses to light as functional measures of retinal degeneration in mice Mus Musculus |
| **Primary category** | `electrophysiology` |
| **Contained modalities** | electrophysiology, tabular |
| **Tasks** | measurement, evaluation |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.0522391 GB |
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

> Scope: adjacent_add. Named file-level object: ERG.pzf, PLR.pzf, and Negative_masking.pzf. Official Dryad API metadata and current file listing reviewed 2026-08-01.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_mouse_pupil_masking_retinal_deg --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dryad_mouse_pupil_masking_retinal_deg --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_mouse_pupil_masking_retinal_deg')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.9kd51c5g5](https://doi.org/10.5061/dryad.9kd51c5g5)

**Source-term evidence:** [https://doi.org/10.5061/dryad.9kd51c5g5](https://doi.org/10.5061/dryad.9kd51c5g5)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_mouse_pupil_masking_retinal_deg,
  title  = { Pupil and masking responses to light as functional measures of retinal degeneration in mice Mus Musculus },
  note   = { Pupil and masking responses to light as functional measures of retinal degeneration in mice Mus Musculus. Dryad Dataset. doi:10.5061/dryad.9kd51c5g5 },
  url    = { https://doi.org/10.5061/dryad.9kd51c5g5 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Pupil and masking responses to light as functional measures of retinal degeneration in mice Mus Musculus. Dryad Dataset. doi:10.5061/dryad.9kd51c5g5.
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
- [dryad_5xfad_retina_dlgn](./dryad_5xfad_retina_dlgn.md): 5xFAD Retina and dLGN Disease-Model Dataset (Not reported, `cc0`)
- [dryad_d12d9f](./dryad_d12d9f.md): Excitatory neurotransmission activates compartmentalized calcium transients in Müller glia without affecting lateral process motility (Not reported, `cc0`)
- [dryad_htr1b_mouse_retina](./dryad_htr1b_mouse_retina.md): &lt;em&gt;Htr1b&lt;/em&gt; is necessary for normal retinal function in mice (Not reported, `cc0`)
- [dryad_pzgmsbcmk](./dryad_pzgmsbcmk.md): Two-photon calcium recordings of cones (Not reported, `cc0`)
- [dryad_zebrafish_thrb_photoreceptors](./dryad_zebrafish_thrb_photoreceptors.md): Thyroid hormone receptor beta mutations alter photoreceptor development and function in Danio rerio (zebrafish) (Not reported, `cc0`)
- [dryad_zkh1893nt](./dryad_zkh1893nt.md): Glaucoma-associated optineurin mutations increase transcellular degradation of mitochondria in a vertebrate optic nerve (Not reported, `cc0`)
