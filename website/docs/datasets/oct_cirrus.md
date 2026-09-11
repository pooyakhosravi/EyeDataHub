---
id: oct_cirrus
title: "Duke Srinivasan Retinal OCT Dataset"
sidebar_label: oct_cirrus
description: "Forty-five retinal OCT volumes acquired with a Spectralis system: 15 dry AMD, 15 diabetic macular edema, and 15 normal volumes. The official Duke release provides the study data."
tags: ["oct", "research-only", "manual", "classification", "resource-role-current-dataset", "dataset-family-oct-cirrus"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Duke Srinivasan Retinal OCT Dataset

Forty-five retinal OCT volumes acquired with a Spectralis system: 15 dry AMD, 15 diabetic macular edema, and 15 normal volumes. The official Duke release provides the study data.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `oct_cirrus` |
| **Full name** | Duke Srinivasan Retinal OCT Dataset |
| **Publication date** | Unknown |
| **Date basis** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Date notes** | - |
| **Primary category** | `oct` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `oct_cirrus` |
| **Contained modalities** | oct |
| **Tasks** | classification |
| **Primary reported quantity** | 45 volumes |
| **Classes** | 3 (AMD, DME, Normal) |
| **Splits** | all |
| **Size** | 0.58 GB |
| **Source-stated terms** | Research only: research and educational use; commercialization and redistribution prohibited |
| **Normalized terms** | `research-only` |
| **Descriptive screening label** | Research or challenge restriction recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `guided_instructions_only` |
| **Legacy sample-loader status** | Standard loader included |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 45 | `volumes` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [people.duke.edu/~sf59](https://people.duke.edu/~sf59/Srinivasan_BOE_2014_dataset.htm) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> The source permits research and educational use but prohibits commercialization and redistribution. The sample count records 45 volumes; the loader emits their 3,231 B-scans.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download oct_cirrus --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download oct_cirrus --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('oct_cirrus')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [people.duke.edu/~sf59](https://people.duke.edu/~sf59/Srinivasan_BOE_2014_dataset.htm)

**Source-term evidence:** [people.duke.edu/~sf59](https://people.duke.edu/~sf59/Srinivasan_BOE_2014_dataset.htm)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('oct_cirrus')
samples = ds.load(data_dir, split='all')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{oct_cirrus,
  title  = { Duke Srinivasan Retinal OCT Dataset },
  note   = { Srinivasan PP, Kim LA, Mettu PS, et al. Fully automated detection of diabetic macular edema and dry age-related macular degeneration from optical coherence tomography images. Biomed Opt Express. 2014;5:3568-3577. doi:10.1364/BOE.5.003568 },
  year   = { 2014 },
  url    = { https://people.duke.edu/~sf59/Srinivasan_BOE_2014_dataset.htm },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Srinivasan PP, Kim LA, Mettu PS, et al. Fully automated detection of diabetic macular edema and dry age-related macular degeneration from optical coherence tomography images. Biomed Opt Express. 2014;5:3568-3577. doi:10.1364/BOE.5.003568
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Research only: research and educational use; commercialization and redistribution prohibited
- **Normalized category:** `research-only`
- **Apparent scope:** `dataset_files`
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
