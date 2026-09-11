---
id: mendeley_set_relationship_between_plasma_amino_acid
title: "data set of Relationship between plasma amino acid and carnitine levels and primary angle closure glaucoma based on mass spectrometry metabolomics"
sidebar_label: mendeley_set_relationship_between_plasma_amino_acid
description: "Sample-level mass-spectrometry metabolomics measurements from Plasma measurements from people with primary angle-closure glaucoma, as stated by the linked study title and source description."
tags: ["omics", "cc-by", "manual", "measurement", "resource-role-current-dataset", "dataset-family-mendeley-set-relationship-between-plasma-amino-acid"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# data set of Relationship between plasma amino acid and carnitine levels and primary angle closure glaucoma based on mass spectrometry metabolomics

Sample-level mass-spectrometry metabolomics measurements from Plasma measurements from people with primary angle-closure glaucoma, as stated by the linked study title and source description.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mendeley_set_relationship_between_plasma_amino_acid` |
| **Full name** | data set of Relationship between plasma amino acid and carnitine levels and primary angle closure glaucoma based on mass spectrometry metabolomics |
| **First published** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Primary category** | `omics` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `mendeley_set_relationship_between_plasma_amino_acid` |
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

> Human provenance: Plasma measurements from people with primary angle-closure glaucoma, as stated by the linked study title and source description. Source-review finding: Current listing not independently retrievable; source description states mass-spectrometric plasma amino-acid and carnitine analysis data.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mendeley_set_relationship_between_plasma_amino_acid --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download mendeley_set_relationship_between_plasma_amino_acid --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mendeley_set_relationship_between_plasma_amino_acid')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/fn9986thfh)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/fn9986thfh)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mendeley_set_relationship_between_plasma_amino_acid,
  title  = { data set of Relationship between plasma amino acid and carnitine levels and primary angle closure glaucoma based on mass spectrometry metabolomics },
  note   = { data set of Relationship between plasma amino acid and carnitine levels and primary angle closure glaucoma based on mass spectrometry metabolomics. Mendeley Data. doi:10.17632/fn9986thfh },
  url    = { https://data.mendeley.com/datasets/fn9986thfh },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
data set of Relationship between plasma amino acid and carnitine levels and primary angle closure glaucoma based on mass spectrometry metabolomics. Mendeley Data. doi:10.17632/fn9986thfh.
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
