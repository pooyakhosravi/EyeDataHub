---
id: olives
title: "OLIVES: Ophthalmic Labels for Investigating Visual Eye Semantics"
sidebar_label: olives
description: "Longitudinal OCT + fundus dataset from AMD/DME patients across multiple clinical visits. 9,408 OCT B-scans have biomarker labels for 8 categories (fluid, drusen, scarring, PED variants, etc.); 78,000+"
tags: ["oct", "fundus", "tabular", "cc-by", "zenodo", "multilabel", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# OLIVES: Ophthalmic Labels for Investigating Visual Eye Semantics

Longitudinal OCT + fundus dataset from AMD/DME patients across multiple clinical visits. 9,408 OCT B-scans have biomarker labels for 8 categories (fluid, drusen, scarring, PED variants, etc.); 78,000+ images include clinical measurements (BCVA, CST). Also includes 1,268 paired fundus photographs.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `olives` |
| **Full name** | OLIVES: Ophthalmic Labels for Investigating Visual Eye Semantics |
| **Primary category** | `oct` |
| **Contained modalities** | oct, fundus, tabular |
| **Tasks** | multilabel, classification |
| **Samples** | 9,408 |
| **Classes** | 8 (Fluid, Hard Exudate, Soft Exudate, Drusen, Scar, Laser Scar, Fibrovascular PED, Serous PED) |
| **Splits** | train, val, test |
| **Size** | 20.0 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Zenodo |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Standard loader included |


## Notes

> 9,408 biomarker-labelled B-scans from 96 patients (6 clinical visits × 49 B-scans/visit). Full OCT volume set ~62,000 B-scans. Also available on HuggingFace: gOLIVES/OLIVES_Dataset. Contains paired fundus photos and clinical metadata.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download olives --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download olives --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('olives')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [zenodo.org/records](https://zenodo.org/records/7105232)

**Source-term evidence:** [zenodo.org/records](https://zenodo.org/records/7105232)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('olives')
samples = ds.load(data_dir, split='test')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{olives,
  title  = { OLIVES: Ophthalmic Labels for Investigating Visual Eye Semantics },
  note   = { Prabhushankar M et al., 'OLIVES Dataset: Ophthalmic Labels for Investigating Visual Eye Semantics', NeurIPS Datasets & Benchmarks 2022. https://zenodo.org/records/7105232 },
  year   = { 2022 },
  url    = { https://zenodo.org/records/7105232 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Prabhushankar M et al., 'OLIVES Dataset: Ophthalmic Labels for Investigating Visual Eye Semantics', NeurIPS Datasets & Benchmarks 2022. https://zenodo.org/records/7105232
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
- [grape](./grape.md): GRAPE: Glaucoma Real-world Appraisal Progression Ensemble (1,115 records, `cc0`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 records, `unknown`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (58,036 records, `mit`)
- [harvard_fairvision](./harvard_fairvision.md): Harvard-FairVision (AMD + DR + Glaucoma, paired SLO + OCT) (30,000 records, `cc-by-nc-nd`)
- [mmrdr](./mmrdr.md): MMRDR: Multi-Modal Retinal Diabetic Retinopathy Dataset (24,460 records, `cc-by`)
- [x_pcr](./x_pcr.md): X-PCR Ophthalmology Progressive Clinical Reasoning Benchmark (18,735 records, `unknown`)
- [fairvlmed](./fairvlmed.md): FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset (10,000 records, `cc-by-nc-nd`)
