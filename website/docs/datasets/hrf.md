---
id: hrf
title: "HRF: High-Resolution Fundus Image Database"
sidebar_label: hrf
description: "45 high-resolution fundus images (healthy/DR/glaucoma) with manual vessel segmentation."
tags: ["fundus", "cc-by", "manual", "segmentation", "resource-role-current-dataset", "dataset-family-hrf", "documented-relationship", "relationship-derived_from"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# HRF: High-Resolution Fundus Image Database

45 high-resolution fundus images (healthy/DR/glaucoma) with manual vessel segmentation.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `hrf` |
| **Full name** | HRF: High-Resolution Fundus Image Database |
| **First published** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Primary category** | `fundus` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `hrf` |
| **Contained modalities** | fundus |
| **Tasks** | segmentation |
| **Primary reported quantity** | 45 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.5 GB |
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
| Primary | 45 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [www5.cs.fau.de/research](https://www5.cs.fau.de/research/data/fundus-images/) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Requires manual download from FAU Erlangen-Nuremberg website.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- [amdnet23](./amdnet23.md) is `derived from` this record: AMDNet23 compiles preprocessed images from ODIR, RFMiD, HRF, ARIA, DR_200, and Fundus Dataset. ([evidence](https://doi.org/10.17632/yj35kjgrv3.1))
- [higancnn_generated_glaucoma](./higancnn_generated_glaucoma.md) is `derived from` this record: The official dataset description names ACRIMA, DRISHTI-GS, and HRF among the human fundus sources used to construct the synthetic glaucoma resource. ([evidence](https://www.kaggle.com/datasets/hindsaud/datasets-higancnn-glaucoma-detection))
- [hrf_seg_plus](./hrf_seg_plus.md) is `derived from` this record: HRF-Seg+ adds multi-structure annotations to the 45 HRF images. ([evidence](https://zenodo.org/records/16744782))
- [mm_retinal_reason](./mm_retinal_reason.md) is `derived from` this record: The version-pinned official dataset card lists this record among the CFP or OCT sources used to construct MM-Retinal-Reason. ([evidence](https://huggingface.co/datasets/lxirich/MM-Retinal-Reason/tree/d6243baa82c0914dba3c6f43ca79fdbf856982ef))
- [smdg](./smdg.md) is `derived from` this record: The official SMDG source table lists this catalog record among the 19 standardized source domains. ([evidence](https://www.kaggle.com/datasets/deathtrooper/multichannel-glaucoma-benchmark-dataset))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download hrf --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download hrf --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('hrf')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [www5.cs.fau.de/research](https://www5.cs.fau.de/research/data/fundus-images/)

**Source-term evidence:** [www5.cs.fau.de/research](https://www5.cs.fau.de/research/data/fundus-images/)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('hrf')
samples = ds.load(data_dir, split='all')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{hrf,
  title  = { HRF: High-Resolution Fundus Image Database },
  note   = { Budai et al., 'Robust vessel segmentation in fundus images', Intl Journal of Biomedical Imaging 2013 },
  year   = { 2013 },
  url    = { https://www5.cs.fau.de/research/data/fundus-images/ },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Budai et al., 'Robust vessel segmentation in fundus images', Intl Journal of Biomedical Imaging 2013.
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
