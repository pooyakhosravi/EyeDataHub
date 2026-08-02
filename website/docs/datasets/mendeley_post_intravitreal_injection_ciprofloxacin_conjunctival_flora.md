---
id: mendeley_post_intravitreal_injection_ciprofloxacin_conjunctival_flora
title: "Data for: Post-Intravitreal Injection Ciprofloxacin and Conjunctival Flora Resistance"
sidebar_label: mendeley_post_intravitreal_injection_ciprofloxacin_conjunctival_flora
description: "Observation-level source data, annotations, or signals. from Source describes de-identified conjunctival swab observations from ophthalmic patients."
tags: ["oct", "cc-by-nc", "mendeley", "measurement"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Data for: Post-Intravitreal Injection Ciprofloxacin and Conjunctival Flora Resistance

Observation-level source data, annotations, or signals. from Source describes de-identified conjunctival swab observations from ophthalmic patients.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `mendeley_post_intravitreal_injection_ciprofloxacin_conjunctival_flora` |
| **Full name** | Data for: Post-Intravitreal Injection Ciprofloxacin and Conjunctival Flora Resistance |
| **Primary category** | `oct` |
| **Contained modalities** | oct |
| **Tasks** | measurement |
| **Primary reported quantity** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | Not reported |
| **Source-stated terms** | CC BY-NC 3.0 |
| **Normalized terms** | `cc-by-nc` |
| **Descriptive screening label** | Explicit noncommercial clause recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Mendeley Data |
| **Availability** | `available` (checked 2026-08-02) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Reported quantities

No reproducible primary item count was exposed for the cataloged source version.

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Human provenance: Source describes de-identified conjunctival swab observations from ophthalmic patients. Source-review finding: One XLS workbook named De-Identified Conjswab Data.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mendeley_post_intravitreal_injection_ciprofloxacin_conjunctival_flora --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download mendeley_post_intravitreal_injection_ciprofloxacin_conjunctival_flora --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mendeley_post_intravitreal_injection_ciprofloxacin_conjunctival_flora')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/53nxz6xr5j/1)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/53nxz6xr5j)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{mendeley_post_intravitreal_injection_ciprofloxacin_conjunctival_flora,
  title  = { Data for: Post-Intravitreal Injection Ciprofloxacin and Conjunctival Flora Resistance },
  note   = { Data for: Post-Intravitreal Injection Ciprofloxacin and Conjunctival Flora Resistance. Mendeley Data, V1. doi:10.17632/53nxz6xr5j.1 },
  url    = { https://data.mendeley.com/datasets/53nxz6xr5j/1 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Data for: Post-Intravitreal Injection Ciprofloxacin and Conjunctival Flora Resistance. Mendeley Data, V1. doi:10.17632/53nxz6xr5j.1.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC BY-NC 3.0
- **Normalized category:** `cc-by-nc`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Explicit noncommercial clause recorded; check source

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [syn_oct](./syn_oct.md): SYN-OCT Synthetic Glaucoma OCT Dataset (200,000 images, `cc-by`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (103,959 images, `mit`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [kermany_oct](./kermany_oct.md): Kermany OCT 2018: Retinal OCT Image Classification (84,484 images, `cc-by`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [harvard_fairvision](./harvard_fairvision.md): Harvard-FairVision (AMD + DR + Glaucoma, paired SLO + OCT) (30,000 participants, `cc-by-nc-nd`)
- [mario](./mario.md): MARIO: AMD-Progression Longitudinal OCT (MICCAI 2024) (30,000 images, `cc-by`)
- [mmrdr](./mmrdr.md): MMRDR: Multi-Modal Retinal Diabetic Retinopathy Dataset (24,460 images, `cc-by`)
