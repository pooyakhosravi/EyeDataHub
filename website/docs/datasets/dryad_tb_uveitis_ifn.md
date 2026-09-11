---
id: dryad_tb_uveitis_ifn
title: "Type 1 interferon-inducible gene expression in QuantiFERON Gold TB-positive uveitis: a tool to stratify a high versus low risk of active tuberculosis?"
sidebar_label: dryad_tb_uveitis_ifn
description: "The human uveitis expression workbook has a stated 103-enrollment cohort and supports ocular biomarker classification."
tags: ["omics", "tabular", "cc0", "dryad", "classification", "resource-role-current-dataset", "dataset-family-dryad-tb-uveitis-ifn"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Type 1 interferon-inducible gene expression in QuantiFERON Gold TB-positive uveitis: a tool to stratify a high versus low risk of active tuberculosis?

The human uveitis expression workbook has a stated 103-enrollment cohort and supports ocular biomarker classification.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_tb_uveitis_ifn` |
| **Full name** | Type 1 interferon-inducible gene expression in QuantiFERON Gold TB-positive uveitis: a tool to stratify a high versus low risk of active tuberculosis? |
| **First published** | 2018-11-07 |
| **Publication date precision** | day |
| **Publication date evidence** | [https://doi.org/10.5061/dryad.8jk03jd](https://doi.org/10.5061/dryad.8jk03jd) |
| **Publication date source field** | Published |
| **Publication date reviewed** | 2026-09-11 |
| **Primary category** | `omics` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `dryad_tb_uveitis_ifn` |
| **Contained modalities** | omics, tabular |
| **Tasks** | classification |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 7.6872e-05 GB |
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

> Scope: core_add. Named file-level object: Type I IFN gene signature workbook. No explicit single primary resource total is stated. Official Dryad API metadata and current file listing reviewed 2026-08-01.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_tb_uveitis_ifn --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dryad_tb_uveitis_ifn --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_tb_uveitis_ifn')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.8jk03jd](https://doi.org/10.5061/dryad.8jk03jd)

**Source-term evidence:** [https://doi.org/10.5061/dryad.8jk03jd](https://doi.org/10.5061/dryad.8jk03jd)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_tb_uveitis_ifn,
  title  = { Type 1 interferon-inducible gene expression in QuantiFERON Gold TB-positive uveitis: a tool to stratify a high versus low risk of active tuberculosis? },
  note   = { Type 1 interferon-inducible gene expression in QuantiFERON Gold TB-positive uveitis: a tool to stratify a high versus low risk of active tuberculosis?. Dryad Dataset. doi:10.5061/dryad.8jk03jd },
  url    = { https://doi.org/10.5061/dryad.8jk03jd },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Type 1 interferon-inducible gene expression in QuantiFERON Gold TB-positive uveitis: a tool to stratify a high versus low risk of active tuberculosis?. Dryad Dataset. doi:10.5061/dryad.8jk03jd.
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
- [dryad_corneal_conjunctivitis_biomarker](./dryad_corneal_conjunctivitis_biomarker.md): Corneal Conjunctivitis Biomarker Dataset (Not reported, `cc0`)
- [dryad_glaucoma_lhon_mitochondrial](./dryad_glaucoma_lhon_mitochondrial.md): Glaucoma and LHON Mitochondrial Function Dataset (Not reported, `cc0`)
- [dryad_ocular_surface_amr](./dryad_ocular_surface_amr.md): Ocular Surface AMR Keratitis Dataset (Not reported, `cc0`)
