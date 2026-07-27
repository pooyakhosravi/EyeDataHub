---
id: gamma
title: "GAMMA — Glaucoma Grading from Multi-Modality Images"
sidebar_label: gamma
description: "300 paired fundus + 3D OCT volumes. Glaucoma grading into Normal / Early / Advanced plus OD/OC segmentation and fovea location."
tags: ["multimodal", "fundus", "oct", "cc-by-nc-nd", "gdrive", "grading", "classification", "segmentation"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# GAMMA — Glaucoma Grading from Multi-Modality Images

300 paired fundus + 3D OCT volumes. Glaucoma grading into Normal / Early / Advanced plus OD/OC segmentation and fovea location.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `gamma` |
| **Full name** | GAMMA — Glaucoma Grading from Multi-Modality Images |
| **Primary category** | `multimodal` |
| **Contained modalities** | fundus, oct |
| **Tasks** | grading, classification, segmentation |
| **Samples** | 300 |
| **Classes** | 3 (Normal, Early, Advanced) |
| **Splits** | train, test |
| **Size** | 5.0 GB |
| **Source-stated terms** | CC BY-NC-ND |
| **Normalized terms** | `cc-by-nc-nd` |
| **Descriptive screening label** | Explicit noncommercial clause recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Google Drive |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `loader_implemented_not_live_tested` |
| **Legacy sample-loader status** | Standard loader included |


## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download gamma --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download gamma --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('gamma')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [drive.google.com/file](https://drive.google.com/file/d/1thJDE1_TR-xa8f3H-0PwPpDxun7rV8Sw/view)

**Source-term evidence:** [drive.google.com/file](https://drive.google.com/file/d/1thJDE1_TR-xa8f3H-0PwPpDxun7rV8Sw/view)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('gamma')
samples = ds.load(data_dir, split='test')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{gamma,
  title  = { GAMMA — Glaucoma Grading from Multi-Modality Images },
  note   = { Wu J. et al., 'GAMMA Challenge: Glaucoma Grading from Multi-Modality Imaging', MIA 2023 },
  year   = { 2023 },
  url    = { https://drive.google.com/file/d/1thJDE1_TR-xa8f3H-0PwPpDxun7rV8Sw/view },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Wu J. et al., 'GAMMA Challenge: Glaucoma Grading from Multi-Modality Imaging', MIA 2023.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC BY-NC-ND
- **Normalized category:** `cc-by-nc-nd`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Explicit noncommercial clause recorded; check source

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Related datasets with shared modalities

- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 records, `unknown`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (58,036 records, `mit`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 records, `unknown`)
- [harvard_fairvision](./harvard_fairvision.md): Harvard-FairVision (AMD + DR + Glaucoma, paired SLO + OCT) (30,000 records, `cc-by-nc-nd`)
- [mmrdr](./mmrdr.md): MMRDR: Multi-Modal Retinal Diabetic Retinopathy Dataset (24,460 records, `cc-by`)
- [x_pcr](./x_pcr.md): X-PCR Ophthalmology Progressive Clinical Reasoning Benchmark (18,700 records, `unknown`)
- [olives](./olives.md): OLIVES: Ophthalmic Labels for Investigating Visual Eye Semantics (9,408 records, `cc-by`)
- [oct_fundus_dme_dr_mexico](./oct_fundus_dme_dr_mexico.md): OCT and Eye Fundus Dataset for DME and DR (2,661 records, `unknown`)
