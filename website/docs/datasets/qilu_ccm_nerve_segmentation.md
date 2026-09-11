---
id: qilu_ccm_nerve_segmentation
title: "Qilu Annotated Corneal Confocal Microscopy Nerve Segmentation Dataset"
sidebar_label: qilu_ccm_nerve_segmentation
description: "A human corneal confocal microscopy dataset containing 410 source images from 88 participants, 410 filename-matched pixel-level nerve segmentation masks, 20 repeat annotations, and image-linked clinic"
tags: ["confocal", "tabular", "cc-by", "zenodo", "segmentation", "classification", "measurement", "resource-role-current-dataset", "dataset-family-qilu-ccm-nerve-segmentation"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Qilu Annotated Corneal Confocal Microscopy Nerve Segmentation Dataset

A human corneal confocal microscopy dataset containing 410 source images from 88 participants, 410 filename-matched pixel-level nerve segmentation masks, 20 repeat annotations, and image-linked clinical and demographic data.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `qilu_ccm_nerve_segmentation` |
| **Full name** | Qilu Annotated Corneal Confocal Microscopy Nerve Segmentation Dataset |
| **First published** | 2025-11-10 |
| **Publication date precision** | day |
| **Publication date evidence** | [zenodo.org/api](https://zenodo.org/api/records/17570503) |
| **Publication date source field** | metadata.publication_date (earliest public Zenodo version) |
| **Publication date reviewed** | 2026-09-11 |
| **Primary category** | `confocal` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `qilu_ccm_nerve_segmentation` |
| **Contained modalities** | confocal, tabular |
| **Tasks** | segmentation, classification, measurement |
| **Primary reported quantity** | 410 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | set1, set2 |
| **Size** | 0.06370422896 GB |
| **Source-stated terms** | Creative Commons Attribution 4.0 International |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Zenodo |
| **Availability** | `available` (checked 2026-08-02) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Standard loader included |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 410 | `images` | Original CCM images in Set1 and Set2 Set1 contains 210 images and Set2 contains 200 images. | `associated_publication` | [https://doi.org/10.1038/s41597-026-07418-6](https://doi.org/10.1038/s41597-026-07418-6) |
| Additional | 410 | `annotated_images` | Filename-matched binary nerve segmentation masks One expert-reviewed pixel-level mask per source image. | `associated_publication` | [https://doi.org/10.1038/s41597-026-07418-6](https://doi.org/10.1038/s41597-026-07418-6) |
| Additional | 88 | `participants` | Participants represented across Set1 and Set2 Set1 has 34 participants and Set2 has 54 participants. | `associated_publication` | [https://doi.org/10.1038/s41597-026-07418-6](https://doi.org/10.1038/s41597-026-07418-6) |
| Additional | 20 | `annotated_images` | Subset with repeat annotations These are repeat labels for existing images, not 20 additional images. | `associated_publication` | [https://doi.org/10.1038/s41597-026-07418-6](https://doi.org/10.1038/s41597-026-07418-6) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> The current Zenodo deposit contains one 68,401,895-byte archive with 410 source PNG images, 410 corresponding masks, 20 repeat annotations, and one linked workbook. The version-specific dataset DOI is 10.5281/zenodo.18779434 and the concept DOI is 10.5281/zenodo.17570502. Reference 35 in the published article lists 10.5281/zenodo.17570504, which resolves to an unrelated record; the article's Data Records section and the official deposit identify 10.5281/zenodo.18779434.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download qilu_ccm_nerve_segmentation --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download qilu_ccm_nerve_segmentation --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('qilu_ccm_nerve_segmentation')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [zenodo.org/records](https://zenodo.org/records/18779434)

**Source-term evidence:** [zenodo.org/records](https://zenodo.org/records/18779434)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('qilu_ccm_nerve_segmentation')
samples = ds.load(data_dir, split='set1')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{qilu_ccm_nerve_segmentation,
  title  = { Qilu Annotated Corneal Confocal Microscopy Nerve Segmentation Dataset },
  note   = { Qiao Q, Cao J, Hou X. An Annotated Corneal Confocal Microscopy Dataset for Nerve Segmentation and Clinical Characterization. Scientific Data. 2026;13:1051. doi:10.1038/s41597-026-07418-6. Dataset: doi:10.5281/zenodo.18779434 },
  year   = { 2026 },
  url    = { https://zenodo.org/records/18779434 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Qiao Q, Cao J, Hou X. An Annotated Corneal Confocal Microscopy Dataset for Nerve Segmentation and Clinical Characterization. Scientific Data. 2026;13:1051. doi:10.1038/s41597-026-07418-6. Dataset: doi:10.5281/zenodo.18779434.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Creative Commons Attribution 4.0 International
- **Normalized category:** `cc-by`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Standard label without an explicit NC clause; not a permission finding

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [ocular_chat_vqa](./ocular_chat_vqa.md): OcularChat-VQA: AREDS-Derived Patient-Physician Dialogue Dataset (844,000 records, `cc-by-nc-sa`)
- [brset_mbrset_embeddings](./brset_mbrset_embeddings.md): Embedding-Based Representations for BRSET and mBRSET (53,188 embedding vectors, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [oculoscope](./oculoscope.md): OculoScope: Fairer AI in Ophthalmology Dataset (16,530 images, `cc-by`)
- [dryad_r7s04](./dryad_r7s04.md): Data from: Prevalence of depression, anxiety, adjustment disorders, and somatoform disorders in patients with age-related macular degeneration in Germany (15,160 participants, `cc0`)
- [corn_collection](./corn_collection.md): CORN: Corneal Confocal Microscope Dataset Collection (12,931 images, `cc-by`)
- [fairvlmed](./fairvlmed.md): FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset (10,000 images, `cc-by-nc-nd`)
- [leops_erg](./leops_erg.md): LEOPs Light-Adapted Electroretinogram and Oscillatory Potentials Dataset (9,743 signals, `cc-by`)
