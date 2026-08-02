---
id: eed_astig
title: "EED-Astig Pediatric External-Eye Dataset"
sidebar_label: eed_astig
description: "Pediatric external-eye photographs with gaze-view annotations, corneal masks, eyelid/eyelash-line keypoints, and clinical tabular parameters for astigmatism-related research."
tags: ["external_eye", "tabular", "research-only", "manual", "segmentation", "landmark_detection", "regression"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# EED-Astig Pediatric External-Eye Dataset

Pediatric external-eye photographs with gaze-view annotations, corneal masks, eyelid/eyelash-line keypoints, and clinical tabular parameters for astigmatism-related research.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `eed_astig` |
| **Full name** | EED-Astig Pediatric External-Eye Dataset |
| **Primary category** | `external_eye` |
| **Contained modalities** | external_eye, tabular |
| **Tasks** | segmentation, landmark_detection, regression |
| **Primary reported quantity** | 3,088 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.42 GB |
| **Source-stated terms** | Data Use Agreement; non-commercial research only |
| **Normalized terms** | `research-only` |
| **Descriptive screening label** | Research or challenge restriction recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `controlled_or_manual` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `manual_access_blocked` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 3,088 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [https://doi.org/10.5281/zenodo.18976824](https://doi.org/10.5281/zenodo.18976824) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Zenodo record describes 640 children aged 3-6 years with 3,088 external-eye image files, JSON annotations, masks/keypoints, and Parameter.xls. Access requires explicit agreement to a data-use agreement and is non-commercial research only.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# This route requires upstream human action; no transfer starts.
eyehub download eed_astig --data-dir ./data --dry-run --json
# Follow the official instructions shown by preflight.
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('eed_astig')
print(preflight_dataset(ds, './data'))  # returns manual_access_blocked
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5281/zenodo.18976824](https://doi.org/10.5281/zenodo.18976824)

**Source-term evidence:** [https://doi.org/10.5281/zenodo.18976824](https://doi.org/10.5281/zenodo.18976824)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{eed_astig,
  title  = { EED-Astig Pediatric External-Eye Dataset },
  note   = { Liu H, Lv Y, Li S, Liu R, Hou X, Chen F, Liu Y, You J, Wang H, Liu S. EED-Astig. Zenodo, 2026. doi:10.5281/zenodo.18976824 },
  year   = { 2026 },
  url    = { https://doi.org/10.5281/zenodo.18976824 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Liu H, Lv Y, Li S, Liu R, Hou X, Chen F, Liu Y, You J, Wang H, Liu S. EED-Astig. Zenodo, 2026. doi:10.5281/zenodo.18976824
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Data Use Agreement; non-commercial research only
- **Normalized category:** `research-only`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Research or challenge restriction recorded; check source

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [uveitis_smote](./uveitis_smote.md): Image Dataset on Eye Diseases Classification with Symptoms and SMOTE Validation (3,245 images, `cc-by`)
- [dryad_sbcc2fr6n](./dryad_sbcc2fr6n.md): Exploring phenotypic diversity of pigmented traits and iris features in Pakistani population (514 participants, `cc0`)
- [dryad_iris_surface_features](./dryad_iris_surface_features.md): Iris Surface Features Dataset (Not reported, `cc0`)
- [ocular_chat_vqa](./ocular_chat_vqa.md): OcularChat-VQA: AREDS-Derived Patient-Physician Dialogue Dataset (844,000 records, `cc-by-nc-sa`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [dryad_canine_pra_cea_genotypes](./dryad_canine_pra_cea_genotypes.md): Canine PRA and CEA Genotype Dataset (86,667 records, `cc0`)
- [brset_mbrset_embeddings](./brset_mbrset_embeddings.md): Embedding-Based Representations for BRSET and mBRSET (53,188 embedding vectors, `unknown`)
