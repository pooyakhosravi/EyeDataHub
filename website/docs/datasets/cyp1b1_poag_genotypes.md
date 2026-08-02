---
id: cyp1b1_poag_genotypes
title: "CYP1B1 Primary Open-Angle Glaucoma Genotype Dataset"
sidebar_label: cyp1b1_poag_genotypes
description: "Human POAG genotype observations."
tags: ["omics", "genomics", "cc-by", "figshare", "classification", "resource-role-current-dataset", "dataset-family-cyp1b1-poag-genotypes"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# CYP1B1 Primary Open-Angle Glaucoma Genotype Dataset

Human POAG genotype observations.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `cyp1b1_poag_genotypes` |
| **Full name** | CYP1B1 Primary Open-Angle Glaucoma Genotype Dataset |
| **Primary category** | `omics` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `cyp1b1_poag_genotypes` |
| **Contained modalities** | omics, genomics |
| **Tasks** | classification |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Figshare |
| **Availability** | `available` (checked 2026-08-02) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

No reproducible primary item count was exposed for the cataloged source version.

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download cyp1b1_poag_genotypes --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download cyp1b1_poag_genotypes --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('cyp1b1_poag_genotypes')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.25451/flinders.16545561.v1](https://doi.org/10.25451/flinders.16545561.v1)

**Source-term evidence:** [https://doi.org/10.25451/flinders.16545561.v1](https://doi.org/10.25451/flinders.16545561.v1)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{cyp1b1_poag_genotypes,
  title  = { CYP1B1 Primary Open-Angle Glaucoma Genotype Dataset },
  note   = { Repository dataset record. 10.25451/flinders.16545561.v1 },
  url    = { https://doi.org/10.25451/flinders.16545561.v1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Repository dataset record. 10.25451/flinders.16545561.v1.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC BY 4.0
- **Normalized category:** `cc-by`
- **Apparent scope:** `dataset_files`
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
