---
id: dryad_z8w9ghxpp
title: "ApoM-bound S1P acts via endothelial S1PR1 to suppress choroidal neovascularization and vascular leak"
sidebar_label: dryad_z8w9ghxpp
description: "Official Dryad deposit of source-described ocular microscopy data for the associated study."
tags: ["cell_microscopy", "tabular", "cc0", "dryad", "measurement"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# ApoM-bound S1P acts via endothelial S1PR1 to suppress choroidal neovascularization and vascular leak

Official Dryad deposit of source-described ocular microscopy data for the associated study.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_z8w9ghxpp` |
| **Full name** | ApoM-bound S1P acts via endothelial S1PR1 to suppress choroidal neovascularization and vascular leak |
| **Primary category** | `cell_microscopy` |
| **Contained modalities** | cell_microscopy, tabular |
| **Tasks** | measurement |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 4.159288366 GB |
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

> Scope screen: adjacent_add. Current Dryad v11 file listing: 47 files, 4159288366 bytes.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_z8w9ghxpp --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dryad_z8w9ghxpp --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_z8w9ghxpp')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.z8w9ghxpp](https://doi.org/10.5061/dryad.z8w9ghxpp)

**Source-term evidence:** [https://doi.org/10.5061/dryad.z8w9ghxpp](https://doi.org/10.5061/dryad.z8w9ghxpp)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_z8w9ghxpp,
  title  = { ApoM-bound S1P acts via endothelial S1PR1 to suppress choroidal neovascularization and vascular leak },
  note   = { Jung Bongnam, Yagi Hitomi, Kuo Andrew, Dorweiler Tim, Aikawa Masanori, Kasai Taku, Singh Sasha, Fu Zhongjie, Smith Lois, Niaudet Colin, Hla Timothy. ApoM-bound S1P acts via endothelial S1PR1 to suppress choroidal neovascularization and vascular leak. Dryad. 2025. doi:10.5061/dryad.z8w9ghxpp },
  year   = { 2025 },
  url    = { https://doi.org/10.5061/dryad.z8w9ghxpp },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Jung Bongnam, Yagi Hitomi, Kuo Andrew, Dorweiler Tim, Aikawa Masanori, Kasai Taku, Singh Sasha, Fu Zhongjie, Smith Lois, Niaudet Colin, Hla Timothy. ApoM-bound S1P acts via endothelial S1PR1 to suppress choroidal neovascularization and vascular leak. Dryad. 2025. doi:10.5061/dryad.z8w9ghxpp
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
- [dryad_pk0p2ngzh](./dryad_pk0p2ngzh.md): Morphometric analysis of retinal ganglionic cells (3D confocal images) analyzed using filament tracer from Imaris software (Not reported, `cc0`)
- [dryad_pzgmsbcmk](./dryad_pzgmsbcmk.md): Two-photon calcium recordings of cones (Not reported, `cc0`)
- [dryad_xpnvx0kb6](./dryad_xpnvx0kb6.md): Data from: Oxidative stress in the retina and retinal pigment epithelium (RPE): role of aging, and DJ-1 (Not reported, `cc0`)
- [dryad_zkh1893nt](./dryad_zkh1893nt.md): Glaucoma-associated optineurin mutations increase transcellular degradation of mitochondria in a vertebrate optic nerve (Not reported, `cc0`)
- [ocular_chat_vqa](./ocular_chat_vqa.md): OcularChat-VQA: AREDS-Derived Patient-Physician Dialogue Dataset (844,000 records, `cc-by-nc-sa`)
- [dryad_canine_pra_cea_genotypes](./dryad_canine_pra_cea_genotypes.md): Canine PRA and CEA Genotype Dataset (86,667 records, `cc0`)
