---
id: eyepacs
title: "EyePACS — Diabetic Retinopathy Detection (Kaggle 2015)"
sidebar_label: eyepacs
description: "~88,000 fundus images graded 0–4 for DR severity. Largest public DR dataset; competition images from EyePACS clinics."
tags: ["fundus", "research-only", "kaggle", "grading", "classification", "resource-role-current-dataset", "dataset-family-eyepacs", "documented-relationship", "relationship-derived_from", "alternate-source", "source-kaggle", "source-tianchi", "alternate-role-repository-copy"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# EyePACS — Diabetic Retinopathy Detection (Kaggle 2015)

~88,000 fundus images graded 0–4 for DR severity. Largest public DR dataset; competition images from EyePACS clinics.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `eyepacs` |
| **Full name** | EyePACS — Diabetic Retinopathy Detection (Kaggle 2015) |
| **First published** | 2015-02-17 |
| **Publication date precision** | day |
| **Publication date evidence** | [kaggle.com/c](https://www.kaggle.com/c/diabetic-retinopathy-detection) |
| **Publication date source field** | Kaggle competition Overview: Start |
| **Publication date reviewed** | 2026-09-11 |
| **Primary category** | `fundus` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `eyepacs` |
| **Contained modalities** | fundus |
| **Tasks** | grading, classification |
| **Primary reported quantity** | 88,702 images |
| **Classes** | 5 (No DR, Mild, Moderate, Severe, Proliferative DR) |
| **Splits** | train, test |
| **Size** | 89.0 GB |
| **Source-stated terms** | Kaggle competition rules (non-commercial research) |
| **Normalized terms** | `research-only` |
| **Descriptive screening label** | Research or challenge restriction recorded; check source |
| **Terms scope** | `challenge_participation` |
| **Access friction** | `self_service_clickthrough` |
| **Route backend** | Kaggle |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Standard loader included |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 88,702 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [kaggle.com/c](https://www.kaggle.com/c/diabetic-retinopathy-detection) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Very large (~89 GB). Kaggle competition account and acceptance of rules required. BiDR and Tianchi 93926 are unmodified repackages of the 35,126-image training split and are recorded below as alternate routes rather than separate datasets.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- [eyeq](./eyeq.md) is `derived from` this record: EyeQ provides quality labels for 28,792 images from the EyePACS train and test partitions. ([evidence](https://github.com/HzFu/EyeQ))
- [mm_retinal_reason](./mm_retinal_reason.md) is `derived from` this record: The version-pinned official dataset card lists this record among the CFP or OCT sources used to construct MM-Retinal-Reason. ([evidence](https://huggingface.co/datasets/lxirich/MM-Retinal-Reason/tree/d6243baa82c0914dba3c6f43ca79fdbf856982ef))
- [multieye](./multieye.md) is `derived from` this record: The MultiEYE paper names this record as one of the public fundus or OCT sources assembled for the benchmark. ([evidence](https://arxiv.org/abs/2412.09402))
- [x_pcr](./x_pcr.md) is `derived from` this record: Source labels in the version-pinned public X-PCR deposit identify this catalog record as upstream material. ([evidence](https://huggingface.co/datasets/Fantasy666/X-PCR/tree/06a318fd852230326386e3c6514d8a11b7a6b4af))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download eyepacs --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download eyepacs --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('eyepacs')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [kaggle.com/c](https://www.kaggle.com/c/diabetic-retinopathy-detection)

## Other documented locations

These links identify alternate deposits, components, metadata records, mirrors, versions, or related derived materials. They do not create additional canonical catalog records.

- [kaggle: repository copy (pkdarabi/diagnosis-of-diabetic-retinopathy)](https://www.kaggle.com/datasets/pkdarabi/diagnosis-of-diabetic-retinopathy): BiDR repackage of the 35,126-image EyePACS training split; not counted as a separate catalog record.
- [tianchi: repository copy (93926)](https://tianchi.aliyun.com/dataset/93926): Arranged mirror of the same 35,126-image EyePACS training split; not counted as a separate catalog record.

**Source-term evidence:** [kaggle.com/c](https://www.kaggle.com/c/diabetic-retinopathy-detection)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('eyepacs')
samples = ds.load(data_dir, split='test')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{eyepacs,
  title  = { EyePACS — Diabetic Retinopathy Detection (Kaggle 2015) },
  note   = { EyePACS / California Healthcare Foundation. 'Diabetic Retinopathy Detection', Kaggle Competition, 2015 },
  year   = { 2015 },
  url    = { https://www.kaggle.com/c/diabetic-retinopathy-detection },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
EyePACS / California Healthcare Foundation. 'Diabetic Retinopathy Detection', Kaggle Competition, 2015.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Kaggle competition rules (non-commercial research)
- **Normalized category:** `research-only`
- **Apparent scope:** `challenge_participation`
- **Descriptive screening label:** Research or challenge restriction recorded; check source

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [airogs](./airogs.md): AIROGS: AI for Robust Glaucoma Screening (113,893 images, `cc-by-nc-nd`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (103,959 images, `mit`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [justraigs](./justraigs.md): JustRAIGS: Just Referral AI Glaucoma Screening Dataset (101,442 images, `cc-by-nc-nd`)
- [angioreport](./angioreport.md): AngioReport Fundus Angiography Report Dataset (55,361 images, `unknown`)
- [ffa_ir](./ffa_ir.md): FFA-IR Medical Report Dataset (47,247 images, `unknown`)
- [mfiddr](./mfiddr.md): MFIDDR: Multi-Field Imaging Dataset for Diabetic Retinopathy (34,452 images, `mit`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
