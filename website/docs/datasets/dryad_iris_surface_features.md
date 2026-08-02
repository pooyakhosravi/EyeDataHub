---
id: dryad_iris_surface_features
title: "Iris Surface Features Dataset"
sidebar_label: dryad_iris_surface_features
description: "Individual human iris-feature records are directly reusable for iris biometrics and phenotype classification."
tags: ["iris_biometrics", "external_eye", "tabular", "cc0", "dryad", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Iris Surface Features Dataset

Individual human iris-feature records are directly reusable for iris biometrics and phenotype classification.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_iris_surface_features` |
| **Full name** | Iris Surface Features Dataset |
| **Primary category** | `iris_biometrics` |
| **Contained modalities** | iris_biometrics, external_eye, tabular |
| **Tasks** | classification |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.000175121 GB |
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

> Scope screen: core_add. Current Dryad v1 file listing: 1 files, 155993 bytes.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_iris_surface_features --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dryad_iris_surface_features --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_iris_surface_features')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.0kt87](https://doi.org/10.5061/dryad.0kt87)

**Source-term evidence:** [https://doi.org/10.5061/dryad.0kt87](https://doi.org/10.5061/dryad.0kt87)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_iris_surface_features,
  title  = { Iris Surface Features Dataset },
  note   = { Edwards, Melissa, Cha, David, Krithika, S., Johnson, Monique, and Parra, Esteban J.. Data from: Analysis of iris surface features in populations of diverse ancestry. Dryad. 2015. doi:10.5061/dryad.0kt87 },
  year   = { 2015 },
  url    = { https://doi.org/10.5061/dryad.0kt87 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Edwards, Melissa, Cha, David, Krithika, S., Johnson, Monique, and Parra, Esteban J.. Data from: Analysis of iris surface features in populations of diverse ancestry. Dryad. 2015. doi:10.5061/dryad.0kt87
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

- [dryad_sbcc2fr6n](./dryad_sbcc2fr6n.md): Exploring phenotypic diversity of pigmented traits and iris features in Pakistani population (514 participants, `cc0`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [uveitis_smote](./uveitis_smote.md): Image Dataset on Eye Diseases Classification with Symptoms and SMOTE Validation (3,245 images, `cc-by`)
- [eed_astig](./eed_astig.md): EED-Astig Pediatric External-Eye Dataset (3,088 images, `research-only`)
- [ocular_chat_vqa](./ocular_chat_vqa.md): OcularChat-VQA: AREDS-Derived Patient-Physician Dialogue Dataset (844,000 records, `cc-by-nc-sa`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [nd_iris_0405](./nd_iris_0405.md): ND-IRIS-0405 Iris Image Dataset (64,980 images, `research-only`)
- [casia_iris_v4](./casia_iris_v4.md): CASIA-IrisV4 Iris Image Database (54,601 images, `cc0`)
