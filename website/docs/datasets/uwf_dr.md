---
id: uwf_dr
title: "UWF DR Reasoning Dataset"
sidebar_label: uwf_dr
description: "Ultra-widefield fundus photographs for diabetic retinopathy grading (5-level ICDR scale). Released alongside the Reasoning-Enhanced VLM paper for interpretable UWF DR detection. Related to the UWF4DR "
tags: ["uwf_fundus", "research-only", "gdrive", "grading", "classification", "resource-role-current-dataset", "dataset-family-uwf-dr"]
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# UWF DR Reasoning Dataset

Ultra-widefield fundus photographs for diabetic retinopathy grading (5-level ICDR scale). Released alongside the Reasoning-Enhanced VLM paper for interpretable UWF DR detection. Related to the UWF4DR 2024 MICCAI challenge (~495 images across image quality and DR grading tasks).

## At a glance

| Field | Value |
| --- | --- |
| **Short name** | `uwf_dr` |
| **Full name** | UWF DR Reasoning Dataset |
| **Publication date** | Unknown |
| **Date basis** | Unknown |
| **Publication date precision** | Unknown |
| **Publication date evidence** | Unknown |
| **Publication date source field** | Unknown |
| **Publication date reviewed** | Unknown |
| **Date notes** | - |
| **Primary category** | `uwf_fundus` |
| **Resource role** | `current_dataset` |
| **Dataset family** | `uwf_dr` |
| **Contained modalities** | uwf_fundus |
| **Tasks** | grading, classification |
| **Primary reported quantity** | 495 images |
| **Classes** | 5 (No DR, Mild DR, Moderate DR, Severe DR, Proliferative DR) |
| **Splits** | train, val, test |
| **Size** | 2.0 GB |
| **Source-stated terms** | Research only — see paper terms |
| **Normalized terms** | `research-only` |
| **Descriptive screening label** | Research or challenge restriction recorded; check source |
| **Terms scope** | `dataset_files` |
| **Access friction** | `anonymous_direct` |
| **Route backend** | Google Drive |
| **Availability** | `available` (checked 2026-07-21) |
| **Acquisition support** | `guided_instructions_only` |
| **Legacy sample-loader status** | Standard loader included |


## Reported quantities

| Role | Count | Unit | Scope | Basis | Evidence |
| --- | ---: | --- | --- | --- | --- |
| Primary | 495 | `images` | Primary quantity reported in the reviewed catalog source | `legacy_catalog_field` | [drive.google.com/drive](https://drive.google.com/drive/folders/1wOqM-O_amSwMdli4OlFnGpf4hslPgDNu) |

Counts retain their source-reported units. Additional rows can describe components, paired items, or derivative copies and are not automatically added to the primary quantity.

## Access information and download

<Tabs>
  <TabItem value="cli" label="CLI" default>

```bash
# Read-only preflight
eyehub download uwf_dr --data-dir ./data --dry-run --json

# Download, only when preflight reports supported behavior
eyehub download uwf_dr --data-dir ./data
```

  </TabItem>
  <TabItem value="python" label="Python">

```python
from eyedatahub.acquisition import preflight_dataset
from eyedatahub.datasets.registry import REGISTRY

ds = REGISTRY.get_dataset('uwf_dr')
print(preflight_dataset(ds, './data'))  # no download
```

  </TabItem>
</Tabs>

**Upstream page:** [drive.google.com/drive](https://drive.google.com/drive/folders/1wOqM-O_amSwMdli4OlFnGpf4hslPgDNu)

**Source-term evidence:** [drive.google.com/drive](https://drive.google.com/drive/folders/1wOqM-O_amSwMdli4OlFnGpf4hslPgDNu)

## Loader example

This entry includes a standard `DatasetSample` loader.

```python
from pathlib import Path
from eyedatahub.datasets.registry import REGISTRY

data_dir = Path('~/.eyedatahub/data').expanduser()
ds = REGISTRY.get_dataset('uwf_dr')
samples = ds.load(data_dir, split='test')
for s in samples[:5]:
    print(s.sample_id, s.label, s.image_path)
```

## Citation

<Tabs>
  <TabItem value="bibtex" label="BibTeX" default>

```bibtex
@misc{uwf_dr,
  title  = { UWF DR Reasoning Dataset },
  note   = { Reasoning-Enhanced Vision-Language Model for Interpretable Diabetic Retinopathy Detection in Ultra-Wide-Field Fundus Images. OMIA 2025 (MICCAI Workshop), Springer. DOI: 10.1007/978-3-032-10351-2_12 },
  year   = { 2025 },
  url    = { https://drive.google.com/drive/folders/1wOqM-O_amSwMdli4OlFnGpf4hslPgDNu },
}
```

  </TabItem>
  <TabItem value="apa" label="Plain text">

```text
Reasoning-Enhanced Vision-Language Model for Interpretable Diabetic Retinopathy Detection in Ultra-Wide-Field Fundus Images. OMIA 2025 (MICCAI Workshop), Springer. DOI: 10.1007/978-3-032-10351-2_12
```

  </TabItem>
</Tabs>

## Source-stated terms

- **Raw source string:** Research only — see paper terms
- **Normalized category:** `research-only`
- **Apparent scope:** `dataset_files`
- **Descriptive screening label:** Research or challenge restriction recorded; check source

> :warning: Source-stated terms, scope, and normalized labels are curation metadata, not legal advice or a permission finding. Review the current official source before transfer or reuse.

## Similar resources by shared modality

- [mmrdr](./mmrdr.md): MMRDR: Multi-Modal Retinal Diabetic Retinopathy Dataset (24,460 images, `cc-by`)
- [oculoscope](./oculoscope.md): OculoScope: Fairer AI in Ophthalmology Dataset (16,530 images, `cc-by`)
- [tsukazaki_uwf](./tsukazaki_uwf.md): Tsukazaki Hospital UWF Fundus Dataset (13,047 images, `research-only`)
- [birdshot_wide](./birdshot_wide.md): Birdshot-WIDE Widefield Fundus Dataset (6,352 images, `cc-by`)
- [deepdrid](./deepdrid.md): DeepDRiD: Diabetic Retinopathy Grading and Image Quality Dataset (2,256 images, `cc-by-sa`)
- [uwf_tumor](./uwf_tumor.md): UWF Fundus Intraocular Tumor Dataset (2,031 images, `cc-by`)
- [uwf_dr_peng](./uwf_dr_peng.md): UWF Fundus DR Dataset (Peng et al., 2026) (1,630 images, `cc-by`)
- [uwf_zhejiang](./uwf_zhejiang.md): Open UWF Fundus Dataset with Disease + Quality Labels (700 images, `cc-by`)
