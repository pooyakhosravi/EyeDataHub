---
id: gamma
title: "GAMMA — Glaucoma Grading from Multi-Modality Images"
sidebar_label: gamma
description: "300 paired fundus + 3D OCT volumes. Glaucoma grading into Normal / Early / Advanced plus OD/OC segmentation and fovea location."
tags: ["multimodal", "fundus", "oct", "cc-by-nc-nd", "gdrive", "grading", "classification", "segmentation", "resource-role-component-dataset", "dataset-family-ichallenge-gamma", "documented-relationship", "relationship-derived_from", "relationship-has_component", "relationship-component_of"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# GAMMA — Glaucoma Grading from Multi-Modality Images

300 paired fundus + 3D OCT volumes. Glaucoma grading into Normal / Early / Advanced plus OD/OC segmentation and fovea location.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `gamma` |
| **Full name** | GAMMA — Glaucoma Grading from Multi-Modality Images |
| **Publication date** | Unknown |
| **Date basis** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Date notes** | - |
| **Primary category** | `multimodal` |
| **Resource role** | `component_dataset` |
| **Dataset family** | `ichallenge_gamma` |
| **Contained modalities** | fundus, oct |
| **Tasks** | grading, classification, segmentation |
| **Primary reported quantity** | 300 volumes |
| **Classes** | 3 (Normal, Early, Advanced) |
| **Splits** | train, test |
| **Size** | 5.0 GB |
| **Source-stated terms** | CC BY-NC-ND |
| **Normalized terms** | `cc-by-nc-nd` |
| **Descriptive screening label** | Explicit noncommercial clause recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Google Drive |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `loader_implemented_not_live_tested` |
| **Legacy sample-loader status** | Standard loader included |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 300 | `volumes` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [drive.google.com/file](https://drive.google.com/file/d/1thJDE1_TR-xa8f3H-0PwPpDxun7rV8Sw/view) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Dataset family

This record belongs to `ichallenge_gamma`. Family links group documented collection/component records or exact task views; they do not imply independent cohorts.

- [ichallenge_oct](./ichallenge_oct.md): iChallenge OCT Datasets (HDMILab / OMIA Workshops) (`collection`)

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- [mm_retinal_reason](./mm_retinal_reason.md) is `derived from` this record: The version-pinned official dataset card lists this record among the CFP or OCT sources used to construct MM-Retinal-Reason. ([evidence](https://huggingface.co/datasets/lxirich/MM-Retinal-Reason/tree/d6243baa82c0914dba3c6f43ca79fdbf856982ef))
- [ichallenge_oct](./ichallenge_oct.md) is `has component` this record: The cataloged iChallenge OCT portal record explicitly includes the GAMMA multimodal challenge resource. ([evidence](http://hdmilab.cn/ichallenge))
- This record is `component of` [ichallenge_oct](./ichallenge_oct.md): GAMMA is one of the named resources exposed through the cataloged iChallenge OCT portal record. ([evidence](http://hdmilab.cn/ichallenge))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download gamma --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download gamma --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('gamma')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [drive.google.com/file](https://drive.google.com/file/d/1thJDE1_TR-xa8f3H-0PwPpDxun7rV8Sw/view)

**Source-term evidence:** [drive.google.com/file](https://drive.google.com/file/d/1thJDE1_TR-xa8f3H-0PwPpDxun7rV8Sw/view)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('gamma')
samples = ds.load(data_dir, split='test')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{gamma,
  title  = { GAMMA — Glaucoma Grading from Multi-Modality Images },
  note   = { Wu J. et al., 'GAMMA Challenge: Glaucoma Grading from Multi-Modality Imaging', MIA 2023 },
  year   = { 2023 },
  url    = { https://drive.google.com/file/d/1thJDE1_TR-xa8f3H-0PwPpDxun7rV8Sw/view },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Wu J. et al., 'GAMMA Challenge: Glaucoma Grading from Multi-Modality Imaging', MIA 2023.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC BY-NC-ND
- **Normalized category:** `cc-by-nc-nd`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Explicit noncommercial clause recorded; check source

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (103,959 images, `mit`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [harvard_fairvision](./harvard_fairvision.md): Harvard-FairVision (AMD + DR + Glaucoma, paired SLO + OCT) (30,000 participants, `cc-by-nc-nd`)
- [mmrdr](./mmrdr.md): MMRDR: Multi-Modal Retinal Diabetic Retinopathy Dataset (24,460 images, `cc-by`)
- [x_pcr](./x_pcr.md): X-PCR Ophthalmology Progressive Clinical Reasoning Benchmark (18,735 rows, `unknown`)
- [olives](./olives.md): OLIVES: Ophthalmic Labels for Investigating Visual Eye Semantics (9,408 b scans, `cc-by`)
- [oct_fundus_dme_dr_mexico](./oct_fundus_dme_dr_mexico.md): OCT and Eye Fundus Dataset for DME and DR (2,661 images, `unknown`)
