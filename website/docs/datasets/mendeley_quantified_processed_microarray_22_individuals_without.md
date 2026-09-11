---
id: mendeley_quantified_processed_microarray_22_individuals_without
title: "Quantified processed microarray data for 22 individuals with and without proliferative retinopathy"
sidebar_label: mendeley_quantified_processed_microarray_22_individuals_without
description: "Observation-level source data, annotations, or signals. from Source explicitly identifies 22 people with and without proliferative retinopathy."
tags: ["omics", "cc-by", "mendeley", "segmentation", "resource-role-current-dataset", "dataset-family-mendeley-quantified-processed-microarray-22-individuals-without"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Quantified processed microarray data for 22 individuals with and without proliferative retinopathy

Observation-level source data, annotations, or signals. from Source explicitly identifies 22 people with and without proliferative retinopathy.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mendeley_quantified_processed_microarray_22_individuals_without` |
| **Full name** | Quantified processed microarray data for 22 individuals with and without proliferative retinopathy |
| **First published** | 2020-02-17 |
| **Publication date precision** | day |
| **Publication date evidence** | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/72b47vpgtz/1) |
| **Publication date source field** | citation_publication_date (version 1) |
| **Publication date reviewed** | 2026-09-11 |
| **Primary category** | `omics` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `mendeley_quantified_processed_microarray_22_individuals_without` |
| **Contained modalities** | omics |
| **Tasks** | segmentation |
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

> Human provenance: Source explicitly identifies 22 people with and without proliferative retinopathy. Source-review finding: One normalized microarray expression matrix TXT file.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mendeley_quantified_processed_microarray_22_individuals_without --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download mendeley_quantified_processed_microarray_22_individuals_without --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mendeley_quantified_processed_microarray_22_individuals_without')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/72b47vpgtz/1)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/72b47vpgtz)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mendeley_quantified_processed_microarray_22_individuals_without,
  title  = { Quantified processed microarray data for 22 individuals with and without proliferative retinopathy },
  note   = { Quantified processed microarray data for 22 individuals with and without proliferative retinopathy. Mendeley Data, V1. doi:10.17632/72b47vpgtz.1 },
  url    = { https://data.mendeley.com/datasets/72b47vpgtz/1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Quantified processed microarray data for 22 individuals with and without proliferative retinopathy. Mendeley Data, V1. doi:10.17632/72b47vpgtz.1.
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
