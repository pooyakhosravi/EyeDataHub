---
id: refuge1_multirater
title: "REFUGE Multi-Rater — Glaucoma with Multi-Expert Annotations"
sidebar_label: refuge1_multirater
description: "1200 fundus images from REFUGE1 with optic disc/cup segmentation masks annotated by multiple expert raters."
tags: ["fundus", "cc-by-nc-sa", "gdrive", "classification", "segmentation", "resource-role-annotation-layer", "dataset-family-refuge1-multirater", "documented-relationship", "relationship-derived_from"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# REFUGE Multi-Rater — Glaucoma with Multi-Expert Annotations

1200 fundus images from REFUGE1 with optic disc/cup segmentation masks annotated by multiple expert raters.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `refuge1_multirater` |
| **Full name** | REFUGE Multi-Rater — Glaucoma with Multi-Expert Annotations |
| **Publication date** | Unknown |
| **Date basis** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Date notes** | - |
| **Primary category** | `fundus` |
| **Resource role** | `annotation_layer` |
| **Dataset family** | `refuge1_multirater` |
| **Contained modalities** | fundus |
| **Tasks** | classification, segmentation |
| **Primary reported quantity** | 1,200 images |
| **Classes** | 2 (non-glaucoma, glaucoma) |
| **Splits** | train, val, test |
| **Size** | 0.8 GB |
| **Source-stated terms** | CC BY-NC-SA (see HuggingFace page) |
| **Normalized terms** | `cc-by-nc-sa` |
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
| Primary | 1,200 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [drive.google.com/file](https://drive.google.com/file/d/1TXTrZyaZ76faXek46pEzaYQmAejLf30d/view) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- This record is `derived from` [refuge2](./refuge2.md): The source provides seven-rater annotations for the 1,200 original REFUGE images incorporated into the current REFUGE2 release. ([evidence](https://huggingface.co/datasets/realslimman/REFUGE-MultiRater))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download refuge1_multirater --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download refuge1_multirater --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('refuge1_multirater')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [drive.google.com/file](https://drive.google.com/file/d/1TXTrZyaZ76faXek46pEzaYQmAejLf30d/view)

**Source-term evidence:** [drive.google.com/file](https://drive.google.com/file/d/1TXTrZyaZ76faXek46pEzaYQmAejLf30d/view)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('refuge1_multirater')
samples = ds.load(data_dir, split='test')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{refuge1_multirater,
  title  = { REFUGE Multi-Rater — Glaucoma with Multi-Expert Annotations },
  note   = { Orlando J.I. et al., 'REFUGE Challenge: A Unified Framework for Evaluating Automated Methods for Glaucoma Assessment from Fundus Photographs', MIA 2020 },
  year   = { 2020 },
  url    = { https://drive.google.com/file/d/1TXTrZyaZ76faXek46pEzaYQmAejLf30d/view },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Orlando J.I. et al., 'REFUGE Challenge: A Unified Framework for Evaluating Automated Methods for Glaucoma Assessment from Fundus Photographs', MIA 2020.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC BY-NC-SA (see HuggingFace page)
- **Normalized category:** `cc-by-nc-sa`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Explicit noncommercial clause recorded; check source

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
