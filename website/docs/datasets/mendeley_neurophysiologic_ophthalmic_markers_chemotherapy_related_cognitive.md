---
id: mendeley_neurophysiologic_ophthalmic_markers_chemotherapy_related_cognitive
title: "Data for: Neurophysiologic and ophthalmic markers of chemotherapy-related cognitive impairment in patients diagnosed with hematologic cancer"
sidebar_label: mendeley_neurophysiologic_ophthalmic_markers_chemotherapy_related_cognitive
description: "Participant-level neurophysiologic and ophthalmic outcome measures from Patients diagnosed with hematologic cancer assessed for chemotherapy-related cognitive impairment."
tags: ["tabular", "cc0", "mendeley", "classification", "resource-role-current-dataset", "dataset-family-mendeley-neurophysiologic-ophthalmic-markers-chemotherapy-related-cognitive"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Data for: Neurophysiologic and ophthalmic markers of chemotherapy-related cognitive impairment in patients diagnosed with hematologic cancer

Participant-level neurophysiologic and ophthalmic outcome measures from Patients diagnosed with hematologic cancer assessed for chemotherapy-related cognitive impairment.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mendeley_neurophysiologic_ophthalmic_markers_chemotherapy_related_cognitive` |
| **Full name** | Data for: Neurophysiologic and ophthalmic markers of chemotherapy-related cognitive impairment in patients diagnosed with hematologic cancer |
| **First published** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Primary category** | `tabular` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `mendeley_neurophysiologic_ophthalmic_markers_chemotherapy_related_cognitive` |
| **Contained modalities** | tabular |
| **Tasks** | classification |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | Public Domain Dedication (Embargo: 2020-07-25) |
| **Normalized terms** | `cc0` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `mixed_components` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Mendeley Data |
| **Availability** | `available` (checked 2026-08-02) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

No reproducible primary item count was exposed for the cataloged source version.

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Human provenance: Patients diagnosed with hematologic cancer assessed for chemotherapy-related cognitive impairment. Source-review finding: Source description states MasterSheet.csv contains all outcome measures and a SAS file contains analysis code.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mendeley_neurophysiologic_ophthalmic_markers_chemotherapy_related_cognitive --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download mendeley_neurophysiologic_ophthalmic_markers_chemotherapy_related_cognitive --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mendeley_neurophysiologic_ophthalmic_markers_chemotherapy_related_cognitive')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/npt7rp69gm/1)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/npt7rp69gm)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mendeley_neurophysiologic_ophthalmic_markers_chemotherapy_related_cognitive,
  title  = { Data for: Neurophysiologic and ophthalmic markers of chemotherapy-related cognitive impairment in patients diagnosed with hematologic cancer },
  note   = { Data for: Neurophysiologic and ophthalmic markers of chemotherapy-related cognitive impairment in patients diagnosed with hematologic cancer. Mendeley Data, V1. doi:10.17632/npt7rp69gm.1 },
  url    = { https://data.mendeley.com/datasets/npt7rp69gm/1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Data for: Neurophysiologic and ophthalmic markers of chemotherapy-related cognitive impairment in patients diagnosed with hematologic cancer. Mendeley Data, V1. doi:10.17632/npt7rp69gm.1.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Public Domain Dedication (Embargo: 2020-07-25)
- **Normalized category:** `cc0`
- **Apparent scope:** `mixed_components`
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
