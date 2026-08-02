---
id: mario
title: "MARIO: AMD-Progression Longitudinal OCT (MICCAI 2024)"
sidebar_label: mario
description: "~30,000 longitudinal OCT B-scans across multiple patient visits, annotated for AMD change detection and progression monitoring."
tags: ["oct", "cc-by", "zenodo", "classification", "progression", "resource-role-current-dataset", "dataset-family-mario"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# MARIO: AMD-Progression Longitudinal OCT (MICCAI 2024)

~30,000 longitudinal OCT B-scans across multiple patient visits, annotated for AMD change detection and progression monitoring.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mario` |
| **Full name** | MARIO: AMD-Progression Longitudinal OCT (MICCAI 2024) |
| **Primary category** | `oct` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `mario` |
| **Contained modalities** | oct |
| **Tasks** | classification, progression |
| **Primary reported quantity** | 30,000 images |
| **Classes** | 4 (Not reported) |
| **Splits** | train, val, test |
| **Size** | 25.0 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Zenodo |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 30,000 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [zenodo.org/records](https://zenodo.org/records/15270469) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Distributed as 21 multi-part split zips (Task_1.zip.001-014 + Task_2.zip.001-007, ~21.8 GB). After download, reassemble with `cat Task_1.zip.* &gt; Task_1.zip` then extract with 7-Zip. The Zenodo files are marked CC BY 4.0. Check any separate challenge rules before entering a competition.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mario --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download mario --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mario')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [zenodo.org/records](https://zenodo.org/records/15270469)

**Source-term evidence:** [zenodo.org/records](https://zenodo.org/records/15270469)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mario,
  title  = { MARIO: AMD-Progression Longitudinal OCT (MICCAI 2024) },
  note   = { Quellec G, Zeghlache R, et al., 'MARIO: Monitoring AMD Progression from OCT — MICCAI 2024 Challenge', arXiv 2506.02976. Data: Zenodo doi:10.5281/zenodo.15270469 (2025). Peer-reviewed proceedings pending },
  year   = { 2024 },
  url    = { https://zenodo.org/records/15270469 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Quellec G, Zeghlache R, et al., 'MARIO: Monitoring AMD Progression from OCT — MICCAI 2024 Challenge', arXiv 2506.02976. Data: Zenodo doi:10.5281/zenodo.15270469 (2025). Peer-reviewed proceedings pending.
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

- [syn_oct](./syn_oct.md): SYN-OCT Synthetic Glaucoma OCT Dataset (200,000 images, `cc-by`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (103,959 images, `mit`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [kermany_oct](./kermany_oct.md): Kermany OCT 2018: Retinal OCT Image Classification (84,484 images, `cc-by`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [harvard_fairvision](./harvard_fairvision.md): Harvard-FairVision (AMD + DR + Glaucoma, paired SLO + OCT) (30,000 participants, `cc-by-nc-nd`)
- [mmrdr](./mmrdr.md): MMRDR: Multi-Modal Retinal Diabetic Retinopathy Dataset (24,460 images, `cc-by`)
- [oct_c8](./oct_c8.md): Retinal OCT-C8: 8-Class OCT Classification (24,000 images, `unknown`)
