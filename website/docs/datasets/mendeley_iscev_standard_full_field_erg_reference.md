---
id: mendeley_iscev_standard_full_field_erg_reference
title: "ISCEV standard full-field ERG reference limits from 407 healthy subjects, derived from transference and validation of reference data between electrode types and centres"
sidebar_label: mendeley_iscev_standard_full_field_erg_reference
description: "Subject/eye-level full-field erg amplitude and peak-time measurements from Healthy volunteers and clinical-reference subjects at two centres."
tags: ["electrophysiology", "cc-by", "mendeley", "measurement"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# ISCEV standard full-field ERG reference limits from 407 healthy subjects, derived from transference and validation of reference data between electrode types and centres

Subject/eye-level full-field erg amplitude and peak-time measurements from Healthy volunteers and clinical-reference subjects at two centres.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mendeley_iscev_standard_full_field_erg_reference` |
| **Full name** | ISCEV standard full-field ERG reference limits from 407 healthy subjects, derived from transference and validation of reference data between electrode types and centres |
| **Primary category** | `electrophysiology` |
| **Contained modalities** | electrophysiology |
| **Tasks** | measurement |
| **Primary reported quantity** | 407 participants |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | Creative Commons Attribution 4.0 International |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `unknown` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Mendeley Data |
| **Availability** | `available` (checked 2026-08-02) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 407 | `participants` | Source-stated quantity Preserved from the source-confirmation record. | `official_source_description` | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/kcptb9jrf5) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Human provenance: Healthy volunteers and clinical-reference subjects at two centres. Source-review finding: Source description states ISCEV-standard full-field ERG component amplitude and peak-time data recorded/extracted at two centres.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mendeley_iscev_standard_full_field_erg_reference --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download mendeley_iscev_standard_full_field_erg_reference --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mendeley_iscev_standard_full_field_erg_reference')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/kcptb9jrf5/1)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/kcptb9jrf5)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mendeley_iscev_standard_full_field_erg_reference,
  title  = { ISCEV standard full-field ERG reference limits from 407 healthy subjects, derived from transference and validation of reference data between electrode types and centres },
  note   = { ISCEV standard full-field ERG reference limits from 407 healthy subjects, derived from transference and validation of reference data between electrode types and centres. Mendeley Data, V1. doi:10.17632/kcptb9jrf5.1 },
  url    = { https://data.mendeley.com/datasets/kcptb9jrf5/1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
ISCEV standard full-field ERG reference limits from 407 healthy subjects, derived from transference and validation of reference data between electrode types and centres. Mendeley Data, V1. doi:10.17632/kcptb9jrf5.1.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Creative Commons Attribution 4.0 International
- **Normalized category:** `cc-by`
- **Apparent scope:** `unknown`
- **Descriptive screening label:** Standard label without an explicit NC clause; not a permission finding

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [leops_erg](./leops_erg.md): LEOPs Light-Adapted Electroretinogram and Oscillatory Potentials Dataset (9,743 signals, `cc-by`)
- [perg_ioba](./perg_ioba.md): PERG-IOBA Ocular Electrophysiology Dataset (1,354 signals, `odc-by`)
- [dryad_brvo_bevacizumab_multimodal](./dryad_brvo_bevacizumab_multimodal.md): BRVO Bevacizumab Multimodal Dataset (27 eyes, `cc0`)
- [hesc_rpe_electrical_excitability](./hesc_rpe_electrical_excitability.md): hESC-Derived RPE Electrical Excitability Dataset (Not reported, `cc-by`)
- [mendeley_fferg_reference_healthy_controls_university_eye](./mendeley_fferg_reference_healthy_controls_university_eye.md): ffERG Reference Data from Healthy Controls (University Eye Hospital Tuebingen) (Not reported, `cc-by`)
