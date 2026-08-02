---
id: dryad_gca_optic_nerve_dwi
title: "GCA Optic Nerve Diffusion MRI Dataset"
sidebar_label: dryad_gca_optic_nerve_dwi
description: "Optic-nerve diffusion-MRI assessment data directly support ischemic optic-neuropathy classification."
tags: ["multimodal", "orbital_mri", "tabular", "cc0", "dryad", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# GCA Optic Nerve Diffusion MRI Dataset

Optic-nerve diffusion-MRI assessment data directly support ischemic optic-neuropathy classification.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_gca_optic_nerve_dwi` |
| **Full name** | GCA Optic Nerve Diffusion MRI Dataset |
| **Primary category** | `multimodal` |
| **Contained modalities** | orbital_mri, tabular |
| **Tasks** | classification |
| **Primary reported quantity** | 37 mri scans |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.000753558 GB |
| **Source-stated terms** | https://spdx.org/licenses/CC0-1.0.html |
| **Normalized terms** | `cc0` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Dryad |
| **Availability** | `available` (checked 2026-08-01) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 37 | `mri_scans` | Diffusion-weighted MRI scans in the source-described GCA study Source-stated scientific quantity; deposit file count is recorded separately. | `official_source_description` | [https://doi.org/10.5061/dryad.59zw3r2bk](https://doi.org/10.5061/dryad.59zw3r2bk) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Scope screen: core_add. Current Dryad v4 file listing: 2 files, 695487 bytes.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_gca_optic_nerve_dwi --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dryad_gca_optic_nerve_dwi --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_gca_optic_nerve_dwi')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.59zw3r2bk](https://doi.org/10.5061/dryad.59zw3r2bk)

**Source-term evidence:** [https://doi.org/10.5061/dryad.59zw3r2bk](https://doi.org/10.5061/dryad.59zw3r2bk)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_gca_optic_nerve_dwi,
  title  = { GCA Optic Nerve Diffusion MRI Dataset },
  note   = { Danyel, Leon Alexander. Utility of standard diffusion-weighted magnetic resonance imaging for the identification of ischemic optic neuropathy in giant cell arteritis. Dryad. 2022. doi:10.5061/dryad.59zw3r2bk },
  year   = { 2022 },
  url    = { https://doi.org/10.5061/dryad.59zw3r2bk },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Danyel, Leon Alexander. Utility of standard diffusion-weighted magnetic resonance imaging for the identification of ischemic optic neuropathy in giant cell arteritis. Dryad. 2022. doi:10.5061/dryad.59zw3r2bk
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** https://spdx.org/licenses/CC0-1.0.html
- **Normalized category:** `cc0`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Standard label without an explicit NC clause; not a permission finding

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [tom500](./tom500.md): TOM500: Multi-Organ Annotated Orbital MRI Dataset for Thyroid Eye Disease (500 volumes, `cc0`)
- [ocular_chat_vqa](./ocular_chat_vqa.md): OcularChat-VQA: AREDS-Derived Patient-Physician Dialogue Dataset (844,000 records, `cc-by-nc-sa`)
- [brset_mbrset_embeddings](./brset_mbrset_embeddings.md): Embedding-Based Representations for BRSET and mBRSET (53,188 embedding vectors, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [oculoscope](./oculoscope.md): OculoScope: Fairer AI in Ophthalmology Dataset (16,530 images, `cc-by`)
- [dryad_r7s04](./dryad_r7s04.md): Data from: Prevalence of depression, anxiety, adjustment disorders, and somatoform disorders in patients with age-related macular degeneration in Germany (15,160 participants, `cc0`)
- [fairvlmed](./fairvlmed.md): FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset (10,000 images, `cc-by-nc-nd`)
- [leops_erg](./leops_erg.md): LEOPs Light-Adapted Electroretinogram and Oscillatory Potentials Dataset (9,743 signals, `cc-by`)
