---
id: mmrdr
title: "MMRDR: Multi-Modal Retinal Diabetic Retinopathy Dataset"
sidebar_label: mmrdr
description: "Multi-modal DR dataset combining color fundus photographs (CFP), OCT B-scans, and ultra-widefield (UWF) fundus images, annotated for DR detection and severity grading. Published in Nature Scientific D"
tags: ["multimodal", "fundus", "oct", "uwf_fundus", "cc-by", "figshare", "grading", "classification", "resource-role-derivative-dataset", "dataset-family-mmrdr", "documented-relationship", "relationship-derived_from"]
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
| **First published** | 2025-06-30 |
| **Publication date precision** | day |
| **Publication date evidence** | [api.figshare.com/v2](https://api.figshare.com/v2/articles/29423747/versions/1) |
| **Publication date source field** | published_date (Figshare version 1) |
| **Publication date reviewed** | 2026-09-11 |
| **Primary category** | `multimodal` |
| **Resource role** | `derivative_dataset` |
| **Dataset family** | `mmrdr` |
| **Contained modalities** | fundus, oct, uwf_fundus |
| **Tasks** | grading, classification |
| **Primary reported quantity** | 24,460 images |
| **Classes** | 5 (No DR, Mild DR, Moderate DR, Severe DR, Proliferative DR) |
| **Splits** | train, test |
| **Size** | 18.61 GB |
| **Source-stated terms** | CC BY 4.0 |
| **Normalized terms** | `cc-by` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Figshare |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `end_to_end_tested` |
| **Legacy sample-loader status** | Standard loader included |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 24,460 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [https://doi.org/10.6084/m9.figshare.29423747](https://doi.org/10.6084/m9.figshare.29423747) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Contains 24,460 images across CFP, OCT, and UWF modalities. The CFP component is derived from OIA-DDR; OCT and UWF components are independently collected QEH cohorts. The source-reported unit is images rather than unique patients. Evaluation code: https://github.com/Vladimirovich2019/MMRDR_Evaluation

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- This record is `derived from` [ddr](./ddr.md): The MMRDR Data Descriptor identifies OIA-DDR as the source of its CFP images; MMRDR also adds independently collected OCT and UWF cohorts and new annotations. ([evidence](https://doi.org/10.1038/s41597-026-07005-9))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download mmrdr --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download mmrdr --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('mmrdr')
print(preflight_dataset(ds, './data'))  # no download
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

## Similar resources by shared modality

- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (103,959 images, `mit`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [harvard_fairvision](./harvard_fairvision.md): Harvard-FairVision (AMD + DR + Glaucoma, paired SLO + OCT) (30,000 participants, `cc-by-nc-nd`)
- [x_pcr](./x_pcr.md): X-PCR Ophthalmology Progressive Clinical Reasoning Benchmark (18,735 rows, `unknown`)
- [olives](./olives.md): OLIVES: Ophthalmic Labels for Investigating Visual Eye Semantics (9,408 b scans, `cc-by`)
- [oct_fundus_dme_dr_mexico](./oct_fundus_dme_dr_mexico.md): OCT and Eye Fundus Dataset for DME and DR (2,661 images, `unknown`)
- [deepdrid](./deepdrid.md): DeepDRiD: Diabetic Retinopathy Grading and Image Quality Dataset (2,256 images, `cc-by-sa`)
