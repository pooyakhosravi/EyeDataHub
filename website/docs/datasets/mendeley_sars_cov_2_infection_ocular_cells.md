---
id: mendeley_sars_cov_2_infection_ocular_cells
title: "SARS-CoV-2 infection of ocular cells from human adult donor eyes and hESC-derived ocular lineages, Eriksen et al"
sidebar_label: mendeley_sars_cov_2_infection_ocular_cells
description: "Human-derived ocular cell experimental measurements from Human adult donor-eye cells and hESC-derived ocular lineages."
tags: ["omics", "cc-by", "mendeley", "measurement", "resource-role-current-dataset", "dataset-family-mendeley-sars-cov-2-infection-ocular-cells"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# SARS-CoV-2 infection of ocular cells from human adult donor eyes and hESC-derived ocular lineages, Eriksen et al

Human-derived ocular cell experimental measurements from Human adult donor-eye cells and hESC-derived ocular lineages.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mendeley_sars_cov_2_infection_ocular_cells` |
| **Full name** | SARS-CoV-2 infection of ocular cells from human adult donor eyes and hESC-derived ocular lineages, Eriksen et al |
| **Primary category** | `omics` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `mendeley_sars_cov_2_infection_ocular_cells` |
| **Contained modalities** | omics |
| **Tasks** | measurement |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | Creative Commons Attribution 4.0 International |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `unknown` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Mendeley Data |
| **Availability** | `available` (checked 2026-08-02) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

No reproducible primary item count was exposed for the cataloged source version.

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Human provenance: Human adult donor-eye cells and hESC-derived ocular lineages. Source-review finding: Current listing not independently retrievable; source description concerns SARS-CoV-2 infection of human adult donor-eye and hESC-derived ocular cells.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mendeley_sars_cov_2_infection_ocular_cells --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download mendeley_sars_cov_2_infection_ocular_cells --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mendeley_sars_cov_2_infection_ocular_cells')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/jgw2mcgb67/1)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/jgw2mcgb67)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mendeley_sars_cov_2_infection_ocular_cells,
  title  = { SARS-CoV-2 infection of ocular cells from human adult donor eyes and hESC-derived ocular lineages, Eriksen et al },
  note   = { SARS-CoV-2 infection of ocular cells from human adult donor eyes and hESC-derived ocular lineages, Eriksen et al. Mendeley Data, V1. doi:10.17632/jgw2mcgb67.1 },
  url    = { https://data.mendeley.com/datasets/jgw2mcgb67/1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
SARS-CoV-2 infection of ocular cells from human adult donor eyes and hESC-derived ocular lineages, Eriksen et al. Mendeley Data, V1. doi:10.17632/jgw2mcgb67.1.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Creative Commons Attribution 4.0 International
- **Normalized category:** `cc-by`
- **Apparent scope:** `unknown`
- **Descriptive screening label:** Standard label without an explicit NC clause; not a permission finding

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [dryad_uveal_melanoma_coog2](./dryad_uveal_melanoma_coog2.md): COOG2.1 Uveal Melanoma Prognostic Dataset (1,577 participants, `cc0`)
- [dryad_uveitis_vitreous_biomarkers](./dryad_uveitis_vitreous_biomarkers.md): Uveitis Vitreous Biomarker Dataset (234 eyes, `cc0`)
- [dryad_dry_eye_nlrp3](./dryad_dry_eye_nlrp3.md): Dry Eye NLRP3 Ocular Surface Dataset (150 participants, `cc0`)
- [dryad_amd_zinc_complement](./dryad_amd_zinc_complement.md): AMD Zinc Complement Dataset (72 participants, `cc0`)
- [dryad_stargardt_wes](./dryad_stargardt_wes.md): Stargardt Disease WES Variant Dataset (33 participants, `cc0`)
- [mendeley_exome_sequencing_clec3b](./mendeley_exome_sequencing_clec3b.md): Exome sequencing data for CLEC3B (9 participants, `cc-by`)
- [mendeley_proteomic_analysis_human_autoimmune_retinopathy_air](./mendeley_proteomic_analysis_human_autoimmune_retinopathy_air.md): Proteomic analysis of human autoimmune retinopathy (AIR) vitreous (5 participants, `cc-by`)
- [dryad_congenital_glaucoma_wes](./dryad_congenital_glaucoma_wes.md): Identification of novel variants in LTBP2 and PXDN using whole-exome sequencing in developmental and congenital glaucoma (3 families, `cc0`)
