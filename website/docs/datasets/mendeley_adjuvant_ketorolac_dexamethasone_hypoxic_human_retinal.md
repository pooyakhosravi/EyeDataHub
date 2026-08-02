---
id: mendeley_adjuvant_ketorolac_dexamethasone_hypoxic_human_retinal
title: "Adjuvant Ketorolac and Dexamethasone + Hypoxic Human Retinal Pigment Epithelium (RPE) and Endothelial Cells (HREC)"
sidebar_label: mendeley_adjuvant_ketorolac_dexamethasone_hypoxic_human_retinal
description: "Observation-level human or human-derived measurements/signals. from Human RPE and retinal endothelial cells cultured under hypoxia."
tags: ["omics", "cc-by", "mendeley", "measurement", "resource-role-current-dataset", "dataset-family-mendeley-adjuvant-ketorolac-dexamethasone-hypoxic-human-retinal"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Adjuvant Ketorolac and Dexamethasone + Hypoxic Human Retinal Pigment Epithelium (RPE) and Endothelial Cells (HREC)

Observation-level human or human-derived measurements/signals. from Human RPE and retinal endothelial cells cultured under hypoxia.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mendeley_adjuvant_ketorolac_dexamethasone_hypoxic_human_retinal` |
| **Full name** | Adjuvant Ketorolac and Dexamethasone + Hypoxic Human Retinal Pigment Epithelium (RPE) and Endothelial Cells (HREC) |
| **Primary category** | `omics` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `mendeley_adjuvant_ketorolac_dexamethasone_hypoxic_human_retinal` |
| **Contained modalities** | omics |
| **Tasks** | measurement |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Mendeley Data |
| **Availability** | `available` (checked 2026-08-02) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

No reproducible primary item count was exposed for the cataloged source version.

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Human provenance: Human RPE and retinal endothelial cells cultured under hypoxia. Source-review finding: SPSS data with viability and relative mRNA/protein expression across treatments.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mendeley_adjuvant_ketorolac_dexamethasone_hypoxic_human_retinal --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download mendeley_adjuvant_ketorolac_dexamethasone_hypoxic_human_retinal --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mendeley_adjuvant_ketorolac_dexamethasone_hypoxic_human_retinal')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/xzf382pby9/1)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/xzf382pby9)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mendeley_adjuvant_ketorolac_dexamethasone_hypoxic_human_retinal,
  title  = { Adjuvant Ketorolac and Dexamethasone + Hypoxic Human Retinal Pigment Epithelium (RPE) and Endothelial Cells (HREC) },
  note   = { Adjuvant Ketorolac and Dexamethasone + Hypoxic Human Retinal Pigment Epithelium (RPE) and Endothelial Cells (HREC). Mendeley Data, V1. doi:10.17632/xzf382pby9.1 },
  url    = { https://data.mendeley.com/datasets/xzf382pby9/1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Adjuvant Ketorolac and Dexamethasone + Hypoxic Human Retinal Pigment Epithelium (RPE) and Endothelial Cells (HREC). Mendeley Data, V1. doi:10.17632/xzf382pby9.1.
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
