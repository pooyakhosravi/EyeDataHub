---
id: riga
title: "RIGA: Retinal Fundus Images for Glaucoma Analysis"
sidebar_label: riga
description: "750 fundus images with optic disc and optic cup segmentations from 6 ophthalmologists per image. Multi-rater benchmark."
tags: ["fundus", "cc-by-nc", "direct", "segmentation"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# RIGA: Retinal Fundus Images for Glaucoma Analysis

750 fundus images with optic disc and optic cup segmentations from 6 ophthalmologists per image. Multi-rater benchmark.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `riga` |
| **Full name** | RIGA: Retinal Fundus Images for Glaucoma Analysis |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | segmentation |
| **Samples** | 750 |
| **Classes** | 3 (background, optic_disc, optic_cup) |
| **Splits** | all |
| **Size** | 2.0 GB |
| **Source-stated terms** | CC BY-NC 4.0 |
| **Normalized terms** | `cc-by-nc` |
| **Descriptive screening label** | Explicit noncommercial clause recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Direct HTTP |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `guided_instructions_only` |
| **Legacy sample-loader status** | Metadata and access only |


## Notes

> Deep Blue provides BinRushed, Magrabi, and MESSIDOR components. Its current documentation directs users to Globus for the large MESSIDOR component.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download riga --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download riga --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('riga')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [deepblue.lib.umich.edu/data](https://deepblue.lib.umich.edu/data/concern/data_sets/3b591905z)

**Source-term evidence:** [deepblue.lib.umich.edu/data](https://deepblue.lib.umich.edu/data/concern/data_sets/3b591905z)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{riga,
  title  = { RIGA: Retinal Fundus Images for Glaucoma Analysis },
  note   = { Almazroa et al., 'Retinal Fundus Images for Glaucoma Analysis: The RIGA Dataset', J. Medical Imaging 2018 },
  year   = { 2018 },
  url    = { https://deepblue.lib.umich.edu/data/concern/data_sets/3b591905z },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Almazroa et al., 'Retinal Fundus Images for Glaucoma Analysis: The RIGA Dataset', J. Medical Imaging 2018.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC BY-NC 4.0
- **Normalized category:** `cc-by-nc`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Explicit noncommercial clause recorded; check source

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
