---
id: mendeley_fferg_reference_healthy_controls_university_eye
title: "ffERG Reference Data from Healthy Controls (University Eye Hospital Tuebingen)"
sidebar_label: mendeley_fferg_reference_healthy_controls_university_eye
description: "Observation-level source data, annotations, or signals. from Healthy controls at a university eye hospital are explicitly stated."
tags: ["electrophysiology", "cc-by", "mendeley", "measurement", "resource-role-current-dataset", "dataset-family-mendeley-fferg-reference-healthy-controls-university-eye"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# ffERG Reference Data from Healthy Controls (University Eye Hospital Tuebingen)

Observation-level source data, annotations, or signals. from Healthy controls at a university eye hospital are explicitly stated.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mendeley_fferg_reference_healthy_controls_university_eye` |
| **Full name** | ffERG Reference Data from Healthy Controls (University Eye Hospital Tuebingen) |
| **Primary category** | `electrophysiology` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `mendeley_fferg_reference_healthy_controls_university_eye` |
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
| **Route backend** | Mendeley Data |
| **Availability** | `available` (checked 2026-08-02) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

No reproducible primary item count was exposed for the cataloged source version.

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Human provenance: Healthy controls at a university eye hospital are explicitly stated. Source-review finding: One XLSX workbook of full-field ERG reference data.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mendeley_fferg_reference_healthy_controls_university_eye --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download mendeley_fferg_reference_healthy_controls_university_eye --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mendeley_fferg_reference_healthy_controls_university_eye')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/37wxt2ybvj/1)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/37wxt2ybvj)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mendeley_fferg_reference_healthy_controls_university_eye,
  title  = { ffERG Reference Data from Healthy Controls (University Eye Hospital Tuebingen) },
  note   = { ffERG Reference Data from Healthy Controls (University Eye Hospital Tuebingen). Mendeley Data, V1. doi:10.17632/37wxt2ybvj.1 },
  url    = { https://data.mendeley.com/datasets/37wxt2ybvj/1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
ffERG Reference Data from Healthy Controls (University Eye Hospital Tuebingen). Mendeley Data, V1. doi:10.17632/37wxt2ybvj.1.
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
- [hesc_rpe_electrical_excitability](./hesc_rpe_electrical_excitability.md): hESC-Derived RPE Electrical Excitability Dataset (Not reported, `cc-by`)
