---
id: dryad_corneal_conjunctivitis_biomarker
title: "Corneal Conjunctivitis Biomarker Dataset"
sidebar_label: dryad_corneal_conjunctivitis_biomarker
description: "Human conjunctivitis count matrices and sample metadata are direct corneal-disease biomarker data."
tags: ["omics", "tabular", "cc0", "dryad", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Corneal Conjunctivitis Biomarker Dataset

Human conjunctivitis count matrices and sample metadata are direct corneal-disease biomarker data.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_corneal_conjunctivitis_biomarker` |
| **Full name** | Corneal Conjunctivitis Biomarker Dataset |
| **Primary category** | `omics` |
| **Contained modalities** | omics, tabular |
| **Tasks** | classification |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.008983041 GB |
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

No reproducible primary item count was exposed for the cataloged source version.

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Scope screen: core_add. Current Dryad v3 file listing: 4 files, 8983041 bytes.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_corneal_conjunctivitis_biomarker --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dryad_corneal_conjunctivitis_biomarker --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_corneal_conjunctivitis_biomarker')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.4j0zpc8mm](https://doi.org/10.5061/dryad.4j0zpc8mm)

**Source-term evidence:** [https://doi.org/10.5061/dryad.4j0zpc8mm](https://doi.org/10.5061/dryad.4j0zpc8mm)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_corneal_conjunctivitis_biomarker,
  title  = { Corneal Conjunctivitis Biomarker Dataset },
  note   = { Seitzman, Gerami, Lalitha, Prajna, Prajna, N. Venkatesh, Sansanayudh, Wiwan, Satitpitakul, Vannarut, Laovirojjanakul, Wipada, Chen, Cindi, Zhong, Lina, Ruder, Kevin, Redd, Travis, Deiner, Michael, Porco, Travis, McLeod, Stephen, Lietman, Thomas, Hinterwirth, Armin, and Doan, Thuy. Data from: Biomarker detection and validation for corneal involvement in patients with acute infectious conjunctivitis: A multi-country study. Dryad. 2025. doi:10.5061/dryad.4j0zpc8mm },
  year   = { 2025 },
  url    = { https://doi.org/10.5061/dryad.4j0zpc8mm },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Seitzman, Gerami, Lalitha, Prajna, Prajna, N. Venkatesh, Sansanayudh, Wiwan, Satitpitakul, Vannarut, Laovirojjanakul, Wipada, Chen, Cindi, Zhong, Lina, Ruder, Kevin, Redd, Travis, Deiner, Michael, Porco, Travis, McLeod, Stephen, Lietman, Thomas, Hinterwirth, Armin, and Doan, Thuy. Data from: Biomarker detection and validation for corneal involvement in patients with acute infectious conjunctivitis: A multi-country study. Dryad. 2025. doi:10.5061/dryad.4j0zpc8mm
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
- [dryad_congenital_glaucoma_wes](./dryad_congenital_glaucoma_wes.md): Identification of novel variants in LTBP2 and PXDN using whole-exome sequencing in developmental and congenital glaucoma (3 families, `cc0`)
- [dryad_acanthamoeba_keratitis_transcriptome](./dryad_acanthamoeba_keratitis_transcriptome.md): Human conjunctival transcriptome in Acanthamoeba keratitis: An exploratory study (Not reported, `cc0`)
- [dryad_glaucoma_lhon_mitochondrial](./dryad_glaucoma_lhon_mitochondrial.md): Glaucoma and LHON Mitochondrial Function Dataset (Not reported, `cc0`)
- [dryad_ocular_surface_amr](./dryad_ocular_surface_amr.md): Ocular Surface AMR Keratitis Dataset (Not reported, `cc0`)
- [dryad_rao_multiomics](./dryad_rao_multiomics.md): Data and code from: Fatty acid metabolism reprograms immune microenvironment in retinal artery occlusion: Multi-Omics analysis highlights immunometabolic crosstalk (Not reported, `cc0`)
