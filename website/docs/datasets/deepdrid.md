---
id: deepdrid
title: "DeepDRiD: Diabetic Retinopathy Grading and Image Quality Dataset"
sidebar_label: deepdrid
description: "2,000 regular fundus images (500 patients × 2 fields × 2 eyes) plus 256 ultra-widefield fundus images labeled for DR severity (ICDR grades 0-4) and image quality assessment (gradable/ungradable). From"
tags: ["fundus", "uwf_fundus", "cc-by-sa", "zenodo", "grading", "classification", "quality"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# DeepDRiD: Diabetic Retinopathy Grading and Image Quality Dataset

2,000 regular fundus images (500 patients × 2 fields × 2 eyes) plus 256 ultra-widefield fundus images labeled for DR severity (ICDR grades 0-4) and image quality assessment (gradable/ungradable). From the DeepDRiD challenge (MICCAI 2020 / ISBI 2020).

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `deepdrid` |
| **Full name** | DeepDRiD: Diabetic Retinopathy Grading and Image Quality Dataset |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus, uwf_fundus |
| **Tasks** | grading, classification, quality |
| **Samples** | 2,256 |
| **Classes** | 5 (No DR, Mild NPDR, Moderate NPDR, Severe NPDR, Proliferative DR) |
| **Splits** | train, val, test |
| **Size** | 3.0 GB |
| **Source-stated terms** | CC BY-SA 4.0 |
| **Normalized terms** | `cc-by-sa` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Zenodo |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Standard loader included |


## Notes

> Contains both regular fundus (2000 images in dual-field pairs) and ultra-widefield fundus (256 images). Labels CSV includes DR grade (0-4) and quality score.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download deepdrid --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download deepdrid --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('deepdrid')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [zenodo.org/records](https://zenodo.org/records/8248825)

**Source-term evidence:** [zenodo.org/records](https://zenodo.org/records/8248825)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('deepdrid')
samples = ds.load(data_dir, split='test')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{deepdrid,
  title  = { DeepDRiD: Diabetic Retinopathy Grading and Image Quality Dataset },
  note   = { Liu R et al., 'DeepDRiD: Diabetic Retinopathy—Grading and Image Quality Estimation Challenge', Patterns 2022. Zenodo: https://zenodo.org/records/8248825 },
  year   = { 2022 },
  url    = { https://zenodo.org/records/8248825 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Liu R et al., 'DeepDRiD: Diabetic Retinopathy—Grading and Image Quality Estimation Challenge', Patterns 2022. Zenodo: https://zenodo.org/records/8248825
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC BY-SA 4.0
- **Normalized category:** `cc-by-sa`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Standard label without an explicit NC clause; not a permission finding

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Related datasets with shared modalities

- [mmrdr](./mmrdr.md): MMRDR: Multi-Modal Retinal Diabetic Retinopathy Dataset (24,460 records, `cc-by`)
- [fundus_report_dataset](./fundus_report_dataset.md): Fundus Report Dataset (422 records, `cc-by`)
- [airogs](./airogs.md): AIROGS: AI for Robust Glaucoma Screening (113,893 records, `cc-by-nc-nd`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 records, `unknown`)
- [justraigs](./justraigs.md): JustRAIGS: Just Referral AI Glaucoma Screening Dataset (101,442 records, `cc-by-nc-nd`)
- [eyepacs](./eyepacs.md): EyePACS — Diabetic Retinopathy Detection (Kaggle 2015) (88,702 records, `research-only`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (58,036 records, `mit`)
- [angioreport](./angioreport.md): AngioReport Fundus Angiography Report Dataset (55,361 records, `unknown`)
