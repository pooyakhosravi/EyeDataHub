---
id: hassan_composite_retina
title: "Composite Retinal Fundus and OCT Dataset with Clinical Markings"
sidebar_label: hassan_composite_retina
description: "Composite fundus and OCT dataset with retinal layer, retinal lesion, and macular/glaucomatous disorder markings."
tags: ["multimodal", "fundus", "oct", "cc-by", "mendeley", "segmentation", "classification", "grading"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Composite Retinal Fundus and OCT Dataset with Clinical Markings

Composite fundus and OCT dataset with retinal layer, retinal lesion, and macular/glaucomatous disorder markings.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `hassan_composite_retina` |
| **Full name** | Composite Retinal Fundus and OCT Dataset with Clinical Markings |
| **Primary category** | `multimodal` |
| **Contained modalities** | fundus, oct |
| **Tasks** | segmentation, classification, grading |
| **Samples** | Not reported |
| **Classes** | Not reported (Not reported) |
| **Splits** | all |
| **Size** | 2.0 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Mendeley Data |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Metadata and access only |


## Notes

> Composite dataset; verify component provenance before treating as an independent cohort.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download hassan_composite_retina --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download hassan_composite_retina --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('hassan_composite_retina')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/trghs22fpg/4)

**Source-term evidence:** [data.mendeley.com/datasets](https://data.mendeley.com/datasets/trghs22fpg/4)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{hassan_composite_retina,
  title  = { Composite Retinal Fundus and OCT Dataset with Clinical Markings },
  note   = { Hassan T, Akram MU, Nazir MN. A Composite Retinal Fundus and OCT Dataset with Detailed Clinical Markings. Mendeley Data, V4, 2021. doi:10.17632/trghs22fpg.4 },
  year   = { 2021 },
  url    = { https://data.mendeley.com/datasets/trghs22fpg/4 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Hassan T, Akram MU, Nazir MN. A Composite Retinal Fundus and OCT Dataset with Detailed Clinical Markings. Mendeley Data, V4, 2021. doi:10.17632/trghs22fpg.4
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
- [mmrdr](./mmrdr.md): MMRDR: Multi-Modal Retinal Diabetic Retinopathy Dataset (24,460 records, `cc-by`)
- [x_pcr](./x_pcr.md): X-PCR Ophthalmology Progressive Clinical Reasoning Benchmark (18,735 records, `unknown`)
- [olives](./olives.md): OLIVES: Ophthalmic Labels for Investigating Visual Eye Semantics (9,408 records, `cc-by`)
- [oct_fundus_dme_dr_mexico](./oct_fundus_dme_dr_mexico.md): OCT and Eye Fundus Dataset for DME and DR (2,661 records, `unknown`)
