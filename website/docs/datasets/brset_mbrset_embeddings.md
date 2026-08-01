---
id: brset_mbrset_embeddings
title: "Embedding-Based Representations for BRSET and mBRSET"
sidebar_label: brset_mbrset_embeddings
description: "Precomputed image embeddings for BRSET and mBRSET to support efficient ophthalmic AI research without raw-image redistribution."
tags: ["tabular", "unknown", "physionet", "classification", "retrieval"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Embedding-Based Representations for BRSET and mBRSET

Precomputed image embeddings for BRSET and mBRSET to support efficient ophthalmic AI research without raw-image redistribution.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `brset_mbrset_embeddings` |
| **Full name** | Embedding-Based Representations for BRSET and mBRSET |
| **Primary category** | `tabular` |
| **Contained modalities** | tabular |
| **Tasks** | classification, retrieval |
| **Samples** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | PhysioNet credentialed access terms |
| **Normalized terms** | `unknown` |
| **Descriptive screening label** | Unknown or unclear; do not assume permission |
| **Terms scope** | `unknown` |
| **Access friction** | `controlled_or_manual` |
| **Route backend** | PhysioNet |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `manual_access_blocked` |
| **Legacy sample-loader status** | Metadata and access only |


## Notes

> Derivative representation layer for existing BRSET/mBRSET cohorts.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# This route requires upstream human action; no transfer starts.
eyehub download brset_mbrset_embeddings --data-dir ./data --dry-run --json
# Follow the official instructions shown by preflight.
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('brset_mbrset_embeddings')
print(preflight_dataset(ds, './data'))  # returns manual_access_blocked
```

  </TabItem>
</Tabs>

**Upstream page:** [physionet.org/content](https://physionet.org/content/embedding-brset-mbrset/1.0.0/)

**Source-term evidence:** [physionet.org/content](https://physionet.org/content/embedding-brset-mbrset/1.0.0/)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{brset_mbrset_embeddings,
  title  = { Embedding-Based Representations for BRSET and mBRSET },
  note   = { Embedding-Based Representations for BRSET and mBRSET. PhysioNet, 2026 },
  year   = { 2026 },
  url    = { https://physionet.org/content/embedding-brset-mbrset/1.0.0/ },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Embedding-Based Representations for BRSET and mBRSET. PhysioNet, 2026.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** PhysioNet credentialed access terms
- **Normalized category:** `unknown`
- **Apparent scope:** `unknown`
- **Descriptive screening label:** Unknown or unclear; do not assume permission

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Related datasets with shared modalities

- [ocular_chat_vqa](./ocular_chat_vqa.md): OcularChat-VQA: AREDS-Derived Patient-Physician Dialogue Dataset (844,000 records, `cc-by-nc-sa`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 records, `unknown`)
- [oculoscope](./oculoscope.md): OculoScope: Fairer AI in Ophthalmology Dataset (16,530 records, `cc-by`)
- [fairvlmed](./fairvlmed.md): FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset (10,000 records, `cc-by-nc-nd`)
- [leops_erg](./leops_erg.md): LEOPs Light-Adapted Electroretinogram and Oscillatory Potentials Dataset (9,743 records, `cc-by`)
- [olives](./olives.md): OLIVES: Ophthalmic Labels for Investigating Visual Eye Semantics (9,408 records, `cc-by`)
- [fprm_retina](./fprm_retina.md): FPRM Multimodal Eye Imaging and Psychological Assessment Dataset (3,361 records, `research-only`)
- [uveitis_smote](./uveitis_smote.md): Image Dataset on Eye Diseases Classification with Symptoms and SMOTE Validation (3,245 records, `cc-by`)
