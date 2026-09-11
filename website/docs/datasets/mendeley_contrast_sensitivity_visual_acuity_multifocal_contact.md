---
id: mendeley_contrast_sensitivity_visual_acuity_multifocal_contact
title: "Data for: Contrast sensitivity and visual acuity with multifocal contact lenses with high additions dedicated for myopia progression control"
sidebar_label: mendeley_contrast_sensitivity_visual_acuity_multifocal_contact
description: "Participant/eye-level visual-acuity and contrast-sensitivity measurements from Subjects wearing high-addition multifocal contact lenses for myopia-progression control."
tags: ["tabular", "cc-by", "mendeley", "prediction", "resource-role-current-dataset", "dataset-family-mendeley-contrast-sensitivity-visual-acuity-multifocal-contact"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Data for: Contrast sensitivity and visual acuity with multifocal contact lenses with high additions dedicated for myopia progression control 

Participant/eye-level visual-acuity and contrast-sensitivity measurements from Subjects wearing high-addition multifocal contact lenses for myopia-progression control.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mendeley_contrast_sensitivity_visual_acuity_multifocal_contact` |
| **Full name** | Data for: Contrast sensitivity and visual acuity with multifocal contact lenses with high additions dedicated for myopia progression control  |
| **Publication date** | 2019-12-16 |
| **Date basis** | Initial dataset release |
| **Publication date precision** | day |
| **Publication date evidence** | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/j5cw4wn23y/1) |
| **Publication date source field** | citation_publication_date |
| **Publication date reviewed** | 2026-09-11 |
| **Date notes** | Official Mendeley Data version-1 page Published metadata; JSON-LD datePublished agrees. Version 1 is the initial public deposit. |
| **Primary category** | `tabular` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `mendeley_contrast_sensitivity_visual_acuity_multifocal_contact` |
| **Contained modalities** | tabular |
| **Tasks** | prediction |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | Creative Commons Attribution 4.0 International (Embargo: 2020-09-14) |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `unknown` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Mendeley Data |
| **Availability** | `available` (checked 2026-08-02) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

No reproducible primary item count was exposed for the cataloged source version.

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Human provenance: Subjects wearing high-addition multifocal contact lenses for myopia-progression control. Source-review finding: Source description identifies visual-acuity and contrast-sensitivity data with multifocal contact lenses.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mendeley_contrast_sensitivity_visual_acuity_multifocal_contact --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download mendeley_contrast_sensitivity_visual_acuity_multifocal_contact --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mendeley_contrast_sensitivity_visual_acuity_multifocal_contact')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/j5cw4wn23y/1)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/j5cw4wn23y)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mendeley_contrast_sensitivity_visual_acuity_multifocal_contact,
  title  = { Data for: Contrast sensitivity and visual acuity with multifocal contact lenses with high additions dedicated for myopia progression control  },
  note   = { Data for: Contrast sensitivity and visual acuity with multifocal contact lenses with high additions dedicated for myopia progression control . Mendeley Data, V1. doi:10.17632/j5cw4wn23y.1 },
  url    = { https://data.mendeley.com/datasets/j5cw4wn23y/1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Data for: Contrast sensitivity and visual acuity with multifocal contact lenses with high additions dedicated for myopia progression control . Mendeley Data, V1. doi:10.17632/j5cw4wn23y.1.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Creative Commons Attribution 4.0 International (Embargo: 2020-09-14)
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
