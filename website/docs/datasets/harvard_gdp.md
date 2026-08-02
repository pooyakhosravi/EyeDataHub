---
id: harvard_gdp
title: "Harvard GDP: Glaucoma Detection and Progression Dataset"
sidebar_label: harvard_gdp
description: "1,000 patients with OCT RNFLT maps (225×225), visual field measurements, and demographics for glaucoma detection (binary) and longitudinal progression forecasting (6 definitions). First public glaucom"
tags: ["oct", "visual_field", "tabular", "cc-by-nc-nd", "gdrive", "classification", "progression", "documented-relationship", "relationship-derived_from"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Harvard GDP: Glaucoma Detection and Progression Dataset

1,000 patients with OCT RNFLT maps (225×225), visual field measurements, and demographics for glaucoma detection (binary) and longitudinal progression forecasting (6 definitions). First public glaucoma progression dataset from Harvard Ophthalmology AI Lab.

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `harvard_gdp` |
| **Full name** | Harvard GDP: Glaucoma Detection and Progression Dataset |
| **Primary category** | `oct` |
| **Contained modalities** | oct, visual_field, tabular |
| **Tasks** | classification, progression |
| **Primary reported quantity** | 1,000 participants |
| **Classes** | 2 (Non-Glaucoma, Glaucoma) |
| **Splits** | train, val, test |
| **Size** | 2.0 GB |
| **Source-stated terms** | CC BY-NC-ND 4.0 |
| **Normalized terms** | `cc-by-nc-nd` |
| **Descriptive screening label** | Explicit noncommercial clause recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Google Drive |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `guided_instructions_only` |
| **Legacy sample-loader status** | Standard loader included |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 1,000 | `participants` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [drive.google.com/drive](https://drive.google.com/drive/folders/1JMi_HCql113uc9X0DOaMkNfEWfxaDlEz) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Documented relationships

These links record source-supported lineage or overlap, not merely similar modality tags.

- [x_pcr](./x_pcr.md) is `derived from` this record: Source labels in the version-pinned public X-PCR deposit identify this catalog record as upstream material. ([evidence](https://huggingface.co/datasets/Fantasy666/X-PCR/tree/06a318fd852230326386e3c6514d8a11b7a6b4af))

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download harvard_gdp --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download harvard_gdp --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('harvard_gdp')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [drive.google.com/drive](https://drive.google.com/drive/folders/1JMi_HCql113uc9X0DOaMkNfEWfxaDlEz)

**Source-term evidence:** [drive.google.com/drive](https://drive.google.com/drive/folders/1JMi_HCql113uc9X0DOaMkNfEWfxaDlEz)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('harvard_gdp')
samples = ds.load(data_dir, split='test')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{harvard_gdp,
  title  = { Harvard GDP: Glaucoma Detection and Progression Dataset },
  note   = { Luo Z et al., 'Glaucoma Progression Prediction Using Retinal Thickness via Deep Learning', arXiv 2308.13411, 2023. https://github.com/Harvard-Ophthalmology-AI-Lab/Harvard-GDP },
  year   = { 2023 },
  url    = { https://drive.google.com/drive/folders/1JMi_HCql113uc9X0DOaMkNfEWfxaDlEz },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Luo Z et al., 'Glaucoma Progression Prediction Using Retinal Thickness via Deep Learning', arXiv 2308.13411, 2023. https://github.com/Harvard-Ophthalmology-AI-Lab/Harvard-GDP
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

- [grape](./grape.md): GRAPE: Glaucoma Real-world Appraisal Progression Ensemble (1,115 examinations, `cc0`)
- [lmod_plus](./lmod_plus.md): LMOD+ Multimodal Ophthalmology Benchmark (32,633 annotated instances, `unknown`)
- [fairvlmed](./fairvlmed.md): FairVLMed: Fair Vision-Language Medical Ophthalmic Dataset (10,000 images, `cc-by-nc-nd`)
- [olives](./olives.md): OLIVES: Ophthalmic Labels for Investigating Visual Eye Semantics (9,408 b scans, `cc-by`)
- [dryad_namd_oct_quant](./dryad_namd_oct_quant.md): Moorfields nAMD Quantitative OCT Biomarker Dataset (2,966 volumes, `cc0`)
- [dryad_namd_oct_longitudinal](./dryad_namd_oct_longitudinal.md): Quantifying changes on optical coherence tomography in eyes receiving treatment for neovascular age-related macular degeneration (2,115 eyes, `cc0`)
- [dryad_namd_visual_prediction](./dryad_namd_visual_prediction.md): Moorfields nAMD Visual-Change Prediction Dataset (926 eyes, `cc0`)
- [dryad_glaucoma_rnfl_vf](./dryad_glaucoma_rnfl_vf.md): RNFL and Visual-Field Glaucoma Diagnosis Dataset (499 records, `cc0`)
