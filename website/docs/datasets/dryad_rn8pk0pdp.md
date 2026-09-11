---
id: dryad_rn8pk0pdp
title: "Detection of SARS-CoV-2 in conjunctival secretion and tears in patients with COVID-19 in a tertiary care centre, South India"
sidebar_label: dryad_rn8pk0pdp
description: "Official Dryad deposit of source-described tabular ophthalmic data for the associated study."
tags: ["tabular", "cc0", "dryad", "detection", "resource-role-current-dataset", "dataset-family-dryad-rn8pk0pdp"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Detection of SARS-CoV-2 in conjunctival secretion and tears in patients with COVID-19 in a tertiary care centre, South India

Official Dryad deposit of source-described tabular ophthalmic data for the associated study.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_rn8pk0pdp` |
| **Full name** | Detection of SARS-CoV-2 in conjunctival secretion and tears in patients with COVID-19 in a tertiary care centre, South India |
| **First published** | 2022-10-16 |
| **Publication date precision** | day |
| **Publication date evidence** | [https://doi.org/10.5061/dryad.rn8pk0pdp](https://doi.org/10.5061/dryad.rn8pk0pdp) |
| **Publication date source field** | Published |
| **Publication date reviewed** | 2026-09-11 |
| **Primary category** | `tabular` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `dryad_rn8pk0pdp` |
| **Contained modalities** | tabular |
| **Tasks** | detection |
| **Primary reported quantity** | 80 participants |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.000197569 GB |
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
| Primary | 80 | `participants` | Source-described COVID-19 participants with conjunctival sampling Source-stated scientific quantity; current Dryad file count is separate repository metadata. | `official_source_description` | [https://doi.org/10.5061/dryad.rn8pk0pdp](https://doi.org/10.5061/dryad.rn8pk0pdp) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Scope screen: core_add. Current Dryad v6 file listing: 2 files, 197569 bytes.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_rn8pk0pdp --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dryad_rn8pk0pdp --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_rn8pk0pdp')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.rn8pk0pdp](https://doi.org/10.5061/dryad.rn8pk0pdp)

**Source-term evidence:** [https://doi.org/10.5061/dryad.rn8pk0pdp](https://doi.org/10.5061/dryad.rn8pk0pdp)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_rn8pk0pdp,
  title  = { Detection of SARS-CoV-2 in conjunctival secretion and tears in patients with COVID-19 in a tertiary care centre, South India },
  note   = { Nayak Rajesh, Bhat Sevitha, R Kamath Ajay, Chandak Anshul, Khare Kanishk. Detection of SARS-CoV-2 in conjunctival secretion and tears in patients with COVID-19 in a tertiary care centre, South India. Dryad. 2022. doi:10.5061/dryad.rn8pk0pdp },
  year   = { 2022 },
  url    = { https://doi.org/10.5061/dryad.rn8pk0pdp },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Nayak Rajesh, Bhat Sevitha, R Kamath Ajay, Chandak Anshul, Khare Kanishk. Detection of SARS-CoV-2 in conjunctival secretion and tears in patients with COVID-19 in a tertiary care centre, South India. Dryad. 2022. doi:10.5061/dryad.rn8pk0pdp
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
