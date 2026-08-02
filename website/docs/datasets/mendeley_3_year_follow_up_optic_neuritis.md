---
id: mendeley_3_year_follow_up_optic_neuritis
title: "a 3-year follow-up of optic neuritis phenotypes in Chinese cohort"
sidebar_label: mendeley_3_year_follow_up_optic_neuritis
description: "Observation-level human or human-derived measurements/signals. from Chinese new-onset optic-neuritis cohort followed three years."
tags: ["tabular", "cc-by", "mendeley", "measurement"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# a 3-year follow-up of optic neuritis phenotypes in Chinese cohort

Observation-level human or human-derived measurements/signals. from Chinese new-onset optic-neuritis cohort followed three years.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mendeley_3_year_follow_up_optic_neuritis` |
| **Full name** | a 3-year follow-up of optic neuritis phenotypes in Chinese cohort |
| **Primary category** | `tabular` |
| **Contained modalities** | tabular |
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

> Human provenance: Chinese new-onset optic-neuritis cohort followed three years. Source-review finding: Indexed source describes clinical characteristics and OCT follow-up.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mendeley_3_year_follow_up_optic_neuritis --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download mendeley_3_year_follow_up_optic_neuritis --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mendeley_3_year_follow_up_optic_neuritis')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/zvb55v8mzw/1)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/zvb55v8mzw)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mendeley_3_year_follow_up_optic_neuritis,
  title  = { a 3-year follow-up of optic neuritis phenotypes in Chinese cohort },
  note   = { a 3-year follow-up of optic neuritis phenotypes in Chinese cohort. Mendeley Data, V1. doi:10.17632/zvb55v8mzw.1 },
  url    = { https://data.mendeley.com/datasets/zvb55v8mzw/1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
a 3-year follow-up of optic neuritis phenotypes in Chinese cohort. Mendeley Data, V1. doi:10.17632/zvb55v8mzw.1.
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

- [ocular_chat_vqa](./ocular_chat_vqa.md): OcularChat-VQA: AREDS-Derived Patient-Physician Dialogue Dataset (844,000 records, `cc-by-nc-sa`)
- [brset_mbrset_embeddings](./brset_mbrset_embeddings.md): Embedding-Based Representations for BRSET and mBRSET (53,188 embedding vectors, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [oculoscope](./oculoscope.md): OculoScope: Fairer AI in Ophthalmology Dataset (16,530 images, `cc-by`)
- [dryad_r7s04](./dryad_r7s04.md): Data from: Prevalence of depression, anxiety, adjustment disorders, and somatoform disorders in patients with age-related macular degeneration in Germany (15,160 participants, `cc0`)
- [fairvlmed](./fairvlmed.md): FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset (10,000 images, `cc-by-nc-nd`)
- [leops_erg](./leops_erg.md): LEOPs Light-Adapted Electroretinogram and Oscillatory Potentials Dataset (9,743 signals, `cc-by`)
- [dryad_icmr_eye_see_cataract](./dryad_icmr_eye_see_cataract.md): ICMR EYE SEE Cataract and Sun Exposure Dataset (9,735 participants, `cc0`)
