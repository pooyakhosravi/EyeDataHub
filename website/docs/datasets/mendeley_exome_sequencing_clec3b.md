---
id: mendeley_exome_sequencing_clec3b
title: "Exome sequencing data for CLEC3B"
sidebar_label: mendeley_exome_sequencing_clec3b
description: "Observation-level human or human-derived measurements/signals. from Six inherited-macular-disorder patients and three healthy relatives from Japanese families."
tags: ["omics", "cc-by", "mendeley", "measurement", "resource-role-current-dataset", "dataset-family-mendeley-exome-sequencing-clec3b"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Exome sequencing data for CLEC3B

Observation-level human or human-derived measurements/signals. from Six inherited-macular-disorder patients and three healthy relatives from Japanese families.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mendeley_exome_sequencing_clec3b` |
| **Full name** | Exome sequencing data for CLEC3B |
| **Publication date** | 2022-03-10 |
| **Date basis** | Initial dataset release |
| **Publication date precision** | day |
| **Publication date evidence** | [data.mendeley.com/public-api](https://data.mendeley.com/public-api/datasets/xcw5x5z49r) |
| **Publication date source field** | versions[version=1].publish_date |
| **Publication date reviewed** | 2026-09-11 |
| **Date notes** | - |
| **Primary category** | `omics` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `mendeley_exome_sequencing_clec3b` |
| **Contained modalities** | omics |
| **Tasks** | measurement |
| **Primary reported quantity** | 9 participants |
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

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 9 | `participants` | Source-stated quantity Preserved from the source-confirmation record. | `official_source_description` | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/xcw5x5z49r) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Human provenance: Six inherited-macular-disorder patients and three healthy relatives from Japanese families. Source-review finding: Exome-sequencing data/variant observations are described.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mendeley_exome_sequencing_clec3b --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download mendeley_exome_sequencing_clec3b --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mendeley_exome_sequencing_clec3b')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/xcw5x5z49r/1)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/xcw5x5z49r)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mendeley_exome_sequencing_clec3b,
  title  = { Exome sequencing data for CLEC3B },
  note   = { Exome sequencing data for CLEC3B. Mendeley Data, V1. doi:10.17632/xcw5x5z49r.1 },
  url    = { https://data.mendeley.com/datasets/xcw5x5z49r/1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Exome sequencing data for CLEC3B. Mendeley Data, V1. doi:10.17632/xcw5x5z49r.1.
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
- [mendeley_proteomic_analysis_human_autoimmune_retinopathy_air](./mendeley_proteomic_analysis_human_autoimmune_retinopathy_air.md): Proteomic analysis of human autoimmune retinopathy (AIR) vitreous (5 participants, `cc-by`)
- [dryad_congenital_glaucoma_wes](./dryad_congenital_glaucoma_wes.md): Identification of novel variants in LTBP2 and PXDN using whole-exome sequencing in developmental and congenital glaucoma (3 families, `cc0`)
- [dryad_rpgr_cone_rod_wes](./dryad_rpgr_cone_rod_wes.md): RPGR Cone-Rod Dystrophy WES Dataset (1 participants, `cc0`)
