---
id: idrid
title: "IDRiD: Indian Diabetic Retinopathy Image Dataset"
sidebar_label: idrid
description: "516 fundus images with DR grade (0-4), macular edema grade (0-2), and pixel-level lesion segmentation for 81 images."
tags: ["fundus", "cc-by", "manual", "grading", "classification", "segmentation", "resource-role-current-dataset", "dataset-family-idrid", "documented-relationship", "relationship-derived_from"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# IDRiD: Indian Diabetic Retinopathy Image Dataset

516 fundus images with DR grade (0-4), macular edema grade (0-2), and pixel-level lesion segmentation for 81 images.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `idrid` |
| **Full name** | IDRiD: Indian Diabetic Retinopathy Image Dataset |
| **Publication date** | 2018-01-20 |
| **Date basis** | Initial dataset release |
| **Publication date precision** | day |
| **Publication date evidence** | [idrid.grand-challenge.org/Dates](https://idrid.grand-challenge.org/Dates/) |
| **Publication date source field** | Official IDRiD challenge Important Dates: Training Data Release (Images + Groundtruth) |
| **Publication date reviewed** | 2026-09-11 |
| **Date notes** | The official IDRiD challenge page dates the training data release to January 20, 2018; this predates the later IEEE DataPort deposit and directly supports initial public availability. |
| **Primary category** | `fundus` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `idrid` |
| **Contained modalities** | fundus |
| **Tasks** | grading, classification, segmentation |
| **Primary reported quantity** | 516 images |
| **Classes** | 5 (Grade 0, Grade 1, Grade 2, Grade 3, Grade 4) |
| **Splits** | train, test |
| **Size** | 2.5 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `guided_instructions_only` |
| **Legacy sample-loader status** | Standard loader included |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 516 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [ieee-dataport.org/open-access](https://ieee-dataport.org/open-access/indian-diabetic-retinopathy-image-dataset-idrid) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Requires IEEE DataPort account (free).

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- [dme_vqa](./dme_vqa.md) is `derived from` this record: The DME VQA deposit identifies IDRiD images as source material. ([evidence](https://zenodo.org/records/6784358))
- [lmod_plus](./lmod_plus.md) is `derived from` this record: The LMOD+ project page lists nine component datasets, including the five cataloged targets represented by these edges. ([evidence](https://kfzyqin.github.io/lmod_plus/))
- [mm_retinal_reason](./mm_retinal_reason.md) is `derived from` this record: The version-pinned official dataset card lists this record among the CFP or OCT sources used to construct MM-Retinal-Reason. ([evidence](https://huggingface.co/datasets/lxirich/MM-Retinal-Reason/tree/d6243baa82c0914dba3c6f43ca79fdbf856982ef))
- [reta_benchmark](./reta_benchmark.md) is `derived from` this record: RETA reuses 81 images from the first IDRiD subset and adds vascular-tree annotations. ([evidence](https://doi.org/10.6084/m9.figshare.16960855))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download idrid --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download idrid --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('idrid')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [ieee-dataport.org/open-access](https://ieee-dataport.org/open-access/indian-diabetic-retinopathy-image-dataset-idrid)

**Source-term evidence:** [ieee-dataport.org/open-access](https://ieee-dataport.org/open-access/indian-diabetic-retinopathy-image-dataset-idrid)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('idrid')
samples = ds.load(data_dir, split='test')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{idrid,
  title  = { IDRiD: Indian Diabetic Retinopathy Image Dataset },
  note   = { Porwal et al., 'Indian diabetic retinopathy image dataset (IDRiD): A database for diabetic retinopathy screening research', Data 2018 },
  year   = { 2018 },
  url    = { https://ieee-dataport.org/open-access/indian-diabetic-retinopathy-image-dataset-idrid },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Porwal et al., 'Indian diabetic retinopathy image dataset (IDRiD): A database for diabetic retinopathy screening research', Data 2018.
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
