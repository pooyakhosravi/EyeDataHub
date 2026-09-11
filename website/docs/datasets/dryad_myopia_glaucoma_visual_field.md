---
id: dryad_myopia_glaucoma_visual_field
title: "Myopia and Glaucoma Visual Field Prognosis Dataset"
sidebar_label: dryad_myopia_glaucoma_visual_field
description: "The 270-eye glaucoma visual-field dataset directly supports prognosis and progression analysis."
tags: ["visual_field", "tabular", "cc0", "dryad", "prognosis", "regression", "resource-role-current-dataset", "dataset-family-dryad-myopia-glaucoma-visual-field"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Myopia and Glaucoma Visual Field Prognosis Dataset

The 270-eye glaucoma visual-field dataset directly supports prognosis and progression analysis.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_myopia_glaucoma_visual_field` |
| **Full name** | Myopia and Glaucoma Visual Field Prognosis Dataset |
| **First published** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Primary category** | `visual_field` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `dryad_myopia_glaucoma_visual_field` |
| **Contained modalities** | visual_field, tabular |
| **Tasks** | prognosis, regression |
| **Primary reported quantity** | 270 eyes |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.000100077 GB |
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
| Primary | 270 | `eyes` | Source-described primary open-angle glaucoma eyes Source-stated quantity; Dryad file count is separate metadata and is not a scientific sample count. | `official_source_description` | [https://doi.org/10.5061/dryad.1n50q](https://doi.org/10.5061/dryad.1n50q) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Scope screen: core_add. Current Dryad v1 file listing: 1 files, 77824 bytes.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_myopia_glaucoma_visual_field --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dryad_myopia_glaucoma_visual_field --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_myopia_glaucoma_visual_field')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.1n50q](https://doi.org/10.5061/dryad.1n50q)

**Source-term evidence:** [https://doi.org/10.5061/dryad.1n50q](https://doi.org/10.5061/dryad.1n50q)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_myopia_glaucoma_visual_field,
  title  = { Myopia and Glaucoma Visual Field Prognosis Dataset },
  note   = { Qiu, Chen, Qian, Shaohong, Sun, Xinghuai, Zhou, Chuandi, and Meng, Fanrong. Data from: Axial myopia is associated with visual field prognosis of primary open-angle glaucoma. Dryad. 2015. doi:10.5061/dryad.1n50q },
  year   = { 2015 },
  url    = { https://doi.org/10.5061/dryad.1n50q },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Qiu, Chen, Qian, Shaohong, Sun, Xinghuai, Zhou, Chuandi, and Meng, Fanrong. Data from: Axial myopia is associated with visual field prognosis of primary open-angle glaucoma. Dryad. 2015. doi:10.5061/dryad.1n50q
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
- [dryad_xgxd254pk](./dryad_xgxd254pk.md): Supporting information for: Discrimination ability of central visual field testing using stimulus size I, II, and III and relationship with macular ganglion cell thickness in chiasmal compression (60 eyes, `cc0`)
- [ocular_chat_vqa](./ocular_chat_vqa.md): OcularChat-VQA: AREDS-Derived Patient-Physician Dialogue Dataset (844,000 records, `cc-by-nc-sa`)
- [brset_mbrset_embeddings](./brset_mbrset_embeddings.md): Embedding-Based Representations for BRSET and mBRSET (53,188 embedding vectors, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
