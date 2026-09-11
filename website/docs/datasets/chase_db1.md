---
id: chase_db1
title: "CHASE_DB1: Child Heart and Health Study in England"
sidebar_label: chase_db1
description: "28 fundus images with manual vessel segmentations (two annotators)."
tags: ["fundus", "cc-by", "manual", "segmentation", "resource-role-current-dataset", "dataset-family-chase-db1", "documented-relationship", "relationship-derived_from"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# CHASE_DB1: Child Heart and Health Study in England

28 fundus images with manual vessel segmentations (two annotators).

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `chase_db1` |
| **Full name** | CHASE_DB1: Child Heart and Health Study in England |
| **Publication date** | Unknown |
| **Date basis** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Date notes** | - |
| **Primary category** | `fundus` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `chase_db1` |
| **Contained modalities** | fundus |
| **Tasks** | segmentation |
| **Primary reported quantity** | 28 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.05 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `guided_instructions_only` |
| **Legacy sample-loader status** | Standard loader included |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 28 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [researchinnovation.kingston.ac.uk/en](https://researchinnovation.kingston.ac.uk/en/datasets/chasedb1-retinal-vessel-reference-dataset-4/) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Manual access only. Kingston landing pages: CHASE_DB1: https://researchinnovation.kingston.ac.uk/en/datasets/chasedb1-retinal-vessel-reference-dataset-4/; CHASE-AV: https://researchinnovation.kingston.ac.uk/en/datasets/chase-av-retinal-vessel-reference-dataset/

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- [retinal_vessel_robustness](./retinal_vessel_robustness.md) is `derived from` this record: The robustness benchmark contains augmented versions of DRIVE, STARE, and CHASE_DB1 images. ([evidence](https://zenodo.org/records/12659652))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download chase_db1 --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download chase_db1 --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('chase_db1')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [researchinnovation.kingston.ac.uk/en](https://researchinnovation.kingston.ac.uk/en/datasets/chasedb1-retinal-vessel-reference-dataset-4/)

**Source-term evidence:** [researchinnovation.kingston.ac.uk/en](https://researchinnovation.kingston.ac.uk/en/datasets/chasedb1-retinal-vessel-reference-dataset-4/)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('chase_db1')
samples = ds.load(data_dir, split='all')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{chase_db1,
  title  = { CHASE_DB1: Child Heart and Health Study in England },
  note   = { Owen et al., 'Measuring retinal vessel tortuosity in 10-year-old children: validation of the computer-assisted image analysis of the retina (CAIAR) program', Invest Ophthalmol Vis Sci 2009. Data: https://researchinnovation.kingston.ac.uk/en/datasets/chasedb1-retinal-vessel-reference-dataset-4/; CHASE-AV reference: https://researchinnovation.kingston.ac.uk/en/datasets/chase-av-retinal-vessel-reference-dataset/ },
  year   = { 2009 },
  url    = { https://researchinnovation.kingston.ac.uk/en/datasets/chasedb1-retinal-vessel-reference-dataset-4/ },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Owen et al., 'Measuring retinal vessel tortuosity in 10-year-old children: validation of the computer-assisted image analysis of the retina (CAIAR) program', Invest Ophthalmol Vis Sci 2009. Data: https://researchinnovation.kingston.ac.uk/en/datasets/chasedb1-retinal-vessel-reference-dataset-4/; CHASE-AV reference: https://researchinnovation.kingston.ac.uk/en/datasets/chase-av-retinal-vessel-reference-dataset/
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

- [airogs](./airogs.md): AIROGS: AI for Robust Glaucoma Screening (113,893 images, `cc-by-nc-nd`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (103,959 images, `mit`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [justraigs](./justraigs.md): JustRAIGS: Just Referral AI Glaucoma Screening Dataset (101,442 images, `cc-by-nc-nd`)
- [eyepacs](./eyepacs.md): EyePACS — Diabetic Retinopathy Detection (Kaggle 2015) (88,702 images, `research-only`)
- [angioreport](./angioreport.md): AngioReport Fundus Angiography Report Dataset (55,361 images, `unknown`)
- [ffa_ir](./ffa_ir.md): FFA-IR Medical Report Dataset (47,247 images, `unknown`)
- [mfiddr](./mfiddr.md): MFIDDR: Multi-Field Imaging Dataset for Diabetic Retinopathy (34,452 images, `mit`)
