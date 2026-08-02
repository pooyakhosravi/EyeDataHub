---
id: mendeley_radial_peripapillary_capillary_density_as_predictive
title: "Radial peripapillary capillary density as a predictive factor for glaucoma in eyes with ocular hypertension"
sidebar_label: mendeley_radial_peripapillary_capillary_density_as_predictive
description: "Eye-level octa/peripapillary microcirculation measurements from De-identified human research data concerning radial peripapillary microcirculation in ocular hypertension/glaucoma."
tags: ["tabular", "cc-by", "manual", "prediction"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Radial peripapillary capillary density as a predictive factor for glaucoma in eyes with ocular hypertension

Eye-level octa/peripapillary microcirculation measurements from De-identified human research data concerning radial peripapillary microcirculation in ocular hypertension/glaucoma.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mendeley_radial_peripapillary_capillary_density_as_predictive` |
| **Full name** | Radial peripapillary capillary density as a predictive factor for glaucoma in eyes with ocular hypertension |
| **Primary category** | `tabular` |
| **Contained modalities** | tabular |
| **Tasks** | prediction |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | Creative Commons Attribution 4.0 International |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `unknown` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-08-02) |
| **Acquisition support** | `guided_instructions_only` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

No reproducible primary item count was exposed for the cataloged source version.

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Human provenance: De-identified human research data concerning radial peripapillary microcirculation in ocular hypertension/glaucoma. Source-review finding: Current listing not independently retrievable; source description calls the deposit de-identified original-research data on radial peripapillary plexus alterations.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mendeley_radial_peripapillary_capillary_density_as_predictive --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download mendeley_radial_peripapillary_capillary_density_as_predictive --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mendeley_radial_peripapillary_capillary_density_as_predictive')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/h9tntd4gkf)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/h9tntd4gkf)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mendeley_radial_peripapillary_capillary_density_as_predictive,
  title  = { Radial peripapillary capillary density as a predictive factor for glaucoma in eyes with ocular hypertension },
  note   = { Radial peripapillary capillary density as a predictive factor for glaucoma in eyes with ocular hypertension. Mendeley Data. doi:10.17632/h9tntd4gkf },
  url    = { https://data.mendeley.com/datasets/h9tntd4gkf },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Radial peripapillary capillary density as a predictive factor for glaucoma in eyes with ocular hypertension. Mendeley Data. doi:10.17632/h9tntd4gkf.
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

- [ocular_chat_vqa](./ocular_chat_vqa.md): OcularChat-VQA: AREDS-Derived Patient-Physician Dialogue Dataset (844,000 records, `cc-by-nc-sa`)
- [brset_mbrset_embeddings](./brset_mbrset_embeddings.md): Embedding-Based Representations for BRSET and mBRSET (53,188 embedding vectors, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [oculoscope](./oculoscope.md): OculoScope: Fairer AI in Ophthalmology Dataset (16,530 images, `cc-by`)
- [dryad_r7s04](./dryad_r7s04.md): Data from: Prevalence of depression, anxiety, adjustment disorders, and somatoform disorders in patients with age-related macular degeneration in Germany (15,160 participants, `cc0`)
- [fairvlmed](./fairvlmed.md): FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset (10,000 images, `cc-by-nc-nd`)
- [leops_erg](./leops_erg.md): LEOPs Light-Adapted Electroretinogram and Oscillatory Potentials Dataset (9,743 signals, `cc-by`)
- [dryad_icmr_eye_see_cataract](./dryad_icmr_eye_see_cataract.md): ICMR EYE SEE Cataract and Sun Exposure Dataset (9,735 participants, `cc0`)
