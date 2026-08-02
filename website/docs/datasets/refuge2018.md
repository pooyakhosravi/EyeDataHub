---
id: refuge2018
title: "REFUGE 2018: Retinal Fundus Glaucoma Challenge"
sidebar_label: refuge2018
description: "1200 fundus images: 400 train, 400 val, 400 test. Labels: glaucoma/non-glaucoma + optic disc/cup segmentation."
tags: ["fundus", "research-only", "manual", "classification", "segmentation", "documented-relationship", "relationship-derived_from", "relationship-version_of"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# REFUGE 2018: Retinal Fundus Glaucoma Challenge

1200 fundus images: 400 train, 400 val, 400 test. Labels: glaucoma/non-glaucoma + optic disc/cup segmentation.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `refuge2018` |
| **Full name** | REFUGE 2018: Retinal Fundus Glaucoma Challenge |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | classification, segmentation |
| **Primary reported quantity** | 1,200 images |
| **Classes** | 2 (Non-glaucoma, Glaucoma) |
| **Splits** | train, val, test |
| **Size** | 2.5 GB |
| **Source-stated terms** | Research only — requires Grand Challenge registration |
| **Normalized terms** | `research-only` |
| **Descriptive screening label** | Research or challenge restriction recorded; check source |
| **Terms scope** | `challenge_participation` |
| **Access friction** | `controlled_or_manual` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `manual_access_blocked` |
| **Legacy sample-loader status** | Standard loader included |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 1,200 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [refuge.grand-challenge.org](https://refuge.grand-challenge.org/) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Requires Grand Challenge account and challenge participation.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- [fundus_domain_generalization](./fundus_domain_generalization.md) is `derived from` this record: The official description states that the benchmark is based on REFUGE, Drishti-GS, ORIGA, and RIGA. ([evidence](https://zenodo.org/records/8009107))
- [lmod_plus](./lmod_plus.md) is `derived from` this record: The LMOD+ project page lists nine component datasets, including the five cataloged targets represented by these edges. ([evidence](https://kfzyqin.github.io/lmod_plus/))
- [mm_retinal_reason](./mm_retinal_reason.md) is `derived from` this record: The version-pinned official dataset card lists this record among the CFP or OCT sources used to construct MM-Retinal-Reason. ([evidence](https://huggingface.co/datasets/lxirich/MM-Retinal-Reason/tree/d6243baa82c0914dba3c6f43ca79fdbf856982ef))
- [refuge1_multirater](./refuge1_multirater.md) is `derived from` this record: The source provides seven-rater annotations for the 1,200 REFUGE challenge images. ([evidence](https://huggingface.co/datasets/realslimman/REFUGE-MultiRater))
- [smdg](./smdg.md) is `derived from` this record: The official SMDG source table lists this catalog record among the 19 standardized source domains. ([evidence](https://www.kaggle.com/datasets/deathtrooper/multichannel-glaucoma-benchmark-dataset))
- [refuge2](./refuge2.md) is `version of` this record: REFUGE2 contains all 1,200 REFUGE images and adds 800 images from another domain. ([evidence](https://refuge.grand-challenge.org/))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# This route requires upstream human action; no transfer starts.
eyehub download refuge2018 --data-dir ./data --dry-run --json
# Follow the official instructions shown by preflight.
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('refuge2018')
print(preflight_dataset(ds, './data'))  # returns manual_access_blocked
```

  </TabItem>
</Tabs>

**Upstream page:** [refuge.grand-challenge.org](https://refuge.grand-challenge.org/)

**Source-term evidence:** [refuge.grand-challenge.org](https://refuge.grand-challenge.org/)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('refuge2018')
samples = ds.load(data_dir, split='test')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{refuge2018,
  title  = { REFUGE 2018: Retinal Fundus Glaucoma Challenge },
  note   = { Orlando et al., 'REFUGE challenge: A unified framework for evaluating automated methods for glaucoma assessment from fundus photographs', MedIA 2020 },
  year   = { 2020 },
  url    = { https://refuge.grand-challenge.org/ },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Orlando et al., 'REFUGE challenge: A unified framework for evaluating automated methods for glaucoma assessment from fundus photographs', MedIA 2020.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Research only — requires Grand Challenge registration
- **Normalized category:** `research-only`
- **Apparent scope:** `challenge_participation`
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
- [bidr](./bidr.md): BiDR: Diabetic Retinopathy Diagnosis Dataset (35,126 images, `unknown`)
