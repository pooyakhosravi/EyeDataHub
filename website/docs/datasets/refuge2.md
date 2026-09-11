---
id: refuge2
title: "REFUGE2 — Retinal Fundus Glaucoma Challenge 2"
sidebar_label: refuge2
description: "2000 fundus images for glaucoma classification, optic disc/cup segmentation, and fovea localisation. Extends REFUGE1."
tags: ["fundus", "research-only", "gdrive", "classification", "segmentation", "resource-role-current-dataset", "dataset-family-refuge2", "documented-relationship", "relationship-derived_from", "alternate-source", "source-grand_challenge", "source-kaggle", "alternate-role-previous-version", "alternate-role-mirror"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# REFUGE2 — Retinal Fundus Glaucoma Challenge 2

2000 fundus images for glaucoma classification, optic disc/cup segmentation, and fovea localisation. Extends REFUGE1.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `refuge2` |
| **Full name** | REFUGE2 — Retinal Fundus Glaucoma Challenge 2 |
| **First published** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Primary category** | `fundus` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `refuge2` |
| **Contained modalities** | fundus |
| **Tasks** | classification, segmentation |
| **Primary reported quantity** | 2,000 images |
| **Classes** | 2 (non-glaucoma, glaucoma) |
| **Splits** | train, val, test |
| **Size** | 1.2 GB |
| **Source-stated terms** | Research use (Grand Challenge) |
| **Normalized terms** | `research-only` |
| **Descriptive screening label** | Research or challenge restriction recorded; check source |
| **Terms scope** | `challenge_participation` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Google Drive |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `loader_implemented_not_live_tested` |
| **Legacy sample-loader status** | Standard loader included |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 2,000 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [drive.google.com/file](https://drive.google.com/file/d/1DspRzDqypeBOxZnWPQxmXprNVmJwkBRJ/view) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Notes

> Current release containing all 1,200 REFUGE 2018 images plus 800 additional images. REFUGE 2018 is retained as version history below and is not counted separately.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- [fundus_domain_generalization](./fundus_domain_generalization.md) is `derived from` this record: The official description states that the benchmark is based on the original REFUGE images, now represented by the current REFUGE2 record, plus Drishti-GS, ORIGA, and RIGA. ([evidence](https://zenodo.org/records/8009107))
- [lmod_plus](./lmod_plus.md) is `derived from` this record: The LMOD+ project page lists nine component datasets, including the five cataloged targets represented by these edges. ([evidence](https://kfzyqin.github.io/lmod_plus/))
- [mm_retinal_reason](./mm_retinal_reason.md) is `derived from` this record: The version-pinned official dataset card lists this record among the CFP or OCT sources used to construct MM-Retinal-Reason. ([evidence](https://huggingface.co/datasets/lxirich/MM-Retinal-Reason/tree/d6243baa82c0914dba3c6f43ca79fdbf856982ef))
- [refuge1_multirater](./refuge1_multirater.md) is `derived from` this record: The source provides seven-rater annotations for the 1,200 original REFUGE images incorporated into the current REFUGE2 release. ([evidence](https://huggingface.co/datasets/realslimman/REFUGE-MultiRater))
- [smdg](./smdg.md) is `derived from` this record: The official SMDG source table lists this catalog record among the 19 standardized source domains. ([evidence](https://www.kaggle.com/datasets/deathtrooper/multichannel-glaucoma-benchmark-dataset))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download refuge2 --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download refuge2 --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('refuge2')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [drive.google.com/file](https://drive.google.com/file/d/1DspRzDqypeBOxZnWPQxmXprNVmJwkBRJ/view)

## Other documented locations

These links identify alternate deposits, components, metadata records, mirrors, versions, or related derived materials. They do not create additional canonical catalog records.

- [grand_challenge: previous version (REFUGE-2018, version 2018)](https://refuge.grand-challenge.org/): Earlier 1,200-image release incorporated into REFUGE2; not counted as a separate current catalog record.
- [kaggle: mirror (victorlemosml/refuge2)](https://www.kaggle.com/datasets/victorlemosml/refuge2): Non-authoritative mirror of the current REFUGE2 release.

**Source-term evidence:** [drive.google.com/file](https://drive.google.com/file/d/1DspRzDqypeBOxZnWPQxmXprNVmJwkBRJ/view)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('refuge2')
samples = ds.load(data_dir, split='test')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{refuge2,
  title  = { REFUGE2 — Retinal Fundus Glaucoma Challenge 2 },
  note   = { Fang H. et al., 'REFUGE2 Challenge: Treasure for Multi-Domain Learning in Glaucoma Assessment', MIA 2022 },
  year   = { 2022 },
  url    = { https://drive.google.com/file/d/1DspRzDqypeBOxZnWPQxmXprNVmJwkBRJ/view },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Fang H. et al., 'REFUGE2 Challenge: Treasure for Multi-Domain Learning in Glaucoma Assessment', MIA 2022.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Research use (Grand Challenge)
- **Normalized category:** `research-only`
- **Apparent scope:** `challenge_participation`
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
- [mfiddr](./mfiddr.md): MFIDDR: Multi-Field Imaging Dataset for Diabetic Retinopathy (34,452 images, `mit`)
