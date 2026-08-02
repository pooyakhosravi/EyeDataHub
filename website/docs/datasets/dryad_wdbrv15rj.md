---
id: dryad_wdbrv15rj
title: "Natural disease history of a canine model of oligogenic RPGRIP1-cone-rod dystrophy establishes variable effects of previously and newly mapped modifier loci"
sidebar_label: dryad_wdbrv15rj
description: "Official Dryad deposit of source-described ocular omics data for the associated study."
tags: ["omics", "tabular", "cc0", "dryad", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Natural disease history of a canine model of oligogenic RPGRIP1-cone-rod dystrophy establishes variable effects of previously and newly mapped modifier loci

Official Dryad deposit of source-described ocular omics data for the associated study.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_wdbrv15rj` |
| **Full name** | Natural disease history of a canine model of oligogenic RPGRIP1-cone-rod dystrophy establishes variable effects of previously and newly mapped modifier loci |
| **Primary category** | `omics` |
| **Contained modalities** | omics, tabular |
| **Tasks** | classification |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 212.240887027 GB |
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

> Scope screen: adjacent_add. Current Dryad v5 file listing: 19 files, 212240887027 bytes.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_wdbrv15rj --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dryad_wdbrv15rj --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_wdbrv15rj')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.wdbrv15rj](https://doi.org/10.5061/dryad.wdbrv15rj)

**Source-term evidence:** [https://doi.org/10.5061/dryad.wdbrv15rj](https://doi.org/10.5061/dryad.wdbrv15rj)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_wdbrv15rj,
  title  = { Natural disease history of a canine model of oligogenic RPGRIP1-cone-rod dystrophy establishes variable effects of previously and newly mapped modifier loci },
  note   = { Ripolles-Garcia Ana, Murgiano Leonardo, Ziolkowska Natalia, Marinho Felipe Pompeo, Roszak Karolina, Iffrig Sommer, Aguirre Gustavo D., Miyadera Keiko. Natural disease history of a canine model of oligogenic RPGRIP1-cone-rod dystrophy establishes variable effects of previously and newly mapped modifier loci. Dryad. 2023. doi:10.5061/dryad.wdbrv15rj },
  year   = { 2023 },
  url    = { https://doi.org/10.5061/dryad.wdbrv15rj },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Ripolles-Garcia Ana, Murgiano Leonardo, Ziolkowska Natalia, Marinho Felipe Pompeo, Roszak Karolina, Iffrig Sommer, Aguirre Gustavo D., Miyadera Keiko. Natural disease history of a canine model of oligogenic RPGRIP1-cone-rod dystrophy establishes variable effects of previously and newly mapped modifier loci. Dryad. 2023. doi:10.5061/dryad.wdbrv15rj
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
- [dryad_uveitis_vitreous_biomarkers](./dryad_uveitis_vitreous_biomarkers.md): Uveitis Vitreous Biomarker Dataset (234 eyes, `cc0`)
- [dryad_dry_eye_nlrp3](./dryad_dry_eye_nlrp3.md): Dry Eye NLRP3 Ocular Surface Dataset (150 participants, `cc0`)
- [dryad_amd_zinc_complement](./dryad_amd_zinc_complement.md): AMD Zinc Complement Dataset (72 participants, `cc0`)
- [dryad_congenital_glaucoma_wes](./dryad_congenital_glaucoma_wes.md): Identification of novel variants in LTBP2 and PXDN using whole-exome sequencing in developmental and congenital glaucoma (3 families, `cc0`)
- [dryad_ird_mouse_proteome](./dryad_ird_mouse_proteome.md): Retinal proteome profiling of inherited retinal degeneration across three different mouse models suggests common drug targets in retinitis pigmentosa (3 animal models, `cc0`)
- [dryad_acanthamoeba_keratitis_transcriptome](./dryad_acanthamoeba_keratitis_transcriptome.md): Human conjunctival transcriptome in Acanthamoeba keratitis: An exploratory study (Not reported, `cc0`)
- [dryad_corneal_conjunctivitis_biomarker](./dryad_corneal_conjunctivitis_biomarker.md): Corneal Conjunctivitis Biomarker Dataset (Not reported, `cc0`)
