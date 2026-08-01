---
id: slid
title: "SLID: Slit-Lamp Image Dataset"
sidebar_label: slid
description: "~2,617 annotated slit-lamp frames covering anterior-segment anatomy + multi-lesion detection (cataract, corneal disease, conjunctivitis)."
tags: ["multimodal", "external_eye", "unknown", "direct", "segmentation", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# SLID: Slit-Lamp Image Dataset

~2,617 annotated slit-lamp frames covering anterior-segment anatomy + multi-lesion detection (cataract, corneal disease, conjunctivitis).

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `slid` |
| **Full name** | SLID: Slit-Lamp Image Dataset |
| **Primary category** | `multimodal` |
| **Contained modalities** | external_eye |
| **Tasks** | segmentation, classification |
| **Primary reported quantity** | 2,617 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 1.0 GB |
| **Source-stated terms** | See repo (no LICENSE file as of 2026-06; assume research-only) |
| **Normalized terms** | `unknown` |
| **Descriptive screening label** | Unknown or unclear; do not assume permission |
| **Terms scope** | `unknown` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Direct HTTP |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `end_to_end_tested` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 2,617 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [github.com/xumingyu-hub](https://github.com/xumingyu-hub/SLID) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Modality EyeDataHub otherwise lacks (slit-lamp anterior-segment). Annotations CSV is at github.com/xumingyu-hub/SLID/raw/main/Annotations.csv.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download slid --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download slid --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('slid')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [github.com/xumingyu-hub](https://github.com/xumingyu-hub/SLID)

**Source-term evidence:** [github.com/xumingyu-hub](https://github.com/xumingyu-hub/SLID)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{slid,
  title  = { SLID: Slit-Lamp Image Dataset },
  note   = { Xu et al., 'SLID: Slit-Lamp Image Dataset', Frontiers Digital Health 2025. doi:10.3389/fdgth.2025.1716501 },
  year   = { 2025 },
  url    = { https://github.com/xumingyu-hub/SLID },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Xu et al., 'SLID: Slit-Lamp Image Dataset', Frontiers Digital Health 2025. doi:10.3389/fdgth.2025.1716501
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** See repo (no LICENSE file as of 2026-06; assume research-only)
- **Normalized category:** `unknown`
- **Apparent scope:** `unknown`
- **Descriptive screening label:** Unknown or unclear; do not assume permission

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
