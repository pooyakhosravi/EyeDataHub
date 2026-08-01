---
id: papila
title: "PAPILA: Glaucoma Fundus Dataset with Clinical Data"
sidebar_label: papila
description: "488 fundus images from 244 patients (both eyes). Expert OD/OC segmentation, glaucoma stage, IOP, and clinical metadata."
tags: ["fundus", "tabular", "cc-by", "direct", "classification", "segmentation"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# PAPILA: Glaucoma Fundus Dataset with Clinical Data

488 fundus images from 244 patients (both eyes). Expert OD/OC segmentation, glaucoma stage, IOP, and clinical metadata.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `papila` |
| **Full name** | PAPILA: Glaucoma Fundus Dataset with Clinical Data |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus, tabular |
| **Tasks** | classification, segmentation |
| **Samples** | 488 |
| **Classes** | 3 (Healthy, Glaucoma suspect, Glaucoma) |
| **Splits** | all |
| **Size** | 0.4 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Direct HTTP |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `guided_instructions_only` |
| **Legacy sample-loader status** | Standard loader included |


## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download papila --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download papila --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('papila')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [zenodo.org/records](https://zenodo.org/records/6379970)

**Source-term evidence:** [zenodo.org/records](https://zenodo.org/records/6379970)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('papila')
samples = ds.load(data_dir, split='all')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{papila,
  title  = { PAPILA: Glaucoma Fundus Dataset with Clinical Data },
  note   = { Kovalyk et al., 'PAPILA: Dataset with fundus images and clinical data of both eyes of the same patient for glaucoma assessment', Scientific Data 2022 },
  year   = { 2022 },
  url    = { https://zenodo.org/records/6379970 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Kovalyk et al., 'PAPILA: Dataset with fundus images and clinical data of both eyes of the same patient for glaucoma assessment', Scientific Data 2022.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC BY 4.0
- **Normalized category:** `cc-by`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Standard label without an explicit NC clause; not a permission finding

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Related datasets with shared modalities

- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 records, `unknown`)
- [fairvlmed](./fairvlmed.md): FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset (10,000 records, `cc-by-nc-nd`)
- [olives](./olives.md): OLIVES: Ophthalmic Labels for Investigating Visual Eye Semantics (9,408 records, `cc-by`)
- [fprm_retina](./fprm_retina.md): FPRM Multimodal Eye Imaging and Psychological Assessment Dataset (3,361 records, `research-only`)
- [grape](./grape.md): GRAPE: Glaucoma Real-world Appraisal Progression Ensemble (1,115 records, `cc0`)
- [ocular_chat_vqa](./ocular_chat_vqa.md): OcularChat-VQA: AREDS-Derived Patient-Physician Dialogue Dataset (844,000 records, `cc-by-nc-sa`)
- [airogs](./airogs.md): AIROGS: AI for Robust Glaucoma Screening (113,893 records, `cc-by-nc-nd`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 records, `unknown`)
