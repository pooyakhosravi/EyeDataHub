---
id: stare
title: "STARE: Structured Analysis of the Retina"
sidebar_label: stare
description: "20 fundus images with manual vessel segmentation (two annotators)."
tags: ["fundus", "research-only", "direct", "segmentation", "resource-role-current-dataset", "dataset-family-stare", "documented-relationship", "relationship-derived_from"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# STARE: Structured Analysis of the Retina

20 fundus images with manual vessel segmentation (two annotators).

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `stare` |
| **Full name** | STARE: Structured Analysis of the Retina |
| **Publication date** | Unknown |
| **Date basis** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Date notes** | - |
| **Primary category** | `fundus` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `stare` |
| **Contained modalities** | fundus |
| **Tasks** | segmentation |
| **Primary reported quantity** | 20 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.02 GB |
| **Source-stated terms** | Research only |
| **Normalized terms** | `research-only` |
| **Descriptive screening label** | Research or challenge restriction recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Direct HTTP |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `end_to_end_tested` |
| **Legacy sample-loader status** | Standard loader included |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 20 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [cecas.clemson.edu/~ahoover](https://cecas.clemson.edu/~ahoover/stare/) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- [mm_retinal_reason](./mm_retinal_reason.md) is `derived from` this record: The version-pinned official dataset card lists this record among the CFP or OCT sources used to construct MM-Retinal-Reason. ([evidence](https://huggingface.co/datasets/lxirich/MM-Retinal-Reason/tree/d6243baa82c0914dba3c6f43ca79fdbf856982ef))
- [multieye](./multieye.md) is `derived from` this record: The MultiEYE paper names this record as one of the public fundus or OCT sources assembled for the benchmark. ([evidence](https://arxiv.org/abs/2412.09402))
- [mured](./mured.md) is `derived from` this record: The MuReD description identifies STARE, RFMiD, and ARIA as image sources and applies post-processing. ([evidence](https://doi.org/10.17632/pc4mb3h8hz.1))
- [retinal_vessel_robustness](./retinal_vessel_robustness.md) is `derived from` this record: The robustness benchmark contains augmented versions of DRIVE, STARE, and CHASE_DB1 images. ([evidence](https://zenodo.org/records/12659652))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download stare --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download stare --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('stare')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [cecas.clemson.edu/~ahoover](https://cecas.clemson.edu/~ahoover/stare/)

**Source-term evidence:** [cecas.clemson.edu/~ahoover](https://cecas.clemson.edu/~ahoover/stare/)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('stare')
samples = ds.load(data_dir, split='all')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{stare,
  title  = { STARE: Structured Analysis of the Retina },
  note   = { Hoover et al., 'Locating blood vessels in retinal images by piece-wise threshold probing of a matched filter response', IEEE TMI 2000 },
  year   = { 2000 },
  url    = { https://cecas.clemson.edu/~ahoover/stare/ },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Hoover et al., 'Locating blood vessels in retinal images by piece-wise threshold probing of a matched filter response', IEEE TMI 2000.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Research only
- **Normalized category:** `research-only`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Research or challenge restriction recorded; check source

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
