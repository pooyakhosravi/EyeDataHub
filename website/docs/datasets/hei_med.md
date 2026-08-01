---
id: hei_med
title: "HEI-MED: Hamilton Eye Institute Macular Edema Dataset"
sidebar_label: hei_med
description: "A collection of 169 fundus photographs with expert exudate and bright lesion annotations, clinical metadata, optic nerve locations, vessel estimates, and image quality scores."
tags: ["fundus", "research-only", "github", "segmentation", "classification", "quality"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# HEI-MED: Hamilton Eye Institute Macular Edema Dataset

A collection of 169 fundus photographs with expert exudate and bright lesion annotations, clinical metadata, optic nerve locations, vessel estimates, and image quality scores.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `hei_med` |
| **Full name** | HEI-MED: Hamilton Eye Institute Macular Edema Dataset |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | segmentation, classification, quality |
| **Samples** | 169 |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 0.32 GB |
| **Source-stated terms** | Research only: non-commercial research use |
| **Normalized terms** | `research-only` |
| **Descriptive screening label** | Research or challenge restriction recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | GitHub |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `end_to_end_tested` |
| **Legacy sample-loader status** | Metadata and access only |


## Notes

> The source README permits only non-commercial research use and requires citation. No SPDX license file is present.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download hei_med --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download hei_med --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('hei_med')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [github.com/lgiancaUTH](https://github.com/lgiancaUTH/HEI-MED)

**Source-term evidence:** [github.com/lgiancaUTH](https://github.com/lgiancaUTH/HEI-MED)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{hei_med,
  title  = { HEI-MED: Hamilton Eye Institute Macular Edema Dataset },
  note   = { Giancardo L, Meriaudeau F, Karnowski TP, et al. Exudate-based diabetic macular edema detection in fundus images using publicly available datasets. Med Image Anal. 2012;16:216-226. doi:10.1016/j.media.2011.07.004 },
  year   = { 2012 },
  url    = { https://github.com/lgiancaUTH/HEI-MED },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Giancardo L, Meriaudeau F, Karnowski TP, et al. Exudate-based diabetic macular edema detection in fundus images using publicly available datasets. Med Image Anal. 2012;16:216-226. doi:10.1016/j.media.2011.07.004
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Research only: non-commercial research use
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
