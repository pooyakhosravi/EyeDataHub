---
id: jsiec
title: "JSIEC Fundus Photo Dataset"
sidebar_label: jsiec
description: "1,000 fundus images spanning 39 ophthalmic disease categories from the Joint Shantou International Eye Center. Used for multi-class fundus disease classification."
tags: ["fundus", "unknown", "zenodo", "classification"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# JSIEC Fundus Photo Dataset

1,000 fundus images spanning 39 ophthalmic disease categories from the Joint Shantou International Eye Center. Used for multi-class fundus disease classification.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `jsiec` |
| **Full name** | JSIEC Fundus Photo Dataset |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | classification |
| **Samples** | 1,000 |
| **Classes** | 39 (0.0.Normal, 0.1.Tessellated fundus, 0.2.Large optic cup, 0.3.DR1, 1.0.DR2, 1.1.DR3, 10.0.Possible glaucoma, 10.1.Optic atrophy, 11.Severe hypertensive retinopathy, 12.Disc swelling and elevation, 13.Dragged Disc, 14.Congenital disc abnormality, 15.0.Retinitis pigmentosa, 15.1.Bietti crystalline dystrophy, 16.Peripheral retinal degeneration and break, 17.Myelinated nerve fiber, 18.Vitreous particles, 19.Fundus neoplasm, 2.0.BRVO, 2.1.CRVO, 20.Massive hard exudates, 21.Yellow-white spots-flecks, 22.Cotton-wool spots, 23.Vessel tortuosity, 24.Chorioretinal atrophy-coloboma, 25.Preretinal hemorrhage, 26.Fibrosis, 27.Laser Spots, 28.Silicon oil in eye, 29.0.Blur fundus without PDR, 29.1.Blur fundus with suspected PDR, 3.RAO, 4.Rhegmatogenous RD, 5.0.CSCR, 5.1.VKH disease, 6.Maculopathy, 7.ERM, 8.MH, 9.Pathological myopia) |
| **Splits** | all |
| **Size** | 0.4 GB |
| **Source-stated terms** | Other open access (Zenodo; no standard license identifier) |
| **Normalized terms** | `unknown` |
| **Descriptive screening label** | Unknown or unclear; do not assume permission |
| **Terms scope** | `unknown` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Zenodo |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `transfer_tested_partial` |
| **Legacy sample-loader status** | Standard loader included |


## Notes

> Zenodo labels the deposit as other open access but does not name a standard reuse license. Verify terms before redistribution.

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download jsiec --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download jsiec --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('jsiec')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [zenodo.org/record](https://zenodo.org/record/3477553)

**Source-term evidence:** [zenodo.org/record](https://zenodo.org/record/3477553)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('jsiec')
samples = ds.load(data_dir, split='all')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{jsiec,
  title  = { JSIEC Fundus Photo Dataset },
  note   = { Cen et al., 'Automatic detection of 39 fundus diseases and conditions in retinal photographs using deep neural networks', Nature Communications 2021. doi:10.1038/s41467-021-25138-w. Data: doi:10.5281/zenodo.3477553 },
  year   = { 2021 },
  url    = { https://zenodo.org/record/3477553 },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Cen et al., 'Automatic detection of 39 fundus diseases and conditions in retinal photographs using deep neural networks', Nature Communications 2021. doi:10.1038/s41467-021-25138-w. Data: doi:10.5281/zenodo.3477553
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Other open access (Zenodo; no standard license identifier)
- **Normalized category:** `unknown`
- **Apparent scope:** `unknown`
- **Descriptive screening label:** Unknown or unclear; do not assume permission

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Related datasets with shared modalities

- [airogs](./airogs.md): AIROGS: AI for Robust Glaucoma Screening (113,893 records, `cc-by-nc-nd`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 records, `unknown`)
- [justraigs](./justraigs.md): JustRAIGS: Just Referral AI Glaucoma Screening Dataset (101,442 records, `cc-by-nc-nd`)
- [eyepacs](./eyepacs.md): EyePACS — Diabetic Retinopathy Detection (Kaggle 2015) (88,702 records, `research-only`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (58,036 records, `mit`)
- [angioreport](./angioreport.md): AngioReport Fundus Angiography Report Dataset (55,361 records, `unknown`)
- [ffa_ir](./ffa_ir.md): FFA-IR Medical Report Dataset (47,247 records, `unknown`)
- [bidr](./bidr.md): BiDR: Diabetic Retinopathy Diagnosis Dataset (35,126 records, `unknown`)
