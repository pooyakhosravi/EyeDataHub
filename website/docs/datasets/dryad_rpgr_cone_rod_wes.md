---
id: dryad_rpgr_cone_rod_wes
title: "RPGR Cone-Rod Dystrophy WES Dataset"
sidebar_label: dryad_rpgr_cone_rod_wes
description: "The paired FASTQ files represent a defined human RPGR cone-rod-dystrophy sequencing object."
tags: ["omics", "cc0", "dryad", "classification", "resource-role-current-dataset", "dataset-family-dryad-rpgr-cone-rod-wes"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# RPGR Cone-Rod Dystrophy WES Dataset

The paired FASTQ files represent a defined human RPGR cone-rod-dystrophy sequencing object.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_rpgr_cone_rod_wes` |
| **Full name** | RPGR Cone-Rod Dystrophy WES Dataset |
| **Publication date** | 2021-06-09 |
| **Date basis** | Initial dataset release |
| **Publication date precision** | day |
| **Publication date evidence** | [https://doi.org/10.5061/dryad.5qfttdz5d](https://doi.org/10.5061/dryad.5qfttdz5d) |
| **Publication date source field** | Published |
| **Publication date reviewed** | 2026-09-11 |
| **Date notes** | - |
| **Primary category** | `omics` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `dryad_rpgr_cone_rod_wes` |
| **Contained modalities** | omics |
| **Tasks** | classification |
| **Primary reported quantity** | 1 participants |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 4.478968648 GB |
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

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 1 | `participants` | Proband represented by the paired whole-exome sequencing files The complete current Dryad version 2 deposit contains paired reads for one source-described proband. | `official_source_description` | [https://doi.org/10.5061/dryad.5qfttdz5d](https://doi.org/10.5061/dryad.5qfttdz5d) |
| Additional | 2 | `deposited_files` | Paired FASTQ files in the current Dryad version 2 deposit Both source checksums matched during complete-deposit inspection. | `current_deposit_file_listing` | [https://doi.org/10.5061/dryad.5qfttdz5d](https://doi.org/10.5061/dryad.5qfttdz5d) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Scope screen: core_add. Current Dryad v2 file listing: 2 files, 4478935663 bytes.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_rpgr_cone_rod_wes --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dryad_rpgr_cone_rod_wes --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_rpgr_cone_rod_wes')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.5qfttdz5d](https://doi.org/10.5061/dryad.5qfttdz5d)

**Source-term evidence:** [https://doi.org/10.5061/dryad.5qfttdz5d](https://doi.org/10.5061/dryad.5qfttdz5d)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_rpgr_cone_rod_wes,
  title  = { RPGR Cone-Rod Dystrophy WES Dataset },
  note   = { Wang, Yafang. WES of the proband with a novel RPGR mutation. Dryad. 2021. doi:10.5061/dryad.5qfttdz5d },
  year   = { 2021 },
  url    = { https://doi.org/10.5061/dryad.5qfttdz5d },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Wang, Yafang. WES of the proband with a novel RPGR mutation. Dryad. 2021. doi:10.5061/dryad.5qfttdz5d
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

- [dryad_uveal_melanoma_coog2](./dryad_uveal_melanoma_coog2.md): COOG2.1 Uveal Melanoma Prognostic Dataset (1,577 participants, `cc0`)
- [dryad_uveitis_vitreous_biomarkers](./dryad_uveitis_vitreous_biomarkers.md): Uveitis Vitreous Biomarker Dataset (234 eyes, `cc0`)
- [dryad_dry_eye_nlrp3](./dryad_dry_eye_nlrp3.md): Dry Eye NLRP3 Ocular Surface Dataset (150 participants, `cc0`)
- [dryad_amd_zinc_complement](./dryad_amd_zinc_complement.md): AMD Zinc Complement Dataset (72 participants, `cc0`)
- [dryad_stargardt_wes](./dryad_stargardt_wes.md): Stargardt Disease WES Variant Dataset (33 participants, `cc0`)
- [mendeley_exome_sequencing_clec3b](./mendeley_exome_sequencing_clec3b.md): Exome sequencing data for CLEC3B (9 participants, `cc-by`)
- [mendeley_proteomic_analysis_human_autoimmune_retinopathy_air](./mendeley_proteomic_analysis_human_autoimmune_retinopathy_air.md): Proteomic analysis of human autoimmune retinopathy (AIR) vitreous (5 participants, `cc-by`)
- [dryad_congenital_glaucoma_wes](./dryad_congenital_glaucoma_wes.md): Identification of novel variants in LTBP2 and PXDN using whole-exome sequencing in developmental and congenital glaucoma (3 families, `cc0`)
