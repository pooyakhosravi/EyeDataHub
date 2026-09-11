---
id: papila
title: "PAPILA: Glaucoma Fundus Dataset with Clinical Data"
sidebar_label: papila
description: "488 fundus images from 244 patients (both eyes). Expert OD/OC segmentation, glaucoma stage, IOP, and clinical metadata."
tags: ["fundus", "tabular", "cc-by", "direct", "classification", "segmentation", "resource-role-current-dataset", "dataset-family-papila", "documented-relationship", "relationship-derived_from"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# PAPILA: Glaucoma Fundus Dataset with Clinical Data

488 fundus images from 244 patients (both eyes). Expert OD/OC segmentation, glaucoma stage, IOP, and clinical metadata.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `papila` |
| **Full name** | PAPILA: Glaucoma Fundus Dataset with Clinical Data |
| **First published** | 2022-04-29 |
| **Publication date precision** | day |
| **Publication date evidence** | [api.figshare.com/v2](https://api.figshare.com/v2/articles/14798004/versions/1) |
| **Publication date source field** | published_date (original Figshare version 1) |
| **Publication date reviewed** | 2026-09-11 |
| **Primary category** | `fundus` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `papila` |
| **Contained modalities** | fundus, tabular |
| **Tasks** | classification, segmentation |
| **Primary reported quantity** | 488 images |
| **Classes** | 3 (Healthy, Glaucoma suspect, Glaucoma) |
| **Splits** | all |
| **Size** | 0.4 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Direct HTTP |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `guided_instructions_only` |
| **Legacy sample-loader status** | Standard loader included |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 488 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [zenodo.org/records](https://zenodo.org/records/6379970) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- [glaucoma_expert_cot_refined](./glaucoma_expert_cot_refined.md) is `derived from` this record: The official dataset card identifies LAG and PAPILA as the source fundus resources paired with the refined glaucoma reasoning records. ([evidence](https://huggingface.co/datasets/yuzhench/glaucoma-expert-cot-refined-1077))
- [mm_retinal_reason](./mm_retinal_reason.md) is `derived from` this record: The version-pinned official dataset card lists this record among the CFP or OCT sources used to construct MM-Retinal-Reason. ([evidence](https://huggingface.co/datasets/lxirich/MM-Retinal-Reason/tree/d6243baa82c0914dba3c6f43ca79fdbf856982ef))
- [smdg](./smdg.md) is `derived from` this record: The official SMDG source table lists this catalog record among the 19 standardized source domains. ([evidence](https://www.kaggle.com/datasets/deathtrooper/multichannel-glaucoma-benchmark-dataset))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download papila --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download papila --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('papila')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [zenodo.org/records](https://zenodo.org/records/6379970)

**Source-term evidence:** [zenodo.org/records](https://zenodo.org/records/6379970)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('papila')
samples = ds.load(data_dir, split='all')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{papila,
  title  = { PAPILA: Glaucoma Fundus Dataset with Clinical Data },
  note   = { Kovalyk et al., 'PAPILA: Dataset with fundus images and clinical data of both eyes of the same patient for glaucoma assessment', Scientific Data 2022 },
  year   = { 2022 },
  url    = { https://zenodo.org/records/6379970 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Kovalyk et al., 'PAPILA: Dataset with fundus images and clinical data of both eyes of the same patient for glaucoma assessment', Scientific Data 2022.
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

- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [fairvlmed](./fairvlmed.md): FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset (10,000 images, `cc-by-nc-nd`)
- [olives](./olives.md): OLIVES: Ophthalmic Labels for Investigating Visual Eye Semantics (9,408 b scans, `cc-by`)
- [fprm_retina](./fprm_retina.md): FPRM Multimodal Eye Imaging and Psychological Assessment Dataset (3,361 images, `research-only`)
- [grape](./grape.md): GRAPE: Glaucoma Real-world Appraisal Progression Ensemble (1,115 examinations, `cc0`)
- [mendeley_retina_identification_database_ridb](./mendeley_retina_identification_database_ridb.md): Retina Identification Database (RIDB) (100 images, `cc-by`)
- [dryad_diabetes_retinal_capillary](./dryad_diabetes_retinal_capillary.md): Diabetes Retinal Capillary Rarefaction Dataset (73 participants, `cc0`)
- [mendeley_two_photon_excited_fluorescence_scanning_laser](./mendeley_two_photon_excited_fluorescence_scanning_laser.md): Two-photon excited fluorescence scanning laser ophthalmoscopy images and software for data processing (1 participants, `cc-by`)
