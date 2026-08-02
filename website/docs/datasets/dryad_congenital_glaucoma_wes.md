---
id: dryad_congenital_glaucoma_wes
title: "Identification of novel variants in LTBP2 and PXDN using whole-exome sequencing in developmental and congenital glaucoma"
sidebar_label: dryad_congenital_glaucoma_wes
description: "Four exome difference files for three congenital-glaucoma families are directly translational human ocular genetics data."
tags: ["omics", "tabular", "cc0", "dryad", "classification", "resource-role-current-dataset", "dataset-family-dryad-congenital-glaucoma-wes"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Identification of novel variants in LTBP2 and PXDN using whole-exome sequencing in developmental and congenital glaucoma

Four exome difference files for three congenital-glaucoma families are directly translational human ocular genetics data.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_congenital_glaucoma_wes` |
| **Full name** | Identification of novel variants in LTBP2 and PXDN using whole-exome sequencing in developmental and congenital glaucoma |
| **Primary category** | `omics` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `dryad_congenital_glaucoma_wes` |
| **Contained modalities** | omics, tabular |
| **Tasks** | classification |
| **Primary reported quantity** | 3 families |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.442139301 GB |
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
| Primary | 3 | `families` | Source-stated primary resource quantity. Current official Dryad metadata. | `official_source_description` | [https://doi.org/10.5061/dryad.k7455](https://doi.org/10.5061/dryad.k7455) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Scope: core_add. Named file-level object: Four WES difference files. Official Dryad API metadata and current file listing reviewed 2026-08-01.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_congenital_glaucoma_wes --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dryad_congenital_glaucoma_wes --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_congenital_glaucoma_wes')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.k7455](https://doi.org/10.5061/dryad.k7455)

**Source-term evidence:** [https://doi.org/10.5061/dryad.k7455](https://doi.org/10.5061/dryad.k7455)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_congenital_glaucoma_wes,
  title  = { Identification of novel variants in LTBP2 and PXDN using whole-exome sequencing in developmental and congenital glaucoma },
  note   = { Identification of novel variants in LTBP2 and PXDN using whole-exome sequencing in developmental and congenital glaucoma. Dryad Dataset. doi:10.5061/dryad.k7455 },
  url    = { https://doi.org/10.5061/dryad.k7455 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Identification of novel variants in LTBP2 and PXDN using whole-exome sequencing in developmental and congenital glaucoma. Dryad Dataset. doi:10.5061/dryad.k7455.
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

- [dryad_uveitis_vitreous_biomarkers](./dryad_uveitis_vitreous_biomarkers.md): Uveitis Vitreous Biomarker Dataset (234 eyes, `cc0`)
- [dryad_dry_eye_nlrp3](./dryad_dry_eye_nlrp3.md): Dry Eye NLRP3 Ocular Surface Dataset (150 participants, `cc0`)
- [dryad_amd_zinc_complement](./dryad_amd_zinc_complement.md): AMD Zinc Complement Dataset (72 participants, `cc0`)
- [dryad_acanthamoeba_keratitis_transcriptome](./dryad_acanthamoeba_keratitis_transcriptome.md): Human conjunctival transcriptome in Acanthamoeba keratitis: An exploratory study (Not reported, `cc0`)
- [dryad_corneal_conjunctivitis_biomarker](./dryad_corneal_conjunctivitis_biomarker.md): Corneal Conjunctivitis Biomarker Dataset (Not reported, `cc0`)
- [dryad_glaucoma_lhon_mitochondrial](./dryad_glaucoma_lhon_mitochondrial.md): Glaucoma and LHON Mitochondrial Function Dataset (Not reported, `cc0`)
- [dryad_ocular_surface_amr](./dryad_ocular_surface_amr.md): Ocular Surface AMR Keratitis Dataset (Not reported, `cc0`)
- [dryad_rao_multiomics](./dryad_rao_multiomics.md): Data and code from: Fatty acid metabolism reprograms immune microenvironment in retinal artery occlusion: Multi-Omics analysis highlights immunometabolic crosstalk (Not reported, `cc0`)
