---
id: duke_chiu_boe
title: "Duke OCT DME Dataset (Chiu BOE 2014)"
sidebar_label: duke_chiu_boe
description: "110 OCT B-scans from 10 DME subjects with 8 layer boundaries and fluid region annotations by 2 clinicians."
tags: ["oct", "research-only", "direct", "segmentation", "documented-relationship", "relationship-derived_from"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Duke OCT DME Dataset (Chiu BOE 2014)

110 OCT B-scans from 10 DME subjects with 8 layer boundaries and fluid region annotations by 2 clinicians.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `duke_chiu_boe` |
| **Full name** | Duke OCT DME Dataset (Chiu BOE 2014) |
| **Primary category** | `oct` |
| **Contained modalities** | oct |
| **Tasks** | segmentation |
| **Primary reported quantity** | 110 images |
| **Classes** | 8 (ILM, NFL-GCL, IPL-INL, INL-OPL, OPL-ONL, IS-OS, OS-RPE, BM) |
| **Splits** | all |
| **Size** | 0.1 GB |
| **Source-stated terms** | Research use (Duke University) |
| **Normalized terms** | `research-only` |
| **Descriptive screening label** | Research or challenge restriction recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Direct HTTP |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `loader_implemented_not_live_tested` |
| **Legacy sample-loader status** | Standard loader included |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 110 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [people.duke.edu/~sf59](http://people.duke.edu/~sf59/Chiu_BOE_2014_dataset.htm) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- [mm_retinal_reason](./mm_retinal_reason.md) is `derived from` this record: The version-pinned official dataset card lists this record among the CFP or OCT sources used to construct MM-Retinal-Reason. ([evidence](https://huggingface.co/datasets/lxirich/MM-Retinal-Reason/tree/d6243baa82c0914dba3c6f43ca79fdbf856982ef))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download duke_chiu_boe --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download duke_chiu_boe --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('duke_chiu_boe')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [people.duke.edu/~sf59](http://people.duke.edu/~sf59/Chiu_BOE_2014_dataset.htm)

**Source-term evidence:** [people.duke.edu/~sf59](http://people.duke.edu/~sf59/Chiu_BOE_2014_dataset.htm)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('duke_chiu_boe')
samples = ds.load(data_dir, split='all')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{duke_chiu_boe,
  title  = { Duke OCT DME Dataset (Chiu BOE 2014) },
  note   = { Chiu et al., 'Kernel regression based segmentation of optical coherence tomography images with diabetic macular edema', Biomedical Optics Express 2014. DOI: 10.1364/BOE.6.001172 },
  year   = { 2014 },
  url    = { http://people.duke.edu/~sf59/Chiu_BOE_2014_dataset.htm },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Chiu et al., 'Kernel regression based segmentation of optical coherence tomography images with diabetic macular edema', Biomedical Optics Express 2014. DOI: 10.1364/BOE.6.001172
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Research use (Duke University)
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
