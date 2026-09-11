---
id: tsukazaki_uwf
title: "Tsukazaki Hospital UWF Fundus Dataset"
sidebar_label: tsukazaki_uwf
description: "13,047 ultra-widefield fundus photographs (Optos, 200° FOV) from Tsukazaki Hospital, annotated with 8 binary disease labels: AO, AMD, DR, Glaucoma, MH, RD, RP, RVO. Associated with Scientific Data 202"
tags: ["uwf_fundus", "research-only", "github", "multilabel", "classification", "resource-role-current-dataset", "dataset-family-tsukazaki-uwf"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Tsukazaki Hospital UWF Fundus Dataset

13,047 ultra-widefield fundus photographs (Optos, 200° FOV) from Tsukazaki Hospital, annotated with 8 binary disease labels: AO, AMD, DR, Glaucoma, MH, RD, RP, RVO. Associated with Scientific Data 2024.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `tsukazaki_uwf` |
| **Full name** | Tsukazaki Hospital UWF Fundus Dataset |
| **First published** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Primary category** | `uwf_fundus` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `tsukazaki_uwf` |
| **Contained modalities** | uwf_fundus |
| **Tasks** | multilabel, classification |
| **Primary reported quantity** | 13,047 images |
| **Classes** | 8 (AO, AMD, DR, Gla, MH, RD, RP, RVO) |
| **Splits** | train, test |
| **Size** | 15.0 GB |
| **Source-stated terms** | Research only — contact authors for data access |
| **Normalized terms** | `research-only` |
| **Descriptive screening label** | Research or challenge restriction recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `author_contact` |
| **Route backend** | GitHub |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `manual_access_blocked` |
| **Legacy sample-loader status** | Standard loader included |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 13,047 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [github.com/DateCazuki](https://github.com/DateCazuki/Fundus_Diagnosis) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Full dataset is subject to Japanese export restrictions. Contact the authors for access. A public subset may be available via the GitHub repo or linked Figshare.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# This route requires upstream human action; no transfer starts.
eyehub download tsukazaki_uwf --data-dir ./data --dry-run --json
# Follow the official instructions shown by preflight.
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('tsukazaki_uwf')
print(preflight_dataset(ds, './data'))  # returns manual_access_blocked
```

  </TabItem>
</Tabs>

**Upstream page:** [github.com/DateCazuki](https://github.com/DateCazuki/Fundus_Diagnosis)

**Source-term evidence:** [github.com/DateCazuki](https://github.com/DateCazuki/Fundus_Diagnosis)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('tsukazaki_uwf')
samples = ds.load(data_dir, split='test')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{tsukazaki_uwf,
  title  = { Tsukazaki Hospital UWF Fundus Dataset },
  note   = { Nagasawa T et al., 'Automatic detection of multiple retinal diseases in ultra-widefield fundus images using deep learning', Nature Machine Intelligence 2022. https://www.nature.com/articles/s42256-022-00566-5 — Data: https://github.com/DateCazuki/Fundus_Diagnosis },
  year   = { 2022 },
  url    = { https://github.com/DateCazuki/Fundus_Diagnosis },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Nagasawa T et al., 'Automatic detection of multiple retinal diseases in ultra-widefield fundus images using deep learning', Nature Machine Intelligence 2022. https://www.nature.com/articles/s42256-022-00566-5 — Data: https://github.com/DateCazuki/Fundus_Diagnosis
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Research only — contact authors for data access
- **Normalized category:** `research-only`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Research or challenge restriction recorded; check source

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [mmrdr](./mmrdr.md): MMRDR: Multi-Modal Retinal Diabetic Retinopathy Dataset (24,460 images, `cc-by`)
- [oculoscope](./oculoscope.md): OculoScope: Fairer AI in Ophthalmology Dataset (16,530 images, `cc-by`)
- [birdshot_wide](./birdshot_wide.md): Birdshot-WIDE Widefield Fundus Dataset (6,352 images, `cc-by`)
- [deepdrid](./deepdrid.md): DeepDRiD: Diabetic Retinopathy Grading and Image Quality Dataset (2,256 images, `cc-by-sa`)
- [uwf_tumor](./uwf_tumor.md): UWF Fundus Intraocular Tumor Dataset (2,031 images, `cc-by`)
- [uwf_dr_peng](./uwf_dr_peng.md): UWF Fundus DR Dataset (Peng et al., 2026) (1,630 images, `cc-by`)
- [uwf_zhejiang](./uwf_zhejiang.md): Open UWF Fundus Dataset with Disease + Quality Labels (700 images, `cc-by`)
- [uwf_dr](./uwf_dr.md): UWF DR Reasoning Dataset (495 images, `research-only`)
