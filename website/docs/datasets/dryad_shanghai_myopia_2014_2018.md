---
id: dryad_shanghai_myopia_2014_2018
title: "Age-related change of axial length, spherical equivalent, prevalence of myopia and high myopia in school-age children in Shanghai: 2014 to 2018"
sidebar_label: dryad_shanghai_myopia_2014_2018
description: "The named DATA.xls and README define a human pediatric ocular-biometry cohort even though the deposit does not state one primary total."
tags: ["tabular", "cc0", "dryad", "measurement", "resource-role-current-dataset", "dataset-family-dryad-shanghai-myopia-2014-2018"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Age-related change of axial length, spherical equivalent, prevalence of myopia and high myopia in school-age children in Shanghai: 2014 to 2018

The named DATA.xls and README define a human pediatric ocular-biometry cohort even though the deposit does not state one primary total.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_shanghai_myopia_2014_2018` |
| **Full name** | Age-related change of axial length, spherical equivalent, prevalence of myopia and high myopia in school-age children in Shanghai: 2014 to 2018 |
| **First published** | 2020-11-09 |
| **Publication date precision** | day |
| **Publication date evidence** | [https://doi.org/10.5061/dryad.c2fqz615c](https://doi.org/10.5061/dryad.c2fqz615c) |
| **Publication date source field** | Published |
| **Publication date reviewed** | 2026-09-11 |
| **Primary category** | `tabular` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `dryad_shanghai_myopia_2014_2018` |
| **Contained modalities** | tabular |
| **Tasks** | measurement |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.005062221 GB |
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

No reproducible primary item count was exposed for the cataloged source version.

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Scope: core_add. Named file-level object: DATA.xls plus README.docx. Official Dryad API metadata and current file listing reviewed 2026-08-01.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_shanghai_myopia_2014_2018 --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dryad_shanghai_myopia_2014_2018 --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_shanghai_myopia_2014_2018')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.c2fqz615c](https://doi.org/10.5061/dryad.c2fqz615c)

**Source-term evidence:** [https://doi.org/10.5061/dryad.c2fqz615c](https://doi.org/10.5061/dryad.c2fqz615c)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_shanghai_myopia_2014_2018,
  title  = { Age-related change of axial length, spherical equivalent, prevalence of myopia and high myopia in school-age children in Shanghai: 2014 to 2018 },
  note   = { Age-related change of axial length, spherical equivalent, prevalence of myopia and high myopia in school-age children in Shanghai: 2014 to 2018. Dryad Dataset. doi:10.5061/dryad.c2fqz615c },
  year   = { 2014 },
  url    = { https://doi.org/10.5061/dryad.c2fqz615c },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Age-related change of axial length, spherical equivalent, prevalence of myopia and high myopia in school-age children in Shanghai: 2014 to 2018. Dryad Dataset. doi:10.5061/dryad.c2fqz615c.
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
