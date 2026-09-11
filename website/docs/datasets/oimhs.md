---
id: oimhs
title: "OIMHS: OCT Image Macular Hole Segmentation Dataset"
sidebar_label: oimhs
description: "3,859 OCT B-scan images (125 eyes, 119 patients) for macular hole segmentation. Each PNG is side-by-side: left half raw B-scan, right half colour-coded mask for 4 classes: Retina, Macular Hole, Intrar"
tags: ["oct", "cc0", "figshare", "segmentation", "resource-role-current-dataset", "dataset-family-oimhs", "documented-relationship", "relationship-derived_from"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# OIMHS: OCT Image Macular Hole Segmentation Dataset

3,859 OCT B-scan images (125 eyes, 119 patients) for macular hole segmentation. Each PNG is side-by-side: left half raw B-scan, right half colour-coded mask for 4 classes: Retina, Macular Hole, Intraretinal Cysts, Choroid.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `oimhs` |
| **Full name** | OIMHS: OCT Image Macular Hole Segmentation Dataset |
| **First published** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Primary category** | `oct` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `oimhs` |
| **Contained modalities** | oct |
| **Tasks** | segmentation |
| **Primary reported quantity** | 3,859 images |
| **Classes** | 4 (Retina, Macular Hole, Intraretinal Cysts, Choroid) |
| **Splits** | train |
| **Size** | 2.0 GB |
| **Source-stated terms** | CC0 1.0 |
| **Normalized terms** | `cc0` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Figshare |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `end_to_end_tested` |
| **Legacy sample-loader status** | Standard loader included |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 3,859 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [https://doi.org/10.6084/m9.figshare.23508453](https://doi.org/10.6084/m9.figshare.23508453) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Images are side-by-side PNGs (left=raw, right=mask). 125 eye-level subfolders under images/. No official split — apply your own train/val/test division.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- [lmod_plus](./lmod_plus.md) is `derived from` this record: The LMOD+ project page lists nine component datasets, including the five cataloged targets represented by these edges. ([evidence](https://kfzyqin.github.io/lmod_plus/))
- [mm_retinal_reason](./mm_retinal_reason.md) is `derived from` this record: The version-pinned official dataset card lists this record among the CFP or OCT sources used to construct MM-Retinal-Reason. ([evidence](https://huggingface.co/datasets/lxirich/MM-Retinal-Reason/tree/d6243baa82c0914dba3c6f43ca79fdbf856982ef))
- [x_pcr](./x_pcr.md) is `derived from` this record: Source labels in the version-pinned public X-PCR deposit identify this catalog record as upstream material. ([evidence](https://huggingface.co/datasets/Fantasy666/X-PCR/tree/06a318fd852230326386e3c6514d8a11b7a6b4af))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download oimhs --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download oimhs --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('oimhs')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.6084/m9.figshare.23508453](https://doi.org/10.6084/m9.figshare.23508453)

**Source-term evidence:** [https://doi.org/10.6084/m9.figshare.23508453](https://doi.org/10.6084/m9.figshare.23508453)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('oimhs')
samples = ds.load(data_dir, split='train')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{oimhs,
  title  = { OIMHS: OCT Image Macular Hole Segmentation Dataset },
  note   = { Ye X et al., 'OIMHS: An Optical Coherence Tomography Image Dataset Based on Macular Hole Manual Segmentation', Scientific Data 10, 769 (2023). doi:10.1038/s41597-023-02675-1 },
  year   = { 2023 },
  url    = { https://doi.org/10.6084/m9.figshare.23508453 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Ye X et al., 'OIMHS: An Optical Coherence Tomography Image Dataset Based on Macular Hole Manual Segmentation', Scientific Data 10, 769 (2023). doi:10.1038/s41597-023-02675-1
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC0 1.0
- **Normalized category:** `cc0`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Standard label without an explicit NC clause; not a permission finding

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
