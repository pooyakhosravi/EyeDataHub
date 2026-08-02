---
id: dryad_retinal_pufa_aging_mouse
title: "Retinal polyunsaturated fatty acid supplementation reverses aging-related vision decline in mice"
sidebar_label: dryad_retinal_pufa_aging_mouse
description: "Fourteen named retinal lipidomic and expression tables define a disease-mechanism resource for retinal aging."
tags: ["omics", "tabular", "cc0", "dryad", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Retinal polyunsaturated fatty acid supplementation reverses aging-related vision decline in mice

Fourteen named retinal lipidomic and expression tables define a disease-mechanism resource for retinal aging.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_retinal_pufa_aging_mouse` |
| **Full name** | Retinal polyunsaturated fatty acid supplementation reverses aging-related vision decline in mice |
| **Primary category** | `omics` |
| **Contained modalities** | omics, tabular |
| **Tasks** | classification |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.013798287 GB |
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

> Scope: adjacent_add. Named file-level object: Retinal lipidomics/transcript/protein tables plus README. Official Dryad API metadata and current file listing reviewed 2026-08-01.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_retinal_pufa_aging_mouse --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dryad_retinal_pufa_aging_mouse --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_retinal_pufa_aging_mouse')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.gxd25480h](https://doi.org/10.5061/dryad.gxd25480h)

**Source-term evidence:** [https://doi.org/10.5061/dryad.gxd25480h](https://doi.org/10.5061/dryad.gxd25480h)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_retinal_pufa_aging_mouse,
  title  = { Retinal polyunsaturated fatty acid supplementation reverses aging-related vision decline in mice },
  note   = { Retinal polyunsaturated fatty acid supplementation reverses aging-related vision decline in mice. Dryad Dataset. doi:10.5061/dryad.gxd25480h },
  url    = { https://doi.org/10.5061/dryad.gxd25480h },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Retinal polyunsaturated fatty acid supplementation reverses aging-related vision decline in mice. Dryad Dataset. doi:10.5061/dryad.gxd25480h.
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

- [dryad_canine_pra_cea_genotypes](./dryad_canine_pra_cea_genotypes.md): Canine PRA and CEA Genotype Dataset (86,667 records, `cc0`)
- [dryad_uveitis_vitreous_biomarkers](./dryad_uveitis_vitreous_biomarkers.md): Uveitis Vitreous Biomarker Dataset (234 eyes, `cc0`)
- [dryad_dry_eye_nlrp3](./dryad_dry_eye_nlrp3.md): Dry Eye NLRP3 Ocular Surface Dataset (150 participants, `cc0`)
- [dryad_amd_zinc_complement](./dryad_amd_zinc_complement.md): AMD Zinc Complement Dataset (72 participants, `cc0`)
- [dryad_congenital_glaucoma_wes](./dryad_congenital_glaucoma_wes.md): Identification of novel variants in LTBP2 and PXDN using whole-exome sequencing in developmental and congenital glaucoma (3 families, `cc0`)
- [dryad_ird_mouse_proteome](./dryad_ird_mouse_proteome.md): Retinal proteome profiling of inherited retinal degeneration across three different mouse models suggests common drug targets in retinitis pigmentosa (3 animal models, `cc0`)
- [dryad_acanthamoeba_keratitis_transcriptome](./dryad_acanthamoeba_keratitis_transcriptome.md): Human conjunctival transcriptome in Acanthamoeba keratitis: An exploratory study (Not reported, `cc0`)
- [dryad_corneal_conjunctivitis_biomarker](./dryad_corneal_conjunctivitis_biomarker.md): Corneal Conjunctivitis Biomarker Dataset (Not reported, `cc0`)
