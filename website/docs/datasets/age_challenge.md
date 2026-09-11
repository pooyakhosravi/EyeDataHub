---
id: age_challenge
title: "AGE — Angle-Closure Glaucoma Evaluation Challenge (AS-OCT)"
sidebar_label: age_challenge
description: "4800 AS-OCT images from 199 patients. Two tasks: angle closure classification and scleral spur localization."
tags: ["oct", "research-only", "gdrive", "classification", "resource-role-current-dataset", "dataset-family-age-challenge"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# AGE — Angle-Closure Glaucoma Evaluation Challenge (AS-OCT)

4800 AS-OCT images from 199 patients. Two tasks: angle closure classification and scleral spur localization.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `age_challenge` |
| **Full name** | AGE — Angle-Closure Glaucoma Evaluation Challenge (AS-OCT) |
| **First published** | 2019-07-10 |
| **Publication date precision** | day |
| **Publication date evidence** | [age.grand-challenge.org/Home](https://age.grand-challenge.org/Home/) |
| **Publication date source field** | Official AGE challenge Updates: Training images and annotations are released |
| **Publication date reviewed** | 2026-09-11 |
| **Primary category** | `oct` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `age_challenge` |
| **Contained modalities** | oct |
| **Tasks** | classification |
| **Primary reported quantity** | 4,800 images |
| **Classes** | 2 (open, closed) |
| **Splits** | train, test |
| **Size** | 1.2 GB |
| **Source-stated terms** | Challenge data-use agreement (IEEE DataPort) |
| **Normalized terms** | `research-only` |
| **Descriptive screening label** | Research or challenge restriction recorded; check source |
| **Terms scope** | `challenge_participation` |
| **Access friction** | `controlled_or_manual` |
| **Route backend** | Google Drive |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `manual_access_blocked` |
| **Legacy sample-loader status** | Standard loader included |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 4,800 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [drive.google.com/file](https://drive.google.com/file/d/1Qlkqj74SW8DJRKdYL_-ApC_0H5Z7uyvr/view) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# This route requires upstream human action; no transfer starts.
eyehub download age_challenge --data-dir ./data --dry-run --json
# Follow the official instructions shown by preflight.
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('age_challenge')
print(preflight_dataset(ds, './data'))  # returns manual_access_blocked
```

  </TabItem>
</Tabs>

**Upstream page:** [drive.google.com/file](https://drive.google.com/file/d/1Qlkqj74SW8DJRKdYL_-ApC_0H5Z7uyvr/view)

**Source-term evidence:** [drive.google.com/file](https://drive.google.com/file/d/1Qlkqj74SW8DJRKdYL_-ApC_0H5Z7uyvr/view)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('age_challenge')
samples = ds.load(data_dir, split='test')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{age_challenge,
  title  = { AGE — Angle-Closure Glaucoma Evaluation Challenge (AS-OCT) },
  note   = { Fu H. et al., 'AGE Challenge: Angle Closure Glaucoma Evaluation', MICCAI 2019 Workshop },
  year   = { 2019 },
  url    = { https://drive.google.com/file/d/1Qlkqj74SW8DJRKdYL_-ApC_0H5Z7uyvr/view },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Fu H. et al., 'AGE Challenge: Angle Closure Glaucoma Evaluation', MICCAI 2019 Workshop.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Challenge data-use agreement (IEEE DataPort)
- **Normalized category:** `research-only`
- **Apparent scope:** `challenge_participation`
- **Descriptive screening label:** Research or challenge restriction recorded; check source

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [syn_oct](./syn_oct.md): SYN-OCT Synthetic Glaucoma OCT Dataset (200,000 images, `cc-by`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (103,959 images, `mit`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [kermany_oct](./kermany_oct.md): Kermany OCT 2018: Retinal OCT Image Classification (84,484 images, `cc-by`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [harvard_fairvision](./harvard_fairvision.md): Harvard-FairVision (AMD + DR + Glaucoma, paired SLO + OCT) (30,000 participants, `cc-by-nc-nd`)
- [mario](./mario.md): MARIO: AMD-Progression Longitudinal OCT (MICCAI 2024) (30,000 images, `cc-by`)
- [mmrdr](./mmrdr.md): MMRDR: Multi-Modal Retinal Diabetic Retinopathy Dataset (24,460 images, `cc-by`)
