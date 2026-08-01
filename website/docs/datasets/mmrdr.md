---
id: mmrdr
title: "MMRDR: Multi-Modal Retinal Diabetic Retinopathy Dataset"
sidebar_label: mmrdr
description: "Multi-modal DR dataset combining color fundus photographs (CFP), OCT B-scans, and ultra-widefield (UWF) fundus images, annotated for DR detection and severity grading. Published in Nature Scientific D"
tags: ["multimodal", "fundus", "oct", "uwf_fundus", "cc-by", "figshare", "grading", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# MMRDR: Multi-Modal Retinal Diabetic Retinopathy Dataset

Multi-modal DR dataset combining color fundus photographs (CFP), OCT B-scans, and ultra-widefield (UWF) fundus images, annotated for DR detection and severity grading. Published in Nature Scientific Data 2026.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mmrdr` |
| **Full name** | MMRDR: Multi-Modal Retinal Diabetic Retinopathy Dataset |
| **Primary category** | `multimodal` |
| **Contained modalities** | fundus, oct, uwf_fundus |
| **Tasks** | grading, classification |
| **Samples** | 24,460 |
| **Classes** | 5 (No DR, Mild DR, Moderate DR, Severe DR, Proliferative DR) |
| **Splits** | train, test |
| **Size** | 18.61 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Figshare |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `end_to_end_tested` |
| **Legacy sample-loader status** | Standard loader included |


## Notes

> Contains 24,460 images across CFP, OCT, and UWF modalities. The source-reported unit is images rather than unique patients. Evaluation code: https://github.com/Vladimirovich2019/MMRDR_Evaluation

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mmrdr --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download mmrdr --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mmrdr')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [https://doi.org/10.6084/m9.figshare.29423747](https://doi.org/10.6084/m9.figshare.29423747)

**Source-term evidence:** [https://doi.org/10.6084/m9.figshare.29423747](https://doi.org/10.6084/m9.figshare.29423747)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('mmrdr')
samples = ds.load(data_dir, split='test')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mmrdr,
  title  = { MMRDR: Multi-Modal Retinal Diabetic Retinopathy Dataset },
  note   = { MMRDR: Multi-Modal Retinal Diabetic Retinopathy Dataset. Nature Scientific Data 2026. Figshare: https://doi.org/10.6084/m9.figshare.29423747 — GitHub: https://github.com/Vladimirovich2019/MMRDR_Evaluation },
  year   = { 2026 },
  url    = { https://doi.org/10.6084/m9.figshare.29423747 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
MMRDR: Multi-Modal Retinal Diabetic Retinopathy Dataset. Nature Scientific Data 2026. Figshare: https://doi.org/10.6084/m9.figshare.29423747 — GitHub: https://github.com/Vladimirovich2019/MMRDR_Evaluation
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

- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 records, `unknown`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (58,036 records, `mit`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 records, `unknown`)
- [harvard_fairvision](./harvard_fairvision.md): Harvard-FairVision (AMD + DR + Glaucoma, paired SLO + OCT) (30,000 records, `cc-by-nc-nd`)
- [x_pcr](./x_pcr.md): X-PCR Ophthalmology Progressive Clinical Reasoning Benchmark (18,700 records, `unknown`)
- [olives](./olives.md): OLIVES: Ophthalmic Labels for Investigating Visual Eye Semantics (9,408 records, `cc-by`)
- [oct_fundus_dme_dr_mexico](./oct_fundus_dme_dr_mexico.md): OCT and Eye Fundus Dataset for DME and DR (2,661 records, `unknown`)
- [deepdrid](./deepdrid.md): DeepDRiD: Diabetic Retinopathy Grading and Image Quality Dataset (2,256 records, `cc-by-sa`)
