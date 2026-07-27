---
id: perg_ioba
title: "PERG-IOBA Ocular Electrophysiology Dataset"
sidebar_label: perg_ioba
description: "Transient pattern electroretinogram responses from 304 subjects in 336 records with clinical metadata."
tags: ["electrophysiology", "tabular", "odc-by", "physionet", "classification", "regression"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# PERG-IOBA Ocular Electrophysiology Dataset

Transient pattern electroretinogram responses from 304 subjects in 336 records with clinical metadata.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `perg_ioba` |
| **Full name** | PERG-IOBA Ocular Electrophysiology Dataset |
| **Primary category** | `electrophysiology` |
| **Contained modalities** | electrophysiology, tabular |
| **Tasks** | classification, regression |
| **Samples** | 1,354 |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.1 GB |
| **Source-stated terms** | ODC-BY 1.0 (Open Data Commons Attribution) |
| **Normalized terms** | `odc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | PhysioNet |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `transfer_tested_partial` |
| **Legacy sample-loader status** | Metadata and access only |


## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download perg_ioba --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download perg_ioba --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('perg_ioba')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [physionet.org/content](https://physionet.org/content/perg-ioba-dataset/1.0.0/)

**Source-term evidence:** [physionet.org/content](https://physionet.org/content/perg-ioba-dataset/1.0.0/)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{perg_ioba,
  title  = { PERG-IOBA Ocular Electrophysiology Dataset },
  note   = { The PERG-IOBA Dataset. PhysioNet, 2024. doi:10.13026/d24m-w054 },
  year   = { 2024 },
  url    = { https://physionet.org/content/perg-ioba-dataset/1.0.0/ },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
The PERG-IOBA Dataset. PhysioNet, 2024. doi:10.13026/d24m-w054
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** ODC-BY 1.0 (Open Data Commons Attribution)
- **Normalized category:** `odc-by`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Standard label without an explicit NC clause; not a permission finding

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Related datasets with shared modalities

- [leops_erg](./leops_erg.md): LEOPs Light-Adapted Electroretinogram and Oscillatory Potentials Dataset (9,743 records, `cc-by`)
- [ocular_chat_vqa](./ocular_chat_vqa.md): OcularChat-VQA: AREDS-Derived Patient-Physician Dialogue Dataset (844,000 records, `cc-by-nc-sa`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 records, `unknown`)
- [oculoscope](./oculoscope.md): OculoScope: Fairer AI in Ophthalmology Dataset (16,530 records, `cc-by`)
- [olives](./olives.md): OLIVES: Ophthalmic Labels for Investigating Visual Eye Semantics (9,408 records, `cc-by`)
- [fprm_retina](./fprm_retina.md): FPRM Multimodal Eye Imaging and Psychological Assessment Dataset (3,361 records, `research-only`)
- [uveitis_smote](./uveitis_smote.md): Image Dataset on Eye Diseases Classification with Symptoms and SMOTE Validation (3,245 records, `cc-by`)
- [eed_astig](./eed_astig.md): EED-Astig Pediatric External-Eye Dataset (3,088 records, `research-only`)
