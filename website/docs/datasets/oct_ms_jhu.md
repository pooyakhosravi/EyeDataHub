---
id: oct_ms_jhu
title: "OCT Retinal Layer Segmentation — MS & Healthy Controls (JHU/IACL)"
sidebar_label: oct_ms_jhu
description: "35 Spectralis OCT volumes (1,715 B-scans) with 9 manually delineated retinal layer boundaries. 14 healthy controls, 21 MS subjects."
tags: ["oct", "cc-by-nc-nd", "direct", "segmentation", "resource-role-current-dataset", "dataset-family-oct-ms-jhu"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# OCT Retinal Layer Segmentation — MS & Healthy Controls (JHU/IACL)

35 Spectralis OCT volumes (1,715 B-scans) with 9 manually delineated retinal layer boundaries. 14 healthy controls, 21 MS subjects.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `oct_ms_jhu` |
| **Full name** | OCT Retinal Layer Segmentation — MS & Healthy Controls (JHU/IACL) |
| **Publication date** | Unknown |
| **Date basis** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Date notes** | - |
| **Primary category** | `oct` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `oct_ms_jhu` |
| **Contained modalities** | oct |
| **Tasks** | segmentation |
| **Primary reported quantity** | 1,715 b scans |
| **Classes** | 9 (ILM, RNFL-OPL, OPL-ONL, ELM, MZ, EZ, OSP, IZ-RPE, RPE) |
| **Splits** | all |
| **Size** | 1.8 GB |
| **Source-stated terms** | CC BY-NC-ND |
| **Normalized terms** | `cc-by-nc-nd` |
| **Descriptive screening label** | Explicit noncommercial clause recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Direct HTTP |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `loader_implemented_not_live_tested` |
| **Legacy sample-loader status** | Standard loader included |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 1,715 | `b_scans` | B-scans in 35 OCT volumes | `associated_publication` | [https://doi.org/10.1016/j.dib.2018.11.060](https://doi.org/10.1016/j.dib.2018.11.060) |
| Additional | 35 | `volumes` | Spectralis OCT volumes | `associated_publication` | [https://doi.org/10.1016/j.dib.2018.11.060](https://doi.org/10.1016/j.dib.2018.11.060) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download oct_ms_jhu --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download oct_ms_jhu --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('oct_ms_jhu')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [iacl.ece.jhu.edu/~aaron](https://iacl.ece.jhu.edu/~aaron/data/OCT_Manual_Delineations-2018_June_29_b.zip)

**Source-term evidence:** [iacl.ece.jhu.edu/~aaron](https://iacl.ece.jhu.edu/~aaron/data/OCT_Manual_Delineations-2018_June_29_b.zip)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('oct_ms_jhu')
samples = ds.load(data_dir, split='all')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{oct_ms_jhu,
  title  = { OCT Retinal Layer Segmentation — MS & Healthy Controls (JHU/IACL) },
  note   = { Y. He et al., 'Retinal layer parcellation of optical coherence tomography images: Data resource for Multiple Sclerosis and Healthy Controls', Data in Brief 22:601-604, 2019 },
  year   = { 2019 },
  url    = { https://iacl.ece.jhu.edu/~aaron/data/OCT_Manual_Delineations-2018_June_29_b.zip },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Y. He et al., 'Retinal layer parcellation of optical coherence tomography images: Data resource for Multiple Sclerosis and Healthy Controls', Data in Brief 22:601-604, 2019.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC BY-NC-ND
- **Normalized category:** `cc-by-nc-nd`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Explicit noncommercial clause recorded; check source

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
