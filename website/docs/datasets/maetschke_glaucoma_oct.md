---
id: maetschke_glaucoma_oct
title: "OCT Volumes for Glaucoma Detection"
sidebar_label: maetschke_glaucoma_oct
description: "A set of 1,110 optic nerve head OCT volumes from 624 patients, including 847 scans with primary open angle glaucoma and 263 healthy scans."
tags: ["oct", "cc-by-nc", "zenodo", "classification", "resource-role-current-dataset", "dataset-family-maetschke-glaucoma-oct"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# OCT Volumes for Glaucoma Detection

A set of 1,110 optic nerve head OCT volumes from 624 patients, including 847 scans with primary open angle glaucoma and 263 healthy scans.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `maetschke_glaucoma_oct` |
| **Full name** | OCT Volumes for Glaucoma Detection |
| **Publication date** | 2018-11-09 |
| **Date basis** | Initial dataset release |
| **Publication date precision** | day |
| **Publication date evidence** | [zenodo.org/api](https://zenodo.org/api/records/1481223) |
| **Publication date source field** | metadata.publication_date (earliest repository version) |
| **Publication date reviewed** | 2026-09-11 |
| **Date notes** | Zenodo versions history lists this as the only version; metadata.publication_date is used. |
| **Primary category** | `oct` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `maetschke_glaucoma_oct` |
| **Contained modalities** | oct |
| **Tasks** | classification |
| **Primary reported quantity** | 1,110 volumes |
| **Classes** | 2 (healthy, primary_open_angle_glaucoma) |
| **Splits** | train, val, test |
| **Size** | 0.43 GB |
| **Source-stated terms** | CC BY-NC 4.0 |
| **Normalized terms** | `cc-by-nc` |
| **Descriptive screening label** | Explicit noncommercial clause recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Zenodo |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 1,110 | `volumes` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [https://doi.org/10.5281/zenodo.1481223](https://doi.org/10.5281/zenodo.1481223) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> The paper reports patient-grouped splits of 888 training, 112 validation, and 110 test scans. Volumes are stored as NumPy arrays.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download maetschke_glaucoma_oct --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download maetschke_glaucoma_oct --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('maetschke_glaucoma_oct')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5281/zenodo.1481223](https://doi.org/10.5281/zenodo.1481223)

**Source-term evidence:** [https://doi.org/10.5281/zenodo.1481223](https://doi.org/10.5281/zenodo.1481223)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{maetschke_glaucoma_oct,
  title  = { OCT Volumes for Glaucoma Detection },
  note   = { Maetschke S, Antony B, Ishikawa H, Wollstein G, Schuman J, Garnavi R. A feature agnostic approach for glaucoma detection in OCT volumes. PLoS One. 2019;14:e0219126. doi:10.1371/journal.pone.0219126. Data: doi:10.5281/zenodo.1481223 },
  year   = { 2019 },
  url    = { https://doi.org/10.5281/zenodo.1481223 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Maetschke S, Antony B, Ishikawa H, Wollstein G, Schuman J, Garnavi R. A feature agnostic approach for glaucoma detection in OCT volumes. PLoS One. 2019;14:e0219126. doi:10.1371/journal.pone.0219126. Data: doi:10.5281/zenodo.1481223
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC BY-NC 4.0
- **Normalized category:** `cc-by-nc`
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
