---
id: e_ophtha
title: "E-ophtha (EX + MA): Exudate and Microaneurysm Segmentation"
sidebar_label: e_ophtha
description: "463 color fundus images with pixel-level segmentation: 82 with exudate (EX) + 381 with microaneurysm (MA) annotations. Standard DR lesion-segmentation benchmark."
tags: ["fundus", "research-only", "kaggle", "segmentation"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# E-ophtha (EX + MA): Exudate and Microaneurysm Segmentation

463 color fundus images with pixel-level segmentation: 82 with exudate (EX) + 381 with microaneurysm (MA) annotations. Standard DR lesion-segmentation benchmark.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `e_ophtha` |
| **Full name** | E-ophtha (EX + MA): Exudate and Microaneurysm Segmentation |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | segmentation |
| **Samples** | 463 |
| **Classes** | 2 (Not reported) |
| **Splits** | all |
| **Size** | 1.0 GB |
| **Source-stated terms** | Research only (TeleOphta project; Kaggle mirror) |
| **Normalized terms** | `research-only` |
| **Descriptive screening label** | Research or challenge restriction recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `controlled_or_manual` |
| **Route backend** | Kaggle |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `manual_access_blocked` |
| **Legacy sample-loader status** | Metadata and access only |


## Notes

> Official source (ADCIS) requires a request form. EyeDataHub uses the Kaggle community mirror. Verify license terms with the original ADCIS distribution before commercial use.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# This route requires upstream human action; no transfer starts.
eyehub download e_ophtha --data-dir ./data --dry-run --json
# Follow the official instructions shown by preflight.
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('e_ophtha')
print(preflight_dataset(ds, './data'))  # returns manual_access_blocked
```

  </TabItem>
</Tabs>

**Upstream page:** [kaggle.com/datasets](https://www.kaggle.com/datasets/samriddhibagchi/e-ophtha-diabetic-retinopathy-datasets-ex-ma)

**Source-term evidence:** [kaggle.com/datasets](https://www.kaggle.com/datasets/samriddhibagchi/e-ophtha-diabetic-retinopathy-datasets-ex-ma)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{e_ophtha,
  title  = { E-ophtha (EX + MA): Exudate and Microaneurysm Segmentation },
  note   = { Decencière et al., 'TeleOphta: Machine Learning and Image Processing Methods for Teleophthalmology', IRBM 2013 },
  year   = { 2013 },
  url    = { https://www.kaggle.com/datasets/samriddhibagchi/e-ophtha-diabetic-retinopathy-datasets-ex-ma },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Decencière et al., 'TeleOphta: Machine Learning and Image Processing Methods for Teleophthalmology', IRBM 2013.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Research only (TeleOphta project; Kaggle mirror)
- **Normalized category:** `research-only`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Research or challenge restriction recorded; check source

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Related datasets with shared modalities

- [airogs](./airogs.md): AIROGS: AI for Robust Glaucoma Screening (113,893 records, `cc-by-nc-nd`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 records, `unknown`)
- [justraigs](./justraigs.md): JustRAIGS: Just Referral AI Glaucoma Screening Dataset (101,442 records, `cc-by-nc-nd`)
- [eyepacs](./eyepacs.md): EyePACS — Diabetic Retinopathy Detection (Kaggle 2015) (88,702 records, `research-only`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (58,036 records, `mit`)
- [angioreport](./angioreport.md): AngioReport Fundus Angiography Report Dataset (55,361 records, `unknown`)
- [ffa_ir](./ffa_ir.md): FFA-IR Medical Report Dataset (47,247 records, `unknown`)
- [bidr](./bidr.md): BiDR: Diabetic Retinopathy Diagnosis Dataset (35,126 records, `unknown`)
