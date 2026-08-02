---
id: dryad_primate_on_dsgc
title: "Primate ON Direction-Selective Ganglion Cell Dataset"
sidebar_label: dryad_primate_on_dsgc
description: "Primate ON-DSGC transcriptomic and retinal physiology archives are a defined, translationally relevant retinal-cell resource."
tags: ["electrophysiology", "omics", "cc0", "dryad", "classification", "measurement"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Primate ON Direction-Selective Ganglion Cell Dataset

Primate ON-DSGC transcriptomic and retinal physiology archives are a defined, translationally relevant retinal-cell resource.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_primate_on_dsgc` |
| **Full name** | Primate ON Direction-Selective Ganglion Cell Dataset |
| **Primary category** | `electrophysiology` |
| **Contained modalities** | electrophysiology, omics |
| **Tasks** | classification, measurement |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 64.655408401 GB |
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

> Scope screen: adjacent_add. Current Dryad v4 file listing: 13 files, 64655258350 bytes.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_primate_on_dsgc --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dryad_primate_on_dsgc --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_primate_on_dsgc')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.47d7wm3kx](https://doi.org/10.5061/dryad.47d7wm3kx)

**Source-term evidence:** [https://doi.org/10.5061/dryad.47d7wm3kx](https://doi.org/10.5061/dryad.47d7wm3kx)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_primate_on_dsgc,
  title  = { Primate ON Direction-Selective Ganglion Cell Dataset },
  note   = { Wang, Anna Y. M., Kulkarni, Manoj M., McLaughlin, Amanda J., Gayet, Jacqueline, Smith, Benjamin E., Hauptschein, Max, McHugh, Cyrus F., Yao, Yvette Y., and Puthussery, Teresa. An ON-type direction selective ganglion cell in primate retina. Dryad. 2023. doi:10.5061/dryad.47d7wm3kx },
  year   = { 2023 },
  url    = { https://doi.org/10.5061/dryad.47d7wm3kx },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Wang, Anna Y. M., Kulkarni, Manoj M., McLaughlin, Amanda J., Gayet, Jacqueline, Smith, Benjamin E., Hauptschein, Max, McHugh, Cyrus F., Yao, Yvette Y., and Puthussery, Teresa. An ON-type direction selective ganglion cell in primate retina. Dryad. 2023. doi:10.5061/dryad.47d7wm3kx
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

- [dryad_canine_pra_cea_genotypes](./dryad_canine_pra_cea_genotypes.md): Canine PRA and CEA Genotype Dataset (86,667 records, `cc0`)
- [leops_erg](./leops_erg.md): LEOPs Light-Adapted Electroretinogram and Oscillatory Potentials Dataset (9,743 signals, `cc-by`)
- [dryad_uveal_melanoma_coog2](./dryad_uveal_melanoma_coog2.md): COOG2.1 Uveal Melanoma Prognostic Dataset (1,577 participants, `cc0`)
- [perg_ioba](./perg_ioba.md): PERG-IOBA Ocular Electrophysiology Dataset (1,354 signals, `odc-by`)
- [dryad_uveitis_vitreous_biomarkers](./dryad_uveitis_vitreous_biomarkers.md): Uveitis Vitreous Biomarker Dataset (234 eyes, `cc0`)
- [dryad_dry_eye_nlrp3](./dryad_dry_eye_nlrp3.md): Dry Eye NLRP3 Ocular Surface Dataset (150 participants, `cc0`)
- [dryad_amd_zinc_complement](./dryad_amd_zinc_complement.md): AMD Zinc Complement Dataset (72 participants, `cc0`)
- [dryad_stargardt_wes](./dryad_stargardt_wes.md): Stargardt Disease WES Variant Dataset (33 participants, `cc0`)
