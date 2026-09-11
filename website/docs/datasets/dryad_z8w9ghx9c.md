---
id: dryad_z8w9ghx9c
title: "Accuracy of intraocular lens calculation formulas in cataract patients with steep corneal curvature"
sidebar_label: dryad_z8w9ghx9c
description: "Official Dryad deposit of source-described tabular ophthalmic data for the associated study."
tags: ["tabular", "cc0", "dryad", "regression", "resource-role-current-dataset", "dataset-family-dryad-z8w9ghx9c"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Accuracy of intraocular lens calculation formulas in cataract patients with steep corneal curvature

Official Dryad deposit of source-described tabular ophthalmic data for the associated study.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_z8w9ghx9c` |
| **Full name** | Accuracy of intraocular lens calculation formulas in cataract patients with steep corneal curvature |
| **First published** | 2020-10-26 |
| **Publication date precision** | day |
| **Publication date evidence** | [https://doi.org/10.5061/dryad.z8w9ghx9c](https://doi.org/10.5061/dryad.z8w9ghx9c) |
| **Publication date source field** | Published |
| **Publication date reviewed** | 2026-09-11 |
| **Primary category** | `tabular` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `dryad_z8w9ghx9c` |
| **Contained modalities** | tabular |
| **Tasks** | regression |
| **Primary reported quantity** | 112 eyes |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.000120727 GB |
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
| Primary | 112 | `eyes` | Source-described cataract eyes for IOL formula evaluation Source-stated scientific quantity; current Dryad file count is separate repository metadata. | `official_source_description` | [https://doi.org/10.5061/dryad.z8w9ghx9c](https://doi.org/10.5061/dryad.z8w9ghx9c) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Scope screen: core_add. Current Dryad v3 file listing: 1 files, 120727 bytes.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_z8w9ghx9c --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dryad_z8w9ghx9c --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_z8w9ghx9c')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.z8w9ghx9c](https://doi.org/10.5061/dryad.z8w9ghx9c)

**Source-term evidence:** [https://doi.org/10.5061/dryad.z8w9ghx9c](https://doi.org/10.5061/dryad.z8w9ghx9c)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_z8w9ghx9c,
  title  = { Accuracy of intraocular lens calculation formulas in cataract patients with steep corneal curvature },
  note   = { Pazo Emmanuel, Zhang Chenguang, Dai Guangzheng, Liu Shasha, He Wei, Xu Ling. Accuracy of intraocular lens calculation formulas in cataract patients with steep corneal curvature. Dryad. 2020. doi:10.5061/dryad.z8w9ghx9c },
  year   = { 2020 },
  url    = { https://doi.org/10.5061/dryad.z8w9ghx9c },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Pazo Emmanuel, Zhang Chenguang, Dai Guangzheng, Liu Shasha, He Wei, Xu Ling. Accuracy of intraocular lens calculation formulas in cataract patients with steep corneal curvature. Dryad. 2020. doi:10.5061/dryad.z8w9ghx9c
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
