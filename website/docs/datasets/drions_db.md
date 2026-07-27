---
id: drions_db
title: "DRIONS-DB: Digital Retinal Images for Optic Nerve Segmentation"
sidebar_label: drions_db
description: "110 color fundus images with optic-disc contour annotations by two experts. Foundational OD-segmentation dataset."
tags: ["fundus", "research-only", "direct", "segmentation"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# DRIONS-DB: Digital Retinal Images for Optic Nerve Segmentation

110 color fundus images with optic-disc contour annotations by two experts. Foundational OD-segmentation dataset.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `drions_db` |
| **Full name** | DRIONS-DB: Digital Retinal Images for Optic Nerve Segmentation |
| **Primary category** | `fundus` |
| **Contained modalities** | fundus |
| **Tasks** | segmentation |
| **Samples** | 110 |
| **Classes** | 2 (background, optic_disc) |
| **Splits** | all |
| **Size** | 0.2 GB |
| **Source-stated terms** | Research only (UNED public release) |
| **Normalized terms** | `research-only` |
| **Descriptive screening label** | Research or challenge restriction recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Direct HTTP |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `loader_implemented_not_live_tested` |
| **Legacy sample-loader status** | Metadata and access only |


## Notes

> UNED host serves an expired SSL certificate as of 2026-07. EyeDataHub falls back to an unverified HTTPS request; set PYTHONHTTPSVERIFY=0 in your environment if requests still fails cert validation. Distributed as .rar — needs `unrar` (Linux: `apt install unrar`; macOS: `brew install rar`; Windows: 7-Zip).

## Access preflight and acquisition

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download drions_db --data-dir ./data --dry-run --json

# Explicit transfer, only when preflight reports supported behavior
eyehub download drions_db --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('drions_db')
print(preflight_dataset(ds, './data'))  # no transfer
```

  </TabItem>
</Tabs>

**Upstream page:** [ia.uned.es/~ejcarmona](https://www.ia.uned.es/~ejcarmona/DRIONS-DB.html)

**Source-term evidence:** [ia.uned.es/~ejcarmona](https://www.ia.uned.es/~ejcarmona/DRIONS-DB.html)

## Loader status

This catalog record provides metadata and access instructions, but it does not yet include a standard `DatasetSample` loader. Inspect the source file structure or contribute a loader before using it in a training pipeline.

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{drions_db,
  title  = { DRIONS-DB: Digital Retinal Images for Optic Nerve Segmentation },
  note   = { Carmona et al., 'Identification of the Optic Nerve Head with Genetic Algorithms', Artificial Intelligence in Medicine 2008 },
  year   = { 2008 },
  url    = { https://www.ia.uned.es/~ejcarmona/DRIONS-DB.html },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Carmona et al., 'Identification of the Optic Nerve Head with Genetic Algorithms', Artificial Intelligence in Medicine 2008.
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Research only (UNED public release)
- **Normalized category:** `research-only`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Research or challenge restriction recorded; check source

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
