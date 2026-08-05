---
id: deepdrid
title: "DeepDRiD: Diabetic Retinopathy Grading and Image Quality Dataset"
sidebar_label: deepdrid
description: "2,000 regular fundus images (500 patients × 2 fields × 2 eyes) plus 256 ultra-widefield fundus images labeled for DR severity (ICDR grades 0-4) and image quality assessment (gradable/ungradable). From"
tags: ["fundus", "uwf_fundus", "cc-by-sa", "zenodo", "grading", "classification", "quality", "resource-role-current-dataset", "dataset-family-deepdrid", "documented-relationship", "relationship-derived_from"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# DeepDRiD: Diabetic Retinopathy Grading and Image Quality Dataset

2,000 regular fundus images (500 patients × 2 fields × 2 eyes) plus 256 ultra-widefield fundus images labeled for DR severity (ICDR grades 0-4) and image quality assessment (gradable/ungradable). From the DeepDRiD challenge (MICCAI 2020 / ISBI 2020).

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `deepdrid` |
| **Full name** | DeepDRiD: Diabetic Retinopathy Grading and Image Quality Dataset |
| **Primary category** | `fundus` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `deepdrid` |
| **Contained modalities** | fundus, uwf_fundus |
| **Tasks** | grading, classification, quality |
| **Primary reported quantity** | 2,256 images |
| **Classes** | 5 (No DR, Mild NPDR, Moderate NPDR, Severe NPDR, Proliferative DR) |
| **Splits** | train, val, test |
| **Size** | 3.0 GB |
| **Source-stated terms** | CC BY-SA 4.0 |
| **Normalized terms** | `cc-by-sa` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Zenodo |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Standard loader included |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 2,256 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [zenodo.org/records](https://zenodo.org/records/8248825) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Contains both regular fundus (2000 images in dual-field pairs) and ultra-widefield fundus (256 images). Labels CSV includes DR grade (0-4) and quality score.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- [fundus_report_dataset](./fundus_report_dataset.md) is `derived from` this record: The dataset card reports 203 source images from DeepDRiD and 219 from OUWFD. ([evidence](https://huggingface.co/datasets/zzzzineun/fundus-report-dataset))
- [mm_retinal_reason](./mm_retinal_reason.md) is `derived from` this record: The version-pinned official dataset card lists this record among the CFP or OCT sources used to construct MM-Retinal-Reason. ([evidence](https://huggingface.co/datasets/lxirich/MM-Retinal-Reason/tree/d6243baa82c0914dba3c6f43ca79fdbf856982ef))
- [x_pcr](./x_pcr.md) is `derived from` this record: Source labels in the version-pinned public X-PCR deposit identify this catalog record as upstream material. ([evidence](https://huggingface.co/datasets/Fantasy666/X-PCR/tree/06a318fd852230326386e3c6514d8a11b7a6b4af))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download deepdrid --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download deepdrid --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('deepdrid')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [zenodo.org/records](https://zenodo.org/records/8248825)

**Source-term evidence:** [zenodo.org/records](https://zenodo.org/records/8248825)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('deepdrid')
samples = ds.load(data_dir, split='test')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{deepdrid,
  title  = { DeepDRiD: Diabetic Retinopathy Grading and Image Quality Dataset },
  note   = { Liu R et al., 'DeepDRiD: Diabetic Retinopathy—Grading and Image Quality Estimation Challenge', Patterns 2022. Zenodo: https://zenodo.org/records/8248825 },
  year   = { 2022 },
  url    = { https://zenodo.org/records/8248825 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Liu R et al., 'DeepDRiD: Diabetic Retinopathy—Grading and Image Quality Estimation Challenge', Patterns 2022. Zenodo: https://zenodo.org/records/8248825
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC BY-SA 4.0
- **Normalized category:** `cc-by-sa`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Standard label without an explicit NC clause; not a permission finding

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [mmrdr](./mmrdr.md): MMRDR: Multi-Modal Retinal Diabetic Retinopathy Dataset (24,460 images, `cc-by`)
- [fundus_report_dataset](./fundus_report_dataset.md): Fundus Report Dataset (422 image report pairs, `cc-by`)
- [airogs](./airogs.md): AIROGS: AI for Robust Glaucoma Screening (113,893 images, `cc-by-nc-nd`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (103,959 images, `mit`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [justraigs](./justraigs.md): JustRAIGS: Just Referral AI Glaucoma Screening Dataset (101,442 images, `cc-by-nc-nd`)
- [eyepacs](./eyepacs.md): EyePACS — Diabetic Retinopathy Detection (Kaggle 2015) (88,702 images, `research-only`)
- [angioreport](./angioreport.md): AngioReport Fundus Angiography Report Dataset (55,361 images, `unknown`)
