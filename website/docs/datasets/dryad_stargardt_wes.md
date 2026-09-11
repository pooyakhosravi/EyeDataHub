---
id: dryad_stargardt_wes
title: "Stargardt Disease WES Variant Dataset"
sidebar_label: dryad_stargardt_wes
description: "The 33-proband Stargardt variant table is a direct inherited-retinal-disease genomics resource."
tags: ["omics", "cc0", "dryad", "classification", "resource-role-current-dataset", "dataset-family-dryad-stargardt-wes"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Stargardt Disease WES Variant Dataset

The 33-proband Stargardt variant table is a direct inherited-retinal-disease genomics resource.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_stargardt_wes` |
| **Full name** | Stargardt Disease WES Variant Dataset |
| **First published** | 2016-06-29 |
| **Publication date precision** | day |
| **Publication date evidence** | [https://doi.org/10.5061/dryad.0qk7f](https://doi.org/10.5061/dryad.0qk7f) |
| **Publication date source field** | Published |
| **Publication date reviewed** | 2026-09-11 |
| **Primary category** | `omics` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `dryad_stargardt_wes` |
| **Contained modalities** | omics |
| **Tasks** | classification |
| **Primary reported quantity** | 33 participants |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.000304159 GB |
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
| Primary | 33 | `participants` | Source-described Stargardt disease probands Source-stated quantity; Dryad file count is separate metadata and is not a scientific sample count. | `official_source_description` | [https://doi.org/10.5061/dryad.0qk7f](https://doi.org/10.5061/dryad.0qk7f) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Scope screen: core_add. Current Dryad v1 file listing: 1 files, 284937 bytes.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_stargardt_wes --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dryad_stargardt_wes --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_stargardt_wes')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.0qk7f](https://doi.org/10.5061/dryad.0qk7f)

**Source-term evidence:** [https://doi.org/10.5061/dryad.0qk7f](https://doi.org/10.5061/dryad.0qk7f)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_stargardt_wes,
  title  = { Stargardt Disease WES Variant Dataset },
  note   = { Xin, Wei, Xiao, Xueshan, Li, Shiqiang, Jia, Xaioyun, Guo, Xiangming, Zhang, Qingjiong, and Jia, Xiaoyun. Data from: Identification of genetic defects in 33 probands with Stargardt disease by WES-based bioinformatics gene panel analysis. Dryad. 2016. doi:10.5061/dryad.0qk7f },
  year   = { 2016 },
  url    = { https://doi.org/10.5061/dryad.0qk7f },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Xin, Wei, Xiao, Xueshan, Li, Shiqiang, Jia, Xaioyun, Guo, Xiangming, Zhang, Qingjiong, and Jia, Xiaoyun. Data from: Identification of genetic defects in 33 probands with Stargardt disease by WES-based bioinformatics gene panel analysis. Dryad. 2016. doi:10.5061/dryad.0qk7f
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
- [mendeley_exome_sequencing_clec3b](./mendeley_exome_sequencing_clec3b.md): Exome sequencing data for CLEC3B (9 participants, `cc-by`)
- [mendeley_proteomic_analysis_human_autoimmune_retinopathy_air](./mendeley_proteomic_analysis_human_autoimmune_retinopathy_air.md): Proteomic analysis of human autoimmune retinopathy (AIR) vitreous (5 participants, `cc-by`)
- [dryad_congenital_glaucoma_wes](./dryad_congenital_glaucoma_wes.md): Identification of novel variants in LTBP2 and PXDN using whole-exome sequencing in developmental and congenital glaucoma (3 families, `cc0`)
- [dryad_rpgr_cone_rod_wes](./dryad_rpgr_cone_rod_wes.md): RPGR Cone-Rod Dystrophy WES Dataset (1 participants, `cc0`)
