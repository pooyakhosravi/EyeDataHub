---
id: airogs
title: "AIROGS: AI for Robust Glaucoma Screening"
sidebar_label: airogs
description: "~113,893 color fundus images labelled as referable glaucoma (RG), no referable glaucoma (NRG), or ungradable. Large-scale, multi-ethnic, multi-site screening dataset."
tags: ["fundus", "cc-by-nc-nd", "direct", "classification", "documented-relationship", "relationship-derived_from"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# AIROGS: AI for Robust Glaucoma Screening

~113,893 color fundus images labelled as referable glaucoma (RG), no referable glaucoma (NRG), or ungradable. Large-scale, multi-ethnic, multi-site screening dataset.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `airogs` |
| **Full name** | AIROGS: AI for Robust Glaucoma Screening |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | classification |
| **Primary reported quantity** | 113,893 images |
| **Classes** | 2 (NRG, RG) |
| **Splits** | train, test |
| **Size** | 40.0 GB |
| **Source-stated terms** | CC BY-NC-ND 4.0 |
| **Normalized terms** | `cc-by-nc-nd` |
| **Descriptive screening label** | Explicit noncommercial clause recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Direct HTTP |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `guided_instructions_only` |
| **Legacy sample-loader status** | Standard loader included |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 113,893 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [zenodo.org/records](https://zenodo.org/records/5793241) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Training set (~101k images) on Zenodo. Test set distributed through Grand Challenge. Requires free account for Grand Challenge.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- [smdg](./smdg.md) is `derived from` this record: The official SMDG source table lists this catalog record among the 19 standardized source domains. ([evidence](https://www.kaggle.com/datasets/deathtrooper/multichannel-glaucoma-benchmark-dataset))

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download airogs --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download airogs --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('airogs')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [zenodo.org/records](https://zenodo.org/records/5793241)

**Source-term evidence:** [zenodo.org/records](https://zenodo.org/records/5793241)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('airogs')
samples = ds.load(data_dir, split='test')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{airogs,
  title  = { AIROGS: AI for Robust Glaucoma Screening },
  note   = { De Vente et al., 'AIROGS: Artificial Intelligence for Robust Glaucoma Screening Challenge', TMI 2023 },
  year   = { 2023 },
  url    = { https://zenodo.org/records/5793241 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
De Vente et al., 'AIROGS: Artificial Intelligence for Robust Glaucoma Screening Challenge', TMI 2023.
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
- [justraigs](./justraigs.md): JustRAIGS: Just Referral AI Glaucoma Screening Dataset (101,442 images, `cc-by-nc-nd`)
- [eyepacs](./eyepacs.md): EyePACS — Diabetic Retinopathy Detection (Kaggle 2015) (88,702 images, `research-only`)
- [angioreport](./angioreport.md): AngioReport Fundus Angiography Report Dataset (55,361 images, `unknown`)
- [ffa_ir](./ffa_ir.md): FFA-IR Medical Report Dataset (47,247 images, `unknown`)
- [bidr](./bidr.md): BiDR: Diabetic Retinopathy Diagnosis Dataset (35,126 images, `unknown`)
- [dr_arranged](./dr_arranged.md): Diabetic Retinopathy Arranged Dataset (Tianchi 93926) (35,126 images, `cc-by-nc-sa`)
