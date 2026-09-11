---
id: drac22
title: "DRAC 2022: Diabetic Retinopathy Analysis Challenge"
sidebar_label: drac22
description: "174 OCTA images for DR lesion segmentation (IRMA, NPA, NV), image quality assessment, and DR grading (3-class)."
tags: ["octa", "cc-by", "zenodo", "segmentation", "classification", "grading", "resource-role-current-dataset", "dataset-family-drac22"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# DRAC 2022: Diabetic Retinopathy Analysis Challenge

174 OCTA images for DR lesion segmentation (IRMA, NPA, NV), image quality assessment, and DR grading (3-class).

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `drac22` |
| **Full name** | DRAC 2022: Diabetic Retinopathy Analysis Challenge |
| **Publication date** | 2022-07-08 |
| **Date basis** | Initial dataset release |
| **Publication date precision** | day |
| **Publication date evidence** | [drac22.grand-challenge.org/Timeline](https://drac22.grand-challenge.org/Timeline/) |
| **Publication date source field** | official DRAC22 challenge timeline: training sets for Tasks 2 and 3 released |
| **Publication date reviewed** | 2026-09-11 |
| **Date notes** | DRAC22 official timeline records Task 2 and Task 3 training-set release on 2022-07-08, before Task 1 training on 2022-08-02 and testing sets for all tasks on 2022-08-08. Zenodo record 10280359 (metadata publication_date year 2023) is a later archive, not the resource-level initial release. |
| **Primary category** | `octa` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `drac22` |
| **Contained modalities** | octa |
| **Tasks** | segmentation, classification, grading |
| **Primary reported quantity** | 174 images |
| **Classes** | 3 (No DR, Non-proliferative DR, Proliferative DR) |
| **Splits** | train, test |
| **Size** | 0.3 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Zenodo |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Standard loader included |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 174 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [zenodo.org/records](https://zenodo.org/records/10280359) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Available from Grand Challenge after free registration.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download drac22 --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download drac22 --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('drac22')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [zenodo.org/records](https://zenodo.org/records/10280359)

**Source-term evidence:** [zenodo.org/records](https://zenodo.org/records/10280359)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('drac22')
samples = ds.load(data_dir, split='test')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{drac22,
  title  = { DRAC 2022: Diabetic Retinopathy Analysis Challenge },
  note   = { Qin et al., 'DRAC: Diabetic Retinopathy Analysis Challenge with Ultra-Wide Optical Coherence Tomography Angiography Images', Medical Image Analysis 2024 },
  year   = { 2024 },
  url    = { https://zenodo.org/records/10280359 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Qin et al., 'DRAC: Diabetic Retinopathy Analysis Challenge with Ultra-Wide Optical Coherence Tomography Angiography Images', Medical Image Analysis 2024.
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

- [octa_macula_coronal](./octa_macula_coronal.md): OCTA Macula Coronal Views (82,560 images, `cc-by`)
- [octa_500](./octa_500.md): OCTA-500: Large-scale OCTA Multi-task Benchmark (500 participants, `research-only`)
- [aroma_octa](./aroma_octa.md): AROMA Retinal OCTA Artifact Dataset (281 images, `cc-by`)
- [rose](./rose.md): ROSE: Retinal OCT-Angiography Vessel Segmentation (229 images, `cc-by`)
- [soul_octa](./soul_octa.md): SOUL: OCTA Human-Machine Collaborative Annotation Dataset (178 longitudinal samples, `cc-by`)
- [ut_fsocta](./ut_fsocta.md): UTHealth Fundus and Synthetic OCTA Dataset (112 participants, `unknown`)
- [dryad_preeclampsia_ocular_octa](./dryad_preeclampsia_ocular_octa.md): Plane wave ultrasound and OCT angiography of the eye in preeclampsia (Not reported, `cc0`)
- [retinal_oct_octa_two_subjects_processed](./retinal_oct_octa_two_subjects_processed.md): Processed Retinal OCT and OCTA Two-Subject Dataset (Not reported, `cc-by`)
