---
id: uveitis_smote
title: "Image Dataset on Eye Diseases Classification with Symptoms and SMOTE Validation"
sidebar_label: uveitis_smote
description: "Image and symptom dataset for normal, uveitis, conjunctivitis, cataract, and eyelid-drooping classification, with source-reported SMOTE balancing to 649 images per class."
tags: ["multimodal", "external_eye", "tabular", "cc-by", "mendeley", "classification", "text_generation", "resource-role-current-dataset", "dataset-family-uveitis-smote"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Image Dataset on Eye Diseases Classification with Symptoms and SMOTE Validation

Image and symptom dataset for normal, uveitis, conjunctivitis, cataract, and eyelid-drooping classification, with source-reported SMOTE balancing to 649 images per class.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `uveitis_smote` |
| **Full name** | Image Dataset on Eye Diseases Classification with Symptoms and SMOTE Validation |
| **Publication date** | 2024-11-28 |
| **Date basis** | Initial dataset release |
| **Publication date precision** | day |
| **Publication date evidence** | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/n9zp473wfw/1) |
| **Publication date source field** | citation_publication_date (version 1) |
| **Publication date reviewed** | 2026-09-11 |
| **Date notes** | - |
| **Primary category** | `multimodal` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `uveitis_smote` |
| **Contained modalities** | external_eye, tabular |
| **Tasks** | classification, text_generation |
| **Primary reported quantity** | 3,245 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.5 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Mendeley Data |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 3,245 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/n9zp473wfw/2) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Web-sourced images and SMOTE-based synthetic balancing are reported. Use original images, not synthetic oversampling, for clinical validation where possible.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download uveitis_smote --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download uveitis_smote --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('uveitis_smote')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/n9zp473wfw/2)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/n9zp473wfw/2)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{uveitis_smote,
  title  = { Image Dataset on Eye Diseases Classification with Symptoms and SMOTE Validation },
  note   = { Bitto AK, Ahmed M. Image Dataset on Eye Diseases Classification (Uveitis, Conjunctivitis, Cataract, Eyelid) with Symptoms and SMOTE Validation. Mendeley Data, V2, 2024. doi:10.17632/n9zp473wfw.2 },
  year   = { 2024 },
  url    = { https://data.mendeley.com/datasets/n9zp473wfw/2 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Bitto AK, Ahmed M. Image Dataset on Eye Diseases Classification (Uveitis, Conjunctivitis, Cataract, Eyelid) with Symptoms and SMOTE Validation. Mendeley Data, V2, 2024. doi:10.17632/n9zp473wfw.2
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

- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [eed_astig](./eed_astig.md): EED-Astig Pediatric External-Eye Dataset (3,088 images, `research-only`)
- [dryad_sbcc2fr6n](./dryad_sbcc2fr6n.md): Exploring phenotypic diversity of pigmented traits and iris features in Pakistani population (514 participants, `cc0`)
- [dryad_iris_surface_features](./dryad_iris_surface_features.md): Iris Surface Features Dataset (Not reported, `cc0`)
- [mendeley_application_machine_learning_detecting_iron_deficiency](./mendeley_application_machine_learning_detecting_iron_deficiency.md): Application of Machine Learning in Detecting Iron Deficiency Anemia Using  Conjunctiva image Dataset from Ghana (Not reported, `cc-by`)
- [mendeley_conjunctival_melanoma_detection_using_deep_learning](./mendeley_conjunctival_melanoma_detection_using_deep_learning.md): Conjunctival melanoma detection using deep learning in smartphone images (Not reported, `cc-by-nc`)
- [mendeley_cp_anemic_conjunctival_pallor_ghana](./mendeley_cp_anemic_conjunctival_pallor_ghana.md): CP-AnemiC (A Conjunctival Pallor) Dataset from Ghana (Not reported, `cc-by`)
- [mendeley_nuclear_cataract_database_biomedical_machine_learning](./mendeley_nuclear_cataract_database_biomedical_machine_learning.md): Nuclear Cataract Database for Biomedical and Machine Learning Applications (Not reported, `cc-by`)
