---
id: migs_video
title: "Multicenter Fine-Annotated MIGS Surgical Video Dataset"
sidebar_label: migs_video
description: "A multicenter collection of 186 minimally invasive glaucoma surgery (MIGS) videos with annotations for surgical-phase recognition and semantic segmentation of instruments and anatomical structures."
tags: ["surgical_video", "cc-by", "zenodo", "classification", "segmentation", "resource-role-current-dataset", "dataset-family-migs-video"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Multicenter Fine-Annotated MIGS Surgical Video Dataset

A multicenter collection of 186 minimally invasive glaucoma surgery (MIGS) videos with annotations for surgical-phase recognition and semantic segmentation of instruments and anatomical structures.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `migs_video` |
| **Full name** | Multicenter Fine-Annotated MIGS Surgical Video Dataset |
| **Publication date** | 2026-01-23 |
| **Date basis** | Initial dataset release |
| **Publication date precision** | day |
| **Publication date evidence** | [zenodo.org/api](https://zenodo.org/api/records/18231909) |
| **Publication date source field** | metadata.publication_date (earliest public Zenodo version) |
| **Publication date reviewed** | 2026-09-11 |
| **Date notes** | Earliest listed Zenodo version; current record is later. |
| **Primary category** | `surgical_video` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `migs_video` |
| **Contained modalities** | surgical_video |
| **Tasks** | classification, segmentation |
| **Primary reported quantity** | 186 videos |
| **Classes** | Not reported (Not reported) |
| **Splits** | train, val, test |
| **Size** | 10.23 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Zenodo |
| **Availability** | `available` (checked 2026-07-25) |
| **Acquisition support** | `transfer_tested_partial` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 186 | `videos` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [https://doi.org/10.1038/s41597-026-07535-2](https://doi.org/10.1038/s41597-026-07535-2) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> The current Zenodo version is 10.5281/zenodo.19438128 under CC BY 4.0; the version-independent concept DOI is 10.5281/zenodo.18231908. The associated article cites the earlier deposit version 10.5281/zenodo.18231909.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download migs_video --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download migs_video --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('migs_video')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [zenodo.org/records](https://zenodo.org/records/19438128)

**Source-term evidence:** [zenodo.org/records](https://zenodo.org/records/19438128)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{migs_video,
  title  = { Multicenter Fine-Annotated MIGS Surgical Video Dataset },
  note   = { Wang D, Zhang Y, Li Y, et al., 'Multicenter fine annotated surgical video dataset for minimally invasive glaucoma surgery', Scientific Data 2026. doi:10.1038/s41597-026-07535-2 },
  year   = { 2026 },
  url    = { https://zenodo.org/records/19438128 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Wang D, Zhang Y, Li Y, et al., 'Multicenter fine annotated surgical video dataset for minimally invasive glaucoma surgery', Scientific Data 2026. doi:10.1038/s41597-026-07535-2
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC BY 4.0
- **Normalized category:** `cc-by`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Standard label without an explicit NC clause; not a permission finding

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [ophora](./ophora.md): Ophora-160K: Ophthalmic Surgical Video Instruction Dataset (162,185 video clip instruction pairs, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [insegcat](./insegcat.md): InSegCat: Instance Segmentation for Cataract Surgery (5,581 annotated images, `research-only`)
- [cadis](./cadis.md): CaDIS: Cataract Dataset for Image Segmentation (4,670 images, `research-only`)
- [cataract_lmm](./cataract_lmm.md): Cataract-LMM: Large-Scale Multi-Source Multi-Task Cataract Surgery Benchmark (3,000 videos, `cc-by-nc-nd`)
- [ophnet2024](./ophnet2024.md): OphNet2024: Ophthalmic Surgical Video Dataset (2,278 videos, `cc-by-nc-sa`)
- [lmod_cataract_1k](./lmod_cataract_1k.md): LMOD-Cataract-1K (2,256 images, `cc-by`)
- [lmod_cataract_1k_cot](./lmod_cataract_1k_cot.md): Cataract-1K Surgical Analysis Chain-of-Thought Dataset (2,256 images, `mit`)
