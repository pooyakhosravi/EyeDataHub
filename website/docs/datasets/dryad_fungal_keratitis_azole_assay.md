---
id: dryad_fungal_keratitis_azole_assay
title: "Phase-dependent differential in vitro and ex vivo susceptibility of Aspergillus flavus and Fusarium keratoplasticum to azole antifungals"
sidebar_label: dryad_fungal_keratitis_azole_assay
description: "The raw corneal-coverage and absorbance CSVs are a defined fungal-keratitis drug-response assay resource."
tags: ["tabular", "cc0", "dryad", "evaluation"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Phase-dependent differential in vitro and ex vivo susceptibility of Aspergillus flavus and Fusarium keratoplasticum to azole antifungals

The raw corneal-coverage and absorbance CSVs are a defined fungal-keratitis drug-response assay resource.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_fungal_keratitis_azole_assay` |
| **Full name** | Phase-dependent differential in vitro and ex vivo susceptibility of Aspergillus flavus and Fusarium keratoplasticum to azole antifungals |
| **Primary category** | `tabular` |
| **Contained modalities** | tabular |
| **Tasks** | evaluation |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 7.4796e-05 GB |
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

> Scope: adjacent_add. Named file-level object: Two raw assay CSVs plus README. Official Dryad API metadata and current file listing reviewed 2026-08-01.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_fungal_keratitis_azole_assay --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dryad_fungal_keratitis_azole_assay --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_fungal_keratitis_azole_assay')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.bk3j9kdjf](https://doi.org/10.5061/dryad.bk3j9kdjf)

**Source-term evidence:** [https://doi.org/10.5061/dryad.bk3j9kdjf](https://doi.org/10.5061/dryad.bk3j9kdjf)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_fungal_keratitis_azole_assay,
  title  = { Phase-dependent differential in vitro and ex vivo susceptibility of Aspergillus flavus and Fusarium keratoplasticum to azole antifungals },
  note   = { Phase-dependent differential in vitro and ex vivo susceptibility of Aspergillus flavus and Fusarium keratoplasticum to azole antifungals. Dryad Dataset. doi:10.5061/dryad.bk3j9kdjf },
  url    = { https://doi.org/10.5061/dryad.bk3j9kdjf },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Phase-dependent differential in vitro and ex vivo susceptibility of Aspergillus flavus and Fusarium keratoplasticum to azole antifungals. Dryad Dataset. doi:10.5061/dryad.bk3j9kdjf.
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

- [ocular_chat_vqa](./ocular_chat_vqa.md): OcularChat-VQA: AREDS-Derived Patient-Physician Dialogue Dataset (844,000 records, `cc-by-nc-sa`)
- [dryad_canine_pra_cea_genotypes](./dryad_canine_pra_cea_genotypes.md): Canine PRA and CEA Genotype Dataset (86,667 records, `cc0`)
- [brset_mbrset_embeddings](./brset_mbrset_embeddings.md): Embedding-Based Representations for BRSET and mBRSET (53,188 embedding vectors, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [oculoscope](./oculoscope.md): OculoScope: Fairer AI in Ophthalmology Dataset (16,530 images, `cc-by`)
- [dryad_r7s04](./dryad_r7s04.md): Data from: Prevalence of depression, anxiety, adjustment disorders, and somatoform disorders in patients with age-related macular degeneration in Germany (15,160 participants, `cc0`)
- [fairvlmed](./fairvlmed.md): FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset (10,000 images, `cc-by-nc-nd`)
- [leops_erg](./leops_erg.md): LEOPs Light-Adapted Electroretinogram and Oscillatory Potentials Dataset (9,743 signals, `cc-by`)
