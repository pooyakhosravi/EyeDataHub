---
id: mendeley_micro_go_study_transcriptional_profiling_orbital
title: "MICRO-GO study: transcriptional profiling of orbital tissues in Graves’ orbitopathy & microbiome composition"
sidebar_label: mendeley_micro_go_study_transcriptional_profiling_orbital
description: "Human tissue transcriptional and microbiome measurements from Orbital tissue from people with Graves' orbitopathy and relevant human microbiome samples."
tags: ["omics", "cc-by", "manual", "measurement"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# MICRO-GO study: transcriptional profiling of orbital tissues in Graves’ orbitopathy & microbiome composition

Human tissue transcriptional and microbiome measurements from Orbital tissue from people with Graves' orbitopathy and relevant human microbiome samples.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mendeley_micro_go_study_transcriptional_profiling_orbital` |
| **Full name** | MICRO-GO study: transcriptional profiling of orbital tissues in Graves’ orbitopathy & microbiome composition |
| **Primary category** | `omics` |
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
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-08-02) |
| **Acquisition support** | `guided_instructions_only` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

No reproducible primary item count was exposed for the cataloged source version.

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Human provenance: Orbital tissue from people with Graves' orbitopathy and relevant human microbiome samples. Source-review finding: Current listing not independently retrievable; source description identifies transcriptional profiling of orbital tissues and microbiome composition.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mendeley_micro_go_study_transcriptional_profiling_orbital --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download mendeley_micro_go_study_transcriptional_profiling_orbital --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mendeley_micro_go_study_transcriptional_profiling_orbital')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/mrvmsrn9r6)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/mrvmsrn9r6)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mendeley_micro_go_study_transcriptional_profiling_orbital,
  title  = { MICRO-GO study: transcriptional profiling of orbital tissues in Graves’ orbitopathy & microbiome composition },
  note   = { MICRO-GO study: transcriptional profiling of orbital tissues in Graves’ orbitopathy & microbiome composition. Mendeley Data. doi:10.17632/mrvmsrn9r6 },
  url    = { https://data.mendeley.com/datasets/mrvmsrn9r6 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
MICRO-GO study: transcriptional profiling of orbital tissues in Graves’ orbitopathy & microbiome composition. Mendeley Data. doi:10.17632/mrvmsrn9r6.
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
