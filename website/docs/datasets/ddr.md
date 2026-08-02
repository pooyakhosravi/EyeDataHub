---
id: ddr
title: "DDR: Diabetic Retinopathy Detection & Grading"
sidebar_label: ddr
description: "12522 fundus images with DR grading (0-5) and lesion-level segmentation annotations."
tags: ["fundus", "mit", "gdrive", "grading", "classification", "documented-relationship", "relationship-derived_from"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# DDR: Diabetic Retinopathy Detection & Grading

12522 fundus images with DR grading (0-5) and lesion-level segmentation annotations.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `ddr` |
| **Full name** | DDR: Diabetic Retinopathy Detection & Grading |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | grading, classification |
| **Primary reported quantity** | 12,522 images |
| **Classes** | 6 (No DR, Mild, Moderate, Severe, Proliferative, Ungradable) |
| **Splits** | train, valid, test |
| **Size** | 4.0 GB |
| **Source-stated terms** | MIT |
| **Normalized terms** | `mit` |
| **Descriptive screening label** | Standard label without an explicit NC clause; verify that it applies to data |
| **Terms scope** | `unknown` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Google Drive |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `loader_implemented_not_live_tested` |
| **Legacy sample-loader status** | Standard loader included |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 12,522 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [drive.google.com/drive](https://drive.google.com/drive/folders/1z6tSFmxW_aNayUqVxx6h6bY4kwGzUTEC) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- [mm_retinal_reason](./mm_retinal_reason.md) is `derived from` this record: The version-pinned official dataset card lists this record among the CFP or OCT sources used to construct MM-Retinal-Reason. ([evidence](https://huggingface.co/datasets/lxirich/MM-Retinal-Reason/tree/d6243baa82c0914dba3c6f43ca79fdbf856982ef))
- [mmrdr](./mmrdr.md) is `derived from` this record: The MMRDR Data Descriptor identifies OIA-DDR as the source of its CFP images; MMRDR also adds independently collected OCT and UWF cohorts and new annotations. ([evidence](https://doi.org/10.1038/s41597-026-07005-9))
- [multieye](./multieye.md) is `derived from` this record: The MultiEYE paper names this record as one of the public fundus or OCT sources assembled for the benchmark. ([evidence](https://arxiv.org/abs/2412.09402))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download ddr --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download ddr --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('ddr')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [drive.google.com/drive](https://drive.google.com/drive/folders/1z6tSFmxW_aNayUqVxx6h6bY4kwGzUTEC)

**Source-term evidence:** [drive.google.com/drive](https://drive.google.com/drive/folders/1z6tSFmxW_aNayUqVxx6h6bY4kwGzUTEC)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('ddr')
samples = ds.load(data_dir, split='test')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{ddr,
  title  = { DDR: Diabetic Retinopathy Detection & Grading },
  note   = { Li et al., 'Diagnostic Assessment of Deep Learning Algorithms for Diabetic Retinopathy Screening', Information Sciences 2019. Data: https://github.com/nkicsl/DDR-dataset — GDrive: https://drive.google.com/drive/folders/1z6tSFmxW_aNayUqVxx6h6bY4kwGzUTEC },
  year   = { 2019 },
  url    = { https://drive.google.com/drive/folders/1z6tSFmxW_aNayUqVxx6h6bY4kwGzUTEC },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Li et al., 'Diagnostic Assessment of Deep Learning Algorithms for Diabetic Retinopathy Screening', Information Sciences 2019. Data: https://github.com/nkicsl/DDR-dataset — GDrive: https://drive.google.com/drive/folders/1z6tSFmxW_aNayUqVxx6h6bY4kwGzUTEC
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** MIT
- **Normalized category:** `mit`
- **Apparent scope:** `unknown`
- **Descriptive screening label:** Standard label without an explicit NC clause; verify that it applies to data

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [airogs](./airogs.md): AIROGS: AI for Robust Glaucoma Screening (113,893 images, `cc-by-nc-nd`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (103,959 images, `mit`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [justraigs](./justraigs.md): JustRAIGS: Just Referral AI Glaucoma Screening Dataset (101,442 images, `cc-by-nc-nd`)
- [eyepacs](./eyepacs.md): EyePACS — Diabetic Retinopathy Detection (Kaggle 2015) (88,702 images, `research-only`)
- [angioreport](./angioreport.md): AngioReport Fundus Angiography Report Dataset (55,361 images, `unknown`)
- [ffa_ir](./ffa_ir.md): FFA-IR Medical Report Dataset (47,247 images, `unknown`)
- [bidr](./bidr.md): BiDR: Diabetic Retinopathy Diagnosis Dataset (35,126 images, `unknown`)
