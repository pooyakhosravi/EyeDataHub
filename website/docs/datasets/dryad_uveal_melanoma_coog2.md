---
id: dryad_uveal_melanoma_coog2
title: "COOG2.1 Uveal Melanoma Prognostic Dataset"
sidebar_label: dryad_uveal_melanoma_coog2
description: "Multicenter uveal-melanoma gene-expression, PRAME, clinical, and metastasis-free-survival data for prognostic modeling."
tags: ["omics", "cc0", "dryad", "classification", "survival_analysis", "prognosis"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# COOG2.1 Uveal Melanoma Prognostic Dataset

Multicenter uveal-melanoma gene-expression, PRAME, clinical, and metastasis-free-survival data for prognostic modeling.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_uveal_melanoma_coog2` |
| **Full name** | COOG2.1 Uveal Melanoma Prognostic Dataset |
| **Primary category** | `omics` |
| **Contained modalities** | omics |
| **Tasks** | classification, survival_analysis, prognosis |
| **Primary reported quantity** | 1,577 participants |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 8.4e-05 GB |
| **Source-stated terms** | CC0 1.0 |
| **Normalized terms** | `cc0` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Dryad |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `end_to_end_tested` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 1,577 | `participants` | Multicenter prognostic cohort | `official_source_description` | [https://doi.org/10.5061/dryad.n8pk0p340](https://doi.org/10.5061/dryad.n8pk0p340) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Contains 1,577 subjects enrolled across 26 centers with a 15-gene expression profile, PRAME status, clinical variables, and follow-up.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_uveal_melanoma_coog2 --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download dryad_uveal_melanoma_coog2 --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_uveal_melanoma_coog2')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.n8pk0p340](https://doi.org/10.5061/dryad.n8pk0p340)

**Source-term evidence:** [https://doi.org/10.5061/dryad.n8pk0p340](https://doi.org/10.5061/dryad.n8pk0p340)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_uveal_melanoma_coog2,
  title  = { COOG2.1 Uveal Melanoma Prognostic Dataset },
  note   = { 15-gene expression profile and PRAME as an integrated prognostic test for uveal melanoma: First report of Collaborative Ocular Oncology Group Study No. 2 (COOG2.1). Dryad. 2025. doi:10.5061/dryad.n8pk0p340 },
  year   = { 2025 },
  url    = { https://doi.org/10.5061/dryad.n8pk0p340 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
15-gene expression profile and PRAME as an integrated prognostic test for uveal melanoma: First report of Collaborative Ocular Oncology Group Study No. 2 (COOG2.1). Dryad. 2025. doi:10.5061/dryad.n8pk0p340
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC0 1.0
- **Normalized category:** `cc0`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Standard label without an explicit NC clause; not a permission finding

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.
