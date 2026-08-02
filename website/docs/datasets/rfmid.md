---
id: rfmid
title: "RFMiD: Retinal Fundus Multi-disease Image Dataset"
sidebar_label: rfmid
description: "3200 fundus images annotated for 45 retinal conditions. Used for multi-label disease classification."
tags: ["fundus", "cc-by-sa", "kaggle", "multilabel", "classification", "documented-relationship", "relationship-derived_from", "relationship-extension_of"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# RFMiD: Retinal Fundus Multi-disease Image Dataset

3200 fundus images annotated for 45 retinal conditions. Used for multi-label disease classification.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `rfmid` |
| **Full name** | RFMiD: Retinal Fundus Multi-disease Image Dataset |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | multilabel, classification |
| **Primary reported quantity** | 3,200 images |
| **Classes** | 29 (Disease_Risk, DR, ARMD, MH, DN, MYA, BRVO, TSLN, ERM, LS, MS, CSR, ODC, CRVO, TV, AH, ODP, ODE, ST, AION, PT, RT, RS, CRS, EDN, RPEC, MHL, RP, other) |
| **Splits** | train, val, test |
| **Size** | 1.5 GB |
| **Source-stated terms** | CC BY-SA 4.0 |
| **Normalized terms** | `cc-by-sa` |
| **Descriptive screening label** | Standard label without an explicit NC clause; not a permission finding |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Kaggle |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Standard loader included |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 3,200 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [kaggle.com/datasets](https://www.kaggle.com/datasets/andrewmvd/retinal-disease-classification) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- [amdnet23](./amdnet23.md) is `derived from` this record: AMDNet23 compiles preprocessed images from ODIR, RFMiD, HRF, ARIA, DR_200, and Fundus Dataset. ([evidence](https://doi.org/10.17632/yj35kjgrv3.1))
- [mm_retinal_reason](./mm_retinal_reason.md) is `derived from` this record: The version-pinned official dataset card lists this record among the CFP or OCT sources used to construct MM-Retinal-Reason. ([evidence](https://huggingface.co/datasets/lxirich/MM-Retinal-Reason/tree/d6243baa82c0914dba3c6f43ca79fdbf856982ef))
- [multieye](./multieye.md) is `derived from` this record: The MultiEYE paper names this record as one of the public fundus or OCT sources assembled for the benchmark. ([evidence](https://arxiv.org/abs/2412.09402))
- [mured](./mured.md) is `derived from` this record: The MuReD description identifies STARE, RFMiD, and ARIA as image sources and applies post-processing. ([evidence](https://doi.org/10.17632/pc4mb3h8hz.1))
- [rao_fundus](./rao_fundus.md) is `derived from` this record: The RAO source reports use of public web images plus RFMiD and JSIEC images. ([evidence](https://doi.org/10.17632/5428684j44.2))
- [rfmid2](./rfmid2.md) is `extension of` this record: RFMiD 2.0 is described as an auxiliary dataset to the earlier RFMiD release, not as the same image cohort. ([evidence](https://zenodo.org/records/7505822))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download rfmid --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download rfmid --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('rfmid')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [kaggle.com/datasets](https://www.kaggle.com/datasets/andrewmvd/retinal-disease-classification)

**Source-term evidence:** [kaggle.com/datasets](https://www.kaggle.com/datasets/andrewmvd/retinal-disease-classification)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('rfmid')
samples = ds.load(data_dir, split='test')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{rfmid,
  title  = { RFMiD: Retinal Fundus Multi-disease Image Dataset },
  note   = { Pachade et al., 'Retinal Fundus Multi-disease Image Dataset (RFMiD): A Dataset for Multi-Disease Detection Research', Data 2021 },
  year   = { 2021 },
  url    = { https://www.kaggle.com/datasets/andrewmvd/retinal-disease-classification },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Pachade et al., 'Retinal Fundus Multi-disease Image Dataset (RFMiD): A Dataset for Multi-Disease Detection Research', Data 2021.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** CC BY-SA 4.0
- **Normalized category:** `cc-by-sa`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Standard label without an explicit NC clause; not a permission finding

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [airogs](./airogs.md): AIROGS: AI for Robust Glaucoma Screening (113,893 images, `cc-by-nc-nd`)
- [multieye](./multieye.md): MultiEYE: OCT-Enhanced Fundus Multi-Disease Benchmark (103,959 images, `mit`)
- [eyecare_100k](./eyecare_100k.md): Eyecare-100K: Multimodal Ophthalmology VQA Corpus (102,000 question answer pairs, `unknown`)
- [justraigs](./justraigs.md): JustRAIGS: Just Referral AI Glaucoma Screening Dataset (101,442 images, `cc-by-nc-nd`)
- [eyepacs](./eyepacs.md): EyePACS — Diabetic Retinopathy Detection (Kaggle 2015) (88,702 images, `research-only`)
- [angioreport](./angioreport.md): AngioReport Fundus Angiography Report Dataset (55,361 images, `unknown`)
- [ffa_ir](./ffa_ir.md): FFA-IR Medical Report Dataset (47,247 images, `unknown`)
- [bidr](./bidr.md): BiDR: Diabetic Retinopathy Diagnosis Dataset (35,126 images, `unknown`)
