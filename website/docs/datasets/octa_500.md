---
id: octa_500
title: "OCTA-500: Large-scale OCTA Multi-task Benchmark"
sidebar_label: octa_500
description: "500 subjects with OCTA volumes, vessel segmentation, FAZ (foveal avascular zone) annotations, and layer segmentation. Largest public OCTA dataset."
tags: ["octa", "research-only", "manual", "segmentation", "classification", "resource-role-current-dataset", "dataset-family-octa-500", "documented-relationship", "relationship-derived_from"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# OCTA-500: Large-scale OCTA Multi-task Benchmark

500 subjects with OCTA volumes, vessel segmentation, FAZ (foveal avascular zone) annotations, and layer segmentation. Largest public OCTA dataset.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `octa_500` |
| **Full name** | OCTA-500: Large-scale OCTA Multi-task Benchmark |
| **Primary category** | `octa` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `octa_500` |
| **Contained modalities** | octa |
| **Tasks** | segmentation, classification |
| **Primary reported quantity** | 500 participants |
| **Classes** | 4 (Not reported) |
| **Splits** | train, val, test |
| **Size** | 70.0 GB |
| **Source-stated terms** | IEEE DataPort Open Access (research only) |
| **Normalized terms** | `research-only` |
| **Descriptive screening label** | Research or challenge restriction recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `author_contact` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `manual_access_blocked` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 500 | `participants` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [ieee-dataport.org/open-access](https://ieee-dataport.org/open-access/octa-500) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> IEEE login + password-protected zip — email chen2qiang@njust.edu.cn for the unlock password.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- [mm_retinal_reason](./mm_retinal_reason.md) is `derived from` this record: The version-pinned official dataset card lists this record among the CFP or OCT sources used to construct MM-Retinal-Reason. ([evidence](https://huggingface.co/datasets/lxirich/MM-Retinal-Reason/tree/d6243baa82c0914dba3c6f43ca79fdbf856982ef))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# This route requires upstream human action; no transfer starts.
eyehub download octa_500 --data-dir ./data --dry-run --json
# Follow the official instructions shown by preflight.
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('octa_500')
print(preflight_dataset(ds, './data'))  # returns manual_access_blocked
```

  </TabItem>
</Tabs>

**Upstream page:** [ieee-dataport.org/open-access](https://ieee-dataport.org/open-access/octa-500)

**Source-term evidence:** [ieee-dataport.org/open-access](https://ieee-dataport.org/open-access/octa-500)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{octa_500,
  title  = { OCTA-500: Large-scale OCTA Multi-task Benchmark },
  note   = { Li et al., 'OCTA-500: A retinal dataset for optical coherence tomography angiography study', Medical Image Analysis 2024 },
  year   = { 2024 },
  url    = { https://ieee-dataport.org/open-access/octa-500 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Li et al., 'OCTA-500: A retinal dataset for optical coherence tomography angiography study', Medical Image Analysis 2024.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** IEEE DataPort Open Access (research only)
- **Normalized category:** `research-only`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Research or challenge restriction recorded; check source

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [octa_macula_coronal](./octa_macula_coronal.md): OCTA Macula Coronal Views (82,560 images, `cc-by`)
- [aroma_octa](./aroma_octa.md): AROMA Retinal OCTA Artifact Dataset (281 images, `cc-by`)
- [rose](./rose.md): ROSE: Retinal OCT-Angiography Vessel Segmentation (229 images, `cc-by`)
- [soul_octa](./soul_octa.md): SOUL: OCTA Human-Machine Collaborative Annotation Dataset (178 longitudinal samples, `cc-by`)
- [drac22](./drac22.md): DRAC 2022: Diabetic Retinopathy Analysis Challenge (174 images, `cc-by`)
- [ut_fsocta](./ut_fsocta.md): UTHealth Fundus and Synthetic OCTA Dataset (112 participants, `unknown`)
- [dryad_preeclampsia_ocular_octa](./dryad_preeclampsia_ocular_octa.md): Plane wave ultrasound and OCT angiography of the eye in preeclampsia (Not reported, `cc0`)
- [mendeley_imaging_retinal_choroidal_vasculature_using_spatio](./mendeley_imaging_retinal_choroidal_vasculature_using_spatio.md): Imaging the retinal and choroidal vasculature using Spatio-Temporal Optical Coherence Tomography (STOC-T) (Not reported, `cc-by`)
