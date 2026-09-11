---
id: octid
title: "OCTID: OCT Image Database"
sidebar_label: octid
description: "500 OCT images: NORMAL (206), AMD (50), CSC (128), DR (59), MH (57). High-resolution B-scans for 5-class classification."
tags: ["oct", "cc0", "manual", "classification", "resource-role-current-dataset", "dataset-family-octid", "documented-relationship", "relationship-derived_from"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# OCTID: OCT Image Database

500 OCT images: NORMAL (206), AMD (50), CSC (128), DR (59), MH (57). High-resolution B-scans for 5-class classification.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `octid` |
| **Full name** | OCTID: OCT Image Database |
| **Publication date** | 2018-12-19 |
| **Date basis** | Initial dataset release |
| **Publication date precision** | day |
| **Publication date evidence** | [borealisdata.ca/api](https://borealisdata.ca/api/search?q=OCTID&type=dataset&per_page=100) |
| **Publication date source field** | Borealis Dataverse API search: published_at / versionState |
| **Publication date reviewed** | 2026-09-11 |
| **Date notes** | The official OCTID Dataverse search returns the OCTID citation dataset as RELEASED version 1 with published_at 2018-12-19; the OCTID dataverse contents list all eight component records with the same publicationDate. |
| **Primary category** | `oct` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `octid` |
| **Contained modalities** | oct |
| **Tasks** | classification |
| **Primary reported quantity** | 500 images |
| **Classes** | 5 (NORMAL, AMD, CSC, DR, MH) |
| **Splits** | all |
| **Size** | 0.3 GB |
| **Source-stated terms** | CC0 1.0 Universal |
| **Normalized terms** | `cc0` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `guided_instructions_only` |
| **Legacy sample-loader status** | Standard loader included |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 500 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [borealisdata.ca/dataverse](https://borealisdata.ca/dataverse/OCTID) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Freely available from Borealis Data Repository. No account required.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- [mm_retinal_reason](./mm_retinal_reason.md) is `derived from` this record: The version-pinned official dataset card lists this record among the CFP or OCT sources used to construct MM-Retinal-Reason. ([evidence](https://huggingface.co/datasets/lxirich/MM-Retinal-Reason/tree/d6243baa82c0914dba3c6f43ca79fdbf856982ef))
- [multieye](./multieye.md) is `derived from` this record: The MultiEYE paper names this record as one of the public fundus or OCT sources assembled for the benchmark. ([evidence](https://arxiv.org/abs/2412.09402))
- [x_pcr](./x_pcr.md) is `derived from` this record: Source labels in the version-pinned public X-PCR deposit identify this catalog record as upstream material. ([evidence](https://huggingface.co/datasets/Fantasy666/X-PCR/tree/06a318fd852230326386e3c6514d8a11b7a6b4af))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download octid --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download octid --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('octid')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [borealisdata.ca/dataverse](https://borealisdata.ca/dataverse/OCTID)

**Source-term evidence:** [borealisdata.ca/dataverse](https://borealisdata.ca/dataverse/OCTID)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('octid')
samples = ds.load(data_dir, split='all')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{octid,
  title  = { OCTID: OCT Image Database },
  note   = { Gholami et al., 'OCTID: Optical Coherence Tomography Image Database', Elsevier 2020 },
  year   = { 2020 },
  url    = { https://borealisdata.ca/dataverse/OCTID },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Gholami et al., 'OCTID: Optical Coherence Tomography Image Database', Elsevier 2020.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC0 1.0 Universal
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
