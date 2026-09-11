---
id: dryad_ocular_chemical_injuries_shanghai
title: "Clinical characteristics of patients hospitalized for ocular chemical injuries in Shanghai from 2012 to 2017"
sidebar_label: dryad_ocular_chemical_injuries_shanghai
description: "This 160-patient clinical workbook is directly relevant to ocular injury outcomes and ophthalmic epidemiology."
tags: ["tabular", "cc0", "dryad", "prognosis", "resource-role-current-dataset", "dataset-family-dryad-ocular-chemical-injuries-shanghai"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Clinical characteristics of patients hospitalized for ocular chemical injuries in Shanghai from 2012 to 2017

This 160-patient clinical workbook is directly relevant to ocular injury outcomes and ophthalmic epidemiology.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_ocular_chemical_injuries_shanghai` |
| **Full name** | Clinical characteristics of patients hospitalized for ocular chemical injuries in Shanghai from 2012 to 2017 |
| **First published** | 2020-01-09 |
| **Publication date precision** | day |
| **Publication date evidence** | [https://doi.org/10.5061/dryad.9707661](https://doi.org/10.5061/dryad.9707661) |
| **Publication date source field** | Published |
| **Publication date reviewed** | 2026-09-11 |
| **Primary category** | `tabular` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `dryad_ocular_chemical_injuries_shanghai` |
| **Contained modalities** | tabular |
| **Tasks** | prognosis |
| **Primary reported quantity** | 160 participants |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 7.0431e-05 GB |
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
| Primary | 160 | `participants` | Source-stated primary resource quantity. Current official Dryad metadata. | `official_source_description` | [https://doi.org/10.5061/dryad.9707661](https://doi.org/10.5061/dryad.9707661) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Scope: core_add. Named file-level object: Data.xlsx. Official Dryad API metadata and current file listing reviewed 2026-08-01.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_ocular_chemical_injuries_shanghai --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dryad_ocular_chemical_injuries_shanghai --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_ocular_chemical_injuries_shanghai')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.9707661](https://doi.org/10.5061/dryad.9707661)

**Source-term evidence:** [https://doi.org/10.5061/dryad.9707661](https://doi.org/10.5061/dryad.9707661)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_ocular_chemical_injuries_shanghai,
  title  = { Clinical characteristics of patients hospitalized for ocular chemical injuries in Shanghai from 2012 to 2017 },
  note   = { Clinical characteristics of patients hospitalized for ocular chemical injuries in Shanghai from 2012 to 2017. Dryad Dataset. doi:10.5061/dryad.9707661 },
  year   = { 2012 },
  url    = { https://doi.org/10.5061/dryad.9707661 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Clinical characteristics of patients hospitalized for ocular chemical injuries in Shanghai from 2012 to 2017. Dryad Dataset. doi:10.5061/dryad.9707661.
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

- [ocular_chat_vqa](./ocular_chat_vqa.md): OcularChat-VQA: AREDS-Derived Patient-Physician Dialogue Dataset (844,000 records, `cc-by-nc-sa`)
- [brset_mbrset_embeddings](./brset_mbrset_embeddings.md): Embedding-Based Representations for BRSET and mBRSET (53,188 embedding vectors, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [oculoscope](./oculoscope.md): OculoScope: Fairer AI in Ophthalmology Dataset (16,530 images, `cc-by`)
- [dryad_r7s04](./dryad_r7s04.md): Data from: Prevalence of depression, anxiety, adjustment disorders, and somatoform disorders in patients with age-related macular degeneration in Germany (15,160 participants, `cc0`)
- [fairvlmed](./fairvlmed.md): FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset (10,000 images, `cc-by-nc-nd`)
- [leops_erg](./leops_erg.md): LEOPs Light-Adapted Electroretinogram and Oscillatory Potentials Dataset (9,743 signals, `cc-by`)
- [dryad_icmr_eye_see_cataract](./dryad_icmr_eye_see_cataract.md): ICMR EYE SEE Cataract and Sun Exposure Dataset (9,735 participants, `cc0`)
