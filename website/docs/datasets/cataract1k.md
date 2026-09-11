---
id: cataract1k
title: "Cataract-1K: Large-Scale Cataract Surgery Video Dataset"
sidebar_label: cataract1k
description: "1000 cataract surgery videos from multiple surgeons annotated for 10 surgical phases, instrument segmentation, and tool presence detection. First large-scale cataract surgical video dataset."
tags: ["surgical_video", "research-only", "manual", "phase_recognition", "segmentation", "detection", "resource-role-current-dataset", "dataset-family-cataract1k", "documented-relationship", "relationship-derived_from"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Cataract-1K: Large-Scale Cataract Surgery Video Dataset

1000 cataract surgery videos from multiple surgeons annotated for 10 surgical phases, instrument segmentation, and tool presence detection. First large-scale cataract surgical video dataset.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `cataract1k` |
| **Full name** | Cataract-1K: Large-Scale Cataract Surgery Video Dataset |
| **Publication date** | Unknown |
| **Date basis** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Date notes** | - |
| **Primary category** | `surgical_video` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `cataract1k` |
| **Contained modalities** | surgical_video |
| **Tasks** | phase_recognition, segmentation, detection |
| **Primary reported quantity** | 1,000 videos |
| **Classes** | 10 (Incision, Viscoelastic, Capsulorhexis, Hydrodissection, Phacoemulsification, Irrigation-Aspiration, Capsule Polishing, Lens Implant, Viscoelastic Suction, Tonifying-Antibiotics) |
| **Splits** | train, val, test |
| **Size** | 50.0 GB |
| **Source-stated terms** | Research only — see Synapse terms |
| **Normalized terms** | `research-only` |
| **Descriptive screening label** | Research or challenge restriction recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `controlled_or_manual` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `manual_access_blocked` |
| **Legacy sample-loader status** | Standard loader included |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 1,000 | `videos` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [synapse.org](https://www.synapse.org/#!Synapse:syn53404917) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Data hosted on Synapse (free registration required). Install synapseclient: pip install synapseclient. Then: synapse get syn53404917

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- [lmod_cataract_1k](./lmod_cataract_1k.md) is `derived from` this record: The dataset card identifies Cataract-1K as the source of the processed surgical frames. ([evidence](https://huggingface.co/datasets/mehti/LMOD-Cataract-1K))
- [lmod_plus](./lmod_plus.md) is `derived from` this record: The LMOD+ project page lists nine component datasets, including the five cataloged targets represented by these edges. ([evidence](https://kfzyqin.github.io/lmod_plus/))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# This route requires upstream human action; no transfer starts.
eyehub download cataract1k --data-dir ./data --dry-run --json
# Follow the official instructions shown by preflight.
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('cataract1k')
print(preflight_dataset(ds, './data'))  # returns manual_access_blocked
```

  </TabItem>
</Tabs>

**Upstream page:** [synapse.org](https://www.synapse.org/#!Synapse:syn53404917)

**Source-term evidence:** [synapse.org](https://www.synapse.org/#!Synapse:syn53404917)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('cataract1k')
samples = ds.load(data_dir, split='test')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{cataract1k,
  title  = { Cataract-1K: Large-Scale Cataract Surgery Video Dataset },
  note   = { Ghamsarian N et al., 'Cataract-1K: Cataract Surgery Dataset for Domain Generalization of Surgical Workflow Analysis', IEEE TMI 2024. https://github.com/Negin-Ghamsarian/Cataract-1K },
  year   = { 2024 },
  url    = { https://www.synapse.org/#!Synapse:syn53404917 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Ghamsarian N et al., 'Cataract-1K: Cataract Surgery Dataset for Domain Generalization of Surgical Workflow Analysis', IEEE TMI 2024. https://github.com/Negin-Ghamsarian/Cataract-1K
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Research only — see Synapse terms
- **Normalized category:** `research-only`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Research or challenge restriction recorded; check source

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
