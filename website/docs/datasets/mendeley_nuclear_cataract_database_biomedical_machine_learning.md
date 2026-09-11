---
id: mendeley_nuclear_cataract_database_biomedical_machine_learning
title: "Nuclear Cataract Database for Biomedical and Machine Learning Applications"
sidebar_label: mendeley_nuclear_cataract_database_biomedical_machine_learning
description: "Observation-level source data, annotations, or signals. from Source describes clinical slit-lamp images for nuclear cataract classification."
tags: ["external_eye", "tabular", "cc-by", "mendeley", "classification", "resource-role-current-dataset", "dataset-family-mendeley-nuclear-cataract-database-biomedical-machine-learning"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Nuclear Cataract Database for Biomedical and Machine Learning Applications

Observation-level source data, annotations, or signals. from Source describes clinical slit-lamp images for nuclear cataract classification.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mendeley_nuclear_cataract_database_biomedical_machine_learning` |
| **Full name** | Nuclear Cataract Database for Biomedical and Machine Learning Applications |
| **Publication date** | 2023-03-29 |
| **Date basis** | Initial dataset release |
| **Publication date precision** | day |
| **Publication date evidence** | [data.mendeley.com/datasets](https://data.mendeley.com/datasets/6wv33nbcvv/1) |
| **Publication date source field** | citation_publication_date (version 1) |
| **Publication date reviewed** | 2026-09-11 |
| **Date notes** | - |
| **Primary category** | `external_eye` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `mendeley_nuclear_cataract_database_biomedical_machine_learning` |
| **Contained modalities** | external_eye, tabular |
| **Tasks** | classification |
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

> Human provenance: Source describes clinical slit-lamp images for nuclear cataract classification. Source-review finding: 1,436 listed files: 1,320 JPG, one XLSX, and supporting files.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mendeley_nuclear_cataract_database_biomedical_machine_learning --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download mendeley_nuclear_cataract_database_biomedical_machine_learning --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mendeley_nuclear_cataract_database_biomedical_machine_learning')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/6wv33nbcvv/2)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/6wv33nbcvv)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mendeley_nuclear_cataract_database_biomedical_machine_learning,
  title  = { Nuclear Cataract Database for Biomedical and Machine Learning Applications },
  note   = { Nuclear Cataract Database for Biomedical and Machine Learning Applications. Mendeley Data, V2. doi:10.17632/6wv33nbcvv.2 },
  url    = { https://data.mendeley.com/datasets/6wv33nbcvv/2 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Nuclear Cataract Database for Biomedical and Machine Learning Applications. Mendeley Data, V2. doi:10.17632/6wv33nbcvv.2.
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
- [uveitis_smote](./uveitis_smote.md): Image Dataset on Eye Diseases Classification with Symptoms and SMOTE Validation (3,245 images, `cc-by`)
- [eed_astig](./eed_astig.md): EED-Astig Pediatric External-Eye Dataset (3,088 images, `research-only`)
- [dryad_sbcc2fr6n](./dryad_sbcc2fr6n.md): Exploring phenotypic diversity of pigmented traits and iris features in Pakistani population (514 participants, `cc0`)
- [dryad_iris_surface_features](./dryad_iris_surface_features.md): Iris Surface Features Dataset (Not reported, `cc0`)
- [mendeley_application_machine_learning_detecting_iron_deficiency](./mendeley_application_machine_learning_detecting_iron_deficiency.md): Application of Machine Learning in Detecting Iron Deficiency Anemia Using  Conjunctiva image Dataset from Ghana (Not reported, `cc-by`)
- [mendeley_conjunctival_melanoma_detection_using_deep_learning](./mendeley_conjunctival_melanoma_detection_using_deep_learning.md): Conjunctival melanoma detection using deep learning in smartphone images (Not reported, `cc-by-nc`)
- [mendeley_cp_anemic_conjunctival_pallor_ghana](./mendeley_cp_anemic_conjunctival_pallor_ghana.md): CP-AnemiC (A Conjunctival Pallor) Dataset from Ghana (Not reported, `cc-by`)
