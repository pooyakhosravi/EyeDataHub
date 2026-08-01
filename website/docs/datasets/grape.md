---
id: grape
title: "GRAPE: Glaucoma Real-world Appraisal Progression Ensemble"
sidebar_label: grape
description: "263 eyes × 1,115 visits. Multi-modal: VF (HFA 24-2), fundus photographs, OCT RNFL, IOP, CCT. Labels: VF progression, OD segmentation, glaucoma stage."
tags: ["multimodal", "fundus", "oct", "visual_field", "tabular", "cc0", "figshare", "regression", "segmentation", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# GRAPE: Glaucoma Real-world Appraisal Progression Ensemble

263 eyes × 1,115 visits. Multi-modal: VF (HFA 24-2), fundus photographs, OCT RNFL, IOP, CCT. Labels: VF progression, OD segmentation, glaucoma stage.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `grape` |
| **Full name** | GRAPE: Glaucoma Real-world Appraisal Progression Ensemble |
| **Primary category** | `multimodal` |
| **Contained modalities** | fundus, oct, visual_field, tabular |
| **Tasks** | regression, segmentation, classification |
| **Samples** | 1,115 |
| **Classes** | 2 (Stable, Progressing) |
| **Splits** | all |
| **Size** | 1.5 GB |
| **Source-stated terms** | CC0 1.0 |
| **Normalized terms** | `cc0` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Figshare |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `end_to_end_tested` |
| **Legacy sample-loader status** | Standard loader included |


## Notes

> Multi-modal: contains fundus images, VF data, OCT measurements, and clinical metadata. Requires manual download from Figshare.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download grape --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download grape --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('grape')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.6084/m9.figshare.c.6406319](https://doi.org/10.6084/m9.figshare.c.6406319)

**Source-term evidence:** [https://doi.org/10.6084/m9.figshare.c.6406319](https://doi.org/10.6084/m9.figshare.c.6406319)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('grape')
samples = ds.load(data_dir, split='all')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{grape,
  title  = { GRAPE: Glaucoma Real-world Appraisal Progression Ensemble },
  note   = { Wen et al., 'GRAPE: A multi-modal dataset for glaucoma progression ',Figshare collection 2022 },
  year   = { 2022 },
  url    = { https://doi.org/10.6084/m9.figshare.c.6406319 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Wen et al., 'GRAPE: A multi-modal dataset for glaucoma progression ',Figshare collection 2022.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC0 1.0
- **Normalized category:** `cc0`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Standard label without an explicit NC clause; not a permission finding

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Related datasets with shared modalities

- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 records, `unknown`)
- [olives](./olives.md): OLIVES: Ophthalmic Labels for Investigating Visual Eye Semantics (9,408 records, `cc-by`)
- [harvard_gdp](./harvard_gdp.md): Harvard GDP: Glaucoma Detection and Progression Dataset (1,000 records, `cc-by-nc-nd`)
- [fairvlmed](./fairvlmed.md): FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset (count not reported records, `unknown`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 records, `unknown`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (58,036 records, `mit`)
- [harvard_fairvision](./harvard_fairvision.md): Harvard-FairVision (AMD + DR + Glaucoma, paired SLO + OCT) (30,000 records, `cc-by-nc-nd`)
- [mmrdr](./mmrdr.md): MMRDR: Multi-Modal Retinal Diabetic Retinopathy Dataset (24,460 records, `cc-by`)
