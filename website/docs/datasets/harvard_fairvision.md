---
id: harvard_fairvision
title: "Harvard-FairVision (AMD + DR + Glaucoma, paired SLO + OCT)"
sidebar_label: harvard_fairvision
description: "30,000 subjects (10K each AMD, DR, glaucoma) with paired SLO fundus and OCT B-scans, demographic attributes (race, ethnicity, gender, language), for fairness analysis."
tags: ["multimodal", "fundus", "oct", "cc-by-nc-nd", "manual", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Harvard-FairVision (AMD + DR + Glaucoma, paired SLO + OCT)

30,000 subjects (10K each AMD, DR, glaucoma) with paired SLO fundus and OCT B-scans, demographic attributes (race, ethnicity, gender, language), for fairness analysis.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `harvard_fairvision` |
| **Full name** | Harvard-FairVision (AMD + DR + Glaucoma, paired SLO + OCT) |
| **Primary category** | `multimodal` |
| **Contained modalities** | fundus, oct |
| **Tasks** | classification |
| **Primary reported quantity** | 30,000 participants |
| **Classes** | 3 (amd, dr, glaucoma) |
| **Splits** | train, val, test |
| **Size** | 600.0 GB |
| **Source-stated terms** | CC BY-NC-ND 4.0 |
| **Normalized terms** | `cc-by-nc-nd` |
| **Descriptive screening label** | Explicit noncommercial clause recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `controlled_or_manual` |
| **Route backend** | Manual (upstream-gated) |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `manual_access_blocked` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 30,000 | `participants` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [ophai.hms.harvard.edu/datasets](https://ophai.hms.harvard.edu/datasets/harvard-fairvision30k) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Application-gated (Harvard form). No automated mirror. Sub-repos: github.com/Harvard-Ophthalmology-AI-Lab/Harvard-&#123;AMD,DR,Glaucoma&#125;.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# This route requires upstream human action; no transfer starts.
eyehub download harvard_fairvision --data-dir ./data --dry-run --json
# Follow the official instructions shown by preflight.
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('harvard_fairvision')
print(preflight_dataset(ds, './data'))  # returns manual_access_blocked
```

  </TabItem>
</Tabs>

**Upstream page:** [ophai.hms.harvard.edu/datasets](https://ophai.hms.harvard.edu/datasets/harvard-fairvision30k)

**Source-term evidence:** [ophai.hms.harvard.edu/datasets](https://ophai.hms.harvard.edu/datasets/harvard-fairvision30k)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{harvard_fairvision,
  title  = { Harvard-FairVision (AMD + DR + Glaucoma, paired SLO + OCT) },
  note   = { Luo et al., 'FairVision: Equitable Deep Learning for Eye Disease Screening via Fair Identity Scaling', arXiv 2310.02492; Harvard Ophthalmology AI Lab 2024. Three disease sub-repos: Harvard-AMD, Harvard-DR, Harvard-Glaucoma. 30,000 subjects total (10K each) },
  year   = { 2024 },
  url    = { https://ophai.hms.harvard.edu/datasets/harvard-fairvision30k },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Luo et al., 'FairVision: Equitable Deep Learning for Eye Disease Screening via Fair Identity Scaling', arXiv 2310.02492; Harvard Ophthalmology AI Lab 2024. Three disease sub-repos: Harvard-AMD, Harvard-DR, Harvard-Glaucoma. 30,000 subjects total (10K each).
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC BY-NC-ND 4.0
- **Normalized category:** `cc-by-nc-nd`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Explicit noncommercial clause recorded; check source

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (103,959 images, `mit`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [mmrdr](./mmrdr.md): MMRDR: Multi-Modal Retinal Diabetic Retinopathy Dataset (24,460 images, `cc-by`)
- [x_pcr](./x_pcr.md): X-PCR Ophthalmology Progressive Clinical Reasoning Benchmark (18,735 rows, `unknown`)
- [olives](./olives.md): OLIVES: Ophthalmic Labels for Investigating Visual Eye Semantics (9,408 b scans, `cc-by`)
- [oct_fundus_dme_dr_mexico](./oct_fundus_dme_dr_mexico.md): OCT and Eye Fundus Dataset for DME and DR (2,661 images, `unknown`)
- [grape](./grape.md): GRAPE: Glaucoma Real-world Appraisal Progression Ensemble (1,115 examinations, `cc0`)
