---
id: dual_scheimpflug_ss_oct_biometry
title: "Dual Scheimpflug and Swept-Source OCT Biometry Dataset"
sidebar_label: dual_scheimpflug_ss_oct_biometry
description: "Human ocular-biometry measurements from dual Scheimpflug and swept-source OCT instruments."
tags: ["tabular", "biometry", "cc-by", "figshare", "measurement", "resource-role-current-dataset", "dataset-family-dual-scheimpflug-ss-oct-biometry"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Dual Scheimpflug and Swept-Source OCT Biometry Dataset

Human ocular-biometry measurements from dual Scheimpflug and swept-source OCT instruments.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dual_scheimpflug_ss_oct_biometry` |
| **Full name** | Dual Scheimpflug and Swept-Source OCT Biometry Dataset |
| **First published** | 2021-10-19 |
| **Publication date precision** | day |
| **Publication date evidence** | [api.figshare.com/v2](https://api.figshare.com/v2/articles/16828996/versions/1) |
| **Publication date source field** | published_date (Figshare version 1) |
| **Publication date reviewed** | 2026-09-11 |
| **Primary category** | `tabular` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `dual_scheimpflug_ss_oct_biometry` |
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
eyehub download dual_scheimpflug_ss_oct_biometry --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dual_scheimpflug_ss_oct_biometry --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dual_scheimpflug_ss_oct_biometry')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.6084/m9.figshare.16828996.v1](https://doi.org/10.6084/m9.figshare.16828996.v1)

**Source-term evidence:** [https://doi.org/10.6084/m9.figshare.16828996.v1](https://doi.org/10.6084/m9.figshare.16828996.v1)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dual_scheimpflug_ss_oct_biometry,
  title  = { Dual Scheimpflug and Swept-Source OCT Biometry Dataset },
  note   = { Repository dataset record. 10.6084/m9.figshare.16828996.v1 },
  url    = { https://doi.org/10.6084/m9.figshare.16828996.v1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Repository dataset record. 10.6084/m9.figshare.16828996.v1.
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
- [cataract_lenstar_biometric_symmetry](./cataract_lenstar_biometric_symmetry.md): Cataract LenStar Biometric Symmetry Dataset (Not reported, `cc-by`)
- [ocular_chat_vqa](./ocular_chat_vqa.md): OcularChat-VQA: AREDS-Derived Patient-Physician Dialogue Dataset (844,000 records, `cc-by-nc-sa`)
- [brset_mbrset_embeddings](./brset_mbrset_embeddings.md): Embedding-Based Representations for BRSET and mBRSET (53,188 embedding vectors, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [oculoscope](./oculoscope.md): OculoScope: Fairer AI in Ophthalmology Dataset (16,530 images, `cc-by`)
- [dryad_r7s04](./dryad_r7s04.md): Data from: Prevalence of depression, anxiety, adjustment disorders, and somatoform disorders in patients with age-related macular degeneration in Germany (15,160 participants, `cc0`)
- [fairvlmed](./fairvlmed.md): FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset (10,000 images, `cc-by-nc-nd`)
