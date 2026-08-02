---
id: dryad_uveal_melanoma_coog2
title: "COOG2.1 Uveal Melanoma Prognostic Dataset"
sidebar_label: dryad_uveal_melanoma_coog2
description: "Multicenter uveal-melanoma gene-expression, PRAME, clinical, and metastasis-free-survival data for prognostic modeling."
tags: ["omics", "cc0", "dryad", "classification", "survival_analysis", "prognosis", "resource-role-current-dataset", "dataset-family-dryad-uveal-melanoma-coog2"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# COOG2.1 Uveal Melanoma Prognostic Dataset

Multicenter uveal-melanoma gene-expression, PRAME, clinical, and metastasis-free-survival data for prognostic modeling.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_uveal_melanoma_coog2` |
| **Full name** | COOG2.1 Uveal Melanoma Prognostic Dataset |
| **Primary category** | `omics` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `dryad_uveal_melanoma_coog2` |
| **Contained modalities** | omics |
| **Tasks** | classification, survival_analysis, prognosis |
| **Primary reported quantity** | 1,577 participants |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 8.4e-05 GB |
| **Source-stated terms** | CC0 1.0 |
| **Normalized terms** | `cc0` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Dryad |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `end_to_end_tested` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 1,577 | `participants` | Multicenter prognostic cohort | `official_source_description` | [https://doi.org/10.5061/dryad.n8pk0p340](https://doi.org/10.5061/dryad.n8pk0p340) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Contains 1,577 subjects enrolled across 26 centers with a 15-gene expression profile, PRAME status, clinical variables, and follow-up.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_uveal_melanoma_coog2 --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dryad_uveal_melanoma_coog2 --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_uveal_melanoma_coog2')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.n8pk0p340](https://doi.org/10.5061/dryad.n8pk0p340)

**Source-term evidence:** [https://doi.org/10.5061/dryad.n8pk0p340](https://doi.org/10.5061/dryad.n8pk0p340)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_uveal_melanoma_coog2,
  title  = { COOG2.1 Uveal Melanoma Prognostic Dataset },
  note   = { 15-gene expression profile and PRAME as an integrated prognostic test for uveal melanoma: First report of Collaborative Ocular Oncology Group Study No. 2 (COOG2.1). Dryad. 2025. doi:10.5061/dryad.n8pk0p340 },
  year   = { 2025 },
  url    = { https://doi.org/10.5061/dryad.n8pk0p340 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
15-gene expression profile and PRAME as an integrated prognostic test for uveal melanoma: First report of Collaborative Ocular Oncology Group Study No. 2 (COOG2.1). Dryad. 2025. doi:10.5061/dryad.n8pk0p340
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC0 1.0
- **Normalized category:** `cc0`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Standard label without an explicit NC clause; not a permission finding

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [dryad_uveitis_vitreous_biomarkers](./dryad_uveitis_vitreous_biomarkers.md): Uveitis Vitreous Biomarker Dataset (234 eyes, `cc0`)
- [dryad_dry_eye_nlrp3](./dryad_dry_eye_nlrp3.md): Dry Eye NLRP3 Ocular Surface Dataset (150 participants, `cc0`)
- [dryad_amd_zinc_complement](./dryad_amd_zinc_complement.md): AMD Zinc Complement Dataset (72 participants, `cc0`)
- [dryad_stargardt_wes](./dryad_stargardt_wes.md): Stargardt Disease WES Variant Dataset (33 participants, `cc0`)
- [mendeley_exome_sequencing_clec3b](./mendeley_exome_sequencing_clec3b.md): Exome sequencing data for CLEC3B (9 participants, `cc-by`)
- [mendeley_proteomic_analysis_human_autoimmune_retinopathy_air](./mendeley_proteomic_analysis_human_autoimmune_retinopathy_air.md): Proteomic analysis of human autoimmune retinopathy (AIR) vitreous (5 participants, `cc-by`)
- [dryad_congenital_glaucoma_wes](./dryad_congenital_glaucoma_wes.md): Identification of novel variants in LTBP2 and PXDN using whole-exome sequencing in developmental and congenital glaucoma (3 families, `cc0`)
- [cyp1b1_poag_genotypes](./cyp1b1_poag_genotypes.md): CYP1B1 Primary Open-Angle Glaucoma Genotype Dataset (Not reported, `cc-by`)
