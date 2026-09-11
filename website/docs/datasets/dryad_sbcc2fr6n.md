---
id: dryad_sbcc2fr6n
title: "Exploring phenotypic diversity of pigmented traits and iris features in Pakistani population"
sidebar_label: dryad_sbcc2fr6n
description: "Official Dryad deposit of source-described iris biometric data for the associated study."
tags: ["iris_biometrics", "external_eye", "tabular", "cc0", "dryad", "classification", "resource-role-current-dataset", "dataset-family-dryad-sbcc2fr6n"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Exploring phenotypic diversity of pigmented traits and iris features in Pakistani population

Official Dryad deposit of source-described iris biometric data for the associated study.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_sbcc2fr6n` |
| **Full name** | Exploring phenotypic diversity of pigmented traits and iris features in Pakistani population |
| **First published** | 2021-07-08 |
| **Publication date precision** | day |
| **Publication date evidence** | [https://doi.org/10.5061/dryad.sbcc2fr6n](https://doi.org/10.5061/dryad.sbcc2fr6n) |
| **Publication date source field** | Published |
| **Publication date reviewed** | 2026-09-11 |
| **Primary category** | `iris_biometrics` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `dryad_sbcc2fr6n` |
| **Contained modalities** | iris_biometrics, external_eye, tabular |
| **Tasks** | classification |
| **Primary reported quantity** | 514 participants |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.00656227 GB |
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
| Primary | 514 | `participants` | Source-described Pakistani iris-feature volunteers Source-stated scientific quantity; current Dryad file count is separate repository metadata. | `official_source_description` | [https://doi.org/10.5061/dryad.sbcc2fr6n](https://doi.org/10.5061/dryad.sbcc2fr6n) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Scope screen: core_add. Current Dryad v7 file listing: 2 files, 6562270 bytes.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_sbcc2fr6n --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dryad_sbcc2fr6n --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_sbcc2fr6n')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.sbcc2fr6n](https://doi.org/10.5061/dryad.sbcc2fr6n)

**Source-term evidence:** [https://doi.org/10.5061/dryad.sbcc2fr6n](https://doi.org/10.5061/dryad.sbcc2fr6n)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_sbcc2fr6n,
  title  = { Exploring phenotypic diversity of pigmented traits and iris features in Pakistani population },
  note   = { Bashir Saliha, Shafique Muhammad, Shahzad Muhammad, Anjum Muhammad Sohail, Shahid Ahmad Ali. Exploring phenotypic diversity of pigmented traits and iris features in Pakistani population. Dryad. 2021. doi:10.5061/dryad.sbcc2fr6n },
  year   = { 2021 },
  url    = { https://doi.org/10.5061/dryad.sbcc2fr6n },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Bashir Saliha, Shafique Muhammad, Shahzad Muhammad, Anjum Muhammad Sohail, Shahid Ahmad Ali. Exploring phenotypic diversity of pigmented traits and iris features in Pakistani population. Dryad. 2021. doi:10.5061/dryad.sbcc2fr6n
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

- [dryad_iris_surface_features](./dryad_iris_surface_features.md): Iris Surface Features Dataset (Not reported, `cc0`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [uveitis_smote](./uveitis_smote.md): Image Dataset on Eye Diseases Classification with Symptoms and SMOTE Validation (3,245 images, `cc-by`)
- [eed_astig](./eed_astig.md): EED-Astig Pediatric External-Eye Dataset (3,088 images, `research-only`)
- [mendeley_application_machine_learning_detecting_iron_deficiency](./mendeley_application_machine_learning_detecting_iron_deficiency.md): Application of Machine Learning in Detecting Iron Deficiency Anemia Using  Conjunctiva image Dataset from Ghana (Not reported, `cc-by`)
- [mendeley_conjunctival_melanoma_detection_using_deep_learning](./mendeley_conjunctival_melanoma_detection_using_deep_learning.md): Conjunctival melanoma detection using deep learning in smartphone images (Not reported, `cc-by-nc`)
- [mendeley_cp_anemic_conjunctival_pallor_ghana](./mendeley_cp_anemic_conjunctival_pallor_ghana.md): CP-AnemiC (A Conjunctival Pallor) Dataset from Ghana (Not reported, `cc-by`)
- [mendeley_nuclear_cataract_database_biomedical_machine_learning](./mendeley_nuclear_cataract_database_biomedical_machine_learning.md): Nuclear Cataract Database for Biomedical and Machine Learning Applications (Not reported, `cc-by`)
