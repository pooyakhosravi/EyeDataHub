---
id: dryad_clcc1_retinitis_pigmentosa
title: "CLCC1 Retinitis Pigmentosa Genomics Dataset"
sidebar_label: dryad_clcc1_retinitis_pigmentosa
description: "Human retinitis-pigmentosa WES/SNP data from eight families directly support inherited-retinal-disease analysis."
tags: ["omics", "cc0", "dryad", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# CLCC1 Retinitis Pigmentosa Genomics Dataset

Human retinitis-pigmentosa WES/SNP data from eight families directly support inherited-retinal-disease analysis.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_clcc1_retinitis_pigmentosa` |
| **Full name** | CLCC1 Retinitis Pigmentosa Genomics Dataset |
| **Primary category** | `omics` |
| **Contained modalities** | omics |
| **Tasks** | classification |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.036634248 GB |
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

> Scope screen: core_add. Current Dryad v1 file listing: 1 files, 36607394 bytes.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_clcc1_retinitis_pigmentosa --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dryad_clcc1_retinitis_pigmentosa --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_clcc1_retinitis_pigmentosa')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.3vv31qq](https://doi.org/10.5061/dryad.3vv31qq)

**Source-term evidence:** [https://doi.org/10.5061/dryad.3vv31qq](https://doi.org/10.5061/dryad.3vv31qq)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_clcc1_retinitis_pigmentosa,
  title  = { CLCC1 Retinitis Pigmentosa Genomics Dataset },
  note   = { Li, Lin, Jiao, Xiaodong, D'Atri, Ilaria, Ono, Fumihito, Nelson, Ralph, Chan, Chi-Chao, Nakaya, Naoki, Ma, Zhiwei, Ma, Yan, Cai, Xiaoying, Zhang, Longhua, Lin, Siying, Hameed, Abdul, Chioza, Barry A., Hardy, Holly, Arno, Gavin, Hull, Sarah, Khan, Muhammad Imran, Fasham, James, Harlalka, V. Gaurav, Michaelides, Michel, Moore, Anthony T., Coban Akdemir, Zeynep Hande, Jhangiani, Shalini, Lupski, James R., Cremers, Frans P.M., Qamar, Raheel, Salman, Ahmed, Chilton, John, Self, Jay, Ayyagari, Radha, Kabir, Firoz, Naeem, Muhammad Asif, Ali, Muhammad, Akram, Javed, Sieving, Paul A., Riazuddin, Sheikh, Baple, Emma L., Riazuddin, Sheikh Amer, Crosby, Andrew H., Hejtmancik, J. Fielding, and Cremers, Frans P. M.. Data from: Mutation in the intracellular chloride channel CLCC1 associated with autosomal recessive retinitis pigmentosa. Dryad. 2019. doi:10.5061/dryad.3vv31qq },
  year   = { 2019 },
  url    = { https://doi.org/10.5061/dryad.3vv31qq },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Li, Lin, Jiao, Xiaodong, D'Atri, Ilaria, Ono, Fumihito, Nelson, Ralph, Chan, Chi-Chao, Nakaya, Naoki, Ma, Zhiwei, Ma, Yan, Cai, Xiaoying, Zhang, Longhua, Lin, Siying, Hameed, Abdul, Chioza, Barry A., Hardy, Holly, Arno, Gavin, Hull, Sarah, Khan, Muhammad Imran, Fasham, James, Harlalka, V. Gaurav, Michaelides, Michel, Moore, Anthony T., Coban Akdemir, Zeynep Hande, Jhangiani, Shalini, Lupski, James R., Cremers, Frans P.M., Qamar, Raheel, Salman, Ahmed, Chilton, John, Self, Jay, Ayyagari, Radha, Kabir, Firoz, Naeem, Muhammad Asif, Ali, Muhammad, Akram, Javed, Sieving, Paul A., Riazuddin, Sheikh, Baple, Emma L., Riazuddin, Sheikh Amer, Crosby, Andrew H., Hejtmancik, J. Fielding, and Cremers, Frans P. M.. Data from: Mutation in the intracellular chloride channel CLCC1 associated with autosomal recessive retinitis pigmentosa. Dryad. 2019. doi:10.5061/dryad.3vv31qq
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
- [dryad_uveal_melanoma_coog2](./dryad_uveal_melanoma_coog2.md): COOG2.1 Uveal Melanoma Prognostic Dataset (1,577 participants, `cc0`)
- [dryad_uveitis_vitreous_biomarkers](./dryad_uveitis_vitreous_biomarkers.md): Uveitis Vitreous Biomarker Dataset (234 eyes, `cc0`)
- [dryad_dry_eye_nlrp3](./dryad_dry_eye_nlrp3.md): Dry Eye NLRP3 Ocular Surface Dataset (150 participants, `cc0`)
- [dryad_amd_zinc_complement](./dryad_amd_zinc_complement.md): AMD Zinc Complement Dataset (72 participants, `cc0`)
- [dryad_stargardt_wes](./dryad_stargardt_wes.md): Stargardt Disease WES Variant Dataset (33 participants, `cc0`)
- [dryad_congenital_glaucoma_wes](./dryad_congenital_glaucoma_wes.md): Identification of novel variants in LTBP2 and PXDN using whole-exome sequencing in developmental and congenital glaucoma (3 families, `cc0`)
- [dryad_ird_mouse_proteome](./dryad_ird_mouse_proteome.md): Retinal proteome profiling of inherited retinal degeneration across three different mouse models suggests common drug targets in retinitis pigmentosa (3 animal models, `cc0`)
