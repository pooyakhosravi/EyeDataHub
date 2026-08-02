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
| **Primary reported quantity** | 406 eyes |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 1.3e-05 GB |
| **Source-stated terms** | CC0 1.0 |
| **Normalized terms** | `cc0` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Dryad |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `end_to_end_tested` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 406 | `eyes` | Eye-level table rows | `official_source_description` | [https://doi.org/10.5061/dryad.xwdbrv1tn](https://doi.org/10.5061/dryad.xwdbrv1tn) |
| Additional | 203 | `participants` | Participants contributing 406 eye rows | `official_source_description` | [https://doi.org/10.5061/dryad.xwdbrv1tn](https://doi.org/10.5061/dryad.xwdbrv1tn) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Contains 406 eye-level rows from 203 participants (POAG, glaucoma suspect, and control). Both eyes can occur, so analyses must account for within-participant correlation.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_gcc_glaucoma --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dryad_gcc_glaucoma --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_gcc_glaucoma')
print(preflight_dataset(ds, './data'))  # no download
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

## Similar resources by shared modality

- [ocular_chat_vqa](./ocular_chat_vqa.md): OcularChat-VQA: AREDS-Derived Patient-Physician Dialogue Dataset (844,000 records, `cc-by-nc-sa`)
- [brset_mbrset_embeddings](./brset_mbrset_embeddings.md): Embedding-Based Representations for BRSET and mBRSET (53,188 embedding vectors, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [oculoscope](./oculoscope.md): OculoScope: Fairer AI in Ophthalmology Dataset (16,530 images, `cc-by`)
- [dryad_r7s04](./dryad_r7s04.md): Data from: Prevalence of depression, anxiety, adjustment disorders, and somatoform disorders in patients with age-related macular degeneration in Germany (15,160 participants, `cc0`)
- [fairvlmed](./fairvlmed.md): FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset (10,000 images, `cc-by-nc-nd`)
- [leops_erg](./leops_erg.md): LEOPs Light-Adapted Electroretinogram and Oscillatory Potentials Dataset (9,743 signals, `cc-by`)
- [dryad_icmr_eye_see_cataract](./dryad_icmr_eye_see_cataract.md): ICMR EYE SEE Cataract and Sun Exposure Dataset (9,735 participants, `cc0`)
