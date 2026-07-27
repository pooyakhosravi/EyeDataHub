---
id: dryad_gcc_glaucoma
title: "Glaucoma Ganglion Cell Complex Clinical Dataset"
sidebar_label: dryad_gcc_glaucoma
description: "Eye-level demographics, clinical measurements, and SD-OCT-derived macular ganglion-cell-complex thickness for glaucoma assessment."
tags: ["tabular", "cc0", "dryad", "classification", "regression"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Glaucoma Ganglion Cell Complex Clinical Dataset

Eye-level demographics, clinical measurements, and SD-OCT-derived macular ganglion-cell-complex thickness for glaucoma assessment.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_gcc_glaucoma` |
| **Full name** | Glaucoma Ganglion Cell Complex Clinical Dataset |
| **Primary category** | `tabular` |
| **Contained modalities** | tabular |
| **Tasks** | classification, regression |
| **Samples** | 406 |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 1.3e-05 GB |
| **Source-stated terms** | CC0 1.0 |
| **Normalized terms** | `cc0` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Dryad |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `transfer_tested_partial` |
| **Legacy sample-loader status** | Metadata and access only |


## Notes

> Contains 406 eye-level rows from 203 participants (POAG, glaucoma suspect, and control). Both eyes can occur, so analyses must account for within-participant correlation.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_gcc_glaucoma --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download dryad_gcc_glaucoma --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_gcc_glaucoma')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.xwdbrv1tn](https://doi.org/10.5061/dryad.xwdbrv1tn)

**Source-term evidence:** [https://doi.org/10.5061/dryad.xwdbrv1tn](https://doi.org/10.5061/dryad.xwdbrv1tn)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_gcc_glaucoma,
  title  = { Glaucoma Ganglion Cell Complex Clinical Dataset },
  note   = { Poudel A, Gautam Adhikari P, Ghimire B, Thapa M. Diagnostic capability of ganglion cell complex thickness via spectral domain optical coherence tomography in glaucoma. Dryad. 2026. doi:10.5061/dryad.xwdbrv1tn },
  year   = { 2026 },
  url    = { https://doi.org/10.5061/dryad.xwdbrv1tn },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Poudel A, Gautam Adhikari P, Ghimire B, Thapa M. Diagnostic capability of ganglion cell complex thickness via spectral domain optical coherence tomography in glaucoma. Dryad. 2026. doi:10.5061/dryad.xwdbrv1tn
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC0 1.0
- **Normalized category:** `cc0`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Standard label without an explicit NC clause; not a permission finding

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Related datasets with shared modalities

- [ocular_chat_vqa](./ocular_chat_vqa.md): OcularChat-VQA: AREDS-Derived Patient-Physician Dialogue Dataset (844,000 records, `cc-by-nc-sa`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 records, `unknown`)
- [oculoscope](./oculoscope.md): OculoScope: Fairer AI in Ophthalmology Dataset (16,530 records, `cc-by`)
- [leops_erg](./leops_erg.md): LEOPs Light-Adapted Electroretinogram and Oscillatory Potentials Dataset (9,743 records, `cc-by`)
- [olives](./olives.md): OLIVES: Ophthalmic Labels for Investigating Visual Eye Semantics (9,408 records, `cc-by`)
- [fprm_retina](./fprm_retina.md): FPRM Multimodal Eye Imaging and Psychological Assessment Dataset (3,361 records, `research-only`)
- [uveitis_smote](./uveitis_smote.md): Image Dataset on Eye Diseases Classification with Symptoms and SMOTE Validation (3,245 records, `cc-by`)
- [eed_astig](./eed_astig.md): EED-Astig Pediatric External-Eye Dataset (3,088 records, `research-only`)
