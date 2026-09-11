---
id: dryad_xgxd254pk
title: "Supporting information for: Discrimination ability of central visual field testing using stimulus size I, II, and III and relationship with macular ganglion cell thickness in chiasmal compression"
sidebar_label: dryad_xgxd254pk
description: "Official Dryad deposit of source-described visual-field and retinal measurement data for the associated study."
tags: ["visual_field", "tabular", "cc0", "dryad", "measurement", "resource-role-current-dataset", "dataset-family-dryad-xgxd254pk"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Supporting information for: Discrimination ability of central visual field testing using stimulus size I, II, and III and relationship with macular ganglion cell thickness in chiasmal compression

Official Dryad deposit of source-described visual-field and retinal measurement data for the associated study.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_xgxd254pk` |
| **Full name** | Supporting information for: Discrimination ability of central visual field testing using stimulus size I, II, and III and relationship with macular ganglion cell thickness in chiasmal compression |
| **Publication date** | 2024-01-29 |
| **Date basis** | Initial dataset release |
| **Publication date precision** | day |
| **Publication date evidence** | [https://doi.org/10.5061/dryad.xgxd254pk](https://doi.org/10.5061/dryad.xgxd254pk) |
| **Publication date source field** | Published |
| **Publication date reviewed** | 2026-09-11 |
| **Date notes** | - |
| **Primary category** | `visual_field` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `dryad_xgxd254pk` |
| **Contained modalities** | visual_field, tabular |
| **Tasks** | measurement |
| **Primary reported quantity** | 60 eyes |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.000333966 GB |
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
| Primary | 60 | `eyes` | Source-described patient and control eyes in visual-field study Source-stated scientific quantity; current Dryad file count is separate repository metadata. | `official_source_description` | [https://doi.org/10.5061/dryad.xgxd254pk](https://doi.org/10.5061/dryad.xgxd254pk) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Scope screen: core_add. Current Dryad v5 file listing: 2 files, 333966 bytes.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_xgxd254pk --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dryad_xgxd254pk --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_xgxd254pk')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.xgxd254pk](https://doi.org/10.5061/dryad.xgxd254pk)

**Source-term evidence:** [https://doi.org/10.5061/dryad.xgxd254pk](https://doi.org/10.5061/dryad.xgxd254pk)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_xgxd254pk,
  title  = { Supporting information for: Discrimination ability of central visual field testing using stimulus size I, II, and III and relationship with macular ganglion cell thickness in chiasmal compression },
  note   = { Monteiro Mario, Rocha Arthur, Benassi Thais, Mello Luiz, Zacharias Leandro, Preti Rony, Cunha Leonardo. Supporting information for: Discrimination ability of central visual field testing using stimulus size I, II, and III and relationship with macular ganglion cell thickness in chiasmal compression. Dryad. 2024. doi:10.5061/dryad.xgxd254pk },
  year   = { 2024 },
  url    = { https://doi.org/10.5061/dryad.xgxd254pk },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Monteiro Mario, Rocha Arthur, Benassi Thais, Mello Luiz, Zacharias Leandro, Preti Rony, Cunha Leonardo. Supporting information for: Discrimination ability of central visual field testing using stimulus size I, II, and III and relationship with macular ganglion cell thickness in chiasmal compression. Dryad. 2024. doi:10.5061/dryad.xgxd254pk
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

- [fairvlmed](./fairvlmed.md): FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset (10,000 images, `cc-by-nc-nd`)
- [grape](./grape.md): GRAPE: Glaucoma Real-world Appraisal Progression Ensemble (1,115 examinations, `cc0`)
- [harvard_gdp](./harvard_gdp.md): Harvard GDP: Glaucoma Detection and Progression Dataset (1,000 participants, `cc-by-nc-nd`)
- [dryad_glaucoma_rnfl_vf](./dryad_glaucoma_rnfl_vf.md): RNFL and Visual-Field Glaucoma Diagnosis Dataset (499 records, `cc0`)
- [dryad_myopia_glaucoma_visual_field](./dryad_myopia_glaucoma_visual_field.md): Myopia and Glaucoma Visual Field Prognosis Dataset (270 eyes, `cc0`)
- [ocular_chat_vqa](./ocular_chat_vqa.md): OcularChat-VQA: AREDS-Derived Patient-Physician Dialogue Dataset (844,000 records, `cc-by-nc-sa`)
- [brset_mbrset_embeddings](./brset_mbrset_embeddings.md): Embedding-Based Representations for BRSET and mBRSET (53,188 embedding vectors, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
