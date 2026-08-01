---
id: hassan_composite_retina
title: "Composite Retinal Fundus and OCT Dataset with Clinical Markings"
sidebar_label: hassan_composite_retina
description: "Composite fundus and OCT dataset with retinal layer, retinal lesion, and macular/glaucomatous disorder markings."
tags: ["multimodal", "fundus", "oct", "cc-by", "mendeley", "segmentation", "classification", "grading", "documented-relationship", "relationship-derived_from"]
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
| **Primary reported quantity** | Not reported |
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


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Additional | 64 | `images` | Fundus component described by the associated publication The count was not confirmed as the exact content of the cataloged Mendeley v4 archive. | `associated_publication` | [https://doi.org/10.1016/B978-0-12-817438-8.00005-5](https://doi.org/10.1016/B978-0-12-817438-8.00005-5) |
| Additional | 2,497 | `b_scans` | OCT component described by the associated publication The count was not confirmed as the exact content of the cataloged Mendeley v4 archive. | `associated_publication` | [https://doi.org/10.1016/B978-0-12-817438-8.00005-5](https://doi.org/10.1016/B978-0-12-817438-8.00005-5) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Composite dataset; verify component provenance before treating as an independent cohort.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- [mm_retinal_reason](./mm_retinal_reason.md) is `derived from` this record: The version-pinned official dataset card lists this record among the CFP or OCT sources used to construct MM-Retinal-Reason. ([evidence](https://huggingface.co/datasets/lxirich/MM-Retinal-Reason/tree/d6243baa82c0914dba3c6f43ca79fdbf856982ef))
- [multieye](./multieye.md) is `derived from` this record: The MultiEYE paper names this record as one of the public fundus or OCT sources assembled for the benchmark. ([evidence](https://arxiv.org/abs/2412.09402))

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

## Similar resources by shared modality

- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (103,959 images, `mit`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [harvard_fairvision](./harvard_fairvision.md): Harvard-FairVision (AMD + DR + Glaucoma, paired SLO + OCT) (30,000 participants, `cc-by-nc-nd`)
- [mmrdr](./mmrdr.md): MMRDR: Multi-Modal Retinal Diabetic Retinopathy Dataset (24,460 images, `cc-by`)
- [x_pcr](./x_pcr.md): X-PCR Ophthalmology Progressive Clinical Reasoning Benchmark (18,735 rows, `unknown`)
- [olives](./olives.md): OLIVES: Ophthalmic Labels for Investigating Visual Eye Semantics (9,408 b scans, `cc-by`)
- [oct_fundus_dme_dr_mexico](./oct_fundus_dme_dr_mexico.md): OCT and Eye Fundus Dataset for DME and DR (2,661 images, `unknown`)
