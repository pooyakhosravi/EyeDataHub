---
id: uveitis_smote
title: "Image Dataset on Eye Diseases Classification with Symptoms and SMOTE Validation"
sidebar_label: uveitis_smote
description: "Image and symptom dataset for normal, uveitis, conjunctivitis, cataract, and eyelid-drooping classification, with source-reported SMOTE balancing to 649 images per class."
tags: ["multimodal", "external_eye", "tabular", "cc-by", "mendeley", "classification", "text_generation"]
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
| **Primary category** | `multimodal` |
| **Contained modalities** | external_eye, tabular |
| **Tasks** | classification, text_generation |
| **Samples** | 3,245 |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.5 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Mendeley Data |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Notes

> Web-sourced images and SMOTE-based synthetic balancing are reported. Use original images, not synthetic oversampling, for clinical validation where possible.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download uveitis_smote --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download uveitis_smote --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('uveitis_smote')
print(preflight_dataset(ds, './data'))  # no transfer
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

## Related datasets with shared modalities

- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 records, `unknown`)
- [eed_astig](./eed_astig.md): EED-Astig Pediatric External-Eye Dataset (3,088 records, `research-only`)
- [ocular_chat_vqa](./ocular_chat_vqa.md): OcularChat-VQA: AREDS-Derived Patient-Physician Dialogue Dataset (844,000 records, `cc-by-nc-sa`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 records, `unknown`)
- [x_pcr](./x_pcr.md): X-PCR Ophthalmology Progressive Clinical Reasoning Benchmark (18,735 records, `unknown`)
- [oculoscope](./oculoscope.md): OculoScope: Fairer AI in Ophthalmology Dataset (16,530 records, `cc-by`)
- [popeye_nir](./popeye_nir.md): PopEYE Infrared Ocular Image Dataset (14,976 records, `cc-by`)
- [fairvlmed](./fairvlmed.md): FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset (10,000 records, `cc-by-nc-nd`)
