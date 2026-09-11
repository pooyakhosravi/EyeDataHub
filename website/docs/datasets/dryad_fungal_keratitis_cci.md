---
id: dryad_fungal_keratitis_cci
title: "CCI.net fungal keratitis cases dataset"
sidebar_label: dryad_fungal_keratitis_cci
description: "The 8,697-image fungal-keratitis dataset has explicit classification and segmentation splits and is directly usable for translational corneal imaging."
tags: ["external_eye", "cc0", "dryad", "classification", "segmentation", "resource-role-current-dataset", "dataset-family-dryad-fungal-keratitis-cci"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# CCI.net fungal keratitis cases dataset

The 8,697-image fungal-keratitis dataset has explicit classification and segmentation splits and is directly usable for translational corneal imaging.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `dryad_fungal_keratitis_cci` |
| **Full name** | CCI.net fungal keratitis cases dataset |
| **First published** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Primary category** | `external_eye` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `dryad_fungal_keratitis_cci` |
| **Contained modalities** | external_eye |
| **Tasks** | classification, segmentation |
| **Primary reported quantity** | 8,697 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.258950684 GB |
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
| Primary | 8,697 | `images` | Source-stated primary resource quantity. Current official Dryad metadata. | `official_source_description` | [https://doi.org/10.5061/dryad.8931zcrw5](https://doi.org/10.5061/dryad.8931zcrw5) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Scope: core_add. Named file-level object: CCI_net_dataset.zip plus README. Official Dryad API metadata and current file listing reviewed 2026-08-01.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download dryad_fungal_keratitis_cci --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download dryad_fungal_keratitis_cci --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('dryad_fungal_keratitis_cci')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.5061/dryad.8931zcrw5](https://doi.org/10.5061/dryad.8931zcrw5)

**Source-term evidence:** [https://doi.org/10.5061/dryad.8931zcrw5](https://doi.org/10.5061/dryad.8931zcrw5)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{dryad_fungal_keratitis_cci,
  title  = { CCI.net fungal keratitis cases dataset },
  note   = { CCI.net fungal keratitis cases dataset. Dryad Dataset. doi:10.5061/dryad.8931zcrw5 },
  url    = { https://doi.org/10.5061/dryad.8931zcrw5 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
CCI.net fungal keratitis cases dataset. Dryad Dataset. doi:10.5061/dryad.8931zcrw5.
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

- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [x_pcr](./x_pcr.md): X-PCR Ophthalmology Progressive Clinical Reasoning Benchmark (18,735 rows, `unknown`)
- [popeye_nir](./popeye_nir.md): PopEYE Infrared Ocular Image Dataset (14,976 images, `cc-by`)
- [mcoa](./mcoa.md): MCOA: Multimodal Corneal Opacity Assessment Dataset (6,664 images, `cc-by`)
- [tear_meniscus](./tear_meniscus.md): Multicentre Tear Meniscus Segmentation Dataset (3,432 images, `cc-by`)
- [uveitis_smote](./uveitis_smote.md): Image Dataset on Eye Diseases Classification with Symptoms and SMOTE Validation (3,245 images, `cc-by`)
- [eed_astig](./eed_astig.md): EED-Astig Pediatric External-Eye Dataset (3,088 images, `research-only`)
