---
id: dryad_crvo_vegf_tortuosity
title: "CRVO Retinal Tortuosity and VEGF Dataset"
sidebar_label: dryad_crvo_vegf_tortuosity
description: "The 32-eye CRVO tortuosity/VEGF table is direct human retinal vascular disease data."
tags: ["tabular", "cc0", "dryad", "regression", "resource-role-current-dataset", "dataset-family-dryad-crvo-vegf-tortuosity"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# CRVO Retinal Tortuosity and VEGF Dataset

The 32-eye CRVO tortuosity/VEGF table is direct human retinal vascular disease data.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_crvo_vegf_tortuosity` |
| **Full name** | CRVO Retinal Tortuosity and VEGF Dataset |
| **Publication date** | 2016-07-16 |
| **Date basis** | Initial dataset release |
| **Publication date precision** | day |
| **Publication date evidence** | [datadryad.org/api](https://datadryad.org/api/v2/datasets/doi%3A10.5061%2Fdryad.5dn13) |
| **Publication date source field** | publicationDate |
| **Publication date reviewed** | 2026-09-11 |
| **Date notes** | Official Dryad API v2 publicationDate; current record version 1 and later lastModificationDate do not replace the publication date. |
| **Primary category** | `tabular` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `dryad_crvo_vegf_tortuosity` |
| **Contained modalities** | tabular |
| **Tasks** | regression |
| **Primary reported quantity** | 32 eyes |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 3.8504e-05 GB |
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
| Primary | 32 | `eyes` | Source-described central retinal vein occlusion eyes Source-stated quantity; Dryad file count is separate metadata and is not a scientific sample count. | `official_source_description` | [https://doi.org/10.5061/dryad.5dn13](https://doi.org/10.5061/dryad.5dn13) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Scope screen: core_add. Current Dryad v1 file listing: 1 files, 18399 bytes.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_crvo_vegf_tortuosity --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dryad_crvo_vegf_tortuosity --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_crvo_vegf_tortuosity')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.5dn13](https://doi.org/10.5061/dryad.5dn13)

**Source-term evidence:** [https://doi.org/10.5061/dryad.5dn13](https://doi.org/10.5061/dryad.5dn13)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_crvo_vegf_tortuosity,
  title  = { CRVO Retinal Tortuosity and VEGF Dataset },
  note   = { Yasuda, Shunsuke, Kachi, Shu, Kondo, Mineo, Ueno, Shinji, Kaneko, Hiroki, and Terasaki, Hiroko. Data from: Significant correlation between retinal venous tortuosity and aqueous vascular endothelial growth factor concentration in eyes with central retinal vein occlusion. Dryad. 2016. doi:10.5061/dryad.5dn13 },
  year   = { 2016 },
  url    = { https://doi.org/10.5061/dryad.5dn13 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Yasuda, Shunsuke, Kachi, Shu, Kondo, Mineo, Ueno, Shinji, Kaneko, Hiroki, and Terasaki, Hiroko. Data from: Significant correlation between retinal venous tortuosity and aqueous vascular endothelial growth factor concentration in eyes with central retinal vein occlusion. Dryad. 2016. doi:10.5061/dryad.5dn13
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
- [brset_mbrset_embeddings](./brset_mbrset_embeddings.md): Embedding-Based Representations for BRSET and mBRSET (53,188 embedding vectors, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [oculoscope](./oculoscope.md): OculoScope: Fairer AI in Ophthalmology Dataset (16,530 images, `cc-by`)
- [dryad_r7s04](./dryad_r7s04.md): Data from: Prevalence of depression, anxiety, adjustment disorders, and somatoform disorders in patients with age-related macular degeneration in Germany (15,160 participants, `cc0`)
- [fairvlmed](./fairvlmed.md): FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset (10,000 images, `cc-by-nc-nd`)
- [leops_erg](./leops_erg.md): LEOPs Light-Adapted Electroretinogram and Oscillatory Potentials Dataset (9,743 signals, `cc-by`)
- [dryad_icmr_eye_see_cataract](./dryad_icmr_eye_see_cataract.md): ICMR EYE SEE Cataract and Sun Exposure Dataset (9,735 participants, `cc0`)
