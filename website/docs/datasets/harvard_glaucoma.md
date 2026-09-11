---
id: harvard_glaucoma
title: "Harvard Glaucoma Fundus Image Dataset"
sidebar_label: harvard_glaucoma
description: "Fundus images for glaucoma detection from Harvard Medical School / Mass Eye and Ear. Binary glaucoma classification."
tags: ["fundus", "cc0", "direct", "classification", "resource-role-current-dataset", "dataset-family-harvard-glaucoma"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Harvard Glaucoma Fundus Image Dataset

Fundus images for glaucoma detection from Harvard Medical School / Mass Eye and Ear. Binary glaucoma classification.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `harvard_glaucoma` |
| **Full name** | Harvard Glaucoma Fundus Image Dataset |
| **First published** | 2018-11-15 |
| **Publication date precision** | day |
| **Publication date evidence** | [dataverse.harvard.edu/api](https://dataverse.harvard.edu/api/datasets/:persistentId/versions/1.0?persistentId=doi:10.7910/DVN/1YRRAC) |
| **Publication date source field** | Harvard Dataverse API: version 1.0 releaseTime |
| **Publication date reviewed** | 2026-09-11 |
| **Primary category** | `fundus` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `harvard_glaucoma` |
| **Contained modalities** | fundus |
| **Tasks** | classification |
| **Primary reported quantity** | 1,000 images |
| **Classes** | 2 (Non-glaucoma, Glaucoma) |
| **Splits** | all |
| **Size** | 1.5 GB |
| **Source-stated terms** | CC0 1.0 (Public Domain) |
| **Normalized terms** | `cc0` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Direct HTTP |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `end_to_end_tested` |
| **Legacy sample-loader status** | Standard loader included |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 1,000 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [https://doi.org/10.7910/DVN/1YRRAC](https://doi.org/10.7910/DVN/1YRRAC) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download harvard_glaucoma --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download harvard_glaucoma --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('harvard_glaucoma')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.7910/DVN/1YRRAC](https://doi.org/10.7910/DVN/1YRRAC)

**Source-term evidence:** [https://doi.org/10.7910/DVN/1YRRAC](https://doi.org/10.7910/DVN/1YRRAC)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('harvard_glaucoma')
samples = ds.load(data_dir, split='all')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{harvard_glaucoma,
  title  = { Harvard Glaucoma Fundus Image Dataset },
  note   = { Luo X. et al., 'Harvard Glaucoma Detection and Progression Dataset', Harvard Dataverse, doi:10.7910/DVN/1YRRAC, 2023 },
  year   = { 2023 },
  url    = { https://doi.org/10.7910/DVN/1YRRAC },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Luo X. et al., 'Harvard Glaucoma Detection and Progression Dataset', Harvard Dataverse, doi:10.7910/DVN/1YRRAC, 2023.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC0 1.0 (Public Domain)
- **Normalized category:** `cc0`
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
