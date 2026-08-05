---
id: rasti_oct
title: "Rasti OCT Dataset (Noor Eye Hospital, Tehran)"
sidebar_label: rasti_oct
description: "148 Heidelberg Spectralis SD-OCT volumes (~4,254 B-scans) for 3-class volume-level classification: Normal (50 volumes), AMD (48 volumes), DME (50 volumes). Variable B-scans per volume: 19, 25, 31, or "
tags: ["oct", "research-only", "manual", "classification", "resource-role-current-dataset", "dataset-family-rasti-oct"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Rasti OCT Dataset (Noor Eye Hospital, Tehran)

148 Heidelberg Spectralis SD-OCT volumes (~4,254 B-scans) for 3-class volume-level classification: Normal (50 volumes), AMD (48 volumes), DME (50 volumes). Variable B-scans per volume: 19, 25, 31, or 61 slices. Acquired at Noor Eye Hospital, Tehran, Iran.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `rasti_oct` |
| **Full name** | Rasti OCT Dataset (Noor Eye Hospital, Tehran) |
| **Primary category** | `oct` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `rasti_oct` |
| **Contained modalities** | oct |
| **Tasks** | classification |
| **Primary reported quantity** | 4,254 b scans |
| **Classes** | 3 (Normal, AMD, DME) |
| **Splits** | train |
| **Size** | 2.0 GB |
| **Source-stated terms** | Research use only |
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
| Primary | 4,254 | `b_scans` | Approximate B-scan count | `associated_publication` | [https://doi.org/10.1109/TMI.2017.2780115](https://doi.org/10.1109/TMI.2017.2780115) |
| Additional | 148 | `volumes` | Heidelberg Spectralis volumes | `associated_publication` | [https://doi.org/10.1109/TMI.2017.2780115](https://doi.org/10.1109/TMI.2017.2780115) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> The Google Drive archive is password-protected. Obtain the current archive password from the official source and download manually:
>   Main archive: https://drive.google.com/file/d/1Rv82F7CjPveyONdy1YbRHh05emCb6_Eu
>   DME labels:   https://drive.google.com/file/d/1ocxB44TiiInE-jnt8Go6XQNmFwdTxOyN
>   AMD labels:   https://drive.google.com/file/d/1yaNiK40QL_s7fgMLM98l_F3TCMwFERnP
> Label files flag 'suspicious' B-scans (≥50% threshold) within each volume.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download rasti_oct --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download rasti_oct --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('rasti_oct')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [drive.google.com/file](https://drive.google.com/file/d/1Rv82F7CjPveyONdy1YbRHh05emCb6_Eu)

**Source-term evidence:** [drive.google.com/file](https://drive.google.com/file/d/1Rv82F7CjPveyONdy1YbRHh05emCb6_Eu)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('rasti_oct')
samples = ds.load(data_dir, split='train')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{rasti_oct,
  title  = { Rasti OCT Dataset (Noor Eye Hospital, Tehran) },
  note   = { Rasti R et al., 'Macular OCT Classification Using a Multi-Scale Convolutional Neural Network Ensemble', IEEE Transactions on Medical Imaging 37(4):1024–1034 (2018). doi:10.1109/TMI.2017.2780115 },
  year   = { 2018 },
  url    = { https://drive.google.com/file/d/1Rv82F7CjPveyONdy1YbRHh05emCb6_Eu },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Rasti R et al., 'Macular OCT Classification Using a Multi-Scale Convolutional Neural Network Ensemble', IEEE Transactions on Medical Imaging 37(4):1024–1034 (2018). doi:10.1109/TMI.2017.2780115
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Research use only
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
