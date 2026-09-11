---
id: mendeley_application_machine_learning_detecting_iron_deficiency
title: "Application of Machine Learning in Detecting Iron Deficiency Anemia Using  Conjunctiva image Dataset from Ghana"
sidebar_label: mendeley_application_machine_learning_detecting_iron_deficiency
description: "Image-level conjunctival observations with anemia target from Human conjunctiva images from Ghana used for iron-deficiency-anemia detection."
tags: ["external_eye", "tabular", "cc-by", "manual", "classification", "resource-role-current-dataset", "dataset-family-mendeley-application-machine-learning-detecting-iron-deficiency"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Application of Machine Learning in Detecting Iron Deficiency Anemia Using  Conjunctiva image Dataset from Ghana

Image-level conjunctival observations with anemia target from Human conjunctiva images from Ghana used for iron-deficiency-anemia detection.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mendeley_application_machine_learning_detecting_iron_deficiency` |
| **Full name** | Application of Machine Learning in Detecting Iron Deficiency Anemia Using  Conjunctiva image Dataset from Ghana |
| **First published** | 2022-06-27 |
| **Publication date precision** | day |
| **Publication date evidence** | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/nt7r8hv2pz/1) |
| **Publication date source field** | Mendeley dataset version 1 page: Published |
| **Publication date reviewed** | 2026-09-11 |
| **Primary category** | `external_eye` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `mendeley_application_machine_learning_detecting_iron_deficiency` |
| **Contained modalities** | external_eye, tabular |
| **Tasks** | classification |
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

> Human provenance: Human conjunctiva images from Ghana used for iron-deficiency-anemia detection. Source-review finding: Current listing not independently retrievable; source description identifies non-invasive anemia detection from conjunctiva images.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mendeley_application_machine_learning_detecting_iron_deficiency --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download mendeley_application_machine_learning_detecting_iron_deficiency --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mendeley_application_machine_learning_detecting_iron_deficiency')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/nt7r8hv2pz)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/nt7r8hv2pz)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mendeley_application_machine_learning_detecting_iron_deficiency,
  title  = { Application of Machine Learning in Detecting Iron Deficiency Anemia Using  Conjunctiva image Dataset from Ghana },
  note   = { Application of Machine Learning in Detecting Iron Deficiency Anemia Using  Conjunctiva image Dataset from Ghana. Mendeley Data. doi:10.17632/nt7r8hv2pz },
  url    = { https://data.mendeley.com/datasets/nt7r8hv2pz },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Application of Machine Learning in Detecting Iron Deficiency Anemia Using  Conjunctiva image Dataset from Ghana. Mendeley Data. doi:10.17632/nt7r8hv2pz.
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

- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [uveitis_smote](./uveitis_smote.md): Image Dataset on Eye Diseases Classification with Symptoms and SMOTE Validation (3,245 images, `cc-by`)
- [eed_astig](./eed_astig.md): EED-Astig Pediatric External-Eye Dataset (3,088 images, `research-only`)
- [dryad_sbcc2fr6n](./dryad_sbcc2fr6n.md): Exploring phenotypic diversity of pigmented traits and iris features in Pakistani population (514 participants, `cc0`)
- [dryad_iris_surface_features](./dryad_iris_surface_features.md): Iris Surface Features Dataset (Not reported, `cc0`)
- [mendeley_conjunctival_melanoma_detection_using_deep_learning](./mendeley_conjunctival_melanoma_detection_using_deep_learning.md): Conjunctival melanoma detection using deep learning in smartphone images (Not reported, `cc-by-nc`)
- [mendeley_cp_anemic_conjunctival_pallor_ghana](./mendeley_cp_anemic_conjunctival_pallor_ghana.md): CP-AnemiC (A Conjunctival Pallor) Dataset from Ghana (Not reported, `cc-by`)
- [mendeley_nuclear_cataract_database_biomedical_machine_learning](./mendeley_nuclear_cataract_database_biomedical_machine_learning.md): Nuclear Cataract Database for Biomedical and Machine Learning Applications (Not reported, `cc-by`)
