---
id: hesc_rpe_electrical_excitability
title: "hESC-Derived RPE Electrical Excitability Dataset"
sidebar_label: hesc_rpe_electrical_excitability
description: "Human embryonic-stem-cell-derived RPE electrophysiology data."
tags: ["electrophysiology", "cc-by", "figshare", "measurement", "resource-role-current-dataset", "dataset-family-hesc-rpe-electrical-excitability"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# hESC-Derived RPE Electrical Excitability Dataset

Human embryonic-stem-cell-derived RPE electrophysiology data.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `hesc_rpe_electrical_excitability` |
| **Full name** | hESC-Derived RPE Electrical Excitability Dataset |
| **Primary category** | `electrophysiology` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `hesc_rpe_electrical_excitability` |
| **Contained modalities** | electrophysiology |
| **Tasks** | measurement |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Figshare |
| **Availability** | `available` (checked 2026-08-02) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

No reproducible primary item count was exposed for the cataloged source version.

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download hesc_rpe_electrical_excitability --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download hesc_rpe_electrical_excitability --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('hesc_rpe_electrical_excitability')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.6084/m9.figshare.22246969.v2](https://doi.org/10.6084/m9.figshare.22246969.v2)

**Source-term evidence:** [https://doi.org/10.6084/m9.figshare.22246969.v2](https://doi.org/10.6084/m9.figshare.22246969.v2)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{hesc_rpe_electrical_excitability,
  title  = { hESC-Derived RPE Electrical Excitability Dataset },
  note   = { Repository dataset record. 10.6084/m9.figshare.22246969.v2 },
  url    = { https://doi.org/10.6084/m9.figshare.22246969.v2 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Repository dataset record. 10.6084/m9.figshare.22246969.v2.
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

- [leops_erg](./leops_erg.md): LEOPs Light-Adapted Electroretinogram and Oscillatory Potentials Dataset (9,743 signals, `cc-by`)
- [perg_ioba](./perg_ioba.md): PERG-IOBA Ocular Electrophysiology Dataset (1,354 signals, `odc-by`)
- [mendeley_iscev_standard_full_field_erg_reference](./mendeley_iscev_standard_full_field_erg_reference.md): ISCEV standard full-field ERG reference limits from 407 healthy subjects, derived from transference and validation of reference data between electrode types and centres (407 participants, `cc-by`)
- [dryad_brvo_bevacizumab_multimodal](./dryad_brvo_bevacizumab_multimodal.md): BRVO Bevacizumab Multimodal Dataset (27 eyes, `cc0`)
- [mendeley_fferg_reference_healthy_controls_university_eye](./mendeley_fferg_reference_healthy_controls_university_eye.md): ffERG Reference Data from Healthy Controls (University Eye Hospital Tuebingen) (Not reported, `cc-by`)
