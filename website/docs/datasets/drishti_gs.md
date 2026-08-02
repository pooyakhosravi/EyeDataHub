---
id: drishti_gs
title: "DRISHTI-GS: Optic Disc and Cup Segmentation"
sidebar_label: drishti_gs
description: "101 fundus images annotated for optic disc and cup segmentation by 4 clinicians. Train/test: 50/51."
tags: ["fundus", "research-only", "kaggle", "segmentation", "documented-relationship", "relationship-derived_from"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# DRISHTI-GS: Optic Disc and Cup Segmentation

101 fundus images annotated for optic disc and cup segmentation by 4 clinicians. Train/test: 50/51.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `drishti_gs` |
| **Full name** | DRISHTI-GS: Optic Disc and Cup Segmentation |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | segmentation |
| **Primary reported quantity** | 101 images |
| **Classes** | Not reported (Not reported) |
| **Splits** | train, test |
| **Size** | 0.8 GB |
| **Source-stated terms** | Research only |
| **Normalized terms** | `research-only` |
| **Descriptive screening label** | Research or challenge restriction recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `self_service_authenticated` |
| **Route backend** | Kaggle |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `standard_platform_supported` |
| **Legacy sample-loader status** | Standard loader included |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 101 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [kaggle.com/datasets](https://www.kaggle.com/datasets/lokeshsaipureddi/drishtigs-retina-dataset-for-onh-segmentation) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- [fundus_domain_generalization](./fundus_domain_generalization.md) is `derived from` this record: The official description states that the benchmark is based on REFUGE, Drishti-GS, ORIGA, and RIGA. ([evidence](https://zenodo.org/records/8009107))
- [higancnn_generated_glaucoma](./higancnn_generated_glaucoma.md) is `derived from` this record: The official dataset description names ACRIMA, DRISHTI-GS, and HRF among the human fundus sources used to construct the synthetic glaucoma resource. ([evidence](https://www.kaggle.com/datasets/hindsaud/datasets-higancnn-glaucoma-detection))
- [mendeley_utilizing_responsive_web_portal_studying_disc](./mendeley_utilizing_responsive_web_portal_studying_disc.md) is `derived from` this record: The Mendeley deposit is a distinct annotation and task layer built from DRISHTI-GS fundus images. ([evidence](https://data.mendeley.com/datasets/7xv5rzxgrh))
- [mm_retinal_reason](./mm_retinal_reason.md) is `derived from` this record: The version-pinned official dataset card lists this record among the CFP or OCT sources used to construct MM-Retinal-Reason. ([evidence](https://huggingface.co/datasets/lxirich/MM-Retinal-Reason/tree/d6243baa82c0914dba3c6f43ca79fdbf856982ef))
- [smdg](./smdg.md) is `derived from` this record: The official SMDG source table lists this catalog record among the 19 standardized source domains. ([evidence](https://www.kaggle.com/datasets/deathtrooper/multichannel-glaucoma-benchmark-dataset))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download drishti_gs --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download drishti_gs --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('drishti_gs')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [kaggle.com/datasets](https://www.kaggle.com/datasets/lokeshsaipureddi/drishtigs-retina-dataset-for-onh-segmentation)

**Source-term evidence:** [kaggle.com/datasets](https://www.kaggle.com/datasets/lokeshsaipureddi/drishtigs-retina-dataset-for-onh-segmentation)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('drishti_gs')
samples = ds.load(data_dir, split='test')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{drishti_gs,
  title  = { DRISHTI-GS: Optic Disc and Cup Segmentation },
  note   = { Sivaswamy et al., 'Drishti-GS: Retinal image dataset for optic nerve head (ONH) segmentation', ISBI 2014 },
  year   = { 2014 },
  url    = { https://www.kaggle.com/datasets/lokeshsaipureddi/drishtigs-retina-dataset-for-onh-segmentation },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Sivaswamy et al., 'Drishti-GS: Retinal image dataset for optic nerve head (ONH) segmentation', ISBI 2014.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Research only
- **Normalized category:** `research-only`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Research or challenge restriction recorded; check source

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
