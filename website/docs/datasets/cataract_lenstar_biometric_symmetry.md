---
id: cataract_lenstar_biometric_symmetry
title: "Cataract LenStar Biometric Symmetry Dataset"
sidebar_label: cataract_lenstar_biometric_symmetry
description: "Bilateral LenStar biometrics from a human cataract population."
tags: ["tabular", "biometry", "cc-by", "figshare", "measurement", "resource-role-current-dataset", "dataset-family-cataract-lenstar-biometric-symmetry"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Cataract LenStar Biometric Symmetry Dataset

Bilateral LenStar biometrics from a human cataract population.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `cataract_lenstar_biometric_symmetry` |
| **Full name** | Cataract LenStar Biometric Symmetry Dataset |
| **Publication date** | 2026-06-30 |
| **Date basis** | Initial dataset release |
| **Publication date precision** | day |
| **Publication date evidence** | [api.figshare.com/v2](https://api.figshare.com/v2/articles/32833895/versions/1) |
| **Publication date source field** | published_date (Figshare version 1) |
| **Publication date reviewed** | 2026-09-11 |
| **Date notes** | Only listed Figshare version. |
| **Primary category** | `tabular` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `cataract_lenstar_biometric_symmetry` |
| **Contained modalities** | tabular, biometry |
| **Tasks** | measurement |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Figshare |
| **Availability** | `available` (checked 2026-08-02) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

No reproducible primary item count was exposed for the cataloged source version.

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download cataract_lenstar_biometric_symmetry --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download cataract_lenstar_biometric_symmetry --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('cataract_lenstar_biometric_symmetry')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.6084/m9.figshare.32833895.v1](https://doi.org/10.6084/m9.figshare.32833895.v1)

**Source-term evidence:** [https://doi.org/10.6084/m9.figshare.32833895.v1](https://doi.org/10.6084/m9.figshare.32833895.v1)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{cataract_lenstar_biometric_symmetry,
  title  = { Cataract LenStar Biometric Symmetry Dataset },
  note   = { Repository dataset record. 10.6084/m9.figshare.32833895.v1 },
  url    = { https://doi.org/10.6084/m9.figshare.32833895.v1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Repository dataset record. 10.6084/m9.figshare.32833895.v1.
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

- [cataract_iol_biometry_outcomes](./cataract_iol_biometry_outcomes.md): Cataract IOL Biometry and Outcomes Dataset (Not reported, `cc-by`)
- [dual_scheimpflug_ss_oct_biometry](./dual_scheimpflug_ss_oct_biometry.md): Dual Scheimpflug and Swept-Source OCT Biometry Dataset (Not reported, `cc-by`)
- [ocular_chat_vqa](./ocular_chat_vqa.md): OcularChat-VQA: AREDS-Derived Patient-Physician Dialogue Dataset (844,000 records, `cc-by-nc-sa`)
- [brset_mbrset_embeddings](./brset_mbrset_embeddings.md): Embedding-Based Representations for BRSET and mBRSET (53,188 embedding vectors, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [oculoscope](./oculoscope.md): OculoScope: Fairer AI in Ophthalmology Dataset (16,530 images, `cc-by`)
- [dryad_r7s04](./dryad_r7s04.md): Data from: Prevalence of depression, anxiety, adjustment disorders, and somatoform disorders in patients with age-related macular degeneration in Germany (15,160 participants, `cc0`)
- [fairvlmed](./fairvlmed.md): FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset (10,000 images, `cc-by-nc-nd`)
