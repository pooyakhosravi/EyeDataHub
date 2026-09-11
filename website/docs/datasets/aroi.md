---
id: aroi
title: "AROI: Annotated Retinal OCT Images Database"
sidebar_label: aroi
description: "1,136 OCT B-scans from 24 AMD patients. Expert annotations for 3 retinal fluid types (IRF, SRF, PED) and 3 retinal layer boundaries for joint layer and fluid segmentation."
tags: ["oct", "research-only", "gdrive", "segmentation", "resource-role-current-dataset", "dataset-family-aroi"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# AROI: Annotated Retinal OCT Images Database

1,136 OCT B-scans from 24 AMD patients. Expert annotations for 3 retinal fluid types (IRF, SRF, PED) and 3 retinal layer boundaries for joint layer and fluid segmentation.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `aroi` |
| **Full name** | AROI: Annotated Retinal OCT Images Database |
| **Publication date** | Unknown |
| **Date basis** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Date notes** | - |
| **Primary category** | `oct` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `aroi` |
| **Contained modalities** | oct |
| **Tasks** | segmentation |
| **Primary reported quantity** | 1,136 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | train, test |
| **Size** | 0.5 GB |
| **Source-stated terms** | Research only — cite required papers (see citation field) |
| **Normalized terms** | `research-only` |
| **Descriptive screening label** | Research or challenge restriction recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Google Drive |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `loader_implemented_not_live_tested` |
| **Legacy sample-loader status** | Standard loader included |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 1,136 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [drive.google.com/file](https://drive.google.com/file/d/10Ys4xsw81evjHewZEvqHy4Kri0my8C2S/view) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download aroi --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download aroi --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('aroi')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [drive.google.com/file](https://drive.google.com/file/d/10Ys4xsw81evjHewZEvqHy4Kri0my8C2S/view)

**Source-term evidence:** [drive.google.com/file](https://drive.google.com/file/d/10Ys4xsw81evjHewZEvqHy4Kri0my8C2S/view)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('aroi')
samples = ds.load(data_dir, split='test')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{aroi,
  title  = { AROI: Annotated Retinal OCT Images Database },
  note   = { M. Melinščak, M. Radmilović, Z. Vatavuk, S. Lončarić, 'Annotated retinal optical coherence tomography images (AROI) database for joint retinal layer and fluid segmentation', Automatika, vol. 62, no. 3, pp. 375–385, Jul. 2021. doi:10.1080/00051144.2021.1973298 | M. Melinščak et al., 'AROI: Annotated Retinal OCT Images database', MIPRO 2021, pp. 400–405 | M. Melinščak, 'Attention-based U-net: Joint segmentation of layers and fluids from retinal OCT images', MIPRO 2023, pp. 391–396 | M. Melinščak, 'Enhancing Interpretability in Retinal OCT Analysis Using Grad-CAM: A Study on the AROI Dataset', MIPRO 2025, pp. 1433–1438 },
  year   = { 2021 },
  url    = { https://drive.google.com/file/d/10Ys4xsw81evjHewZEvqHy4Kri0my8C2S/view },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
M. Melinščak, M. Radmilović, Z. Vatavuk, S. Lončarić, 'Annotated retinal optical coherence tomography images (AROI) database for joint retinal layer and fluid segmentation', Automatika, vol. 62, no. 3, pp. 375–385, Jul. 2021. doi:10.1080/00051144.2021.1973298 | M. Melinščak et al., 'AROI: Annotated Retinal OCT Images database', MIPRO 2021, pp. 400–405 | M. Melinščak, 'Attention-based U-net: Joint segmentation of layers and fluids from retinal OCT images', MIPRO 2023, pp. 391–396 | M. Melinščak, 'Enhancing Interpretability in Retinal OCT Analysis Using Grad-CAM: A Study on the AROI Dataset', MIPRO 2025, pp. 1433–1438.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Research only — cite required papers (see citation field)
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
